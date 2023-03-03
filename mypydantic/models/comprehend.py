# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AugmentedManifestsListItemModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    attribute_names: Sequence[str] = Field(alias="AttributeNames")
    split: Optional[Literal["TEST", "TRAIN"]] = Field(default=None, alias="Split")
    annotation_data_s3_uri: Optional[str] = Field(
        default=None, alias="AnnotationDataS3Uri"
    )
    source_documents_s3_uri: Optional[str] = Field(
        default=None, alias="SourceDocumentsS3Uri"
    )
    document_type: Optional[
        Literal["PLAIN_TEXT_DOCUMENT", "SEMI_STRUCTURED_DOCUMENT"]
    ] = Field(default=None, alias="DocumentType")


class DominantLanguageModel(BaseModel):
    language_code: Optional[str] = Field(default=None, alias="LanguageCode")
    score: Optional[float] = Field(default=None, alias="Score")


class BatchDetectDominantLanguageRequestModel(BaseModel):
    text_list: Sequence[str] = Field(alias="TextList")


class BatchItemErrorModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchDetectEntitiesRequestModel(BaseModel):
    text_list: Sequence[str] = Field(alias="TextList")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class KeyPhraseModel(BaseModel):
    score: Optional[float] = Field(default=None, alias="Score")
    text: Optional[str] = Field(default=None, alias="Text")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")


class BatchDetectKeyPhrasesRequestModel(BaseModel):
    text_list: Sequence[str] = Field(alias="TextList")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class SentimentScoreModel(BaseModel):
    positive: Optional[float] = Field(default=None, alias="Positive")
    negative: Optional[float] = Field(default=None, alias="Negative")
    neutral: Optional[float] = Field(default=None, alias="Neutral")
    mixed: Optional[float] = Field(default=None, alias="Mixed")


class BatchDetectSentimentRequestModel(BaseModel):
    text_list: Sequence[str] = Field(alias="TextList")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class BatchDetectSyntaxRequestModel(BaseModel):
    text_list: Sequence[str] = Field(alias="TextList")
    language_code: Literal["de", "en", "es", "fr", "it", "pt"] = Field(
        alias="LanguageCode"
    )


class BatchDetectTargetedSentimentRequestModel(BaseModel):
    text_list: Sequence[str] = Field(alias="TextList")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class ChildBlockModel(BaseModel):
    child_block_id: Optional[str] = Field(default=None, alias="ChildBlockId")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")


class RelationshipsListItemModel(BaseModel):
    ids: Optional[List[str]] = Field(default=None, alias="Ids")
    type: Optional[Literal["CHILD"]] = Field(default=None, alias="Type")


class BoundingBoxModel(BaseModel):
    height: Optional[float] = Field(default=None, alias="Height")
    left: Optional[float] = Field(default=None, alias="Left")
    top: Optional[float] = Field(default=None, alias="Top")
    width: Optional[float] = Field(default=None, alias="Width")


class ClassifierEvaluationMetricsModel(BaseModel):
    accuracy: Optional[float] = Field(default=None, alias="Accuracy")
    precision: Optional[float] = Field(default=None, alias="Precision")
    recall: Optional[float] = Field(default=None, alias="Recall")
    f1_score: Optional[float] = Field(default=None, alias="F1Score")
    micro_precision: Optional[float] = Field(default=None, alias="MicroPrecision")
    micro_recall: Optional[float] = Field(default=None, alias="MicroRecall")
    micro_f1_score: Optional[float] = Field(default=None, alias="MicroF1Score")
    hamming_loss: Optional[float] = Field(default=None, alias="HammingLoss")


class DocumentReaderConfigModel(BaseModel):
    document_read_action: Literal[
        "TEXTRACT_ANALYZE_DOCUMENT", "TEXTRACT_DETECT_DOCUMENT_TEXT"
    ] = Field(alias="DocumentReadAction")
    document_read_mode: Optional[
        Literal["FORCE_DOCUMENT_READ_ACTION", "SERVICE_DEFAULT"]
    ] = Field(default=None, alias="DocumentReadMode")
    feature_types: Optional[Sequence[Literal["FORMS", "TABLES"]]] = Field(
        default=None, alias="FeatureTypes"
    )


class DocumentClassModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    score: Optional[float] = Field(default=None, alias="Score")
    page: Optional[int] = Field(default=None, alias="Page")


class DocumentLabelModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    score: Optional[float] = Field(default=None, alias="Score")
    page: Optional[int] = Field(default=None, alias="Page")


class DocumentTypeListItemModel(BaseModel):
    page: Optional[int] = Field(default=None, alias="Page")
    type: Optional[
        Literal[
            "IMAGE",
            "MS_WORD",
            "NATIVE_PDF",
            "PLAIN_TEXT",
            "SCANNED_PDF",
            "TEXTRACT_ANALYZE_DOCUMENT_JSON",
            "TEXTRACT_DETECT_DOCUMENT_TEXT_JSON",
        ]
    ] = Field(default=None, alias="Type")


