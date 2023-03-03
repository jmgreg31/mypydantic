# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TraitModel(BaseModel):
    name: Optional[
        Literal[
            "DIAGNOSIS",
            "FUTURE",
            "HYPOTHETICAL",
            "LOW_CONFIDENCE",
            "NEGATION",
            "PAST_HISTORY",
            "PERTAINS_TO_FAMILY",
            "SIGN",
            "SYMPTOM",
        ]
    ] = Field(default=None, alias="Name")
    score: Optional[float] = Field(default=None, alias="Score")


class CharactersModel(BaseModel):
    original_text_characters: Optional[int] = Field(
        default=None, alias="OriginalTextCharacters"
    )


class ComprehendMedicalAsyncJobFilterModel(BaseModel):
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "PARTIAL_SUCCESS",
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


class InputDataConfigModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")


class OutputDataConfigModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")


class DescribeEntitiesDetectionV2JobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeICD10CMInferenceJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribePHIDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeRxNormInferenceJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DescribeSNOMEDCTInferenceJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class DetectEntitiesRequestModel(BaseModel):
    text: str = Field(alias="Text")


class DetectEntitiesV2RequestModel(BaseModel):
    text: str = Field(alias="Text")


class DetectPHIRequestModel(BaseModel):
    text: str = Field(alias="Text")


class ICD10CMTraitModel(BaseModel):
    name: Optional[
        Literal[
            "DIAGNOSIS",
            "HYPOTHETICAL",
            "LOW_CONFIDENCE",
            "NEGATION",
            "PERTAINS_TO_FAMILY",
            "SIGN",
            "SYMPTOM",
        ]
    ] = Field(default=None, alias="Name")
    score: Optional[float] = Field(default=None, alias="Score")


class ICD10CMConceptModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    code: Optional[str] = Field(default=None, alias="Code")
    score: Optional[float] = Field(default=None, alias="Score")


class InferICD10CMRequestModel(BaseModel):
    text: str = Field(alias="Text")


class InferRxNormRequestModel(BaseModel):
    text: str = Field(alias="Text")


class InferSNOMEDCTRequestModel(BaseModel):
    text: str = Field(alias="Text")


class SNOMEDCTDetailsModel(BaseModel):
    edition: Optional[str] = Field(default=None, alias="Edition")
    language: Optional[str] = Field(default=None, alias="Language")
    version_date: Optional[str] = Field(default=None, alias="VersionDate")


class RxNormTraitModel(BaseModel):
    name: Optional[Literal["NEGATION"]] = Field(default=None, alias="Name")
    score: Optional[float] = Field(default=None, alias="Score")


class RxNormConceptModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    code: Optional[str] = Field(default=None, alias="Code")
    score: Optional[float] = Field(default=None, alias="Score")


class SNOMEDCTConceptModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    code: Optional[str] = Field(default=None, alias="Code")
    score: Optional[float] = Field(default=None, alias="Score")


class SNOMEDCTTraitModel(BaseModel):
    name: Optional[
        Literal[
            "DIAGNOSIS",
            "FUTURE",
            "HYPOTHETICAL",
            "LOW_CONFIDENCE",
            "NEGATION",
            "PAST_HISTORY",
            "PERTAINS_TO_FAMILY",
            "SIGN",
            "SYMPTOM",
        ]
    ] = Field(default=None, alias="Name")
    score: Optional[float] = Field(default=None, alias="Score")


