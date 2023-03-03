# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessLogSettingsModel(BaseModel):
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    format: Optional[str] = Field(default=None, alias="Format")


class ApiMappingModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    stage: str = Field(alias="Stage")
    api_mapping_id: Optional[str] = Field(default=None, alias="ApiMappingId")
    api_mapping_key: Optional[str] = Field(default=None, alias="ApiMappingKey")


class CorsModel(BaseModel):
    allow_credentials: Optional[bool] = Field(default=None, alias="AllowCredentials")
    allow_headers: Optional[Sequence[str]] = Field(default=None, alias="AllowHeaders")
    allow_methods: Optional[Sequence[str]] = Field(default=None, alias="AllowMethods")
    allow_origins: Optional[Sequence[str]] = Field(default=None, alias="AllowOrigins")
    expose_headers: Optional[Sequence[str]] = Field(default=None, alias="ExposeHeaders")
    max_age: Optional[int] = Field(default=None, alias="MaxAge")


class JWTConfigurationModel(BaseModel):
    audience: Optional[Sequence[str]] = Field(default=None, alias="Audience")
    issuer: Optional[str] = Field(default=None, alias="Issuer")


class CreateApiMappingRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    domain_name: str = Field(alias="DomainName")
    stage: str = Field(alias="Stage")
    api_mapping_key: Optional[str] = Field(default=None, alias="ApiMappingKey")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateDeploymentRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    description: Optional[str] = Field(default=None, alias="Description")
    stage_name: Optional[str] = Field(default=None, alias="StageName")


class DomainNameConfigurationModel(BaseModel):
    api_gateway_domain_name: Optional[str] = Field(
        default=None, alias="ApiGatewayDomainName"
    )
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    certificate_name: Optional[str] = Field(default=None, alias="CertificateName")
    certificate_upload_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="CertificateUploadDate"
    )
    domain_name_status: Optional[
        Literal[
            "AVAILABLE",
            "PENDING_CERTIFICATE_REIMPORT",
            "PENDING_OWNERSHIP_VERIFICATION",
            "UPDATING",
        ]
    ] = Field(default=None, alias="DomainNameStatus")
    domain_name_status_message: Optional[str] = Field(
        default=None, alias="DomainNameStatusMessage"
    )
    endpoint_type: Optional[Literal["EDGE", "REGIONAL"]] = Field(
        default=None, alias="EndpointType"
    )
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")
    security_policy: Optional[Literal["TLS_1_0", "TLS_1_2"]] = Field(
        default=None, alias="SecurityPolicy"
    )
    ownership_verification_certificate_arn: Optional[str] = Field(
        default=None, alias="OwnershipVerificationCertificateArn"
    )


class MutualTlsAuthenticationInputModel(BaseModel):
    truststore_uri: Optional[str] = Field(default=None, alias="TruststoreUri")
    truststore_version: Optional[str] = Field(default=None, alias="TruststoreVersion")


class MutualTlsAuthenticationModel(BaseModel):
    truststore_uri: Optional[str] = Field(default=None, alias="TruststoreUri")
    truststore_version: Optional[str] = Field(default=None, alias="TruststoreVersion")
    truststore_warnings: Optional[List[str]] = Field(
        default=None, alias="TruststoreWarnings"
    )


class TlsConfigInputModel(BaseModel):
    server_name_to_verify: Optional[str] = Field(
        default=None, alias="ServerNameToVerify"
    )


class CreateIntegrationResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")
    integration_response_key: str = Field(alias="IntegrationResponseKey")
    content_handling_strategy: Optional[
        Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
    ] = Field(default=None, alias="ContentHandlingStrategy")
    response_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="ResponseParameters"
    )
    response_templates: Optional[Mapping[str, str]] = Field(
        default=None, alias="ResponseTemplates"
    )
    template_selection_expression: Optional[str] = Field(
        default=None, alias="TemplateSelectionExpression"
    )


class TlsConfigModel(BaseModel):
    server_name_to_verify: Optional[str] = Field(
        default=None, alias="ServerNameToVerify"
    )


class CreateModelRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    name: str = Field(alias="Name")
    schema_: str = Field(alias="Schema")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    description: Optional[str] = Field(default=None, alias="Description")


class ParameterConstraintsModel(BaseModel):
    required: Optional[bool] = Field(default=None, alias="Required")


class RouteSettingsModel(BaseModel):
    data_trace_enabled: Optional[bool] = Field(default=None, alias="DataTraceEnabled")
    detailed_metrics_enabled: Optional[bool] = Field(
        default=None, alias="DetailedMetricsEnabled"
    )
    logging_level: Optional[Literal["ERROR", "INFO", "OFF"]] = Field(
        default=None, alias="LoggingLevel"
    )
    throttling_burst_limit: Optional[int] = Field(
        default=None, alias="ThrottlingBurstLimit"
    )
    throttling_rate_limit: Optional[float] = Field(
        default=None, alias="ThrottlingRateLimit"
    )


class CreateVpcLinkRequestModel(BaseModel):
    name: str = Field(alias="Name")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DeleteAccessLogSettingsRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    stage_name: str = Field(alias="StageName")


class DeleteApiMappingRequestModel(BaseModel):
    api_mapping_id: str = Field(alias="ApiMappingId")
    domain_name: str = Field(alias="DomainName")


class DeleteApiRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")


class DeleteAuthorizerRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    authorizer_id: str = Field(alias="AuthorizerId")


class DeleteCorsConfigurationRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")


class DeleteDeploymentRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    deployment_id: str = Field(alias="DeploymentId")


class DeleteDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DeleteIntegrationRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")


class DeleteIntegrationResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")
    integration_response_id: str = Field(alias="IntegrationResponseId")


class DeleteModelRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    model_id: str = Field(alias="ModelId")


class DeleteRouteRequestParameterRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    request_parameter_key: str = Field(alias="RequestParameterKey")
    route_id: str = Field(alias="RouteId")


class DeleteRouteRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")


class DeleteRouteResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")
    route_response_id: str = Field(alias="RouteResponseId")


class DeleteRouteSettingsRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_key: str = Field(alias="RouteKey")
    stage_name: str = Field(alias="StageName")


class DeleteStageRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    stage_name: str = Field(alias="StageName")


class DeleteVpcLinkRequestModel(BaseModel):
    vpc_link_id: str = Field(alias="VpcLinkId")


class DeploymentModel(BaseModel):
    auto_deployed: Optional[bool] = Field(default=None, alias="AutoDeployed")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    deployment_status: Optional[Literal["DEPLOYED", "FAILED", "PENDING"]] = Field(
        default=None, alias="DeploymentStatus"
    )
    deployment_status_message: Optional[str] = Field(
        default=None, alias="DeploymentStatusMessage"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ExportApiRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    output_type: Literal["JSON", "YAML"] = Field(alias="OutputType")
    specification: Literal["OAS30"] = Field(alias="Specification")
    export_version: Optional[str] = Field(default=None, alias="ExportVersion")
    include_extensions: Optional[bool] = Field(default=None, alias="IncludeExtensions")
    stage_name: Optional[str] = Field(default=None, alias="StageName")


class GetApiMappingRequestModel(BaseModel):
    api_mapping_id: str = Field(alias="ApiMappingId")
    domain_name: str = Field(alias="DomainName")


class GetApiMappingsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetApiRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetApisRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetAuthorizerRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    authorizer_id: str = Field(alias="AuthorizerId")


class GetAuthorizersRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetDeploymentRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    deployment_id: str = Field(alias="DeploymentId")


class GetDeploymentsRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class GetDomainNamesRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetIntegrationRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")


class GetIntegrationResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")
    integration_response_id: str = Field(alias="IntegrationResponseId")


class GetIntegrationResponsesRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class IntegrationResponseModel(BaseModel):
    integration_response_key: str = Field(alias="IntegrationResponseKey")
    content_handling_strategy: Optional[
        Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
    ] = Field(default=None, alias="ContentHandlingStrategy")
    integration_response_id: Optional[str] = Field(
        default=None, alias="IntegrationResponseId"
    )
    response_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="ResponseParameters"
    )
    response_templates: Optional[Dict[str, str]] = Field(
        default=None, alias="ResponseTemplates"
    )
    template_selection_expression: Optional[str] = Field(
        default=None, alias="TemplateSelectionExpression"
    )


class GetIntegrationsRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetModelRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    model_id: str = Field(alias="ModelId")


class GetModelTemplateRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    model_id: str = Field(alias="ModelId")


class GetModelsRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ModelModel(BaseModel):
    name: str = Field(alias="Name")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    description: Optional[str] = Field(default=None, alias="Description")
    model_id: Optional[str] = Field(default=None, alias="ModelId")
    schema_: Optional[str] = Field(default=None, alias="Schema")


class GetRouteRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")


class GetRouteResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")
    route_response_id: str = Field(alias="RouteResponseId")


class GetRouteResponsesRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetRoutesRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetStageRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    stage_name: str = Field(alias="StageName")


class GetStagesRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetVpcLinkRequestModel(BaseModel):
    vpc_link_id: str = Field(alias="VpcLinkId")


class GetVpcLinksRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class VpcLinkModel(BaseModel):
    name: str = Field(alias="Name")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    vpc_link_id: str = Field(alias="VpcLinkId")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    vpc_link_status: Optional[
        Literal["AVAILABLE", "DELETING", "FAILED", "INACTIVE", "PENDING"]
    ] = Field(default=None, alias="VpcLinkStatus")
    vpc_link_status_message: Optional[str] = Field(
        default=None, alias="VpcLinkStatusMessage"
    )
    vpc_link_version: Optional[Literal["V2"]] = Field(
        default=None, alias="VpcLinkVersion"
    )


class ImportApiRequestModel(BaseModel):
    body: str = Field(alias="Body")
    basepath: Optional[str] = Field(default=None, alias="Basepath")
    fail_on_warnings: Optional[bool] = Field(default=None, alias="FailOnWarnings")


class ReimportApiRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    body: str = Field(alias="Body")
    basepath: Optional[str] = Field(default=None, alias="Basepath")
    fail_on_warnings: Optional[bool] = Field(default=None, alias="FailOnWarnings")


class ResetAuthorizersCacheRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    stage_name: str = Field(alias="StageName")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateApiMappingRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    api_mapping_id: str = Field(alias="ApiMappingId")
    domain_name: str = Field(alias="DomainName")
    api_mapping_key: Optional[str] = Field(default=None, alias="ApiMappingKey")
    stage: Optional[str] = Field(default=None, alias="Stage")


class UpdateDeploymentRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    deployment_id: str = Field(alias="DeploymentId")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateIntegrationResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")
    integration_response_id: str = Field(alias="IntegrationResponseId")
    content_handling_strategy: Optional[
        Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
    ] = Field(default=None, alias="ContentHandlingStrategy")
    integration_response_key: Optional[str] = Field(
        default=None, alias="IntegrationResponseKey"
    )
    response_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="ResponseParameters"
    )
    response_templates: Optional[Mapping[str, str]] = Field(
        default=None, alias="ResponseTemplates"
    )
    template_selection_expression: Optional[str] = Field(
        default=None, alias="TemplateSelectionExpression"
    )


class UpdateModelRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    model_id: str = Field(alias="ModelId")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    schema_: Optional[str] = Field(default=None, alias="Schema")


class UpdateVpcLinkRequestModel(BaseModel):
    vpc_link_id: str = Field(alias="VpcLinkId")
    name: Optional[str] = Field(default=None, alias="Name")


class ApiModel(BaseModel):
    name: str = Field(alias="Name")
    protocol_type: Literal["HTTP", "WEBSOCKET"] = Field(alias="ProtocolType")
    route_selection_expression: str = Field(alias="RouteSelectionExpression")
    api_endpoint: Optional[str] = Field(default=None, alias="ApiEndpoint")
    api_gateway_managed: Optional[bool] = Field(default=None, alias="ApiGatewayManaged")
    api_id: Optional[str] = Field(default=None, alias="ApiId")
    api_key_selection_expression: Optional[str] = Field(
        default=None, alias="ApiKeySelectionExpression"
    )
    cors_configuration: Optional[CorsModel] = Field(
        default=None, alias="CorsConfiguration"
    )
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    description: Optional[str] = Field(default=None, alias="Description")
    disable_schema_validation: Optional[bool] = Field(
        default=None, alias="DisableSchemaValidation"
    )
    disable_execute_api_endpoint: Optional[bool] = Field(
        default=None, alias="DisableExecuteApiEndpoint"
    )
    import_info: Optional[List[str]] = Field(default=None, alias="ImportInfo")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    version: Optional[str] = Field(default=None, alias="Version")
    warnings: Optional[List[str]] = Field(default=None, alias="Warnings")


