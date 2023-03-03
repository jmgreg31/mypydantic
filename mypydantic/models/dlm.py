# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class RetentionArchiveTierModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")
    interval: Optional[int] = Field(default=None, alias="Interval")
    interval_unit: Optional[Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]] = Field(
        default=None, alias="IntervalUnit"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateRuleModel(BaseModel):
    location: Optional[Literal["CLOUD", "OUTPOST_LOCAL"]] = Field(
        default=None, alias="Location"
    )
    interval: Optional[int] = Field(default=None, alias="Interval")
    interval_unit: Optional[Literal["HOURS"]] = Field(
        default=None, alias="IntervalUnit"
    )
    times: Optional[Sequence[str]] = Field(default=None, alias="Times")
    cron_expression: Optional[str] = Field(default=None, alias="CronExpression")


class CrossRegionCopyRetainRuleModel(BaseModel):
    interval: Optional[int] = Field(default=None, alias="Interval")
    interval_unit: Optional[Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]] = Field(
        default=None, alias="IntervalUnit"
    )


class EncryptionConfigurationModel(BaseModel):
    encrypted: bool = Field(alias="Encrypted")
    cmk_arn: Optional[str] = Field(default=None, alias="CmkArn")


class CrossRegionCopyDeprecateRuleModel(BaseModel):
    interval: Optional[int] = Field(default=None, alias="Interval")
    interval_unit: Optional[Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]] = Field(
        default=None, alias="IntervalUnit"
    )


class DeleteLifecyclePolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")


class DeprecateRuleModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")
    interval: Optional[int] = Field(default=None, alias="Interval")
    interval_unit: Optional[Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]] = Field(
        default=None, alias="IntervalUnit"
    )


class EventParametersModel(BaseModel):
    event_type: Literal["shareSnapshot"] = Field(alias="EventType")
    snapshot_owner: Sequence[str] = Field(alias="SnapshotOwner")
    description_regex: str = Field(alias="DescriptionRegex")


class FastRestoreRuleModel(BaseModel):
    availability_zones: Sequence[str] = Field(alias="AvailabilityZones")
    count: Optional[int] = Field(default=None, alias="Count")
    interval: Optional[int] = Field(default=None, alias="Interval")
    interval_unit: Optional[Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]] = Field(
        default=None, alias="IntervalUnit"
    )


class GetLifecyclePoliciesRequestModel(BaseModel):
    policy_ids: Optional[Sequence[str]] = Field(default=None, alias="PolicyIds")
    state: Optional[Literal["DISABLED", "ENABLED", "ERROR"]] = Field(
        default=None, alias="State"
    )
    resource_types: Optional[Sequence[Literal["INSTANCE", "VOLUME"]]] = Field(
        default=None, alias="ResourceTypes"
    )
    target_tags: Optional[Sequence[str]] = Field(default=None, alias="TargetTags")
    tags_to_add: Optional[Sequence[str]] = Field(default=None, alias="TagsToAdd")


class LifecyclePolicySummaryModel(BaseModel):
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    description: Optional[str] = Field(default=None, alias="Description")
    state: Optional[Literal["DISABLED", "ENABLED", "ERROR"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    policy_type: Optional[
        Literal["EBS_SNAPSHOT_MANAGEMENT", "EVENT_BASED_POLICY", "IMAGE_MANAGEMENT"]
    ] = Field(default=None, alias="PolicyType")


class GetLifecyclePolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class RetainRuleModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")
    interval: Optional[int] = Field(default=None, alias="Interval")
    interval_unit: Optional[Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]] = Field(
        default=None, alias="IntervalUnit"
    )


class ShareRuleModel(BaseModel):
    target_accounts: Sequence[str] = Field(alias="TargetAccounts")
    unshare_interval: Optional[int] = Field(default=None, alias="UnshareInterval")
    unshare_interval_unit: Optional[
        Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]
    ] = Field(default=None, alias="UnshareIntervalUnit")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ArchiveRetainRuleModel(BaseModel):
    retention_archive_tier: RetentionArchiveTierModel = Field(
        alias="RetentionArchiveTier"
    )


class CreateLifecyclePolicyResponseModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CrossRegionCopyActionModel(BaseModel):
    target: str = Field(alias="Target")
    encryption_configuration: EncryptionConfigurationModel = Field(
        alias="EncryptionConfiguration"
    )
    retain_rule: Optional[CrossRegionCopyRetainRuleModel] = Field(
        default=None, alias="RetainRule"
    )


