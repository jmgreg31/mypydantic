# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountEnrollmentStatusModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    status: Optional[Literal["Active", "Failed", "Inactive", "Pending"]] = Field(
        default=None, alias="status"
    )
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="lastUpdatedTimestamp"
    )


class AutoScalingGroupConfigurationModel(BaseModel):
    desired_capacity: Optional[int] = Field(default=None, alias="desiredCapacity")
    min_size: Optional[int] = Field(default=None, alias="minSize")
    max_size: Optional[int] = Field(default=None, alias="maxSize")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")


class UtilizationMetricModel(BaseModel):
    name: Optional[
        Literal[
            "Cpu",
            "DISK_READ_BYTES_PER_SECOND",
            "DISK_READ_OPS_PER_SECOND",
            "DISK_WRITE_BYTES_PER_SECOND",
            "DISK_WRITE_OPS_PER_SECOND",
            "EBS_READ_BYTES_PER_SECOND",
            "EBS_READ_OPS_PER_SECOND",
            "EBS_WRITE_BYTES_PER_SECOND",
            "EBS_WRITE_OPS_PER_SECOND",
            "Memory",
            "NETWORK_IN_BYTES_PER_SECOND",
            "NETWORK_OUT_BYTES_PER_SECOND",
            "NETWORK_PACKETS_IN_PER_SECOND",
            "NETWORK_PACKETS_OUT_PER_SECOND",
        ]
    ] = Field(default=None, alias="name")
    statistic: Optional[Literal["Average", "Maximum"]] = Field(
        default=None, alias="statistic"
    )
    value: Optional[float] = Field(default=None, alias="value")


class MemorySizeConfigurationModel(BaseModel):
    memory: Optional[int] = Field(default=None, alias="memory")
    memory_reservation: Optional[int] = Field(default=None, alias="memoryReservation")


class CurrentPerformanceRiskRatingsModel(BaseModel):
    high: Optional[int] = Field(default=None, alias="high")
    medium: Optional[int] = Field(default=None, alias="medium")
    low: Optional[int] = Field(default=None, alias="low")
    very_low: Optional[int] = Field(default=None, alias="veryLow")


class ScopeModel(BaseModel):
    name: Optional[Literal["AccountId", "Organization", "ResourceArn"]] = Field(
        default=None, alias="name"
    )
    value: Optional[str] = Field(default=None, alias="value")


