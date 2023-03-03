# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountAssociationsListElementModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    billing_group_arn: Optional[str] = Field(default=None, alias="BillingGroupArn")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    account_email: Optional[str] = Field(default=None, alias="AccountEmail")


class AccountGroupingModel(BaseModel):
    linked_account_ids: Sequence[str] = Field(alias="LinkedAccountIds")


class AssociateAccountsInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociatePricingRulesInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    pricing_rule_arns: Sequence[str] = Field(alias="PricingRuleArns")


class AssociateResourceErrorModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    reason: Optional[
        Literal[
            "ILLEGAL_CUSTOMLINEITEM",
            "INTERNAL_SERVER_EXCEPTION",
            "INVALID_ARN",
            "INVALID_BILLING_PERIOD_RANGE",
            "SERVICE_LIMIT_EXCEEDED",
        ]
    ] = Field(default=None, alias="Reason")


class CustomLineItemBillingPeriodRangeModel(BaseModel):
    inclusive_start_billing_period: str = Field(alias="InclusiveStartBillingPeriod")
    exclusive_end_billing_period: Optional[str] = Field(
        default=None, alias="ExclusiveEndBillingPeriod"
    )


class BillingGroupCostReportElementModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    aws_cost: Optional[str] = Field(default=None, alias="AWSCost")
    proforma_cost: Optional[str] = Field(default=None, alias="ProformaCost")
    margin: Optional[str] = Field(default=None, alias="Margin")
    margin_percentage: Optional[str] = Field(default=None, alias="MarginPercentage")
    currency: Optional[str] = Field(default=None, alias="Currency")


class ComputationPreferenceModel(BaseModel):
    pricing_plan_arn: str = Field(alias="PricingPlanArn")


class CreateFreeTierConfigModel(BaseModel):
    activated: bool = Field(alias="Activated")


class CreatePricingPlanInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_rule_arns: Optional[Sequence[str]] = Field(
        default=None, alias="PricingRuleArns"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CustomLineItemFlatChargeDetailsModel(BaseModel):
    charge_value: float = Field(alias="ChargeValue")


class CustomLineItemPercentageChargeDetailsModel(BaseModel):
    percentage_value: float = Field(alias="PercentageValue")
    associated_values: Optional[Sequence[str]] = Field(
        default=None, alias="AssociatedValues"
    )


class DeleteBillingGroupInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DeletePricingPlanInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DeletePricingRuleInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DisassociateAccountsInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class DisassociatePricingRulesInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    pricing_rule_arns: Sequence[str] = Field(alias="PricingRuleArns")


class FreeTierConfigModel(BaseModel):
    activated: bool = Field(alias="Activated")


class ListAccountAssociationsFilterModel(BaseModel):
    association: Optional[str] = Field(default=None, alias="Association")
    account_id: Optional[str] = Field(default=None, alias="AccountId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBillingGroupCostReportsFilterModel(BaseModel):
    billing_group_arns: Optional[Sequence[str]] = Field(
        default=None, alias="BillingGroupArns"
    )


class ListBillingGroupsFilterModel(BaseModel):
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")
    pricing_plan: Optional[str] = Field(default=None, alias="PricingPlan")


class ListCustomLineItemFlatChargeDetailsModel(BaseModel):
    charge_value: float = Field(alias="ChargeValue")


class ListCustomLineItemPercentageChargeDetailsModel(BaseModel):
    percentage_value: float = Field(alias="PercentageValue")


class ListCustomLineItemVersionsBillingPeriodRangeFilterModel(BaseModel):
    start_billing_period: Optional[str] = Field(
        default=None, alias="StartBillingPeriod"
    )
    end_billing_period: Optional[str] = Field(default=None, alias="EndBillingPeriod")


class ListCustomLineItemsFilterModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    billing_groups: Optional[Sequence[str]] = Field(default=None, alias="BillingGroups")
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")


class ListPricingPlansAssociatedWithPricingRuleInputRequestModel(BaseModel):
    pricing_rule_arn: str = Field(alias="PricingRuleArn")
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPricingPlansFilterModel(BaseModel):
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")


class PricingPlanListElementModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    size: Optional[int] = Field(default=None, alias="Size")
    creation_time: Optional[int] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[int] = Field(default=None, alias="LastModifiedTime")


class ListPricingRulesAssociatedToPricingPlanInputRequestModel(BaseModel):
    pricing_plan_arn: str = Field(alias="PricingPlanArn")
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPricingRulesFilterModel(BaseModel):
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")


class ListResourcesAssociatedToCustomLineItemFilterModel(BaseModel):
    relationship: Optional[Literal["CHILD", "PARENT"]] = Field(
        default=None, alias="Relationship"
    )


class ListResourcesAssociatedToCustomLineItemResponseElementModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    relationship: Optional[Literal["CHILD", "PARENT"]] = Field(
        default=None, alias="Relationship"
    )
    end_billing_period: Optional[str] = Field(default=None, alias="EndBillingPeriod")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateCustomLineItemFlatChargeDetailsModel(BaseModel):
    charge_value: float = Field(alias="ChargeValue")


class UpdateCustomLineItemPercentageChargeDetailsModel(BaseModel):
    percentage_value: float = Field(alias="PercentageValue")


class UpdateFreeTierConfigModel(BaseModel):
    activated: bool = Field(alias="Activated")


class UpdatePricingPlanInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class AssociateAccountsOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociatePricingRulesOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBillingGroupOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomLineItemOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePricingPlanOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePricingRuleOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBillingGroupOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCustomLineItemOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePricingPlanOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePricingRuleOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateAccountsOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociatePricingRulesOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountAssociationsOutputModel(BaseModel):
    linked_accounts: List[AccountAssociationsListElementModel] = Field(
        alias="LinkedAccounts"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPricingPlansAssociatedWithPricingRuleOutputModel(BaseModel):
    billing_period: str = Field(alias="BillingPeriod")
    pricing_rule_arn: str = Field(alias="PricingRuleArn")
    pricing_plan_arns: List[str] = Field(alias="PricingPlanArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPricingRulesAssociatedToPricingPlanOutputModel(BaseModel):
    billing_period: str = Field(alias="BillingPeriod")
    pricing_plan_arn: str = Field(alias="PricingPlanArn")
    pricing_rule_arns: List[str] = Field(alias="PricingRuleArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBillingGroupOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    primary_account_id: str = Field(alias="PrimaryAccountId")
    pricing_plan_arn: str = Field(alias="PricingPlanArn")
    size: int = Field(alias="Size")
    last_modified_time: int = Field(alias="LastModifiedTime")
    status: Literal["ACTIVE", "PRIMARY_ACCOUNT_MISSING"] = Field(alias="Status")
    status_reason: str = Field(alias="StatusReason")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePricingPlanOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    size: int = Field(alias="Size")
    last_modified_time: int = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateResourceResponseElementModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    error: Optional[AssociateResourceErrorModel] = Field(default=None, alias="Error")


class DisassociateResourceResponseElementModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    error: Optional[AssociateResourceErrorModel] = Field(default=None, alias="Error")


class BatchAssociateResourcesToCustomLineItemInputRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetArn")
    resource_arns: Sequence[str] = Field(alias="ResourceArns")
    billing_period_range: Optional[CustomLineItemBillingPeriodRangeModel] = Field(
        default=None, alias="BillingPeriodRange"
    )


class BatchDisassociateResourcesFromCustomLineItemInputRequestModel(BaseModel):
    target_arn: str = Field(alias="TargetArn")
    resource_arns: Sequence[str] = Field(alias="ResourceArns")
    billing_period_range: Optional[CustomLineItemBillingPeriodRangeModel] = Field(
        default=None, alias="BillingPeriodRange"
    )


class DeleteCustomLineItemInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    billing_period_range: Optional[CustomLineItemBillingPeriodRangeModel] = Field(
        default=None, alias="BillingPeriodRange"
    )


class ListBillingGroupCostReportsOutputModel(BaseModel):
    billing_group_cost_reports: List[BillingGroupCostReportElementModel] = Field(
        alias="BillingGroupCostReports"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BillingGroupListElementModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    primary_account_id: Optional[str] = Field(default=None, alias="PrimaryAccountId")
    computation_preference: Optional[ComputationPreferenceModel] = Field(
        default=None, alias="ComputationPreference"
    )
    size: Optional[int] = Field(default=None, alias="Size")
    creation_time: Optional[int] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[int] = Field(default=None, alias="LastModifiedTime")
    status: Optional[Literal["ACTIVE", "PRIMARY_ACCOUNT_MISSING"]] = Field(
        default=None, alias="Status"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")


class CreateBillingGroupInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    account_grouping: AccountGroupingModel = Field(alias="AccountGrouping")
    computation_preference: ComputationPreferenceModel = Field(
        alias="ComputationPreference"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    primary_account_id: Optional[str] = Field(default=None, alias="PrimaryAccountId")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateBillingGroupInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["ACTIVE", "PRIMARY_ACCOUNT_MISSING"]] = Field(
        default=None, alias="Status"
    )
    computation_preference: Optional[ComputationPreferenceModel] = Field(
        default=None, alias="ComputationPreference"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class CreateTieringInputModel(BaseModel):
    free_tier: CreateFreeTierConfigModel = Field(alias="FreeTier")


class CustomLineItemChargeDetailsModel(BaseModel):
    type: Literal["CREDIT", "FEE"] = Field(alias="Type")
    flat: Optional[CustomLineItemFlatChargeDetailsModel] = Field(
        default=None, alias="Flat"
    )
    percentage: Optional[CustomLineItemPercentageChargeDetailsModel] = Field(
        default=None, alias="Percentage"
    )


class TieringModel(BaseModel):
    free_tier: FreeTierConfigModel = Field(alias="FreeTier")


class ListAccountAssociationsInputRequestModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListAccountAssociationsFilterModel] = Field(
        default=None, alias="Filters"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAccountAssociationsInputListAccountAssociationsPaginateModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListAccountAssociationsFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateModel(
    BaseModel
):
    pricing_rule_arn: str = Field(alias="PricingRuleArn")
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateModel(
    BaseModel
):
    pricing_plan_arn: str = Field(alias="PricingPlanArn")
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateModel(
    BaseModel
):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListBillingGroupCostReportsFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBillingGroupCostReportsInputRequestModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[ListBillingGroupCostReportsFilterModel] = Field(
        default=None, alias="Filters"
    )


class ListBillingGroupsInputListBillingGroupsPaginateModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListBillingGroupsFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBillingGroupsInputRequestModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[ListBillingGroupsFilterModel] = Field(
        default=None, alias="Filters"
    )


class ListCustomLineItemChargeDetailsModel(BaseModel):
    type: Literal["CREDIT", "FEE"] = Field(alias="Type")
    flat: Optional[ListCustomLineItemFlatChargeDetailsModel] = Field(
        default=None, alias="Flat"
    )
    percentage: Optional[ListCustomLineItemPercentageChargeDetailsModel] = Field(
        default=None, alias="Percentage"
    )


class ListCustomLineItemVersionsFilterModel(BaseModel):
    billing_period_range: Optional[
        ListCustomLineItemVersionsBillingPeriodRangeFilterModel
    ] = Field(default=None, alias="BillingPeriodRange")


class ListCustomLineItemsInputListCustomLineItemsPaginateModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListCustomLineItemsFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomLineItemsInputRequestModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[ListCustomLineItemsFilterModel] = Field(
        default=None, alias="Filters"
    )


class ListPricingPlansInputListPricingPlansPaginateModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListPricingPlansFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPricingPlansInputRequestModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListPricingPlansFilterModel] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPricingPlansOutputModel(BaseModel):
    billing_period: str = Field(alias="BillingPeriod")
    pricing_plans: List[PricingPlanListElementModel] = Field(alias="PricingPlans")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPricingRulesInputListPricingRulesPaginateModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListPricingRulesFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPricingRulesInputRequestModel(BaseModel):
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListPricingRulesFilterModel] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateModel(
    BaseModel
):
    arn: str = Field(alias="Arn")
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    filters: Optional[ListResourcesAssociatedToCustomLineItemFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourcesAssociatedToCustomLineItemInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    billing_period: Optional[str] = Field(default=None, alias="BillingPeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[ListResourcesAssociatedToCustomLineItemFilterModel] = Field(
        default=None, alias="Filters"
    )


class ListResourcesAssociatedToCustomLineItemOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    associated_resources: List[
        ListResourcesAssociatedToCustomLineItemResponseElementModel
    ] = Field(alias="AssociatedResources")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCustomLineItemChargeDetailsModel(BaseModel):
    flat: Optional[UpdateCustomLineItemFlatChargeDetailsModel] = Field(
        default=None, alias="Flat"
    )
    percentage: Optional[UpdateCustomLineItemPercentageChargeDetailsModel] = Field(
        default=None, alias="Percentage"
    )


class UpdateTieringInputModel(BaseModel):
    free_tier: UpdateFreeTierConfigModel = Field(alias="FreeTier")


class BatchAssociateResourcesToCustomLineItemOutputModel(BaseModel):
    successfully_associated_resources: List[
        AssociateResourceResponseElementModel
    ] = Field(alias="SuccessfullyAssociatedResources")
    failed_associated_resources: List[AssociateResourceResponseElementModel] = Field(
        alias="FailedAssociatedResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateResourcesFromCustomLineItemOutputModel(BaseModel):
    successfully_disassociated_resources: List[
        DisassociateResourceResponseElementModel
    ] = Field(alias="SuccessfullyDisassociatedResources")
    failed_disassociated_resources: List[
        DisassociateResourceResponseElementModel
    ] = Field(alias="FailedDisassociatedResources")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBillingGroupsOutputModel(BaseModel):
    billing_groups: List[BillingGroupListElementModel] = Field(alias="BillingGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePricingRuleInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    scope: Literal["BILLING_ENTITY", "GLOBAL", "SERVICE"] = Field(alias="Scope")
    type: Literal["DISCOUNT", "MARKUP", "TIERING"] = Field(alias="Type")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    modifier_percentage: Optional[float] = Field(
        default=None, alias="ModifierPercentage"
    )
    service: Optional[str] = Field(default=None, alias="Service")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    billing_entity: Optional[str] = Field(default=None, alias="BillingEntity")
    tiering: Optional[CreateTieringInputModel] = Field(default=None, alias="Tiering")
    usage_type: Optional[str] = Field(default=None, alias="UsageType")
    operation: Optional[str] = Field(default=None, alias="Operation")


class CreateCustomLineItemInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    billing_group_arn: str = Field(alias="BillingGroupArn")
    charge_details: CustomLineItemChargeDetailsModel = Field(alias="ChargeDetails")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    billing_period_range: Optional[CustomLineItemBillingPeriodRangeModel] = Field(
        default=None, alias="BillingPeriodRange"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class PricingRuleListElementModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    scope: Optional[Literal["BILLING_ENTITY", "GLOBAL", "SERVICE"]] = Field(
        default=None, alias="Scope"
    )
    type: Optional[Literal["DISCOUNT", "MARKUP", "TIERING"]] = Field(
        default=None, alias="Type"
    )
    modifier_percentage: Optional[float] = Field(
        default=None, alias="ModifierPercentage"
    )
    service: Optional[str] = Field(default=None, alias="Service")
    associated_pricing_plan_count: Optional[int] = Field(
        default=None, alias="AssociatedPricingPlanCount"
    )
    creation_time: Optional[int] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[int] = Field(default=None, alias="LastModifiedTime")
    billing_entity: Optional[str] = Field(default=None, alias="BillingEntity")
    tiering: Optional[TieringModel] = Field(default=None, alias="Tiering")


class CustomLineItemListElementModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    charge_details: Optional[ListCustomLineItemChargeDetailsModel] = Field(
        default=None, alias="ChargeDetails"
    )
    currency_code: Optional[Literal["CNY", "USD"]] = Field(
        default=None, alias="CurrencyCode"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    product_code: Optional[str] = Field(default=None, alias="ProductCode")
    billing_group_arn: Optional[str] = Field(default=None, alias="BillingGroupArn")
    creation_time: Optional[int] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[int] = Field(default=None, alias="LastModifiedTime")
    association_size: Optional[int] = Field(default=None, alias="AssociationSize")


class CustomLineItemVersionListElementModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    charge_details: Optional[ListCustomLineItemChargeDetailsModel] = Field(
        default=None, alias="ChargeDetails"
    )
    currency_code: Optional[Literal["CNY", "USD"]] = Field(
        default=None, alias="CurrencyCode"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    product_code: Optional[str] = Field(default=None, alias="ProductCode")
    billing_group_arn: Optional[str] = Field(default=None, alias="BillingGroupArn")
    creation_time: Optional[int] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[int] = Field(default=None, alias="LastModifiedTime")
    association_size: Optional[int] = Field(default=None, alias="AssociationSize")
    start_billing_period: Optional[str] = Field(
        default=None, alias="StartBillingPeriod"
    )
    end_billing_period: Optional[str] = Field(default=None, alias="EndBillingPeriod")


class UpdateCustomLineItemOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    billing_group_arn: str = Field(alias="BillingGroupArn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    charge_details: ListCustomLineItemChargeDetailsModel = Field(alias="ChargeDetails")
    last_modified_time: int = Field(alias="LastModifiedTime")
    association_size: int = Field(alias="AssociationSize")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateModel(BaseModel):
    arn: str = Field(alias="Arn")
    filters: Optional[ListCustomLineItemVersionsFilterModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomLineItemVersionsInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[ListCustomLineItemVersionsFilterModel] = Field(
        default=None, alias="Filters"
    )


class UpdateCustomLineItemInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    charge_details: Optional[UpdateCustomLineItemChargeDetailsModel] = Field(
        default=None, alias="ChargeDetails"
    )
    billing_period_range: Optional[CustomLineItemBillingPeriodRangeModel] = Field(
        default=None, alias="BillingPeriodRange"
    )


class UpdatePricingRuleInputRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[Literal["DISCOUNT", "MARKUP", "TIERING"]] = Field(
        default=None, alias="Type"
    )
    modifier_percentage: Optional[float] = Field(
        default=None, alias="ModifierPercentage"
    )
    tiering: Optional[UpdateTieringInputModel] = Field(default=None, alias="Tiering")


class UpdatePricingRuleOutputModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    scope: Literal["BILLING_ENTITY", "GLOBAL", "SERVICE"] = Field(alias="Scope")
    type: Literal["DISCOUNT", "MARKUP", "TIERING"] = Field(alias="Type")
    modifier_percentage: float = Field(alias="ModifierPercentage")
    service: str = Field(alias="Service")
    associated_pricing_plan_count: int = Field(alias="AssociatedPricingPlanCount")
    last_modified_time: int = Field(alias="LastModifiedTime")
    billing_entity: str = Field(alias="BillingEntity")
    tiering: UpdateTieringInputModel = Field(alias="Tiering")
    usage_type: str = Field(alias="UsageType")
    operation: str = Field(alias="Operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPricingRulesOutputModel(BaseModel):
    billing_period: str = Field(alias="BillingPeriod")
    pricing_rules: List[PricingRuleListElementModel] = Field(alias="PricingRules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomLineItemsOutputModel(BaseModel):
    custom_line_items: List[CustomLineItemListElementModel] = Field(
        alias="CustomLineItems"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomLineItemVersionsOutputModel(BaseModel):
    custom_line_item_versions: List[CustomLineItemVersionListElementModel] = Field(
        alias="CustomLineItemVersions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
