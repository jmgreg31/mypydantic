# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApiGatewayProxyConfigModel(BaseModel):
    api_gateway_id: Optional[str] = Field(default=None, alias="ApiGatewayId")
    endpoint_type: Optional[Literal["PRIVATE", "REGIONAL"]] = Field(
        default=None, alias="EndpointType"
    )
    nlb_arn: Optional[str] = Field(default=None, alias="NlbArn")
    nlb_name: Optional[str] = Field(default=None, alias="NlbName")
    proxy_url: Optional[str] = Field(default=None, alias="ProxyUrl")
    stage_name: Optional[str] = Field(default=None, alias="StageName")
    vpc_link_id: Optional[str] = Field(default=None, alias="VpcLinkId")


class ApiGatewayProxyInputModel(BaseModel):
    endpoint_type: Optional[Literal["PRIVATE", "REGIONAL"]] = Field(
        default=None, alias="EndpointType"
    )
    stage_name: Optional[str] = Field(default=None, alias="StageName")


class ApiGatewayProxySummaryModel(BaseModel):
    api_gateway_id: Optional[str] = Field(default=None, alias="ApiGatewayId")
    endpoint_type: Optional[Literal["PRIVATE", "REGIONAL"]] = Field(
        default=None, alias="EndpointType"
    )
    nlb_arn: Optional[str] = Field(default=None, alias="NlbArn")
    nlb_name: Optional[str] = Field(default=None, alias="NlbName")
    proxy_url: Optional[str] = Field(default=None, alias="ProxyUrl")
    stage_name: Optional[str] = Field(default=None, alias="StageName")
    vpc_link_id: Optional[str] = Field(default=None, alias="VpcLinkId")


class ErrorResponseModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    additional_details: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalDetails"
    )
    code: Optional[
        Literal[
            "INVALID_RESOURCE_STATE",
            "NOT_AUTHORIZED",
            "REQUEST_LIMIT_EXCEEDED",
            "RESOURCE_CREATION_FAILURE",
            "RESOURCE_DELETION_FAILURE",
            "RESOURCE_IN_USE",
            "RESOURCE_LIMIT_EXCEEDED",
            "RESOURCE_NOT_FOUND",
            "RESOURCE_RETRIEVAL_FAILURE",
            "RESOURCE_UPDATE_FAILURE",
            "SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE",
            "STATE_TRANSITION_FAILURE",
        ]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    resource_type: Optional[
        Literal[
            "API_GATEWAY",
            "APPLICATION",
            "ENVIRONMENT",
            "IAM_ROLE",
            "LAMBDA",
            "LOAD_BALANCER_LISTENER",
            "NLB",
            "RESOURCE_SHARE",
            "ROUTE",
            "ROUTE_TABLE",
            "SECURITY_GROUP",
            "SERVICE",
            "SUBNET",
            "TARGET_GROUP",
            "TRANSIT_GATEWAY",
            "TRANSIT_GATEWAY_ATTACHMENT",
            "VPC",
            "VPC_ENDPOINT_SERVICE_CONFIGURATION",
            "VPC_LINK",
        ]
    ] = Field(default=None, alias="ResourceType")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateEnvironmentRequestModel(BaseModel):
    name: str = Field(alias="Name")
    network_fabric_type: Literal["NONE", "TRANSIT_GATEWAY"] = Field(
        alias="NetworkFabricType"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DefaultRouteInputModel(BaseModel):
    activation_state: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="ActivationState"
    )


class UriPathRouteInputModel(BaseModel):
    activation_state: Literal["ACTIVE", "INACTIVE"] = Field(alias="ActivationState")
    source_path: str = Field(alias="SourcePath")
    include_child_paths: Optional[bool] = Field(default=None, alias="IncludeChildPaths")
    methods: Optional[
        Sequence[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]]
    ] = Field(default=None, alias="Methods")


class LambdaEndpointInputModel(BaseModel):
    arn: str = Field(alias="Arn")


class UrlEndpointInputModel(BaseModel):
    url: str = Field(alias="Url")
    health_url: Optional[str] = Field(default=None, alias="HealthUrl")


class DeleteApplicationRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")


class DeleteEnvironmentRequestModel(BaseModel):
    environment_identifier: str = Field(alias="EnvironmentIdentifier")


class DeleteResourcePolicyRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class DeleteRouteRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    route_identifier: str = Field(alias="RouteIdentifier")


class DeleteServiceRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    service_identifier: str = Field(alias="ServiceIdentifier")


class EnvironmentVpcModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    cidr_blocks: Optional[List[str]] = Field(default=None, alias="CidrBlocks")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    vpc_name: Optional[str] = Field(default=None, alias="VpcName")


class GetApplicationRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")


class GetEnvironmentRequestModel(BaseModel):
    environment_identifier: str = Field(alias="EnvironmentIdentifier")


class GetResourcePolicyRequestModel(BaseModel):
    identifier: str = Field(alias="Identifier")


class GetRouteRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    route_identifier: str = Field(alias="RouteIdentifier")


class GetServiceRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    service_identifier: str = Field(alias="ServiceIdentifier")


class LambdaEndpointConfigModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class UrlEndpointConfigModel(BaseModel):
    health_url: Optional[str] = Field(default=None, alias="HealthUrl")
    url: Optional[str] = Field(default=None, alias="Url")


class LambdaEndpointSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationsRequestModel(BaseModel):
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListEnvironmentVpcsRequestModel(BaseModel):
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListEnvironmentsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRoutesRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListServicesRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PutResourcePolicyRequestModel(BaseModel):
    policy: str = Field(alias="Policy")
    resource_arn: str = Field(alias="ResourceArn")


class UrlEndpointSummaryModel(BaseModel):
    health_url: Optional[str] = Field(default=None, alias="HealthUrl")
    url: Optional[str] = Field(default=None, alias="Url")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateRouteRequestModel(BaseModel):
    activation_state: Literal["ACTIVE", "INACTIVE"] = Field(alias="ActivationState")
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    route_identifier: str = Field(alias="RouteIdentifier")