class JobFilterModel(BaseModel):
    name: Optional[Literal["JobStatus", "ResourceType"]] = Field(
        default=None, alias="name"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EBSFilterModel(BaseModel):
    name: Optional[Literal["Finding"]] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class EBSUtilizationMetricModel(BaseModel):
    name: Optional[
        Literal[
            "VolumeReadBytesPerSecond",
            "VolumeReadOpsPerSecond",
            "VolumeWriteBytesPerSecond",
            "VolumeWriteOpsPerSecond",
        ]
    ] = Field(default=None, alias="name")
    statistic: Optional[Literal["Average", "Maximum"]] = Field(
        default=None, alias="statistic"
    )
    value: Optional[float] = Field(default=None, alias="value")


class ECSServiceProjectedMetricModel(BaseModel):
    name: Optional[Literal["Cpu", "Memory"]] = Field(default=None, alias="name")
    timestamps: Optional[List[datetime]] = Field(default=None, alias="timestamps")
    upper_bound_values: Optional[List[float]] = Field(
        default=None, alias="upperBoundValues"
    )
    lower_bound_values: Optional[List[float]] = Field(
        default=None, alias="lowerBoundValues"
    )


class ECSServiceProjectedUtilizationMetricModel(BaseModel):
    name: Optional[Literal["Cpu", "Memory"]] = Field(default=None, alias="name")
    statistic: Optional[Literal["Average", "Maximum"]] = Field(
        default=None, alias="statistic"
    )
    lower_bound_value: Optional[float] = Field(default=None, alias="lowerBoundValue")
    upper_bound_value: Optional[float] = Field(default=None, alias="upperBoundValue")


class ECSServiceRecommendationFilterModel(BaseModel):
    name: Optional[Literal["Finding", "FindingReasonCode"]] = Field(
        default=None, alias="name"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class ECSServiceUtilizationMetricModel(BaseModel):
    name: Optional[Literal["Cpu", "Memory"]] = Field(default=None, alias="name")
    statistic: Optional[Literal["Average", "Maximum"]] = Field(
        default=None, alias="statistic"
    )
    value: Optional[float] = Field(default=None, alias="value")


class ExternalMetricsPreferenceModel(BaseModel):
    source: Optional[Literal["Datadog", "Dynatrace", "Instana", "NewRelic"]] = Field(
        default=None, alias="source"
    )


class EnrollmentFilterModel(BaseModel):
    name: Optional[Literal["Status"]] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class EstimatedMonthlySavingsModel(BaseModel):
    currency: Optional[Literal["CNY", "USD"]] = Field(default=None, alias="currency")
    value: Optional[float] = Field(default=None, alias="value")


class FilterModel(BaseModel):
    name: Optional[
        Literal["Finding", "FindingReasonCodes", "RecommendationSourceType"]
    ] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class RecommendationPreferencesModel(BaseModel):
    cpu_vendor_architectures: Optional[
        Sequence[Literal["AWS_ARM64", "CURRENT"]]
    ] = Field(default=None, alias="cpuVendorArchitectures")


class S3DestinationConfigModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key_prefix: Optional[str] = Field(default=None, alias="keyPrefix")


class S3DestinationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key: Optional[str] = Field(default=None, alias="key")
    metadata_key: Optional[str] = Field(default=None, alias="metadataKey")


class LambdaFunctionRecommendationFilterModel(BaseModel):
    name: Optional[Literal["Finding", "FindingReasonCode"]] = Field(
        default=None, alias="name"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class GetRecommendationErrorModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="identifier")
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class GetECSServiceRecommendationProjectedMetricsRequestModel(BaseModel):
    service_arn: str = Field(alias="serviceArn")
    stat: Literal["Average", "Maximum"] = Field(alias="stat")
    period: int = Field(alias="period")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")


class GetEffectiveRecommendationPreferencesRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class GetRecommendationSummariesRequestModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RecommendationSourceModel(BaseModel):
    recommendation_source_arn: Optional[str] = Field(
        default=None, alias="recommendationSourceArn"
    )
    recommendation_source_type: Optional[
        Literal[
            "AutoScalingGroup",
            "EbsVolume",
            "Ec2Instance",
            "EcsService",
            "LambdaFunction",
        ]
    ] = Field(default=None, alias="recommendationSourceType")


class LambdaFunctionMemoryProjectedMetricModel(BaseModel):
    name: Optional[Literal["Duration"]] = Field(default=None, alias="name")
    statistic: Optional[Literal["Expected", "LowerBound", "UpperBound"]] = Field(
        default=None, alias="statistic"
    )
    value: Optional[float] = Field(default=None, alias="value")


class LambdaFunctionUtilizationMetricModel(BaseModel):
    name: Optional[Literal["Duration", "Memory"]] = Field(default=None, alias="name")
    statistic: Optional[Literal["Average", "Maximum"]] = Field(
        default=None, alias="statistic"
    )
    value: Optional[float] = Field(default=None, alias="value")


class ProjectedMetricModel(BaseModel):
    name: Optional[
        Literal[
            "Cpu",
            "DISK_READ_BYTES_PER_SECOND",
            "DISK_READ_OPS_PER_SECOND",
            "DISK_WRITE_BYTES_PER_SECOND",
            "DISK_WRITE_OPS_PER_SECOND",
            "EBS_READ_BYTES_PER_SECOND",
            "EBS_READ_OPS_PER_SECOND",
            "EBS_WRITE_BYTES_PER_SECOND",
            "EBS_WRITE_OPS_PER_SECOND",
            "Memory",
            "NETWORK_IN_BYTES_PER_SECOND",
            "NETWORK_OUT_BYTES_PER_SECOND",
            "NETWORK_PACKETS_IN_PER_SECOND",
            "NETWORK_PACKETS_OUT_PER_SECOND",
        ]
    ] = Field(default=None, alias="name")
    timestamps: Optional[List[datetime]] = Field(default=None, alias="timestamps")
    values: Optional[List[float]] = Field(default=None, alias="values")


class ReasonCodeSummaryModel(BaseModel):
    name: Optional[Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]] = Field(
        default=None, alias="name"
    )
    value: Optional[float] = Field(default=None, alias="value")


class UpdateEnrollmentStatusRequestModel(BaseModel):
    status: Literal["Active", "Failed", "Inactive", "Pending"] = Field(alias="status")
    include_member_accounts: Optional[bool] = Field(
        default=None, alias="includeMemberAccounts"
    )


class VolumeConfigurationModel(BaseModel):
    volume_type: Optional[str] = Field(default=None, alias="volumeType")
    volume_size: Optional[int] = Field(default=None, alias="volumeSize")
    volume_baseline_iop_s: Optional[int] = Field(
        default=None, alias="volumeBaselineIOPS"
    )
    volume_burst_iop_s: Optional[int] = Field(default=None, alias="volumeBurstIOPS")
    volume_baseline_throughput: Optional[int] = Field(
        default=None, alias="volumeBaselineThroughput"
    )
    volume_burst_throughput: Optional[int] = Field(
        default=None, alias="volumeBurstThroughput"
    )


class ContainerConfigurationModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="containerName")
    memory_size_configuration: Optional[MemorySizeConfigurationModel] = Field(
        default=None, alias="memorySizeConfiguration"
    )
    cpu: Optional[int] = Field(default=None, alias="cpu")


class ContainerRecommendationModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="containerName")
    memory_size_configuration: Optional[MemorySizeConfigurationModel] = Field(
        default=None, alias="memorySizeConfiguration"
    )
    cpu: Optional[int] = Field(default=None, alias="cpu")


class DeleteRecommendationPreferencesRequestModel(BaseModel):
    resource_type: Literal[
        "AutoScalingGroup",
        "EbsVolume",
        "Ec2Instance",
        "EcsService",
        "LambdaFunction",
        "NotApplicable",
    ] = Field(alias="resourceType")
    recommendation_preference_names: Sequence[
        Literal[
            "EnhancedInfrastructureMetrics",
            "ExternalMetricsPreference",
            "InferredWorkloadTypes",
        ]
    ] = Field(alias="recommendationPreferenceNames")
    scope: Optional[ScopeModel] = Field(default=None, alias="scope")


