# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelRotateSecretRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ReplicaRegionTypeModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="Region")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ReplicationStatusTypeModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="Region")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    status: Optional[Literal["Failed", "InProgress", "InSync"]] = Field(
        default=None, alias="Status"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    last_accessed_date: Optional[datetime] = Field(
        default=None, alias="LastAccessedDate"
    )


class DeleteResourcePolicyRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")


class DeleteSecretRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    recovery_window_in_days: Optional[int] = Field(
        default=None, alias="RecoveryWindowInDays"
    )
    force_delete_without_recovery: Optional[bool] = Field(
        default=None, alias="ForceDeleteWithoutRecovery"
    )


class DescribeSecretRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")


class RotationRulesTypeModel(BaseModel):
    automatically_after_days: Optional[int] = Field(
        default=None, alias="AutomaticallyAfterDays"
    )
    duration: Optional[str] = Field(default=None, alias="Duration")
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")


class FilterModel(BaseModel):
    key: Optional[
        Literal[
            "all",
            "description",
            "name",
            "owning-service",
            "primary-region",
            "tag-key",
            "tag-value",
        ]
    ] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class GetRandomPasswordRequestModel(BaseModel):
    password_length: Optional[int] = Field(default=None, alias="PasswordLength")
    exclude_characters: Optional[str] = Field(default=None, alias="ExcludeCharacters")
    exclude_numbers: Optional[bool] = Field(default=None, alias="ExcludeNumbers")
    exclude_punctuation: Optional[bool] = Field(
        default=None, alias="ExcludePunctuation"
    )
    exclude_uppercase: Optional[bool] = Field(default=None, alias="ExcludeUppercase")
    exclude_lowercase: Optional[bool] = Field(default=None, alias="ExcludeLowercase")
    include_space: Optional[bool] = Field(default=None, alias="IncludeSpace")
    require_each_included_type: Optional[bool] = Field(
        default=None, alias="RequireEachIncludedType"
    )


class GetResourcePolicyRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")


class GetSecretValueRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    version_stage: Optional[str] = Field(default=None, alias="VersionStage")


class ListSecretVersionIdsRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    include_deprecated: Optional[bool] = Field(default=None, alias="IncludeDeprecated")


class SecretVersionsListEntryModel(BaseModel):
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    version_stages: Optional[List[str]] = Field(default=None, alias="VersionStages")
    last_accessed_date: Optional[datetime] = Field(
        default=None, alias="LastAccessedDate"
    )
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    kms_key_ids: Optional[List[str]] = Field(default=None, alias="KmsKeyIds")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class PutResourcePolicyRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    resource_policy: str = Field(alias="ResourcePolicy")
    block_public_policy: Optional[bool] = Field(default=None, alias="BlockPublicPolicy")


class PutSecretValueRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    secret_binary: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="SecretBinary")
    secret_string: Optional[str] = Field(default=None, alias="SecretString")
    version_stages: Optional[Sequence[str]] = Field(default=None, alias="VersionStages")


class RemoveRegionsFromReplicationRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    remove_replica_regions: Sequence[str] = Field(alias="RemoveReplicaRegions")


class RestoreSecretRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")


class StopReplicationToReplicaRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")


class UntagResourceRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateSecretRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    secret_binary: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="SecretBinary")
    secret_string: Optional[str] = Field(default=None, alias="SecretString")


class UpdateSecretVersionStageRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    version_stage: str = Field(alias="VersionStage")
    remove_from_version_id: Optional[str] = Field(
        default=None, alias="RemoveFromVersionId"
    )
    move_to_version_id: Optional[str] = Field(default=None, alias="MoveToVersionId")


class ValidateResourcePolicyRequestModel(BaseModel):
    resource_policy: str = Field(alias="ResourcePolicy")
    secret_id: Optional[str] = Field(default=None, alias="SecretId")


