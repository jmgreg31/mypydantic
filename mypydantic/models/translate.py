# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TermModel(BaseModel):
    source_text: Optional[str] = Field(default=None, alias="SourceText")
    target_text: Optional[str] = Field(default=None, alias="TargetText")


class EncryptionKeyModel(BaseModel):
    type: Literal["KMS"] = Field(alias="Type")
    id: str = Field(alias="Id")


class ParallelDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    format: Literal["CSV", "TMX", "TSV"] = Field(alias="Format")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteParallelDataRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteTerminologyRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeTextTranslationJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class GetParallelDataRequestModel(BaseModel):
    name: str = Field(alias="Name")


class ParallelDataDataLocationModel(BaseModel):
    repository_type: str = Field(alias="RepositoryType")
    location: str = Field(alias="Location")


class GetTerminologyRequestModel(BaseModel):
    name: str = Field(alias="Name")
    terminology_data_format: Optional[Literal["CSV", "TMX", "TSV"]] = Field(
        default=None, alias="TerminologyDataFormat"
    )


class TerminologyDataLocationModel(BaseModel):
    repository_type: str = Field(alias="RepositoryType")
    location: str = Field(alias="Location")


class TerminologyDataModel(BaseModel):
    file: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="File")
    format: Literal["CSV", "TMX", "TSV"] = Field(alias="Format")
    directionality: Optional[Literal["MULTI", "UNI"]] = Field(
        default=None, alias="Directionality"
    )


class InputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    content_type: str = Field(alias="ContentType")


class JobDetailsModel(BaseModel):
    translated_documents_count: Optional[int] = Field(
        default=None, alias="TranslatedDocumentsCount"
    )
    documents_with_errors_count: Optional[int] = Field(
        default=None, alias="DocumentsWithErrorsCount"
    )
    input_documents_count: Optional[int] = Field(
        default=None, alias="InputDocumentsCount"
    )


class LanguageModel(BaseModel):
    language_name: str = Field(alias="LanguageName")
    language_code: str = Field(alias="LanguageCode")


class ListLanguagesRequestModel(BaseModel):
    display_language_code: Optional[
        Literal["de", "en", "es", "fr", "it", "ja", "ko", "pt", "zh", "zh-TW"]
    ] = Field(default=None, alias="DisplayLanguageCode")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListParallelDataRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListTerminologiesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class TextTranslationJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    submitted_before_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedBeforeTime"
    )
    submitted_after_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedAfterTime"
    )


class TranslationSettingsModel(BaseModel):
    formality: Optional[Literal["FORMAL", "INFORMAL"]] = Field(
        default=None, alias="Formality"
    )
    profanity: Optional[Literal["MASK"]] = Field(default=None, alias="Profanity")


class StopTextTranslationJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AppliedTerminologyModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    terms: Optional[List[TermModel]] = Field(default=None, alias="Terms")


class OutputDataConfigModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="EncryptionKey"
    )


class TerminologyPropertiesModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    arn: Optional[str] = Field(default=None, alias="Arn")
    source_language_code: Optional[str] = Field(
        default=None, alias="SourceLanguageCode"
    )
    target_language_codes: Optional[List[str]] = Field(
        default=None, alias="TargetLanguageCodes"
    )
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="EncryptionKey"
    )
    size_bytes: Optional[int] = Field(default=None, alias="SizeBytes")
    term_count: Optional[int] = Field(default=None, alias="TermCount")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    directionality: Optional[Literal["MULTI", "UNI"]] = Field(
        default=None, alias="Directionality"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    skipped_term_count: Optional[int] = Field(default=None, alias="SkippedTermCount")
    format: Optional[Literal["CSV", "TMX", "TSV"]] = Field(default=None, alias="Format")


class ParallelDataPropertiesModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="Status")
    source_language_code: Optional[str] = Field(
        default=None, alias="SourceLanguageCode"
    )
    target_language_codes: Optional[List[str]] = Field(
        default=None, alias="TargetLanguageCodes"
    )
    parallel_data_config: Optional[ParallelDataConfigModel] = Field(
        default=None, alias="ParallelDataConfig"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    imported_data_size: Optional[int] = Field(default=None, alias="ImportedDataSize")
    imported_record_count: Optional[int] = Field(
        default=None, alias="ImportedRecordCount"
    )
    failed_record_count: Optional[int] = Field(default=None, alias="FailedRecordCount")
    skipped_record_count: Optional[int] = Field(
        default=None, alias="SkippedRecordCount"
    )
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="EncryptionKey"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    latest_update_attempt_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="LatestUpdateAttemptStatus")
    latest_update_attempt_at: Optional[datetime] = Field(
        default=None, alias="LatestUpdateAttemptAt"
    )


