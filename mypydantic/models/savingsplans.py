# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CreateSavingsPlanRequestModel(BaseModel):
    savings_plan_offering_id: str = Field(alias="savingsPlanOfferingId")
    commitment: str = Field(alias="commitment")
    upfront_payment_amount: Optional[str] = Field(
        default=None, alias="upfrontPaymentAmount"
    )
    purchase_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="purchaseTime"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteQueuedSavingsPlanRequestModel(BaseModel):
    savings_plan_id: str = Field(alias="savingsPlanId")


class SavingsPlanRateFilterModel(BaseModel):
    name: Optional[
        Literal[
            "instanceType",
            "operation",
            "productDescription",
            "productType",
            "region",
            "serviceCode",
            "tenancy",
            "usageType",
        ]
    ] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class SavingsPlanOfferingRateFilterElementModel(BaseModel):
    name: Optional[
        Literal[
            "instanceFamily",
            "instanceType",
            "productDescription",
            "productId",
            "region",
            "tenancy",
        ]
    ] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class SavingsPlanOfferingFilterElementModel(BaseModel):
    name: Optional[Literal["instanceFamily", "region"]] = Field(
        default=None, alias="name"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class SavingsPlanFilterModel(BaseModel):
    name: Optional[
        Literal[
            "commitment",
            "ec2-instance-family",
            "end",
            "payment-option",
            "region",
            "savings-plan-type",
            "start",
            "term",
            "upfront",
        ]
    ] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class SavingsPlanModel(BaseModel):
    offering_id: Optional[str] = Field(default=None, alias="offeringId")
    savings_plan_id: Optional[str] = Field(default=None, alias="savingsPlanId")
    savings_plan_arn: Optional[str] = Field(default=None, alias="savingsPlanArn")
    description: Optional[str] = Field(default=None, alias="description")
    start: Optional[str] = Field(default=None, alias="start")
    end: Optional[str] = Field(default=None, alias="end")
    state: Optional[
        Literal[
            "active",
            "payment-failed",
            "payment-pending",
            "queued",
            "queued-deleted",
            "retired",
        ]
    ] = Field(default=None, alias="state")
    region: Optional[str] = Field(default=None, alias="region")
    ec2_instance_family: Optional[str] = Field(default=None, alias="ec2InstanceFamily")
    savings_plan_type: Optional[Literal["Compute", "EC2Instance", "SageMaker"]] = Field(
        default=None, alias="savingsPlanType"
    )
    payment_option: Optional[
        Literal["All Upfront", "No Upfront", "Partial Upfront"]
    ] = Field(default=None, alias="paymentOption")
    product_types: Optional[
        List[Literal["EC2", "Fargate", "Lambda", "SageMaker"]]
    ] = Field(default=None, alias="productTypes")
    currency: Optional[Literal["CNY", "USD"]] = Field(default=None, alias="currency")
    commitment: Optional[str] = Field(default=None, alias="commitment")
    upfront_payment_amount: Optional[str] = Field(
        default=None, alias="upfrontPaymentAmount"
    )
    recurring_payment_amount: Optional[str] = Field(
        default=None, alias="recurringPaymentAmount"
    )
    term_duration_in_seconds: Optional[int] = Field(
        default=None, alias="termDurationInSeconds"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ParentSavingsPlanOfferingModel(BaseModel):
    offering_id: Optional[str] = Field(default=None, alias="offeringId")
    payment_option: Optional[
        Literal["All Upfront", "No Upfront", "Partial Upfront"]
    ] = Field(default=None, alias="paymentOption")
    plan_type: Optional[Literal["Compute", "EC2Instance", "SageMaker"]] = Field(
        default=None, alias="planType"
    )
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")
    currency: Optional[Literal["CNY", "USD"]] = Field(default=None, alias="currency")
    plan_description: Optional[str] = Field(default=None, alias="planDescription")


class SavingsPlanOfferingPropertyModel(BaseModel):
    name: Optional[Literal["instanceFamily", "region"]] = Field(
        default=None, alias="name"
    )
    value: Optional[str] = Field(default=None, alias="value")


class SavingsPlanOfferingRatePropertyModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class SavingsPlanRatePropertyModel(BaseModel):
    name: Optional[
        Literal[
            "instanceFamily", "instanceType", "productDescription", "region", "tenancy"
        ]
    ] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CreateSavingsPlanResponseModel(BaseModel):
    savings_plan_id: str = Field(alias="savingsPlanId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSavingsPlanRatesRequestModel(BaseModel):
    savings_plan_id: str = Field(alias="savingsPlanId")
    filters: Optional[Sequence[SavingsPlanRateFilterModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeSavingsPlansOfferingRatesRequestModel(BaseModel):
    savings_plan_offering_ids: Optional[Sequence[str]] = Field(
        default=None, alias="savingsPlanOfferingIds"
    )
    savings_plan_payment_options: Optional[
        Sequence[Literal["All Upfront", "No Upfront", "Partial Upfront"]]
    ] = Field(default=None, alias="savingsPlanPaymentOptions")
    savings_plan_types: Optional[
        Sequence[Literal["Compute", "EC2Instance", "SageMaker"]]
    ] = Field(default=None, alias="savingsPlanTypes")
    products: Optional[
        Sequence[Literal["EC2", "Fargate", "Lambda", "SageMaker"]]
    ] = Field(default=None, alias="products")
    service_codes: Optional[
        Sequence[
            Literal[
                "AWSLambda", "AmazonEC2", "AmazonECS", "AmazonEKS", "AmazonSageMaker"
            ]
        ]
    ] = Field(default=None, alias="serviceCodes")
    usage_types: Optional[Sequence[str]] = Field(default=None, alias="usageTypes")
    operations: Optional[Sequence[str]] = Field(default=None, alias="operations")
    filters: Optional[Sequence[SavingsPlanOfferingRateFilterElementModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeSavingsPlansOfferingsRequestModel(BaseModel):
    offering_ids: Optional[Sequence[str]] = Field(default=None, alias="offeringIds")
    payment_options: Optional[
        Sequence[Literal["All Upfront", "No Upfront", "Partial Upfront"]]
    ] = Field(default=None, alias="paymentOptions")
    product_type: Optional[Literal["EC2", "Fargate", "Lambda", "SageMaker"]] = Field(
        default=None, alias="productType"
    )
    plan_types: Optional[
        Sequence[Literal["Compute", "EC2Instance", "SageMaker"]]
    ] = Field(default=None, alias="planTypes")
    durations: Optional[Sequence[int]] = Field(default=None, alias="durations")
    currencies: Optional[Sequence[Literal["CNY", "USD"]]] = Field(
        default=None, alias="currencies"
    )
    descriptions: Optional[Sequence[str]] = Field(default=None, alias="descriptions")
    service_codes: Optional[Sequence[str]] = Field(default=None, alias="serviceCodes")
    usage_types: Optional[Sequence[str]] = Field(default=None, alias="usageTypes")
    operations: Optional[Sequence[str]] = Field(default=None, alias="operations")
    filters: Optional[Sequence[SavingsPlanOfferingFilterElementModel]] = Field(
        default=None, alias="filters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class DescribeSavingsPlansRequestModel(BaseModel):
    savings_plan_arns: Optional[Sequence[str]] = Field(
        default=None, alias="savingsPlanArns"
    )
    savings_plan_ids: Optional[Sequence[str]] = Field(
        default=None, alias="savingsPlanIds"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    states: Optional[
        Sequence[
            Literal[
                "active",
                "payment-failed",
                "payment-pending",
                "queued",
                "queued-deleted",
                "retired",
            ]
        ]
    ] = Field(default=None, alias="states")
    filters: Optional[Sequence[SavingsPlanFilterModel]] = Field(
        default=None, alias="filters"
    )


class DescribeSavingsPlansResponseModel(BaseModel):
    savings_plans: List[SavingsPlanModel] = Field(alias="savingsPlans")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SavingsPlanOfferingModel(BaseModel):
    offering_id: Optional[str] = Field(default=None, alias="offeringId")
    product_types: Optional[
        List[Literal["EC2", "Fargate", "Lambda", "SageMaker"]]
    ] = Field(default=None, alias="productTypes")
    plan_type: Optional[Literal["Compute", "EC2Instance", "SageMaker"]] = Field(
        default=None, alias="planType"
    )
    description: Optional[str] = Field(default=None, alias="description")
    payment_option: Optional[
        Literal["All Upfront", "No Upfront", "Partial Upfront"]
    ] = Field(default=None, alias="paymentOption")
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")
    currency: Optional[Literal["CNY", "USD"]] = Field(default=None, alias="currency")
    service_code: Optional[str] = Field(default=None, alias="serviceCode")
    usage_type: Optional[str] = Field(default=None, alias="usageType")
    operation: Optional[str] = Field(default=None, alias="operation")
    properties: Optional[List[SavingsPlanOfferingPropertyModel]] = Field(
        default=None, alias="properties"
    )


class SavingsPlanOfferingRateModel(BaseModel):
    savings_plan_offering: Optional[ParentSavingsPlanOfferingModel] = Field(
        default=None, alias="savingsPlanOffering"
    )
    rate: Optional[str] = Field(default=None, alias="rate")
    unit: Optional[Literal["Hrs", "Lambda-GB-Second", "Request"]] = Field(
        default=None, alias="unit"
    )
    product_type: Optional[Literal["EC2", "Fargate", "Lambda", "SageMaker"]] = Field(
        default=None, alias="productType"
    )
    service_code: Optional[
        Literal["AWSLambda", "AmazonEC2", "AmazonECS", "AmazonEKS", "AmazonSageMaker"]
    ] = Field(default=None, alias="serviceCode")
    usage_type: Optional[str] = Field(default=None, alias="usageType")
    operation: Optional[str] = Field(default=None, alias="operation")
    properties: Optional[List[SavingsPlanOfferingRatePropertyModel]] = Field(
        default=None, alias="properties"
    )


class SavingsPlanRateModel(BaseModel):
    rate: Optional[str] = Field(default=None, alias="rate")
    currency: Optional[Literal["CNY", "USD"]] = Field(default=None, alias="currency")
    unit: Optional[Literal["Hrs", "Lambda-GB-Second", "Request"]] = Field(
        default=None, alias="unit"
    )
    product_type: Optional[Literal["EC2", "Fargate", "Lambda", "SageMaker"]] = Field(
        default=None, alias="productType"
    )
    service_code: Optional[
        Literal["AWSLambda", "AmazonEC2", "AmazonECS", "AmazonEKS", "AmazonSageMaker"]
    ] = Field(default=None, alias="serviceCode")
    usage_type: Optional[str] = Field(default=None, alias="usageType")
    operation: Optional[str] = Field(default=None, alias="operation")
    properties: Optional[List[SavingsPlanRatePropertyModel]] = Field(
        default=None, alias="properties"
    )


class DescribeSavingsPlansOfferingsResponseModel(BaseModel):
    search_results: List[SavingsPlanOfferingModel] = Field(alias="searchResults")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSavingsPlansOfferingRatesResponseModel(BaseModel):
    search_results: List[SavingsPlanOfferingRateModel] = Field(alias="searchResults")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSavingsPlanRatesResponseModel(BaseModel):
    savings_plan_id: str = Field(alias="savingsPlanId")
    search_results: List[SavingsPlanRateModel] = Field(alias="searchResults")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