class CreateApiRequestModel(BaseModel):
    name: str = Field(alias="Name")
    protocol_type: Literal["HTTP", "WEBSOCKET"] = Field(alias="ProtocolType")
    api_key_selection_expression: Optional[str] = Field(
        default=None, alias="ApiKeySelectionExpression"
    )
    cors_configuration: Optional[CorsModel] = Field(
        default=None, alias="CorsConfiguration"
    )
    credentials_arn: Optional[str] = Field(default=None, alias="CredentialsArn")
    description: Optional[str] = Field(default=None, alias="Description")
    disable_schema_validation: Optional[bool] = Field(
        default=None, alias="DisableSchemaValidation"
    )
    disable_execute_api_endpoint: Optional[bool] = Field(
        default=None, alias="DisableExecuteApiEndpoint"
    )
    route_key: Optional[str] = Field(default=None, alias="RouteKey")
    route_selection_expression: Optional[str] = Field(
        default=None, alias="RouteSelectionExpression"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    target: Optional[str] = Field(default=None, alias="Target")
    version: Optional[str] = Field(default=None, alias="Version")


class UpdateApiRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    api_key_selection_expression: Optional[str] = Field(
        default=None, alias="ApiKeySelectionExpression"
    )
    cors_configuration: Optional[CorsModel] = Field(
        default=None, alias="CorsConfiguration"
    )
    credentials_arn: Optional[str] = Field(default=None, alias="CredentialsArn")
    description: Optional[str] = Field(default=None, alias="Description")
    disable_schema_validation: Optional[bool] = Field(
        default=None, alias="DisableSchemaValidation"
    )
    disable_execute_api_endpoint: Optional[bool] = Field(
        default=None, alias="DisableExecuteApiEndpoint"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    route_key: Optional[str] = Field(default=None, alias="RouteKey")
    route_selection_expression: Optional[str] = Field(
        default=None, alias="RouteSelectionExpression"
    )
    target: Optional[str] = Field(default=None, alias="Target")
    version: Optional[str] = Field(default=None, alias="Version")


class AuthorizerModel(BaseModel):
    name: str = Field(alias="Name")
    authorizer_credentials_arn: Optional[str] = Field(
        default=None, alias="AuthorizerCredentialsArn"
    )
    authorizer_id: Optional[str] = Field(default=None, alias="AuthorizerId")
    authorizer_payload_format_version: Optional[str] = Field(
        default=None, alias="AuthorizerPayloadFormatVersion"
    )
    authorizer_result_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="AuthorizerResultTtlInSeconds"
    )
    authorizer_type: Optional[Literal["JWT", "REQUEST"]] = Field(
        default=None, alias="AuthorizerType"
    )
    authorizer_uri: Optional[str] = Field(default=None, alias="AuthorizerUri")
    enable_simple_responses: Optional[bool] = Field(
        default=None, alias="EnableSimpleResponses"
    )
    identity_source: Optional[List[str]] = Field(default=None, alias="IdentitySource")
    identity_validation_expression: Optional[str] = Field(
        default=None, alias="IdentityValidationExpression"
    )
    jwt_configuration: Optional[JWTConfigurationModel] = Field(
        default=None, alias="JwtConfiguration"
    )


class CreateAuthorizerRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    authorizer_type: Literal["JWT", "REQUEST"] = Field(alias="AuthorizerType")
    identity_source: Sequence[str] = Field(alias="IdentitySource")
    name: str = Field(alias="Name")
    authorizer_credentials_arn: Optional[str] = Field(
        default=None, alias="AuthorizerCredentialsArn"
    )
    authorizer_payload_format_version: Optional[str] = Field(
        default=None, alias="AuthorizerPayloadFormatVersion"
    )
    authorizer_result_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="AuthorizerResultTtlInSeconds"
    )
    authorizer_uri: Optional[str] = Field(default=None, alias="AuthorizerUri")
    enable_simple_responses: Optional[bool] = Field(
        default=None, alias="EnableSimpleResponses"
    )
    identity_validation_expression: Optional[str] = Field(
        default=None, alias="IdentityValidationExpression"
    )
    jwt_configuration: Optional[JWTConfigurationModel] = Field(
        default=None, alias="JwtConfiguration"
    )


class UpdateAuthorizerRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    authorizer_id: str = Field(alias="AuthorizerId")
    authorizer_credentials_arn: Optional[str] = Field(
        default=None, alias="AuthorizerCredentialsArn"
    )
    authorizer_payload_format_version: Optional[str] = Field(
        default=None, alias="AuthorizerPayloadFormatVersion"
    )
    authorizer_result_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="AuthorizerResultTtlInSeconds"
    )
    authorizer_type: Optional[Literal["JWT", "REQUEST"]] = Field(
        default=None, alias="AuthorizerType"
    )
    authorizer_uri: Optional[str] = Field(default=None, alias="AuthorizerUri")
    enable_simple_responses: Optional[bool] = Field(
        default=None, alias="EnableSimpleResponses"
    )
    identity_source: Optional[Sequence[str]] = Field(
        default=None, alias="IdentitySource"
    )
    identity_validation_expression: Optional[str] = Field(
        default=None, alias="IdentityValidationExpression"
    )
    jwt_configuration: Optional[JWTConfigurationModel] = Field(
        default=None, alias="JwtConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class CreateApiMappingResponseModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    api_mapping_id: str = Field(alias="ApiMappingId")
    api_mapping_key: str = Field(alias="ApiMappingKey")
    stage: str = Field(alias="Stage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApiResponseModel(BaseModel):
    api_endpoint: str = Field(alias="ApiEndpoint")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_id: str = Field(alias="ApiId")
    api_key_selection_expression: str = Field(alias="ApiKeySelectionExpression")
    cors_configuration: CorsModel = Field(alias="CorsConfiguration")
    created_date: datetime = Field(alias="CreatedDate")
    description: str = Field(alias="Description")
    disable_schema_validation: bool = Field(alias="DisableSchemaValidation")
    disable_execute_api_endpoint: bool = Field(alias="DisableExecuteApiEndpoint")
    import_info: List[str] = Field(alias="ImportInfo")
    name: str = Field(alias="Name")
    protocol_type: Literal["HTTP", "WEBSOCKET"] = Field(alias="ProtocolType")
    route_selection_expression: str = Field(alias="RouteSelectionExpression")
    tags: Dict[str, str] = Field(alias="Tags")
    version: str = Field(alias="Version")
    warnings: List[str] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAuthorizerResponseModel(BaseModel):
    authorizer_credentials_arn: str = Field(alias="AuthorizerCredentialsArn")
    authorizer_id: str = Field(alias="AuthorizerId")
    authorizer_payload_format_version: str = Field(
        alias="AuthorizerPayloadFormatVersion"
    )
    authorizer_result_ttl_in_seconds: int = Field(alias="AuthorizerResultTtlInSeconds")
    authorizer_type: Literal["JWT", "REQUEST"] = Field(alias="AuthorizerType")
    authorizer_uri: str = Field(alias="AuthorizerUri")
    enable_simple_responses: bool = Field(alias="EnableSimpleResponses")
    identity_source: List[str] = Field(alias="IdentitySource")
    identity_validation_expression: str = Field(alias="IdentityValidationExpression")
    jwt_configuration: JWTConfigurationModel = Field(alias="JwtConfiguration")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentResponseModel(BaseModel):
    auto_deployed: bool = Field(alias="AutoDeployed")
    created_date: datetime = Field(alias="CreatedDate")
    deployment_id: str = Field(alias="DeploymentId")
    deployment_status: Literal["DEPLOYED", "FAILED", "PENDING"] = Field(
        alias="DeploymentStatus"
    )
    deployment_status_message: str = Field(alias="DeploymentStatusMessage")
    description: str = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIntegrationResponseResponseModel(BaseModel):
    content_handling_strategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="ContentHandlingStrategy"
    )
    integration_response_id: str = Field(alias="IntegrationResponseId")
    integration_response_key: str = Field(alias="IntegrationResponseKey")
    response_parameters: Dict[str, str] = Field(alias="ResponseParameters")
    response_templates: Dict[str, str] = Field(alias="ResponseTemplates")
    template_selection_expression: str = Field(alias="TemplateSelectionExpression")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelResponseModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    description: str = Field(alias="Description")
    model_id: str = Field(alias="ModelId")
    name: str = Field(alias="Name")
    schema_: str = Field(alias="Schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVpcLinkResponseModel(BaseModel):
    created_date: datetime = Field(alias="CreatedDate")
    name: str = Field(alias="Name")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    tags: Dict[str, str] = Field(alias="Tags")
    vpc_link_id: str = Field(alias="VpcLinkId")
    vpc_link_status: Literal[
        "AVAILABLE", "DELETING", "FAILED", "INACTIVE", "PENDING"
    ] = Field(alias="VpcLinkStatus")
    vpc_link_status_message: str = Field(alias="VpcLinkStatusMessage")
    vpc_link_version: Literal["V2"] = Field(alias="VpcLinkVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportApiResponseModel(BaseModel):
    body: Type[StreamingBody] = Field(alias="body")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApiMappingResponseModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    api_mapping_id: str = Field(alias="ApiMappingId")
    api_mapping_key: str = Field(alias="ApiMappingKey")
    stage: str = Field(alias="Stage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApiMappingsResponseModel(BaseModel):
    items: List[ApiMappingModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApiResponseModel(BaseModel):
    api_endpoint: str = Field(alias="ApiEndpoint")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_id: str = Field(alias="ApiId")
    api_key_selection_expression: str = Field(alias="ApiKeySelectionExpression")
    cors_configuration: CorsModel = Field(alias="CorsConfiguration")
    created_date: datetime = Field(alias="CreatedDate")
    description: str = Field(alias="Description")
    disable_schema_validation: bool = Field(alias="DisableSchemaValidation")
    disable_execute_api_endpoint: bool = Field(alias="DisableExecuteApiEndpoint")
    import_info: List[str] = Field(alias="ImportInfo")
    name: str = Field(alias="Name")
    protocol_type: Literal["HTTP", "WEBSOCKET"] = Field(alias="ProtocolType")
    route_selection_expression: str = Field(alias="RouteSelectionExpression")
    tags: Dict[str, str] = Field(alias="Tags")
    version: str = Field(alias="Version")
    warnings: List[str] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAuthorizerResponseModel(BaseModel):
    authorizer_credentials_arn: str = Field(alias="AuthorizerCredentialsArn")
    authorizer_id: str = Field(alias="AuthorizerId")
    authorizer_payload_format_version: str = Field(
        alias="AuthorizerPayloadFormatVersion"
    )
    authorizer_result_ttl_in_seconds: int = Field(alias="AuthorizerResultTtlInSeconds")
    authorizer_type: Literal["JWT", "REQUEST"] = Field(alias="AuthorizerType")
    authorizer_uri: str = Field(alias="AuthorizerUri")
    enable_simple_responses: bool = Field(alias="EnableSimpleResponses")
    identity_source: List[str] = Field(alias="IdentitySource")
    identity_validation_expression: str = Field(alias="IdentityValidationExpression")
    jwt_configuration: JWTConfigurationModel = Field(alias="JwtConfiguration")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentResponseModel(BaseModel):
    auto_deployed: bool = Field(alias="AutoDeployed")
    created_date: datetime = Field(alias="CreatedDate")
    deployment_id: str = Field(alias="DeploymentId")
    deployment_status: Literal["DEPLOYED", "FAILED", "PENDING"] = Field(
        alias="DeploymentStatus"
    )
    deployment_status_message: str = Field(alias="DeploymentStatusMessage")
    description: str = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIntegrationResponseResponseModel(BaseModel):
    content_handling_strategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="ContentHandlingStrategy"
    )
    integration_response_id: str = Field(alias="IntegrationResponseId")
    integration_response_key: str = Field(alias="IntegrationResponseKey")
    response_parameters: Dict[str, str] = Field(alias="ResponseParameters")
    response_templates: Dict[str, str] = Field(alias="ResponseTemplates")
    template_selection_expression: str = Field(alias="TemplateSelectionExpression")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetModelResponseModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    description: str = Field(alias="Description")
    model_id: str = Field(alias="ModelId")
    name: str = Field(alias="Name")
    schema_: str = Field(alias="Schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetModelTemplateResponseModel(BaseModel):
    value: str = Field(alias="Value")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTagsResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVpcLinkResponseModel(BaseModel):
    created_date: datetime = Field(alias="CreatedDate")
    name: str = Field(alias="Name")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    tags: Dict[str, str] = Field(alias="Tags")
    vpc_link_id: str = Field(alias="VpcLinkId")
    vpc_link_status: Literal[
        "AVAILABLE", "DELETING", "FAILED", "INACTIVE", "PENDING"
    ] = Field(alias="VpcLinkStatus")
    vpc_link_status_message: str = Field(alias="VpcLinkStatusMessage")
    vpc_link_version: Literal["V2"] = Field(alias="VpcLinkVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportApiResponseModel(BaseModel):
    api_endpoint: str = Field(alias="ApiEndpoint")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_id: str = Field(alias="ApiId")
    api_key_selection_expression: str = Field(alias="ApiKeySelectionExpression")
    cors_configuration: CorsModel = Field(alias="CorsConfiguration")
    created_date: datetime = Field(alias="CreatedDate")
    description: str = Field(alias="Description")
    disable_schema_validation: bool = Field(alias="DisableSchemaValidation")
    disable_execute_api_endpoint: bool = Field(alias="DisableExecuteApiEndpoint")
    import_info: List[str] = Field(alias="ImportInfo")
    name: str = Field(alias="Name")
    protocol_type: Literal["HTTP", "WEBSOCKET"] = Field(alias="ProtocolType")
    route_selection_expression: str = Field(alias="RouteSelectionExpression")
    tags: Dict[str, str] = Field(alias="Tags")
    version: str = Field(alias="Version")
    warnings: List[str] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReimportApiResponseModel(BaseModel):
    api_endpoint: str = Field(alias="ApiEndpoint")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_id: str = Field(alias="ApiId")
    api_key_selection_expression: str = Field(alias="ApiKeySelectionExpression")
    cors_configuration: CorsModel = Field(alias="CorsConfiguration")
    created_date: datetime = Field(alias="CreatedDate")
    description: str = Field(alias="Description")
    disable_schema_validation: bool = Field(alias="DisableSchemaValidation")
    disable_execute_api_endpoint: bool = Field(alias="DisableExecuteApiEndpoint")
    import_info: List[str] = Field(alias="ImportInfo")
    name: str = Field(alias="Name")
    protocol_type: Literal["HTTP", "WEBSOCKET"] = Field(alias="ProtocolType")
    route_selection_expression: str = Field(alias="RouteSelectionExpression")
    tags: Dict[str, str] = Field(alias="Tags")
    version: str = Field(alias="Version")
    warnings: List[str] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApiMappingResponseModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    api_mapping_id: str = Field(alias="ApiMappingId")
    api_mapping_key: str = Field(alias="ApiMappingKey")
    stage: str = Field(alias="Stage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApiResponseModel(BaseModel):
    api_endpoint: str = Field(alias="ApiEndpoint")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_id: str = Field(alias="ApiId")
    api_key_selection_expression: str = Field(alias="ApiKeySelectionExpression")
    cors_configuration: CorsModel = Field(alias="CorsConfiguration")
    created_date: datetime = Field(alias="CreatedDate")
    description: str = Field(alias="Description")
    disable_schema_validation: bool = Field(alias="DisableSchemaValidation")
    disable_execute_api_endpoint: bool = Field(alias="DisableExecuteApiEndpoint")
    import_info: List[str] = Field(alias="ImportInfo")
    name: str = Field(alias="Name")
    protocol_type: Literal["HTTP", "WEBSOCKET"] = Field(alias="ProtocolType")
    route_selection_expression: str = Field(alias="RouteSelectionExpression")
    tags: Dict[str, str] = Field(alias="Tags")
    version: str = Field(alias="Version")
    warnings: List[str] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAuthorizerResponseModel(BaseModel):
    authorizer_credentials_arn: str = Field(alias="AuthorizerCredentialsArn")
    authorizer_id: str = Field(alias="AuthorizerId")
    authorizer_payload_format_version: str = Field(
        alias="AuthorizerPayloadFormatVersion"
    )
    authorizer_result_ttl_in_seconds: int = Field(alias="AuthorizerResultTtlInSeconds")
    authorizer_type: Literal["JWT", "REQUEST"] = Field(alias="AuthorizerType")
    authorizer_uri: str = Field(alias="AuthorizerUri")
    enable_simple_responses: bool = Field(alias="EnableSimpleResponses")
    identity_source: List[str] = Field(alias="IdentitySource")
    identity_validation_expression: str = Field(alias="IdentityValidationExpression")
    jwt_configuration: JWTConfigurationModel = Field(alias="JwtConfiguration")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDeploymentResponseModel(BaseModel):
    auto_deployed: bool = Field(alias="AutoDeployed")
    created_date: datetime = Field(alias="CreatedDate")
    deployment_id: str = Field(alias="DeploymentId")
    deployment_status: Literal["DEPLOYED", "FAILED", "PENDING"] = Field(
        alias="DeploymentStatus"
    )
    deployment_status_message: str = Field(alias="DeploymentStatusMessage")
    description: str = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIntegrationResponseResponseModel(BaseModel):
    content_handling_strategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="ContentHandlingStrategy"
    )
    integration_response_id: str = Field(alias="IntegrationResponseId")
    integration_response_key: str = Field(alias="IntegrationResponseKey")
    response_parameters: Dict[str, str] = Field(alias="ResponseParameters")
    response_templates: Dict[str, str] = Field(alias="ResponseTemplates")
    template_selection_expression: str = Field(alias="TemplateSelectionExpression")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateModelResponseModel(BaseModel):
    content_type: str = Field(alias="ContentType")
    description: str = Field(alias="Description")
    model_id: str = Field(alias="ModelId")
    name: str = Field(alias="Name")
    schema_: str = Field(alias="Schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVpcLinkResponseModel(BaseModel):
    created_date: datetime = Field(alias="CreatedDate")
    name: str = Field(alias="Name")
    security_group_ids: List[str] = Field(alias="SecurityGroupIds")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    tags: Dict[str, str] = Field(alias="Tags")
    vpc_link_id: str = Field(alias="VpcLinkId")
    vpc_link_status: Literal[
        "AVAILABLE", "DELETING", "FAILED", "INACTIVE", "PENDING"
    ] = Field(alias="VpcLinkStatus")
    vpc_link_status_message: str = Field(alias="VpcLinkStatusMessage")
    vpc_link_version: Literal["V2"] = Field(alias="VpcLinkVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    domain_name_configurations: Optional[
        Sequence[DomainNameConfigurationModel]
    ] = Field(default=None, alias="DomainNameConfigurations")
    mutual_tls_authentication: Optional[MutualTlsAuthenticationInputModel] = Field(
        default=None, alias="MutualTlsAuthentication"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    domain_name_configurations: Optional[
        Sequence[DomainNameConfigurationModel]
    ] = Field(default=None, alias="DomainNameConfigurations")
    mutual_tls_authentication: Optional[MutualTlsAuthenticationInputModel] = Field(
        default=None, alias="MutualTlsAuthentication"
    )


class CreateDomainNameResponseModel(BaseModel):
    api_mapping_selection_expression: str = Field(alias="ApiMappingSelectionExpression")
    domain_name: str = Field(alias="DomainName")
    domain_name_configurations: List[DomainNameConfigurationModel] = Field(
        alias="DomainNameConfigurations"
    )
    mutual_tls_authentication: MutualTlsAuthenticationModel = Field(
        alias="MutualTlsAuthentication"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainNameModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    api_mapping_selection_expression: Optional[str] = Field(
        default=None, alias="ApiMappingSelectionExpression"
    )
    domain_name_configurations: Optional[List[DomainNameConfigurationModel]] = Field(
        default=None, alias="DomainNameConfigurations"
    )
    mutual_tls_authentication: Optional[MutualTlsAuthenticationModel] = Field(
        default=None, alias="MutualTlsAuthentication"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class GetDomainNameResponseModel(BaseModel):
    api_mapping_selection_expression: str = Field(alias="ApiMappingSelectionExpression")
    domain_name: str = Field(alias="DomainName")
    domain_name_configurations: List[DomainNameConfigurationModel] = Field(
        alias="DomainNameConfigurations"
    )
    mutual_tls_authentication: MutualTlsAuthenticationModel = Field(
        alias="MutualTlsAuthentication"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainNameResponseModel(BaseModel):
    api_mapping_selection_expression: str = Field(alias="ApiMappingSelectionExpression")
    domain_name: str = Field(alias="DomainName")
    domain_name_configurations: List[DomainNameConfigurationModel] = Field(
        alias="DomainNameConfigurations"
    )
    mutual_tls_authentication: MutualTlsAuthenticationModel = Field(
        alias="MutualTlsAuthentication"
    )
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIntegrationRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_type: Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"] = Field(
        alias="IntegrationType"
    )
    connection_id: Optional[str] = Field(default=None, alias="ConnectionId")
    connection_type: Optional[Literal["INTERNET", "VPC_LINK"]] = Field(
        default=None, alias="ConnectionType"
    )
    content_handling_strategy: Optional[
        Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
    ] = Field(default=None, alias="ContentHandlingStrategy")
    credentials_arn: Optional[str] = Field(default=None, alias="CredentialsArn")
    description: Optional[str] = Field(default=None, alias="Description")
    integration_method: Optional[str] = Field(default=None, alias="IntegrationMethod")
    integration_subtype: Optional[str] = Field(default=None, alias="IntegrationSubtype")
    integration_uri: Optional[str] = Field(default=None, alias="IntegrationUri")
    passthrough_behavior: Optional[
        Literal["NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"]
    ] = Field(default=None, alias="PassthroughBehavior")
    payload_format_version: Optional[str] = Field(
        default=None, alias="PayloadFormatVersion"
    )
    request_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="RequestParameters"
    )
    request_templates: Optional[Mapping[str, str]] = Field(
        default=None, alias="RequestTemplates"
    )
    response_parameters: Optional[Mapping[str, Mapping[str, str]]] = Field(
        default=None, alias="ResponseParameters"
    )
    template_selection_expression: Optional[str] = Field(
        default=None, alias="TemplateSelectionExpression"
    )
    timeout_in_millis: Optional[int] = Field(default=None, alias="TimeoutInMillis")
    tls_config: Optional[TlsConfigInputModel] = Field(default=None, alias="TlsConfig")


class UpdateIntegrationRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")
    connection_id: Optional[str] = Field(default=None, alias="ConnectionId")
    connection_type: Optional[Literal["INTERNET", "VPC_LINK"]] = Field(
        default=None, alias="ConnectionType"
    )
    content_handling_strategy: Optional[
        Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
    ] = Field(default=None, alias="ContentHandlingStrategy")
    credentials_arn: Optional[str] = Field(default=None, alias="CredentialsArn")
    description: Optional[str] = Field(default=None, alias="Description")
    integration_method: Optional[str] = Field(default=None, alias="IntegrationMethod")
    integration_subtype: Optional[str] = Field(default=None, alias="IntegrationSubtype")
    integration_type: Optional[
        Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]
    ] = Field(default=None, alias="IntegrationType")
    integration_uri: Optional[str] = Field(default=None, alias="IntegrationUri")
    passthrough_behavior: Optional[
        Literal["NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"]
    ] = Field(default=None, alias="PassthroughBehavior")
    payload_format_version: Optional[str] = Field(
        default=None, alias="PayloadFormatVersion"
    )
    request_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="RequestParameters"
    )
    request_templates: Optional[Mapping[str, str]] = Field(
        default=None, alias="RequestTemplates"
    )
    response_parameters: Optional[Mapping[str, Mapping[str, str]]] = Field(
        default=None, alias="ResponseParameters"
    )
    template_selection_expression: Optional[str] = Field(
        default=None, alias="TemplateSelectionExpression"
    )
    timeout_in_millis: Optional[int] = Field(default=None, alias="TimeoutInMillis")
    tls_config: Optional[TlsConfigInputModel] = Field(default=None, alias="TlsConfig")


class CreateIntegrationResultModel(BaseModel):
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    connection_id: str = Field(alias="ConnectionId")
    connection_type: Literal["INTERNET", "VPC_LINK"] = Field(alias="ConnectionType")
    content_handling_strategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="ContentHandlingStrategy"
    )
    credentials_arn: str = Field(alias="CredentialsArn")
    description: str = Field(alias="Description")
    integration_id: str = Field(alias="IntegrationId")
    integration_method: str = Field(alias="IntegrationMethod")
    integration_response_selection_expression: str = Field(
        alias="IntegrationResponseSelectionExpression"
    )
    integration_subtype: str = Field(alias="IntegrationSubtype")
    integration_type: Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"] = Field(
        alias="IntegrationType"
    )
    integration_uri: str = Field(alias="IntegrationUri")
    passthrough_behavior: Literal[
        "NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"
    ] = Field(alias="PassthroughBehavior")
    payload_format_version: str = Field(alias="PayloadFormatVersion")
    request_parameters: Dict[str, str] = Field(alias="RequestParameters")
    request_templates: Dict[str, str] = Field(alias="RequestTemplates")
    response_parameters: Dict[str, Dict[str, str]] = Field(alias="ResponseParameters")
    template_selection_expression: str = Field(alias="TemplateSelectionExpression")
    timeout_in_millis: int = Field(alias="TimeoutInMillis")
    tls_config: TlsConfigModel = Field(alias="TlsConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIntegrationResultModel(BaseModel):
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    connection_id: str = Field(alias="ConnectionId")
    connection_type: Literal["INTERNET", "VPC_LINK"] = Field(alias="ConnectionType")
    content_handling_strategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="ContentHandlingStrategy"
    )
    credentials_arn: str = Field(alias="CredentialsArn")
    description: str = Field(alias="Description")
    integration_id: str = Field(alias="IntegrationId")
    integration_method: str = Field(alias="IntegrationMethod")
    integration_response_selection_expression: str = Field(
        alias="IntegrationResponseSelectionExpression"
    )
    integration_subtype: str = Field(alias="IntegrationSubtype")
    integration_type: Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"] = Field(
        alias="IntegrationType"
    )
    integration_uri: str = Field(alias="IntegrationUri")
    passthrough_behavior: Literal[
        "NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"
    ] = Field(alias="PassthroughBehavior")
    payload_format_version: str = Field(alias="PayloadFormatVersion")
    request_parameters: Dict[str, str] = Field(alias="RequestParameters")
    request_templates: Dict[str, str] = Field(alias="RequestTemplates")
    response_parameters: Dict[str, Dict[str, str]] = Field(alias="ResponseParameters")
    template_selection_expression: str = Field(alias="TemplateSelectionExpression")
    timeout_in_millis: int = Field(alias="TimeoutInMillis")
    tls_config: TlsConfigModel = Field(alias="TlsConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IntegrationModel(BaseModel):
    api_gateway_managed: Optional[bool] = Field(default=None, alias="ApiGatewayManaged")
    connection_id: Optional[str] = Field(default=None, alias="ConnectionId")
    connection_type: Optional[Literal["INTERNET", "VPC_LINK"]] = Field(
        default=None, alias="ConnectionType"
    )
    content_handling_strategy: Optional[
        Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
    ] = Field(default=None, alias="ContentHandlingStrategy")
    credentials_arn: Optional[str] = Field(default=None, alias="CredentialsArn")
    description: Optional[str] = Field(default=None, alias="Description")
    integration_id: Optional[str] = Field(default=None, alias="IntegrationId")
    integration_method: Optional[str] = Field(default=None, alias="IntegrationMethod")
    integration_response_selection_expression: Optional[str] = Field(
        default=None, alias="IntegrationResponseSelectionExpression"
    )
    integration_subtype: Optional[str] = Field(default=None, alias="IntegrationSubtype")
    integration_type: Optional[
        Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]
    ] = Field(default=None, alias="IntegrationType")
    integration_uri: Optional[str] = Field(default=None, alias="IntegrationUri")
    passthrough_behavior: Optional[
        Literal["NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"]
    ] = Field(default=None, alias="PassthroughBehavior")
    payload_format_version: Optional[str] = Field(
        default=None, alias="PayloadFormatVersion"
    )
    request_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="RequestParameters"
    )
    request_templates: Optional[Dict[str, str]] = Field(
        default=None, alias="RequestTemplates"
    )
    response_parameters: Optional[Dict[str, Dict[str, str]]] = Field(
        default=None, alias="ResponseParameters"
    )
    template_selection_expression: Optional[str] = Field(
        default=None, alias="TemplateSelectionExpression"
    )
    timeout_in_millis: Optional[int] = Field(default=None, alias="TimeoutInMillis")
    tls_config: Optional[TlsConfigModel] = Field(default=None, alias="TlsConfig")


class UpdateIntegrationResultModel(BaseModel):
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    connection_id: str = Field(alias="ConnectionId")
    connection_type: Literal["INTERNET", "VPC_LINK"] = Field(alias="ConnectionType")
    content_handling_strategy: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="ContentHandlingStrategy"
    )
    credentials_arn: str = Field(alias="CredentialsArn")
    description: str = Field(alias="Description")
    integration_id: str = Field(alias="IntegrationId")
    integration_method: str = Field(alias="IntegrationMethod")
    integration_response_selection_expression: str = Field(
        alias="IntegrationResponseSelectionExpression"
    )
    integration_subtype: str = Field(alias="IntegrationSubtype")
    integration_type: Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"] = Field(
        alias="IntegrationType"
    )
    integration_uri: str = Field(alias="IntegrationUri")
    passthrough_behavior: Literal[
        "NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"
    ] = Field(alias="PassthroughBehavior")
    payload_format_version: str = Field(alias="PayloadFormatVersion")
    request_parameters: Dict[str, str] = Field(alias="RequestParameters")
    request_templates: Dict[str, str] = Field(alias="RequestTemplates")
    response_parameters: Dict[str, Dict[str, str]] = Field(alias="ResponseParameters")
    template_selection_expression: str = Field(alias="TemplateSelectionExpression")
    timeout_in_millis: int = Field(alias="TimeoutInMillis")
    tls_config: TlsConfigModel = Field(alias="TlsConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRouteRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_key: str = Field(alias="RouteKey")
    api_key_required: Optional[bool] = Field(default=None, alias="ApiKeyRequired")
    authorization_scopes: Optional[Sequence[str]] = Field(
        default=None, alias="AuthorizationScopes"
    )
    authorization_type: Optional[Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"]] = Field(
        default=None, alias="AuthorizationType"
    )
    authorizer_id: Optional[str] = Field(default=None, alias="AuthorizerId")
    model_selection_expression: Optional[str] = Field(
        default=None, alias="ModelSelectionExpression"
    )
    operation_name: Optional[str] = Field(default=None, alias="OperationName")
    request_models: Optional[Mapping[str, str]] = Field(
        default=None, alias="RequestModels"
    )
    request_parameters: Optional[Mapping[str, ParameterConstraintsModel]] = Field(
        default=None, alias="RequestParameters"
    )
    route_response_selection_expression: Optional[str] = Field(
        default=None, alias="RouteResponseSelectionExpression"
    )
    target: Optional[str] = Field(default=None, alias="Target")


class CreateRouteResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")
    route_response_key: str = Field(alias="RouteResponseKey")
    model_selection_expression: Optional[str] = Field(
        default=None, alias="ModelSelectionExpression"
    )
    response_models: Optional[Mapping[str, str]] = Field(
        default=None, alias="ResponseModels"
    )
    response_parameters: Optional[Mapping[str, ParameterConstraintsModel]] = Field(
        default=None, alias="ResponseParameters"
    )


class CreateRouteResponseResponseModel(BaseModel):
    model_selection_expression: str = Field(alias="ModelSelectionExpression")
    response_models: Dict[str, str] = Field(alias="ResponseModels")
    response_parameters: Dict[str, ParameterConstraintsModel] = Field(
        alias="ResponseParameters"
    )
    route_response_id: str = Field(alias="RouteResponseId")
    route_response_key: str = Field(alias="RouteResponseKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRouteResultModel(BaseModel):
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_key_required: bool = Field(alias="ApiKeyRequired")
    authorization_scopes: List[str] = Field(alias="AuthorizationScopes")
    authorization_type: Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"] = Field(
        alias="AuthorizationType"
    )
    authorizer_id: str = Field(alias="AuthorizerId")
    model_selection_expression: str = Field(alias="ModelSelectionExpression")
    operation_name: str = Field(alias="OperationName")
    request_models: Dict[str, str] = Field(alias="RequestModels")
    request_parameters: Dict[str, ParameterConstraintsModel] = Field(
        alias="RequestParameters"
    )
    route_id: str = Field(alias="RouteId")
    route_key: str = Field(alias="RouteKey")
    route_response_selection_expression: str = Field(
        alias="RouteResponseSelectionExpression"
    )
    target: str = Field(alias="Target")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRouteResponseResponseModel(BaseModel):
    model_selection_expression: str = Field(alias="ModelSelectionExpression")
    response_models: Dict[str, str] = Field(alias="ResponseModels")
    response_parameters: Dict[str, ParameterConstraintsModel] = Field(
        alias="ResponseParameters"
    )
    route_response_id: str = Field(alias="RouteResponseId")
    route_response_key: str = Field(alias="RouteResponseKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRouteResultModel(BaseModel):
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_key_required: bool = Field(alias="ApiKeyRequired")
    authorization_scopes: List[str] = Field(alias="AuthorizationScopes")
    authorization_type: Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"] = Field(
        alias="AuthorizationType"
    )
    authorizer_id: str = Field(alias="AuthorizerId")
    model_selection_expression: str = Field(alias="ModelSelectionExpression")
    operation_name: str = Field(alias="OperationName")
    request_models: Dict[str, str] = Field(alias="RequestModels")
    request_parameters: Dict[str, ParameterConstraintsModel] = Field(
        alias="RequestParameters"
    )
    route_id: str = Field(alias="RouteId")
    route_key: str = Field(alias="RouteKey")
    route_response_selection_expression: str = Field(
        alias="RouteResponseSelectionExpression"
    )
    target: str = Field(alias="Target")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RouteResponseModel(BaseModel):
    route_response_key: str = Field(alias="RouteResponseKey")
    model_selection_expression: Optional[str] = Field(
        default=None, alias="ModelSelectionExpression"
    )
    response_models: Optional[Dict[str, str]] = Field(
        default=None, alias="ResponseModels"
    )
    response_parameters: Optional[Dict[str, ParameterConstraintsModel]] = Field(
        default=None, alias="ResponseParameters"
    )
    route_response_id: Optional[str] = Field(default=None, alias="RouteResponseId")


class RouteModel(BaseModel):
    route_key: str = Field(alias="RouteKey")
    api_gateway_managed: Optional[bool] = Field(default=None, alias="ApiGatewayManaged")
    api_key_required: Optional[bool] = Field(default=None, alias="ApiKeyRequired")
    authorization_scopes: Optional[List[str]] = Field(
        default=None, alias="AuthorizationScopes"
    )
    authorization_type: Optional[Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"]] = Field(
        default=None, alias="AuthorizationType"
    )
    authorizer_id: Optional[str] = Field(default=None, alias="AuthorizerId")
    model_selection_expression: Optional[str] = Field(
        default=None, alias="ModelSelectionExpression"
    )
    operation_name: Optional[str] = Field(default=None, alias="OperationName")
    request_models: Optional[Dict[str, str]] = Field(
        default=None, alias="RequestModels"
    )
    request_parameters: Optional[Dict[str, ParameterConstraintsModel]] = Field(
        default=None, alias="RequestParameters"
    )
    route_id: Optional[str] = Field(default=None, alias="RouteId")
    route_response_selection_expression: Optional[str] = Field(
        default=None, alias="RouteResponseSelectionExpression"
    )
    target: Optional[str] = Field(default=None, alias="Target")


class UpdateRouteRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")
    api_key_required: Optional[bool] = Field(default=None, alias="ApiKeyRequired")
    authorization_scopes: Optional[Sequence[str]] = Field(
        default=None, alias="AuthorizationScopes"
    )
    authorization_type: Optional[Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"]] = Field(
        default=None, alias="AuthorizationType"
    )
    authorizer_id: Optional[str] = Field(default=None, alias="AuthorizerId")
    model_selection_expression: Optional[str] = Field(
        default=None, alias="ModelSelectionExpression"
    )
    operation_name: Optional[str] = Field(default=None, alias="OperationName")
    request_models: Optional[Mapping[str, str]] = Field(
        default=None, alias="RequestModels"
    )
    request_parameters: Optional[Mapping[str, ParameterConstraintsModel]] = Field(
        default=None, alias="RequestParameters"
    )
    route_key: Optional[str] = Field(default=None, alias="RouteKey")
    route_response_selection_expression: Optional[str] = Field(
        default=None, alias="RouteResponseSelectionExpression"
    )
    target: Optional[str] = Field(default=None, alias="Target")


class UpdateRouteResponseRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")
    route_response_id: str = Field(alias="RouteResponseId")
    model_selection_expression: Optional[str] = Field(
        default=None, alias="ModelSelectionExpression"
    )
    response_models: Optional[Mapping[str, str]] = Field(
        default=None, alias="ResponseModels"
    )
    response_parameters: Optional[Mapping[str, ParameterConstraintsModel]] = Field(
        default=None, alias="ResponseParameters"
    )
    route_response_key: Optional[str] = Field(default=None, alias="RouteResponseKey")


class UpdateRouteResponseResponseModel(BaseModel):
    model_selection_expression: str = Field(alias="ModelSelectionExpression")
    response_models: Dict[str, str] = Field(alias="ResponseModels")
    response_parameters: Dict[str, ParameterConstraintsModel] = Field(
        alias="ResponseParameters"
    )
    route_response_id: str = Field(alias="RouteResponseId")
    route_response_key: str = Field(alias="RouteResponseKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRouteResultModel(BaseModel):
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    api_key_required: bool = Field(alias="ApiKeyRequired")
    authorization_scopes: List[str] = Field(alias="AuthorizationScopes")
    authorization_type: Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"] = Field(
        alias="AuthorizationType"
    )
    authorizer_id: str = Field(alias="AuthorizerId")
    model_selection_expression: str = Field(alias="ModelSelectionExpression")
    operation_name: str = Field(alias="OperationName")
    request_models: Dict[str, str] = Field(alias="RequestModels")
    request_parameters: Dict[str, ParameterConstraintsModel] = Field(
        alias="RequestParameters"
    )
    route_id: str = Field(alias="RouteId")
    route_key: str = Field(alias="RouteKey")
    route_response_selection_expression: str = Field(
        alias="RouteResponseSelectionExpression"
    )
    target: str = Field(alias="Target")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStageRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    stage_name: str = Field(alias="StageName")
    access_log_settings: Optional[AccessLogSettingsModel] = Field(
        default=None, alias="AccessLogSettings"
    )
    auto_deploy: Optional[bool] = Field(default=None, alias="AutoDeploy")
    client_certificate_id: Optional[str] = Field(
        default=None, alias="ClientCertificateId"
    )
    default_route_settings: Optional[RouteSettingsModel] = Field(
        default=None, alias="DefaultRouteSettings"
    )
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    description: Optional[str] = Field(default=None, alias="Description")
    route_settings: Optional[Mapping[str, RouteSettingsModel]] = Field(
        default=None, alias="RouteSettings"
    )
    stage_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="StageVariables"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateStageResponseModel(BaseModel):
    access_log_settings: AccessLogSettingsModel = Field(alias="AccessLogSettings")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    auto_deploy: bool = Field(alias="AutoDeploy")
    client_certificate_id: str = Field(alias="ClientCertificateId")
    created_date: datetime = Field(alias="CreatedDate")
    default_route_settings: RouteSettingsModel = Field(alias="DefaultRouteSettings")
    deployment_id: str = Field(alias="DeploymentId")
    description: str = Field(alias="Description")
    last_deployment_status_message: str = Field(alias="LastDeploymentStatusMessage")
    last_updated_date: datetime = Field(alias="LastUpdatedDate")
    route_settings: Dict[str, RouteSettingsModel] = Field(alias="RouteSettings")
    stage_name: str = Field(alias="StageName")
    stage_variables: Dict[str, str] = Field(alias="StageVariables")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStageResponseModel(BaseModel):
    access_log_settings: AccessLogSettingsModel = Field(alias="AccessLogSettings")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    auto_deploy: bool = Field(alias="AutoDeploy")
    client_certificate_id: str = Field(alias="ClientCertificateId")
    created_date: datetime = Field(alias="CreatedDate")
    default_route_settings: RouteSettingsModel = Field(alias="DefaultRouteSettings")
    deployment_id: str = Field(alias="DeploymentId")
    description: str = Field(alias="Description")
    last_deployment_status_message: str = Field(alias="LastDeploymentStatusMessage")
    last_updated_date: datetime = Field(alias="LastUpdatedDate")
    route_settings: Dict[str, RouteSettingsModel] = Field(alias="RouteSettings")
    stage_name: str = Field(alias="StageName")
    stage_variables: Dict[str, str] = Field(alias="StageVariables")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StageModel(BaseModel):
    stage_name: str = Field(alias="StageName")
    access_log_settings: Optional[AccessLogSettingsModel] = Field(
        default=None, alias="AccessLogSettings"
    )
    api_gateway_managed: Optional[bool] = Field(default=None, alias="ApiGatewayManaged")
    auto_deploy: Optional[bool] = Field(default=None, alias="AutoDeploy")
    client_certificate_id: Optional[str] = Field(
        default=None, alias="ClientCertificateId"
    )
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    default_route_settings: Optional[RouteSettingsModel] = Field(
        default=None, alias="DefaultRouteSettings"
    )
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    description: Optional[str] = Field(default=None, alias="Description")
    last_deployment_status_message: Optional[str] = Field(
        default=None, alias="LastDeploymentStatusMessage"
    )
    last_updated_date: Optional[datetime] = Field(default=None, alias="LastUpdatedDate")
    route_settings: Optional[Dict[str, RouteSettingsModel]] = Field(
        default=None, alias="RouteSettings"
    )
    stage_variables: Optional[Dict[str, str]] = Field(
        default=None, alias="StageVariables"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class UpdateStageRequestModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    stage_name: str = Field(alias="StageName")
    access_log_settings: Optional[AccessLogSettingsModel] = Field(
        default=None, alias="AccessLogSettings"
    )
    auto_deploy: Optional[bool] = Field(default=None, alias="AutoDeploy")
    client_certificate_id: Optional[str] = Field(
        default=None, alias="ClientCertificateId"
    )
    default_route_settings: Optional[RouteSettingsModel] = Field(
        default=None, alias="DefaultRouteSettings"
    )
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    description: Optional[str] = Field(default=None, alias="Description")
    route_settings: Optional[Mapping[str, RouteSettingsModel]] = Field(
        default=None, alias="RouteSettings"
    )
    stage_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="StageVariables"
    )


class UpdateStageResponseModel(BaseModel):
    access_log_settings: AccessLogSettingsModel = Field(alias="AccessLogSettings")
    api_gateway_managed: bool = Field(alias="ApiGatewayManaged")
    auto_deploy: bool = Field(alias="AutoDeploy")
    client_certificate_id: str = Field(alias="ClientCertificateId")
    created_date: datetime = Field(alias="CreatedDate")
    default_route_settings: RouteSettingsModel = Field(alias="DefaultRouteSettings")
    deployment_id: str = Field(alias="DeploymentId")
    description: str = Field(alias="Description")
    last_deployment_status_message: str = Field(alias="LastDeploymentStatusMessage")
    last_updated_date: datetime = Field(alias="LastUpdatedDate")
    route_settings: Dict[str, RouteSettingsModel] = Field(alias="RouteSettings")
    stage_name: str = Field(alias="StageName")
    stage_variables: Dict[str, str] = Field(alias="StageVariables")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentsResponseModel(BaseModel):
    items: List[DeploymentModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApisRequestGetApisPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAuthorizersRequestGetAuthorizersPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDeploymentsRequestGetDeploymentsPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDomainNamesRequestGetDomainNamesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetIntegrationResponsesRequestGetIntegrationResponsesPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    integration_id: str = Field(alias="IntegrationId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetIntegrationsRequestGetIntegrationsPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetModelsRequestGetModelsPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRouteResponsesRequestGetRouteResponsesPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    route_id: str = Field(alias="RouteId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRoutesRequestGetRoutesPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetStagesRequestGetStagesPaginateModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetIntegrationResponsesResponseModel(BaseModel):
    items: List[IntegrationResponseModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetModelsResponseModel(BaseModel):
    items: List[ModelModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVpcLinksResponseModel(BaseModel):
    items: List[VpcLinkModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApisResponseModel(BaseModel):
    items: List[ApiModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAuthorizersResponseModel(BaseModel):
    items: List[AuthorizerModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainNamesResponseModel(BaseModel):
    items: List[DomainNameModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIntegrationsResponseModel(BaseModel):
    items: List[IntegrationModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRouteResponsesResponseModel(BaseModel):
    items: List[RouteResponseModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRoutesResponseModel(BaseModel):
    items: List[RouteModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStagesResponseModel(BaseModel):
    items: List[StageModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