class CreateApplicationRequestModel(BaseModel):
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    name: str = Field(alias="Name")
    proxy_type: Literal["API_GATEWAY"] = Field(alias="ProxyType")
    vpc_id: str = Field(alias="VpcId")
    api_gateway_proxy: Optional[ApiGatewayProxyInputModel] = Field(
        default=None, alias="ApiGatewayProxy"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ApplicationSummaryModel(BaseModel):
    api_gateway_proxy: Optional[ApiGatewayProxySummaryModel] = Field(
        default=None, alias="ApiGatewayProxy"
    )
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_by_account_id: Optional[str] = Field(
        default=None, alias="CreatedByAccountId"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    error: Optional[ErrorResponseModel] = Field(default=None, alias="Error")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    name: Optional[str] = Field(default=None, alias="Name")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    proxy_type: Optional[Literal["API_GATEWAY"]] = Field(
        default=None, alias="ProxyType"
    )
    state: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class EnvironmentSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    description: Optional[str] = Field(default=None, alias="Description")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    error: Optional[ErrorResponseModel] = Field(default=None, alias="Error")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    name: Optional[str] = Field(default=None, alias="Name")
    network_fabric_type: Optional[Literal["NONE", "TRANSIT_GATEWAY"]] = Field(
        default=None, alias="NetworkFabricType"
    )
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    state: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    transit_gateway_id: Optional[str] = Field(default=None, alias="TransitGatewayId")


class RouteSummaryModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_by_account_id: Optional[str] = Field(
        default=None, alias="CreatedByAccountId"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    error: Optional[ErrorResponseModel] = Field(default=None, alias="Error")
    include_child_paths: Optional[bool] = Field(default=None, alias="IncludeChildPaths")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    methods: Optional[
        List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]]
    ] = Field(default=None, alias="Methods")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    path_resource_to_id: Optional[Dict[str, str]] = Field(
        default=None, alias="PathResourceToId"
    )
    route_id: Optional[str] = Field(default=None, alias="RouteId")
    route_type: Optional[Literal["DEFAULT", "URI_PATH"]] = Field(
        default=None, alias="RouteType"
    )
    service_id: Optional[str] = Field(default=None, alias="ServiceId")
    source_path: Optional[str] = Field(default=None, alias="SourcePath")
    state: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "INACTIVE", "UPDATING"]
    ] = Field(default=None, alias="State")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class CreateApplicationResponseModel(BaseModel):
    api_gateway_proxy: ApiGatewayProxyInputModel = Field(alias="ApiGatewayProxy")
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    created_by_account_id: str = Field(alias="CreatedByAccountId")
    created_time: datetime = Field(alias="CreatedTime")
    environment_id: str = Field(alias="EnvironmentId")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    owner_account_id: str = Field(alias="OwnerAccountId")
    proxy_type: Literal["API_GATEWAY"] = Field(alias="ProxyType")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="State"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    vpc_id: str = Field(alias="VpcId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEnvironmentResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_time: datetime = Field(alias="CreatedTime")
    description: str = Field(alias="Description")
    environment_id: str = Field(alias="EnvironmentId")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    network_fabric_type: Literal["NONE", "TRANSIT_GATEWAY"] = Field(
        alias="NetworkFabricType"
    )
    owner_account_id: str = Field(alias="OwnerAccountId")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteApplicationResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    environment_id: str = Field(alias="EnvironmentId")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="State"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteEnvironmentResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    environment_id: str = Field(alias="EnvironmentId")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRouteResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    route_id: str = Field(alias="RouteId")
    service_id: str = Field(alias="ServiceId")
    state: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "INACTIVE", "UPDATING"
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteServiceResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    environment_id: str = Field(alias="EnvironmentId")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    service_id: str = Field(alias="ServiceId")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationResponseModel(BaseModel):
    api_gateway_proxy: ApiGatewayProxyConfigModel = Field(alias="ApiGatewayProxy")
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    created_by_account_id: str = Field(alias="CreatedByAccountId")
    created_time: datetime = Field(alias="CreatedTime")
    environment_id: str = Field(alias="EnvironmentId")
    error: ErrorResponseModel = Field(alias="Error")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    owner_account_id: str = Field(alias="OwnerAccountId")
    proxy_type: Literal["API_GATEWAY"] = Field(alias="ProxyType")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"] = Field(
        alias="State"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    vpc_id: str = Field(alias="VpcId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnvironmentResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_time: datetime = Field(alias="CreatedTime")
    description: str = Field(alias="Description")
    environment_id: str = Field(alias="EnvironmentId")
    error: ErrorResponseModel = Field(alias="Error")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    network_fabric_type: Literal["NONE", "TRANSIT_GATEWAY"] = Field(
        alias="NetworkFabricType"
    )
    owner_account_id: str = Field(alias="OwnerAccountId")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    transit_gateway_id: str = Field(alias="TransitGatewayId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRouteResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    created_by_account_id: str = Field(alias="CreatedByAccountId")
    created_time: datetime = Field(alias="CreatedTime")
    environment_id: str = Field(alias="EnvironmentId")
    error: ErrorResponseModel = Field(alias="Error")
    include_child_paths: bool = Field(alias="IncludeChildPaths")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    methods: List[
        Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    ] = Field(alias="Methods")
    owner_account_id: str = Field(alias="OwnerAccountId")
    path_resource_to_id: Dict[str, str] = Field(alias="PathResourceToId")
    route_id: str = Field(alias="RouteId")
    route_type: Literal["DEFAULT", "URI_PATH"] = Field(alias="RouteType")
    service_id: str = Field(alias="ServiceId")
    source_path: str = Field(alias="SourcePath")
    state: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "INACTIVE", "UPDATING"
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRouteResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    route_id: str = Field(alias="RouteId")
    service_id: str = Field(alias="ServiceId")
    state: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "INACTIVE", "UPDATING"
    ] = Field(alias="State")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRouteRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    route_type: Literal["DEFAULT", "URI_PATH"] = Field(alias="RouteType")
    service_identifier: str = Field(alias="ServiceIdentifier")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    default_route: Optional[DefaultRouteInputModel] = Field(
        default=None, alias="DefaultRoute"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    uri_path_route: Optional[UriPathRouteInputModel] = Field(
        default=None, alias="UriPathRoute"
    )


class CreateRouteResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    created_by_account_id: str = Field(alias="CreatedByAccountId")
    created_time: datetime = Field(alias="CreatedTime")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    owner_account_id: str = Field(alias="OwnerAccountId")
    route_id: str = Field(alias="RouteId")
    route_type: Literal["DEFAULT", "URI_PATH"] = Field(alias="RouteType")
    service_id: str = Field(alias="ServiceId")
    state: Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "INACTIVE", "UPDATING"
    ] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    uri_path_route: UriPathRouteInputModel = Field(alias="UriPathRoute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServiceRequestModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    endpoint_type: Literal["LAMBDA", "URL"] = Field(alias="EndpointType")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    name: str = Field(alias="Name")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    description: Optional[str] = Field(default=None, alias="Description")
    lambda_endpoint: Optional[LambdaEndpointInputModel] = Field(
        default=None, alias="LambdaEndpoint"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    url_endpoint: Optional[UrlEndpointInputModel] = Field(
        default=None, alias="UrlEndpoint"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class CreateServiceResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    created_by_account_id: str = Field(alias="CreatedByAccountId")
    created_time: datetime = Field(alias="CreatedTime")
    description: str = Field(alias="Description")
    endpoint_type: Literal["LAMBDA", "URL"] = Field(alias="EndpointType")
    environment_id: str = Field(alias="EnvironmentId")
    lambda_endpoint: LambdaEndpointInputModel = Field(alias="LambdaEndpoint")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    owner_account_id: str = Field(alias="OwnerAccountId")
    service_id: str = Field(alias="ServiceId")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    url_endpoint: UrlEndpointInputModel = Field(alias="UrlEndpoint")
    vpc_id: str = Field(alias="VpcId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentVpcsResponseModel(BaseModel):
    environment_vpc_list: List[EnvironmentVpcModel] = Field(alias="EnvironmentVpcList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceResponseModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    arn: str = Field(alias="Arn")
    created_by_account_id: str = Field(alias="CreatedByAccountId")
    created_time: datetime = Field(alias="CreatedTime")
    description: str = Field(alias="Description")
    endpoint_type: Literal["LAMBDA", "URL"] = Field(alias="EndpointType")
    environment_id: str = Field(alias="EnvironmentId")
    error: ErrorResponseModel = Field(alias="Error")
    lambda_endpoint: LambdaEndpointConfigModel = Field(alias="LambdaEndpoint")
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    name: str = Field(alias="Name")
    owner_account_id: str = Field(alias="OwnerAccountId")
    service_id: str = Field(alias="ServiceId")
    state: Literal["ACTIVE", "CREATING", "DELETING", "FAILED"] = Field(alias="State")
    tags: Dict[str, str] = Field(alias="Tags")
    url_endpoint: UrlEndpointConfigModel = Field(alias="UrlEndpoint")
    vpc_id: str = Field(alias="VpcId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsRequestListApplicationsPaginateModel(BaseModel):
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentVpcsRequestListEnvironmentVpcsPaginateModel(BaseModel):
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnvironmentsRequestListEnvironmentsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRoutesRequestListRoutesPaginateModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServicesRequestListServicesPaginateModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")
    environment_identifier: str = Field(alias="EnvironmentIdentifier")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ServiceSummaryModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_by_account_id: Optional[str] = Field(
        default=None, alias="CreatedByAccountId"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    description: Optional[str] = Field(default=None, alias="Description")
    endpoint_type: Optional[Literal["LAMBDA", "URL"]] = Field(
        default=None, alias="EndpointType"
    )
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    error: Optional[ErrorResponseModel] = Field(default=None, alias="Error")
    lambda_endpoint: Optional[LambdaEndpointSummaryModel] = Field(
        default=None, alias="LambdaEndpoint"
    )
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    name: Optional[str] = Field(default=None, alias="Name")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    service_id: Optional[str] = Field(default=None, alias="ServiceId")
    state: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="State"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    url_endpoint: Optional[UrlEndpointSummaryModel] = Field(
        default=None, alias="UrlEndpoint"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class ListApplicationsResponseModel(BaseModel):
    application_summary_list: List[ApplicationSummaryModel] = Field(
        alias="ApplicationSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentsResponseModel(BaseModel):
    environment_summary_list: List[EnvironmentSummaryModel] = Field(
        alias="EnvironmentSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoutesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    route_summary_list: List[RouteSummaryModel] = Field(alias="RouteSummaryList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    service_summary_list: List[ServiceSummaryModel] = Field(alias="ServiceSummaryList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