class StopEntitiesDetectionV2JobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopICD10CMInferenceJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopPHIDetectionJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopRxNormInferenceJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class StopSNOMEDCTInferenceJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class AttributeModel(BaseModel):
    type: Optional[
        Literal[
            "ACUITY",
            "ADDRESS",
            "AGE",
            "ALCOHOL_CONSUMPTION",
            "ALLERGIES",
            "AMOUNT",
            "BRAND_NAME",
            "CONTACT_POINT",
            "DATE",
            "DIRECTION",
            "DOSAGE",
            "DURATION",
            "DX_NAME",
            "EMAIL",
            "FORM",
            "FREQUENCY",
            "GENDER",
            "GENERIC_NAME",
            "ID",
            "IDENTIFIER",
            "NAME",
            "PHONE_OR_FAX",
            "PROCEDURE_NAME",
            "PROFESSION",
            "QUALITY",
            "QUANTITY",
            "RACE_ETHNICITY",
            "RATE",
            "REC_DRUG_USE",
            "ROUTE_OR_MODE",
            "STRENGTH",
            "SYSTEM_ORGAN_SITE",
            "TEST_NAME",
            "TEST_UNIT",
            "TEST_UNITS",
            "TEST_VALUE",
            "TIME_EXPRESSION",
            "TIME_TO_DX_NAME",
            "TIME_TO_MEDICATION_NAME",
            "TIME_TO_PROCEDURE_NAME",
            "TIME_TO_TEST_NAME",
            "TIME_TO_TREATMENT_NAME",
            "TOBACCO_USE",
            "TREATMENT_NAME",
            "URL",
        ]
    ] = Field(default=None, alias="Type")
    score: Optional[float] = Field(default=None, alias="Score")
    relationship_score: Optional[float] = Field(default=None, alias="RelationshipScore")
    relationship_type: Optional[
        Literal[
            "ACUITY",
            "ADMINISTERED_VIA",
            "AMOUNT",
            "DIRECTION",
            "DOSAGE",
            "DURATION",
            "EVERY",
            "FOR",
            "FORM",
            "FREQUENCY",
            "NEGATIVE",
            "OVERLAP",
            "RATE",
            "ROUTE_OR_MODE",
            "STRENGTH",
            "SYSTEM_ORGAN_SITE",
            "TEST_UNIT",
            "TEST_UNITS",
            "TEST_VALUE",
            "WITH_DOSAGE",
        ]
    ] = Field(default=None, alias="RelationshipType")
    id: Optional[int] = Field(default=None, alias="Id")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    text: Optional[str] = Field(default=None, alias="Text")
    category: Optional[
        Literal[
            "ANATOMY",
            "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
            "MEDICAL_CONDITION",
            "MEDICATION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "TIME_EXPRESSION",
        ]
    ] = Field(default=None, alias="Category")
    traits: Optional[List[TraitModel]] = Field(default=None, alias="Traits")


