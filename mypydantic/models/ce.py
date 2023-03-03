# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AnomalyDateIntervalModel(BaseModel):
    start_date: str = Field(alias="StartDate")
    end_date: Optional[str] = Field(default=None, alias="EndDate")


class AnomalyMonitorModel(BaseModel):
    monitor_name: str = Field(alias="MonitorName")
    monitor_type: Literal["CUSTOM", "DIMENSIONAL"] = Field(alias="MonitorType")
    monitor_arn: Optional[str] = Field(default=None, alias="MonitorArn")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    last_updated_date: Optional[str] = Field(default=None, alias="LastUpdatedDate")
    last_evaluated_date: Optional[str] = Field(default=None, alias="LastEvaluatedDate")
    monitor_dimension: Optional[Literal["SERVICE"]] = Field(
        default=None, alias="MonitorDimension"
    )
    monitor_specification: Optional[ExpressionModel] = Field(
        default=None, alias="MonitorSpecification"
    )
    dimensional_value_count: Optional[int] = Field(
        default=None, alias="DimensionalValueCount"
    )


class AnomalyScoreModel(BaseModel):
    max_score: float = Field(alias="MaxScore")
    current_score: float = Field(alias="CurrentScore")


class SubscriberModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    type: Optional[Literal["EMAIL", "SNS"]] = Field(default=None, alias="Type")
    status: Optional[Literal["CONFIRMED", "DECLINED"]] = Field(
        default=None, alias="Status"
    )


class ImpactModel(BaseModel):
    max_impact: float = Field(alias="MaxImpact")
    total_impact: Optional[float] = Field(default=None, alias="TotalImpact")
    total_actual_spend: Optional[float] = Field(default=None, alias="TotalActualSpend")
    total_expected_spend: Optional[float] = Field(
        default=None, alias="TotalExpectedSpend"
    )
    total_impact_percentage: Optional[float] = Field(
        default=None, alias="TotalImpactPercentage"
    )


class RootCauseModel(BaseModel):
    service: Optional[str] = Field(default=None, alias="Service")
    region: Optional[str] = Field(default=None, alias="Region")
    linked_account: Optional[str] = Field(default=None, alias="LinkedAccount")
    usage_type: Optional[str] = Field(default=None, alias="UsageType")
    linked_account_name: Optional[str] = Field(default=None, alias="LinkedAccountName")


class CostAllocationTagStatusEntryModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    status: Literal["Active", "Inactive"] = Field(alias="Status")


class CostAllocationTagModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    type: Literal["AWSGenerated", "UserDefined"] = Field(alias="Type")
    status: Literal["Active", "Inactive"] = Field(alias="Status")


class CostCategoryInheritedValueDimensionModel(BaseModel):
    dimension_name: Optional[Literal["LINKED_ACCOUNT_NAME", "TAG"]] = Field(
        default=None, alias="DimensionName"
    )
    dimension_key: Optional[str] = Field(default=None, alias="DimensionKey")


class CostCategoryProcessingStatusModel(BaseModel):
    component: Optional[Literal["COST_EXPLORER"]] = Field(
        default=None, alias="Component"
    )
    status: Optional[Literal["APPLIED", "PROCESSING"]] = Field(
        default=None, alias="Status"
    )


class CostCategorySplitChargeRuleParameterModel(BaseModel):
    type: Literal["ALLOCATION_PERCENTAGES"] = Field(alias="Type")
    values: Sequence[str] = Field(alias="Values")


class CostCategoryValuesModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    match_options: Optional[
        Sequence[
            Literal[
                "ABSENT",
                "CASE_INSENSITIVE",
                "CASE_SENSITIVE",
                "CONTAINS",
                "ENDS_WITH",
                "EQUALS",
                "GREATER_THAN_OR_EQUAL",
                "STARTS_WITH",
            ]
        ]
    ] = Field(default=None, alias="MatchOptions")


class DateIntervalModel(BaseModel):
    start: str = Field(alias="Start")
    end: str = Field(alias="End")


class CoverageCostModel(BaseModel):
    on_demand_cost: Optional[str] = Field(default=None, alias="OnDemandCost")


class CoverageHoursModel(BaseModel):
    on_demand_hours: Optional[str] = Field(default=None, alias="OnDemandHours")
    reserved_hours: Optional[str] = Field(default=None, alias="ReservedHours")
    total_running_hours: Optional[str] = Field(default=None, alias="TotalRunningHours")
    coverage_hours_percentage: Optional[str] = Field(
        default=None, alias="CoverageHoursPercentage"
    )


class CoverageNormalizedUnitsModel(BaseModel):
    on_demand_normalized_units: Optional[str] = Field(
        default=None, alias="OnDemandNormalizedUnits"
    )
    reserved_normalized_units: Optional[str] = Field(
        default=None, alias="ReservedNormalizedUnits"
    )
    total_running_normalized_units: Optional[str] = Field(
        default=None, alias="TotalRunningNormalizedUnits"
    )
    coverage_normalized_units_percentage: Optional[str] = Field(
        default=None, alias="CoverageNormalizedUnitsPercentage"
    )


class ResourceTagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagValuesModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    match_options: Optional[
        Sequence[
            Literal[
                "ABSENT",
                "CASE_INSENSITIVE",
                "CASE_SENSITIVE",
                "CONTAINS",
                "ENDS_WITH",
                "EQUALS",
                "GREATER_THAN_OR_EQUAL",
                "STARTS_WITH",
            ]
        ]
    ] = Field(default=None, alias="MatchOptions")


class DeleteAnomalyMonitorRequestModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")


class DeleteAnomalySubscriptionRequestModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")


class DeleteCostCategoryDefinitionRequestModel(BaseModel):
    cost_category_arn: str = Field(alias="CostCategoryArn")


class DescribeCostCategoryDefinitionRequestModel(BaseModel):
    cost_category_arn: str = Field(alias="CostCategoryArn")
    effective_on: Optional[str] = Field(default=None, alias="EffectiveOn")


class DimensionValuesModel(BaseModel):
    key: Optional[
        Literal[
            "AGREEMENT_END_DATE_TIME_AFTER",
            "AGREEMENT_END_DATE_TIME_BEFORE",
            "ANOMALY_TOTAL_IMPACT_ABSOLUTE",
            "ANOMALY_TOTAL_IMPACT_PERCENTAGE",
            "AZ",
            "BILLING_ENTITY",
            "CACHE_ENGINE",
            "DATABASE_ENGINE",
            "DEPLOYMENT_OPTION",
            "INSTANCE_TYPE",
            "INSTANCE_TYPE_FAMILY",
            "INVOICING_ENTITY",
            "LEGAL_ENTITY_NAME",
            "LINKED_ACCOUNT",
            "LINKED_ACCOUNT_NAME",
            "OPERATING_SYSTEM",
            "OPERATION",
            "PAYMENT_OPTION",
            "PLATFORM",
            "PURCHASE_TYPE",
            "RECORD_TYPE",
            "REGION",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "SCOPE",
            "SERVICE",
            "SERVICE_CODE",
            "SUBSCRIPTION_ID",
            "TENANCY",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
        ]
    ] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    match_options: Optional[
        Sequence[
            Literal[
                "ABSENT",
                "CASE_INSENSITIVE",
                "CASE_SENSITIVE",
                "CONTAINS",
                "ENDS_WITH",
                "EQUALS",
                "GREATER_THAN_OR_EQUAL",
                "STARTS_WITH",
            ]
        ]
    ] = Field(default=None, alias="MatchOptions")


class DimensionValuesWithAttributesModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")