class GetRecommendationPreferencesRequestModel(BaseModel):
    resource_type: Literal[
        "AutoScalingGroup",
        "EbsVolume",
        "Ec2Instance",
        "EcsService",
        "LambdaFunction",
        "NotApplicable",
    ] = Field(alias="resourceType")
    scope: Optional[ScopeModel] = Field(default=None, alias="scope")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeRecommendationExportJobsRequestModel(BaseModel):
    job_ids: Optional[Sequence[str]] = Field(default=None, alias="jobIds")
    filters: Optional[Sequence[JobFilterModel]] = Field(default=None, alias="filters")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeRecommendationExportJobsRequestDescribeRecommendationExportJobsPaginateModel(
    BaseModel
):
    job_ids: Optional[Sequence[str]] = Field(default=None, alias="jobIds")
    filters: Optional[Sequence[JobFilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRecommendationPreferencesRequestGetRecommendationPreferencesPaginateModel(
    BaseModel
):
    resource_type: Literal[
        "AutoScalingGroup",
        "EbsVolume",
        "Ec2Instance",
        "EcsService",
        "LambdaFunction",
        "NotApplicable",
    ] = Field(alias="resourceType")
    scope: Optional[ScopeModel] = Field(default=None, alias="scope")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRecommendationSummariesRequestGetRecommendationSummariesPaginateModel(
    BaseModel
):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetEnrollmentStatusResponseModel(BaseModel):
    status: Literal["Active", "Failed", "Inactive", "Pending"] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    member_accounts_enrolled: bool = Field(alias="memberAccountsEnrolled")
    last_updated_timestamp: datetime = Field(alias="lastUpdatedTimestamp")
    number_of_member_accounts_opted_in: int = Field(
        alias="numberOfMemberAccountsOptedIn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnrollmentStatusesForOrganizationResponseModel(BaseModel):
    account_enrollment_statuses: List[AccountEnrollmentStatusModel] = Field(
        alias="accountEnrollmentStatuses"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnrollmentStatusResponseModel(BaseModel):
    status: Literal["Active", "Failed", "Inactive", "Pending"] = Field(alias="status")
    status_reason: str = Field(alias="statusReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEBSVolumeRecommendationsRequestModel(BaseModel):
    volume_arns: Optional[Sequence[str]] = Field(default=None, alias="volumeArns")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[EBSFilterModel]] = Field(default=None, alias="filters")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")


class ECSServiceRecommendedOptionProjectedMetricModel(BaseModel):
    recommended_cpu_units: Optional[int] = Field(
        default=None, alias="recommendedCpuUnits"
    )
    recommended_memory_size: Optional[int] = Field(
        default=None, alias="recommendedMemorySize"
    )
    projected_metrics: Optional[List[ECSServiceProjectedMetricModel]] = Field(
        default=None, alias="projectedMetrics"
    )


class GetECSServiceRecommendationsRequestModel(BaseModel):
    service_arns: Optional[Sequence[str]] = Field(default=None, alias="serviceArns")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[ECSServiceRecommendationFilterModel]] = Field(
        default=None, alias="filters"
    )
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")


class EffectiveRecommendationPreferencesModel(BaseModel):
    cpu_vendor_architectures: Optional[List[Literal["AWS_ARM64", "CURRENT"]]] = Field(
        default=None, alias="cpuVendorArchitectures"
    )
    enhanced_infrastructure_metrics: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="enhancedInfrastructureMetrics"
    )
    inferred_workload_types: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="inferredWorkloadTypes"
    )
    external_metrics_preference: Optional[ExternalMetricsPreferenceModel] = Field(
        default=None, alias="externalMetricsPreference"
    )


class GetEffectiveRecommendationPreferencesResponseModel(BaseModel):
    enhanced_infrastructure_metrics: Literal["Active", "Inactive"] = Field(
        alias="enhancedInfrastructureMetrics"
    )
    external_metrics_preference: ExternalMetricsPreferenceModel = Field(
        alias="externalMetricsPreference"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRecommendationPreferencesRequestModel(BaseModel):
    resource_type: Literal[
        "AutoScalingGroup",
        "EbsVolume",
        "Ec2Instance",
        "EcsService",
        "LambdaFunction",
        "NotApplicable",
    ] = Field(alias="resourceType")
    scope: Optional[ScopeModel] = Field(default=None, alias="scope")
    enhanced_infrastructure_metrics: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="enhancedInfrastructureMetrics"
    )
    inferred_workload_types: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="inferredWorkloadTypes"
    )
    external_metrics_preference: Optional[ExternalMetricsPreferenceModel] = Field(
        default=None, alias="externalMetricsPreference"
    )


class RecommendationPreferencesDetailModel(BaseModel):
    scope: Optional[ScopeModel] = Field(default=None, alias="scope")
    resource_type: Optional[
        Literal[
            "AutoScalingGroup",
            "EbsVolume",
            "Ec2Instance",
            "EcsService",
            "LambdaFunction",
            "NotApplicable",
        ]
    ] = Field(default=None, alias="resourceType")
    enhanced_infrastructure_metrics: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="enhancedInfrastructureMetrics"
    )
    inferred_workload_types: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="inferredWorkloadTypes"
    )
    external_metrics_preference: Optional[ExternalMetricsPreferenceModel] = Field(
        default=None, alias="externalMetricsPreference"
    )