class ValidationErrorsEntryModel(BaseModel):
    check_name: Optional[str] = Field(default=None, alias="CheckName")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class CancelRotateSecretResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    version_id: str = Field(alias="VersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResourcePolicyResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSecretResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    deletion_date: datetime = Field(alias="DeletionDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRandomPasswordResponseModel(BaseModel):
    random_password: str = Field(alias="RandomPassword")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePolicyResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    resource_policy: str = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSecretValueResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    version_id: str = Field(alias="VersionId")
    secret_binary: bytes = Field(alias="SecretBinary")
    secret_string: str = Field(alias="SecretString")
    version_stages: List[str] = Field(alias="VersionStages")
    created_date: datetime = Field(alias="CreatedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSecretValueResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    version_id: str = Field(alias="VersionId")
    version_stages: List[str] = Field(alias="VersionStages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreSecretResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RotateSecretResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    version_id: str = Field(alias="VersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopReplicationToReplicaResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSecretResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    version_id: str = Field(alias="VersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSecretVersionStageResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicateSecretToRegionsRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    add_replica_regions: Sequence[ReplicaRegionTypeModel] = Field(
        alias="AddReplicaRegions"
    )
    force_overwrite_replica_secret: Optional[bool] = Field(
        default=None, alias="ForceOverwriteReplicaSecret"
    )


class CreateSecretRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    secret_binary: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="SecretBinary")
    secret_string: Optional[str] = Field(default=None, alias="SecretString")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    add_replica_regions: Optional[Sequence[ReplicaRegionTypeModel]] = Field(
        default=None, alias="AddReplicaRegions"
    )
    force_overwrite_replica_secret: Optional[bool] = Field(
        default=None, alias="ForceOverwriteReplicaSecret"
    )


class TagResourceRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateSecretResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    version_id: str = Field(alias="VersionId")
    replication_status: List[ReplicationStatusTypeModel] = Field(
        alias="ReplicationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveRegionsFromReplicationResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    replication_status: List[ReplicationStatusTypeModel] = Field(
        alias="ReplicationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicateSecretToRegionsResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    replication_status: List[ReplicationStatusTypeModel] = Field(
        alias="ReplicationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSecretResponseModel(BaseModel):
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    kms_key_id: str = Field(alias="KmsKeyId")
    rotation_enabled: bool = Field(alias="RotationEnabled")
    rotation_lambda_arn: str = Field(alias="RotationLambdaARN")
    rotation_rules: RotationRulesTypeModel = Field(alias="RotationRules")
    last_rotated_date: datetime = Field(alias="LastRotatedDate")
    last_changed_date: datetime = Field(alias="LastChangedDate")
    last_accessed_date: datetime = Field(alias="LastAccessedDate")
    deleted_date: datetime = Field(alias="DeletedDate")
    next_rotation_date: datetime = Field(alias="NextRotationDate")
    tags: List[TagModel] = Field(alias="Tags")
    version_ids_to_stages: Dict[str, List[str]] = Field(alias="VersionIdsToStages")
    owning_service: str = Field(alias="OwningService")
    created_date: datetime = Field(alias="CreatedDate")
    primary_region: str = Field(alias="PrimaryRegion")
    replication_status: List[ReplicationStatusTypeModel] = Field(
        alias="ReplicationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RotateSecretRequestModel(BaseModel):
    secret_id: str = Field(alias="SecretId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    rotation_lambda_arn: Optional[str] = Field(default=None, alias="RotationLambdaARN")
    rotation_rules: Optional[RotationRulesTypeModel] = Field(
        default=None, alias="RotationRules"
    )
    rotate_immediately: Optional[bool] = Field(default=None, alias="RotateImmediately")


class SecretListEntryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="ARN")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    rotation_enabled: Optional[bool] = Field(default=None, alias="RotationEnabled")
    rotation_lambda_arn: Optional[str] = Field(default=None, alias="RotationLambdaARN")
    rotation_rules: Optional[RotationRulesTypeModel] = Field(
        default=None, alias="RotationRules"
    )
    last_rotated_date: Optional[datetime] = Field(default=None, alias="LastRotatedDate")
    last_changed_date: Optional[datetime] = Field(default=None, alias="LastChangedDate")
    last_accessed_date: Optional[datetime] = Field(
        default=None, alias="LastAccessedDate"
    )
    deleted_date: Optional[datetime] = Field(default=None, alias="DeletedDate")
    next_rotation_date: Optional[datetime] = Field(
        default=None, alias="NextRotationDate"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    secret_versions_to_stages: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="SecretVersionsToStages"
    )
    owning_service: Optional[str] = Field(default=None, alias="OwningService")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    primary_region: Optional[str] = Field(default=None, alias="PrimaryRegion")


class ListSecretsRequestModel(BaseModel):
    include_planned_deletion: Optional[bool] = Field(
        default=None, alias="IncludePlannedDeletion"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_order: Optional[Literal["asc", "desc"]] = Field(
        default=None, alias="SortOrder"
    )


class ListSecretVersionIdsResponseModel(BaseModel):
    versions: List[SecretVersionsListEntryModel] = Field(alias="Versions")
    next_token: str = Field(alias="NextToken")
    arn: str = Field(alias="ARN")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecretsRequestListSecretsPaginateModel(BaseModel):
    include_planned_deletion: Optional[bool] = Field(
        default=None, alias="IncludePlannedDeletion"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    sort_order: Optional[Literal["asc", "desc"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ValidateResourcePolicyResponseModel(BaseModel):
    policy_validation_passed: bool = Field(alias="PolicyValidationPassed")
    validation_errors: List[ValidationErrorsEntryModel] = Field(
        alias="ValidationErrors"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecretsResponseModel(BaseModel):
    secret_list: List[SecretListEntryModel] = Field(alias="SecretList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
