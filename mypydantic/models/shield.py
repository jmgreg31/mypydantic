# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseActionModel(BaseModel):
    block: Optional[Dict[str, Any]] = Field(default=None, alias="Block")
    count: Optional[Dict[str, Any]] = Field(default=None, alias="Count")


class AssociateDRTLogBucketRequestModel(BaseModel):
    log_bucket: str = Field(alias="LogBucket")


class AssociateDRTRoleRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")


class AssociateHealthCheckRequestModel(BaseModel):
    protection_id: str = Field(alias="ProtectionId")
    health_check_arn: str = Field(alias="HealthCheckArn")


class EmergencyContactModel(BaseModel):
    email_address: str = Field(alias="EmailAddress")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    contact_notes: Optional[str] = Field(default=None, alias="ContactNotes")


class MitigationModel(BaseModel):
    mitigation_name: Optional[str] = Field(default=None, alias="MitigationName")


class SummarizedCounterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    max: Optional[float] = Field(default=None, alias="Max")
    average: Optional[float] = Field(default=None, alias="Average")
    sum: Optional[float] = Field(default=None, alias="Sum")
    n: Optional[int] = Field(default=None, alias="N")
    unit: Optional[str] = Field(default=None, alias="Unit")


class ContributorModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[int] = Field(default=None, alias="Value")


class AttackVectorDescriptionModel(BaseModel):
    vector_type: str = Field(alias="VectorType")


class AttackVolumeStatisticsModel(BaseModel):
    max: float = Field(alias="Max")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteProtectionGroupRequestModel(BaseModel):
    protection_group_id: str = Field(alias="ProtectionGroupId")


class DeleteProtectionRequestModel(BaseModel):
    protection_id: str = Field(alias="ProtectionId")


class DescribeAttackRequestModel(BaseModel):
    attack_id: str = Field(alias="AttackId")


class TimeRangeModel(BaseModel):
    from_inclusive: Optional[datetime] = Field(default=None, alias="FromInclusive")
    to_exclusive: Optional[datetime] = Field(default=None, alias="ToExclusive")


class DescribeProtectionGroupRequestModel(BaseModel):
    protection_group_id: str = Field(alias="ProtectionGroupId")


class ProtectionGroupModel(BaseModel):
    protection_group_id: str = Field(alias="ProtectionGroupId")
    aggregation: Literal["MAX", "MEAN", "SUM"] = Field(alias="Aggregation")
    pattern: Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"] = Field(alias="Pattern")
    members: List[str] = Field(alias="Members")
    resource_type: Optional[
        Literal[
            "APPLICATION_LOAD_BALANCER",
            "CLASSIC_LOAD_BALANCER",
            "CLOUDFRONT_DISTRIBUTION",
            "ELASTIC_IP_ALLOCATION",
            "GLOBAL_ACCELERATOR",
            "ROUTE_53_HOSTED_ZONE",
        ]
    ] = Field(default=None, alias="ResourceType")
    protection_group_arn: Optional[str] = Field(
        default=None, alias="ProtectionGroupArn"
    )


class DescribeProtectionRequestModel(BaseModel):
    protection_id: Optional[str] = Field(default=None, alias="ProtectionId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class DisableApplicationLayerAutomaticResponseRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DisassociateDRTLogBucketRequestModel(BaseModel):
    log_bucket: str = Field(alias="LogBucket")


class DisassociateHealthCheckRequestModel(BaseModel):
    protection_id: str = Field(alias="ProtectionId")
    health_check_arn: str = Field(alias="HealthCheckArn")


class InclusionProtectionFiltersModel(BaseModel):
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="ResourceArns")
    protection_names: Optional[Sequence[str]] = Field(
        default=None, alias="ProtectionNames"
    )
    resource_types: Optional[
        Sequence[
            Literal[
                "APPLICATION_LOAD_BALANCER",
                "CLASSIC_LOAD_BALANCER",
                "CLOUDFRONT_DISTRIBUTION",
                "ELASTIC_IP_ALLOCATION",
                "GLOBAL_ACCELERATOR",
                "ROUTE_53_HOSTED_ZONE",
            ]
        ]
    ] = Field(default=None, alias="ResourceTypes")