class GetEnrollmentStatusesForOrganizationRequestGetEnrollmentStatusesForOrganizationPaginateModel(
    BaseModel
):
    filters: Optional[Sequence[EnrollmentFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetEnrollmentStatusesForOrganizationRequestModel(BaseModel):
    filters: Optional[Sequence[EnrollmentFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SavingsOpportunityModel(BaseModel):
    savings_opportunity_percentage: Optional[float] = Field(
        default=None, alias="savingsOpportunityPercentage"
    )
    estimated_monthly_savings: Optional[EstimatedMonthlySavingsModel] = Field(
        default=None, alias="estimatedMonthlySavings"
    )


class GetAutoScalingGroupRecommendationsRequestModel(BaseModel):
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    auto_scaling_group_arns: Optional[Sequence[str]] = Field(
        default=None, alias="autoScalingGroupArns"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    recommendation_preferences: Optional[RecommendationPreferencesModel] = Field(
        default=None, alias="recommendationPreferences"
    )


class GetEC2InstanceRecommendationsRequestModel(BaseModel):
    instance_arns: Optional[Sequence[str]] = Field(default=None, alias="instanceArns")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    recommendation_preferences: Optional[RecommendationPreferencesModel] = Field(
        default=None, alias="recommendationPreferences"
    )


class GetEC2RecommendationProjectedMetricsRequestModel(BaseModel):
    instance_arn: str = Field(alias="instanceArn")
    stat: Literal["Average", "Maximum"] = Field(alias="stat")
    period: int = Field(alias="period")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    recommendation_preferences: Optional[RecommendationPreferencesModel] = Field(
        default=None, alias="recommendationPreferences"
    )


class ExportAutoScalingGroupRecommendationsRequestModel(BaseModel):
    s3_destination_config: S3DestinationConfigModel = Field(alias="s3DestinationConfig")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    fields_to_export: Optional[
        Sequence[
            Literal[
                "AccountId",
                "AutoScalingGroupArn",
                "AutoScalingGroupName",
                "CurrentConfigurationDesiredCapacity",
                "CurrentConfigurationInstanceType",
                "CurrentConfigurationMaxSize",
                "CurrentConfigurationMinSize",
                "CurrentMemory",
                "CurrentNetwork",
                "CurrentOnDemandPrice",
                "CurrentPerformanceRisk",
                "CurrentStandardOneYearNoUpfrontReservedPrice",
                "CurrentStandardThreeYearNoUpfrontReservedPrice",
                "CurrentStorage",
                "CurrentVCpus",
                "EffectiveRecommendationPreferencesCpuVendorArchitectures",
                "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
                "EffectiveRecommendationPreferencesInferredWorkloadTypes",
                "Finding",
                "InferredWorkloadTypes",
                "LastRefreshTimestamp",
                "LookbackPeriodInDays",
                "RecommendationOptionsConfigurationDesiredCapacity",
                "RecommendationOptionsConfigurationInstanceType",
                "RecommendationOptionsConfigurationMaxSize",
                "RecommendationOptionsConfigurationMinSize",
                "RecommendationOptionsEstimatedMonthlySavingsCurrency",
                "RecommendationOptionsEstimatedMonthlySavingsValue",
                "RecommendationOptionsMemory",
                "RecommendationOptionsMigrationEffort",
                "RecommendationOptionsNetwork",
                "RecommendationOptionsOnDemandPrice",
                "RecommendationOptionsPerformanceRisk",
                "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
                "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
                "RecommendationOptionsSavingsOpportunityPercentage",
                "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
                "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
                "RecommendationOptionsStorage",
                "RecommendationOptionsVcpus",
                "UtilizationMetricsCpuMaximum",
                "UtilizationMetricsDiskReadBytesPerSecondMaximum",
                "UtilizationMetricsDiskReadOpsPerSecondMaximum",
                "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
                "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
                "UtilizationMetricsEbsReadBytesPerSecondMaximum",
                "UtilizationMetricsEbsReadOpsPerSecondMaximum",
                "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
                "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
                "UtilizationMetricsMemoryMaximum",
                "UtilizationMetricsNetworkInBytesPerSecondMaximum",
                "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
                "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
                "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
            ]
        ]
    ] = Field(default=None, alias="fieldsToExport")
    file_format: Optional[Literal["Csv"]] = Field(default=None, alias="fileFormat")
    include_member_accounts: Optional[bool] = Field(
        default=None, alias="includeMemberAccounts"
    )
    recommendation_preferences: Optional[RecommendationPreferencesModel] = Field(
        default=None, alias="recommendationPreferences"
    )


class ExportEBSVolumeRecommendationsRequestModel(BaseModel):
    s3_destination_config: S3DestinationConfigModel = Field(alias="s3DestinationConfig")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    filters: Optional[Sequence[EBSFilterModel]] = Field(default=None, alias="filters")
    fields_to_export: Optional[
        Sequence[
            Literal[
                "AccountId",
                "CurrentConfigurationVolumeBaselineIOPS",
                "CurrentConfigurationVolumeBaselineThroughput",
                "CurrentConfigurationVolumeBurstIOPS",
                "CurrentConfigurationVolumeBurstThroughput",
                "CurrentConfigurationVolumeSize",
                "CurrentConfigurationVolumeType",
                "CurrentMonthlyPrice",
                "CurrentPerformanceRisk",
                "Finding",
                "LastRefreshTimestamp",
                "LookbackPeriodInDays",
                "RecommendationOptionsConfigurationVolumeBaselineIOPS",
                "RecommendationOptionsConfigurationVolumeBaselineThroughput",
                "RecommendationOptionsConfigurationVolumeBurstIOPS",
                "RecommendationOptionsConfigurationVolumeBurstThroughput",
                "RecommendationOptionsConfigurationVolumeSize",
                "RecommendationOptionsConfigurationVolumeType",
                "RecommendationOptionsEstimatedMonthlySavingsCurrency",
                "RecommendationOptionsEstimatedMonthlySavingsValue",
                "RecommendationOptionsMonthlyPrice",
                "RecommendationOptionsPerformanceRisk",
                "RecommendationOptionsSavingsOpportunityPercentage",
                "UtilizationMetricsVolumeReadBytesPerSecondMaximum",
                "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
                "UtilizationMetricsVolumeWriteBytesPerSecondMaximum",
                "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
                "VolumeArn",
            ]
        ]
    ] = Field(default=None, alias="fieldsToExport")
    file_format: Optional[Literal["Csv"]] = Field(default=None, alias="fileFormat")
    include_member_accounts: Optional[bool] = Field(
        default=None, alias="includeMemberAccounts"
    )


class ExportEC2InstanceRecommendationsRequestModel(BaseModel):
    s3_destination_config: S3DestinationConfigModel = Field(alias="s3DestinationConfig")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    fields_to_export: Optional[
        Sequence[
            Literal[
                "AccountId",
                "CurrentInstanceType",
                "CurrentMemory",
                "CurrentNetwork",
                "CurrentOnDemandPrice",
                "CurrentPerformanceRisk",
                "CurrentStandardOneYearNoUpfrontReservedPrice",
                "CurrentStandardThreeYearNoUpfrontReservedPrice",
                "CurrentStorage",
                "CurrentVCpus",
                "EffectiveRecommendationPreferencesCpuVendorArchitectures",
                "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
                "EffectiveRecommendationPreferencesExternalMetricsSource",
                "EffectiveRecommendationPreferencesInferredWorkloadTypes",
                "Finding",
                "FindingReasonCodes",
                "InferredWorkloadTypes",
                "InstanceArn",
                "InstanceName",
                "LastRefreshTimestamp",
                "LookbackPeriodInDays",
                "RecommendationOptionsEstimatedMonthlySavingsCurrency",
                "RecommendationOptionsEstimatedMonthlySavingsValue",
                "RecommendationOptionsInstanceType",
                "RecommendationOptionsMemory",
                "RecommendationOptionsMigrationEffort",
                "RecommendationOptionsNetwork",
                "RecommendationOptionsOnDemandPrice",
                "RecommendationOptionsPerformanceRisk",
                "RecommendationOptionsPlatformDifferences",
                "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
                "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
                "RecommendationOptionsSavingsOpportunityPercentage",
                "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
                "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
                "RecommendationOptionsStorage",
                "RecommendationOptionsVcpus",
                "RecommendationsSourcesRecommendationSourceArn",
                "RecommendationsSourcesRecommendationSourceType",
                "UtilizationMetricsCpuMaximum",
                "UtilizationMetricsDiskReadBytesPerSecondMaximum",
                "UtilizationMetricsDiskReadOpsPerSecondMaximum",
                "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
                "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
                "UtilizationMetricsEbsReadBytesPerSecondMaximum",
                "UtilizationMetricsEbsReadOpsPerSecondMaximum",
                "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
                "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
                "UtilizationMetricsMemoryMaximum",
                "UtilizationMetricsNetworkInBytesPerSecondMaximum",
                "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
                "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
                "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
            ]
        ]
    ] = Field(default=None, alias="fieldsToExport")
    file_format: Optional[Literal["Csv"]] = Field(default=None, alias="fileFormat")
    include_member_accounts: Optional[bool] = Field(
        default=None, alias="includeMemberAccounts"
    )
    recommendation_preferences: Optional[RecommendationPreferencesModel] = Field(
        default=None, alias="recommendationPreferences"
    )


class ExportECSServiceRecommendationsRequestModel(BaseModel):
    s3_destination_config: S3DestinationConfigModel = Field(alias="s3DestinationConfig")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    filters: Optional[Sequence[ECSServiceRecommendationFilterModel]] = Field(
        default=None, alias="filters"
    )
    fields_to_export: Optional[
        Sequence[
            Literal[
                "AccountId",
                "CurrentPerformanceRisk",
                "CurrentServiceConfigurationAutoScalingConfiguration",
                "CurrentServiceConfigurationCpu",
                "CurrentServiceConfigurationMemory",
                "CurrentServiceConfigurationTaskDefinitionArn",
                "CurrentServiceContainerConfigurations",
                "Finding",
                "FindingReasonCodes",
                "LastRefreshTimestamp",
                "LaunchType",
                "LookbackPeriodInDays",
                "RecommendationOptionsContainerRecommendations",
                "RecommendationOptionsCpu",
                "RecommendationOptionsEstimatedMonthlySavingsCurrency",
                "RecommendationOptionsEstimatedMonthlySavingsValue",
                "RecommendationOptionsMemory",
                "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
                "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
                "RecommendationOptionsSavingsOpportunityPercentage",
                "ServiceArn",
                "UtilizationMetricsCpuMaximum",
                "UtilizationMetricsMemoryMaximum",
            ]
        ]
    ] = Field(default=None, alias="fieldsToExport")
    file_format: Optional[Literal["Csv"]] = Field(default=None, alias="fileFormat")
    include_member_accounts: Optional[bool] = Field(
        default=None, alias="includeMemberAccounts"
    )


class ExportAutoScalingGroupRecommendationsResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    s3_destination: S3DestinationModel = Field(alias="s3Destination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportDestinationModel(BaseModel):
    s3: Optional[S3DestinationModel] = Field(default=None, alias="s3")


class ExportEBSVolumeRecommendationsResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    s3_destination: S3DestinationModel = Field(alias="s3Destination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportEC2InstanceRecommendationsResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    s3_destination: S3DestinationModel = Field(alias="s3Destination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportECSServiceRecommendationsResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    s3_destination: S3DestinationModel = Field(alias="s3Destination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportLambdaFunctionRecommendationsResponseModel(BaseModel):
    job_id: str = Field(alias="jobId")
    s3_destination: S3DestinationModel = Field(alias="s3Destination")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportLambdaFunctionRecommendationsRequestModel(BaseModel):
    s3_destination_config: S3DestinationConfigModel = Field(alias="s3DestinationConfig")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterModel]] = Field(
        default=None, alias="filters"
    )
    fields_to_export: Optional[
        Sequence[
            Literal[
                "AccountId",
                "CurrentConfigurationMemorySize",
                "CurrentConfigurationTimeout",
                "CurrentCostAverage",
                "CurrentCostTotal",
                "CurrentPerformanceRisk",
                "Finding",
                "FindingReasonCodes",
                "FunctionArn",
                "FunctionVersion",
                "LastRefreshTimestamp",
                "LookbackPeriodInDays",
                "NumberOfInvocations",
                "RecommendationOptionsConfigurationMemorySize",
                "RecommendationOptionsCostHigh",
                "RecommendationOptionsCostLow",
                "RecommendationOptionsEstimatedMonthlySavingsCurrency",
                "RecommendationOptionsEstimatedMonthlySavingsValue",
                "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
                "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
                "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
                "RecommendationOptionsSavingsOpportunityPercentage",
                "UtilizationMetricsDurationAverage",
                "UtilizationMetricsDurationMaximum",
                "UtilizationMetricsMemoryAverage",
                "UtilizationMetricsMemoryMaximum",
            ]
        ]
    ] = Field(default=None, alias="fieldsToExport")
    file_format: Optional[Literal["Csv"]] = Field(default=None, alias="fileFormat")
    include_member_accounts: Optional[bool] = Field(
        default=None, alias="includeMemberAccounts"
    )


class GetLambdaFunctionRecommendationsRequestGetLambdaFunctionRecommendationsPaginateModel(
    BaseModel
):
    function_arns: Optional[Sequence[str]] = Field(default=None, alias="functionArns")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetLambdaFunctionRecommendationsRequestModel(BaseModel):
    function_arns: Optional[Sequence[str]] = Field(default=None, alias="functionArns")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="accountIds")
    filters: Optional[Sequence[LambdaFunctionRecommendationFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RecommendedOptionProjectedMetricModel(BaseModel):
    recommended_instance_type: Optional[str] = Field(
        default=None, alias="recommendedInstanceType"
    )
    rank: Optional[int] = Field(default=None, alias="rank")
    projected_metrics: Optional[List[ProjectedMetricModel]] = Field(
        default=None, alias="projectedMetrics"
    )


class SummaryModel(BaseModel):
    name: Optional[
        Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
    ] = Field(default=None, alias="name")
    value: Optional[float] = Field(default=None, alias="value")
    reason_code_summaries: Optional[List[ReasonCodeSummaryModel]] = Field(
        default=None, alias="reasonCodeSummaries"
    )


class ServiceConfigurationModel(BaseModel):
    memory: Optional[int] = Field(default=None, alias="memory")
    cpu: Optional[int] = Field(default=None, alias="cpu")
    container_configurations: Optional[List[ContainerConfigurationModel]] = Field(
        default=None, alias="containerConfigurations"
    )
    auto_scaling_configuration: Optional[
        Literal["TargetTrackingScalingCpu", "TargetTrackingScalingMemory"]
    ] = Field(default=None, alias="autoScalingConfiguration")
    task_definition_arn: Optional[str] = Field(default=None, alias="taskDefinitionArn")


class GetECSServiceRecommendationProjectedMetricsResponseModel(BaseModel):
    recommended_option_projected_metrics: List[
        ECSServiceRecommendedOptionProjectedMetricModel
    ] = Field(alias="recommendedOptionProjectedMetrics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommendationPreferencesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    recommendation_preferences_details: List[
        RecommendationPreferencesDetailModel
    ] = Field(alias="recommendationPreferencesDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoScalingGroupRecommendationOptionModel(BaseModel):
    configuration: Optional[AutoScalingGroupConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    projected_utilization_metrics: Optional[List[UtilizationMetricModel]] = Field(
        default=None, alias="projectedUtilizationMetrics"
    )
    performance_risk: Optional[float] = Field(default=None, alias="performanceRisk")
    rank: Optional[int] = Field(default=None, alias="rank")
    savings_opportunity: Optional[SavingsOpportunityModel] = Field(
        default=None, alias="savingsOpportunity"
    )
    migration_effort: Optional[Literal["High", "Low", "Medium", "VeryLow"]] = Field(
        default=None, alias="migrationEffort"
    )


class ECSServiceRecommendationOptionModel(BaseModel):
    memory: Optional[int] = Field(default=None, alias="memory")
    cpu: Optional[int] = Field(default=None, alias="cpu")
    savings_opportunity: Optional[SavingsOpportunityModel] = Field(
        default=None, alias="savingsOpportunity"
    )
    projected_utilization_metrics: Optional[
        List[ECSServiceProjectedUtilizationMetricModel]
    ] = Field(default=None, alias="projectedUtilizationMetrics")
    container_recommendations: Optional[List[ContainerRecommendationModel]] = Field(
        default=None, alias="containerRecommendations"
    )


class InstanceRecommendationOptionModel(BaseModel):
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    projected_utilization_metrics: Optional[List[UtilizationMetricModel]] = Field(
        default=None, alias="projectedUtilizationMetrics"
    )
    platform_differences: Optional[
        List[
            Literal[
                "Architecture",
                "Hypervisor",
                "InstanceStoreAvailability",
                "NetworkInterface",
                "StorageInterface",
                "VirtualizationType",
            ]
        ]
    ] = Field(default=None, alias="platformDifferences")
    performance_risk: Optional[float] = Field(default=None, alias="performanceRisk")
    rank: Optional[int] = Field(default=None, alias="rank")
    savings_opportunity: Optional[SavingsOpportunityModel] = Field(
        default=None, alias="savingsOpportunity"
    )
    migration_effort: Optional[Literal["High", "Low", "Medium", "VeryLow"]] = Field(
        default=None, alias="migrationEffort"
    )


class LambdaFunctionMemoryRecommendationOptionModel(BaseModel):
    rank: Optional[int] = Field(default=None, alias="rank")
    memory_size: Optional[int] = Field(default=None, alias="memorySize")
    projected_utilization_metrics: Optional[
        List[LambdaFunctionMemoryProjectedMetricModel]
    ] = Field(default=None, alias="projectedUtilizationMetrics")
    savings_opportunity: Optional[SavingsOpportunityModel] = Field(
        default=None, alias="savingsOpportunity"
    )


class VolumeRecommendationOptionModel(BaseModel):
    configuration: Optional[VolumeConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    performance_risk: Optional[float] = Field(default=None, alias="performanceRisk")
    rank: Optional[int] = Field(default=None, alias="rank")
    savings_opportunity: Optional[SavingsOpportunityModel] = Field(
        default=None, alias="savingsOpportunity"
    )


class RecommendationExportJobModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    destination: Optional[ExportDestinationModel] = Field(
        default=None, alias="destination"
    )
    resource_type: Optional[
        Literal[
            "AutoScalingGroup",
            "EbsVolume",
            "Ec2Instance",
            "EcsService",
            "LambdaFunction",
            "NotApplicable",
        ]
    ] = Field(default=None, alias="resourceType")
    status: Optional[Literal["Complete", "Failed", "InProgress", "Queued"]] = Field(
        default=None, alias="status"
    )
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="creationTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="lastUpdatedTimestamp"
    )
    failure_reason: Optional[str] = Field(default=None, alias="failureReason")


class GetEC2RecommendationProjectedMetricsResponseModel(BaseModel):
    recommended_option_projected_metrics: List[
        RecommendedOptionProjectedMetricModel
    ] = Field(alias="recommendedOptionProjectedMetrics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecommendationSummaryModel(BaseModel):
    summaries: Optional[List[SummaryModel]] = Field(default=None, alias="summaries")
    recommendation_resource_type: Optional[
        Literal[
            "AutoScalingGroup",
            "EbsVolume",
            "Ec2Instance",
            "EcsService",
            "LambdaFunction",
        ]
    ] = Field(default=None, alias="recommendationResourceType")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    savings_opportunity: Optional[SavingsOpportunityModel] = Field(
        default=None, alias="savingsOpportunity"
    )
    current_performance_risk_ratings: Optional[
        CurrentPerformanceRiskRatingsModel
    ] = Field(default=None, alias="currentPerformanceRiskRatings")


class AutoScalingGroupRecommendationModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="accountId")
    auto_scaling_group_arn: Optional[str] = Field(
        default=None, alias="autoScalingGroupArn"
    )
    auto_scaling_group_name: Optional[str] = Field(
        default=None, alias="autoScalingGroupName"
    )
    finding: Optional[
        Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
    ] = Field(default=None, alias="finding")
    utilization_metrics: Optional[List[UtilizationMetricModel]] = Field(
        default=None, alias="utilizationMetrics"
    )
    look_back_period_in_days: Optional[float] = Field(
        default=None, alias="lookBackPeriodInDays"
    )
    current_configuration: Optional[AutoScalingGroupConfigurationModel] = Field(
        default=None, alias="currentConfiguration"
    )
    recommendation_options: Optional[
        List[AutoScalingGroupRecommendationOptionModel]
    ] = Field(default=None, alias="recommendationOptions")
    last_refresh_timestamp: Optional[datetime] = Field(
        default=None, alias="lastRefreshTimestamp"
    )
    current_performance_risk: Optional[
        Literal["High", "Low", "Medium", "VeryLow"]
    ] = Field(default=None, alias="currentPerformanceRisk")
    effective_recommendation_preferences: Optional[
        EffectiveRecommendationPreferencesModel
    ] = Field(default=None, alias="effectiveRecommendationPreferences")
    inferred_workload_types: Optional[
        List[
            Literal[
                "AmazonEmr",
                "ApacheCassandra",
                "ApacheHadoop",
                "Kafka",
                "Memcached",
                "Nginx",
                "PostgreSql",
                "Redis",
            ]
        ]
    ] = Field(default=None, alias="inferredWorkloadTypes")


class ECSServiceRecommendationModel(BaseModel):
    service_arn: Optional[str] = Field(default=None, alias="serviceArn")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    current_service_configuration: Optional[ServiceConfigurationModel] = Field(
        default=None, alias="currentServiceConfiguration"
    )
    utilization_metrics: Optional[List[ECSServiceUtilizationMetricModel]] = Field(
        default=None, alias="utilizationMetrics"
    )
    lookback_period_in_days: Optional[float] = Field(
        default=None, alias="lookbackPeriodInDays"
    )
    launch_type: Optional[Literal["EC2", "Fargate"]] = Field(
        default=None, alias="launchType"
    )
    last_refresh_timestamp: Optional[datetime] = Field(
        default=None, alias="lastRefreshTimestamp"
    )
    finding: Optional[
        Literal["Optimized", "Overprovisioned", "Underprovisioned"]
    ] = Field(default=None, alias="finding")
    finding_reason_codes: Optional[
        List[
            Literal[
                "CPUOverprovisioned",
                "CPUUnderprovisioned",
                "MemoryOverprovisioned",
                "MemoryUnderprovisioned",
            ]
        ]
    ] = Field(default=None, alias="findingReasonCodes")
    service_recommendation_options: Optional[
        List[ECSServiceRecommendationOptionModel]
    ] = Field(default=None, alias="serviceRecommendationOptions")
    current_performance_risk: Optional[
        Literal["High", "Low", "Medium", "VeryLow"]
    ] = Field(default=None, alias="currentPerformanceRisk")


class InstanceRecommendationModel(BaseModel):
    instance_arn: Optional[str] = Field(default=None, alias="instanceArn")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    instance_name: Optional[str] = Field(default=None, alias="instanceName")
    current_instance_type: Optional[str] = Field(
        default=None, alias="currentInstanceType"
    )
    finding: Optional[
        Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
    ] = Field(default=None, alias="finding")
    finding_reason_codes: Optional[
        List[
            Literal[
                "CPUOverprovisioned",
                "CPUUnderprovisioned",
                "DiskIOPSOverprovisioned",
                "DiskIOPSUnderprovisioned",
                "DiskThroughputOverprovisioned",
                "DiskThroughputUnderprovisioned",
                "EBSIOPSOverprovisioned",
                "EBSIOPSUnderprovisioned",
                "EBSThroughputOverprovisioned",
                "EBSThroughputUnderprovisioned",
                "MemoryOverprovisioned",
                "MemoryUnderprovisioned",
                "NetworkBandwidthOverprovisioned",
                "NetworkBandwidthUnderprovisioned",
                "NetworkPPSOverprovisioned",
                "NetworkPPSUnderprovisioned",
            ]
        ]
    ] = Field(default=None, alias="findingReasonCodes")
    utilization_metrics: Optional[List[UtilizationMetricModel]] = Field(
        default=None, alias="utilizationMetrics"
    )
    look_back_period_in_days: Optional[float] = Field(
        default=None, alias="lookBackPeriodInDays"
    )
    recommendation_options: Optional[List[InstanceRecommendationOptionModel]] = Field(
        default=None, alias="recommendationOptions"
    )
    recommendation_sources: Optional[List[RecommendationSourceModel]] = Field(
        default=None, alias="recommendationSources"
    )
    last_refresh_timestamp: Optional[datetime] = Field(
        default=None, alias="lastRefreshTimestamp"
    )
    current_performance_risk: Optional[
        Literal["High", "Low", "Medium", "VeryLow"]
    ] = Field(default=None, alias="currentPerformanceRisk")
    effective_recommendation_preferences: Optional[
        EffectiveRecommendationPreferencesModel
    ] = Field(default=None, alias="effectiveRecommendationPreferences")
    inferred_workload_types: Optional[
        List[
            Literal[
                "AmazonEmr",
                "ApacheCassandra",
                "ApacheHadoop",
                "Kafka",
                "Memcached",
                "Nginx",
                "PostgreSql",
                "Redis",
            ]
        ]
    ] = Field(default=None, alias="inferredWorkloadTypes")


class LambdaFunctionRecommendationModel(BaseModel):
    function_arn: Optional[str] = Field(default=None, alias="functionArn")
    function_version: Optional[str] = Field(default=None, alias="functionVersion")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    current_memory_size: Optional[int] = Field(default=None, alias="currentMemorySize")
    number_of_invocations: Optional[int] = Field(
        default=None, alias="numberOfInvocations"
    )
    utilization_metrics: Optional[List[LambdaFunctionUtilizationMetricModel]] = Field(
        default=None, alias="utilizationMetrics"
    )
    lookback_period_in_days: Optional[float] = Field(
        default=None, alias="lookbackPeriodInDays"
    )
    last_refresh_timestamp: Optional[datetime] = Field(
        default=None, alias="lastRefreshTimestamp"
    )
    finding: Optional[Literal["NotOptimized", "Optimized", "Unavailable"]] = Field(
        default=None, alias="finding"
    )
    finding_reason_codes: Optional[
        List[
            Literal[
                "Inconclusive",
                "InsufficientData",
                "MemoryOverprovisioned",
                "MemoryUnderprovisioned",
            ]
        ]
    ] = Field(default=None, alias="findingReasonCodes")
    memory_size_recommendation_options: Optional[
        List[LambdaFunctionMemoryRecommendationOptionModel]
    ] = Field(default=None, alias="memorySizeRecommendationOptions")
    current_performance_risk: Optional[
        Literal["High", "Low", "Medium", "VeryLow"]
    ] = Field(default=None, alias="currentPerformanceRisk")


class VolumeRecommendationModel(BaseModel):
    volume_arn: Optional[str] = Field(default=None, alias="volumeArn")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    current_configuration: Optional[VolumeConfigurationModel] = Field(
        default=None, alias="currentConfiguration"
    )
    finding: Optional[Literal["NotOptimized", "Optimized"]] = Field(
        default=None, alias="finding"
    )
    utilization_metrics: Optional[List[EBSUtilizationMetricModel]] = Field(
        default=None, alias="utilizationMetrics"
    )
    look_back_period_in_days: Optional[float] = Field(
        default=None, alias="lookBackPeriodInDays"
    )
    volume_recommendation_options: Optional[
        List[VolumeRecommendationOptionModel]
    ] = Field(default=None, alias="volumeRecommendationOptions")
    last_refresh_timestamp: Optional[datetime] = Field(
        default=None, alias="lastRefreshTimestamp"
    )
    current_performance_risk: Optional[
        Literal["High", "Low", "Medium", "VeryLow"]
    ] = Field(default=None, alias="currentPerformanceRisk")


class DescribeRecommendationExportJobsResponseModel(BaseModel):
    recommendation_export_jobs: List[RecommendationExportJobModel] = Field(
        alias="recommendationExportJobs"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommendationSummariesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    recommendation_summaries: List[RecommendationSummaryModel] = Field(
        alias="recommendationSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAutoScalingGroupRecommendationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    auto_scaling_group_recommendations: List[
        AutoScalingGroupRecommendationModel
    ] = Field(alias="autoScalingGroupRecommendations")
    errors: List[GetRecommendationErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetECSServiceRecommendationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    ecs_service_recommendations: List[ECSServiceRecommendationModel] = Field(
        alias="ecsServiceRecommendations"
    )
    errors: List[GetRecommendationErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEC2InstanceRecommendationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    instance_recommendations: List[InstanceRecommendationModel] = Field(
        alias="instanceRecommendations"
    )
    errors: List[GetRecommendationErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLambdaFunctionRecommendationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    lambda_function_recommendations: List[LambdaFunctionRecommendationModel] = Field(
        alias="lambdaFunctionRecommendations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEBSVolumeRecommendationsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    volume_recommendations: List[VolumeRecommendationModel] = Field(
        alias="volumeRecommendations"
    )
    errors: List[GetRecommendationErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
