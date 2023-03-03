# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BatchGetRecordErrorModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    record_identifier_value_as_string: str = Field(
        alias="RecordIdentifierValueAsString"
    )
    error_code: str = Field(alias="ErrorCode")
    error_message: str = Field(alias="ErrorMessage")


class BatchGetRecordIdentifierModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    record_identifiers_value_as_string: Sequence[str] = Field(
        alias="RecordIdentifiersValueAsString"
    )
    feature_names: Optional[Sequence[str]] = Field(default=None, alias="FeatureNames")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FeatureValueModel(BaseModel):
    feature_name: str = Field(alias="FeatureName")
    value_as_string: str = Field(alias="ValueAsString")


class DeleteRecordRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    record_identifier_value_as_string: str = Field(
        alias="RecordIdentifierValueAsString"
    )
    event_time: str = Field(alias="EventTime")
    target_stores: Optional[Sequence[Literal["OfflineStore", "OnlineStore"]]] = Field(
        default=None, alias="TargetStores"
    )


class GetRecordRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    record_identifier_value_as_string: str = Field(
        alias="RecordIdentifierValueAsString"
    )
    feature_names: Optional[Sequence[str]] = Field(default=None, alias="FeatureNames")


class BatchGetRecordRequestModel(BaseModel):
    identifiers: Sequence[BatchGetRecordIdentifierModel] = Field(alias="Identifiers")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetRecordResultDetailModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    record_identifier_value_as_string: str = Field(
        alias="RecordIdentifierValueAsString"
    )
    record: List[FeatureValueModel] = Field(alias="Record")


class GetRecordResponseModel(BaseModel):
    record: List[FeatureValueModel] = Field(alias="Record")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRecordRequestModel(BaseModel):
    feature_group_name: str = Field(alias="FeatureGroupName")
    record: Sequence[FeatureValueModel] = Field(alias="Record")
    target_stores: Optional[Sequence[Literal["OfflineStore", "OnlineStore"]]] = Field(
        default=None, alias="TargetStores"
    )


class BatchGetRecordResponseModel(BaseModel):
    records: List[BatchGetRecordResultDetailModel] = Field(alias="Records")
    errors: List[BatchGetRecordErrorModel] = Field(alias="Errors")
    unprocessed_identifiers: List[BatchGetRecordIdentifierModel] = Field(
        alias="UnprocessedIdentifiers"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