class ErrorsListItemModel(BaseModel):
    page: Optional[int] = Field(default=None, alias="Page")
    error_code: Optional[
        Literal[
            "INTERNAL_SERVER_ERROR",
            "PAGE_CHARACTERS_EXCEEDED",
            "PAGE_SIZE_EXCEEDED",
            "TEXTRACT_BAD_PAGE",
            "TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ContainsPiiEntitiesRequestModel(BaseModel):
    text: str = Field(alias="Text")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class EntityLabelModel(BaseModel):
    name: Optional[
        Literal[
            "ADDRESS",
            "AGE",
            "ALL",
            "AWS_ACCESS_KEY",
            "AWS_SECRET_KEY",
            "BANK_ACCOUNT_NUMBER",
            "BANK_ROUTING",
            "CA_HEALTH_NUMBER",
            "CA_SOCIAL_INSURANCE_NUMBER",
            "CREDIT_DEBIT_CVV",
            "CREDIT_DEBIT_EXPIRY",
            "CREDIT_DEBIT_NUMBER",
            "DATE_TIME",
            "DRIVER_ID",
            "EMAIL",
            "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
            "IN_AADHAAR",
            "IN_NREGA",
            "IN_PERMANENT_ACCOUNT_NUMBER",
            "IN_VOTER_NUMBER",
            "IP_ADDRESS",
            "LICENSE_PLATE",
            "MAC_ADDRESS",
            "NAME",
            "PASSPORT_NUMBER",
            "PASSWORD",
            "PHONE",
            "PIN",
            "SSN",
            "SWIFT_CODE",
            "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
            "UK_NATIONAL_INSURANCE_NUMBER",
            "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
            "URL",
            "USERNAME",
            "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
            "VEHICLE_IDENTIFICATION_NUMBER",
        ]
    ] = Field(default=None, alias="Name")
    score: Optional[float] = Field(default=None, alias="Score")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class DocumentClassifierOutputDataConfigModel(BaseModel):
    s3_uri: Optional[str] = Field(default=None, alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    flywheel_stats_s3_prefix: Optional[str] = Field(
        default=None, alias="FlywheelStatsS3Prefix"
    )


class VpcConfigModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    subnets: Sequence[str] = Field(alias="Subnets")


class DatasetAugmentedManifestsListItemModel(BaseModel):
    attribute_names: Sequence[str] = Field(alias="AttributeNames")
    s3_uri: str = Field(alias="S3Uri")
    annotation_data_s3_uri: Optional[str] = Field(
        default=None, alias="AnnotationDataS3Uri"
    )
    source_documents_s3_uri: Optional[str] = Field(
        default=None, alias="SourceDocumentsS3Uri"
    )
    document_type: Optional[
        Literal["PLAIN_TEXT_DOCUMENT", "SEMI_STRUCTURED_DOCUMENT"]
    ] = Field(default=None, alias="DocumentType")


class DatasetDocumentClassifierInputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    label_delimiter: Optional[str] = Field(default=None, alias="LabelDelimiter")


class DatasetEntityRecognizerAnnotationsModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")


class DatasetEntityRecognizerDocumentsModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    input_format: Optional[Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]] = Field(
        default=None, alias="InputFormat"
    )


class DatasetEntityRecognizerEntityListModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")


class DatasetFilterModel(BaseModel):
    status: Optional[Literal["COMPLETED", "CREATING", "FAILED"]] = Field(
        default=None, alias="Status"
    )
    dataset_type: Optional[Literal["TEST", "TRAIN"]] = Field(
        default=None, alias="DatasetType"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )


class DatasetPropertiesModel(BaseModel):
    dataset_arn: Optional[str] = Field(default=None, alias="DatasetArn")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    dataset_type: Optional[Literal["TEST", "TRAIN"]] = Field(
        default=None, alias="DatasetType"
    )
    dataset_s3_uri: Optional[str] = Field(default=None, alias="DatasetS3Uri")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["COMPLETED", "CREATING", "FAILED"]] = Field(
        default=None, alias="Status"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    number_of_documents: Optional[int] = Field(default=None, alias="NumberOfDocuments")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class DeleteDocumentClassifierRequestModel(BaseModel):
    document_classifier_arn: str = Field(alias="DocumentClassifierArn")


class DeleteEndpointRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")


class DeleteEntityRecognizerRequestModel(BaseModel):
    entity_recognizer_arn: str = Field(alias="EntityRecognizerArn")


class DeleteFlywheelRequestModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")


class DeleteResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")


class DescribeDatasetRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")


class DescribeDocumentClassificationJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeDocumentClassifierRequestModel(BaseModel):
    document_classifier_arn: str = Field(alias="DocumentClassifierArn")


class DescribeDominantLanguageDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeEndpointRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")


class EndpointPropertiesModel(BaseModel):
    endpoint_arn: Optional[str] = Field(default=None, alias="EndpointArn")
    status: Optional[
        Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"]
    ] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    desired_model_arn: Optional[str] = Field(default=None, alias="DesiredModelArn")
    desired_inference_units: Optional[int] = Field(
        default=None, alias="DesiredInferenceUnits"
    )
    current_inference_units: Optional[int] = Field(
        default=None, alias="CurrentInferenceUnits"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    desired_data_access_role_arn: Optional[str] = Field(
        default=None, alias="DesiredDataAccessRoleArn"
    )
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")


class DescribeEntitiesDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeEntityRecognizerRequestModel(BaseModel):
    entity_recognizer_arn: str = Field(alias="EntityRecognizerArn")


class DescribeEventsDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeFlywheelIterationRequestModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")
    flywheel_iteration_id: str = Field(alias="FlywheelIterationId")


class DescribeFlywheelRequestModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")


class DescribeKeyPhrasesDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribePiiEntitiesDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DescribeSentimentDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeTargetedSentimentDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeTopicsDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DetectDominantLanguageRequestModel(BaseModel):
    text: str = Field(alias="Text")


class DetectKeyPhrasesRequestModel(BaseModel):
    text: str = Field(alias="Text")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class DetectPiiEntitiesRequestModel(BaseModel):
    text: str = Field(alias="Text")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class PiiEntityModel(BaseModel):
    score: Optional[float] = Field(default=None, alias="Score")
    type: Optional[
        Literal[
            "ADDRESS",
            "AGE",
            "ALL",
            "AWS_ACCESS_KEY",
            "AWS_SECRET_KEY",
            "BANK_ACCOUNT_NUMBER",
            "BANK_ROUTING",
            "CA_HEALTH_NUMBER",
            "CA_SOCIAL_INSURANCE_NUMBER",
            "CREDIT_DEBIT_CVV",
            "CREDIT_DEBIT_EXPIRY",
            "CREDIT_DEBIT_NUMBER",
            "DATE_TIME",
            "DRIVER_ID",
            "EMAIL",
            "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
            "IN_AADHAAR",
            "IN_NREGA",
            "IN_PERMANENT_ACCOUNT_NUMBER",
            "IN_VOTER_NUMBER",
            "IP_ADDRESS",
            "LICENSE_PLATE",
            "MAC_ADDRESS",
            "NAME",
            "PASSPORT_NUMBER",
            "PASSWORD",
            "PHONE",
            "PIN",
            "SSN",
            "SWIFT_CODE",
            "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
            "UK_NATIONAL_INSURANCE_NUMBER",
            "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
            "URL",
            "USERNAME",
            "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
            "VEHICLE_IDENTIFICATION_NUMBER",
        ]
    ] = Field(default=None, alias="Type")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")


class DetectSentimentRequestModel(BaseModel):
    text: str = Field(alias="Text")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class DetectSyntaxRequestModel(BaseModel):
    text: str = Field(alias="Text")
    language_code: Literal["de", "en", "es", "fr", "it", "pt"] = Field(
        alias="LanguageCode"
    )


class DetectTargetedSentimentRequestModel(BaseModel):
    text: str = Field(alias="Text")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")


class DocumentClassificationConfigModel(BaseModel):
    mode: Literal["MULTI_CLASS", "MULTI_LABEL"] = Field(alias="Mode")
    labels: Optional[Sequence[str]] = Field(default=None, alias="Labels")


class DocumentClassificationJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class OutputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class DocumentClassifierFilterModel(BaseModel):
    status: Optional[
        Literal[
            "DELETING",
            "IN_ERROR",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
            "TRAINED",
            "TRAINING",
        ]
    ] = Field(default=None, alias="Status")
    document_classifier_name: Optional[str] = Field(
        default=None, alias="DocumentClassifierName"
    )
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class DocumentClassifierSummaryModel(BaseModel):
    document_classifier_name: Optional[str] = Field(
        default=None, alias="DocumentClassifierName"
    )
    number_of_versions: Optional[int] = Field(default=None, alias="NumberOfVersions")
    latest_version_created_at: Optional[datetime] = Field(
        default=None, alias="LatestVersionCreatedAt"
    )
    latest_version_name: Optional[str] = Field(default=None, alias="LatestVersionName")
    latest_version_status: Optional[
        Literal[
            "DELETING",
            "IN_ERROR",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
            "TRAINED",
            "TRAINING",
        ]
    ] = Field(default=None, alias="LatestVersionStatus")


class ExtractedCharactersListItemModel(BaseModel):
    page: Optional[int] = Field(default=None, alias="Page")
    count: Optional[int] = Field(default=None, alias="Count")


class DominantLanguageDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class EndpointFilterModel(BaseModel):
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    status: Optional[
        Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"]
    ] = Field(default=None, alias="Status")
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )


class EntitiesDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class EntityTypesListItemModel(BaseModel):
    type: str = Field(alias="Type")


class EntityRecognizerAnnotationsModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    test_s3_uri: Optional[str] = Field(default=None, alias="TestS3Uri")


class EntityRecognizerDocumentsModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    test_s3_uri: Optional[str] = Field(default=None, alias="TestS3Uri")
    input_format: Optional[Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]] = Field(
        default=None, alias="InputFormat"
    )


class EntityRecognizerEntityListModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")


class EntityRecognizerEvaluationMetricsModel(BaseModel):
    precision: Optional[float] = Field(default=None, alias="Precision")
    recall: Optional[float] = Field(default=None, alias="Recall")
    f1_score: Optional[float] = Field(default=None, alias="F1Score")


class EntityRecognizerFilterModel(BaseModel):
    status: Optional[
        Literal[
            "DELETING",
            "IN_ERROR",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
            "TRAINED",
            "TRAINING",
        ]
    ] = Field(default=None, alias="Status")
    recognizer_name: Optional[str] = Field(default=None, alias="RecognizerName")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class EntityTypesEvaluationMetricsModel(BaseModel):
    precision: Optional[float] = Field(default=None, alias="Precision")
    recall: Optional[float] = Field(default=None, alias="Recall")
    f1_score: Optional[float] = Field(default=None, alias="F1Score")


class EntityRecognizerOutputDataConfigModel(BaseModel):
    flywheel_stats_s3_prefix: Optional[str] = Field(
        default=None, alias="FlywheelStatsS3Prefix"
    )


class EntityRecognizerSummaryModel(BaseModel):
    recognizer_name: Optional[str] = Field(default=None, alias="RecognizerName")
    number_of_versions: Optional[int] = Field(default=None, alias="NumberOfVersions")
    latest_version_created_at: Optional[datetime] = Field(
        default=None, alias="LatestVersionCreatedAt"
    )
    latest_version_name: Optional[str] = Field(default=None, alias="LatestVersionName")
    latest_version_status: Optional[
        Literal[
            "DELETING",
            "IN_ERROR",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
            "TRAINED",
            "TRAINING",
        ]
    ] = Field(default=None, alias="LatestVersionStatus")


class EventsDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class FlywheelFilterModel(BaseModel):
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )


