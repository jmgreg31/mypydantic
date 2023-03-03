# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class RegisterUsageRequestModel(BaseModel):
    product_code: str = Field(alias="ProductCode")
    public_key_version: int = Field(alias="PublicKeyVersion")
    nonce: Optional[str] = Field(default=None, alias="Nonce")


class ResolveCustomerRequestModel(BaseModel):
    registration_token: str = Field(alias="RegistrationToken")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class MeterUsageResultModel(BaseModel):
    metering_record_id: str = Field(alias="MeteringRecordId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterUsageResultModel(BaseModel):
    public_key_rotation_timestamp: datetime = Field(alias="PublicKeyRotationTimestamp")
    signature: str = Field(alias="Signature")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResolveCustomerResultModel(BaseModel):
    customer_identifier: str = Field(alias="CustomerIdentifier")
    product_code: str = Field(alias="ProductCode")
    customer_aws_account_id: str = Field(alias="CustomerAWSAccountId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsageAllocationModel(BaseModel):
    allocated_usage_quantity: int = Field(alias="AllocatedUsageQuantity")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class MeterUsageRequestModel(BaseModel):
    product_code: str = Field(alias="ProductCode")
    timestamp: Union[datetime, str] = Field(alias="Timestamp")
    usage_dimension: str = Field(alias="UsageDimension")
    usage_quantity: Optional[int] = Field(default=None, alias="UsageQuantity")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    usage_allocations: Optional[Sequence[UsageAllocationModel]] = Field(
        default=None, alias="UsageAllocations"
    )


class UsageRecordModel(BaseModel):
    timestamp: Union[datetime, str] = Field(alias="Timestamp")
    customer_identifier: str = Field(alias="CustomerIdentifier")
    dimension: str = Field(alias="Dimension")
    quantity: Optional[int] = Field(default=None, alias="Quantity")
    usage_allocations: Optional[Sequence[UsageAllocationModel]] = Field(
        default=None, alias="UsageAllocations"
    )


class BatchMeterUsageRequestModel(BaseModel):
    usage_records: Sequence[UsageRecordModel] = Field(alias="UsageRecords")
    product_code: str = Field(alias="ProductCode")


class UsageRecordResultModel(BaseModel):
    usage_record: Optional[UsageRecordModel] = Field(default=None, alias="UsageRecord")
    metering_record_id: Optional[str] = Field(default=None, alias="MeteringRecordId")
    status: Optional[
        Literal["CustomerNotSubscribed", "DuplicateRecord", "Success"]
    ] = Field(default=None, alias="Status")


class BatchMeterUsageResultModel(BaseModel):
    results: List[UsageRecordResultModel] = Field(alias="Results")
    unprocessed_records: List[UsageRecordModel] = Field(alias="UnprocessedRecords")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
