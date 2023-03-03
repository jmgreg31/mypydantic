# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, Literal, Mapping, Optional, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class GenerateDataSetRequestModel(BaseModel):
    data_set_type: Literal[
        "customer_profile_by_geography",
        "customer_profile_by_industry",
        "customer_profile_by_revenue",
        "customer_subscriber_annual_subscriptions",
        "customer_subscriber_hourly_monthly_subscriptions",
        "daily_business_canceled_product_subscribers",
        "daily_business_fees",
        "daily_business_free_trial_conversions",
        "daily_business_new_instances",
        "daily_business_new_product_subscribers",
        "daily_business_usage_by_instance_type",
        "disbursed_amount_by_age_of_disbursed_funds",
        "disbursed_amount_by_age_of_past_due_funds",
        "disbursed_amount_by_age_of_uncollected_funds",
        "disbursed_amount_by_customer_geo",
        "disbursed_amount_by_instance_hours",
        "disbursed_amount_by_product",
        "disbursed_amount_by_product_with_uncollected_funds",
        "disbursed_amount_by_uncollected_funds_breakdown",
        "monthly_revenue_annual_subscriptions",
        "monthly_revenue_billing_and_revenue_data",
        "monthly_revenue_field_demonstration_usage",
        "monthly_revenue_flexible_payment_schedule",
        "sales_compensation_billed_revenue",
        "us_sales_and_use_tax_records",
    ] = Field(alias="dataSetType")
    data_set_publication_date: Union[datetime, str] = Field(
        alias="dataSetPublicationDate"
    )
    role_name_arn: str = Field(alias="roleNameArn")
    destination_s3_bucket_name: str = Field(alias="destinationS3BucketName")
    sns_topic_arn: str = Field(alias="snsTopicArn")
    destination_s3_prefix: Optional[str] = Field(
        default=None, alias="destinationS3Prefix"
    )
    customer_defined_values: Optional[Mapping[str, str]] = Field(
        default=None, alias="customerDefinedValues"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class StartSupportDataExportRequestModel(BaseModel):
    data_set_type: Literal[
        "customer_support_contacts_data", "test_customer_support_contacts_data"
    ] = Field(alias="dataSetType")
    from_date: Union[datetime, str] = Field(alias="fromDate")
    role_name_arn: str = Field(alias="roleNameArn")
    destination_s3_bucket_name: str = Field(alias="destinationS3BucketName")
    sns_topic_arn: str = Field(alias="snsTopicArn")
    destination_s3_prefix: Optional[str] = Field(
        default=None, alias="destinationS3Prefix"
    )
    customer_defined_values: Optional[Mapping[str, str]] = Field(
        default=None, alias="customerDefinedValues"
    )


class GenerateDataSetResultModel(BaseModel):
    data_set_request_id: str = Field(alias="dataSetRequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSupportDataExportResultModel(BaseModel):
    data_set_request_id: str = Field(alias="dataSetRequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