class DiskResourceUtilizationModel(BaseModel):
    disk_read_ops_per_second: Optional[str] = Field(
        default=None, alias="DiskReadOpsPerSecond"
    )
    disk_write_ops_per_second: Optional[str] = Field(
        default=None, alias="DiskWriteOpsPerSecond"
    )
    disk_read_bytes_per_second: Optional[str] = Field(
        default=None, alias="DiskReadBytesPerSecond"
    )
    disk_write_bytes_per_second: Optional[str] = Field(
        default=None, alias="DiskWriteBytesPerSecond"
    )


class EBSResourceUtilizationModel(BaseModel):
    ebs_read_ops_per_second: Optional[str] = Field(
        default=None, alias="EbsReadOpsPerSecond"
    )
    ebs_write_ops_per_second: Optional[str] = Field(
        default=None, alias="EbsWriteOpsPerSecond"
    )
    ebs_read_bytes_per_second: Optional[str] = Field(
        default=None, alias="EbsReadBytesPerSecond"
    )
    ebs_write_bytes_per_second: Optional[str] = Field(
        default=None, alias="EbsWriteBytesPerSecond"
    )


class EC2InstanceDetailsModel(BaseModel):
    family: Optional[str] = Field(default=None, alias="Family")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    region: Optional[str] = Field(default=None, alias="Region")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    platform: Optional[str] = Field(default=None, alias="Platform")
    tenancy: Optional[str] = Field(default=None, alias="Tenancy")
    current_generation: Optional[bool] = Field(default=None, alias="CurrentGeneration")
    size_flex_eligible: Optional[bool] = Field(default=None, alias="SizeFlexEligible")


class EC2ResourceDetailsModel(BaseModel):
    hourly_on_demand_rate: Optional[str] = Field(
        default=None, alias="HourlyOnDemandRate"
    )
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    platform: Optional[str] = Field(default=None, alias="Platform")
    region: Optional[str] = Field(default=None, alias="Region")
    sku: Optional[str] = Field(default=None, alias="Sku")
    memory: Optional[str] = Field(default=None, alias="Memory")
    network_performance: Optional[str] = Field(default=None, alias="NetworkPerformance")
    storage: Optional[str] = Field(default=None, alias="Storage")
    vcpu: Optional[str] = Field(default=None, alias="Vcpu")


class NetworkResourceUtilizationModel(BaseModel):
    network_in_bytes_per_second: Optional[str] = Field(
        default=None, alias="NetworkInBytesPerSecond"
    )
    network_out_bytes_per_second: Optional[str] = Field(
        default=None, alias="NetworkOutBytesPerSecond"
    )
    network_packets_in_per_second: Optional[str] = Field(
        default=None, alias="NetworkPacketsInPerSecond"
    )
    network_packets_out_per_second: Optional[str] = Field(
        default=None, alias="NetworkPacketsOutPerSecond"
    )


class EC2SpecificationModel(BaseModel):
    offering_class: Optional[Literal["CONVERTIBLE", "STANDARD"]] = Field(
        default=None, alias="OfferingClass"
    )


class ESInstanceDetailsModel(BaseModel):
    instance_class: Optional[str] = Field(default=None, alias="InstanceClass")
    instance_size: Optional[str] = Field(default=None, alias="InstanceSize")
    region: Optional[str] = Field(default=None, alias="Region")
    current_generation: Optional[bool] = Field(default=None, alias="CurrentGeneration")
    size_flex_eligible: Optional[bool] = Field(default=None, alias="SizeFlexEligible")


class ElastiCacheInstanceDetailsModel(BaseModel):
    family: Optional[str] = Field(default=None, alias="Family")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    region: Optional[str] = Field(default=None, alias="Region")
    product_description: Optional[str] = Field(default=None, alias="ProductDescription")
    current_generation: Optional[bool] = Field(default=None, alias="CurrentGeneration")
    size_flex_eligible: Optional[bool] = Field(default=None, alias="SizeFlexEligible")


class GenerationSummaryModel(BaseModel):
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")
    generation_status: Optional[Literal["FAILED", "PROCESSING", "SUCCEEDED"]] = Field(
        default=None, alias="GenerationStatus"
    )
    generation_started_time: Optional[str] = Field(
        default=None, alias="GenerationStartedTime"
    )
    generation_completion_time: Optional[str] = Field(
        default=None, alias="GenerationCompletionTime"
    )
    estimated_completion_time: Optional[str] = Field(
        default=None, alias="EstimatedCompletionTime"
    )


class TotalImpactFilterModel(BaseModel):
    numeric_operator: Literal[
        "BETWEEN",
        "EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
    ] = Field(alias="NumericOperator")
    start_value: float = Field(alias="StartValue")
    end_value: Optional[float] = Field(default=None, alias="EndValue")


class GetAnomalyMonitorsRequestModel(BaseModel):
    monitor_arn_list: Optional[Sequence[str]] = Field(
        default=None, alias="MonitorArnList"
    )
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetAnomalySubscriptionsRequestModel(BaseModel):
    subscription_arn_list: Optional[Sequence[str]] = Field(
        default=None, alias="SubscriptionArnList"
    )
    monitor_arn: Optional[str] = Field(default=None, alias="MonitorArn")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GroupDefinitionModel(BaseModel):
    type: Optional[Literal["COST_CATEGORY", "DIMENSION", "TAG"]] = Field(
        default=None, alias="Type"
    )
    key: Optional[str] = Field(default=None, alias="Key")


class SortDefinitionModel(BaseModel):
    key: str = Field(alias="Key")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )


class MetricValueModel(BaseModel):
    amount: Optional[str] = Field(default=None, alias="Amount")
    unit: Optional[str] = Field(default=None, alias="Unit")


class ReservationPurchaseRecommendationMetadataModel(BaseModel):
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")
    generation_timestamp: Optional[str] = Field(
        default=None, alias="GenerationTimestamp"
    )


class ReservationAggregatesModel(BaseModel):
    utilization_percentage: Optional[str] = Field(
        default=None, alias="UtilizationPercentage"
    )
    utilization_percentage_in_units: Optional[str] = Field(
        default=None, alias="UtilizationPercentageInUnits"
    )
    purchased_hours: Optional[str] = Field(default=None, alias="PurchasedHours")
    purchased_units: Optional[str] = Field(default=None, alias="PurchasedUnits")
    total_actual_hours: Optional[str] = Field(default=None, alias="TotalActualHours")
    total_actual_units: Optional[str] = Field(default=None, alias="TotalActualUnits")
    unused_hours: Optional[str] = Field(default=None, alias="UnusedHours")
    unused_units: Optional[str] = Field(default=None, alias="UnusedUnits")
    on_demand_cost_of_rihours_used: Optional[str] = Field(
        default=None, alias="OnDemandCostOfRIHoursUsed"
    )
    net_risavings: Optional[str] = Field(default=None, alias="NetRISavings")
    total_potential_risavings: Optional[str] = Field(
        default=None, alias="TotalPotentialRISavings"
    )
    amortized_upfront_fee: Optional[str] = Field(
        default=None, alias="AmortizedUpfrontFee"
    )
    amortized_recurring_fee: Optional[str] = Field(
        default=None, alias="AmortizedRecurringFee"
    )
    total_amortized_fee: Optional[str] = Field(default=None, alias="TotalAmortizedFee")
    ricost_for_unused_hours: Optional[str] = Field(
        default=None, alias="RICostForUnusedHours"
    )
    realized_savings: Optional[str] = Field(default=None, alias="RealizedSavings")
    unrealized_savings: Optional[str] = Field(default=None, alias="UnrealizedSavings")


class RightsizingRecommendationConfigurationModel(BaseModel):
    recommendation_target: Literal[
        "CROSS_INSTANCE_FAMILY", "SAME_INSTANCE_FAMILY"
    ] = Field(alias="RecommendationTarget")
    benefits_considered: bool = Field(alias="BenefitsConsidered")