class UpdateParallelDataRequestModel(BaseModel):
    name: str = Field(alias="Name")
    parallel_data_config: ParallelDataConfigModel = Field(alias="ParallelDataConfig")
    client_token: str = Field(alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateParallelDataRequestModel(BaseModel):
    name: str = Field(alias="Name")
    parallel_data_config: ParallelDataConfigModel = Field(alias="ParallelDataConfig")
    client_token: str = Field(alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="EncryptionKey"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateParallelDataResponseModel(BaseModel):
    name: str = Field(alias="Name")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteParallelDataResponseModel(BaseModel):
    name: str = Field(alias="Name")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="Status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTextTranslationJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED",
        "COMPLETED_WITH_ERROR",
        "FAILED",
        "IN_PROGRESS",
        "STOPPED",
        "STOP_REQUESTED",
        "SUBMITTED",
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopTextTranslationJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED",
        "COMPLETED_WITH_ERROR",
        "FAILED",
        "IN_PROGRESS",
        "STOPPED",
        "STOP_REQUESTED",
        "SUBMITTED",
    ] = Field(alias="JobStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateParallelDataResponseModel(BaseModel):
    name: str = Field(alias="Name")
    status: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="Status"
    )
    latest_update_attempt_status: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"
    ] = Field(alias="LatestUpdateAttemptStatus")
    latest_update_attempt_at: datetime = Field(alias="LatestUpdateAttemptAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportTerminologyRequestModel(BaseModel):
    name: str = Field(alias="Name")
    merge_strategy: Literal["OVERWRITE"] = Field(alias="MergeStrategy")
    terminology_data: TerminologyDataModel = Field(alias="TerminologyData")
    description: Optional[str] = Field(default=None, alias="Description")
    encryption_key: Optional[EncryptionKeyModel] = Field(
        default=None, alias="EncryptionKey"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListLanguagesResponseModel(BaseModel):
    languages: List[LanguageModel] = Field(alias="Languages")
    display_language_code: Literal[
        "de", "en", "es", "fr", "it", "ja", "ko", "pt", "zh", "zh-TW"
    ] = Field(alias="DisplayLanguageCode")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTerminologiesRequestListTerminologiesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTextTranslationJobsRequestModel(BaseModel):
    filter: Optional[TextTranslationJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class TranslateTextRequestModel(BaseModel):
    text: str = Field(alias="Text")
    source_language_code: str = Field(alias="SourceLanguageCode")
    target_language_code: str = Field(alias="TargetLanguageCode")
    terminology_names: Optional[Sequence[str]] = Field(
        default=None, alias="TerminologyNames"
    )
    settings: Optional[TranslationSettingsModel] = Field(default=None, alias="Settings")


class TranslateTextResponseModel(BaseModel):
    translated_text: str = Field(alias="TranslatedText")
    source_language_code: str = Field(alias="SourceLanguageCode")
    target_language_code: str = Field(alias="TargetLanguageCode")
    applied_terminologies: List[AppliedTerminologyModel] = Field(
        alias="AppliedTerminologies"
    )
    applied_settings: TranslationSettingsModel = Field(alias="AppliedSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTextTranslationJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    source_language_code: str = Field(alias="SourceLanguageCode")
    target_language_codes: Sequence[str] = Field(alias="TargetLanguageCodes")
    client_token: str = Field(alias="ClientToken")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    terminology_names: Optional[Sequence[str]] = Field(
        default=None, alias="TerminologyNames"
    )
    parallel_data_names: Optional[Sequence[str]] = Field(
        default=None, alias="ParallelDataNames"
    )
    settings: Optional[TranslationSettingsModel] = Field(default=None, alias="Settings")


class TextTranslationJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "IN_PROGRESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    job_details: Optional[JobDetailsModel] = Field(default=None, alias="JobDetails")
    source_language_code: Optional[str] = Field(
        default=None, alias="SourceLanguageCode"
    )
    target_language_codes: Optional[List[str]] = Field(
        default=None, alias="TargetLanguageCodes"
    )
    terminology_names: Optional[List[str]] = Field(
        default=None, alias="TerminologyNames"
    )
    parallel_data_names: Optional[List[str]] = Field(
        default=None, alias="ParallelDataNames"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    submitted_time: Optional[datetime] = Field(default=None, alias="SubmittedTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    settings: Optional[TranslationSettingsModel] = Field(default=None, alias="Settings")


class GetTerminologyResponseModel(BaseModel):
    terminology_properties: TerminologyPropertiesModel = Field(
        alias="TerminologyProperties"
    )
    terminology_data_location: TerminologyDataLocationModel = Field(
        alias="TerminologyDataLocation"
    )
    auxiliary_data_location: TerminologyDataLocationModel = Field(
        alias="AuxiliaryDataLocation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportTerminologyResponseModel(BaseModel):
    terminology_properties: TerminologyPropertiesModel = Field(
        alias="TerminologyProperties"
    )
    auxiliary_data_location: TerminologyDataLocationModel = Field(
        alias="AuxiliaryDataLocation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTerminologiesResponseModel(BaseModel):
    terminology_properties_list: List[TerminologyPropertiesModel] = Field(
        alias="TerminologyPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetParallelDataResponseModel(BaseModel):
    parallel_data_properties: ParallelDataPropertiesModel = Field(
        alias="ParallelDataProperties"
    )
    data_location: ParallelDataDataLocationModel = Field(alias="DataLocation")
    auxiliary_data_location: ParallelDataDataLocationModel = Field(
        alias="AuxiliaryDataLocation"
    )
    latest_update_attempt_auxiliary_data_location: ParallelDataDataLocationModel = (
        Field(alias="LatestUpdateAttemptAuxiliaryDataLocation")
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListParallelDataResponseModel(BaseModel):
    parallel_data_properties_list: List[ParallelDataPropertiesModel] = Field(
        alias="ParallelDataPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTextTranslationJobResponseModel(BaseModel):
    text_translation_job_properties: TextTranslationJobPropertiesModel = Field(
        alias="TextTranslationJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTextTranslationJobsResponseModel(BaseModel):
    text_translation_job_properties_list: List[
        TextTranslationJobPropertiesModel
    ] = Field(alias="TextTranslationJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