class FlywheelIterationFilterModel(BaseModel):
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreationTimeBefore"
    )


class FlywheelModelEvaluationMetricsModel(BaseModel):
    average_f1_score: Optional[float] = Field(default=None, alias="AverageF1Score")
    average_precision: Optional[float] = Field(default=None, alias="AveragePrecision")
    average_recall: Optional[float] = Field(default=None, alias="AverageRecall")
    average_accuracy: Optional[float] = Field(default=None, alias="AverageAccuracy")


class FlywheelSummaryModel(BaseModel):
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")
    active_model_arn: Optional[str] = Field(default=None, alias="ActiveModelArn")
    data_lake_s3_uri: Optional[str] = Field(default=None, alias="DataLakeS3Uri")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")
    model_type: Optional[Literal["DOCUMENT_CLASSIFIER", "ENTITY_RECOGNIZER"]] = Field(
        default=None, alias="ModelType"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    latest_flywheel_iteration: Optional[str] = Field(
        default=None, alias="LatestFlywheelIteration"
    )


class PointModel(BaseModel):
    x: Optional[float] = Field(default=None, alias="X")
    y: Optional[float] = Field(default=None, alias="Y")


class KeyPhrasesDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDocumentClassifierSummariesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEntityRecognizerSummariesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PiiEntitiesDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class SentimentDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TargetedSentimentDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class TopicsDetectionJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submit_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeBefore"
    )
    submit_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmitTimeAfter"
    )


class PartOfSpeechTagModel(BaseModel):
    tag: Optional[
        Literal[
            "ADJ",
            "ADP",
            "ADV",
            "AUX",
            "CCONJ",
            "CONJ",
            "DET",
            "INTJ",
            "NOUN",
            "NUM",
            "O",
            "PART",
            "PRON",
            "PROPN",
            "PUNCT",
            "SCONJ",
            "SYM",
            "VERB",
        ]
    ] = Field(default=None, alias="Tag")
    score: Optional[float] = Field(default=None, alias="Score")


class PiiOutputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class RedactionConfigModel(BaseModel):
    pii_entity_types: Optional[
        List[
            Literal[
                "ADDRESS",
                "AGE",
                "ALL",
                "AWS_ACCESS_KEY",
                "AWS_SECRET_KEY",
                "BANK_ACCOUNT_NUMBER",
                "BANK_ROUTING",
                "CA_HEALTH_NUMBER",
                "CA_SOCIAL_INSURANCE_NUMBER",
                "CREDIT_DEBIT_CVV",
                "CREDIT_DEBIT_EXPIRY",
                "CREDIT_DEBIT_NUMBER",
                "DATE_TIME",
                "DRIVER_ID",
                "EMAIL",
                "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
                "IN_AADHAAR",
                "IN_NREGA",
                "IN_PERMANENT_ACCOUNT_NUMBER",
                "IN_VOTER_NUMBER",
                "IP_ADDRESS",
                "LICENSE_PLATE",
                "MAC_ADDRESS",
                "NAME",
                "PASSPORT_NUMBER",
                "PASSWORD",
                "PHONE",
                "PIN",
                "SSN",
                "SWIFT_CODE",
                "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
                "UK_NATIONAL_INSURANCE_NUMBER",
                "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
                "URL",
                "USERNAME",
                "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
                "VEHICLE_IDENTIFICATION_NUMBER",
            ]
        ]
    ] = Field(default=None, alias="PiiEntityTypes")
    mask_mode: Optional[Literal["MASK", "REPLACE_WITH_PII_ENTITY_TYPE"]] = Field(
        default=None, alias="MaskMode"
    )
    mask_character: Optional[str] = Field(default=None, alias="MaskCharacter")


class PutResourcePolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_policy: str = Field(alias="ResourcePolicy")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")


class StartFlywheelIterationRequestModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class StopDominantLanguageDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopEntitiesDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopEventsDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopKeyPhrasesDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopPiiEntitiesDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopSentimentDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopTargetedSentimentDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopTrainingDocumentClassifierRequestModel(BaseModel):
    document_classifier_arn: str = Field(alias="DocumentClassifierArn")


class StopTrainingEntityRecognizerRequestModel(BaseModel):
    entity_recognizer_arn: str = Field(alias="EntityRecognizerArn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateEndpointRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    desired_model_arn: Optional[str] = Field(default=None, alias="DesiredModelArn")
    desired_inference_units: Optional[int] = Field(
        default=None, alias="DesiredInferenceUnits"
    )
    desired_data_access_role_arn: Optional[str] = Field(
        default=None, alias="DesiredDataAccessRoleArn"
    )
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")


class DocumentClassifierInputDataConfigModel(BaseModel):
    data_format: Optional[Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]] = Field(
        default=None, alias="DataFormat"
    )
    s3_uri: Optional[str] = Field(default=None, alias="S3Uri")
    test_s3_uri: Optional[str] = Field(default=None, alias="TestS3Uri")
    label_delimiter: Optional[str] = Field(default=None, alias="LabelDelimiter")
    augmented_manifests: Optional[Sequence[AugmentedManifestsListItemModel]] = Field(
        default=None, alias="AugmentedManifests"
    )


class BatchDetectDominantLanguageItemResultModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    languages: Optional[List[DominantLanguageModel]] = Field(
        default=None, alias="Languages"
    )


class CreateDatasetResponseModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDocumentClassifierResponseModel(BaseModel):
    document_classifier_arn: str = Field(alias="DocumentClassifierArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointResponseModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    model_arn: str = Field(alias="ModelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEntityRecognizerResponseModel(BaseModel):
    entity_recognizer_arn: str = Field(alias="EntityRecognizerArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFlywheelResponseModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")
    active_model_arn: str = Field(alias="ActiveModelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourcePolicyResponseModel(BaseModel):
    resource_policy: str = Field(alias="ResourcePolicy")
    creation_time: datetime = Field(alias="CreationTime")
    last_modified_time: datetime = Field(alias="LastModifiedTime")
    policy_revision_id: str = Field(alias="PolicyRevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectDominantLanguageResponseModel(BaseModel):
    languages: List[DominantLanguageModel] = Field(alias="Languages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportModelResponseModel(BaseModel):
    model_arn: str = Field(alias="ModelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    policy_revision_id: str = Field(alias="PolicyRevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDocumentClassificationJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    document_classifier_arn: str = Field(alias="DocumentClassifierArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDominantLanguageDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartEntitiesDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    entity_recognizer_arn: str = Field(alias="EntityRecognizerArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartEventsDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFlywheelIterationResponseModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")
    flywheel_iteration_id: str = Field(alias="FlywheelIterationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartKeyPhrasesDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPiiEntitiesDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSentimentDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTargetedSentimentDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTopicsDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_arn: str = Field(alias="JobArn")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDominantLanguageDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopEntitiesDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopEventsDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopKeyPhrasesDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopPiiEntitiesDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopSentimentDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopTargetedSentimentDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEndpointResponseModel(BaseModel):
    desired_model_arn: str = Field(alias="DesiredModelArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectKeyPhrasesItemResultModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    key_phrases: Optional[List[KeyPhraseModel]] = Field(
        default=None, alias="KeyPhrases"
    )


class DetectKeyPhrasesResponseModel(BaseModel):
    key_phrases: List[KeyPhraseModel] = Field(alias="KeyPhrases")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectSentimentItemResultModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    sentiment: Optional[Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]] = Field(
        default=None, alias="Sentiment"
    )
    sentiment_score: Optional[SentimentScoreModel] = Field(
        default=None, alias="SentimentScore"
    )


class DetectSentimentResponseModel(BaseModel):
    sentiment: Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"] = Field(
        alias="Sentiment"
    )
    sentiment_score: SentimentScoreModel = Field(alias="SentimentScore")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MentionSentimentModel(BaseModel):
    sentiment: Optional[Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]] = Field(
        default=None, alias="Sentiment"
    )
    sentiment_score: Optional[SentimentScoreModel] = Field(
        default=None, alias="SentimentScore"
    )


class BlockReferenceModel(BaseModel):
    block_id: Optional[str] = Field(default=None, alias="BlockId")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    child_blocks: Optional[List[ChildBlockModel]] = Field(
        default=None, alias="ChildBlocks"
    )


class ClassifierMetadataModel(BaseModel):
    number_of_labels: Optional[int] = Field(default=None, alias="NumberOfLabels")
    number_of_trained_documents: Optional[int] = Field(
        default=None, alias="NumberOfTrainedDocuments"
    )
    number_of_test_documents: Optional[int] = Field(
        default=None, alias="NumberOfTestDocuments"
    )
    evaluation_metrics: Optional[ClassifierEvaluationMetricsModel] = Field(
        default=None, alias="EvaluationMetrics"
    )


class ClassifyDocumentRequestModel(BaseModel):
    endpoint_arn: str = Field(alias="EndpointArn")
    text: Optional[str] = Field(default=None, alias="Text")
    bytes: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Bytes"
    )
    document_reader_config: Optional[DocumentReaderConfigModel] = Field(
        default=None, alias="DocumentReaderConfig"
    )


class DetectEntitiesRequestModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    endpoint_arn: Optional[str] = Field(default=None, alias="EndpointArn")
    bytes: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Bytes"
    )
    document_reader_config: Optional[DocumentReaderConfigModel] = Field(
        default=None, alias="DocumentReaderConfig"
    )


class InputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    input_format: Optional[Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]] = Field(
        default=None, alias="InputFormat"
    )
    document_reader_config: Optional[DocumentReaderConfigModel] = Field(
        default=None, alias="DocumentReaderConfig"
    )


class ContainsPiiEntitiesResponseModel(BaseModel):
    labels: List[EntityLabelModel] = Field(alias="Labels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEndpointRequestModel(BaseModel):
    endpoint_name: str = Field(alias="EndpointName")
    desired_inference_units: int = Field(alias="DesiredInferenceUnits")
    model_arn: Optional[str] = Field(default=None, alias="ModelArn")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")


class ImportModelRequestModel(BaseModel):
    source_model_arn: str = Field(alias="SourceModelArn")
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    model_kms_key_id: Optional[str] = Field(default=None, alias="ModelKmsKeyId")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DataSecurityConfigModel(BaseModel):
    model_kms_key_id: Optional[str] = Field(default=None, alias="ModelKmsKeyId")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    data_lake_kms_key_id: Optional[str] = Field(default=None, alias="DataLakeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class UpdateDataSecurityConfigModel(BaseModel):
    model_kms_key_id: Optional[str] = Field(default=None, alias="ModelKmsKeyId")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class DatasetEntityRecognizerInputDataConfigModel(BaseModel):
    documents: DatasetEntityRecognizerDocumentsModel = Field(alias="Documents")
    annotations: Optional[DatasetEntityRecognizerAnnotationsModel] = Field(
        default=None, alias="Annotations"
    )
    entity_list: Optional[DatasetEntityRecognizerEntityListModel] = Field(
        default=None, alias="EntityList"
    )


class ListDatasetsRequestModel(BaseModel):
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")
    filter: Optional[DatasetFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeDatasetResponseModel(BaseModel):
    dataset_properties: DatasetPropertiesModel = Field(alias="DatasetProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetsResponseModel(BaseModel):
    dataset_properties_list: List[DatasetPropertiesModel] = Field(
        alias="DatasetPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointResponseModel(BaseModel):
    endpoint_properties: EndpointPropertiesModel = Field(alias="EndpointProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEndpointsResponseModel(BaseModel):
    endpoint_properties_list: List[EndpointPropertiesModel] = Field(
        alias="EndpointPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectPiiEntitiesResponseModel(BaseModel):
    entities: List[PiiEntityModel] = Field(alias="Entities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDocumentClassificationJobsRequestModel(BaseModel):
    filter: Optional[DocumentClassificationJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDocumentClassifiersRequestModel(BaseModel):
    filter: Optional[DocumentClassifierFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDocumentClassifierSummariesResponseModel(BaseModel):
    document_classifier_summaries_list: List[DocumentClassifierSummaryModel] = Field(
        alias="DocumentClassifierSummariesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentMetadataModel(BaseModel):
    pages: Optional[int] = Field(default=None, alias="Pages")
    extracted_characters: Optional[List[ExtractedCharactersListItemModel]] = Field(
        default=None, alias="ExtractedCharacters"
    )


class ListDominantLanguageDetectionJobsRequestModel(BaseModel):
    filter: Optional[DominantLanguageDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEndpointsRequestModel(BaseModel):
    filter: Optional[EndpointFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListEntitiesDetectionJobsRequestModel(BaseModel):
    filter: Optional[EntitiesDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class EntityRecognitionConfigModel(BaseModel):
    entity_types: Sequence[EntityTypesListItemModel] = Field(alias="EntityTypes")


class EntityRecognizerInputDataConfigModel(BaseModel):
    entity_types: Sequence[EntityTypesListItemModel] = Field(alias="EntityTypes")
    data_format: Optional[Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]] = Field(
        default=None, alias="DataFormat"
    )
    documents: Optional[EntityRecognizerDocumentsModel] = Field(
        default=None, alias="Documents"
    )
    annotations: Optional[EntityRecognizerAnnotationsModel] = Field(
        default=None, alias="Annotations"
    )
    entity_list: Optional[EntityRecognizerEntityListModel] = Field(
        default=None, alias="EntityList"
    )
    augmented_manifests: Optional[Sequence[AugmentedManifestsListItemModel]] = Field(
        default=None, alias="AugmentedManifests"
    )


class ListEntityRecognizersRequestModel(BaseModel):
    filter: Optional[EntityRecognizerFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class EntityRecognizerMetadataEntityTypesListItemModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    evaluation_metrics: Optional[EntityTypesEvaluationMetricsModel] = Field(
        default=None, alias="EvaluationMetrics"
    )
    number_of_train_mentions: Optional[int] = Field(
        default=None, alias="NumberOfTrainMentions"
    )


class ListEntityRecognizerSummariesResponseModel(BaseModel):
    entity_recognizer_summaries_list: List[EntityRecognizerSummaryModel] = Field(
        alias="EntityRecognizerSummariesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventsDetectionJobsRequestModel(BaseModel):
    filter: Optional[EventsDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFlywheelsRequestModel(BaseModel):
    filter: Optional[FlywheelFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFlywheelIterationHistoryRequestModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")
    filter: Optional[FlywheelIterationFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class FlywheelIterationPropertiesModel(BaseModel):
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")
    flywheel_iteration_id: Optional[str] = Field(
        default=None, alias="FlywheelIterationId"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    status: Optional[
        Literal[
            "COMPLETED", "EVALUATING", "FAILED", "STOPPED", "STOP_REQUESTED", "TRAINING"
        ]
    ] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    evaluated_model_arn: Optional[str] = Field(default=None, alias="EvaluatedModelArn")
    evaluated_model_metrics: Optional[FlywheelModelEvaluationMetricsModel] = Field(
        default=None, alias="EvaluatedModelMetrics"
    )
    trained_model_arn: Optional[str] = Field(default=None, alias="TrainedModelArn")
    trained_model_metrics: Optional[FlywheelModelEvaluationMetricsModel] = Field(
        default=None, alias="TrainedModelMetrics"
    )
    evaluation_manifest_s3_prefix: Optional[str] = Field(
        default=None, alias="EvaluationManifestS3Prefix"
    )


class ListFlywheelsResponseModel(BaseModel):
    flywheel_summary_list: List[FlywheelSummaryModel] = Field(
        alias="FlywheelSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GeometryModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    polygon: Optional[List[PointModel]] = Field(default=None, alias="Polygon")


class ListKeyPhrasesDetectionJobsRequestModel(BaseModel):
    filter: Optional[KeyPhrasesDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDocumentClassificationJobsRequestListDocumentClassificationJobsPaginateModel(
    BaseModel
):
    filter: Optional[DocumentClassificationJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDocumentClassifiersRequestListDocumentClassifiersPaginateModel(BaseModel):
    filter: Optional[DocumentClassifierFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDominantLanguageDetectionJobsRequestListDominantLanguageDetectionJobsPaginateModel(
    BaseModel
):
    filter: Optional[DominantLanguageDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEndpointsRequestListEndpointsPaginateModel(BaseModel):
    filter: Optional[EndpointFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEntitiesDetectionJobsRequestListEntitiesDetectionJobsPaginateModel(BaseModel):
    filter: Optional[EntitiesDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEntityRecognizersRequestListEntityRecognizersPaginateModel(BaseModel):
    filter: Optional[EntityRecognizerFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListKeyPhrasesDetectionJobsRequestListKeyPhrasesDetectionJobsPaginateModel(
    BaseModel
):
    filter: Optional[KeyPhrasesDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPiiEntitiesDetectionJobsRequestListPiiEntitiesDetectionJobsPaginateModel(
    BaseModel
):
    filter: Optional[PiiEntitiesDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPiiEntitiesDetectionJobsRequestModel(BaseModel):
    filter: Optional[PiiEntitiesDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSentimentDetectionJobsRequestListSentimentDetectionJobsPaginateModel(
    BaseModel
):
    filter: Optional[SentimentDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSentimentDetectionJobsRequestModel(BaseModel):
    filter: Optional[SentimentDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTargetedSentimentDetectionJobsRequestModel(BaseModel):
    filter: Optional[TargetedSentimentDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTopicsDetectionJobsRequestListTopicsDetectionJobsPaginateModel(BaseModel):
    filter: Optional[TopicsDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTopicsDetectionJobsRequestModel(BaseModel):
    filter: Optional[TopicsDetectionJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SyntaxTokenModel(BaseModel):
    token_id: Optional[int] = Field(default=None, alias="TokenId")
    text: Optional[str] = Field(default=None, alias="Text")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    part_of_speech: Optional[PartOfSpeechTagModel] = Field(
        default=None, alias="PartOfSpeech"
    )


class CreateDocumentClassifierRequestModel(BaseModel):
    document_classifier_name: str = Field(alias="DocumentClassifierName")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    input_data_config: DocumentClassifierInputDataConfigModel = Field(
        alias="InputDataConfig"
    )
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    output_data_config: Optional[DocumentClassifierOutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    mode: Optional[Literal["MULTI_CLASS", "MULTI_LABEL"]] = Field(
        default=None, alias="Mode"
    )
    model_kms_key_id: Optional[str] = Field(default=None, alias="ModelKmsKeyId")
    model_policy: Optional[str] = Field(default=None, alias="ModelPolicy")


class BatchDetectDominantLanguageResponseModel(BaseModel):
    result_list: List[BatchDetectDominantLanguageItemResultModel] = Field(
        alias="ResultList"
    )
    error_list: List[BatchItemErrorModel] = Field(alias="ErrorList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectKeyPhrasesResponseModel(BaseModel):
    result_list: List[BatchDetectKeyPhrasesItemResultModel] = Field(alias="ResultList")
    error_list: List[BatchItemErrorModel] = Field(alias="ErrorList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectSentimentResponseModel(BaseModel):
    result_list: List[BatchDetectSentimentItemResultModel] = Field(alias="ResultList")
    error_list: List[BatchItemErrorModel] = Field(alias="ErrorList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TargetedSentimentMentionModel(BaseModel):
    score: Optional[float] = Field(default=None, alias="Score")
    group_score: Optional[float] = Field(default=None, alias="GroupScore")
    text: Optional[str] = Field(default=None, alias="Text")
    type: Optional[
        Literal[
            "ATTRIBUTE",
            "BOOK",
            "BRAND",
            "COMMERCIAL_ITEM",
            "DATE",
            "EVENT",
            "FACILITY",
            "GAME",
            "LOCATION",
            "MOVIE",
            "MUSIC",
            "ORGANIZATION",
            "OTHER",
            "PERSON",
            "PERSONAL_TITLE",
            "QUANTITY",
            "SOFTWARE",
        ]
    ] = Field(default=None, alias="Type")
    mention_sentiment: Optional[MentionSentimentModel] = Field(
        default=None, alias="MentionSentiment"
    )
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")


class EntityModel(BaseModel):
    score: Optional[float] = Field(default=None, alias="Score")
    type: Optional[
        Literal[
            "COMMERCIAL_ITEM",
            "DATE",
            "EVENT",
            "LOCATION",
            "ORGANIZATION",
            "OTHER",
            "PERSON",
            "QUANTITY",
            "TITLE",
        ]
    ] = Field(default=None, alias="Type")
    text: Optional[str] = Field(default=None, alias="Text")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    block_references: Optional[List[BlockReferenceModel]] = Field(
        default=None, alias="BlockReferences"
    )


class DocumentClassifierPropertiesModel(BaseModel):
    document_classifier_arn: Optional[str] = Field(
        default=None, alias="DocumentClassifierArn"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    status: Optional[
        Literal[
            "DELETING",
            "IN_ERROR",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
            "TRAINED",
            "TRAINING",
        ]
    ] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    training_start_time: Optional[datetime] = Field(
        default=None, alias="TrainingStartTime"
    )
    training_end_time: Optional[datetime] = Field(default=None, alias="TrainingEndTime")
    input_data_config: Optional[DocumentClassifierInputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[DocumentClassifierOutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    classifier_metadata: Optional[ClassifierMetadataModel] = Field(
        default=None, alias="ClassifierMetadata"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    mode: Optional[Literal["MULTI_CLASS", "MULTI_LABEL"]] = Field(
        default=None, alias="Mode"
    )
    model_kms_key_id: Optional[str] = Field(default=None, alias="ModelKmsKeyId")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    source_model_arn: Optional[str] = Field(default=None, alias="SourceModelArn")
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")


class DocumentClassificationJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    document_classifier_arn: Optional[str] = Field(
        default=None, alias="DocumentClassifierArn"
    )
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")


class DominantLanguageDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class EntitiesDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    entity_recognizer_arn: Optional[str] = Field(
        default=None, alias="EntityRecognizerArn"
    )
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class EventsDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    target_event_types: Optional[List[str]] = Field(
        default=None, alias="TargetEventTypes"
    )


class KeyPhrasesDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class PiiEntitiesDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[PiiOutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    redaction_config: Optional[RedactionConfigModel] = Field(
        default=None, alias="RedactionConfig"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    mode: Optional[Literal["ONLY_OFFSETS", "ONLY_REDACTION"]] = Field(
        default=None, alias="Mode"
    )


class SentimentDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class StartDocumentClassificationJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    document_classifier_arn: Optional[str] = Field(
        default=None, alias="DocumentClassifierArn"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")


class StartDominantLanguageDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StartEntitiesDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    entity_recognizer_arn: Optional[str] = Field(
        default=None, alias="EntityRecognizerArn"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")


class StartEventsDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    target_event_types: Sequence[str] = Field(alias="TargetEventTypes")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StartKeyPhrasesDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StartPiiEntitiesDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    mode: Literal["ONLY_OFFSETS", "ONLY_REDACTION"] = Field(alias="Mode")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    redaction_config: Optional[RedactionConfigModel] = Field(
        default=None, alias="RedactionConfig"
    )
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StartSentimentDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StartTargetedSentimentDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StartTopicsDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    number_of_topics: Optional[int] = Field(default=None, alias="NumberOfTopics")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TargetedSentimentDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class TopicsDetectionJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_arn: Optional[str] = Field(default=None, alias="JobArn")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    number_of_topics: Optional[int] = Field(default=None, alias="NumberOfTopics")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")


class UpdateFlywheelRequestModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")
    active_model_arn: Optional[str] = Field(default=None, alias="ActiveModelArn")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    data_security_config: Optional[UpdateDataSecurityConfigModel] = Field(
        default=None, alias="DataSecurityConfig"
    )


class DatasetInputDataConfigModel(BaseModel):
    augmented_manifests: Optional[
        Sequence[DatasetAugmentedManifestsListItemModel]
    ] = Field(default=None, alias="AugmentedManifests")
    data_format: Optional[Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]] = Field(
        default=None, alias="DataFormat"
    )
    document_classifier_input_data_config: Optional[
        DatasetDocumentClassifierInputDataConfigModel
    ] = Field(default=None, alias="DocumentClassifierInputDataConfig")
    entity_recognizer_input_data_config: Optional[
        DatasetEntityRecognizerInputDataConfigModel
    ] = Field(default=None, alias="EntityRecognizerInputDataConfig")


class ClassifyDocumentResponseModel(BaseModel):
    classes: List[DocumentClassModel] = Field(alias="Classes")
    labels: List[DocumentLabelModel] = Field(alias="Labels")
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    document_type: List[DocumentTypeListItemModel] = Field(alias="DocumentType")
    errors: List[ErrorsListItemModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TaskConfigModel(BaseModel):
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    document_classification_config: Optional[DocumentClassificationConfigModel] = Field(
        default=None, alias="DocumentClassificationConfig"
    )
    entity_recognition_config: Optional[EntityRecognitionConfigModel] = Field(
        default=None, alias="EntityRecognitionConfig"
    )


class CreateEntityRecognizerRequestModel(BaseModel):
    recognizer_name: str = Field(alias="RecognizerName")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    input_data_config: EntityRecognizerInputDataConfigModel = Field(
        alias="InputDataConfig"
    )
    language_code: Literal[
        "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="LanguageCode")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    model_kms_key_id: Optional[str] = Field(default=None, alias="ModelKmsKeyId")
    model_policy: Optional[str] = Field(default=None, alias="ModelPolicy")


class EntityRecognizerMetadataModel(BaseModel):
    number_of_trained_documents: Optional[int] = Field(
        default=None, alias="NumberOfTrainedDocuments"
    )
    number_of_test_documents: Optional[int] = Field(
        default=None, alias="NumberOfTestDocuments"
    )
    evaluation_metrics: Optional[EntityRecognizerEvaluationMetricsModel] = Field(
        default=None, alias="EvaluationMetrics"
    )
    entity_types: Optional[
        List[EntityRecognizerMetadataEntityTypesListItemModel]
    ] = Field(default=None, alias="EntityTypes")


class DescribeFlywheelIterationResponseModel(BaseModel):
    flywheel_iteration_properties: FlywheelIterationPropertiesModel = Field(
        alias="FlywheelIterationProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFlywheelIterationHistoryResponseModel(BaseModel):
    flywheel_iteration_properties_list: List[FlywheelIterationPropertiesModel] = Field(
        alias="FlywheelIterationPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BlockModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    block_type: Optional[Literal["LINE", "WORD"]] = Field(
        default=None, alias="BlockType"
    )
    text: Optional[str] = Field(default=None, alias="Text")
    page: Optional[int] = Field(default=None, alias="Page")
    geometry: Optional[GeometryModel] = Field(default=None, alias="Geometry")
    relationships: Optional[List[RelationshipsListItemModel]] = Field(
        default=None, alias="Relationships"
    )


class BatchDetectSyntaxItemResultModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    syntax_tokens: Optional[List[SyntaxTokenModel]] = Field(
        default=None, alias="SyntaxTokens"
    )


class DetectSyntaxResponseModel(BaseModel):
    syntax_tokens: List[SyntaxTokenModel] = Field(alias="SyntaxTokens")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TargetedSentimentEntityModel(BaseModel):
    descriptive_mention_index: Optional[List[int]] = Field(
        default=None, alias="DescriptiveMentionIndex"
    )
    mentions: Optional[List[TargetedSentimentMentionModel]] = Field(
        default=None, alias="Mentions"
    )


class BatchDetectEntitiesItemResultModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    entities: Optional[List[EntityModel]] = Field(default=None, alias="Entities")


class DescribeDocumentClassifierResponseModel(BaseModel):
    document_classifier_properties: DocumentClassifierPropertiesModel = Field(
        alias="DocumentClassifierProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDocumentClassifiersResponseModel(BaseModel):
    document_classifier_properties_list: List[
        DocumentClassifierPropertiesModel
    ] = Field(alias="DocumentClassifierPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDocumentClassificationJobResponseModel(BaseModel):
    document_classification_job_properties: DocumentClassificationJobPropertiesModel = (
        Field(alias="DocumentClassificationJobProperties")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDocumentClassificationJobsResponseModel(BaseModel):
    document_classification_job_properties_list: List[
        DocumentClassificationJobPropertiesModel
    ] = Field(alias="DocumentClassificationJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDominantLanguageDetectionJobResponseModel(BaseModel):
    dominant_language_detection_job_properties: DominantLanguageDetectionJobPropertiesModel = Field(
        alias="DominantLanguageDetectionJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDominantLanguageDetectionJobsResponseModel(BaseModel):
    dominant_language_detection_job_properties_list: List[
        DominantLanguageDetectionJobPropertiesModel
    ] = Field(alias="DominantLanguageDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEntitiesDetectionJobResponseModel(BaseModel):
    entities_detection_job_properties: EntitiesDetectionJobPropertiesModel = Field(
        alias="EntitiesDetectionJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEntitiesDetectionJobsResponseModel(BaseModel):
    entities_detection_job_properties_list: List[
        EntitiesDetectionJobPropertiesModel
    ] = Field(alias="EntitiesDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEventsDetectionJobResponseModel(BaseModel):
    events_detection_job_properties: EventsDetectionJobPropertiesModel = Field(
        alias="EventsDetectionJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventsDetectionJobsResponseModel(BaseModel):
    events_detection_job_properties_list: List[
        EventsDetectionJobPropertiesModel
    ] = Field(alias="EventsDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeKeyPhrasesDetectionJobResponseModel(BaseModel):
    key_phrases_detection_job_properties: KeyPhrasesDetectionJobPropertiesModel = Field(
        alias="KeyPhrasesDetectionJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListKeyPhrasesDetectionJobsResponseModel(BaseModel):
    key_phrases_detection_job_properties_list: List[
        KeyPhrasesDetectionJobPropertiesModel
    ] = Field(alias="KeyPhrasesDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePiiEntitiesDetectionJobResponseModel(BaseModel):
    pii_entities_detection_job_properties: PiiEntitiesDetectionJobPropertiesModel = (
        Field(alias="PiiEntitiesDetectionJobProperties")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPiiEntitiesDetectionJobsResponseModel(BaseModel):
    pii_entities_detection_job_properties_list: List[
        PiiEntitiesDetectionJobPropertiesModel
    ] = Field(alias="PiiEntitiesDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSentimentDetectionJobResponseModel(BaseModel):
    sentiment_detection_job_properties: SentimentDetectionJobPropertiesModel = Field(
        alias="SentimentDetectionJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSentimentDetectionJobsResponseModel(BaseModel):
    sentiment_detection_job_properties_list: List[
        SentimentDetectionJobPropertiesModel
    ] = Field(alias="SentimentDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTargetedSentimentDetectionJobResponseModel(BaseModel):
    targeted_sentiment_detection_job_properties: TargetedSentimentDetectionJobPropertiesModel = Field(
        alias="TargetedSentimentDetectionJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTargetedSentimentDetectionJobsResponseModel(BaseModel):
    targeted_sentiment_detection_job_properties_list: List[
        TargetedSentimentDetectionJobPropertiesModel
    ] = Field(alias="TargetedSentimentDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTopicsDetectionJobResponseModel(BaseModel):
    topics_detection_job_properties: TopicsDetectionJobPropertiesModel = Field(
        alias="TopicsDetectionJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTopicsDetectionJobsResponseModel(BaseModel):
    topics_detection_job_properties_list: List[
        TopicsDetectionJobPropertiesModel
    ] = Field(alias="TopicsDetectionJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetRequestModel(BaseModel):
    flywheel_arn: str = Field(alias="FlywheelArn")
    dataset_name: str = Field(alias="DatasetName")
    input_data_config: DatasetInputDataConfigModel = Field(alias="InputDataConfig")
    dataset_type: Optional[Literal["TEST", "TRAIN"]] = Field(
        default=None, alias="DatasetType"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateFlywheelRequestModel(BaseModel):
    flywheel_name: str = Field(alias="FlywheelName")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    data_lake_s3_uri: str = Field(alias="DataLakeS3Uri")
    active_model_arn: Optional[str] = Field(default=None, alias="ActiveModelArn")
    task_config: Optional[TaskConfigModel] = Field(default=None, alias="TaskConfig")
    model_type: Optional[Literal["DOCUMENT_CLASSIFIER", "ENTITY_RECOGNIZER"]] = Field(
        default=None, alias="ModelType"
    )
    data_security_config: Optional[DataSecurityConfigModel] = Field(
        default=None, alias="DataSecurityConfig"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class FlywheelPropertiesModel(BaseModel):
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")
    active_model_arn: Optional[str] = Field(default=None, alias="ActiveModelArn")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    task_config: Optional[TaskConfigModel] = Field(default=None, alias="TaskConfig")
    data_lake_s3_uri: Optional[str] = Field(default=None, alias="DataLakeS3Uri")
    data_security_config: Optional[DataSecurityConfigModel] = Field(
        default=None, alias="DataSecurityConfig"
    )
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")
    model_type: Optional[Literal["DOCUMENT_CLASSIFIER", "ENTITY_RECOGNIZER"]] = Field(
        default=None, alias="ModelType"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )
    latest_flywheel_iteration: Optional[str] = Field(
        default=None, alias="LatestFlywheelIteration"
    )


class EntityRecognizerPropertiesModel(BaseModel):
    entity_recognizer_arn: Optional[str] = Field(
        default=None, alias="EntityRecognizerArn"
    )
    language_code: Optional[
        Literal[
            "ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"
        ]
    ] = Field(default=None, alias="LanguageCode")
    status: Optional[
        Literal[
            "DELETING",
            "IN_ERROR",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
            "TRAINED",
            "TRAINING",
        ]
    ] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    training_start_time: Optional[datetime] = Field(
        default=None, alias="TrainingStartTime"
    )
    training_end_time: Optional[datetime] = Field(default=None, alias="TrainingEndTime")
    input_data_config: Optional[EntityRecognizerInputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    recognizer_metadata: Optional[EntityRecognizerMetadataModel] = Field(
        default=None, alias="RecognizerMetadata"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    volume_kms_key_id: Optional[str] = Field(default=None, alias="VolumeKmsKeyId")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    model_kms_key_id: Optional[str] = Field(default=None, alias="ModelKmsKeyId")
    version_name: Optional[str] = Field(default=None, alias="VersionName")
    source_model_arn: Optional[str] = Field(default=None, alias="SourceModelArn")
    flywheel_arn: Optional[str] = Field(default=None, alias="FlywheelArn")
    output_data_config: Optional[EntityRecognizerOutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )


class DetectEntitiesResponseModel(BaseModel):
    entities: List[EntityModel] = Field(alias="Entities")
    document_metadata: DocumentMetadataModel = Field(alias="DocumentMetadata")
    document_type: List[DocumentTypeListItemModel] = Field(alias="DocumentType")
    blocks: List[BlockModel] = Field(alias="Blocks")
    errors: List[ErrorsListItemModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectSyntaxResponseModel(BaseModel):
    result_list: List[BatchDetectSyntaxItemResultModel] = Field(alias="ResultList")
    error_list: List[BatchItemErrorModel] = Field(alias="ErrorList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectTargetedSentimentItemResultModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    entities: Optional[List[TargetedSentimentEntityModel]] = Field(
        default=None, alias="Entities"
    )


class DetectTargetedSentimentResponseModel(BaseModel):
    entities: List[TargetedSentimentEntityModel] = Field(alias="Entities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectEntitiesResponseModel(BaseModel):
    result_list: List[BatchDetectEntitiesItemResultModel] = Field(alias="ResultList")
    error_list: List[BatchItemErrorModel] = Field(alias="ErrorList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFlywheelResponseModel(BaseModel):
    flywheel_properties: FlywheelPropertiesModel = Field(alias="FlywheelProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlywheelResponseModel(BaseModel):
    flywheel_properties: FlywheelPropertiesModel = Field(alias="FlywheelProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEntityRecognizerResponseModel(BaseModel):
    entity_recognizer_properties: EntityRecognizerPropertiesModel = Field(
        alias="EntityRecognizerProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEntityRecognizersResponseModel(BaseModel):
    entity_recognizer_properties_list: List[EntityRecognizerPropertiesModel] = Field(
        alias="EntityRecognizerPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDetectTargetedSentimentResponseModel(BaseModel):
    result_list: List[BatchDetectTargetedSentimentItemResultModel] = Field(
        alias="ResultList"
    )
    error_list: List[BatchItemErrorModel] = Field(alias="ErrorList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
