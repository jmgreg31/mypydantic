# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class HealthCheckConfigModel(BaseModel):
    type: Literal["HTTP", "HTTPS", "TCP"] = Field(alias="Type")
    resource_path: Optional[str] = Field(default=None, alias="ResourcePath")
    failure_threshold: Optional[int] = Field(default=None, alias="FailureThreshold")


class HealthCheckCustomConfigModel(BaseModel):
    failure_threshold: Optional[int] = Field(default=None, alias="FailureThreshold")


class DeleteNamespaceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteServiceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeregisterInstanceRequestModel(BaseModel):
    service_id: str = Field(alias="ServiceId")
    instance_id: str = Field(alias="InstanceId")


class DiscoverInstancesRequestModel(BaseModel):
    namespace_name: str = Field(alias="NamespaceName")
    service_name: str = Field(alias="ServiceName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    query_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="QueryParameters"
    )
    optional_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="OptionalParameters"
    )
    health_status: Optional[
        Literal["ALL", "HEALTHY", "HEALTHY_OR_ELSE_ALL", "UNHEALTHY"]
    ] = Field(default=None, alias="HealthStatus")


class HttpInstanceSummaryModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    namespace_name: Optional[str] = Field(default=None, alias="NamespaceName")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    health_status: Optional[Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]] = Field(
        default=None, alias="HealthStatus"
    )
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")


class DnsRecordModel(BaseModel):
    type: Literal["A", "AAAA", "CNAME", "SRV"] = Field(alias="Type")
    ttl: int = Field(alias="TTL")


class SOAModel(BaseModel):
    ttl: int = Field(alias="TTL")


class GetInstanceRequestModel(BaseModel):
    service_id: str = Field(alias="ServiceId")
    instance_id: str = Field(alias="InstanceId")


class InstanceModel(BaseModel):
    id: str = Field(alias="Id")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")


class GetInstancesHealthStatusRequestModel(BaseModel):
    service_id: str = Field(alias="ServiceId")
    instances: Optional[Sequence[str]] = Field(default=None, alias="Instances")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetNamespaceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetOperationRequestModel(BaseModel):
    operation_id: str = Field(alias="OperationId")


class OperationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[
        Literal[
            "CREATE_NAMESPACE",
            "DELETE_NAMESPACE",
            "DEREGISTER_INSTANCE",
            "REGISTER_INSTANCE",
            "UPDATE_NAMESPACE",
            "UPDATE_SERVICE",
        ]
    ] = Field(default=None, alias="Type")
    status: Optional[Literal["FAIL", "PENDING", "SUBMITTED", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    update_date: Optional[datetime] = Field(default=None, alias="UpdateDate")
    targets: Optional[Dict[Literal["INSTANCE", "NAMESPACE", "SERVICE"], str]] = Field(
        default=None, alias="Targets"
    )


class GetServiceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class HttpNamespaceChangeModel(BaseModel):
    description: str = Field(alias="Description")


class HttpPropertiesModel(BaseModel):
    http_name: Optional[str] = Field(default=None, alias="HttpName")


class InstanceSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListInstancesRequestModel(BaseModel):
    service_id: str = Field(alias="ServiceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class NamespaceFilterModel(BaseModel):
    name: Literal["HTTP_NAME", "NAME", "TYPE"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")
    condition: Optional[Literal["BEGINS_WITH", "BETWEEN", "EQ", "IN"]] = Field(
        default=None, alias="Condition"
    )


class OperationFilterModel(BaseModel):
    name: Literal[
        "NAMESPACE_ID", "SERVICE_ID", "STATUS", "TYPE", "UPDATE_DATE"
    ] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")
    condition: Optional[Literal["BEGINS_WITH", "BETWEEN", "EQ", "IN"]] = Field(
        default=None, alias="Condition"
    )


class OperationSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    status: Optional[Literal["FAIL", "PENDING", "SUBMITTED", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )


class ServiceFilterModel(BaseModel):
    name: Literal["NAMESPACE_ID"] = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")
    condition: Optional[Literal["BEGINS_WITH", "BETWEEN", "EQ", "IN"]] = Field(
        default=None, alias="Condition"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class SOAChangeModel(BaseModel):
    ttl: int = Field(alias="TTL")


class RegisterInstanceRequestModel(BaseModel):
    service_id: str = Field(alias="ServiceId")
    instance_id: str = Field(alias="InstanceId")
    attributes: Mapping[str, str] = Field(alias="Attributes")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateInstanceCustomHealthStatusRequestModel(BaseModel):
    service_id: str = Field(alias="ServiceId")
    instance_id: str = Field(alias="InstanceId")
    status: Literal["HEALTHY", "UNHEALTHY"] = Field(alias="Status")


class CreateHttpNamespaceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateHttpNamespaceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePrivateDnsNamespaceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePublicDnsNamespaceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNamespaceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterInstanceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstancesHealthStatusResponseModel(BaseModel):
    status: Dict[str, Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]] = Field(
        alias="Status"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterInstanceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateHttpNamespaceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePrivateDnsNamespaceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePublicDnsNamespaceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DiscoverInstancesResponseModel(BaseModel):
    instances: List[HttpInstanceSummaryModel] = Field(alias="Instances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DnsConfigChangeModel(BaseModel):
    dns_records: Sequence[DnsRecordModel] = Field(alias="DnsRecords")


class DnsConfigModel(BaseModel):
    dns_records: Sequence[DnsRecordModel] = Field(alias="DnsRecords")
    namespace_id: Optional[str] = Field(default=None, alias="NamespaceId")
    routing_policy: Optional[Literal["MULTIVALUE", "WEIGHTED"]] = Field(
        default=None, alias="RoutingPolicy"
    )


class DnsPropertiesModel(BaseModel):
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")
    s_oa: Optional[SOAModel] = Field(default=None, alias="SOA")


class PrivateDnsPropertiesMutableModel(BaseModel):
    s_oa: SOAModel = Field(alias="SOA")


class PublicDnsPropertiesMutableModel(BaseModel):
    s_oa: SOAModel = Field(alias="SOA")


class GetInstanceResponseModel(BaseModel):
    instance: InstanceModel = Field(alias="Instance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOperationResponseModel(BaseModel):
    operation: OperationModel = Field(alias="Operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateHttpNamespaceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    namespace: HttpNamespaceChangeModel = Field(alias="Namespace")
    updater_request_id: Optional[str] = Field(default=None, alias="UpdaterRequestId")


class ListInstancesResponseModel(BaseModel):
    instances: List[InstanceSummaryModel] = Field(alias="Instances")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstancesRequestListInstancesPaginateModel(BaseModel):
    service_id: str = Field(alias="ServiceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNamespacesRequestListNamespacesPaginateModel(BaseModel):
    filters: Optional[Sequence[NamespaceFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNamespacesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[NamespaceFilterModel]] = Field(
        default=None, alias="Filters"
    )


class ListOperationsRequestListOperationsPaginateModel(BaseModel):
    filters: Optional[Sequence[OperationFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOperationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[OperationFilterModel]] = Field(
        default=None, alias="Filters"
    )


class ListOperationsResponseModel(BaseModel):
    operations: List[OperationSummaryModel] = Field(alias="Operations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicesRequestListServicesPaginateModel(BaseModel):
    filters: Optional[Sequence[ServiceFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filters: Optional[Sequence[ServiceFilterModel]] = Field(
        default=None, alias="Filters"
    )


class PrivateDnsPropertiesMutableChangeModel(BaseModel):
    s_oa: SOAChangeModel = Field(alias="SOA")


class PublicDnsPropertiesMutableChangeModel(BaseModel):
    s_oa: SOAChangeModel = Field(alias="SOA")


class ServiceChangeModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    dns_config: Optional[DnsConfigChangeModel] = Field(default=None, alias="DnsConfig")
    health_check_config: Optional[HealthCheckConfigModel] = Field(
        default=None, alias="HealthCheckConfig"
    )


class CreateServiceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    namespace_id: Optional[str] = Field(default=None, alias="NamespaceId")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    description: Optional[str] = Field(default=None, alias="Description")
    dns_config: Optional[DnsConfigModel] = Field(default=None, alias="DnsConfig")
    health_check_config: Optional[HealthCheckConfigModel] = Field(
        default=None, alias="HealthCheckConfig"
    )
    health_check_custom_config: Optional[HealthCheckCustomConfigModel] = Field(
        default=None, alias="HealthCheckCustomConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    type: Optional[Literal["HTTP"]] = Field(default=None, alias="Type")


class ServiceSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["DNS", "DNS_HTTP", "HTTP"]] = Field(
        default=None, alias="Type"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    dns_config: Optional[DnsConfigModel] = Field(default=None, alias="DnsConfig")
    health_check_config: Optional[HealthCheckConfigModel] = Field(
        default=None, alias="HealthCheckConfig"
    )
    health_check_custom_config: Optional[HealthCheckCustomConfigModel] = Field(
        default=None, alias="HealthCheckCustomConfig"
    )
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")


class ServiceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    namespace_id: Optional[str] = Field(default=None, alias="NamespaceId")
    description: Optional[str] = Field(default=None, alias="Description")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    dns_config: Optional[DnsConfigModel] = Field(default=None, alias="DnsConfig")
    type: Optional[Literal["DNS", "DNS_HTTP", "HTTP"]] = Field(
        default=None, alias="Type"
    )
    health_check_config: Optional[HealthCheckConfigModel] = Field(
        default=None, alias="HealthCheckConfig"
    )
    health_check_custom_config: Optional[HealthCheckCustomConfigModel] = Field(
        default=None, alias="HealthCheckCustomConfig"
    )
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")


class NamespacePropertiesModel(BaseModel):
    dns_properties: Optional[DnsPropertiesModel] = Field(
        default=None, alias="DnsProperties"
    )
    http_properties: Optional[HttpPropertiesModel] = Field(
        default=None, alias="HttpProperties"
    )


class PrivateDnsNamespacePropertiesModel(BaseModel):
    dns_properties: PrivateDnsPropertiesMutableModel = Field(alias="DnsProperties")


class PublicDnsNamespacePropertiesModel(BaseModel):
    dns_properties: PublicDnsPropertiesMutableModel = Field(alias="DnsProperties")


class PrivateDnsNamespacePropertiesChangeModel(BaseModel):
    dns_properties: PrivateDnsPropertiesMutableChangeModel = Field(
        alias="DnsProperties"
    )


class PublicDnsNamespacePropertiesChangeModel(BaseModel):
    dns_properties: PublicDnsPropertiesMutableChangeModel = Field(alias="DnsProperties")


class UpdateServiceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    service: ServiceChangeModel = Field(alias="Service")


class ListServicesResponseModel(BaseModel):
    services: List[ServiceSummaryModel] = Field(alias="Services")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NamespaceSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["DNS_PRIVATE", "DNS_PUBLIC", "HTTP"]] = Field(
        default=None, alias="Type"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    service_count: Optional[int] = Field(default=None, alias="ServiceCount")
    properties: Optional[NamespacePropertiesModel] = Field(
        default=None, alias="Properties"
    )
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")


class NamespaceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["DNS_PRIVATE", "DNS_PUBLIC", "HTTP"]] = Field(
        default=None, alias="Type"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    service_count: Optional[int] = Field(default=None, alias="ServiceCount")
    properties: Optional[NamespacePropertiesModel] = Field(
        default=None, alias="Properties"
    )
    create_date: Optional[datetime] = Field(default=None, alias="CreateDate")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")


class CreatePrivateDnsNamespaceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    vpc: str = Field(alias="Vpc")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    properties: Optional[PrivateDnsNamespacePropertiesModel] = Field(
        default=None, alias="Properties"
    )


class CreatePublicDnsNamespaceRequestModel(BaseModel):
    name: str = Field(alias="Name")
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    properties: Optional[PublicDnsNamespacePropertiesModel] = Field(
        default=None, alias="Properties"
    )


class PrivateDnsNamespaceChangeModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    properties: Optional[PrivateDnsNamespacePropertiesChangeModel] = Field(
        default=None, alias="Properties"
    )


class PublicDnsNamespaceChangeModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    properties: Optional[PublicDnsNamespacePropertiesChangeModel] = Field(
        default=None, alias="Properties"
    )


class ListNamespacesResponseModel(BaseModel):
    namespaces: List[NamespaceSummaryModel] = Field(alias="Namespaces")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNamespaceResponseModel(BaseModel):
    namespace: NamespaceModel = Field(alias="Namespace")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePrivateDnsNamespaceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    namespace: PrivateDnsNamespaceChangeModel = Field(alias="Namespace")
    updater_request_id: Optional[str] = Field(default=None, alias="UpdaterRequestId")


class UpdatePublicDnsNamespaceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    namespace: PublicDnsNamespaceChangeModel = Field(alias="Namespace")
    updater_request_id: Optional[str] = Field(default=None, alias="UpdaterRequestId")
