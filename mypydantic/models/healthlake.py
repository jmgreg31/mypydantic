# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class PreloadDataConfigModel(BaseModel):
    preload_data_type: Literal["SYNTHEA"] = Field(alias="PreloadDataType")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DatastoreFilterModel(BaseModel):
    datastore_name: Optional[str] = Field(default=None, alias="DatastoreName")
    datastore_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETED", "DELETING"]
    ] = Field(default=None, alias="DatastoreStatus")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )


class DeleteFHIRDatastoreRequestModel(BaseModel):
    datastore_id: Optional[str] = Field(default=None, alias="DatastoreId")


class DescribeFHIRDatastoreRequestModel(BaseModel):
    datastore_id: Optional[str] = Field(default=None, alias="DatastoreId")


class DescribeFHIRExportJobRequestModel(BaseModel):
    datastore_id: str = Field(alias="DatastoreId")
    job_id: str = Field(alias="JobId")


class DescribeFHIRImportJobRequestModel(BaseModel):
    datastore_id: str = Field(alias="DatastoreId")
    job_id: str = Field(alias="JobId")


class InputDataConfigModel(BaseModel):
    s3_uri: Optional[str] = Field(default=None, alias="S3Uri")


class KmsEncryptionConfigModel(BaseModel):
    cmk_type: Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_MANAGED_KMS_KEY"] = Field(
        alias="CmkType"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class ListFHIRExportJobsRequestModel(BaseModel):
    datastore_id: str = Field(alias="DatastoreId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    submitted_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedBefore"
    )
    submitted_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedAfter"
    )


class ListFHIRImportJobsRequestModel(BaseModel):
    datastore_id: str = Field(alias="DatastoreId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    job_status: Optional[
        Literal[
            "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
        ]
    ] = Field(default=None, alias="JobStatus")
    submitted_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedBefore"
    )
    submitted_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="SubmittedAfter"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class S3ConfigurationModel(BaseModel):
    s3_uri: str = Field(alias="S3Uri")
    kms_key_id: str = Field(alias="KmsKeyId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateFHIRDatastoreResponseModel(BaseModel):
    datastore_id: str = Field(alias="DatastoreId")
    datastore_arn: str = Field(alias="DatastoreArn")
    datastore_status: Literal["ACTIVE", "CREATING", "DELETED", "DELETING"] = Field(
        alias="DatastoreStatus"
    )
    datastore_endpoint: str = Field(alias="DatastoreEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFHIRDatastoreResponseModel(BaseModel):
    datastore_id: str = Field(alias="DatastoreId")
    datastore_arn: str = Field(alias="DatastoreArn")
    datastore_status: Literal["ACTIVE", "CREATING", "DELETED", "DELETING"] = Field(
        alias="DatastoreStatus"
    )
    datastore_endpoint: str = Field(alias="DatastoreEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFHIRExportJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
    ] = Field(alias="JobStatus")
    datastore_id: str = Field(alias="DatastoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFHIRImportJobResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
    ] = Field(alias="JobStatus")
    datastore_id: str = Field(alias="DatastoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFHIRDatastoresRequestModel(BaseModel):
    filter: Optional[DatastoreFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SseConfigurationModel(BaseModel):
    kms_encryption_config: KmsEncryptionConfigModel = Field(alias="KmsEncryptionConfig")


class OutputDataConfigModel(BaseModel):
    s3_configuration: Optional[S3ConfigurationModel] = Field(
        default=None, alias="S3Configuration"
    )


class CreateFHIRDatastoreRequestModel(BaseModel):
    datastore_type_version: Literal["R4"] = Field(alias="DatastoreTypeVersion")
    datastore_name: Optional[str] = Field(default=None, alias="DatastoreName")
    sse_configuration: Optional[SseConfigurationModel] = Field(
        default=None, alias="SseConfiguration"
    )
    preload_data_config: Optional[PreloadDataConfigModel] = Field(
        default=None, alias="PreloadDataConfig"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DatastorePropertiesModel(BaseModel):
    datastore_id: str = Field(alias="DatastoreId")
    datastore_arn: str = Field(alias="DatastoreArn")
    datastore_status: Literal["ACTIVE", "CREATING", "DELETED", "DELETING"] = Field(
        alias="DatastoreStatus"
    )
    datastore_type_version: Literal["R4"] = Field(alias="DatastoreTypeVersion")
    datastore_endpoint: str = Field(alias="DatastoreEndpoint")
    datastore_name: Optional[str] = Field(default=None, alias="DatastoreName")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    sse_configuration: Optional[SseConfigurationModel] = Field(
        default=None, alias="SseConfiguration"
    )
    preload_data_config: Optional[PreloadDataConfigModel] = Field(
        default=None, alias="PreloadDataConfig"
    )


class ExportJobPropertiesModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
    ] = Field(alias="JobStatus")
    submit_time: datetime = Field(alias="SubmitTime")
    datastore_id: str = Field(alias="DatastoreId")
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    message: Optional[str] = Field(default=None, alias="Message")


class ImportJobPropertiesModel(BaseModel):
    job_id: str = Field(alias="JobId")
    job_status: Literal[
        "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "IN_PROGRESS", "SUBMITTED"
    ] = Field(alias="JobStatus")
    submit_time: datetime = Field(alias="SubmitTime")
    datastore_id: str = Field(alias="DatastoreId")
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    job_name: Optional[str] = Field(default=None, alias="JobName")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    job_output_data_config: Optional[OutputDataConfigModel] = Field(
        default=None, alias="JobOutputDataConfig"
    )
    data_access_role_arn: Optional[str] = Field(default=None, alias="DataAccessRoleArn")
    message: Optional[str] = Field(default=None, alias="Message")


class StartFHIRExportJobRequestModel(BaseModel):
    output_data_config: OutputDataConfigModel = Field(alias="OutputDataConfig")
    datastore_id: str = Field(alias="DatastoreId")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    client_token: str = Field(alias="ClientToken")
    job_name: Optional[str] = Field(default=None, alias="JobName")


class StartFHIRImportJobRequestModel(BaseModel):
    input_data_config: InputDataConfigModel = Field(alias="InputDataConfig")
    job_output_data_config: OutputDataConfigModel = Field(alias="JobOutputDataConfig")
    datastore_id: str = Field(alias="DatastoreId")
    data_access_role_arn: str = Field(alias="DataAccessRoleArn")
    client_token: str = Field(alias="ClientToken")
    job_name: Optional[str] = Field(default=None, alias="JobName")


class DescribeFHIRDatastoreResponseModel(BaseModel):
    datastore_properties: DatastorePropertiesModel = Field(alias="DatastoreProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFHIRDatastoresResponseModel(BaseModel):
    datastore_properties_list: List[DatastorePropertiesModel] = Field(
        alias="DatastorePropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFHIRExportJobResponseModel(BaseModel):
    export_job_properties: ExportJobPropertiesModel = Field(alias="ExportJobProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFHIRExportJobsResponseModel(BaseModel):
    export_job_properties_list: List[ExportJobPropertiesModel] = Field(
        alias="ExportJobPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFHIRImportJobResponseModel(BaseModel):
    import_job_properties: ImportJobPropertiesModel = Field(alias="ImportJobProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFHIRImportJobsResponseModel(BaseModel):
    import_job_properties_list: List[ImportJobPropertiesModel] = Field(
        alias="ImportJobPropertiesList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