class InclusionProtectionGroupFiltersModel(BaseModel):
    protection_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ProtectionGroupIds"
    )
    patterns: Optional[
        Sequence[Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"]]
    ] = Field(default=None, alias="Patterns")
    resource_types: Optional[
        Sequence[
            Literal[
                "APPLICATION_LOAD_BALANCER",
                "CLASSIC_LOAD_BALANCER",
                "CLOUDFRONT_DISTRIBUTION",
                "ELASTIC_IP_ALLOCATION",
                "GLOBAL_ACCELERATOR",
                "ROUTE_53_HOSTED_ZONE",
            ]
        ]
    ] = Field(default=None, alias="ResourceTypes")
    aggregations: Optional[Sequence[Literal["MAX", "MEAN", "SUM"]]] = Field(
        default=None, alias="Aggregations"
    )


class LimitModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    max: Optional[int] = Field(default=None, alias="Max")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListResourcesInProtectionGroupRequestModel(BaseModel):
    protection_group_id: str = Field(alias="ProtectionGroupId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class ProtectionGroupArbitraryPatternLimitsModel(BaseModel):
    max_members: int = Field(alias="MaxMembers")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateProtectionGroupRequestModel(BaseModel):
    protection_group_id: str = Field(alias="ProtectionGroupId")
    aggregation: Literal["MAX", "MEAN", "SUM"] = Field(alias="Aggregation")
    pattern: Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"] = Field(alias="Pattern")
    resource_type: Optional[
        Literal[
            "APPLICATION_LOAD_BALANCER",
            "CLASSIC_LOAD_BALANCER",
            "CLOUDFRONT_DISTRIBUTION",
            "ELASTIC_IP_ALLOCATION",
            "GLOBAL_ACCELERATOR",
            "ROUTE_53_HOSTED_ZONE",
        ]
    ] = Field(default=None, alias="ResourceType")
    members: Optional[Sequence[str]] = Field(default=None, alias="Members")


class UpdateSubscriptionRequestModel(BaseModel):
    auto_renew: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AutoRenew"
    )


class ApplicationLayerAutomaticResponseConfigurationModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")
    action: ResponseActionModel = Field(alias="Action")


class EnableApplicationLayerAutomaticResponseRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    action: ResponseActionModel = Field(alias="Action")


class UpdateApplicationLayerAutomaticResponseRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    action: ResponseActionModel = Field(alias="Action")


class AssociateProactiveEngagementDetailsRequestModel(BaseModel):
    emergency_contact_list: Sequence[EmergencyContactModel] = Field(
        alias="EmergencyContactList"
    )


class UpdateEmergencyContactSettingsRequestModel(BaseModel):
    emergency_contact_list: Optional[Sequence[EmergencyContactModel]] = Field(
        default=None, alias="EmergencyContactList"
    )


class SummarizedAttackVectorModel(BaseModel):
    vector_type: str = Field(alias="VectorType")
    vector_counters: Optional[List[SummarizedCounterModel]] = Field(
        default=None, alias="VectorCounters"
    )


class AttackPropertyModel(BaseModel):
    attack_layer: Optional[Literal["APPLICATION", "NETWORK"]] = Field(
        default=None, alias="AttackLayer"
    )
    attack_property_identifier: Optional[
        Literal[
            "DESTINATION_URL",
            "REFERRER",
            "SOURCE_ASN",
            "SOURCE_COUNTRY",
            "SOURCE_IP_ADDRESS",
            "SOURCE_USER_AGENT",
            "WORDPRESS_PINGBACK_REFLECTOR",
            "WORDPRESS_PINGBACK_SOURCE",
        ]
    ] = Field(default=None, alias="AttackPropertyIdentifier")
    top_contributors: Optional[List[ContributorModel]] = Field(
        default=None, alias="TopContributors"
    )
    unit: Optional[Literal["BITS", "BYTES", "PACKETS", "REQUESTS"]] = Field(
        default=None, alias="Unit"
    )
    total: Optional[int] = Field(default=None, alias="Total")


class AttackSummaryModel(BaseModel):
    attack_id: Optional[str] = Field(default=None, alias="AttackId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    attack_vectors: Optional[List[AttackVectorDescriptionModel]] = Field(
        default=None, alias="AttackVectors"
    )


class AttackVolumeModel(BaseModel):
    bits_per_second: Optional[AttackVolumeStatisticsModel] = Field(
        default=None, alias="BitsPerSecond"
    )
    packets_per_second: Optional[AttackVolumeStatisticsModel] = Field(
        default=None, alias="PacketsPerSecond"
    )
    requests_per_second: Optional[AttackVolumeStatisticsModel] = Field(
        default=None, alias="RequestsPerSecond"
    )


class CreateProtectionGroupRequestModel(BaseModel):
    protection_group_id: str = Field(alias="ProtectionGroupId")
    aggregation: Literal["MAX", "MEAN", "SUM"] = Field(alias="Aggregation")
    pattern: Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"] = Field(alias="Pattern")
    resource_type: Optional[
        Literal[
            "APPLICATION_LOAD_BALANCER",
            "CLASSIC_LOAD_BALANCER",
            "CLOUDFRONT_DISTRIBUTION",
            "ELASTIC_IP_ALLOCATION",
            "GLOBAL_ACCELERATOR",
            "ROUTE_53_HOSTED_ZONE",
        ]
    ] = Field(default=None, alias="ResourceType")
    members: Optional[Sequence[str]] = Field(default=None, alias="Members")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateProtectionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    resource_arn: str = Field(alias="ResourceArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateProtectionResponseModel(BaseModel):
    protection_id: str = Field(alias="ProtectionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDRTAccessResponseModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    log_bucket_list: List[str] = Field(alias="LogBucketList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEmergencyContactSettingsResponseModel(BaseModel):
    emergency_contact_list: List[EmergencyContactModel] = Field(
        alias="EmergencyContactList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSubscriptionStateResponseModel(BaseModel):
    subscription_state: Literal["ACTIVE", "INACTIVE"] = Field(alias="SubscriptionState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesInProtectionGroupResponseModel(BaseModel):
    resource_arns: List[str] = Field(alias="ResourceArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttacksRequestModel(BaseModel):
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="ResourceArns")
    start_time: Optional[TimeRangeModel] = Field(default=None, alias="StartTime")
    end_time: Optional[TimeRangeModel] = Field(default=None, alias="EndTime")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeProtectionGroupResponseModel(BaseModel):
    protection_group: ProtectionGroupModel = Field(alias="ProtectionGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProtectionGroupsResponseModel(BaseModel):
    protection_groups: List[ProtectionGroupModel] = Field(alias="ProtectionGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProtectionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    inclusion_filters: Optional[InclusionProtectionFiltersModel] = Field(
        default=None, alias="InclusionFilters"
    )


class ListProtectionGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    inclusion_filters: Optional[InclusionProtectionGroupFiltersModel] = Field(
        default=None, alias="InclusionFilters"
    )


class ProtectionLimitsModel(BaseModel):
    protected_resource_type_limits: List[LimitModel] = Field(
        alias="ProtectedResourceTypeLimits"
    )


class ListAttacksRequestListAttacksPaginateModel(BaseModel):
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="ResourceArns")
    start_time: Optional[TimeRangeModel] = Field(default=None, alias="StartTime")
    end_time: Optional[TimeRangeModel] = Field(default=None, alias="EndTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProtectionsRequestListProtectionsPaginateModel(BaseModel):
    inclusion_filters: Optional[InclusionProtectionFiltersModel] = Field(
        default=None, alias="InclusionFilters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ProtectionGroupPatternTypeLimitsModel(BaseModel):
    arbitrary_pattern_limits: ProtectionGroupArbitraryPatternLimitsModel = Field(
        alias="ArbitraryPatternLimits"
    )


class ProtectionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    health_check_ids: Optional[List[str]] = Field(default=None, alias="HealthCheckIds")
    protection_arn: Optional[str] = Field(default=None, alias="ProtectionArn")
    application_layer_automatic_response_configuration: Optional[
        ApplicationLayerAutomaticResponseConfigurationModel
    ] = Field(default=None, alias="ApplicationLayerAutomaticResponseConfiguration")


class SubResourceSummaryModel(BaseModel):
    type: Optional[Literal["IP", "URL"]] = Field(default=None, alias="Type")
    id: Optional[str] = Field(default=None, alias="Id")
    attack_vectors: Optional[List[SummarizedAttackVectorModel]] = Field(
        default=None, alias="AttackVectors"
    )
    counters: Optional[List[SummarizedCounterModel]] = Field(
        default=None, alias="Counters"
    )


class ListAttacksResponseModel(BaseModel):
    attack_summaries: List[AttackSummaryModel] = Field(alias="AttackSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttackStatisticsDataItemModel(BaseModel):
    attack_count: int = Field(alias="AttackCount")
    attack_volume: Optional[AttackVolumeModel] = Field(
        default=None, alias="AttackVolume"
    )


class ProtectionGroupLimitsModel(BaseModel):
    max_protection_groups: int = Field(alias="MaxProtectionGroups")
    pattern_type_limits: ProtectionGroupPatternTypeLimitsModel = Field(
        alias="PatternTypeLimits"
    )


class DescribeProtectionResponseModel(BaseModel):
    protection: ProtectionModel = Field(alias="Protection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProtectionsResponseModel(BaseModel):
    protections: List[ProtectionModel] = Field(alias="Protections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttackDetailModel(BaseModel):
    attack_id: Optional[str] = Field(default=None, alias="AttackId")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    sub_resources: Optional[List[SubResourceSummaryModel]] = Field(
        default=None, alias="SubResources"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    attack_counters: Optional[List[SummarizedCounterModel]] = Field(
        default=None, alias="AttackCounters"
    )
    attack_properties: Optional[List[AttackPropertyModel]] = Field(
        default=None, alias="AttackProperties"
    )
    mitigations: Optional[List[MitigationModel]] = Field(
        default=None, alias="Mitigations"
    )


class DescribeAttackStatisticsResponseModel(BaseModel):
    time_range: TimeRangeModel = Field(alias="TimeRange")
    data_items: List[AttackStatisticsDataItemModel] = Field(alias="DataItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubscriptionLimitsModel(BaseModel):
    protection_limits: ProtectionLimitsModel = Field(alias="ProtectionLimits")
    protection_group_limits: ProtectionGroupLimitsModel = Field(
        alias="ProtectionGroupLimits"
    )


class DescribeAttackResponseModel(BaseModel):
    attack: AttackDetailModel = Field(alias="Attack")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubscriptionModel(BaseModel):
    subscription_limits: SubscriptionLimitsModel = Field(alias="SubscriptionLimits")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    time_commitment_in_seconds: Optional[int] = Field(
        default=None, alias="TimeCommitmentInSeconds"
    )
    auto_renew: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AutoRenew"
    )
    limits: Optional[List[LimitModel]] = Field(default=None, alias="Limits")
    proactive_engagement_status: Optional[
        Literal["DISABLED", "ENABLED", "PENDING"]
    ] = Field(default=None, alias="ProactiveEngagementStatus")
    subscription_arn: Optional[str] = Field(default=None, alias="SubscriptionArn")


class DescribeSubscriptionResponseModel(BaseModel):
    subscription: SubscriptionModel = Field(alias="Subscription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