class CrossRegionCopyRuleModel(BaseModel):
    encrypted: bool = Field(alias="Encrypted")
    target_region: Optional[str] = Field(default=None, alias="TargetRegion")
    target: Optional[str] = Field(default=None, alias="Target")
    cmk_arn: Optional[str] = Field(default=None, alias="CmkArn")
    copy_tags: Optional[bool] = Field(default=None, alias="CopyTags")
    retain_rule: Optional[CrossRegionCopyRetainRuleModel] = Field(
        default=None, alias="RetainRule"
    )
    deprecate_rule: Optional[CrossRegionCopyDeprecateRuleModel] = Field(
        default=None, alias="DeprecateRule"
    )


class EventSourceModel(BaseModel):
    type: Literal["MANAGED_CWE"] = Field(alias="Type")
    parameters: Optional[EventParametersModel] = Field(default=None, alias="Parameters")


class GetLifecyclePoliciesResponseModel(BaseModel):
    policies: List[LifecyclePolicySummaryModel] = Field(alias="Policies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ParametersModel(BaseModel):
    exclude_boot_volume: Optional[bool] = Field(default=None, alias="ExcludeBootVolume")
    no_reboot: Optional[bool] = Field(default=None, alias="NoReboot")
    exclude_data_volume_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="ExcludeDataVolumeTags"
    )


class ArchiveRuleModel(BaseModel):
    retain_rule: ArchiveRetainRuleModel = Field(alias="RetainRule")


class ActionModel(BaseModel):
    name: str = Field(alias="Name")
    cross_region_copy: Sequence[CrossRegionCopyActionModel] = Field(
        alias="CrossRegionCopy"
    )


class ScheduleModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    copy_tags: Optional[bool] = Field(default=None, alias="CopyTags")
    tags_to_add: Optional[Sequence[TagModel]] = Field(default=None, alias="TagsToAdd")
    variable_tags: Optional[Sequence[TagModel]] = Field(
        default=None, alias="VariableTags"
    )
    create_rule: Optional[CreateRuleModel] = Field(default=None, alias="CreateRule")
    retain_rule: Optional[RetainRuleModel] = Field(default=None, alias="RetainRule")
    fast_restore_rule: Optional[FastRestoreRuleModel] = Field(
        default=None, alias="FastRestoreRule"
    )
    cross_region_copy_rules: Optional[Sequence[CrossRegionCopyRuleModel]] = Field(
        default=None, alias="CrossRegionCopyRules"
    )
    share_rules: Optional[Sequence[ShareRuleModel]] = Field(
        default=None, alias="ShareRules"
    )
    deprecate_rule: Optional[DeprecateRuleModel] = Field(
        default=None, alias="DeprecateRule"
    )
    archive_rule: Optional[ArchiveRuleModel] = Field(default=None, alias="ArchiveRule")


class PolicyDetailsModel(BaseModel):
    policy_type: Optional[
        Literal["EBS_SNAPSHOT_MANAGEMENT", "EVENT_BASED_POLICY", "IMAGE_MANAGEMENT"]
    ] = Field(default=None, alias="PolicyType")
    resource_types: Optional[Sequence[Literal["INSTANCE", "VOLUME"]]] = Field(
        default=None, alias="ResourceTypes"
    )
    resource_locations: Optional[Sequence[Literal["CLOUD", "OUTPOST"]]] = Field(
        default=None, alias="ResourceLocations"
    )
    target_tags: Optional[Sequence[TagModel]] = Field(default=None, alias="TargetTags")
    schedules: Optional[Sequence[ScheduleModel]] = Field(
        default=None, alias="Schedules"
    )
    parameters: Optional[ParametersModel] = Field(default=None, alias="Parameters")
    event_source: Optional[EventSourceModel] = Field(default=None, alias="EventSource")
    actions: Optional[Sequence[ActionModel]] = Field(default=None, alias="Actions")


class CreateLifecyclePolicyRequestModel(BaseModel):
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    description: str = Field(alias="Description")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="State")
    policy_details: PolicyDetailsModel = Field(alias="PolicyDetails")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class LifecyclePolicyModel(BaseModel):
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    description: Optional[str] = Field(default=None, alias="Description")
    state: Optional[Literal["DISABLED", "ENABLED", "ERROR"]] = Field(
        default=None, alias="State"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_modified: Optional[datetime] = Field(default=None, alias="DateModified")
    policy_details: Optional[PolicyDetailsModel] = Field(
        default=None, alias="PolicyDetails"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")


class UpdateLifecyclePolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="State")
    description: Optional[str] = Field(default=None, alias="Description")
    policy_details: Optional[PolicyDetailsModel] = Field(
        default=None, alias="PolicyDetails"
    )


class GetLifecyclePolicyResponseModel(BaseModel):
    policy: LifecyclePolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
