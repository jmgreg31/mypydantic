# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ContainerModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    arn: Optional[str] = Field(default=None, alias="ARN")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="Status"
    )
    access_logging_enabled: Optional[bool] = Field(
        default=None, alias="AccessLoggingEnabled"
    )


class CorsRuleModel(BaseModel):
    allowed_origins: List[str] = Field(alias="AllowedOrigins")
    allowed_headers: List[str] = Field(alias="AllowedHeaders")
    allowed_methods: Optional[List[Literal["DELETE", "GET", "HEAD", "PUT"]]] = Field(
        default=None, alias="AllowedMethods"
    )
    max_age_seconds: Optional[int] = Field(default=None, alias="MaxAgeSeconds")
    expose_headers: Optional[List[str]] = Field(default=None, alias="ExposeHeaders")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteContainerInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class DeleteContainerPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class DeleteCorsPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class DeleteLifecyclePolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class DeleteMetricPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class DescribeContainerInputRequestModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="ContainerName")


class GetContainerPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class GetCorsPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class GetLifecyclePolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class GetMetricPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListContainersInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource: str = Field(alias="Resource")


class MetricPolicyRuleModel(BaseModel):
    object_group: str = Field(alias="ObjectGroup")
    object_group_name: str = Field(alias="ObjectGroupName")


class PutContainerPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")
    policy: str = Field(alias="Policy")


class PutLifecyclePolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")
    lifecycle_policy: str = Field(alias="LifecyclePolicy")


class StartAccessLoggingInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class StopAccessLoggingInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")


class UntagResourceInputRequestModel(BaseModel):
    resource: str = Field(alias="Resource")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class PutCorsPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")
    cors_policy: Sequence[CorsRuleModel] = Field(alias="CorsPolicy")


class CreateContainerInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceInputRequestModel(BaseModel):
    resource: str = Field(alias="Resource")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateContainerOutputModel(BaseModel):
    container: ContainerModel = Field(alias="Container")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeContainerOutputModel(BaseModel):
    container: ContainerModel = Field(alias="Container")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContainerPolicyOutputModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCorsPolicyOutputModel(BaseModel):
    cors_policy: List[CorsRuleModel] = Field(alias="CorsPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLifecyclePolicyOutputModel(BaseModel):
    lifecycle_policy: str = Field(alias="LifecyclePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContainersOutputModel(BaseModel):
    containers: List[ContainerModel] = Field(alias="Containers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListContainersInputListContainersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class MetricPolicyModel(BaseModel):
    container_level_metrics: Literal["DISABLED", "ENABLED"] = Field(
        alias="ContainerLevelMetrics"
    )
    metric_policy_rules: Optional[List[MetricPolicyRuleModel]] = Field(
        default=None, alias="MetricPolicyRules"
    )


class GetMetricPolicyOutputModel(BaseModel):
    metric_policy: MetricPolicyModel = Field(alias="MetricPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutMetricPolicyInputRequestModel(BaseModel):
    container_name: str = Field(alias="ContainerName")
    metric_policy: MetricPolicyModel = Field(alias="MetricPolicy")