class ListEntitiesDetectionV2JobsRequestModel(BaseModel):
    filter: Optional[ComprehendMedicalAsyncJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListICD10CMInferenceJobsRequestModel(BaseModel):
    filter: Optional[ComprehendMedicalAsyncJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPHIDetectionJobsRequestModel(BaseModel):
    filter: Optional[ComprehendMedicalAsyncJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRxNormInferenceJobsRequestModel(BaseModel):
    filter: Optional[ComprehendMedicalAsyncJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSNOMEDCTInferenceJobsRequestModel(BaseModel):
    filter: Optional[ComprehendMedicalAsyncJobFilterModel] = Field(
        default=None, alias="Filter"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ComprehendMedicalAsyncJobPropertiesModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="JobId")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "IN_PROGRESS",
            "PARTIAL_SUCCESS",
            "STOPPED",
            "STOP_REQUESTED",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="JobStatus")
    message: Optional[str] = Field(default=None, alias="Message")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    expiration_time: Optional[datetime] = Field(default=None, alias="ExpirationTime")
    input_data_config: Optional[InputDataConfigModel] = Field(
        default=None, alias="InputDataConfig"
    )
    output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="OutputDataConfig"
    )
    language_code: Optional[Literal["en"]] = Field(default=None, alias="LanguageCode")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    manifest_file_path: Optional[str] = Field(default=None, alias="ManifestFilePath")
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")


class StartEntitiesDetectionV2JobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal["en"] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")


class StartICD10CMInferenceJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal["en"] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")


class StartPHIDetectionJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal["en"] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")


class StartRxNormInferenceJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal["en"] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")


class StartSNOMEDCTInferenceJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    language_code: Literal["en"] = Field(alias="LanguageCode")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    kms_key: Optional[str] = Field(default=None, alias="KMSKey")


class StartEntitiesDetectionV2JobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartICD10CMInferenceJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPHIDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRxNormInferenceJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSNOMEDCTInferenceJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopEntitiesDetectionV2JobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopICD10CMInferenceJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopPHIDetectionJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopRxNormInferenceJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopSNOMEDCTInferenceJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ICD10CMAttributeModel(BaseModel):
    type: Optional[
        Literal[
            "ACUITY",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
            "SYSTEM_ORGAN_SITE",
            "TIME_EXPRESSION",
            "TIME_TO_DX_NAME",
        ]
    ] = Field(default=None, alias="Type")
    score: Optional[float] = Field(default=None, alias="Score")
    relationship_score: Optional[float] = Field(default=None, alias="RelationshipScore")
    id: Optional[int] = Field(default=None, alias="Id")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    text: Optional[str] = Field(default=None, alias="Text")
    traits: Optional[List[ICD10CMTraitModel]] = Field(default=None, alias="Traits")
    category: Optional[Literal["DX_NAME", "TIME_EXPRESSION"]] = Field(
        default=None, alias="Category"
    )
    relationship_type: Optional[Literal["OVERLAP", "SYSTEM_ORGAN_SITE"]] = Field(
        default=None, alias="RelationshipType"
    )


class RxNormAttributeModel(BaseModel):
    type: Optional[
        Literal[
            "DOSAGE",
            "DURATION",
            "FORM",
            "FREQUENCY",
            "RATE",
            "ROUTE_OR_MODE",
            "STRENGTH",
        ]
    ] = Field(default=None, alias="Type")
    score: Optional[float] = Field(default=None, alias="Score")
    relationship_score: Optional[float] = Field(default=None, alias="RelationshipScore")
    id: Optional[int] = Field(default=None, alias="Id")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    text: Optional[str] = Field(default=None, alias="Text")
    traits: Optional[List[RxNormTraitModel]] = Field(default=None, alias="Traits")


class SNOMEDCTAttributeModel(BaseModel):
    category: Optional[
        Literal["ANATOMY", "MEDICAL_CONDITION", "TEST_TREATMENT_PROCEDURE"]
    ] = Field(default=None, alias="Category")
    type: Optional[
        Literal[
            "ACUITY",
            "DIRECTION",
            "QUALITY",
            "SYSTEM_ORGAN_SITE",
            "TEST_UNIT",
            "TEST_VALUE",
        ]
    ] = Field(default=None, alias="Type")
    score: Optional[float] = Field(default=None, alias="Score")
    relationship_score: Optional[float] = Field(default=None, alias="RelationshipScore")
    relationship_type: Optional[
        Literal[
            "ACUITY",
            "DIRECTION",
            "QUALITY",
            "SYSTEM_ORGAN_SITE",
            "TEST_UNITS",
            "TEST_VALUE",
        ]
    ] = Field(default=None, alias="RelationshipType")
    id: Optional[int] = Field(default=None, alias="Id")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    text: Optional[str] = Field(default=None, alias="Text")
    traits: Optional[List[SNOMEDCTTraitModel]] = Field(default=None, alias="Traits")
    s_nomedctconcepts: Optional[List[SNOMEDCTConceptModel]] = Field(
        default=None, alias="SNOMEDCTConcepts"
    )


class EntityModel(BaseModel):
    id: Optional[int] = Field(default=None, alias="Id")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    score: Optional[float] = Field(default=None, alias="Score")
    text: Optional[str] = Field(default=None, alias="Text")
    category: Optional[
        Literal[
            "ANATOMY",
            "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
            "MEDICAL_CONDITION",
            "MEDICATION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "TIME_EXPRESSION",
        ]
    ] = Field(default=None, alias="Category")
    type: Optional[
        Literal[
            "ACUITY",
            "ADDRESS",
            "AGE",
            "ALCOHOL_CONSUMPTION",
            "ALLERGIES",
            "AMOUNT",
            "BRAND_NAME",
            "CONTACT_POINT",
            "DATE",
            "DIRECTION",
            "DOSAGE",
            "DURATION",
            "DX_NAME",
            "EMAIL",
            "FORM",
            "FREQUENCY",
            "GENDER",
            "GENERIC_NAME",
            "ID",
            "IDENTIFIER",
            "NAME",
            "PHONE_OR_FAX",
            "PROCEDURE_NAME",
            "PROFESSION",
            "QUALITY",
            "QUANTITY",
            "RACE_ETHNICITY",
            "RATE",
            "REC_DRUG_USE",
            "ROUTE_OR_MODE",
            "STRENGTH",
            "SYSTEM_ORGAN_SITE",
            "TEST_NAME",
            "TEST_UNIT",
            "TEST_UNITS",
            "TEST_VALUE",
            "TIME_EXPRESSION",
            "TIME_TO_DX_NAME",
            "TIME_TO_MEDICATION_NAME",
            "TIME_TO_PROCEDURE_NAME",
            "TIME_TO_TEST_NAME",
            "TIME_TO_TREATMENT_NAME",
            "TOBACCO_USE",
            "TREATMENT_NAME",
            "URL",
        ]
    ] = Field(default=None, alias="Type")
    traits: Optional[List[TraitModel]] = Field(default=None, alias="Traits")
    attributes: Optional[List[AttributeModel]] = Field(default=None, alias="Attributes")


class UnmappedAttributeModel(BaseModel):
    type: Optional[
        Literal[
            "ANATOMY",
            "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
            "MEDICAL_CONDITION",
            "MEDICATION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "TIME_EXPRESSION",
        ]
    ] = Field(default=None, alias="Type")
    attribute: Optional[AttributeModel] = Field(default=None, alias="Attribute")


class DescribeEntitiesDetectionV2JobResponseModel(BaseModel):
    comprehend_medical_async_job_properties: ComprehendMedicalAsyncJobPropertiesModel = Field(
        alias="ComprehendMedicalAsyncJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeICD10CMInferenceJobResponseModel(BaseModel):
    comprehend_medical_async_job_properties: ComprehendMedicalAsyncJobPropertiesModel = Field(
        alias="ComprehendMedicalAsyncJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePHIDetectionJobResponseModel(BaseModel):
    comprehend_medical_async_job_properties: ComprehendMedicalAsyncJobPropertiesModel = Field(
        alias="ComprehendMedicalAsyncJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRxNormInferenceJobResponseModel(BaseModel):
    comprehend_medical_async_job_properties: ComprehendMedicalAsyncJobPropertiesModel = Field(
        alias="ComprehendMedicalAsyncJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSNOMEDCTInferenceJobResponseModel(BaseModel):
    comprehend_medical_async_job_properties: ComprehendMedicalAsyncJobPropertiesModel = Field(
        alias="ComprehendMedicalAsyncJobProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEntitiesDetectionV2JobsResponseModel(BaseModel):
    comprehend_medical_async_job_properties_list: List[
        ComprehendMedicalAsyncJobPropertiesModel
    ] = Field(alias="ComprehendMedicalAsyncJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListICD10CMInferenceJobsResponseModel(BaseModel):
    comprehend_medical_async_job_properties_list: List[
        ComprehendMedicalAsyncJobPropertiesModel
    ] = Field(alias="ComprehendMedicalAsyncJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPHIDetectionJobsResponseModel(BaseModel):
    comprehend_medical_async_job_properties_list: List[
        ComprehendMedicalAsyncJobPropertiesModel
    ] = Field(alias="ComprehendMedicalAsyncJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRxNormInferenceJobsResponseModel(BaseModel):
    comprehend_medical_async_job_properties_list: List[
        ComprehendMedicalAsyncJobPropertiesModel
    ] = Field(alias="ComprehendMedicalAsyncJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSNOMEDCTInferenceJobsResponseModel(BaseModel):
    comprehend_medical_async_job_properties_list: List[
        ComprehendMedicalAsyncJobPropertiesModel
    ] = Field(alias="ComprehendMedicalAsyncJobPropertiesList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ICD10CMEntityModel(BaseModel):
    id: Optional[int] = Field(default=None, alias="Id")
    text: Optional[str] = Field(default=None, alias="Text")
    category: Optional[Literal["MEDICAL_CONDITION"]] = Field(
        default=None, alias="Category"
    )
    type: Optional[Literal["DX_NAME", "TIME_EXPRESSION"]] = Field(
        default=None, alias="Type"
    )
    score: Optional[float] = Field(default=None, alias="Score")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    attributes: Optional[List[ICD10CMAttributeModel]] = Field(
        default=None, alias="Attributes"
    )
    traits: Optional[List[ICD10CMTraitModel]] = Field(default=None, alias="Traits")
    icd10_cmconcepts: Optional[List[ICD10CMConceptModel]] = Field(
        default=None, alias="ICD10CMConcepts"
    )


class RxNormEntityModel(BaseModel):
    id: Optional[int] = Field(default=None, alias="Id")
    text: Optional[str] = Field(default=None, alias="Text")
    category: Optional[Literal["MEDICATION"]] = Field(default=None, alias="Category")
    type: Optional[Literal["BRAND_NAME", "GENERIC_NAME"]] = Field(
        default=None, alias="Type"
    )
    score: Optional[float] = Field(default=None, alias="Score")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    attributes: Optional[List[RxNormAttributeModel]] = Field(
        default=None, alias="Attributes"
    )
    traits: Optional[List[RxNormTraitModel]] = Field(default=None, alias="Traits")
    rx_norm_concepts: Optional[List[RxNormConceptModel]] = Field(
        default=None, alias="RxNormConcepts"
    )


class SNOMEDCTEntityModel(BaseModel):
    id: Optional[int] = Field(default=None, alias="Id")
    text: Optional[str] = Field(default=None, alias="Text")
    category: Optional[
        Literal["ANATOMY", "MEDICAL_CONDITION", "TEST_TREATMENT_PROCEDURE"]
    ] = Field(default=None, alias="Category")
    type: Optional[
        Literal["DX_NAME", "PROCEDURE_NAME", "TEST_NAME", "TREATMENT_NAME"]
    ] = Field(default=None, alias="Type")
    score: Optional[float] = Field(default=None, alias="Score")
    begin_offset: Optional[int] = Field(default=None, alias="BeginOffset")
    end_offset: Optional[int] = Field(default=None, alias="EndOffset")
    attributes: Optional[List[SNOMEDCTAttributeModel]] = Field(
        default=None, alias="Attributes"
    )
    traits: Optional[List[SNOMEDCTTraitModel]] = Field(default=None, alias="Traits")
    s_nomedctconcepts: Optional[List[SNOMEDCTConceptModel]] = Field(
        default=None, alias="SNOMEDCTConcepts"
    )


class DetectPHIResponseModel(BaseModel):
    entities: List[EntityModel] = Field(alias="Entities")
    pagination_token: str = Field(alias="PaginationToken")
    model_version: str = Field(alias="ModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectEntitiesResponseModel(BaseModel):
    entities: List[EntityModel] = Field(alias="Entities")
    unmapped_attributes: List[UnmappedAttributeModel] = Field(
        alias="UnmappedAttributes"
    )
    pagination_token: str = Field(alias="PaginationToken")
    model_version: str = Field(alias="ModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectEntitiesV2ResponseModel(BaseModel):
    entities: List[EntityModel] = Field(alias="Entities")
    unmapped_attributes: List[UnmappedAttributeModel] = Field(
        alias="UnmappedAttributes"
    )
    pagination_token: str = Field(alias="PaginationToken")
    model_version: str = Field(alias="ModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InferICD10CMResponseModel(BaseModel):
    entities: List[ICD10CMEntityModel] = Field(alias="Entities")
    pagination_token: str = Field(alias="PaginationToken")
    model_version: str = Field(alias="ModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InferRxNormResponseModel(BaseModel):
    entities: List[RxNormEntityModel] = Field(alias="Entities")
    pagination_token: str = Field(alias="PaginationToken")
    model_version: str = Field(alias="ModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InferSNOMEDCTResponseModel(BaseModel):
    entities: List[SNOMEDCTEntityModel] = Field(alias="Entities")
    pagination_token: str = Field(alias="PaginationToken")
    model_version: str = Field(alias="ModelVersion")
    s_nomedctdetails: SNOMEDCTDetailsModel = Field(alias="SNOMEDCTDetails")
    characters: CharactersModel = Field(alias="Characters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
