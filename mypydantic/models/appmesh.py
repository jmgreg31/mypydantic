# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AwsCloudMapInstanceAttributeModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class ListenerTlsFileCertificateModel(BaseModel):
    certificate_chain: str = Field(alias="certificateChain")
    private_key: str = Field(alias="privateKey")


class ListenerTlsSdsCertificateModel(BaseModel):
    secret_name: str = Field(alias="secretName")


class TagRefModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteGatewayRouteInputRequestModel(BaseModel):
    gateway_route_name: str = Field(alias="gatewayRouteName")
    mesh_name: str = Field(alias="meshName")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DeleteMeshInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")


class DeleteRouteInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    route_name: str = Field(alias="routeName")
    virtual_router_name: str = Field(alias="virtualRouterName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DeleteVirtualGatewayInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DeleteVirtualNodeInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_node_name: str = Field(alias="virtualNodeName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DeleteVirtualRouterInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_router_name: str = Field(alias="virtualRouterName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DeleteVirtualServiceInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_service_name: str = Field(alias="virtualServiceName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DescribeGatewayRouteInputRequestModel(BaseModel):
    gateway_route_name: str = Field(alias="gatewayRouteName")
    mesh_name: str = Field(alias="meshName")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DescribeMeshInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DescribeRouteInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    route_name: str = Field(alias="routeName")
    virtual_router_name: str = Field(alias="virtualRouterName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DescribeVirtualGatewayInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DescribeVirtualNodeInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_node_name: str = Field(alias="virtualNodeName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DescribeVirtualRouterInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_router_name: str = Field(alias="virtualRouterName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DescribeVirtualServiceInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_service_name: str = Field(alias="virtualServiceName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class DnsServiceDiscoveryModel(BaseModel):
    hostname: str = Field(alias="hostname")
    ip_preference: Optional[
        Literal["IPv4_ONLY", "IPv4_PREFERRED", "IPv6_ONLY", "IPv6_PREFERRED"]
    ] = Field(default=None, alias="ipPreference")
    response_type: Optional[Literal["ENDPOINTS", "LOADBALANCER"]] = Field(
        default=None, alias="responseType"
    )


class DurationModel(BaseModel):
    unit: Optional[Literal["ms", "s"]] = Field(default=None, alias="unit")
    value: Optional[int] = Field(default=None, alias="value")


class EgressFilterModel(BaseModel):
    type: Literal["ALLOW_ALL", "DROP_ALL"] = Field(alias="type")


class GatewayRouteStatusModel(BaseModel):
    status: Literal["ACTIVE", "DELETED", "INACTIVE"] = Field(alias="status")


class ResourceMetadataModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    uid: str = Field(alias="uid")
    version: int = Field(alias="version")


class GatewayRouteHostnameMatchModel(BaseModel):
    exact: Optional[str] = Field(default=None, alias="exact")
    suffix: Optional[str] = Field(default=None, alias="suffix")


class GatewayRouteHostnameRewriteModel(BaseModel):
    default_target_hostname: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="defaultTargetHostname"
    )


class GatewayRouteRefModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    gateway_route_name: str = Field(alias="gatewayRouteName")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_name: str = Field(alias="meshName")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    version: int = Field(alias="version")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")


class GatewayRouteVirtualServiceModel(BaseModel):
    virtual_service_name: str = Field(alias="virtualServiceName")


class MatchRangeModel(BaseModel):
    end: int = Field(alias="end")
    start: int = Field(alias="start")


class WeightedTargetModel(BaseModel):
    virtual_node: str = Field(alias="virtualNode")
    weight: int = Field(alias="weight")
    port: Optional[int] = Field(default=None, alias="port")


class HealthCheckPolicyModel(BaseModel):
    healthy_threshold: int = Field(alias="healthyThreshold")
    interval_millis: int = Field(alias="intervalMillis")
    protocol: Literal["grpc", "http", "http2", "tcp"] = Field(alias="protocol")
    timeout_millis: int = Field(alias="timeoutMillis")
    unhealthy_threshold: int = Field(alias="unhealthyThreshold")
    path: Optional[str] = Field(default=None, alias="path")
    port: Optional[int] = Field(default=None, alias="port")


class HttpPathMatchModel(BaseModel):
    exact: Optional[str] = Field(default=None, alias="exact")
    regex: Optional[str] = Field(default=None, alias="regex")


class HttpGatewayRoutePathRewriteModel(BaseModel):
    exact: Optional[str] = Field(default=None, alias="exact")


class HttpGatewayRoutePrefixRewriteModel(BaseModel):
    default_prefix: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="defaultPrefix"
    )
    value: Optional[str] = Field(default=None, alias="value")


class QueryParameterMatchModel(BaseModel):
    exact: Optional[str] = Field(default=None, alias="exact")


class JsonFormatRefModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListGatewayRoutesInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    limit: Optional[int] = Field(default=None, alias="limit")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListMeshesInputRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="limit")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class MeshRefModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_name: str = Field(alias="meshName")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    version: int = Field(alias="version")


class ListRoutesInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_router_name: str = Field(alias="virtualRouterName")
    limit: Optional[int] = Field(default=None, alias="limit")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RouteRefModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_name: str = Field(alias="meshName")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    route_name: str = Field(alias="routeName")
    version: int = Field(alias="version")
    virtual_router_name: str = Field(alias="virtualRouterName")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    limit: Optional[int] = Field(default=None, alias="limit")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListVirtualGatewaysInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    limit: Optional[int] = Field(default=None, alias="limit")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class VirtualGatewayRefModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_name: str = Field(alias="meshName")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    version: int = Field(alias="version")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")


class ListVirtualNodesInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    limit: Optional[int] = Field(default=None, alias="limit")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class VirtualNodeRefModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_name: str = Field(alias="meshName")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    version: int = Field(alias="version")
    virtual_node_name: str = Field(alias="virtualNodeName")


class ListVirtualRoutersInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    limit: Optional[int] = Field(default=None, alias="limit")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class VirtualRouterRefModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_name: str = Field(alias="meshName")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    version: int = Field(alias="version")
    virtual_router_name: str = Field(alias="virtualRouterName")


class ListVirtualServicesInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    limit: Optional[int] = Field(default=None, alias="limit")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class VirtualServiceRefModel(BaseModel):
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    mesh_name: str = Field(alias="meshName")
    mesh_owner: str = Field(alias="meshOwner")
    resource_owner: str = Field(alias="resourceOwner")
    version: int = Field(alias="version")
    virtual_service_name: str = Field(alias="virtualServiceName")


class ListenerTlsAcmCertificateModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")


class TlsValidationContextFileTrustModel(BaseModel):
    certificate_chain: str = Field(alias="certificateChain")


class TlsValidationContextSdsTrustModel(BaseModel):
    secret_name: str = Field(alias="secretName")


class PortMappingModel(BaseModel):
    port: int = Field(alias="port")
    protocol: Literal["grpc", "http", "http2", "tcp"] = Field(alias="protocol")


class MeshStatusModel(BaseModel):
    status: Optional[Literal["ACTIVE", "DELETED", "INACTIVE"]] = Field(
        default=None, alias="status"
    )


class MeshServiceDiscoveryModel(BaseModel):
    ip_preference: Optional[
        Literal["IPv4_ONLY", "IPv4_PREFERRED", "IPv6_ONLY", "IPv6_PREFERRED"]
    ] = Field(default=None, alias="ipPreference")


class RouteStatusModel(BaseModel):
    status: Literal["ACTIVE", "DELETED", "INACTIVE"] = Field(alias="status")


class SubjectAlternativeNameMatchersModel(BaseModel):
    exact: Sequence[str] = Field(alias="exact")


class TcpRouteMatchModel(BaseModel):
    port: Optional[int] = Field(default=None, alias="port")


class TlsValidationContextAcmTrustModel(BaseModel):
    certificate_authority_arns: Sequence[str] = Field(alias="certificateAuthorityArns")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class VirtualGatewayListenerTlsFileCertificateModel(BaseModel):
    certificate_chain: str = Field(alias="certificateChain")
    private_key: str = Field(alias="privateKey")


class VirtualGatewayListenerTlsSdsCertificateModel(BaseModel):
    secret_name: str = Field(alias="secretName")


class VirtualGatewayGrpcConnectionPoolModel(BaseModel):
    max_requests: int = Field(alias="maxRequests")


class VirtualGatewayHttp2ConnectionPoolModel(BaseModel):
    max_requests: int = Field(alias="maxRequests")


class VirtualGatewayHttpConnectionPoolModel(BaseModel):
    max_connections: int = Field(alias="maxConnections")
    max_pending_requests: Optional[int] = Field(
        default=None, alias="maxPendingRequests"
    )


class VirtualGatewayStatusModel(BaseModel):
    status: Literal["ACTIVE", "DELETED", "INACTIVE"] = Field(alias="status")


class VirtualGatewayHealthCheckPolicyModel(BaseModel):
    healthy_threshold: int = Field(alias="healthyThreshold")
    interval_millis: int = Field(alias="intervalMillis")
    protocol: Literal["grpc", "http", "http2"] = Field(alias="protocol")
    timeout_millis: int = Field(alias="timeoutMillis")
    unhealthy_threshold: int = Field(alias="unhealthyThreshold")
    path: Optional[str] = Field(default=None, alias="path")
    port: Optional[int] = Field(default=None, alias="port")


class VirtualGatewayListenerTlsAcmCertificateModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")


class VirtualGatewayTlsValidationContextFileTrustModel(BaseModel):
    certificate_chain: str = Field(alias="certificateChain")


class VirtualGatewayTlsValidationContextSdsTrustModel(BaseModel):
    secret_name: str = Field(alias="secretName")


class VirtualGatewayPortMappingModel(BaseModel):
    port: int = Field(alias="port")
    protocol: Literal["grpc", "http", "http2"] = Field(alias="protocol")


class VirtualGatewayTlsValidationContextAcmTrustModel(BaseModel):
    certificate_authority_arns: Sequence[str] = Field(alias="certificateAuthorityArns")


class VirtualNodeGrpcConnectionPoolModel(BaseModel):
    max_requests: int = Field(alias="maxRequests")


class VirtualNodeHttp2ConnectionPoolModel(BaseModel):
    max_requests: int = Field(alias="maxRequests")


class VirtualNodeHttpConnectionPoolModel(BaseModel):
    max_connections: int = Field(alias="maxConnections")
    max_pending_requests: Optional[int] = Field(
        default=None, alias="maxPendingRequests"
    )


class VirtualNodeTcpConnectionPoolModel(BaseModel):
    max_connections: int = Field(alias="maxConnections")


class VirtualNodeStatusModel(BaseModel):
    status: Literal["ACTIVE", "DELETED", "INACTIVE"] = Field(alias="status")


class VirtualNodeServiceProviderModel(BaseModel):
    virtual_node_name: str = Field(alias="virtualNodeName")


class VirtualRouterStatusModel(BaseModel):
    status: Literal["ACTIVE", "DELETED", "INACTIVE"] = Field(alias="status")


class VirtualRouterServiceProviderModel(BaseModel):
    virtual_router_name: str = Field(alias="virtualRouterName")


class VirtualServiceStatusModel(BaseModel):
    status: Literal["ACTIVE", "DELETED", "INACTIVE"] = Field(alias="status")


class AwsCloudMapServiceDiscoveryModel(BaseModel):
    namespace_name: str = Field(alias="namespaceName")
    service_name: str = Field(alias="serviceName")
    attributes: Optional[Sequence[AwsCloudMapInstanceAttributeModel]] = Field(
        default=None, alias="attributes"
    )
    ip_preference: Optional[
        Literal["IPv4_ONLY", "IPv4_PREFERRED", "IPv6_ONLY", "IPv6_PREFERRED"]
    ] = Field(default=None, alias="ipPreference")


class ClientTlsCertificateModel(BaseModel):
    file: Optional[ListenerTlsFileCertificateModel] = Field(default=None, alias="file")
    sds: Optional[ListenerTlsSdsCertificateModel] = Field(default=None, alias="sds")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagRefModel] = Field(alias="tags")


class ListTagsForResourceOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    tags: List[TagRefModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GrpcRetryPolicyModel(BaseModel):
    max_retries: int = Field(alias="maxRetries")
    per_retry_timeout: DurationModel = Field(alias="perRetryTimeout")
    grpc_retry_events: Optional[
        Sequence[
            Literal[
                "cancelled",
                "deadline-exceeded",
                "internal",
                "resource-exhausted",
                "unavailable",
            ]
        ]
    ] = Field(default=None, alias="grpcRetryEvents")
    http_retry_events: Optional[Sequence[str]] = Field(
        default=None, alias="httpRetryEvents"
    )
    tcp_retry_events: Optional[Sequence[Literal["connection-error"]]] = Field(
        default=None, alias="tcpRetryEvents"
    )


class GrpcTimeoutModel(BaseModel):
    idle: Optional[DurationModel] = Field(default=None, alias="idle")
    per_request: Optional[DurationModel] = Field(default=None, alias="perRequest")


class HttpRetryPolicyModel(BaseModel):
    max_retries: int = Field(alias="maxRetries")
    per_retry_timeout: DurationModel = Field(alias="perRetryTimeout")
    http_retry_events: Optional[Sequence[str]] = Field(
        default=None, alias="httpRetryEvents"
    )
    tcp_retry_events: Optional[Sequence[Literal["connection-error"]]] = Field(
        default=None, alias="tcpRetryEvents"
    )


class HttpTimeoutModel(BaseModel):
    idle: Optional[DurationModel] = Field(default=None, alias="idle")
    per_request: Optional[DurationModel] = Field(default=None, alias="perRequest")


class OutlierDetectionModel(BaseModel):
    base_ejection_duration: DurationModel = Field(alias="baseEjectionDuration")
    interval: DurationModel = Field(alias="interval")
    max_ejection_percent: int = Field(alias="maxEjectionPercent")
    max_server_errors: int = Field(alias="maxServerErrors")


class TcpTimeoutModel(BaseModel):
    idle: Optional[DurationModel] = Field(default=None, alias="idle")


class GrpcGatewayRouteRewriteModel(BaseModel):
    hostname: Optional[GatewayRouteHostnameRewriteModel] = Field(
        default=None, alias="hostname"
    )


class ListGatewayRoutesOutputModel(BaseModel):
    gateway_routes: List[GatewayRouteRefModel] = Field(alias="gatewayRoutes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GatewayRouteTargetModel(BaseModel):
    virtual_service: GatewayRouteVirtualServiceModel = Field(alias="virtualService")
    port: Optional[int] = Field(default=None, alias="port")


class GrpcMetadataMatchMethodModel(BaseModel):
    exact: Optional[str] = Field(default=None, alias="exact")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    range: Optional[MatchRangeModel] = Field(default=None, alias="range")
    regex: Optional[str] = Field(default=None, alias="regex")
    suffix: Optional[str] = Field(default=None, alias="suffix")


class GrpcRouteMetadataMatchMethodModel(BaseModel):
    exact: Optional[str] = Field(default=None, alias="exact")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    range: Optional[MatchRangeModel] = Field(default=None, alias="range")
    regex: Optional[str] = Field(default=None, alias="regex")
    suffix: Optional[str] = Field(default=None, alias="suffix")


class HeaderMatchMethodModel(BaseModel):
    exact: Optional[str] = Field(default=None, alias="exact")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    range: Optional[MatchRangeModel] = Field(default=None, alias="range")
    regex: Optional[str] = Field(default=None, alias="regex")
    suffix: Optional[str] = Field(default=None, alias="suffix")


class GrpcRouteActionModel(BaseModel):
    weighted_targets: Sequence[WeightedTargetModel] = Field(alias="weightedTargets")


class HttpRouteActionModel(BaseModel):
    weighted_targets: Sequence[WeightedTargetModel] = Field(alias="weightedTargets")


class TcpRouteActionModel(BaseModel):
    weighted_targets: Sequence[WeightedTargetModel] = Field(alias="weightedTargets")


class HttpGatewayRouteRewriteModel(BaseModel):
    hostname: Optional[GatewayRouteHostnameRewriteModel] = Field(
        default=None, alias="hostname"
    )
    path: Optional[HttpGatewayRoutePathRewriteModel] = Field(default=None, alias="path")
    prefix: Optional[HttpGatewayRoutePrefixRewriteModel] = Field(
        default=None, alias="prefix"
    )


class HttpQueryParameterModel(BaseModel):
    name: str = Field(alias="name")
    match: Optional[QueryParameterMatchModel] = Field(default=None, alias="match")


class LoggingFormatModel(BaseModel):
    json_: Optional[Sequence[JsonFormatRefModel]] = Field(default=None, alias="json")
    text: Optional[str] = Field(default=None, alias="text")


class ListGatewayRoutesInputListGatewayRoutesPaginateModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMeshesInputListMeshesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRoutesInputListRoutesPaginateModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    virtual_router_name: str = Field(alias="virtualRouterName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceInputListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualGatewaysInputListVirtualGatewaysPaginateModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualNodesInputListVirtualNodesPaginateModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualRoutersInputListVirtualRoutersPaginateModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualServicesInputListVirtualServicesPaginateModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMeshesOutputModel(BaseModel):
    meshes: List[MeshRefModel] = Field(alias="meshes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoutesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    routes: List[RouteRefModel] = Field(alias="routes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVirtualGatewaysOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    virtual_gateways: List[VirtualGatewayRefModel] = Field(alias="virtualGateways")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVirtualNodesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    virtual_nodes: List[VirtualNodeRefModel] = Field(alias="virtualNodes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVirtualRoutersOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    virtual_routers: List[VirtualRouterRefModel] = Field(alias="virtualRouters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVirtualServicesOutputModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    virtual_services: List[VirtualServiceRefModel] = Field(alias="virtualServices")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListenerTlsCertificateModel(BaseModel):
    acm: Optional[ListenerTlsAcmCertificateModel] = Field(default=None, alias="acm")
    file: Optional[ListenerTlsFileCertificateModel] = Field(default=None, alias="file")
    sds: Optional[ListenerTlsSdsCertificateModel] = Field(default=None, alias="sds")


class ListenerTlsValidationContextTrustModel(BaseModel):
    file: Optional[TlsValidationContextFileTrustModel] = Field(
        default=None, alias="file"
    )
    sds: Optional[TlsValidationContextSdsTrustModel] = Field(default=None, alias="sds")


class VirtualRouterListenerModel(BaseModel):
    port_mapping: PortMappingModel = Field(alias="portMapping")


class MeshSpecModel(BaseModel):
    egress_filter: Optional[EgressFilterModel] = Field(
        default=None, alias="egressFilter"
    )
    service_discovery: Optional[MeshServiceDiscoveryModel] = Field(
        default=None, alias="serviceDiscovery"
    )


class SubjectAlternativeNamesModel(BaseModel):
    match: SubjectAlternativeNameMatchersModel = Field(alias="match")


class TlsValidationContextTrustModel(BaseModel):
    acm: Optional[TlsValidationContextAcmTrustModel] = Field(default=None, alias="acm")
    file: Optional[TlsValidationContextFileTrustModel] = Field(
        default=None, alias="file"
    )
    sds: Optional[TlsValidationContextSdsTrustModel] = Field(default=None, alias="sds")


class VirtualGatewayClientTlsCertificateModel(BaseModel):
    file: Optional[VirtualGatewayListenerTlsFileCertificateModel] = Field(
        default=None, alias="file"
    )
    sds: Optional[VirtualGatewayListenerTlsSdsCertificateModel] = Field(
        default=None, alias="sds"
    )


class VirtualGatewayConnectionPoolModel(BaseModel):
    grpc: Optional[VirtualGatewayGrpcConnectionPoolModel] = Field(
        default=None, alias="grpc"
    )
    http: Optional[VirtualGatewayHttpConnectionPoolModel] = Field(
        default=None, alias="http"
    )
    http2: Optional[VirtualGatewayHttp2ConnectionPoolModel] = Field(
        default=None, alias="http2"
    )


class VirtualGatewayListenerTlsCertificateModel(BaseModel):
    acm: Optional[VirtualGatewayListenerTlsAcmCertificateModel] = Field(
        default=None, alias="acm"
    )
    file: Optional[VirtualGatewayListenerTlsFileCertificateModel] = Field(
        default=None, alias="file"
    )
    sds: Optional[VirtualGatewayListenerTlsSdsCertificateModel] = Field(
        default=None, alias="sds"
    )


class VirtualGatewayListenerTlsValidationContextTrustModel(BaseModel):
    file: Optional[VirtualGatewayTlsValidationContextFileTrustModel] = Field(
        default=None, alias="file"
    )
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrustModel] = Field(
        default=None, alias="sds"
    )


class VirtualGatewayTlsValidationContextTrustModel(BaseModel):
    acm: Optional[VirtualGatewayTlsValidationContextAcmTrustModel] = Field(
        default=None, alias="acm"
    )
    file: Optional[VirtualGatewayTlsValidationContextFileTrustModel] = Field(
        default=None, alias="file"
    )
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrustModel] = Field(
        default=None, alias="sds"
    )


class VirtualNodeConnectionPoolModel(BaseModel):
    grpc: Optional[VirtualNodeGrpcConnectionPoolModel] = Field(
        default=None, alias="grpc"
    )
    http: Optional[VirtualNodeHttpConnectionPoolModel] = Field(
        default=None, alias="http"
    )
    http2: Optional[VirtualNodeHttp2ConnectionPoolModel] = Field(
        default=None, alias="http2"
    )
    tcp: Optional[VirtualNodeTcpConnectionPoolModel] = Field(default=None, alias="tcp")


class VirtualServiceProviderModel(BaseModel):
    virtual_node: Optional[VirtualNodeServiceProviderModel] = Field(
        default=None, alias="virtualNode"
    )
    virtual_router: Optional[VirtualRouterServiceProviderModel] = Field(
        default=None, alias="virtualRouter"
    )


class ServiceDiscoveryModel(BaseModel):
    aws_cloud_map: Optional[AwsCloudMapServiceDiscoveryModel] = Field(
        default=None, alias="awsCloudMap"
    )
    dns: Optional[DnsServiceDiscoveryModel] = Field(default=None, alias="dns")


class ListenerTimeoutModel(BaseModel):
    grpc: Optional[GrpcTimeoutModel] = Field(default=None, alias="grpc")
    http: Optional[HttpTimeoutModel] = Field(default=None, alias="http")
    http2: Optional[HttpTimeoutModel] = Field(default=None, alias="http2")
    tcp: Optional[TcpTimeoutModel] = Field(default=None, alias="tcp")


class GrpcGatewayRouteActionModel(BaseModel):
    target: GatewayRouteTargetModel = Field(alias="target")
    rewrite: Optional[GrpcGatewayRouteRewriteModel] = Field(
        default=None, alias="rewrite"
    )


class GrpcGatewayRouteMetadataModel(BaseModel):
    name: str = Field(alias="name")
    invert: Optional[bool] = Field(default=None, alias="invert")
    match: Optional[GrpcMetadataMatchMethodModel] = Field(default=None, alias="match")


class GrpcRouteMetadataModel(BaseModel):
    name: str = Field(alias="name")
    invert: Optional[bool] = Field(default=None, alias="invert")
    match: Optional[GrpcRouteMetadataMatchMethodModel] = Field(
        default=None, alias="match"
    )


class HttpGatewayRouteHeaderModel(BaseModel):
    name: str = Field(alias="name")
    invert: Optional[bool] = Field(default=None, alias="invert")
    match: Optional[HeaderMatchMethodModel] = Field(default=None, alias="match")


class HttpRouteHeaderModel(BaseModel):
    name: str = Field(alias="name")
    invert: Optional[bool] = Field(default=None, alias="invert")
    match: Optional[HeaderMatchMethodModel] = Field(default=None, alias="match")


class TcpRouteModel(BaseModel):
    action: TcpRouteActionModel = Field(alias="action")
    match: Optional[TcpRouteMatchModel] = Field(default=None, alias="match")
    timeout: Optional[TcpTimeoutModel] = Field(default=None, alias="timeout")


class HttpGatewayRouteActionModel(BaseModel):
    target: GatewayRouteTargetModel = Field(alias="target")
    rewrite: Optional[HttpGatewayRouteRewriteModel] = Field(
        default=None, alias="rewrite"
    )


class FileAccessLogModel(BaseModel):
    path: str = Field(alias="path")
    format: Optional[LoggingFormatModel] = Field(default=None, alias="format")


class VirtualGatewayFileAccessLogModel(BaseModel):
    path: str = Field(alias="path")
    format: Optional[LoggingFormatModel] = Field(default=None, alias="format")


class VirtualRouterSpecModel(BaseModel):
    listeners: Optional[Sequence[VirtualRouterListenerModel]] = Field(
        default=None, alias="listeners"
    )


class CreateMeshInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    spec: Optional[MeshSpecModel] = Field(default=None, alias="spec")
    tags: Optional[Sequence[TagRefModel]] = Field(default=None, alias="tags")


class MeshDataModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    metadata: ResourceMetadataModel = Field(alias="metadata")
    spec: MeshSpecModel = Field(alias="spec")
    status: MeshStatusModel = Field(alias="status")


class UpdateMeshInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    spec: Optional[MeshSpecModel] = Field(default=None, alias="spec")


class ListenerTlsValidationContextModel(BaseModel):
    trust: ListenerTlsValidationContextTrustModel = Field(alias="trust")
    subject_alternative_names: Optional[SubjectAlternativeNamesModel] = Field(
        default=None, alias="subjectAlternativeNames"
    )


class TlsValidationContextModel(BaseModel):
    trust: TlsValidationContextTrustModel = Field(alias="trust")
    subject_alternative_names: Optional[SubjectAlternativeNamesModel] = Field(
        default=None, alias="subjectAlternativeNames"
    )


class VirtualGatewayListenerTlsValidationContextModel(BaseModel):
    trust: VirtualGatewayListenerTlsValidationContextTrustModel = Field(alias="trust")
    subject_alternative_names: Optional[SubjectAlternativeNamesModel] = Field(
        default=None, alias="subjectAlternativeNames"
    )


class VirtualGatewayTlsValidationContextModel(BaseModel):
    trust: VirtualGatewayTlsValidationContextTrustModel = Field(alias="trust")
    subject_alternative_names: Optional[SubjectAlternativeNamesModel] = Field(
        default=None, alias="subjectAlternativeNames"
    )


class VirtualServiceSpecModel(BaseModel):
    provider: Optional[VirtualServiceProviderModel] = Field(
        default=None, alias="provider"
    )


class GrpcGatewayRouteMatchModel(BaseModel):
    hostname: Optional[GatewayRouteHostnameMatchModel] = Field(
        default=None, alias="hostname"
    )
    metadata: Optional[Sequence[GrpcGatewayRouteMetadataModel]] = Field(
        default=None, alias="metadata"
    )
    port: Optional[int] = Field(default=None, alias="port")
    service_name: Optional[str] = Field(default=None, alias="serviceName")


class GrpcRouteMatchModel(BaseModel):
    metadata: Optional[Sequence[GrpcRouteMetadataModel]] = Field(
        default=None, alias="metadata"
    )
    method_name: Optional[str] = Field(default=None, alias="methodName")
    port: Optional[int] = Field(default=None, alias="port")
    service_name: Optional[str] = Field(default=None, alias="serviceName")


class HttpGatewayRouteMatchModel(BaseModel):
    headers: Optional[Sequence[HttpGatewayRouteHeaderModel]] = Field(
        default=None, alias="headers"
    )
    hostname: Optional[GatewayRouteHostnameMatchModel] = Field(
        default=None, alias="hostname"
    )
    method: Optional[
        Literal[
            "CONNECT",
            "DELETE",
            "GET",
            "HEAD",
            "OPTIONS",
            "PATCH",
            "POST",
            "PUT",
            "TRACE",
        ]
    ] = Field(default=None, alias="method")
    path: Optional[HttpPathMatchModel] = Field(default=None, alias="path")
    port: Optional[int] = Field(default=None, alias="port")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    query_parameters: Optional[Sequence[HttpQueryParameterModel]] = Field(
        default=None, alias="queryParameters"
    )


class HttpRouteMatchModel(BaseModel):
    headers: Optional[Sequence[HttpRouteHeaderModel]] = Field(
        default=None, alias="headers"
    )
    method: Optional[
        Literal[
            "CONNECT",
            "DELETE",
            "GET",
            "HEAD",
            "OPTIONS",
            "PATCH",
            "POST",
            "PUT",
            "TRACE",
        ]
    ] = Field(default=None, alias="method")
    path: Optional[HttpPathMatchModel] = Field(default=None, alias="path")
    port: Optional[int] = Field(default=None, alias="port")
    prefix: Optional[str] = Field(default=None, alias="prefix")
    query_parameters: Optional[Sequence[HttpQueryParameterModel]] = Field(
        default=None, alias="queryParameters"
    )
    scheme: Optional[Literal["http", "https"]] = Field(default=None, alias="scheme")


class AccessLogModel(BaseModel):
    file: Optional[FileAccessLogModel] = Field(default=None, alias="file")


class VirtualGatewayAccessLogModel(BaseModel):
    file: Optional[VirtualGatewayFileAccessLogModel] = Field(default=None, alias="file")


class CreateVirtualRouterInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualRouterSpecModel = Field(alias="spec")
    virtual_router_name: str = Field(alias="virtualRouterName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    tags: Optional[Sequence[TagRefModel]] = Field(default=None, alias="tags")


class UpdateVirtualRouterInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualRouterSpecModel = Field(alias="spec")
    virtual_router_name: str = Field(alias="virtualRouterName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class VirtualRouterDataModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    metadata: ResourceMetadataModel = Field(alias="metadata")
    spec: VirtualRouterSpecModel = Field(alias="spec")
    status: VirtualRouterStatusModel = Field(alias="status")
    virtual_router_name: str = Field(alias="virtualRouterName")


class CreateMeshOutputModel(BaseModel):
    mesh: MeshDataModel = Field(alias="mesh")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMeshOutputModel(BaseModel):
    mesh: MeshDataModel = Field(alias="mesh")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMeshOutputModel(BaseModel):
    mesh: MeshDataModel = Field(alias="mesh")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMeshOutputModel(BaseModel):
    mesh: MeshDataModel = Field(alias="mesh")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListenerTlsModel(BaseModel):
    certificate: ListenerTlsCertificateModel = Field(alias="certificate")
    mode: Literal["DISABLED", "PERMISSIVE", "STRICT"] = Field(alias="mode")
    validation: Optional[ListenerTlsValidationContextModel] = Field(
        default=None, alias="validation"
    )


class ClientPolicyTlsModel(BaseModel):
    validation: TlsValidationContextModel = Field(alias="validation")
    certificate: Optional[ClientTlsCertificateModel] = Field(
        default=None, alias="certificate"
    )
    enforce: Optional[bool] = Field(default=None, alias="enforce")
    ports: Optional[Sequence[int]] = Field(default=None, alias="ports")


class VirtualGatewayListenerTlsModel(BaseModel):
    certificate: VirtualGatewayListenerTlsCertificateModel = Field(alias="certificate")
    mode: Literal["DISABLED", "PERMISSIVE", "STRICT"] = Field(alias="mode")
    validation: Optional[VirtualGatewayListenerTlsValidationContextModel] = Field(
        default=None, alias="validation"
    )


class VirtualGatewayClientPolicyTlsModel(BaseModel):
    validation: VirtualGatewayTlsValidationContextModel = Field(alias="validation")
    certificate: Optional[VirtualGatewayClientTlsCertificateModel] = Field(
        default=None, alias="certificate"
    )
    enforce: Optional[bool] = Field(default=None, alias="enforce")
    ports: Optional[Sequence[int]] = Field(default=None, alias="ports")


class CreateVirtualServiceInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualServiceSpecModel = Field(alias="spec")
    virtual_service_name: str = Field(alias="virtualServiceName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    tags: Optional[Sequence[TagRefModel]] = Field(default=None, alias="tags")


class UpdateVirtualServiceInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualServiceSpecModel = Field(alias="spec")
    virtual_service_name: str = Field(alias="virtualServiceName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class VirtualServiceDataModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    metadata: ResourceMetadataModel = Field(alias="metadata")
    spec: VirtualServiceSpecModel = Field(alias="spec")
    status: VirtualServiceStatusModel = Field(alias="status")
    virtual_service_name: str = Field(alias="virtualServiceName")


class GrpcGatewayRouteModel(BaseModel):
    action: GrpcGatewayRouteActionModel = Field(alias="action")
    match: GrpcGatewayRouteMatchModel = Field(alias="match")


class GrpcRouteModel(BaseModel):
    action: GrpcRouteActionModel = Field(alias="action")
    match: GrpcRouteMatchModel = Field(alias="match")
    retry_policy: Optional[GrpcRetryPolicyModel] = Field(
        default=None, alias="retryPolicy"
    )
    timeout: Optional[GrpcTimeoutModel] = Field(default=None, alias="timeout")


class HttpGatewayRouteModel(BaseModel):
    action: HttpGatewayRouteActionModel = Field(alias="action")
    match: HttpGatewayRouteMatchModel = Field(alias="match")


class HttpRouteModel(BaseModel):
    action: HttpRouteActionModel = Field(alias="action")
    match: HttpRouteMatchModel = Field(alias="match")
    retry_policy: Optional[HttpRetryPolicyModel] = Field(
        default=None, alias="retryPolicy"
    )
    timeout: Optional[HttpTimeoutModel] = Field(default=None, alias="timeout")


class LoggingModel(BaseModel):
    access_log: Optional[AccessLogModel] = Field(default=None, alias="accessLog")


class VirtualGatewayLoggingModel(BaseModel):
    access_log: Optional[VirtualGatewayAccessLogModel] = Field(
        default=None, alias="accessLog"
    )


class CreateVirtualRouterOutputModel(BaseModel):
    virtual_router: VirtualRouterDataModel = Field(alias="virtualRouter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVirtualRouterOutputModel(BaseModel):
    virtual_router: VirtualRouterDataModel = Field(alias="virtualRouter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVirtualRouterOutputModel(BaseModel):
    virtual_router: VirtualRouterDataModel = Field(alias="virtualRouter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVirtualRouterOutputModel(BaseModel):
    virtual_router: VirtualRouterDataModel = Field(alias="virtualRouter")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListenerModel(BaseModel):
    port_mapping: PortMappingModel = Field(alias="portMapping")
    connection_pool: Optional[VirtualNodeConnectionPoolModel] = Field(
        default=None, alias="connectionPool"
    )
    health_check: Optional[HealthCheckPolicyModel] = Field(
        default=None, alias="healthCheck"
    )
    outlier_detection: Optional[OutlierDetectionModel] = Field(
        default=None, alias="outlierDetection"
    )
    timeout: Optional[ListenerTimeoutModel] = Field(default=None, alias="timeout")
    tls: Optional[ListenerTlsModel] = Field(default=None, alias="tls")


class ClientPolicyModel(BaseModel):
    tls: Optional[ClientPolicyTlsModel] = Field(default=None, alias="tls")


class VirtualGatewayListenerModel(BaseModel):
    port_mapping: VirtualGatewayPortMappingModel = Field(alias="portMapping")
    connection_pool: Optional[VirtualGatewayConnectionPoolModel] = Field(
        default=None, alias="connectionPool"
    )
    health_check: Optional[VirtualGatewayHealthCheckPolicyModel] = Field(
        default=None, alias="healthCheck"
    )
    tls: Optional[VirtualGatewayListenerTlsModel] = Field(default=None, alias="tls")


class VirtualGatewayClientPolicyModel(BaseModel):
    tls: Optional[VirtualGatewayClientPolicyTlsModel] = Field(default=None, alias="tls")


class CreateVirtualServiceOutputModel(BaseModel):
    virtual_service: VirtualServiceDataModel = Field(alias="virtualService")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVirtualServiceOutputModel(BaseModel):
    virtual_service: VirtualServiceDataModel = Field(alias="virtualService")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVirtualServiceOutputModel(BaseModel):
    virtual_service: VirtualServiceDataModel = Field(alias="virtualService")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVirtualServiceOutputModel(BaseModel):
    virtual_service: VirtualServiceDataModel = Field(alias="virtualService")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GatewayRouteSpecModel(BaseModel):
    grpc_route: Optional[GrpcGatewayRouteModel] = Field(default=None, alias="grpcRoute")
    http2_route: Optional[HttpGatewayRouteModel] = Field(
        default=None, alias="http2Route"
    )
    http_route: Optional[HttpGatewayRouteModel] = Field(default=None, alias="httpRoute")
    priority: Optional[int] = Field(default=None, alias="priority")


class RouteSpecModel(BaseModel):
    grpc_route: Optional[GrpcRouteModel] = Field(default=None, alias="grpcRoute")
    http2_route: Optional[HttpRouteModel] = Field(default=None, alias="http2Route")
    http_route: Optional[HttpRouteModel] = Field(default=None, alias="httpRoute")
    priority: Optional[int] = Field(default=None, alias="priority")
    tcp_route: Optional[TcpRouteModel] = Field(default=None, alias="tcpRoute")


class BackendDefaultsModel(BaseModel):
    client_policy: Optional[ClientPolicyModel] = Field(
        default=None, alias="clientPolicy"
    )


class VirtualServiceBackendModel(BaseModel):
    virtual_service_name: str = Field(alias="virtualServiceName")
    client_policy: Optional[ClientPolicyModel] = Field(
        default=None, alias="clientPolicy"
    )


class VirtualGatewayBackendDefaultsModel(BaseModel):
    client_policy: Optional[VirtualGatewayClientPolicyModel] = Field(
        default=None, alias="clientPolicy"
    )


class CreateGatewayRouteInputRequestModel(BaseModel):
    gateway_route_name: str = Field(alias="gatewayRouteName")
    mesh_name: str = Field(alias="meshName")
    spec: GatewayRouteSpecModel = Field(alias="spec")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    tags: Optional[Sequence[TagRefModel]] = Field(default=None, alias="tags")


class GatewayRouteDataModel(BaseModel):
    gateway_route_name: str = Field(alias="gatewayRouteName")
    mesh_name: str = Field(alias="meshName")
    metadata: ResourceMetadataModel = Field(alias="metadata")
    spec: GatewayRouteSpecModel = Field(alias="spec")
    status: GatewayRouteStatusModel = Field(alias="status")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")


class UpdateGatewayRouteInputRequestModel(BaseModel):
    gateway_route_name: str = Field(alias="gatewayRouteName")
    mesh_name: str = Field(alias="meshName")
    spec: GatewayRouteSpecModel = Field(alias="spec")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class CreateRouteInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    route_name: str = Field(alias="routeName")
    spec: RouteSpecModel = Field(alias="spec")
    virtual_router_name: str = Field(alias="virtualRouterName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    tags: Optional[Sequence[TagRefModel]] = Field(default=None, alias="tags")


class RouteDataModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    metadata: ResourceMetadataModel = Field(alias="metadata")
    route_name: str = Field(alias="routeName")
    spec: RouteSpecModel = Field(alias="spec")
    status: RouteStatusModel = Field(alias="status")
    virtual_router_name: str = Field(alias="virtualRouterName")


class UpdateRouteInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    route_name: str = Field(alias="routeName")
    spec: RouteSpecModel = Field(alias="spec")
    virtual_router_name: str = Field(alias="virtualRouterName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class BackendModel(BaseModel):
    virtual_service: Optional[VirtualServiceBackendModel] = Field(
        default=None, alias="virtualService"
    )


class VirtualGatewaySpecModel(BaseModel):
    listeners: Sequence[VirtualGatewayListenerModel] = Field(alias="listeners")
    backend_defaults: Optional[VirtualGatewayBackendDefaultsModel] = Field(
        default=None, alias="backendDefaults"
    )
    logging: Optional[VirtualGatewayLoggingModel] = Field(default=None, alias="logging")


class CreateGatewayRouteOutputModel(BaseModel):
    gateway_route: GatewayRouteDataModel = Field(alias="gatewayRoute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGatewayRouteOutputModel(BaseModel):
    gateway_route: GatewayRouteDataModel = Field(alias="gatewayRoute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGatewayRouteOutputModel(BaseModel):
    gateway_route: GatewayRouteDataModel = Field(alias="gatewayRoute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGatewayRouteOutputModel(BaseModel):
    gateway_route: GatewayRouteDataModel = Field(alias="gatewayRoute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRouteOutputModel(BaseModel):
    route: RouteDataModel = Field(alias="route")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRouteOutputModel(BaseModel):
    route: RouteDataModel = Field(alias="route")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRouteOutputModel(BaseModel):
    route: RouteDataModel = Field(alias="route")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRouteOutputModel(BaseModel):
    route: RouteDataModel = Field(alias="route")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VirtualNodeSpecModel(BaseModel):
    backend_defaults: Optional[BackendDefaultsModel] = Field(
        default=None, alias="backendDefaults"
    )
    backends: Optional[Sequence[BackendModel]] = Field(default=None, alias="backends")
    listeners: Optional[Sequence[ListenerModel]] = Field(
        default=None, alias="listeners"
    )
    logging: Optional[LoggingModel] = Field(default=None, alias="logging")
    service_discovery: Optional[ServiceDiscoveryModel] = Field(
        default=None, alias="serviceDiscovery"
    )


class CreateVirtualGatewayInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualGatewaySpecModel = Field(alias="spec")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    tags: Optional[Sequence[TagRefModel]] = Field(default=None, alias="tags")


class UpdateVirtualGatewayInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualGatewaySpecModel = Field(alias="spec")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class VirtualGatewayDataModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    metadata: ResourceMetadataModel = Field(alias="metadata")
    spec: VirtualGatewaySpecModel = Field(alias="spec")
    status: VirtualGatewayStatusModel = Field(alias="status")
    virtual_gateway_name: str = Field(alias="virtualGatewayName")


class CreateVirtualNodeInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualNodeSpecModel = Field(alias="spec")
    virtual_node_name: str = Field(alias="virtualNodeName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")
    tags: Optional[Sequence[TagRefModel]] = Field(default=None, alias="tags")


class UpdateVirtualNodeInputRequestModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    spec: VirtualNodeSpecModel = Field(alias="spec")
    virtual_node_name: str = Field(alias="virtualNodeName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    mesh_owner: Optional[str] = Field(default=None, alias="meshOwner")


class VirtualNodeDataModel(BaseModel):
    mesh_name: str = Field(alias="meshName")
    metadata: ResourceMetadataModel = Field(alias="metadata")
    spec: VirtualNodeSpecModel = Field(alias="spec")
    status: VirtualNodeStatusModel = Field(alias="status")
    virtual_node_name: str = Field(alias="virtualNodeName")


class CreateVirtualGatewayOutputModel(BaseModel):
    virtual_gateway: VirtualGatewayDataModel = Field(alias="virtualGateway")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVirtualGatewayOutputModel(BaseModel):
    virtual_gateway: VirtualGatewayDataModel = Field(alias="virtualGateway")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVirtualGatewayOutputModel(BaseModel):
    virtual_gateway: VirtualGatewayDataModel = Field(alias="virtualGateway")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVirtualGatewayOutputModel(BaseModel):
    virtual_gateway: VirtualGatewayDataModel = Field(alias="virtualGateway")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVirtualNodeOutputModel(BaseModel):
    virtual_node: VirtualNodeDataModel = Field(alias="virtualNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVirtualNodeOutputModel(BaseModel):
    virtual_node: VirtualNodeDataModel = Field(alias="virtualNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVirtualNodeOutputModel(BaseModel):
    virtual_node: VirtualNodeDataModel = Field(alias="virtualNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVirtualNodeOutputModel(BaseModel):
    virtual_node: VirtualNodeDataModel = Field(alias="virtualNode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