class RightsizingRecommendationMetadataModel(BaseModel):
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")
    generation_timestamp: Optional[str] = Field(
        default=None, alias="GenerationTimestamp"
    )
    lookback_period_in_days: Optional[
        Literal["SEVEN_DAYS", "SIXTY_DAYS", "THIRTY_DAYS"]
    ] = Field(default=None, alias="LookbackPeriodInDays")
    additional_metadata: Optional[str] = Field(default=None, alias="AdditionalMetadata")


class RightsizingRecommendationSummaryModel(BaseModel):
    total_recommendation_count: Optional[str] = Field(
        default=None, alias="TotalRecommendationCount"
    )
    estimated_total_monthly_savings_amount: Optional[str] = Field(
        default=None, alias="EstimatedTotalMonthlySavingsAmount"
    )
    savings_currency_code: Optional[str] = Field(
        default=None, alias="SavingsCurrencyCode"
    )
    savings_percentage: Optional[str] = Field(default=None, alias="SavingsPercentage")


class GetSavingsPlansPurchaseRecommendationRequestModel(BaseModel):
    savings_plans_type: Literal[
        "COMPUTE_SP", "EC2_INSTANCE_SP", "SAGEMAKER_SP"
    ] = Field(alias="SavingsPlansType")
    term_in_years: Literal["ONE_YEAR", "THREE_YEARS"] = Field(alias="TermInYears")
    payment_option: Literal[
        "ALL_UPFRONT",
        "HEAVY_UTILIZATION",
        "LIGHT_UTILIZATION",
        "MEDIUM_UTILIZATION",
        "NO_UPFRONT",
        "PARTIAL_UPFRONT",
    ] = Field(alias="PaymentOption")
    lookback_period_in_days: Literal["SEVEN_DAYS", "SIXTY_DAYS", "THIRTY_DAYS"] = Field(
        alias="LookbackPeriodInDays"
    )
    account_scope: Optional[Literal["LINKED", "PAYER"]] = Field(
        default=None, alias="AccountScope"
    )
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")


class SavingsPlansPurchaseRecommendationMetadataModel(BaseModel):
    recommendation_id: Optional[str] = Field(default=None, alias="RecommendationId")
    generation_timestamp: Optional[str] = Field(
        default=None, alias="GenerationTimestamp"
    )
    additional_metadata: Optional[str] = Field(default=None, alias="AdditionalMetadata")


class RDSInstanceDetailsModel(BaseModel):
    family: Optional[str] = Field(default=None, alias="Family")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    region: Optional[str] = Field(default=None, alias="Region")
    database_engine: Optional[str] = Field(default=None, alias="DatabaseEngine")
    database_edition: Optional[str] = Field(default=None, alias="DatabaseEdition")
    deployment_option: Optional[str] = Field(default=None, alias="DeploymentOption")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    current_generation: Optional[bool] = Field(default=None, alias="CurrentGeneration")
    size_flex_eligible: Optional[bool] = Field(default=None, alias="SizeFlexEligible")


class RedshiftInstanceDetailsModel(BaseModel):
    family: Optional[str] = Field(default=None, alias="Family")
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    region: Optional[str] = Field(default=None, alias="Region")
    current_generation: Optional[bool] = Field(default=None, alias="CurrentGeneration")
    size_flex_eligible: Optional[bool] = Field(default=None, alias="SizeFlexEligible")


