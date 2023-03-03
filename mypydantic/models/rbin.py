# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResourceTagModel(BaseModel):
    resource_tag_key: str = Field(alias="ResourceTagKey")
    resource_tag_value: Optional[str] = Field(default=None, alias="ResourceTagValue")


class RetentionPeriodModel(BaseModel):
    retention_period_value: int = Field(alias="RetentionPeriodValue")
    retention_period_unit: Literal["DAYS"] = Field(alias="RetentionPeriodUnit")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteRuleRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class GetRuleRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class UnlockDelayModel(BaseModel):
    unlock_delay_value: int = Field(alias="UnlockDelayValue")
    unlock_delay_unit: Literal["DAYS"] = Field(alias="UnlockDelayUnit")


class UnlockRuleRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ListRulesRequestModel(BaseModel):
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    resource_tags: Optional[Sequence[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )
    lock_state: Optional[Literal["locked", "pending_unlock", "unlocked"]] = Field(
        default=None, alias="LockState"
    )


class RuleSummaryModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    description: Optional[str] = Field(default=None, alias="Description")
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="RetentionPeriod"
    )
    lock_state: Optional[Literal["locked", "pending_unlock", "unlocked"]] = Field(
        default=None, alias="LockState"
    )


class UpdateRuleRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    retention_period: Optional[RetentionPeriodModel] = Field(
        default=None, alias="RetentionPeriod"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    resource_type: Optional[Literal["EBS_SNAPSHOT", "EC2_IMAGE"]] = Field(
        default=None, alias="ResourceType"
    )
    resource_tags: Optional[Sequence[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRuleResponseModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    retention_period: RetentionPeriodModel = Field(alias="RetentionPeriod")
    description: str = Field(alias="Description")
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    resource_tags: List[ResourceTagModel] = Field(alias="ResourceTags")
    status: Literal["available", "pending"] = Field(alias="Status")
    lock_state: Literal["locked", "pending_unlock", "unlocked"] = Field(
        alias="LockState"
    )
    lock_end_time: datetime = Field(alias="LockEndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRulesRequestListRulesPaginateModel(BaseModel):
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    resource_tags: Optional[Sequence[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )
    lock_state: Optional[Literal["locked", "pending_unlock", "unlocked"]] = Field(
        default=None, alias="LockState"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LockConfigurationModel(BaseModel):
    unlock_delay: UnlockDelayModel = Field(alias="UnlockDelay")


class ListRulesResponseModel(BaseModel):
    rules: List[RuleSummaryModel] = Field(alias="Rules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleRequestModel(BaseModel):
    retention_period: RetentionPeriodModel = Field(alias="RetentionPeriod")
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    resource_tags: Optional[Sequence[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )
    lock_configuration: Optional[LockConfigurationModel] = Field(
        default=None, alias="LockConfiguration"
    )


class CreateRuleResponseModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    retention_period: RetentionPeriodModel = Field(alias="RetentionPeriod")
    description: str = Field(alias="Description")
    tags: List[TagModel] = Field(alias="Tags")
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    resource_tags: List[ResourceTagModel] = Field(alias="ResourceTags")
    status: Literal["available", "pending"] = Field(alias="Status")
    lock_configuration: LockConfigurationModel = Field(alias="LockConfiguration")
    lock_state: Literal["locked", "pending_unlock", "unlocked"] = Field(
        alias="LockState"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRuleResponseModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    description: str = Field(alias="Description")
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    retention_period: RetentionPeriodModel = Field(alias="RetentionPeriod")
    resource_tags: List[ResourceTagModel] = Field(alias="ResourceTags")
    status: Literal["available", "pending"] = Field(alias="Status")
    lock_configuration: LockConfigurationModel = Field(alias="LockConfiguration")
    lock_state: Literal["locked", "pending_unlock", "unlocked"] = Field(
        alias="LockState"
    )
    lock_end_time: datetime = Field(alias="LockEndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LockRuleRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    lock_configuration: LockConfigurationModel = Field(alias="LockConfiguration")


class LockRuleResponseModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    description: str = Field(alias="Description")
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    retention_period: RetentionPeriodModel = Field(alias="RetentionPeriod")
    resource_tags: List[ResourceTagModel] = Field(alias="ResourceTags")
    status: Literal["available", "pending"] = Field(alias="Status")
    lock_configuration: LockConfigurationModel = Field(alias="LockConfiguration")
    lock_state: Literal["locked", "pending_unlock", "unlocked"] = Field(
        alias="LockState"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UnlockRuleResponseModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    description: str = Field(alias="Description")
    resource_type: Literal["EBS_SNAPSHOT", "EC2_IMAGE"] = Field(alias="ResourceType")
    retention_period: RetentionPeriodModel = Field(alias="RetentionPeriod")
    resource_tags: List[ResourceTagModel] = Field(alias="ResourceTags")
    status: Literal["available", "pending"] = Field(alias="Status")
    lock_configuration: LockConfigurationModel = Field(alias="LockConfiguration")
    lock_state: Literal["locked", "pending_unlock", "unlocked"] = Field(
        alias="LockState"
    )
    lock_end_time: datetime = Field(alias="LockEndTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
