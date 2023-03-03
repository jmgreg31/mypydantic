# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ComplianceDetailsModel(BaseModel):
    noncompliant_keys: Optional[List[str]] = Field(
        default=None, alias="NoncompliantKeys"
    )
    keys_with_noncompliant_values: Optional[List[str]] = Field(
        default=None, alias="KeysWithNoncompliantValues"
    )
    compliance_status: Optional[bool] = Field(default=None, alias="ComplianceStatus")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FailureInfoModel(BaseModel):
    status_code: Optional[int] = Field(default=None, alias="StatusCode")
    error_code: Optional[
        Literal["InternalServiceException", "InvalidParameterException"]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetComplianceSummaryInputRequestModel(BaseModel):
    target_id_filters: Optional[Sequence[str]] = Field(
        default=None, alias="TargetIdFilters"
    )
    region_filters: Optional[Sequence[str]] = Field(default=None, alias="RegionFilters")
    resource_type_filters: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceTypeFilters"
    )
    tag_key_filters: Optional[Sequence[str]] = Field(
        default=None, alias="TagKeyFilters"
    )
    group_by: Optional[
        Sequence[Literal["REGION", "RESOURCE_TYPE", "TARGET_ID"]]
    ] = Field(default=None, alias="GroupBy")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")


class SummaryModel(BaseModel):
    last_updated: Optional[str] = Field(default=None, alias="LastUpdated")
    target_id: Optional[str] = Field(default=None, alias="TargetId")
    target_id_type: Optional[Literal["ACCOUNT", "OU", "ROOT"]] = Field(
        default=None, alias="TargetIdType"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    non_compliant_resources: Optional[int] = Field(
        default=None, alias="NonCompliantResources"
    )


class TagFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class GetTagKeysInputRequestModel(BaseModel):
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")


class GetTagValuesInputRequestModel(BaseModel):
    key: str = Field(alias="Key")
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class StartReportCreationInputRequestModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")


class TagResourcesInputRequestModel(BaseModel):
    resource_arnlist: Sequence[str] = Field(alias="ResourceARNList")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourcesInputRequestModel(BaseModel):
    resource_arnlist: Sequence[str] = Field(alias="ResourceARNList")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class DescribeReportCreationOutputModel(BaseModel):
    status: str = Field(alias="Status")
    s3_location: str = Field(alias="S3Location")
    error_message: str = Field(alias="ErrorMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTagKeysOutputModel(BaseModel):
    pagination_token: str = Field(alias="PaginationToken")
    tag_keys: List[str] = Field(alias="TagKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTagValuesOutputModel(BaseModel):
    pagination_token: str = Field(alias="PaginationToken")
    tag_values: List[str] = Field(alias="TagValues")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourcesOutputModel(BaseModel):
    failed_resources_map: Dict[str, FailureInfoModel] = Field(
        alias="FailedResourcesMap"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UntagResourcesOutputModel(BaseModel):
    failed_resources_map: Dict[str, FailureInfoModel] = Field(
        alias="FailedResourcesMap"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComplianceSummaryInputGetComplianceSummaryPaginateModel(BaseModel):
    target_id_filters: Optional[Sequence[str]] = Field(
        default=None, alias="TargetIdFilters"
    )
    region_filters: Optional[Sequence[str]] = Field(default=None, alias="RegionFilters")
    resource_type_filters: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceTypeFilters"
    )
    tag_key_filters: Optional[Sequence[str]] = Field(
        default=None, alias="TagKeyFilters"
    )
    group_by: Optional[
        Sequence[Literal["REGION", "RESOURCE_TYPE", "TARGET_ID"]]
    ] = Field(default=None, alias="GroupBy")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTagKeysInputGetTagKeysPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTagValuesInputGetTagValuesPaginateModel(BaseModel):
    key: str = Field(alias="Key")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetComplianceSummaryOutputModel(BaseModel):
    summary_list: List[SummaryModel] = Field(alias="SummaryList")
    pagination_token: str = Field(alias="PaginationToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcesInputGetResourcesPaginateModel(BaseModel):
    tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="TagFilters"
    )
    tags_per_page: Optional[int] = Field(default=None, alias="TagsPerPage")
    resource_type_filters: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceTypeFilters"
    )
    include_compliance_details: Optional[bool] = Field(
        default=None, alias="IncludeComplianceDetails"
    )
    exclude_compliant_resources: Optional[bool] = Field(
        default=None, alias="ExcludeCompliantResources"
    )
    resource_arnlist: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceARNList"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourcesInputRequestModel(BaseModel):
    pagination_token: Optional[str] = Field(default=None, alias="PaginationToken")
    tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="TagFilters"
    )
    resources_per_page: Optional[int] = Field(default=None, alias="ResourcesPerPage")
    tags_per_page: Optional[int] = Field(default=None, alias="TagsPerPage")
    resource_type_filters: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceTypeFilters"
    )
    include_compliance_details: Optional[bool] = Field(
        default=None, alias="IncludeComplianceDetails"
    )
    exclude_compliant_resources: Optional[bool] = Field(
        default=None, alias="ExcludeCompliantResources"
    )
    resource_arnlist: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceARNList"
    )


class ResourceTagMappingModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    compliance_details: Optional[ComplianceDetailsModel] = Field(
        default=None, alias="ComplianceDetails"
    )


class GetResourcesOutputModel(BaseModel):
    pagination_token: str = Field(alias="PaginationToken")
    resource_tag_mapping_list: List[ResourceTagMappingModel] = Field(
        alias="ResourceTagMappingList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