class ListCostAllocationTagsRequestModel(BaseModel):
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")
    type: Optional[Literal["AWSGenerated", "UserDefined"]] = Field(
        default=None, alias="Type"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListCostCategoryDefinitionsRequestModel(BaseModel):
    effective_on: Optional[str] = Field(default=None, alias="EffectiveOn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSavingsPlansPurchaseRecommendationGenerationRequestModel(BaseModel):
    generation_status: Optional[Literal["FAILED", "PROCESSING", "SUCCEEDED"]] = Field(
        default=None, alias="GenerationStatus"
    )
    recommendation_ids: Optional[Sequence[str]] = Field(
        default=None, alias="RecommendationIds"
    )
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ProvideAnomalyFeedbackRequestModel(BaseModel):
    anomaly_id: str = Field(alias="AnomalyId")
    feedback: Literal["NO", "PLANNED_ACTIVITY", "YES"] = Field(alias="Feedback")


class ReservationPurchaseRecommendationSummaryModel(BaseModel):
    total_estimated_monthly_savings_amount: Optional[str] = Field(
        default=None, alias="TotalEstimatedMonthlySavingsAmount"
    )
    total_estimated_monthly_savings_percentage: Optional[str] = Field(
        default=None, alias="TotalEstimatedMonthlySavingsPercentage"
    )
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")


class TerminateRecommendationDetailModel(BaseModel):
    estimated_monthly_savings: Optional[str] = Field(
        default=None, alias="EstimatedMonthlySavings"
    )
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")


class SavingsPlansAmortizedCommitmentModel(BaseModel):
    amortized_recurring_commitment: Optional[str] = Field(
        default=None, alias="AmortizedRecurringCommitment"
    )
    amortized_upfront_commitment: Optional[str] = Field(
        default=None, alias="AmortizedUpfrontCommitment"
    )
    total_amortized_commitment: Optional[str] = Field(
        default=None, alias="TotalAmortizedCommitment"
    )


class SavingsPlansCoverageDataModel(BaseModel):
    spend_covered_by_savings_plans: Optional[str] = Field(
        default=None, alias="SpendCoveredBySavingsPlans"
    )
    on_demand_cost: Optional[str] = Field(default=None, alias="OnDemandCost")
    total_cost: Optional[str] = Field(default=None, alias="TotalCost")
    coverage_percentage: Optional[str] = Field(default=None, alias="CoveragePercentage")


class SavingsPlansDetailsModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="Region")
    instance_family: Optional[str] = Field(default=None, alias="InstanceFamily")
    offering_id: Optional[str] = Field(default=None, alias="OfferingId")


class SavingsPlansPurchaseRecommendationSummaryModel(BaseModel):
    estimated_roi: Optional[str] = Field(default=None, alias="EstimatedROI")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    estimated_total_cost: Optional[str] = Field(
        default=None, alias="EstimatedTotalCost"
    )
    current_on_demand_spend: Optional[str] = Field(
        default=None, alias="CurrentOnDemandSpend"
    )
    estimated_savings_amount: Optional[str] = Field(
        default=None, alias="EstimatedSavingsAmount"
    )
    total_recommendation_count: Optional[str] = Field(
        default=None, alias="TotalRecommendationCount"
    )
    daily_commitment_to_purchase: Optional[str] = Field(
        default=None, alias="DailyCommitmentToPurchase"
    )
    hourly_commitment_to_purchase: Optional[str] = Field(
        default=None, alias="HourlyCommitmentToPurchase"
    )
    estimated_savings_percentage: Optional[str] = Field(
        default=None, alias="EstimatedSavingsPercentage"
    )
    estimated_monthly_savings_amount: Optional[str] = Field(
        default=None, alias="EstimatedMonthlySavingsAmount"
    )
    estimated_on_demand_cost_with_current_commitment: Optional[str] = Field(
        default=None, alias="EstimatedOnDemandCostWithCurrentCommitment"
    )


class SavingsPlansSavingsModel(BaseModel):
    net_savings: Optional[str] = Field(default=None, alias="NetSavings")
    on_demand_cost_equivalent: Optional[str] = Field(
        default=None, alias="OnDemandCostEquivalent"
    )


class SavingsPlansUtilizationModel(BaseModel):
    total_commitment: Optional[str] = Field(default=None, alias="TotalCommitment")
    used_commitment: Optional[str] = Field(default=None, alias="UsedCommitment")
    unused_commitment: Optional[str] = Field(default=None, alias="UnusedCommitment")
    utilization_percentage: Optional[str] = Field(
        default=None, alias="UtilizationPercentage"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_tag_keys: Sequence[str] = Field(alias="ResourceTagKeys")


class UpdateAnomalyMonitorRequestModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")
    monitor_name: Optional[str] = Field(default=None, alias="MonitorName")


class UpdateCostAllocationTagsStatusErrorModel(BaseModel):
    tag_key: Optional[str] = Field(default=None, alias="TagKey")
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class AnomalySubscriptionModel(BaseModel):
    monitor_arn_list: Sequence[str] = Field(alias="MonitorArnList")
    subscribers: Sequence[SubscriberModel] = Field(alias="Subscribers")
    frequency: Literal["DAILY", "IMMEDIATE", "WEEKLY"] = Field(alias="Frequency")
    subscription_name: str = Field(alias="SubscriptionName")
    subscription_arn: Optional[str] = Field(default=None, alias="SubscriptionArn")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    threshold_expression: Optional[ExpressionModel] = Field(
        default=None, alias="ThresholdExpression"
    )


class UpdateAnomalySubscriptionRequestModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    frequency: Optional[Literal["DAILY", "IMMEDIATE", "WEEKLY"]] = Field(
        default=None, alias="Frequency"
    )
    monitor_arn_list: Optional[Sequence[str]] = Field(
        default=None, alias="MonitorArnList"
    )
    subscribers: Optional[Sequence[SubscriberModel]] = Field(
        default=None, alias="Subscribers"
    )
    subscription_name: Optional[str] = Field(default=None, alias="SubscriptionName")
    threshold_expression: Optional[ExpressionModel] = Field(
        default=None, alias="ThresholdExpression"
    )


class AnomalyModel(BaseModel):
    anomaly_id: str = Field(alias="AnomalyId")
    anomaly_score: AnomalyScoreModel = Field(alias="AnomalyScore")
    impact: ImpactModel = Field(alias="Impact")
    monitor_arn: str = Field(alias="MonitorArn")
    anomaly_start_date: Optional[str] = Field(default=None, alias="AnomalyStartDate")
    anomaly_end_date: Optional[str] = Field(default=None, alias="AnomalyEndDate")
    dimension_value: Optional[str] = Field(default=None, alias="DimensionValue")
    root_causes: Optional[List[RootCauseModel]] = Field(
        default=None, alias="RootCauses"
    )
    feedback: Optional[Literal["NO", "PLANNED_ACTIVITY", "YES"]] = Field(
        default=None, alias="Feedback"
    )


class UpdateCostAllocationTagsStatusRequestModel(BaseModel):
    cost_allocation_tags_status: Sequence[CostAllocationTagStatusEntryModel] = Field(
        alias="CostAllocationTagsStatus"
    )


class CostCategoryRuleModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    rule: Optional[ExpressionModel] = Field(default=None, alias="Rule")
    inherited_value: Optional[CostCategoryInheritedValueDimensionModel] = Field(
        default=None, alias="InheritedValue"
    )
    type: Optional[Literal["INHERITED_VALUE", "REGULAR"]] = Field(
        default=None, alias="Type"
    )


class CostCategoryReferenceModel(BaseModel):
    cost_category_arn: Optional[str] = Field(default=None, alias="CostCategoryArn")
    name: Optional[str] = Field(default=None, alias="Name")
    effective_start: Optional[str] = Field(default=None, alias="EffectiveStart")
    effective_end: Optional[str] = Field(default=None, alias="EffectiveEnd")
    number_of_rules: Optional[int] = Field(default=None, alias="NumberOfRules")
    processing_status: Optional[List[CostCategoryProcessingStatusModel]] = Field(
        default=None, alias="ProcessingStatus"
    )
    values: Optional[List[str]] = Field(default=None, alias="Values")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")


class CostCategorySplitChargeRuleModel(BaseModel):
    source: str = Field(alias="Source")
    targets: Sequence[str] = Field(alias="Targets")
    method: Literal["EVEN", "FIXED", "PROPORTIONAL"] = Field(alias="Method")
    parameters: Optional[Sequence[CostCategorySplitChargeRuleParameterModel]] = Field(
        default=None, alias="Parameters"
    )


class ForecastResultModel(BaseModel):
    time_period: Optional[DateIntervalModel] = Field(default=None, alias="TimePeriod")
    mean_value: Optional[str] = Field(default=None, alias="MeanValue")
    prediction_interval_lower_bound: Optional[str] = Field(
        default=None, alias="PredictionIntervalLowerBound"
    )
    prediction_interval_upper_bound: Optional[str] = Field(
        default=None, alias="PredictionIntervalUpperBound"
    )


class GetCostForecastRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    metric: Literal[
        "AMORTIZED_COST",
        "BLENDED_COST",
        "NET_AMORTIZED_COST",
        "NET_UNBLENDED_COST",
        "NORMALIZED_USAGE_AMOUNT",
        "UNBLENDED_COST",
        "USAGE_QUANTITY",
    ] = Field(alias="Metric")
    granularity: Literal["DAILY", "HOURLY", "MONTHLY"] = Field(alias="Granularity")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    prediction_interval_level: Optional[int] = Field(
        default=None, alias="PredictionIntervalLevel"
    )


class GetUsageForecastRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    metric: Literal[
        "AMORTIZED_COST",
        "BLENDED_COST",
        "NET_AMORTIZED_COST",
        "NET_UNBLENDED_COST",
        "NORMALIZED_USAGE_AMOUNT",
        "UNBLENDED_COST",
        "USAGE_QUANTITY",
    ] = Field(alias="Metric")
    granularity: Literal["DAILY", "HOURLY", "MONTHLY"] = Field(alias="Granularity")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    prediction_interval_level: Optional[int] = Field(
        default=None, alias="PredictionIntervalLevel"
    )


class CoverageModel(BaseModel):
    coverage_hours: Optional[CoverageHoursModel] = Field(
        default=None, alias="CoverageHours"
    )
    coverage_normalized_units: Optional[CoverageNormalizedUnitsModel] = Field(
        default=None, alias="CoverageNormalizedUnits"
    )
    coverage_cost: Optional[CoverageCostModel] = Field(
        default=None, alias="CoverageCost"
    )


class CreateAnomalyMonitorRequestModel(BaseModel):
    anomaly_monitor: AnomalyMonitorModel = Field(alias="AnomalyMonitor")
    resource_tags: Optional[Sequence[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_tags: Sequence[ResourceTagModel] = Field(alias="ResourceTags")


class CreateAnomalyMonitorResponseModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAnomalySubscriptionResponseModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCostCategoryDefinitionResponseModel(BaseModel):
    cost_category_arn: str = Field(alias="CostCategoryArn")
    effective_start: str = Field(alias="EffectiveStart")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCostCategoryDefinitionResponseModel(BaseModel):
    cost_category_arn: str = Field(alias="CostCategoryArn")
    effective_end: str = Field(alias="EffectiveEnd")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnomalyMonitorsResponseModel(BaseModel):
    anomaly_monitors: List[AnomalyMonitorModel] = Field(alias="AnomalyMonitors")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCostCategoriesResponseModel(BaseModel):
    next_page_token: str = Field(alias="NextPageToken")
    cost_category_names: List[str] = Field(alias="CostCategoryNames")
    cost_category_values: List[str] = Field(alias="CostCategoryValues")
    return_size: int = Field(alias="ReturnSize")
    total_size: int = Field(alias="TotalSize")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTagsResponseModel(BaseModel):
    next_page_token: str = Field(alias="NextPageToken")
    tags: List[str] = Field(alias="Tags")
    return_size: int = Field(alias="ReturnSize")
    total_size: int = Field(alias="TotalSize")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCostAllocationTagsResponseModel(BaseModel):
    cost_allocation_tags: List[CostAllocationTagModel] = Field(
        alias="CostAllocationTags"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    resource_tags: List[ResourceTagModel] = Field(alias="ResourceTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvideAnomalyFeedbackResponseModel(BaseModel):
    anomaly_id: str = Field(alias="AnomalyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSavingsPlansPurchaseRecommendationGenerationResponseModel(BaseModel):
    recommendation_id: str = Field(alias="RecommendationId")
    generation_started_time: str = Field(alias="GenerationStartedTime")
    estimated_completion_time: str = Field(alias="EstimatedCompletionTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAnomalyMonitorResponseModel(BaseModel):
    monitor_arn: str = Field(alias="MonitorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAnomalySubscriptionResponseModel(BaseModel):
    subscription_arn: str = Field(alias="SubscriptionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCostCategoryDefinitionResponseModel(BaseModel):
    cost_category_arn: str = Field(alias="CostCategoryArn")
    effective_start: str = Field(alias="EffectiveStart")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExpressionModel(BaseModel):
    or_: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="Or")
    and_: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="And")
    not_: Optional[Dict[str, Any]] = Field(default=None, alias="Not")
    dimensions: Optional[DimensionValuesModel] = Field(default=None, alias="Dimensions")
    tags: Optional[TagValuesModel] = Field(default=None, alias="Tags")
    cost_categories: Optional[CostCategoryValuesModel] = Field(
        default=None, alias="CostCategories"
    )


class GetDimensionValuesResponseModel(BaseModel):
    dimension_values: List[DimensionValuesWithAttributesModel] = Field(
        alias="DimensionValues"
    )
    return_size: int = Field(alias="ReturnSize")
    total_size: int = Field(alias="TotalSize")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceDetailsModel(BaseModel):
    ec2_resource_details: Optional[EC2ResourceDetailsModel] = Field(
        default=None, alias="EC2ResourceDetails"
    )


class EC2ResourceUtilizationModel(BaseModel):
    max_cpu_utilization_percentage: Optional[str] = Field(
        default=None, alias="MaxCpuUtilizationPercentage"
    )
    max_memory_utilization_percentage: Optional[str] = Field(
        default=None, alias="MaxMemoryUtilizationPercentage"
    )
    max_storage_utilization_percentage: Optional[str] = Field(
        default=None, alias="MaxStorageUtilizationPercentage"
    )
    ebs_resource_utilization: Optional[EBSResourceUtilizationModel] = Field(
        default=None, alias="EBSResourceUtilization"
    )
    disk_resource_utilization: Optional[DiskResourceUtilizationModel] = Field(
        default=None, alias="DiskResourceUtilization"
    )
    network_resource_utilization: Optional[NetworkResourceUtilizationModel] = Field(
        default=None, alias="NetworkResourceUtilization"
    )


class ServiceSpecificationModel(BaseModel):
    ec2_specification: Optional[EC2SpecificationModel] = Field(
        default=None, alias="EC2Specification"
    )


class ListSavingsPlansPurchaseRecommendationGenerationResponseModel(BaseModel):
    generation_summary_list: List[GenerationSummaryModel] = Field(
        alias="GenerationSummaryList"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnomaliesRequestModel(BaseModel):
    date_interval: AnomalyDateIntervalModel = Field(alias="DateInterval")
    monitor_arn: Optional[str] = Field(default=None, alias="MonitorArn")
    feedback: Optional[Literal["NO", "PLANNED_ACTIVITY", "YES"]] = Field(
        default=None, alias="Feedback"
    )
    total_impact: Optional[TotalImpactFilterModel] = Field(
        default=None, alias="TotalImpact"
    )
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetCostAndUsageRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    granularity: Literal["DAILY", "HOURLY", "MONTHLY"] = Field(alias="Granularity")
    metrics: Sequence[str] = Field(alias="Metrics")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    group_by: Optional[Sequence[GroupDefinitionModel]] = Field(
        default=None, alias="GroupBy"
    )
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class GetCostAndUsageWithResourcesRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    granularity: Literal["DAILY", "HOURLY", "MONTHLY"] = Field(alias="Granularity")
    filter: ExpressionModel = Field(alias="Filter")
    metrics: Optional[Sequence[str]] = Field(default=None, alias="Metrics")
    group_by: Optional[Sequence[GroupDefinitionModel]] = Field(
        default=None, alias="GroupBy"
    )
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class GetCostCategoriesRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    search_string: Optional[str] = Field(default=None, alias="SearchString")
    cost_category_name: Optional[str] = Field(default=None, alias="CostCategoryName")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    sort_by: Optional[Sequence[SortDefinitionModel]] = Field(
        default=None, alias="SortBy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class GetDimensionValuesRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    dimension: Literal[
        "AGREEMENT_END_DATE_TIME_AFTER",
        "AGREEMENT_END_DATE_TIME_BEFORE",
        "ANOMALY_TOTAL_IMPACT_ABSOLUTE",
        "ANOMALY_TOTAL_IMPACT_PERCENTAGE",
        "AZ",
        "BILLING_ENTITY",
        "CACHE_ENGINE",
        "DATABASE_ENGINE",
        "DEPLOYMENT_OPTION",
        "INSTANCE_TYPE",
        "INSTANCE_TYPE_FAMILY",
        "INVOICING_ENTITY",
        "LEGAL_ENTITY_NAME",
        "LINKED_ACCOUNT",
        "LINKED_ACCOUNT_NAME",
        "OPERATING_SYSTEM",
        "OPERATION",
        "PAYMENT_OPTION",
        "PLATFORM",
        "PURCHASE_TYPE",
        "RECORD_TYPE",
        "REGION",
        "RESERVATION_ID",
        "RESOURCE_ID",
        "RIGHTSIZING_TYPE",
        "SAVINGS_PLANS_TYPE",
        "SAVINGS_PLAN_ARN",
        "SCOPE",
        "SERVICE",
        "SERVICE_CODE",
        "SUBSCRIPTION_ID",
        "TENANCY",
        "USAGE_TYPE",
        "USAGE_TYPE_GROUP",
    ] = Field(alias="Dimension")
    search_string: Optional[str] = Field(default=None, alias="SearchString")
    context: Optional[
        Literal["COST_AND_USAGE", "RESERVATIONS", "SAVINGS_PLANS"]
    ] = Field(default=None, alias="Context")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    sort_by: Optional[Sequence[SortDefinitionModel]] = Field(
        default=None, alias="SortBy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class GetReservationCoverageRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    group_by: Optional[Sequence[GroupDefinitionModel]] = Field(
        default=None, alias="GroupBy"
    )
    granularity: Optional[Literal["DAILY", "HOURLY", "MONTHLY"]] = Field(
        default=None, alias="Granularity"
    )
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    metrics: Optional[Sequence[str]] = Field(default=None, alias="Metrics")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")
    sort_by: Optional[SortDefinitionModel] = Field(default=None, alias="SortBy")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetReservationUtilizationRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    group_by: Optional[Sequence[GroupDefinitionModel]] = Field(
        default=None, alias="GroupBy"
    )
    granularity: Optional[Literal["DAILY", "HOURLY", "MONTHLY"]] = Field(
        default=None, alias="Granularity"
    )
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    sort_by: Optional[SortDefinitionModel] = Field(default=None, alias="SortBy")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetSavingsPlansCoverageRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    group_by: Optional[Sequence[GroupDefinitionModel]] = Field(
        default=None, alias="GroupBy"
    )
    granularity: Optional[Literal["DAILY", "HOURLY", "MONTHLY"]] = Field(
        default=None, alias="Granularity"
    )
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    metrics: Optional[Sequence[str]] = Field(default=None, alias="Metrics")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_by: Optional[SortDefinitionModel] = Field(default=None, alias="SortBy")


class GetSavingsPlansUtilizationDetailsRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    data_type: Optional[
        Sequence[
            Literal["AMORTIZED_COMMITMENT", "ATTRIBUTES", "SAVINGS", "UTILIZATION"]
        ]
    ] = Field(default=None, alias="DataType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    sort_by: Optional[SortDefinitionModel] = Field(default=None, alias="SortBy")


class GetSavingsPlansUtilizationRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    granularity: Optional[Literal["DAILY", "HOURLY", "MONTHLY"]] = Field(
        default=None, alias="Granularity"
    )
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    sort_by: Optional[SortDefinitionModel] = Field(default=None, alias="SortBy")


class GetTagsRequestModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    search_string: Optional[str] = Field(default=None, alias="SearchString")
    tag_key: Optional[str] = Field(default=None, alias="TagKey")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    sort_by: Optional[Sequence[SortDefinitionModel]] = Field(
        default=None, alias="SortBy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class GroupModel(BaseModel):
    keys: Optional[List[str]] = Field(default=None, alias="Keys")
    metrics: Optional[Dict[str, MetricValueModel]] = Field(
        default=None, alias="Metrics"
    )


class ReservationUtilizationGroupModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")
    utilization: Optional[ReservationAggregatesModel] = Field(
        default=None, alias="Utilization"
    )


class GetRightsizingRecommendationRequestModel(BaseModel):
    service: str = Field(alias="Service")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    configuration: Optional[RightsizingRecommendationConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class InstanceDetailsModel(BaseModel):
    ec2_instance_details: Optional[EC2InstanceDetailsModel] = Field(
        default=None, alias="EC2InstanceDetails"
    )
    rds_instance_details: Optional[RDSInstanceDetailsModel] = Field(
        default=None, alias="RDSInstanceDetails"
    )
    redshift_instance_details: Optional[RedshiftInstanceDetailsModel] = Field(
        default=None, alias="RedshiftInstanceDetails"
    )
    elasti_cache_instance_details: Optional[ElastiCacheInstanceDetailsModel] = Field(
        default=None, alias="ElastiCacheInstanceDetails"
    )
    es_instance_details: Optional[ESInstanceDetailsModel] = Field(
        default=None, alias="ESInstanceDetails"
    )


class SavingsPlansCoverageModel(BaseModel):
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")
    coverage: Optional[SavingsPlansCoverageDataModel] = Field(
        default=None, alias="Coverage"
    )
    time_period: Optional[DateIntervalModel] = Field(default=None, alias="TimePeriod")


class SavingsPlansPurchaseRecommendationDetailModel(BaseModel):
    savings_plans_details: Optional[SavingsPlansDetailsModel] = Field(
        default=None, alias="SavingsPlansDetails"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    upfront_cost: Optional[str] = Field(default=None, alias="UpfrontCost")
    estimated_roi: Optional[str] = Field(default=None, alias="EstimatedROI")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    estimated_s_p_cost: Optional[str] = Field(default=None, alias="EstimatedSPCost")
    estimated_on_demand_cost: Optional[str] = Field(
        default=None, alias="EstimatedOnDemandCost"
    )
    estimated_on_demand_cost_with_current_commitment: Optional[str] = Field(
        default=None, alias="EstimatedOnDemandCostWithCurrentCommitment"
    )
    estimated_savings_amount: Optional[str] = Field(
        default=None, alias="EstimatedSavingsAmount"
    )
    estimated_savings_percentage: Optional[str] = Field(
        default=None, alias="EstimatedSavingsPercentage"
    )
    hourly_commitment_to_purchase: Optional[str] = Field(
        default=None, alias="HourlyCommitmentToPurchase"
    )
    estimated_average_utilization: Optional[str] = Field(
        default=None, alias="EstimatedAverageUtilization"
    )
    estimated_monthly_savings_amount: Optional[str] = Field(
        default=None, alias="EstimatedMonthlySavingsAmount"
    )
    current_minimum_hourly_on_demand_spend: Optional[str] = Field(
        default=None, alias="CurrentMinimumHourlyOnDemandSpend"
    )
    current_maximum_hourly_on_demand_spend: Optional[str] = Field(
        default=None, alias="CurrentMaximumHourlyOnDemandSpend"
    )
    current_average_hourly_on_demand_spend: Optional[str] = Field(
        default=None, alias="CurrentAverageHourlyOnDemandSpend"
    )


class SavingsPlansUtilizationAggregatesModel(BaseModel):
    utilization: SavingsPlansUtilizationModel = Field(alias="Utilization")
    savings: Optional[SavingsPlansSavingsModel] = Field(default=None, alias="Savings")
    amortized_commitment: Optional[SavingsPlansAmortizedCommitmentModel] = Field(
        default=None, alias="AmortizedCommitment"
    )


class SavingsPlansUtilizationByTimeModel(BaseModel):
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    utilization: SavingsPlansUtilizationModel = Field(alias="Utilization")
    savings: Optional[SavingsPlansSavingsModel] = Field(default=None, alias="Savings")
    amortized_commitment: Optional[SavingsPlansAmortizedCommitmentModel] = Field(
        default=None, alias="AmortizedCommitment"
    )


class SavingsPlansUtilizationDetailModel(BaseModel):
    savings_plan_arn: Optional[str] = Field(default=None, alias="SavingsPlanArn")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")
    utilization: Optional[SavingsPlansUtilizationModel] = Field(
        default=None, alias="Utilization"
    )
    savings: Optional[SavingsPlansSavingsModel] = Field(default=None, alias="Savings")
    amortized_commitment: Optional[SavingsPlansAmortizedCommitmentModel] = Field(
        default=None, alias="AmortizedCommitment"
    )


class UpdateCostAllocationTagsStatusResponseModel(BaseModel):
    errors: List[UpdateCostAllocationTagsStatusErrorModel] = Field(alias="Errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAnomalySubscriptionRequestModel(BaseModel):
    anomaly_subscription: AnomalySubscriptionModel = Field(alias="AnomalySubscription")
    resource_tags: Optional[Sequence[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )


class GetAnomalySubscriptionsResponseModel(BaseModel):
    anomaly_subscriptions: List[AnomalySubscriptionModel] = Field(
        alias="AnomalySubscriptions"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAnomaliesResponseModel(BaseModel):
    anomalies: List[AnomalyModel] = Field(alias="Anomalies")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCostCategoryDefinitionsResponseModel(BaseModel):
    cost_category_references: List[CostCategoryReferenceModel] = Field(
        alias="CostCategoryReferences"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CostCategoryModel(BaseModel):
    cost_category_arn: str = Field(alias="CostCategoryArn")
    effective_start: str = Field(alias="EffectiveStart")
    name: str = Field(alias="Name")
    rule_version: Literal["CostCategoryExpression.v1"] = Field(alias="RuleVersion")
    rules: List[CostCategoryRuleModel] = Field(alias="Rules")
    effective_end: Optional[str] = Field(default=None, alias="EffectiveEnd")
    split_charge_rules: Optional[List[CostCategorySplitChargeRuleModel]] = Field(
        default=None, alias="SplitChargeRules"
    )
    processing_status: Optional[List[CostCategoryProcessingStatusModel]] = Field(
        default=None, alias="ProcessingStatus"
    )
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")


class CreateCostCategoryDefinitionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    rule_version: Literal["CostCategoryExpression.v1"] = Field(alias="RuleVersion")
    rules: Sequence[CostCategoryRuleModel] = Field(alias="Rules")
    effective_start: Optional[str] = Field(default=None, alias="EffectiveStart")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    split_charge_rules: Optional[Sequence[CostCategorySplitChargeRuleModel]] = Field(
        default=None, alias="SplitChargeRules"
    )
    resource_tags: Optional[Sequence[ResourceTagModel]] = Field(
        default=None, alias="ResourceTags"
    )


class UpdateCostCategoryDefinitionRequestModel(BaseModel):
    cost_category_arn: str = Field(alias="CostCategoryArn")
    rule_version: Literal["CostCategoryExpression.v1"] = Field(alias="RuleVersion")
    rules: Sequence[CostCategoryRuleModel] = Field(alias="Rules")
    effective_start: Optional[str] = Field(default=None, alias="EffectiveStart")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    split_charge_rules: Optional[Sequence[CostCategorySplitChargeRuleModel]] = Field(
        default=None, alias="SplitChargeRules"
    )


class GetCostForecastResponseModel(BaseModel):
    total: MetricValueModel = Field(alias="Total")
    forecast_results_by_time: List[ForecastResultModel] = Field(
        alias="ForecastResultsByTime"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUsageForecastResponseModel(BaseModel):
    total: MetricValueModel = Field(alias="Total")
    forecast_results_by_time: List[ForecastResultModel] = Field(
        alias="ForecastResultsByTime"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservationCoverageGroupModel(BaseModel):
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")
    coverage: Optional[CoverageModel] = Field(default=None, alias="Coverage")


class ResourceUtilizationModel(BaseModel):
    ec2_resource_utilization: Optional[EC2ResourceUtilizationModel] = Field(
        default=None, alias="EC2ResourceUtilization"
    )


class GetReservationPurchaseRecommendationRequestModel(BaseModel):
    service: str = Field(alias="Service")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    filter: Optional[ExpressionModel] = Field(default=None, alias="Filter")
    account_scope: Optional[Literal["LINKED", "PAYER"]] = Field(
        default=None, alias="AccountScope"
    )
    lookback_period_in_days: Optional[
        Literal["SEVEN_DAYS", "SIXTY_DAYS", "THIRTY_DAYS"]
    ] = Field(default=None, alias="LookbackPeriodInDays")
    term_in_years: Optional[Literal["ONE_YEAR", "THREE_YEARS"]] = Field(
        default=None, alias="TermInYears"
    )
    payment_option: Optional[
        Literal[
            "ALL_UPFRONT",
            "HEAVY_UTILIZATION",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
        ]
    ] = Field(default=None, alias="PaymentOption")
    service_specification: Optional[ServiceSpecificationModel] = Field(
        default=None, alias="ServiceSpecification"
    )
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class ResultByTimeModel(BaseModel):
    time_period: Optional[DateIntervalModel] = Field(default=None, alias="TimePeriod")
    total: Optional[Dict[str, MetricValueModel]] = Field(default=None, alias="Total")
    groups: Optional[List[GroupModel]] = Field(default=None, alias="Groups")
    estimated: Optional[bool] = Field(default=None, alias="Estimated")


class UtilizationByTimeModel(BaseModel):
    time_period: Optional[DateIntervalModel] = Field(default=None, alias="TimePeriod")
    groups: Optional[List[ReservationUtilizationGroupModel]] = Field(
        default=None, alias="Groups"
    )
    total: Optional[ReservationAggregatesModel] = Field(default=None, alias="Total")


class ReservationPurchaseRecommendationDetailModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    instance_details: Optional[InstanceDetailsModel] = Field(
        default=None, alias="InstanceDetails"
    )
    recommended_number_of_instances_to_purchase: Optional[str] = Field(
        default=None, alias="RecommendedNumberOfInstancesToPurchase"
    )
    recommended_normalized_units_to_purchase: Optional[str] = Field(
        default=None, alias="RecommendedNormalizedUnitsToPurchase"
    )
    minimum_number_of_instances_used_per_hour: Optional[str] = Field(
        default=None, alias="MinimumNumberOfInstancesUsedPerHour"
    )
    minimum_normalized_units_used_per_hour: Optional[str] = Field(
        default=None, alias="MinimumNormalizedUnitsUsedPerHour"
    )
    maximum_number_of_instances_used_per_hour: Optional[str] = Field(
        default=None, alias="MaximumNumberOfInstancesUsedPerHour"
    )
    maximum_normalized_units_used_per_hour: Optional[str] = Field(
        default=None, alias="MaximumNormalizedUnitsUsedPerHour"
    )
    average_number_of_instances_used_per_hour: Optional[str] = Field(
        default=None, alias="AverageNumberOfInstancesUsedPerHour"
    )
    average_normalized_units_used_per_hour: Optional[str] = Field(
        default=None, alias="AverageNormalizedUnitsUsedPerHour"
    )
    average_utilization: Optional[str] = Field(default=None, alias="AverageUtilization")
    estimated_break_even_in_months: Optional[str] = Field(
        default=None, alias="EstimatedBreakEvenInMonths"
    )
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    estimated_monthly_savings_amount: Optional[str] = Field(
        default=None, alias="EstimatedMonthlySavingsAmount"
    )
    estimated_monthly_savings_percentage: Optional[str] = Field(
        default=None, alias="EstimatedMonthlySavingsPercentage"
    )
    estimated_monthly_on_demand_cost: Optional[str] = Field(
        default=None, alias="EstimatedMonthlyOnDemandCost"
    )
    estimated_reservation_cost_for_lookback_period: Optional[str] = Field(
        default=None, alias="EstimatedReservationCostForLookbackPeriod"
    )
    upfront_cost: Optional[str] = Field(default=None, alias="UpfrontCost")
    recurring_standard_monthly_cost: Optional[str] = Field(
        default=None, alias="RecurringStandardMonthlyCost"
    )


class GetSavingsPlansCoverageResponseModel(BaseModel):
    savings_plans_coverages: List[SavingsPlansCoverageModel] = Field(
        alias="SavingsPlansCoverages"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SavingsPlansPurchaseRecommendationModel(BaseModel):
    account_scope: Optional[Literal["LINKED", "PAYER"]] = Field(
        default=None, alias="AccountScope"
    )
    savings_plans_type: Optional[
        Literal["COMPUTE_SP", "EC2_INSTANCE_SP", "SAGEMAKER_SP"]
    ] = Field(default=None, alias="SavingsPlansType")
    term_in_years: Optional[Literal["ONE_YEAR", "THREE_YEARS"]] = Field(
        default=None, alias="TermInYears"
    )
    payment_option: Optional[
        Literal[
            "ALL_UPFRONT",
            "HEAVY_UTILIZATION",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
        ]
    ] = Field(default=None, alias="PaymentOption")
    lookback_period_in_days: Optional[
        Literal["SEVEN_DAYS", "SIXTY_DAYS", "THIRTY_DAYS"]
    ] = Field(default=None, alias="LookbackPeriodInDays")
    savings_plans_purchase_recommendation_details: Optional[
        List[SavingsPlansPurchaseRecommendationDetailModel]
    ] = Field(default=None, alias="SavingsPlansPurchaseRecommendationDetails")
    savings_plans_purchase_recommendation_summary: Optional[
        SavingsPlansPurchaseRecommendationSummaryModel
    ] = Field(default=None, alias="SavingsPlansPurchaseRecommendationSummary")


class GetSavingsPlansUtilizationResponseModel(BaseModel):
    savings_plans_utilizations_by_time: List[
        SavingsPlansUtilizationByTimeModel
    ] = Field(alias="SavingsPlansUtilizationsByTime")
    total: SavingsPlansUtilizationAggregatesModel = Field(alias="Total")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSavingsPlansUtilizationDetailsResponseModel(BaseModel):
    savings_plans_utilization_details: List[SavingsPlansUtilizationDetailModel] = Field(
        alias="SavingsPlansUtilizationDetails"
    )
    total: SavingsPlansUtilizationAggregatesModel = Field(alias="Total")
    time_period: DateIntervalModel = Field(alias="TimePeriod")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCostCategoryDefinitionResponseModel(BaseModel):
    cost_category: CostCategoryModel = Field(alias="CostCategory")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CoverageByTimeModel(BaseModel):
    time_period: Optional[DateIntervalModel] = Field(default=None, alias="TimePeriod")
    groups: Optional[List[ReservationCoverageGroupModel]] = Field(
        default=None, alias="Groups"
    )
    total: Optional[CoverageModel] = Field(default=None, alias="Total")


class CurrentInstanceModel(BaseModel):
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    instance_name: Optional[str] = Field(default=None, alias="InstanceName")
    tags: Optional[List[TagValuesModel]] = Field(default=None, alias="Tags")
    resource_details: Optional[ResourceDetailsModel] = Field(
        default=None, alias="ResourceDetails"
    )
    resource_utilization: Optional[ResourceUtilizationModel] = Field(
        default=None, alias="ResourceUtilization"
    )
    reservation_covered_hours_in_lookback_period: Optional[str] = Field(
        default=None, alias="ReservationCoveredHoursInLookbackPeriod"
    )
    savings_plans_covered_hours_in_lookback_period: Optional[str] = Field(
        default=None, alias="SavingsPlansCoveredHoursInLookbackPeriod"
    )
    on_demand_hours_in_lookback_period: Optional[str] = Field(
        default=None, alias="OnDemandHoursInLookbackPeriod"
    )
    total_running_hours_in_lookback_period: Optional[str] = Field(
        default=None, alias="TotalRunningHoursInLookbackPeriod"
    )
    monthly_cost: Optional[str] = Field(default=None, alias="MonthlyCost")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")


class TargetInstanceModel(BaseModel):
    estimated_monthly_cost: Optional[str] = Field(
        default=None, alias="EstimatedMonthlyCost"
    )
    estimated_monthly_savings: Optional[str] = Field(
        default=None, alias="EstimatedMonthlySavings"
    )
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    default_target_instance: Optional[bool] = Field(
        default=None, alias="DefaultTargetInstance"
    )
    resource_details: Optional[ResourceDetailsModel] = Field(
        default=None, alias="ResourceDetails"
    )
    expected_resource_utilization: Optional[ResourceUtilizationModel] = Field(
        default=None, alias="ExpectedResourceUtilization"
    )
    platform_differences: Optional[
        List[
            Literal[
                "HYPERVISOR",
                "INSTANCE_STORE_AVAILABILITY",
                "NETWORK_INTERFACE",
                "STORAGE_INTERFACE",
                "VIRTUALIZATION_TYPE",
            ]
        ]
    ] = Field(default=None, alias="PlatformDifferences")


class GetCostAndUsageResponseModel(BaseModel):
    next_page_token: str = Field(alias="NextPageToken")
    group_definitions: List[GroupDefinitionModel] = Field(alias="GroupDefinitions")
    results_by_time: List[ResultByTimeModel] = Field(alias="ResultsByTime")
    dimension_value_attributes: List[DimensionValuesWithAttributesModel] = Field(
        alias="DimensionValueAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCostAndUsageWithResourcesResponseModel(BaseModel):
    next_page_token: str = Field(alias="NextPageToken")
    group_definitions: List[GroupDefinitionModel] = Field(alias="GroupDefinitions")
    results_by_time: List[ResultByTimeModel] = Field(alias="ResultsByTime")
    dimension_value_attributes: List[DimensionValuesWithAttributesModel] = Field(
        alias="DimensionValueAttributes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReservationUtilizationResponseModel(BaseModel):
    utilizations_by_time: List[UtilizationByTimeModel] = Field(
        alias="UtilizationsByTime"
    )
    total: ReservationAggregatesModel = Field(alias="Total")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReservationPurchaseRecommendationModel(BaseModel):
    account_scope: Optional[Literal["LINKED", "PAYER"]] = Field(
        default=None, alias="AccountScope"
    )
    lookback_period_in_days: Optional[
        Literal["SEVEN_DAYS", "SIXTY_DAYS", "THIRTY_DAYS"]
    ] = Field(default=None, alias="LookbackPeriodInDays")
    term_in_years: Optional[Literal["ONE_YEAR", "THREE_YEARS"]] = Field(
        default=None, alias="TermInYears"
    )
    payment_option: Optional[
        Literal[
            "ALL_UPFRONT",
            "HEAVY_UTILIZATION",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
        ]
    ] = Field(default=None, alias="PaymentOption")
    service_specification: Optional[ServiceSpecificationModel] = Field(
        default=None, alias="ServiceSpecification"
    )
    recommendation_details: Optional[
        List[ReservationPurchaseRecommendationDetailModel]
    ] = Field(default=None, alias="RecommendationDetails")
    recommendation_summary: Optional[
        ReservationPurchaseRecommendationSummaryModel
    ] = Field(default=None, alias="RecommendationSummary")


class GetSavingsPlansPurchaseRecommendationResponseModel(BaseModel):
    metadata: SavingsPlansPurchaseRecommendationMetadataModel = Field(alias="Metadata")
    savings_plans_purchase_recommendation: SavingsPlansPurchaseRecommendationModel = (
        Field(alias="SavingsPlansPurchaseRecommendation")
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReservationCoverageResponseModel(BaseModel):
    coverages_by_time: List[CoverageByTimeModel] = Field(alias="CoveragesByTime")
    total: CoverageModel = Field(alias="Total")
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyRecommendationDetailModel(BaseModel):
    target_instances: Optional[List[TargetInstanceModel]] = Field(
        default=None, alias="TargetInstances"
    )


class GetReservationPurchaseRecommendationResponseModel(BaseModel):
    metadata: ReservationPurchaseRecommendationMetadataModel = Field(alias="Metadata")
    recommendations: List[ReservationPurchaseRecommendationModel] = Field(
        alias="Recommendations"
    )
    next_page_token: str = Field(alias="NextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RightsizingRecommendationModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    current_instance: Optional[CurrentInstanceModel] = Field(
        default=None, alias="CurrentInstance"
    )
    rightsizing_type: Optional[Literal["MODIFY", "TERMINATE"]] = Field(
        default=None, alias="RightsizingType"
    )
    modify_recommendation_detail: Optional[ModifyRecommendationDetailModel] = Field(
        default=None, alias="ModifyRecommendationDetail"
    )
    terminate_recommendation_detail: Optional[
        TerminateRecommendationDetailModel
    ] = Field(default=None, alias="TerminateRecommendationDetail")
    finding_reason_codes: Optional[
        List[
            Literal[
                "CPU_OVER_PROVISIONED",
                "CPU_UNDER_PROVISIONED",
                "DISK_IOPS_OVER_PROVISIONED",
                "DISK_IOPS_UNDER_PROVISIONED",
                "DISK_THROUGHPUT_OVER_PROVISIONED",
                "DISK_THROUGHPUT_UNDER_PROVISIONED",
                "EBS_IOPS_OVER_PROVISIONED",
                "EBS_IOPS_UNDER_PROVISIONED",
                "EBS_THROUGHPUT_OVER_PROVISIONED",
                "EBS_THROUGHPUT_UNDER_PROVISIONED",
                "MEMORY_OVER_PROVISIONED",
                "MEMORY_UNDER_PROVISIONED",
                "NETWORK_BANDWIDTH_OVER_PROVISIONED",
                "NETWORK_BANDWIDTH_UNDER_PROVISIONED",
                "NETWORK_PPS_OVER_PROVISIONED",
                "NETWORK_PPS_UNDER_PROVISIONED",
            ]
        ]
    ] = Field(default=None, alias="FindingReasonCodes")


class GetRightsizingRecommendationResponseModel(BaseModel):
    metadata: RightsizingRecommendationMetadataModel = Field(alias="Metadata")
    summary: RightsizingRecommendationSummaryModel = Field(alias="Summary")
    rightsizing_recommendations: List[RightsizingRecommendationModel] = Field(
        alias="RightsizingRecommendations"
    )
    next_page_token: str = Field(alias="NextPageToken")
    configuration: RightsizingRecommendationConfigurationModel = Field(
        alias="Configuration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
