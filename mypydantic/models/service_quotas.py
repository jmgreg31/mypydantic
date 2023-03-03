# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class DeleteServiceQuotaIncreaseRequestFromTemplateRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    quota_code: str = Field(alias="QuotaCode")
    aws_region: str = Field(alias="AwsRegion")


class ErrorReasonModel(BaseModel):
    error_code: Optional[
        Literal[
            "DEPENDENCY_ACCESS_DENIED_ERROR",
            "DEPENDENCY_SERVICE_ERROR",
            "DEPENDENCY_THROTTLING_ERROR",
            "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class GetAWSDefaultServiceQuotaRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    quota_code: str = Field(alias="QuotaCode")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetRequestedServiceQuotaChangeRequestModel(BaseModel):
    request_id: str = Field(alias="RequestId")


class RequestedServiceQuotaChangeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    case_id: Optional[str] = Field(default=None, alias="CaseId")
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    quota_code: Optional[str] = Field(default=None, alias="QuotaCode")
    quota_name: Optional[str] = Field(default=None, alias="QuotaName")
    desired_value: Optional[float] = Field(default=None, alias="DesiredValue")
    status: Optional[
        Literal["APPROVED", "CASE_CLOSED", "CASE_OPENED", "DENIED", "PENDING"]
    ] = Field(default=None, alias="Status")
    created: Optional[datetime] = Field(default=None, alias="Created")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    requester: Optional[str] = Field(default=None, alias="Requester")
    quota_arn: Optional[str] = Field(default=None, alias="QuotaArn")
    global_quota: Optional[bool] = Field(default=None, alias="GlobalQuota")
    unit: Optional[str] = Field(default=None, alias="Unit")


class GetServiceQuotaIncreaseRequestFromTemplateRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    quota_code: str = Field(alias="QuotaCode")
    aws_region: str = Field(alias="AwsRegion")


class ServiceQuotaIncreaseRequestInTemplateModel(BaseModel):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    quota_code: Optional[str] = Field(default=None, alias="QuotaCode")
    quota_name: Optional[str] = Field(default=None, alias="QuotaName")
    desired_value: Optional[float] = Field(default=None, alias="DesiredValue")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    unit: Optional[str] = Field(default=None, alias="Unit")
    global_quota: Optional[bool] = Field(default=None, alias="GlobalQuota")


class GetServiceQuotaRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    quota_code: str = Field(alias="QuotaCode")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAWSDefaultServiceQuotasRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRequestedServiceQuotaChangeHistoryByQuotaRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    quota_code: str = Field(alias="QuotaCode")
    status: Optional[
        Literal["APPROVED", "CASE_CLOSED", "CASE_OPENED", "DENIED", "PENDING"]
    ] = Field(default=None, alias="Status")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRequestedServiceQuotaChangeHistoryRequestModel(BaseModel):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    status: Optional[
        Literal["APPROVED", "CASE_CLOSED", "CASE_OPENED", "DENIED", "PENDING"]
    ] = Field(default=None, alias="Status")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListServiceQuotaIncreaseRequestsInTemplateRequestModel(BaseModel):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListServiceQuotasRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListServicesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ServiceInfoModel(BaseModel):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class MetricInfoModel(BaseModel):
    metric_namespace: Optional[str] = Field(default=None, alias="MetricNamespace")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    metric_dimensions: Optional[Dict[str, str]] = Field(
        default=None, alias="MetricDimensions"
    )
    metric_statistic_recommendation: Optional[str] = Field(
        default=None, alias="MetricStatisticRecommendation"
    )


class PutServiceQuotaIncreaseRequestIntoTemplateRequestModel(BaseModel):
    quota_code: str = Field(alias="QuotaCode")
    service_code: str = Field(alias="ServiceCode")
    aws_region: str = Field(alias="AwsRegion")
    desired_value: float = Field(alias="DesiredValue")


class QuotaPeriodModel(BaseModel):
    period_value: Optional[int] = Field(default=None, alias="PeriodValue")
    period_unit: Optional[
        Literal["DAY", "HOUR", "MICROSECOND", "MILLISECOND", "MINUTE", "SECOND", "WEEK"]
    ] = Field(default=None, alias="PeriodUnit")


class RequestServiceQuotaIncreaseRequestModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    quota_code: str = Field(alias="QuotaCode")
    desired_value: float = Field(alias="DesiredValue")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class GetAssociationForServiceQuotaTemplateResponseModel(BaseModel):
    service_quota_template_association_status: Literal[
        "ASSOCIATED", "DISASSOCIATED"
    ] = Field(alias="ServiceQuotaTemplateAssociationStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRequestedServiceQuotaChangeResponseModel(BaseModel):
    requested_quota: RequestedServiceQuotaChangeModel = Field(alias="RequestedQuota")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRequestedServiceQuotaChangeHistoryByQuotaResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    requested_quotas: List[RequestedServiceQuotaChangeModel] = Field(
        alias="RequestedQuotas"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRequestedServiceQuotaChangeHistoryResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    requested_quotas: List[RequestedServiceQuotaChangeModel] = Field(
        alias="RequestedQuotas"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestServiceQuotaIncreaseResponseModel(BaseModel):
    requested_quota: RequestedServiceQuotaChangeModel = Field(alias="RequestedQuota")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceQuotaIncreaseRequestFromTemplateResponseModel(BaseModel):
    service_quota_increase_request_in_template: ServiceQuotaIncreaseRequestInTemplateModel = Field(
        alias="ServiceQuotaIncreaseRequestInTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceQuotaIncreaseRequestsInTemplateResponseModel(BaseModel):
    service_quota_increase_request_in_template_list: List[
        ServiceQuotaIncreaseRequestInTemplateModel
    ] = Field(alias="ServiceQuotaIncreaseRequestInTemplateList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutServiceQuotaIncreaseRequestIntoTemplateResponseModel(BaseModel):
    service_quota_increase_request_in_template: ServiceQuotaIncreaseRequestInTemplateModel = Field(
        alias="ServiceQuotaIncreaseRequestInTemplate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAWSDefaultServiceQuotasRequestListAWSDefaultServiceQuotasPaginateModel(
    BaseModel
):
    service_code: str = Field(alias="ServiceCode")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRequestedServiceQuotaChangeHistoryByQuotaRequestListRequestedServiceQuotaChangeHistoryByQuotaPaginateModel(
    BaseModel
):
    service_code: str = Field(alias="ServiceCode")
    quota_code: str = Field(alias="QuotaCode")
    status: Optional[
        Literal["APPROVED", "CASE_CLOSED", "CASE_OPENED", "DENIED", "PENDING"]
    ] = Field(default=None, alias="Status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRequestedServiceQuotaChangeHistoryRequestListRequestedServiceQuotaChangeHistoryPaginateModel(
    BaseModel
):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    status: Optional[
        Literal["APPROVED", "CASE_CLOSED", "CASE_OPENED", "DENIED", "PENDING"]
    ] = Field(default=None, alias="Status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceQuotaIncreaseRequestsInTemplateRequestListServiceQuotaIncreaseRequestsInTemplatePaginateModel(
    BaseModel
):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServiceQuotasRequestListServiceQuotasPaginateModel(BaseModel):
    service_code: str = Field(alias="ServiceCode")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicesRequestListServicesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    services: List[ServiceInfoModel] = Field(alias="Services")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ServiceQuotaModel(BaseModel):
    service_code: Optional[str] = Field(default=None, alias="ServiceCode")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    quota_arn: Optional[str] = Field(default=None, alias="QuotaArn")
    quota_code: Optional[str] = Field(default=None, alias="QuotaCode")
    quota_name: Optional[str] = Field(default=None, alias="QuotaName")
    value: Optional[float] = Field(default=None, alias="Value")
    unit: Optional[str] = Field(default=None, alias="Unit")
    adjustable: Optional[bool] = Field(default=None, alias="Adjustable")
    global_quota: Optional[bool] = Field(default=None, alias="GlobalQuota")
    usage_metric: Optional[MetricInfoModel] = Field(default=None, alias="UsageMetric")
    period: Optional[QuotaPeriodModel] = Field(default=None, alias="Period")
    error_reason: Optional[ErrorReasonModel] = Field(default=None, alias="ErrorReason")


class GetAWSDefaultServiceQuotaResponseModel(BaseModel):
    quota: ServiceQuotaModel = Field(alias="Quota")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceQuotaResponseModel(BaseModel):
    quota: ServiceQuotaModel = Field(alias="Quota")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAWSDefaultServiceQuotasResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    quotas: List[ServiceQuotaModel] = Field(alias="Quotas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServiceQuotasResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    quotas: List[ServiceQuotaModel] = Field(alias="Quotas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
