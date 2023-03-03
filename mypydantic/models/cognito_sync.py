# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BulkPublishRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CognitoStreamsModel(BaseModel):
    stream_name: Optional[str] = Field(default=None, alias="StreamName")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    streaming_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="StreamingStatus"
    )


class DatasetModel(BaseModel):
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    dataset_name: Optional[str] = Field(default=None, alias="DatasetName")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    data_storage: Optional[int] = Field(default=None, alias="DataStorage")
    num_records: Optional[int] = Field(default=None, alias="NumRecords")


class DeleteDatasetRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    dataset_name: str = Field(alias="DatasetName")


class DescribeDatasetRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    dataset_name: str = Field(alias="DatasetName")


class DescribeIdentityPoolUsageRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class IdentityPoolUsageModel(BaseModel):
    identity_pool_id: Optional[str] = Field(default=None, alias="IdentityPoolId")
    sync_sessions_count: Optional[int] = Field(default=None, alias="SyncSessionsCount")
    data_storage: Optional[int] = Field(default=None, alias="DataStorage")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )


class DescribeIdentityUsageRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")


class IdentityUsageModel(BaseModel):
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    identity_pool_id: Optional[str] = Field(default=None, alias="IdentityPoolId")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    dataset_count: Optional[int] = Field(default=None, alias="DatasetCount")
    data_storage: Optional[int] = Field(default=None, alias="DataStorage")


class GetBulkPublishDetailsRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class GetCognitoEventsRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class GetIdentityPoolConfigurationRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class PushSyncModel(BaseModel):
    application_arns: Optional[List[str]] = Field(default=None, alias="ApplicationArns")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class ListDatasetsRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIdentityPoolUsageRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRecordsRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    dataset_name: str = Field(alias="DatasetName")
    last_sync_count: Optional[int] = Field(default=None, alias="LastSyncCount")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sync_session_token: Optional[str] = Field(default=None, alias="SyncSessionToken")


class RecordModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    sync_count: Optional[int] = Field(default=None, alias="SyncCount")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )
    last_modified_by: Optional[str] = Field(default=None, alias="LastModifiedBy")
    device_last_modified_date: Optional[datetime] = Field(
        default=None, alias="DeviceLastModifiedDate"
    )


class RecordPatchModel(BaseModel):
    op: Literal["remove", "replace"] = Field(alias="Op")
    key: str = Field(alias="Key")
    sync_count: int = Field(alias="SyncCount")
    value: Optional[str] = Field(default=None, alias="Value")
    device_last_modified_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="DeviceLastModifiedDate"
    )


class RegisterDeviceRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    platform: Literal["ADM", "APNS", "APNS_SANDBOX", "GCM"] = Field(alias="Platform")
    token: str = Field(alias="Token")


class SetCognitoEventsRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    events: Mapping[str, str] = Field(alias="Events")


class SubscribeToDatasetRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    dataset_name: str = Field(alias="DatasetName")
    device_id: str = Field(alias="DeviceId")


class UnsubscribeFromDatasetRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    dataset_name: str = Field(alias="DatasetName")
    device_id: str = Field(alias="DeviceId")


class BulkPublishResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBulkPublishDetailsResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    bulk_publish_start_time: datetime = Field(alias="BulkPublishStartTime")
    bulk_publish_complete_time: datetime = Field(alias="BulkPublishCompleteTime")
    bulk_publish_status: Literal[
        "FAILED", "IN_PROGRESS", "NOT_STARTED", "SUCCEEDED"
    ] = Field(alias="BulkPublishStatus")
    failure_message: str = Field(alias="FailureMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCognitoEventsResponseModel(BaseModel):
    events: Dict[str, str] = Field(alias="Events")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterDeviceResponseModel(BaseModel):
    device_id: str = Field(alias="DeviceId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDatasetResponseModel(BaseModel):
    dataset: DatasetModel = Field(alias="Dataset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDatasetResponseModel(BaseModel):
    dataset: DatasetModel = Field(alias="Dataset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetsResponseModel(BaseModel):
    datasets: List[DatasetModel] = Field(alias="Datasets")
    count: int = Field(alias="Count")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIdentityPoolUsageResponseModel(BaseModel):
    identity_pool_usage: IdentityPoolUsageModel = Field(alias="IdentityPoolUsage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityPoolUsageResponseModel(BaseModel):
    identity_pool_usages: List[IdentityPoolUsageModel] = Field(
        alias="IdentityPoolUsages"
    )
    max_results: int = Field(alias="MaxResults")
    count: int = Field(alias="Count")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIdentityUsageResponseModel(BaseModel):
    identity_usage: IdentityUsageModel = Field(alias="IdentityUsage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIdentityPoolConfigurationResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    push_sync: PushSyncModel = Field(alias="PushSync")
    cognito_streams: CognitoStreamsModel = Field(alias="CognitoStreams")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetIdentityPoolConfigurationRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    push_sync: Optional[PushSyncModel] = Field(default=None, alias="PushSync")
    cognito_streams: Optional[CognitoStreamsModel] = Field(
        default=None, alias="CognitoStreams"
    )


class SetIdentityPoolConfigurationResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    push_sync: PushSyncModel = Field(alias="PushSync")
    cognito_streams: CognitoStreamsModel = Field(alias="CognitoStreams")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRecordsResponseModel(BaseModel):
    records: List[RecordModel] = Field(alias="Records")
    next_token: str = Field(alias="NextToken")
    count: int = Field(alias="Count")
    dataset_sync_count: int = Field(alias="DatasetSyncCount")
    last_modified_by: str = Field(alias="LastModifiedBy")
    merged_dataset_names: List[str] = Field(alias="MergedDatasetNames")
    dataset_exists: bool = Field(alias="DatasetExists")
    dataset_deleted_after_requested_sync_count: bool = Field(
        alias="DatasetDeletedAfterRequestedSyncCount"
    )
    sync_session_token: str = Field(alias="SyncSessionToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRecordsResponseModel(BaseModel):
    records: List[RecordModel] = Field(alias="Records")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRecordsRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: str = Field(alias="IdentityId")
    dataset_name: str = Field(alias="DatasetName")
    sync_session_token: str = Field(alias="SyncSessionToken")
    device_id: Optional[str] = Field(default=None, alias="DeviceId")
    record_patches: Optional[Sequence[RecordPatchModel]] = Field(
        default=None, alias="RecordPatches"
    )
    client_context: Optional[str] = Field(default=None, alias="ClientContext")
