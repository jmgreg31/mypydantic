# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Set, Union

from boto3.dynamodb.conditions import ConditionBase
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ArchivalSummaryTableModel(BaseModel):
    archival_date_time: Optional[datetime] = Field(
        default=None, alias="ArchivalDateTime"
    )
    archival_reason: Optional[str] = Field(default=None, alias="ArchivalReason")
    archival_backup_arn: Optional[str] = Field(default=None, alias="ArchivalBackupArn")


class ArchivalSummaryModel(BaseModel):
    archival_date_time: Optional[datetime] = Field(
        default=None, alias="ArchivalDateTime"
    )
    archival_reason: Optional[str] = Field(default=None, alias="ArchivalReason")
    archival_backup_arn: Optional[str] = Field(default=None, alias="ArchivalBackupArn")


class AttributeDefinitionServiceResourceModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    attribute_type: Literal["B", "N", "S"] = Field(alias="AttributeType")


class AttributeDefinitionTableModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    attribute_type: Literal["B", "N", "S"] = Field(alias="AttributeType")


class AttributeDefinitionModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    attribute_type: Literal["B", "N", "S"] = Field(alias="AttributeType")


class AttributeValueModel(BaseModel):
    s: Optional[str] = Field(default=None, alias="S")
    n: Optional[str] = Field(default=None, alias="N")
    b: Optional[bytes] = Field(default=None, alias="B")
    s_s: Optional[Sequence[str]] = Field(default=None, alias="SS")
    ns: Optional[Sequence[str]] = Field(default=None, alias="NS")
    bs: Optional[Sequence[bytes]] = Field(default=None, alias="BS")
    m: Optional[Mapping[str, Any]] = Field(default=None, alias="M")
    l: Optional[Sequence[Any]] = Field(default=None, alias="L")
    nul_l: Optional[bool] = Field(default=None, alias="NULL")
    bool: Optional[bool] = Field(default=None, alias="BOOL")


class AttributeValueUpdateTableModel(BaseModel):
    value: Optional[
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ]
    ] = Field(default=None, alias="Value")
    action: Optional[Literal["ADD", "DELETE", "PUT"]] = Field(
        default=None, alias="Action"
    )


class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionModel(BaseModel):
    target_value: float = Field(alias="TargetValue")
    disable_scale_in: Optional[bool] = Field(default=None, alias="DisableScaleIn")
    scale_in_cooldown: Optional[int] = Field(default=None, alias="ScaleInCooldown")
    scale_out_cooldown: Optional[int] = Field(default=None, alias="ScaleOutCooldown")


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateModel(BaseModel):
    target_value: float = Field(alias="TargetValue")
    disable_scale_in: Optional[bool] = Field(default=None, alias="DisableScaleIn")
    scale_in_cooldown: Optional[int] = Field(default=None, alias="ScaleInCooldown")
    scale_out_cooldown: Optional[int] = Field(default=None, alias="ScaleOutCooldown")


class BackupDetailsModel(BaseModel):
    backup_arn: str = Field(alias="BackupArn")
    backup_name: str = Field(alias="BackupName")
    backup_status: Literal["AVAILABLE", "CREATING", "DELETED"] = Field(
        alias="BackupStatus"
    )
    backup_type: Literal["AWS_BACKUP", "SYSTEM", "USER"] = Field(alias="BackupType")
    backup_creation_date_time: datetime = Field(alias="BackupCreationDateTime")
    backup_size_bytes: Optional[int] = Field(default=None, alias="BackupSizeBytes")
    backup_expiry_date_time: Optional[datetime] = Field(
        default=None, alias="BackupExpiryDateTime"
    )


class BackupSummaryTableModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    table_id: Optional[str] = Field(default=None, alias="TableId")
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    backup_arn: Optional[str] = Field(default=None, alias="BackupArn")
    backup_name: Optional[str] = Field(default=None, alias="BackupName")
    backup_creation_date_time: Optional[datetime] = Field(
        default=None, alias="BackupCreationDateTime"
    )
    backup_expiry_date_time: Optional[datetime] = Field(
        default=None, alias="BackupExpiryDateTime"
    )
    backup_status: Optional[Literal["AVAILABLE", "CREATING", "DELETED"]] = Field(
        default=None, alias="BackupStatus"
    )
    backup_type: Optional[Literal["AWS_BACKUP", "SYSTEM", "USER"]] = Field(
        default=None, alias="BackupType"
    )
    backup_size_bytes: Optional[int] = Field(default=None, alias="BackupSizeBytes")


class BackupSummaryModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    table_id: Optional[str] = Field(default=None, alias="TableId")
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    backup_arn: Optional[str] = Field(default=None, alias="BackupArn")
    backup_name: Optional[str] = Field(default=None, alias="BackupName")
    backup_creation_date_time: Optional[datetime] = Field(
        default=None, alias="BackupCreationDateTime"
    )
    backup_expiry_date_time: Optional[datetime] = Field(
        default=None, alias="BackupExpiryDateTime"
    )
    backup_status: Optional[Literal["AVAILABLE", "CREATING", "DELETED"]] = Field(
        default=None, alias="BackupStatus"
    )
    backup_type: Optional[Literal["AWS_BACKUP", "SYSTEM", "USER"]] = Field(
        default=None, alias="BackupType"
    )
    backup_size_bytes: Optional[int] = Field(default=None, alias="BackupSizeBytes")


class KeysAndAttributesServiceResourceModel(BaseModel):
    keys: Sequence[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(alias="Keys")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )


class BatchStatementErrorModel(BaseModel):
    code: Optional[
        Literal[
            "AccessDenied",
            "ConditionalCheckFailed",
            "DuplicateItem",
            "InternalServerError",
            "ItemCollectionSizeLimitExceeded",
            "ProvisionedThroughputExceeded",
            "RequestLimitExceeded",
            "ResourceNotFound",
            "ThrottlingError",
            "TransactionConflict",
            "ValidationError",
        ]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class ItemCollectionMetricsServiceResourceModel(BaseModel):
    item_collection_key: Optional[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ItemCollectionKey")
    size_estimate_range_gb: Optional[List[float]] = Field(
        default=None, alias="SizeEstimateRangeGB"
    )


class BillingModeSummaryTableModel(BaseModel):
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )
    last_update_to_pay_per_request_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdateToPayPerRequestDateTime"
    )


class BillingModeSummaryModel(BaseModel):
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )
    last_update_to_pay_per_request_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdateToPayPerRequestDateTime"
    )


class CapacityServiceResourceModel(BaseModel):
    read_capacity_units: Optional[float] = Field(
        default=None, alias="ReadCapacityUnits"
    )
    write_capacity_units: Optional[float] = Field(
        default=None, alias="WriteCapacityUnits"
    )
    capacity_units: Optional[float] = Field(default=None, alias="CapacityUnits")


class CapacityTableModel(BaseModel):
    read_capacity_units: Optional[float] = Field(
        default=None, alias="ReadCapacityUnits"
    )
    write_capacity_units: Optional[float] = Field(
        default=None, alias="WriteCapacityUnits"
    )
    capacity_units: Optional[float] = Field(default=None, alias="CapacityUnits")


class CapacityModel(BaseModel):
    read_capacity_units: Optional[float] = Field(
        default=None, alias="ReadCapacityUnits"
    )
    write_capacity_units: Optional[float] = Field(
        default=None, alias="WriteCapacityUnits"
    )
    capacity_units: Optional[float] = Field(default=None, alias="CapacityUnits")


class ConditionTableModel(BaseModel):
    comparison_operator: Literal[
        "BEGINS_WITH",
        "BETWEEN",
        "CONTAINS",
        "EQ",
        "GE",
        "GT",
        "IN",
        "LE",
        "LT",
        "NE",
        "NOT_CONTAINS",
        "NOT_NULL",
        "NULL",
    ] = Field(alias="ComparisonOperator")
    attribute_value_list: Optional[
        Sequence[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ]
    ] = Field(default=None, alias="AttributeValueList")


class PointInTimeRecoveryDescriptionModel(BaseModel):
    point_in_time_recovery_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="PointInTimeRecoveryStatus"
    )
    earliest_restorable_date_time: Optional[datetime] = Field(
        default=None, alias="EarliestRestorableDateTime"
    )
    latest_restorable_date_time: Optional[datetime] = Field(
        default=None, alias="LatestRestorableDateTime"
    )


class ContributorInsightsSummaryModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    contributor_insights_status: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "FAILED"]
    ] = Field(default=None, alias="ContributorInsightsStatus")


class CreateBackupInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    backup_name: str = Field(alias="BackupName")


class KeySchemaElementTableModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    key_type: Literal["HASH", "RANGE"] = Field(alias="KeyType")


class ProjectionTableModel(BaseModel):
    projection_type: Optional[Literal["ALL", "INCLUDE", "KEYS_ONLY"]] = Field(
        default=None, alias="ProjectionType"
    )
    non_key_attributes: Optional[List[str]] = Field(
        default=None, alias="NonKeyAttributes"
    )


class ProvisionedThroughputTableModel(BaseModel):
    read_capacity_units: int = Field(alias="ReadCapacityUnits")
    write_capacity_units: int = Field(alias="WriteCapacityUnits")


class KeySchemaElementModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    key_type: Literal["HASH", "RANGE"] = Field(alias="KeyType")


class ProjectionModel(BaseModel):
    projection_type: Optional[Literal["ALL", "INCLUDE", "KEYS_ONLY"]] = Field(
        default=None, alias="ProjectionType"
    )
    non_key_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="NonKeyAttributes"
    )


class ProvisionedThroughputModel(BaseModel):
    read_capacity_units: int = Field(alias="ReadCapacityUnits")
    write_capacity_units: int = Field(alias="WriteCapacityUnits")


class ReplicaModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")


class CreateReplicaActionModel(BaseModel):
    region_name: str = Field(alias="RegionName")


class ProvisionedThroughputOverrideTableModel(BaseModel):
    read_capacity_units: Optional[int] = Field(default=None, alias="ReadCapacityUnits")


class ProvisionedThroughputOverrideModel(BaseModel):
    read_capacity_units: Optional[int] = Field(default=None, alias="ReadCapacityUnits")


class SSESpecificationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    s_s_etype: Optional[Literal["AES256", "KMS"]] = Field(default=None, alias="SSEType")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")


class StreamSpecificationModel(BaseModel):
    stream_enabled: bool = Field(alias="StreamEnabled")
    stream_view_type: Optional[
        Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
    ] = Field(default=None, alias="StreamViewType")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class KeySchemaElementServiceResourceModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    key_type: Literal["HASH", "RANGE"] = Field(alias="KeyType")


class ProvisionedThroughputServiceResourceModel(BaseModel):
    read_capacity_units: int = Field(alias="ReadCapacityUnits")
    write_capacity_units: int = Field(alias="WriteCapacityUnits")


class SSESpecificationServiceResourceModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    s_s_etype: Optional[Literal["AES256", "KMS"]] = Field(default=None, alias="SSEType")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")


class StreamSpecificationServiceResourceModel(BaseModel):
    stream_enabled: bool = Field(alias="StreamEnabled")
    stream_view_type: Optional[
        Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
    ] = Field(default=None, alias="StreamViewType")


class TagServiceResourceModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CsvOptionsModel(BaseModel):
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    header_list: Optional[List[str]] = Field(default=None, alias="HeaderList")


class DeleteBackupInputRequestModel(BaseModel):
    backup_arn: str = Field(alias="BackupArn")


class DeleteGlobalSecondaryIndexActionTableModel(BaseModel):
    index_name: str = Field(alias="IndexName")


class DeleteGlobalSecondaryIndexActionModel(BaseModel):
    index_name: str = Field(alias="IndexName")


class ExpectedAttributeValueTableModel(BaseModel):
    value: Optional[
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ]
    ] = Field(default=None, alias="Value")
    exists: Optional[bool] = Field(default=None, alias="Exists")
    comparison_operator: Optional[
        Literal[
            "BEGINS_WITH",
            "BETWEEN",
            "CONTAINS",
            "EQ",
            "GE",
            "GT",
            "IN",
            "LE",
            "LT",
            "NE",
            "NOT_CONTAINS",
            "NOT_NULL",
            "NULL",
        ]
    ] = Field(default=None, alias="ComparisonOperator")
    attribute_value_list: Optional[
        Sequence[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ]
    ] = Field(default=None, alias="AttributeValueList")


class ItemCollectionMetricsTableModel(BaseModel):
    item_collection_key: Optional[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ItemCollectionKey")
    size_estimate_range_gb: Optional[List[float]] = Field(
        default=None, alias="SizeEstimateRangeGB"
    )


class DeleteReplicaActionModel(BaseModel):
    region_name: str = Field(alias="RegionName")


class DeleteReplicationGroupMemberActionTableModel(BaseModel):
    region_name: str = Field(alias="RegionName")


class DeleteReplicationGroupMemberActionModel(BaseModel):
    region_name: str = Field(alias="RegionName")


class DeleteRequestServiceResourceModel(BaseModel):
    key: Mapping[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")


class DeleteTableInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")


class DescribeBackupInputRequestModel(BaseModel):
    backup_arn: str = Field(alias="BackupArn")


class DescribeContinuousBackupsInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")


class DescribeContributorInsightsInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    index_name: Optional[str] = Field(default=None, alias="IndexName")


class FailureExceptionModel(BaseModel):
    exception_name: Optional[str] = Field(default=None, alias="ExceptionName")
    exception_description: Optional[str] = Field(
        default=None, alias="ExceptionDescription"
    )


class EndpointModel(BaseModel):
    address: str = Field(alias="Address")
    cache_period_in_minutes: int = Field(alias="CachePeriodInMinutes")


class DescribeExportInputRequestModel(BaseModel):
    export_arn: str = Field(alias="ExportArn")


class ExportDescriptionModel(BaseModel):
    export_arn: Optional[str] = Field(default=None, alias="ExportArn")
    export_status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="ExportStatus"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    export_manifest: Optional[str] = Field(default=None, alias="ExportManifest")
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    table_id: Optional[str] = Field(default=None, alias="TableId")
    export_time: Optional[datetime] = Field(default=None, alias="ExportTime")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_bucket_owner: Optional[str] = Field(default=None, alias="S3BucketOwner")
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")
    s3_sse_algorithm: Optional[Literal["AES256", "KMS"]] = Field(
        default=None, alias="S3SseAlgorithm"
    )
    s3_sse_kms_key_id: Optional[str] = Field(default=None, alias="S3SseKmsKeyId")
    failure_code: Optional[str] = Field(default=None, alias="FailureCode")
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")
    export_format: Optional[Literal["DYNAMODB_JSON", "ION"]] = Field(
        default=None, alias="ExportFormat"
    )
    billed_size_bytes: Optional[int] = Field(default=None, alias="BilledSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")


class DescribeGlobalTableInputRequestModel(BaseModel):
    global_table_name: str = Field(alias="GlobalTableName")


class DescribeGlobalTableSettingsInputRequestModel(BaseModel):
    global_table_name: str = Field(alias="GlobalTableName")


class DescribeImportInputRequestModel(BaseModel):
    import_arn: str = Field(alias="ImportArn")


class DescribeKinesisStreamingDestinationInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")


class KinesisDataStreamDestinationModel(BaseModel):
    stream_arn: Optional[str] = Field(default=None, alias="StreamArn")
    destination_status: Optional[
        Literal["ACTIVE", "DISABLED", "DISABLING", "ENABLE_FAILED", "ENABLING"]
    ] = Field(default=None, alias="DestinationStatus")
    destination_status_description: Optional[str] = Field(
        default=None, alias="DestinationStatusDescription"
    )


class DescribeTableInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeTableReplicaAutoScalingInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")


class DescribeTimeToLiveInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")


class TimeToLiveDescriptionModel(BaseModel):
    time_to_live_status: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
    ] = Field(default=None, alias="TimeToLiveStatus")
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")


class ExportSummaryModel(BaseModel):
    export_arn: Optional[str] = Field(default=None, alias="ExportArn")
    export_status: Optional[Literal["COMPLETED", "FAILED", "IN_PROGRESS"]] = Field(
        default=None, alias="ExportStatus"
    )


class ExportTableToPointInTimeInputRequestModel(BaseModel):
    table_arn: str = Field(alias="TableArn")
    s3_bucket: str = Field(alias="S3Bucket")
    export_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ExportTime"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    s3_bucket_owner: Optional[str] = Field(default=None, alias="S3BucketOwner")
    s3_prefix: Optional[str] = Field(default=None, alias="S3Prefix")
    s3_sse_algorithm: Optional[Literal["AES256", "KMS"]] = Field(
        default=None, alias="S3SseAlgorithm"
    )
    s3_sse_kms_key_id: Optional[str] = Field(default=None, alias="S3SseKmsKeyId")
    export_format: Optional[Literal["DYNAMODB_JSON", "ION"]] = Field(
        default=None, alias="ExportFormat"
    )


class GetItemInputTableGetItemModel(BaseModel):
    key: Mapping[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )


class ProvisionedThroughputDescriptionTableModel(BaseModel):
    last_increase_date_time: Optional[datetime] = Field(
        default=None, alias="LastIncreaseDateTime"
    )
    last_decrease_date_time: Optional[datetime] = Field(
        default=None, alias="LastDecreaseDateTime"
    )
    number_of_decreases_today: Optional[int] = Field(
        default=None, alias="NumberOfDecreasesToday"
    )
    read_capacity_units: Optional[int] = Field(default=None, alias="ReadCapacityUnits")
    write_capacity_units: Optional[int] = Field(
        default=None, alias="WriteCapacityUnits"
    )


class ProvisionedThroughputDescriptionModel(BaseModel):
    last_increase_date_time: Optional[datetime] = Field(
        default=None, alias="LastIncreaseDateTime"
    )
    last_decrease_date_time: Optional[datetime] = Field(
        default=None, alias="LastDecreaseDateTime"
    )
    number_of_decreases_today: Optional[int] = Field(
        default=None, alias="NumberOfDecreasesToday"
    )
    read_capacity_units: Optional[int] = Field(default=None, alias="ReadCapacityUnits")
    write_capacity_units: Optional[int] = Field(
        default=None, alias="WriteCapacityUnits"
    )


class ProjectionServiceResourceModel(BaseModel):
    projection_type: Optional[Literal["ALL", "INCLUDE", "KEYS_ONLY"]] = Field(
        default=None, alias="ProjectionType"
    )
    non_key_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="NonKeyAttributes"
    )


class S3BucketSourceModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")
    s3_bucket_owner: Optional[str] = Field(default=None, alias="S3BucketOwner")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")


class KinesisStreamingDestinationInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    stream_arn: str = Field(alias="StreamArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBackupsInputRequestModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    time_range_lower_bound: Optional[Union[datetime, str]] = Field(
        default=None, alias="TimeRangeLowerBound"
    )
    time_range_upper_bound: Optional[Union[datetime, str]] = Field(
        default=None, alias="TimeRangeUpperBound"
    )
    exclusive_start_backup_arn: Optional[str] = Field(
        default=None, alias="ExclusiveStartBackupArn"
    )
    backup_type: Optional[Literal["ALL", "AWS_BACKUP", "SYSTEM", "USER"]] = Field(
        default=None, alias="BackupType"
    )


class ListContributorInsightsInputRequestModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListExportsInputRequestModel(BaseModel):
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGlobalTablesInputRequestModel(BaseModel):
    exclusive_start_global_table_name: Optional[str] = Field(
        default=None, alias="ExclusiveStartGlobalTableName"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    region_name: Optional[str] = Field(default=None, alias="RegionName")


class ListImportsInputRequestModel(BaseModel):
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTablesInputRequestModel(BaseModel):
    exclusive_start_table_name: Optional[str] = Field(
        default=None, alias="ExclusiveStartTableName"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListTagsOfResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TagTableModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class PointInTimeRecoverySpecificationModel(BaseModel):
    point_in_time_recovery_enabled: bool = Field(alias="PointInTimeRecoveryEnabled")


class PutRequestServiceResourceModel(BaseModel):
    item: Mapping[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Item")


class TableClassSummaryTableModel(BaseModel):
    table_class: Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]] = Field(
        default=None, alias="TableClass"
    )
    last_update_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdateDateTime"
    )


class TableClassSummaryModel(BaseModel):
    table_class: Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]] = Field(
        default=None, alias="TableClass"
    )
    last_update_date_time: Optional[datetime] = Field(
        default=None, alias="LastUpdateDateTime"
    )


class RestoreSummaryTableModel(BaseModel):
    restore_date_time: datetime = Field(alias="RestoreDateTime")
    restore_in_progress: bool = Field(alias="RestoreInProgress")
    source_backup_arn: Optional[str] = Field(default=None, alias="SourceBackupArn")
    source_table_arn: Optional[str] = Field(default=None, alias="SourceTableArn")


class RestoreSummaryModel(BaseModel):
    restore_date_time: datetime = Field(alias="RestoreDateTime")
    restore_in_progress: bool = Field(alias="RestoreInProgress")
    source_backup_arn: Optional[str] = Field(default=None, alias="SourceBackupArn")
    source_table_arn: Optional[str] = Field(default=None, alias="SourceTableArn")


class SSEDescriptionTableModel(BaseModel):
    status: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "UPDATING"]
    ] = Field(default=None, alias="Status")
    s_s_etype: Optional[Literal["AES256", "KMS"]] = Field(default=None, alias="SSEType")
    kms_master_key_arn: Optional[str] = Field(default=None, alias="KMSMasterKeyArn")
    inaccessible_encryption_date_time: Optional[datetime] = Field(
        default=None, alias="InaccessibleEncryptionDateTime"
    )


class SSEDescriptionModel(BaseModel):
    status: Optional[
        Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "UPDATING"]
    ] = Field(default=None, alias="Status")
    s_s_etype: Optional[Literal["AES256", "KMS"]] = Field(default=None, alias="SSEType")
    kms_master_key_arn: Optional[str] = Field(default=None, alias="KMSMasterKeyArn")
    inaccessible_encryption_date_time: Optional[datetime] = Field(
        default=None, alias="InaccessibleEncryptionDateTime"
    )


class SSESpecificationTableModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    s_s_etype: Optional[Literal["AES256", "KMS"]] = Field(default=None, alias="SSEType")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")


class ServiceResourceTableRequestModel(BaseModel):
    name: str = Field(alias="name")


class StreamSpecificationTableModel(BaseModel):
    stream_enabled: bool = Field(alias="StreamEnabled")
    stream_view_type: Optional[
        Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
    ] = Field(default=None, alias="StreamViewType")


class TableBatchWriterRequestModel(BaseModel):
    overwrite_by_pkeys: Optional[List[str]] = Field(
        default=None, alias="overwrite_by_pkeys"
    )


class TimeToLiveSpecificationModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    attribute_name: str = Field(alias="AttributeName")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateContributorInsightsInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    contributor_insights_action: Literal["DISABLE", "ENABLE"] = Field(
        alias="ContributorInsightsAction"
    )
    index_name: Optional[str] = Field(default=None, alias="IndexName")


class ArchivalSummaryResponseMetadataModel(BaseModel):
    archival_date_time: datetime = Field(alias="ArchivalDateTime")
    archival_reason: str = Field(alias="ArchivalReason")
    archival_backup_arn: str = Field(alias="ArchivalBackupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BillingModeSummaryResponseMetadataModel(BaseModel):
    billing_mode: Literal["PAY_PER_REQUEST", "PROVISIONED"] = Field(alias="BillingMode")
    last_update_to_pay_per_request_date_time: datetime = Field(
        alias="LastUpdateToPayPerRequestDateTime"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeLimitsOutputModel(BaseModel):
    account_max_read_capacity_units: int = Field(alias="AccountMaxReadCapacityUnits")
    account_max_write_capacity_units: int = Field(alias="AccountMaxWriteCapacityUnits")
    table_max_read_capacity_units: int = Field(alias="TableMaxReadCapacityUnits")
    table_max_write_capacity_units: int = Field(alias="TableMaxWriteCapacityUnits")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class KinesisStreamingDestinationOutputModel(BaseModel):
    table_name: str = Field(alias="TableName")
    stream_arn: str = Field(alias="StreamArn")
    destination_status: Literal[
        "ACTIVE", "DISABLED", "DISABLING", "ENABLE_FAILED", "ENABLING"
    ] = Field(alias="DestinationStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTablesOutputTableModel(BaseModel):
    table_names: List[str] = Field(alias="TableNames")
    last_evaluated_table_name: str = Field(alias="LastEvaluatedTableName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTablesOutputModel(BaseModel):
    table_names: List[str] = Field(alias="TableNames")
    last_evaluated_table_name: str = Field(alias="LastEvaluatedTableName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisionedThroughputDescriptionResponseMetadataModel(BaseModel):
    last_increase_date_time: datetime = Field(alias="LastIncreaseDateTime")
    last_decrease_date_time: datetime = Field(alias="LastDecreaseDateTime")
    number_of_decreases_today: int = Field(alias="NumberOfDecreasesToday")
    read_capacity_units: int = Field(alias="ReadCapacityUnits")
    write_capacity_units: int = Field(alias="WriteCapacityUnits")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreSummaryResponseMetadataModel(BaseModel):
    source_backup_arn: str = Field(alias="SourceBackupArn")
    source_table_arn: str = Field(alias="SourceTableArn")
    restore_date_time: datetime = Field(alias="RestoreDateTime")
    restore_in_progress: bool = Field(alias="RestoreInProgress")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SSEDescriptionResponseMetadataModel(BaseModel):
    status: Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "UPDATING"] = Field(
        alias="Status"
    )
    s_s_etype: Literal["AES256", "KMS"] = Field(alias="SSEType")
    kms_master_key_arn: str = Field(alias="KMSMasterKeyArn")
    inaccessible_encryption_date_time: datetime = Field(
        alias="InaccessibleEncryptionDateTime"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamSpecificationResponseMetadataModel(BaseModel):
    stream_enabled: bool = Field(alias="StreamEnabled")
    stream_view_type: Literal[
        "KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"
    ] = Field(alias="StreamViewType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TableClassSummaryResponseMetadataModel(BaseModel):
    table_class: Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"] = Field(
        alias="TableClass"
    )
    last_update_date_time: datetime = Field(alias="LastUpdateDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContributorInsightsOutputModel(BaseModel):
    table_name: str = Field(alias="TableName")
    index_name: str = Field(alias="IndexName")
    contributor_insights_status: Literal[
        "DISABLED", "DISABLING", "ENABLED", "ENABLING", "FAILED"
    ] = Field(alias="ContributorInsightsStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttributeValueUpdateModel(BaseModel):
    value: Optional[
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ]
    ] = Field(default=None, alias="Value")
    action: Optional[Literal["ADD", "DELETE", "PUT"]] = Field(
        default=None, alias="Action"
    )


class BatchStatementRequestModel(BaseModel):
    statement: str = Field(alias="Statement")
    parameters: Optional[
        Sequence[
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ]
    ] = Field(default=None, alias="Parameters")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")


class ConditionCheckModel(BaseModel):
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    table_name: str = Field(alias="TableName")
    condition_expression: str = Field(alias="ConditionExpression")
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    return_values_on_condition_check_failure: Optional[
        Literal["ALL_OLD", "NONE"]
    ] = Field(default=None, alias="ReturnValuesOnConditionCheckFailure")


class ConditionModel(BaseModel):
    comparison_operator: Literal[
        "BEGINS_WITH",
        "BETWEEN",
        "CONTAINS",
        "EQ",
        "GE",
        "GT",
        "IN",
        "LE",
        "LT",
        "NE",
        "NOT_CONTAINS",
        "NOT_NULL",
        "NULL",
    ] = Field(alias="ComparisonOperator")
    attribute_value_list: Optional[
        Sequence[
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ]
    ] = Field(default=None, alias="AttributeValueList")


class DeleteRequestModel(BaseModel):
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")


class DeleteModel(BaseModel):
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    table_name: str = Field(alias="TableName")
    condition_expression: Optional[str] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    return_values_on_condition_check_failure: Optional[
        Literal["ALL_OLD", "NONE"]
    ] = Field(default=None, alias="ReturnValuesOnConditionCheckFailure")


class ExecuteStatementInputRequestModel(BaseModel):
    statement: str = Field(alias="Statement")
    parameters: Optional[
        Sequence[
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ]
    ] = Field(default=None, alias="Parameters")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")


class ExpectedAttributeValueModel(BaseModel):
    value: Optional[
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ]
    ] = Field(default=None, alias="Value")
    exists: Optional[bool] = Field(default=None, alias="Exists")
    comparison_operator: Optional[
        Literal[
            "BEGINS_WITH",
            "BETWEEN",
            "CONTAINS",
            "EQ",
            "GE",
            "GT",
            "IN",
            "LE",
            "LT",
            "NE",
            "NOT_CONTAINS",
            "NOT_NULL",
            "NULL",
        ]
    ] = Field(default=None, alias="ComparisonOperator")
    attribute_value_list: Optional[
        Sequence[
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ]
    ] = Field(default=None, alias="AttributeValueList")


class GetItemInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )


class GetModel(BaseModel):
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    table_name: str = Field(alias="TableName")
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )


class ItemCollectionMetricsModel(BaseModel):
    item_collection_key: Optional[Dict[str, AttributeValueModel]] = Field(
        default=None, alias="ItemCollectionKey"
    )
    size_estimate_range_gb: Optional[List[float]] = Field(
        default=None, alias="SizeEstimateRangeGB"
    )


class ItemResponseModel(BaseModel):
    item: Optional[Dict[str, AttributeValueModel]] = Field(default=None, alias="Item")


class KeysAndAttributesModel(BaseModel):
    keys: Sequence[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(alias="Keys")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )


class ParameterizedStatementModel(BaseModel):
    statement: str = Field(alias="Statement")
    parameters: Optional[
        Sequence[
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ]
    ] = Field(default=None, alias="Parameters")


class PutRequestModel(BaseModel):
    item: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Item")


class PutModel(BaseModel):
    item: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Item")
    table_name: str = Field(alias="TableName")
    condition_expression: Optional[str] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    return_values_on_condition_check_failure: Optional[
        Literal["ALL_OLD", "NONE"]
    ] = Field(default=None, alias="ReturnValuesOnConditionCheckFailure")


class UpdateModel(BaseModel):
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    update_expression: str = Field(alias="UpdateExpression")
    table_name: str = Field(alias="TableName")
    condition_expression: Optional[str] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    return_values_on_condition_check_failure: Optional[
        Literal["ALL_OLD", "NONE"]
    ] = Field(default=None, alias="ReturnValuesOnConditionCheckFailure")


class AutoScalingPolicyDescriptionModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    target_tracking_scaling_policy_configuration: Optional[
        AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionModel
    ] = Field(default=None, alias="TargetTrackingScalingPolicyConfiguration")


class AutoScalingPolicyUpdateModel(BaseModel):
    target_tracking_scaling_policy_configuration: AutoScalingTargetTrackingScalingPolicyConfigurationUpdateModel = Field(
        alias="TargetTrackingScalingPolicyConfiguration"
    )
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")


class CreateBackupOutputModel(BaseModel):
    backup_details: BackupDetailsModel = Field(alias="BackupDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupsOutputTableModel(BaseModel):
    backup_summaries: List[BackupSummaryTableModel] = Field(alias="BackupSummaries")
    last_evaluated_backup_arn: str = Field(alias="LastEvaluatedBackupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackupsOutputModel(BaseModel):
    backup_summaries: List[BackupSummaryModel] = Field(alias="BackupSummaries")
    last_evaluated_backup_arn: str = Field(alias="LastEvaluatedBackupArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetItemInputServiceResourceBatchGetItemModel(BaseModel):
    request_items: Mapping[str, KeysAndAttributesServiceResourceModel] = Field(
        alias="RequestItems"
    )
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )


class BatchStatementResponseModel(BaseModel):
    error: Optional[BatchStatementErrorModel] = Field(default=None, alias="Error")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    item: Optional[Dict[str, AttributeValueModel]] = Field(default=None, alias="Item")


class ConsumedCapacityServiceResourceModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    capacity_units: Optional[float] = Field(default=None, alias="CapacityUnits")
    read_capacity_units: Optional[float] = Field(
        default=None, alias="ReadCapacityUnits"
    )
    write_capacity_units: Optional[float] = Field(
        default=None, alias="WriteCapacityUnits"
    )
    table: Optional[CapacityServiceResourceModel] = Field(default=None, alias="Table")
    local_secondary_indexes: Optional[Dict[str, CapacityServiceResourceModel]] = Field(
        default=None, alias="LocalSecondaryIndexes"
    )
    global_secondary_indexes: Optional[Dict[str, CapacityServiceResourceModel]] = Field(
        default=None, alias="GlobalSecondaryIndexes"
    )


class ConsumedCapacityTableModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    capacity_units: Optional[float] = Field(default=None, alias="CapacityUnits")
    read_capacity_units: Optional[float] = Field(
        default=None, alias="ReadCapacityUnits"
    )
    write_capacity_units: Optional[float] = Field(
        default=None, alias="WriteCapacityUnits"
    )
    table: Optional[CapacityTableModel] = Field(default=None, alias="Table")
    local_secondary_indexes: Optional[Dict[str, CapacityTableModel]] = Field(
        default=None, alias="LocalSecondaryIndexes"
    )
    global_secondary_indexes: Optional[Dict[str, CapacityTableModel]] = Field(
        default=None, alias="GlobalSecondaryIndexes"
    )


class ConsumedCapacityModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    capacity_units: Optional[float] = Field(default=None, alias="CapacityUnits")
    read_capacity_units: Optional[float] = Field(
        default=None, alias="ReadCapacityUnits"
    )
    write_capacity_units: Optional[float] = Field(
        default=None, alias="WriteCapacityUnits"
    )
    table: Optional[CapacityModel] = Field(default=None, alias="Table")
    local_secondary_indexes: Optional[Dict[str, CapacityModel]] = Field(
        default=None, alias="LocalSecondaryIndexes"
    )
    global_secondary_indexes: Optional[Dict[str, CapacityModel]] = Field(
        default=None, alias="GlobalSecondaryIndexes"
    )


class QueryInputTableQueryModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"
        ]
    ] = Field(default=None, alias="Select")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    key_conditions: Optional[Mapping[str, ConditionTableModel]] = Field(
        default=None, alias="KeyConditions"
    )
    query_filter: Optional[Mapping[str, ConditionTableModel]] = Field(
        default=None, alias="QueryFilter"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    scan_index_forward: Optional[bool] = Field(default=None, alias="ScanIndexForward")
    exclusive_start_key: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExclusiveStartKey")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    filter_expression: Optional[Union[str, ConditionBase]] = Field(
        default=None, alias="FilterExpression"
    )
    key_condition_expression: Optional[Union[str, ConditionBase]] = Field(
        default=None, alias="KeyConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class ScanInputTableScanModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"
        ]
    ] = Field(default=None, alias="Select")
    scan_filter: Optional[Mapping[str, ConditionTableModel]] = Field(
        default=None, alias="ScanFilter"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    exclusive_start_key: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExclusiveStartKey")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    total_segments: Optional[int] = Field(default=None, alias="TotalSegments")
    segment: Optional[int] = Field(default=None, alias="Segment")
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    filter_expression: Optional[Union[str, ConditionBase]] = Field(
        default=None, alias="FilterExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")


class ContinuousBackupsDescriptionModel(BaseModel):
    continuous_backups_status: Literal["DISABLED", "ENABLED"] = Field(
        alias="ContinuousBackupsStatus"
    )
    point_in_time_recovery_description: Optional[
        PointInTimeRecoveryDescriptionModel
    ] = Field(default=None, alias="PointInTimeRecoveryDescription")


class ListContributorInsightsOutputModel(BaseModel):
    contributor_insights_summaries: List[ContributorInsightsSummaryModel] = Field(
        alias="ContributorInsightsSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LocalSecondaryIndexDescriptionTableModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    key_schema: Optional[List[KeySchemaElementTableModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[ProjectionTableModel] = Field(default=None, alias="Projection")
    index_size_bytes: Optional[int] = Field(default=None, alias="IndexSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    index_arn: Optional[str] = Field(default=None, alias="IndexArn")


class CreateGlobalSecondaryIndexActionTableModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    key_schema: Sequence[KeySchemaElementTableModel] = Field(alias="KeySchema")
    projection: ProjectionTableModel = Field(alias="Projection")
    provisioned_throughput: Optional[ProvisionedThroughputTableModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )


class UpdateGlobalSecondaryIndexActionTableModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    provisioned_throughput: ProvisionedThroughputTableModel = Field(
        alias="ProvisionedThroughput"
    )


class LocalSecondaryIndexDescriptionModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    key_schema: Optional[List[KeySchemaElementModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[ProjectionModel] = Field(default=None, alias="Projection")
    index_size_bytes: Optional[int] = Field(default=None, alias="IndexSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    index_arn: Optional[str] = Field(default=None, alias="IndexArn")


class LocalSecondaryIndexInfoModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    key_schema: Optional[List[KeySchemaElementModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[ProjectionModel] = Field(default=None, alias="Projection")


class LocalSecondaryIndexModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    key_schema: Sequence[KeySchemaElementModel] = Field(alias="KeySchema")
    projection: ProjectionModel = Field(alias="Projection")


class CreateGlobalSecondaryIndexActionModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    key_schema: Sequence[KeySchemaElementModel] = Field(alias="KeySchema")
    projection: ProjectionModel = Field(alias="Projection")
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )


class GlobalSecondaryIndexInfoModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    key_schema: Optional[List[KeySchemaElementModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[ProjectionModel] = Field(default=None, alias="Projection")
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )


class GlobalSecondaryIndexModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    key_schema: Sequence[KeySchemaElementModel] = Field(alias="KeySchema")
    projection: ProjectionModel = Field(alias="Projection")
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )


class SourceTableDetailsModel(BaseModel):
    table_name: str = Field(alias="TableName")
    table_id: str = Field(alias="TableId")
    key_schema: List[KeySchemaElementModel] = Field(alias="KeySchema")
    table_creation_date_time: datetime = Field(alias="TableCreationDateTime")
    provisioned_throughput: ProvisionedThroughputModel = Field(
        alias="ProvisionedThroughput"
    )
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    table_size_bytes: Optional[int] = Field(default=None, alias="TableSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )


class UpdateGlobalSecondaryIndexActionModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    provisioned_throughput: ProvisionedThroughputModel = Field(
        alias="ProvisionedThroughput"
    )


class CreateGlobalTableInputRequestModel(BaseModel):
    global_table_name: str = Field(alias="GlobalTableName")
    replication_group: Sequence[ReplicaModel] = Field(alias="ReplicationGroup")


class GlobalTableModel(BaseModel):
    global_table_name: Optional[str] = Field(default=None, alias="GlobalTableName")
    replication_group: Optional[List[ReplicaModel]] = Field(
        default=None, alias="ReplicationGroup"
    )


class ReplicaGlobalSecondaryIndexDescriptionTableModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideTableModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")


class ReplicaGlobalSecondaryIndexTableModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideTableModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")


class ReplicaGlobalSecondaryIndexDescriptionModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")


class ReplicaGlobalSecondaryIndexModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")


class ListTagsOfResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class InputFormatOptionsModel(BaseModel):
    csv: Optional[CsvOptionsModel] = Field(default=None, alias="Csv")


class DeleteItemInputTableDeleteItemModel(BaseModel):
    key: Mapping[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    expected: Optional[Mapping[str, ExpectedAttributeValueTableModel]] = Field(
        default=None, alias="Expected"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    return_values: Optional[
        Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
    ] = Field(default=None, alias="ReturnValues")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )
    condition_expression: Optional[Union[str, ConditionBase]] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class PutItemInputTablePutItemModel(BaseModel):
    item: Mapping[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Item")
    expected: Optional[Mapping[str, ExpectedAttributeValueTableModel]] = Field(
        default=None, alias="Expected"
    )
    return_values: Optional[
        Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
    ] = Field(default=None, alias="ReturnValues")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    condition_expression: Optional[Union[str, ConditionBase]] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class UpdateItemInputTableUpdateItemModel(BaseModel):
    key: Mapping[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    attribute_updates: Optional[Mapping[str, AttributeValueUpdateTableModel]] = Field(
        default=None, alias="AttributeUpdates"
    )
    expected: Optional[Mapping[str, ExpectedAttributeValueTableModel]] = Field(
        default=None, alias="Expected"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    return_values: Optional[
        Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
    ] = Field(default=None, alias="ReturnValues")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )
    update_expression: Optional[str] = Field(default=None, alias="UpdateExpression")
    condition_expression: Optional[Union[str, ConditionBase]] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class ReplicaUpdateModel(BaseModel):
    create: Optional[CreateReplicaActionModel] = Field(default=None, alias="Create")
    delete: Optional[DeleteReplicaActionModel] = Field(default=None, alias="Delete")


class DescribeContributorInsightsOutputModel(BaseModel):
    table_name: str = Field(alias="TableName")
    index_name: str = Field(alias="IndexName")
    contributor_insights_rule_list: List[str] = Field(
        alias="ContributorInsightsRuleList"
    )
    contributor_insights_status: Literal[
        "DISABLED", "DISABLING", "ENABLED", "ENABLING", "FAILED"
    ] = Field(alias="ContributorInsightsStatus")
    last_update_date_time: datetime = Field(alias="LastUpdateDateTime")
    failure_exception: FailureExceptionModel = Field(alias="FailureException")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointsResponseModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExportOutputModel(BaseModel):
    export_description: ExportDescriptionModel = Field(alias="ExportDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportTableToPointInTimeOutputModel(BaseModel):
    export_description: ExportDescriptionModel = Field(alias="ExportDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeKinesisStreamingDestinationOutputModel(BaseModel):
    table_name: str = Field(alias="TableName")
    kinesis_data_stream_destinations: List[KinesisDataStreamDestinationModel] = Field(
        alias="KinesisDataStreamDestinations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTableInputTableExistsWaitModel(BaseModel):
    table_name: str = Field(alias="TableName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTableInputTableNotExistsWaitModel(BaseModel):
    table_name: str = Field(alias="TableName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeTimeToLiveOutputModel(BaseModel):
    time_to_live_description: TimeToLiveDescriptionModel = Field(
        alias="TimeToLiveDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListExportsOutputModel(BaseModel):
    export_summaries: List[ExportSummaryModel] = Field(alias="ExportSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GlobalSecondaryIndexDescriptionTableModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    key_schema: Optional[List[KeySchemaElementTableModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[ProjectionTableModel] = Field(default=None, alias="Projection")
    index_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
    ] = Field(default=None, alias="IndexStatus")
    backfilling: Optional[bool] = Field(default=None, alias="Backfilling")
    provisioned_throughput: Optional[
        ProvisionedThroughputDescriptionTableModel
    ] = Field(default=None, alias="ProvisionedThroughput")
    index_size_bytes: Optional[int] = Field(default=None, alias="IndexSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    index_arn: Optional[str] = Field(default=None, alias="IndexArn")


class GlobalSecondaryIndexDescriptionModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    key_schema: Optional[List[KeySchemaElementModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[ProjectionModel] = Field(default=None, alias="Projection")
    index_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
    ] = Field(default=None, alias="IndexStatus")
    backfilling: Optional[bool] = Field(default=None, alias="Backfilling")
    provisioned_throughput: Optional[ProvisionedThroughputDescriptionModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    index_size_bytes: Optional[int] = Field(default=None, alias="IndexSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    index_arn: Optional[str] = Field(default=None, alias="IndexArn")


class GlobalSecondaryIndexServiceResourceModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    key_schema: Sequence[KeySchemaElementServiceResourceModel] = Field(
        alias="KeySchema"
    )
    projection: ProjectionServiceResourceModel = Field(alias="Projection")
    provisioned_throughput: Optional[ProvisionedThroughputServiceResourceModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )


class LocalSecondaryIndexServiceResourceModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    key_schema: Sequence[KeySchemaElementServiceResourceModel] = Field(
        alias="KeySchema"
    )
    projection: ProjectionServiceResourceModel = Field(alias="Projection")


class ImportSummaryModel(BaseModel):
    import_arn: Optional[str] = Field(default=None, alias="ImportArn")
    import_status: Optional[
        Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="ImportStatus")
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    s3_bucket_source: Optional[S3BucketSourceModel] = Field(
        default=None, alias="S3BucketSource"
    )
    cloud_watch_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupArn"
    )
    input_format: Optional[Literal["CSV", "DYNAMODB_JSON", "ION"]] = Field(
        default=None, alias="InputFormat"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class ListBackupsInputListBackupsPaginateModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    time_range_lower_bound: Optional[Union[datetime, str]] = Field(
        default=None, alias="TimeRangeLowerBound"
    )
    time_range_upper_bound: Optional[Union[datetime, str]] = Field(
        default=None, alias="TimeRangeUpperBound"
    )
    backup_type: Optional[Literal["ALL", "AWS_BACKUP", "SYSTEM", "USER"]] = Field(
        default=None, alias="BackupType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTablesInputListTablesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsOfResourceInputListTagsOfResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class QueryInputQueryPaginateModel(BaseModel):
    table_name: str = Field(alias="TableName")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"
        ]
    ] = Field(default=None, alias="Select")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    key_conditions: Optional[Mapping[str, ConditionTableModel]] = Field(
        default=None, alias="KeyConditions"
    )
    query_filter: Optional[Mapping[str, ConditionTableModel]] = Field(
        default=None, alias="QueryFilter"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    scan_index_forward: Optional[bool] = Field(default=None, alias="ScanIndexForward")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    key_condition_expression: Optional[str] = Field(
        default=None, alias="KeyConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ScanInputScanPaginateModel(BaseModel):
    table_name: str = Field(alias="TableName")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"
        ]
    ] = Field(default=None, alias="Select")
    scan_filter: Optional[Mapping[str, ConditionTableModel]] = Field(
        default=None, alias="ScanFilter"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    total_segments: Optional[int] = Field(default=None, alias="TotalSegments")
    segment: Optional[int] = Field(default=None, alias="Segment")
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsOfResourceOutputTableModel(BaseModel):
    tags: List[TagTableModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContinuousBackupsInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    point_in_time_recovery_specification: PointInTimeRecoverySpecificationModel = Field(
        alias="PointInTimeRecoverySpecification"
    )


class WriteRequestServiceResourceModel(BaseModel):
    put_request: Optional[PutRequestServiceResourceModel] = Field(
        default=None, alias="PutRequest"
    )
    delete_request: Optional[DeleteRequestServiceResourceModel] = Field(
        default=None, alias="DeleteRequest"
    )


class UpdateTimeToLiveInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    time_to_live_specification: TimeToLiveSpecificationModel = Field(
        alias="TimeToLiveSpecification"
    )


class UpdateTimeToLiveOutputModel(BaseModel):
    time_to_live_specification: TimeToLiveSpecificationModel = Field(
        alias="TimeToLiveSpecification"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchExecuteStatementInputRequestModel(BaseModel):
    statements: Sequence[BatchStatementRequestModel] = Field(alias="Statements")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )


class QueryInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"
        ]
    ] = Field(default=None, alias="Select")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")
    key_conditions: Optional[Mapping[str, ConditionModel]] = Field(
        default=None, alias="KeyConditions"
    )
    query_filter: Optional[Mapping[str, ConditionModel]] = Field(
        default=None, alias="QueryFilter"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    scan_index_forward: Optional[bool] = Field(default=None, alias="ScanIndexForward")
    exclusive_start_key: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExclusiveStartKey")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    key_condition_expression: Optional[str] = Field(
        default=None, alias="KeyConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class ScanInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    attributes_to_get: Optional[Sequence[str]] = Field(
        default=None, alias="AttributesToGet"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    select: Optional[
        Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"
        ]
    ] = Field(default=None, alias="Select")
    scan_filter: Optional[Mapping[str, ConditionModel]] = Field(
        default=None, alias="ScanFilter"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    exclusive_start_key: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExclusiveStartKey")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    total_segments: Optional[int] = Field(default=None, alias="TotalSegments")
    segment: Optional[int] = Field(default=None, alias="Segment")
    projection_expression: Optional[str] = Field(
        default=None, alias="ProjectionExpression"
    )
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")
    consistent_read: Optional[bool] = Field(default=None, alias="ConsistentRead")


class DeleteItemInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    expected: Optional[Mapping[str, ExpectedAttributeValueModel]] = Field(
        default=None, alias="Expected"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    return_values: Optional[
        Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
    ] = Field(default=None, alias="ReturnValues")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )
    condition_expression: Optional[str] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class PutItemInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    item: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Item")
    expected: Optional[Mapping[str, ExpectedAttributeValueModel]] = Field(
        default=None, alias="Expected"
    )
    return_values: Optional[
        Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
    ] = Field(default=None, alias="ReturnValues")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    condition_expression: Optional[str] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class UpdateItemInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    key: Mapping[
        str,
        Union[
            AttributeValueModel,
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Key")
    attribute_updates: Optional[Mapping[str, AttributeValueUpdateModel]] = Field(
        default=None, alias="AttributeUpdates"
    )
    expected: Optional[Mapping[str, ExpectedAttributeValueModel]] = Field(
        default=None, alias="Expected"
    )
    conditional_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="ConditionalOperator"
    )
    return_values: Optional[
        Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
    ] = Field(default=None, alias="ReturnValues")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )
    update_expression: Optional[str] = Field(default=None, alias="UpdateExpression")
    condition_expression: Optional[str] = Field(
        default=None, alias="ConditionExpression"
    )
    expression_attribute_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ExpressionAttributeNames"
    )
    expression_attribute_values: Optional[
        Mapping[
            str,
            Union[
                AttributeValueModel,
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(default=None, alias="ExpressionAttributeValues")


class TransactGetItemModel(BaseModel):
    get: GetModel = Field(alias="Get")


class BatchGetItemInputRequestModel(BaseModel):
    request_items: Mapping[str, KeysAndAttributesModel] = Field(alias="RequestItems")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )


class ExecuteTransactionInputRequestModel(BaseModel):
    transact_statements: Sequence[ParameterizedStatementModel] = Field(
        alias="TransactStatements"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )


class WriteRequestModel(BaseModel):
    put_request: Optional[PutRequestModel] = Field(default=None, alias="PutRequest")
    delete_request: Optional[DeleteRequestModel] = Field(
        default=None, alias="DeleteRequest"
    )


class TransactWriteItemModel(BaseModel):
    condition_check: Optional[ConditionCheckModel] = Field(
        default=None, alias="ConditionCheck"
    )
    put: Optional[PutModel] = Field(default=None, alias="Put")
    delete: Optional[DeleteModel] = Field(default=None, alias="Delete")
    update: Optional[UpdateModel] = Field(default=None, alias="Update")


class AutoScalingSettingsDescriptionModel(BaseModel):
    minimum_units: Optional[int] = Field(default=None, alias="MinimumUnits")
    maximum_units: Optional[int] = Field(default=None, alias="MaximumUnits")
    auto_scaling_disabled: Optional[bool] = Field(
        default=None, alias="AutoScalingDisabled"
    )
    auto_scaling_role_arn: Optional[str] = Field(
        default=None, alias="AutoScalingRoleArn"
    )
    scaling_policies: Optional[List[AutoScalingPolicyDescriptionModel]] = Field(
        default=None, alias="ScalingPolicies"
    )


class AutoScalingSettingsUpdateModel(BaseModel):
    minimum_units: Optional[int] = Field(default=None, alias="MinimumUnits")
    maximum_units: Optional[int] = Field(default=None, alias="MaximumUnits")
    auto_scaling_disabled: Optional[bool] = Field(
        default=None, alias="AutoScalingDisabled"
    )
    auto_scaling_role_arn: Optional[str] = Field(
        default=None, alias="AutoScalingRoleArn"
    )
    scaling_policy_update: Optional[AutoScalingPolicyUpdateModel] = Field(
        default=None, alias="ScalingPolicyUpdate"
    )


class BatchGetItemOutputServiceResourceModel(BaseModel):
    responses: Dict[
        str,
        List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    ] = Field(alias="Responses")
    unprocessed_keys: Dict[str, KeysAndAttributesServiceResourceModel] = Field(
        alias="UnprocessedKeys"
    )
    consumed_capacity: List[ConsumedCapacityServiceResourceModel] = Field(
        alias="ConsumedCapacity"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteItemOutputTableModel(BaseModel):
    attributes: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Attributes")
    consumed_capacity: ConsumedCapacityTableModel = Field(alias="ConsumedCapacity")
    item_collection_metrics: ItemCollectionMetricsTableModel = Field(
        alias="ItemCollectionMetrics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetItemOutputTableModel(BaseModel):
    item: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Item")
    consumed_capacity: ConsumedCapacityTableModel = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutItemOutputTableModel(BaseModel):
    attributes: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Attributes")
    consumed_capacity: ConsumedCapacityTableModel = Field(alias="ConsumedCapacity")
    item_collection_metrics: ItemCollectionMetricsTableModel = Field(
        alias="ItemCollectionMetrics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryOutputTableModel(BaseModel):
    items: List[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(alias="Items")
    count: int = Field(alias="Count")
    scanned_count: int = Field(alias="ScannedCount")
    last_evaluated_key: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="LastEvaluatedKey")
    consumed_capacity: ConsumedCapacityTableModel = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScanOutputTableModel(BaseModel):
    items: List[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ]
    ] = Field(alias="Items")
    count: int = Field(alias="Count")
    scanned_count: int = Field(alias="ScannedCount")
    last_evaluated_key: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="LastEvaluatedKey")
    consumed_capacity: ConsumedCapacityTableModel = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateItemOutputTableModel(BaseModel):
    attributes: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            Sequence[Any],
            Mapping[str, Any],
            None,
        ],
    ] = Field(alias="Attributes")
    consumed_capacity: ConsumedCapacityTableModel = Field(alias="ConsumedCapacity")
    item_collection_metrics: ItemCollectionMetricsTableModel = Field(
        alias="ItemCollectionMetrics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchExecuteStatementOutputModel(BaseModel):
    responses: List[BatchStatementResponseModel] = Field(alias="Responses")
    consumed_capacity: List[ConsumedCapacityModel] = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetItemOutputModel(BaseModel):
    responses: Dict[str, List[Dict[str, AttributeValueModel]]] = Field(
        alias="Responses"
    )
    unprocessed_keys: Dict[str, KeysAndAttributesModel] = Field(alias="UnprocessedKeys")
    consumed_capacity: List[ConsumedCapacityModel] = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteItemOutputModel(BaseModel):
    attributes: Dict[str, AttributeValueModel] = Field(alias="Attributes")
    consumed_capacity: ConsumedCapacityModel = Field(alias="ConsumedCapacity")
    item_collection_metrics: ItemCollectionMetricsModel = Field(
        alias="ItemCollectionMetrics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecuteStatementOutputModel(BaseModel):
    items: List[Dict[str, AttributeValueModel]] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    consumed_capacity: ConsumedCapacityModel = Field(alias="ConsumedCapacity")
    last_evaluated_key: Dict[str, AttributeValueModel] = Field(alias="LastEvaluatedKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecuteTransactionOutputModel(BaseModel):
    responses: List[ItemResponseModel] = Field(alias="Responses")
    consumed_capacity: List[ConsumedCapacityModel] = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetItemOutputModel(BaseModel):
    item: Dict[str, AttributeValueModel] = Field(alias="Item")
    consumed_capacity: ConsumedCapacityModel = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutItemOutputModel(BaseModel):
    attributes: Dict[str, AttributeValueModel] = Field(alias="Attributes")
    consumed_capacity: ConsumedCapacityModel = Field(alias="ConsumedCapacity")
    item_collection_metrics: ItemCollectionMetricsModel = Field(
        alias="ItemCollectionMetrics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class QueryOutputModel(BaseModel):
    items: List[Dict[str, AttributeValueModel]] = Field(alias="Items")
    count: int = Field(alias="Count")
    scanned_count: int = Field(alias="ScannedCount")
    last_evaluated_key: Dict[str, AttributeValueModel] = Field(alias="LastEvaluatedKey")
    consumed_capacity: ConsumedCapacityModel = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScanOutputModel(BaseModel):
    items: List[Dict[str, AttributeValueModel]] = Field(alias="Items")
    count: int = Field(alias="Count")
    scanned_count: int = Field(alias="ScannedCount")
    last_evaluated_key: Dict[str, AttributeValueModel] = Field(alias="LastEvaluatedKey")
    consumed_capacity: ConsumedCapacityModel = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransactGetItemsOutputModel(BaseModel):
    consumed_capacity: List[ConsumedCapacityModel] = Field(alias="ConsumedCapacity")
    responses: List[ItemResponseModel] = Field(alias="Responses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransactWriteItemsOutputModel(BaseModel):
    consumed_capacity: List[ConsumedCapacityModel] = Field(alias="ConsumedCapacity")
    item_collection_metrics: Dict[str, List[ItemCollectionMetricsModel]] = Field(
        alias="ItemCollectionMetrics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateItemOutputModel(BaseModel):
    attributes: Dict[str, AttributeValueModel] = Field(alias="Attributes")
    consumed_capacity: ConsumedCapacityModel = Field(alias="ConsumedCapacity")
    item_collection_metrics: ItemCollectionMetricsModel = Field(
        alias="ItemCollectionMetrics"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeContinuousBackupsOutputModel(BaseModel):
    continuous_backups_description: ContinuousBackupsDescriptionModel = Field(
        alias="ContinuousBackupsDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContinuousBackupsOutputModel(BaseModel):
    continuous_backups_description: ContinuousBackupsDescriptionModel = Field(
        alias="ContinuousBackupsDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GlobalSecondaryIndexUpdateTableModel(BaseModel):
    update: Optional[UpdateGlobalSecondaryIndexActionTableModel] = Field(
        default=None, alias="Update"
    )
    create: Optional[CreateGlobalSecondaryIndexActionTableModel] = Field(
        default=None, alias="Create"
    )
    delete: Optional[DeleteGlobalSecondaryIndexActionTableModel] = Field(
        default=None, alias="Delete"
    )


class SourceTableFeatureDetailsModel(BaseModel):
    local_secondary_indexes: Optional[List[LocalSecondaryIndexInfoModel]] = Field(
        default=None, alias="LocalSecondaryIndexes"
    )
    global_secondary_indexes: Optional[List[GlobalSecondaryIndexInfoModel]] = Field(
        default=None, alias="GlobalSecondaryIndexes"
    )
    stream_description: Optional[StreamSpecificationModel] = Field(
        default=None, alias="StreamDescription"
    )
    time_to_live_description: Optional[TimeToLiveDescriptionModel] = Field(
        default=None, alias="TimeToLiveDescription"
    )
    s_s_edescription: Optional[SSEDescriptionModel] = Field(
        default=None, alias="SSEDescription"
    )


class CreateTableInputRequestModel(BaseModel):
    attribute_definitions: Sequence[AttributeDefinitionModel] = Field(
        alias="AttributeDefinitions"
    )
    table_name: str = Field(alias="TableName")
    key_schema: Sequence[KeySchemaElementModel] = Field(alias="KeySchema")
    local_secondary_indexes: Optional[Sequence[LocalSecondaryIndexModel]] = Field(
        default=None, alias="LocalSecondaryIndexes"
    )
    global_secondary_indexes: Optional[Sequence[GlobalSecondaryIndexModel]] = Field(
        default=None, alias="GlobalSecondaryIndexes"
    )
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    stream_specification: Optional[StreamSpecificationModel] = Field(
        default=None, alias="StreamSpecification"
    )
    s_s_especification: Optional[SSESpecificationModel] = Field(
        default=None, alias="SSESpecification"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    table_class: Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]] = Field(
        default=None, alias="TableClass"
    )


class RestoreTableFromBackupInputRequestModel(BaseModel):
    target_table_name: str = Field(alias="TargetTableName")
    backup_arn: str = Field(alias="BackupArn")
    billing_mode_override: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingModeOverride"
    )
    global_secondary_index_override: Optional[
        Sequence[GlobalSecondaryIndexModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexOverride")
    local_secondary_index_override: Optional[
        Sequence[LocalSecondaryIndexModel]
    ] = Field(default=None, alias="LocalSecondaryIndexOverride")
    provisioned_throughput_override: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughputOverride"
    )
    s_s_especification_override: Optional[SSESpecificationModel] = Field(
        default=None, alias="SSESpecificationOverride"
    )


class RestoreTableToPointInTimeInputRequestModel(BaseModel):
    target_table_name: str = Field(alias="TargetTableName")
    source_table_arn: Optional[str] = Field(default=None, alias="SourceTableArn")
    source_table_name: Optional[str] = Field(default=None, alias="SourceTableName")
    use_latest_restorable_time: Optional[bool] = Field(
        default=None, alias="UseLatestRestorableTime"
    )
    restore_date_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="RestoreDateTime"
    )
    billing_mode_override: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingModeOverride"
    )
    global_secondary_index_override: Optional[
        Sequence[GlobalSecondaryIndexModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexOverride")
    local_secondary_index_override: Optional[
        Sequence[LocalSecondaryIndexModel]
    ] = Field(default=None, alias="LocalSecondaryIndexOverride")
    provisioned_throughput_override: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughputOverride"
    )
    s_s_especification_override: Optional[SSESpecificationModel] = Field(
        default=None, alias="SSESpecificationOverride"
    )


class TableCreationParametersModel(BaseModel):
    table_name: str = Field(alias="TableName")
    attribute_definitions: List[AttributeDefinitionModel] = Field(
        alias="AttributeDefinitions"
    )
    key_schema: List[KeySchemaElementModel] = Field(alias="KeySchema")
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    s_s_especification: Optional[SSESpecificationModel] = Field(
        default=None, alias="SSESpecification"
    )
    global_secondary_indexes: Optional[List[GlobalSecondaryIndexModel]] = Field(
        default=None, alias="GlobalSecondaryIndexes"
    )


class GlobalSecondaryIndexUpdateModel(BaseModel):
    update: Optional[UpdateGlobalSecondaryIndexActionModel] = Field(
        default=None, alias="Update"
    )
    create: Optional[CreateGlobalSecondaryIndexActionModel] = Field(
        default=None, alias="Create"
    )
    delete: Optional[DeleteGlobalSecondaryIndexActionModel] = Field(
        default=None, alias="Delete"
    )


class ListGlobalTablesOutputModel(BaseModel):
    global_tables: List[GlobalTableModel] = Field(alias="GlobalTables")
    last_evaluated_global_table_name: str = Field(alias="LastEvaluatedGlobalTableName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicaDescriptionTableModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    replica_status: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "CREATION_FAILED",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "REGION_DISABLED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="ReplicaStatus")
    replica_status_description: Optional[str] = Field(
        default=None, alias="ReplicaStatusDescription"
    )
    replica_status_percent_progress: Optional[str] = Field(
        default=None, alias="ReplicaStatusPercentProgress"
    )
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideTableModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")
    global_secondary_indexes: Optional[
        List[ReplicaGlobalSecondaryIndexDescriptionTableModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    replica_inaccessible_date_time: Optional[datetime] = Field(
        default=None, alias="ReplicaInaccessibleDateTime"
    )
    replica_table_class_summary: Optional[TableClassSummaryTableModel] = Field(
        default=None, alias="ReplicaTableClassSummary"
    )


class CreateReplicationGroupMemberActionTableModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideTableModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")
    global_secondary_indexes: Optional[
        Sequence[ReplicaGlobalSecondaryIndexTableModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    table_class_override: Optional[
        Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
    ] = Field(default=None, alias="TableClassOverride")


class UpdateReplicationGroupMemberActionTableModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideTableModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")
    global_secondary_indexes: Optional[
        Sequence[ReplicaGlobalSecondaryIndexTableModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    table_class_override: Optional[
        Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
    ] = Field(default=None, alias="TableClassOverride")


class ReplicaDescriptionModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    replica_status: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "CREATION_FAILED",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "REGION_DISABLED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="ReplicaStatus")
    replica_status_description: Optional[str] = Field(
        default=None, alias="ReplicaStatusDescription"
    )
    replica_status_percent_progress: Optional[str] = Field(
        default=None, alias="ReplicaStatusPercentProgress"
    )
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")
    global_secondary_indexes: Optional[
        List[ReplicaGlobalSecondaryIndexDescriptionModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    replica_inaccessible_date_time: Optional[datetime] = Field(
        default=None, alias="ReplicaInaccessibleDateTime"
    )
    replica_table_class_summary: Optional[TableClassSummaryModel] = Field(
        default=None, alias="ReplicaTableClassSummary"
    )


class CreateReplicationGroupMemberActionModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")
    global_secondary_indexes: Optional[
        Sequence[ReplicaGlobalSecondaryIndexModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    table_class_override: Optional[
        Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
    ] = Field(default=None, alias="TableClassOverride")


class UpdateReplicationGroupMemberActionModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyId")
    provisioned_throughput_override: Optional[
        ProvisionedThroughputOverrideModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")
    global_secondary_indexes: Optional[
        Sequence[ReplicaGlobalSecondaryIndexModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    table_class_override: Optional[
        Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
    ] = Field(default=None, alias="TableClassOverride")


class UpdateGlobalTableInputRequestModel(BaseModel):
    global_table_name: str = Field(alias="GlobalTableName")
    replica_updates: Sequence[ReplicaUpdateModel] = Field(alias="ReplicaUpdates")


class CreateTableInputServiceResourceCreateTableModel(BaseModel):
    attribute_definitions: Sequence[AttributeDefinitionServiceResourceModel] = Field(
        alias="AttributeDefinitions"
    )
    table_name: str = Field(alias="TableName")
    key_schema: Sequence[KeySchemaElementServiceResourceModel] = Field(
        alias="KeySchema"
    )
    local_secondary_indexes: Optional[
        Sequence[LocalSecondaryIndexServiceResourceModel]
    ] = Field(default=None, alias="LocalSecondaryIndexes")
    global_secondary_indexes: Optional[
        Sequence[GlobalSecondaryIndexServiceResourceModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )
    provisioned_throughput: Optional[ProvisionedThroughputServiceResourceModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    stream_specification: Optional[StreamSpecificationServiceResourceModel] = Field(
        default=None, alias="StreamSpecification"
    )
    s_s_especification: Optional[SSESpecificationServiceResourceModel] = Field(
        default=None, alias="SSESpecification"
    )
    tags: Optional[Sequence[TagServiceResourceModel]] = Field(
        default=None, alias="Tags"
    )
    table_class: Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]] = Field(
        default=None, alias="TableClass"
    )


class ListImportsOutputModel(BaseModel):
    import_summary_list: List[ImportSummaryModel] = Field(alias="ImportSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchWriteItemInputServiceResourceBatchWriteItemModel(BaseModel):
    request_items: Mapping[str, Sequence[WriteRequestServiceResourceModel]] = Field(
        alias="RequestItems"
    )
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )


class BatchWriteItemOutputServiceResourceModel(BaseModel):
    unprocessed_items: Dict[str, List[WriteRequestServiceResourceModel]] = Field(
        alias="UnprocessedItems"
    )
    item_collection_metrics: Dict[
        str, List[ItemCollectionMetricsServiceResourceModel]
    ] = Field(alias="ItemCollectionMetrics")
    consumed_capacity: List[ConsumedCapacityServiceResourceModel] = Field(
        alias="ConsumedCapacity"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransactGetItemsInputRequestModel(BaseModel):
    transact_items: Sequence[TransactGetItemModel] = Field(alias="TransactItems")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )


class BatchWriteItemInputRequestModel(BaseModel):
    request_items: Mapping[str, Sequence[WriteRequestModel]] = Field(
        alias="RequestItems"
    )
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )


class BatchWriteItemOutputModel(BaseModel):
    unprocessed_items: Dict[str, List[WriteRequestModel]] = Field(
        alias="UnprocessedItems"
    )
    item_collection_metrics: Dict[str, List[ItemCollectionMetricsModel]] = Field(
        alias="ItemCollectionMetrics"
    )
    consumed_capacity: List[ConsumedCapacityModel] = Field(alias="ConsumedCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransactWriteItemsInputRequestModel(BaseModel):
    transact_items: Sequence[TransactWriteItemModel] = Field(alias="TransactItems")
    return_consumed_capacity: Optional[Literal["INDEXES", "NONE", "TOTAL"]] = Field(
        default=None, alias="ReturnConsumedCapacity"
    )
    return_item_collection_metrics: Optional[Literal["NONE", "SIZE"]] = Field(
        default=None, alias="ReturnItemCollectionMetrics"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )


class ReplicaGlobalSecondaryIndexAutoScalingDescriptionModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    index_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
    ] = Field(default=None, alias="IndexStatus")
    provisioned_read_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ProvisionedReadCapacityAutoScalingSettings")
    provisioned_write_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ProvisionedWriteCapacityAutoScalingSettings")


class ReplicaGlobalSecondaryIndexSettingsDescriptionModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    index_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
    ] = Field(default=None, alias="IndexStatus")
    provisioned_read_capacity_units: Optional[int] = Field(
        default=None, alias="ProvisionedReadCapacityUnits"
    )
    provisioned_read_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ProvisionedReadCapacityAutoScalingSettings")
    provisioned_write_capacity_units: Optional[int] = Field(
        default=None, alias="ProvisionedWriteCapacityUnits"
    )
    provisioned_write_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ProvisionedWriteCapacityAutoScalingSettings")


class GlobalSecondaryIndexAutoScalingUpdateModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    provisioned_write_capacity_auto_scaling_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(default=None, alias="ProvisionedWriteCapacityAutoScalingUpdate")


class GlobalTableGlobalSecondaryIndexSettingsUpdateModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    provisioned_write_capacity_units: Optional[int] = Field(
        default=None, alias="ProvisionedWriteCapacityUnits"
    )
    provisioned_write_capacity_auto_scaling_settings_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(default=None, alias="ProvisionedWriteCapacityAutoScalingSettingsUpdate")


class ReplicaGlobalSecondaryIndexAutoScalingUpdateModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    provisioned_read_capacity_auto_scaling_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(default=None, alias="ProvisionedReadCapacityAutoScalingUpdate")


class ReplicaGlobalSecondaryIndexSettingsUpdateModel(BaseModel):
    index_name: str = Field(alias="IndexName")
    provisioned_read_capacity_units: Optional[int] = Field(
        default=None, alias="ProvisionedReadCapacityUnits"
    )
    provisioned_read_capacity_auto_scaling_settings_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(default=None, alias="ProvisionedReadCapacityAutoScalingSettingsUpdate")


class BackupDescriptionModel(BaseModel):
    backup_details: Optional[BackupDetailsModel] = Field(
        default=None, alias="BackupDetails"
    )
    source_table_details: Optional[SourceTableDetailsModel] = Field(
        default=None, alias="SourceTableDetails"
    )
    source_table_feature_details: Optional[SourceTableFeatureDetailsModel] = Field(
        default=None, alias="SourceTableFeatureDetails"
    )


class ImportTableDescriptionModel(BaseModel):
    import_arn: Optional[str] = Field(default=None, alias="ImportArn")
    import_status: Optional[
        Literal["CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="ImportStatus")
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    table_id: Optional[str] = Field(default=None, alias="TableId")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    s3_bucket_source: Optional[S3BucketSourceModel] = Field(
        default=None, alias="S3BucketSource"
    )
    error_count: Optional[int] = Field(default=None, alias="ErrorCount")
    cloud_watch_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupArn"
    )
    input_format: Optional[Literal["CSV", "DYNAMODB_JSON", "ION"]] = Field(
        default=None, alias="InputFormat"
    )
    input_format_options: Optional[InputFormatOptionsModel] = Field(
        default=None, alias="InputFormatOptions"
    )
    input_compression_type: Optional[Literal["GZIP", "NONE", "ZSTD"]] = Field(
        default=None, alias="InputCompressionType"
    )
    table_creation_parameters: Optional[TableCreationParametersModel] = Field(
        default=None, alias="TableCreationParameters"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    processed_size_bytes: Optional[int] = Field(
        default=None, alias="ProcessedSizeBytes"
    )
    processed_item_count: Optional[int] = Field(
        default=None, alias="ProcessedItemCount"
    )
    imported_item_count: Optional[int] = Field(default=None, alias="ImportedItemCount")
    failure_code: Optional[str] = Field(default=None, alias="FailureCode")
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")


class ImportTableInputRequestModel(BaseModel):
    s3_bucket_source: S3BucketSourceModel = Field(alias="S3BucketSource")
    input_format: Literal["CSV", "DYNAMODB_JSON", "ION"] = Field(alias="InputFormat")
    table_creation_parameters: TableCreationParametersModel = Field(
        alias="TableCreationParameters"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    input_format_options: Optional[InputFormatOptionsModel] = Field(
        default=None, alias="InputFormatOptions"
    )
    input_compression_type: Optional[Literal["GZIP", "NONE", "ZSTD"]] = Field(
        default=None, alias="InputCompressionType"
    )


class TableDescriptionTableModel(BaseModel):
    attribute_definitions: Optional[List[AttributeDefinitionTableModel]] = Field(
        default=None, alias="AttributeDefinitions"
    )
    table_name: Optional[str] = Field(default=None, alias="TableName")
    key_schema: Optional[List[KeySchemaElementTableModel]] = Field(
        default=None, alias="KeySchema"
    )
    table_status: Optional[
        Literal[
            "ACTIVE",
            "ARCHIVED",
            "ARCHIVING",
            "CREATING",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "UPDATING",
        ]
    ] = Field(default=None, alias="TableStatus")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    provisioned_throughput: Optional[
        ProvisionedThroughputDescriptionTableModel
    ] = Field(default=None, alias="ProvisionedThroughput")
    table_size_bytes: Optional[int] = Field(default=None, alias="TableSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    table_id: Optional[str] = Field(default=None, alias="TableId")
    billing_mode_summary: Optional[BillingModeSummaryTableModel] = Field(
        default=None, alias="BillingModeSummary"
    )
    local_secondary_indexes: Optional[
        List[LocalSecondaryIndexDescriptionTableModel]
    ] = Field(default=None, alias="LocalSecondaryIndexes")
    global_secondary_indexes: Optional[
        List[GlobalSecondaryIndexDescriptionTableModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    stream_specification: Optional[StreamSpecificationTableModel] = Field(
        default=None, alias="StreamSpecification"
    )
    latest_stream_label: Optional[str] = Field(default=None, alias="LatestStreamLabel")
    latest_stream_arn: Optional[str] = Field(default=None, alias="LatestStreamArn")
    global_table_version: Optional[str] = Field(
        default=None, alias="GlobalTableVersion"
    )
    replicas: Optional[List[ReplicaDescriptionTableModel]] = Field(
        default=None, alias="Replicas"
    )
    restore_summary: Optional[RestoreSummaryTableModel] = Field(
        default=None, alias="RestoreSummary"
    )
    s_s_edescription: Optional[SSEDescriptionTableModel] = Field(
        default=None, alias="SSEDescription"
    )
    archival_summary: Optional[ArchivalSummaryTableModel] = Field(
        default=None, alias="ArchivalSummary"
    )
    table_class_summary: Optional[TableClassSummaryTableModel] = Field(
        default=None, alias="TableClassSummary"
    )


class ReplicationGroupUpdateTableModel(BaseModel):
    create: Optional[CreateReplicationGroupMemberActionTableModel] = Field(
        default=None, alias="Create"
    )
    update: Optional[UpdateReplicationGroupMemberActionTableModel] = Field(
        default=None, alias="Update"
    )
    delete: Optional[DeleteReplicationGroupMemberActionTableModel] = Field(
        default=None, alias="Delete"
    )


class GlobalTableDescriptionModel(BaseModel):
    replication_group: Optional[List[ReplicaDescriptionModel]] = Field(
        default=None, alias="ReplicationGroup"
    )
    global_table_arn: Optional[str] = Field(default=None, alias="GlobalTableArn")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    global_table_status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
    ] = Field(default=None, alias="GlobalTableStatus")
    global_table_name: Optional[str] = Field(default=None, alias="GlobalTableName")


class TableDescriptionModel(BaseModel):
    attribute_definitions: Optional[List[AttributeDefinitionModel]] = Field(
        default=None, alias="AttributeDefinitions"
    )
    table_name: Optional[str] = Field(default=None, alias="TableName")
    key_schema: Optional[List[KeySchemaElementModel]] = Field(
        default=None, alias="KeySchema"
    )
    table_status: Optional[
        Literal[
            "ACTIVE",
            "ARCHIVED",
            "ARCHIVING",
            "CREATING",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "UPDATING",
        ]
    ] = Field(default=None, alias="TableStatus")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    provisioned_throughput: Optional[ProvisionedThroughputDescriptionModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    table_size_bytes: Optional[int] = Field(default=None, alias="TableSizeBytes")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    table_arn: Optional[str] = Field(default=None, alias="TableArn")
    table_id: Optional[str] = Field(default=None, alias="TableId")
    billing_mode_summary: Optional[BillingModeSummaryModel] = Field(
        default=None, alias="BillingModeSummary"
    )
    local_secondary_indexes: Optional[
        List[LocalSecondaryIndexDescriptionModel]
    ] = Field(default=None, alias="LocalSecondaryIndexes")
    global_secondary_indexes: Optional[
        List[GlobalSecondaryIndexDescriptionModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    stream_specification: Optional[StreamSpecificationModel] = Field(
        default=None, alias="StreamSpecification"
    )
    latest_stream_label: Optional[str] = Field(default=None, alias="LatestStreamLabel")
    latest_stream_arn: Optional[str] = Field(default=None, alias="LatestStreamArn")
    global_table_version: Optional[str] = Field(
        default=None, alias="GlobalTableVersion"
    )
    replicas: Optional[List[ReplicaDescriptionModel]] = Field(
        default=None, alias="Replicas"
    )
    restore_summary: Optional[RestoreSummaryModel] = Field(
        default=None, alias="RestoreSummary"
    )
    s_s_edescription: Optional[SSEDescriptionModel] = Field(
        default=None, alias="SSEDescription"
    )
    archival_summary: Optional[ArchivalSummaryModel] = Field(
        default=None, alias="ArchivalSummary"
    )
    table_class_summary: Optional[TableClassSummaryModel] = Field(
        default=None, alias="TableClassSummary"
    )


class ReplicationGroupUpdateModel(BaseModel):
    create: Optional[CreateReplicationGroupMemberActionModel] = Field(
        default=None, alias="Create"
    )
    update: Optional[UpdateReplicationGroupMemberActionModel] = Field(
        default=None, alias="Update"
    )
    delete: Optional[DeleteReplicationGroupMemberActionModel] = Field(
        default=None, alias="Delete"
    )


class ReplicaAutoScalingDescriptionModel(BaseModel):
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    global_secondary_indexes: Optional[
        List[ReplicaGlobalSecondaryIndexAutoScalingDescriptionModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    replica_provisioned_read_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ReplicaProvisionedReadCapacityAutoScalingSettings")
    replica_provisioned_write_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ReplicaProvisionedWriteCapacityAutoScalingSettings")
    replica_status: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "CREATION_FAILED",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "REGION_DISABLED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="ReplicaStatus")


class ReplicaSettingsDescriptionModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    replica_status: Optional[
        Literal[
            "ACTIVE",
            "CREATING",
            "CREATION_FAILED",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "REGION_DISABLED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="ReplicaStatus")
    replica_billing_mode_summary: Optional[BillingModeSummaryModel] = Field(
        default=None, alias="ReplicaBillingModeSummary"
    )
    replica_provisioned_read_capacity_units: Optional[int] = Field(
        default=None, alias="ReplicaProvisionedReadCapacityUnits"
    )
    replica_provisioned_read_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ReplicaProvisionedReadCapacityAutoScalingSettings")
    replica_provisioned_write_capacity_units: Optional[int] = Field(
        default=None, alias="ReplicaProvisionedWriteCapacityUnits"
    )
    replica_provisioned_write_capacity_auto_scaling_settings: Optional[
        AutoScalingSettingsDescriptionModel
    ] = Field(default=None, alias="ReplicaProvisionedWriteCapacityAutoScalingSettings")
    replica_global_secondary_index_settings: Optional[
        List[ReplicaGlobalSecondaryIndexSettingsDescriptionModel]
    ] = Field(default=None, alias="ReplicaGlobalSecondaryIndexSettings")
    replica_table_class_summary: Optional[TableClassSummaryModel] = Field(
        default=None, alias="ReplicaTableClassSummary"
    )


class ReplicaAutoScalingUpdateModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    replica_global_secondary_index_updates: Optional[
        Sequence[ReplicaGlobalSecondaryIndexAutoScalingUpdateModel]
    ] = Field(default=None, alias="ReplicaGlobalSecondaryIndexUpdates")
    replica_provisioned_read_capacity_auto_scaling_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(default=None, alias="ReplicaProvisionedReadCapacityAutoScalingUpdate")


class ReplicaSettingsUpdateModel(BaseModel):
    region_name: str = Field(alias="RegionName")
    replica_provisioned_read_capacity_units: Optional[int] = Field(
        default=None, alias="ReplicaProvisionedReadCapacityUnits"
    )
    replica_provisioned_read_capacity_auto_scaling_settings_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(
        default=None, alias="ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate"
    )
    replica_global_secondary_index_settings_update: Optional[
        Sequence[ReplicaGlobalSecondaryIndexSettingsUpdateModel]
    ] = Field(default=None, alias="ReplicaGlobalSecondaryIndexSettingsUpdate")
    replica_table_class: Optional[
        Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]
    ] = Field(default=None, alias="ReplicaTableClass")


class DeleteBackupOutputModel(BaseModel):
    backup_description: BackupDescriptionModel = Field(alias="BackupDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBackupOutputModel(BaseModel):
    backup_description: BackupDescriptionModel = Field(alias="BackupDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImportOutputModel(BaseModel):
    import_table_description: ImportTableDescriptionModel = Field(
        alias="ImportTableDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportTableOutputModel(BaseModel):
    import_table_description: ImportTableDescriptionModel = Field(
        alias="ImportTableDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTableOutputTableModel(BaseModel):
    table_description: TableDescriptionTableModel = Field(alias="TableDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableInputTableUpdateModel(BaseModel):
    attribute_definitions: Optional[Sequence[AttributeDefinitionTableModel]] = Field(
        default=None, alias="AttributeDefinitions"
    )
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )
    provisioned_throughput: Optional[ProvisionedThroughputTableModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    global_secondary_index_updates: Optional[
        Sequence[GlobalSecondaryIndexUpdateTableModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexUpdates")
    stream_specification: Optional[StreamSpecificationTableModel] = Field(
        default=None, alias="StreamSpecification"
    )
    s_s_especification: Optional[SSESpecificationTableModel] = Field(
        default=None, alias="SSESpecification"
    )
    replica_updates: Optional[Sequence[ReplicationGroupUpdateTableModel]] = Field(
        default=None, alias="ReplicaUpdates"
    )
    table_class: Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]] = Field(
        default=None, alias="TableClass"
    )


class CreateGlobalTableOutputModel(BaseModel):
    global_table_description: GlobalTableDescriptionModel = Field(
        alias="GlobalTableDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGlobalTableOutputModel(BaseModel):
    global_table_description: GlobalTableDescriptionModel = Field(
        alias="GlobalTableDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGlobalTableOutputModel(BaseModel):
    global_table_description: GlobalTableDescriptionModel = Field(
        alias="GlobalTableDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTableOutputModel(BaseModel):
    table_description: TableDescriptionModel = Field(alias="TableDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTableOutputModel(BaseModel):
    table_description: TableDescriptionModel = Field(alias="TableDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTableOutputModel(BaseModel):
    table: TableDescriptionModel = Field(alias="Table")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreTableFromBackupOutputModel(BaseModel):
    table_description: TableDescriptionModel = Field(alias="TableDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreTableToPointInTimeOutputModel(BaseModel):
    table_description: TableDescriptionModel = Field(alias="TableDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableOutputModel(BaseModel):
    table_description: TableDescriptionModel = Field(alias="TableDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    attribute_definitions: Optional[Sequence[AttributeDefinitionModel]] = Field(
        default=None, alias="AttributeDefinitions"
    )
    billing_mode: Optional[Literal["PAY_PER_REQUEST", "PROVISIONED"]] = Field(
        default=None, alias="BillingMode"
    )
    provisioned_throughput: Optional[ProvisionedThroughputModel] = Field(
        default=None, alias="ProvisionedThroughput"
    )
    global_secondary_index_updates: Optional[
        Sequence[GlobalSecondaryIndexUpdateModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexUpdates")
    stream_specification: Optional[StreamSpecificationModel] = Field(
        default=None, alias="StreamSpecification"
    )
    s_s_especification: Optional[SSESpecificationModel] = Field(
        default=None, alias="SSESpecification"
    )
    replica_updates: Optional[Sequence[ReplicationGroupUpdateModel]] = Field(
        default=None, alias="ReplicaUpdates"
    )
    table_class: Optional[Literal["STANDARD", "STANDARD_INFREQUENT_ACCESS"]] = Field(
        default=None, alias="TableClass"
    )


class TableAutoScalingDescriptionModel(BaseModel):
    table_name: Optional[str] = Field(default=None, alias="TableName")
    table_status: Optional[
        Literal[
            "ACTIVE",
            "ARCHIVED",
            "ARCHIVING",
            "CREATING",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
            "UPDATING",
        ]
    ] = Field(default=None, alias="TableStatus")
    replicas: Optional[List[ReplicaAutoScalingDescriptionModel]] = Field(
        default=None, alias="Replicas"
    )


class DescribeGlobalTableSettingsOutputModel(BaseModel):
    global_table_name: str = Field(alias="GlobalTableName")
    replica_settings: List[ReplicaSettingsDescriptionModel] = Field(
        alias="ReplicaSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGlobalTableSettingsOutputModel(BaseModel):
    global_table_name: str = Field(alias="GlobalTableName")
    replica_settings: List[ReplicaSettingsDescriptionModel] = Field(
        alias="ReplicaSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableReplicaAutoScalingInputRequestModel(BaseModel):
    table_name: str = Field(alias="TableName")
    global_secondary_index_updates: Optional[
        Sequence[GlobalSecondaryIndexAutoScalingUpdateModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexUpdates")
    provisioned_write_capacity_auto_scaling_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(default=None, alias="ProvisionedWriteCapacityAutoScalingUpdate")
    replica_updates: Optional[Sequence[ReplicaAutoScalingUpdateModel]] = Field(
        default=None, alias="ReplicaUpdates"
    )


class UpdateGlobalTableSettingsInputRequestModel(BaseModel):
    global_table_name: str = Field(alias="GlobalTableName")
    global_table_billing_mode: Optional[
        Literal["PAY_PER_REQUEST", "PROVISIONED"]
    ] = Field(default=None, alias="GlobalTableBillingMode")
    global_table_provisioned_write_capacity_units: Optional[int] = Field(
        default=None, alias="GlobalTableProvisionedWriteCapacityUnits"
    )
    global_table_provisioned_write_capacity_auto_scaling_settings_update: Optional[
        AutoScalingSettingsUpdateModel
    ] = Field(
        default=None,
        alias="GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate",
    )
    global_table_global_secondary_index_settings_update: Optional[
        Sequence[GlobalTableGlobalSecondaryIndexSettingsUpdateModel]
    ] = Field(default=None, alias="GlobalTableGlobalSecondaryIndexSettingsUpdate")
    replica_settings_update: Optional[Sequence[ReplicaSettingsUpdateModel]] = Field(
        default=None, alias="ReplicaSettingsUpdate"
    )


class DescribeTableReplicaAutoScalingOutputModel(BaseModel):
    table_auto_scaling_description: TableAutoScalingDescriptionModel = Field(
        alias="TableAutoScalingDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTableReplicaAutoScalingOutputModel(BaseModel):
    table_auto_scaling_description: TableAutoScalingDescriptionModel = Field(
        alias="TableAutoScalingDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
