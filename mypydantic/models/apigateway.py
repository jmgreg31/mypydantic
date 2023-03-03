# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessLogSettingsModel(BaseModel):
    format: Optional[str] = Field(default=None, alias="format")
    destination_arn: Optional[str] = Field(default=None, alias="destinationArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ThrottleSettingsModel(BaseModel):
    burst_limit: Optional[int] = Field(default=None, alias="burstLimit")
    rate_limit: Optional[float] = Field(default=None, alias="rateLimit")


class ApiKeyModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    value: Optional[str] = Field(default=None, alias="value")
    name: Optional[str] = Field(default=None, alias="name")
    customer_id: Optional[str] = Field(default=None, alias="customerId")
    description: Optional[str] = Field(default=None, alias="description")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    last_updated_date: Optional[datetime] = Field(default=None, alias="lastUpdatedDate")
    stage_keys: Optional[List[str]] = Field(default=None, alias="stageKeys")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class AuthorizerModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["COGNITO_USER_POOLS", "REQUEST", "TOKEN"]] = Field(
        default=None, alias="type"
    )
    provider_arns: Optional[List[str]] = Field(default=None, alias="providerARNs")
    auth_type: Optional[str] = Field(default=None, alias="authType")
    authorizer_uri: Optional[str] = Field(default=None, alias="authorizerUri")
    authorizer_credentials: Optional[str] = Field(
        default=None, alias="authorizerCredentials"
    )
    identity_source: Optional[str] = Field(default=None, alias="identitySource")
    identity_validation_expression: Optional[str] = Field(
        default=None, alias="identityValidationExpression"
    )
    authorizer_result_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="authorizerResultTtlInSeconds"
    )


class BasePathMappingModel(BaseModel):
    base_path: Optional[str] = Field(default=None, alias="basePath")
    rest_api_id: Optional[str] = Field(default=None, alias="restApiId")
    stage: Optional[str] = Field(default=None, alias="stage")


class CanarySettingsModel(BaseModel):
    percent_traffic: Optional[float] = Field(default=None, alias="percentTraffic")
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    stage_variable_overrides: Optional[Mapping[str, str]] = Field(
        default=None, alias="stageVariableOverrides"
    )
    use_stage_cache: Optional[bool] = Field(default=None, alias="useStageCache")


class ClientCertificateModel(BaseModel):
    client_certificate_id: Optional[str] = Field(
        default=None, alias="clientCertificateId"
    )
    description: Optional[str] = Field(default=None, alias="description")
    pem_encoded_certificate: Optional[str] = Field(
        default=None, alias="pemEncodedCertificate"
    )
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    expiration_date: Optional[datetime] = Field(default=None, alias="expirationDate")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class StageKeyModel(BaseModel):
    rest_api_id: Optional[str] = Field(default=None, alias="restApiId")
    stage_name: Optional[str] = Field(default=None, alias="stageName")


class CreateAuthorizerRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    name: str = Field(alias="name")
    type: Literal["COGNITO_USER_POOLS", "REQUEST", "TOKEN"] = Field(alias="type")
    provider_arns: Optional[Sequence[str]] = Field(default=None, alias="providerARNs")
    auth_type: Optional[str] = Field(default=None, alias="authType")
    authorizer_uri: Optional[str] = Field(default=None, alias="authorizerUri")
    authorizer_credentials: Optional[str] = Field(
        default=None, alias="authorizerCredentials"
    )
    identity_source: Optional[str] = Field(default=None, alias="identitySource")
    identity_validation_expression: Optional[str] = Field(
        default=None, alias="identityValidationExpression"
    )
    authorizer_result_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="authorizerResultTtlInSeconds"
    )


class CreateBasePathMappingRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    rest_api_id: str = Field(alias="restApiId")
    base_path: Optional[str] = Field(default=None, alias="basePath")
    stage: Optional[str] = Field(default=None, alias="stage")


class DeploymentCanarySettingsModel(BaseModel):
    percent_traffic: Optional[float] = Field(default=None, alias="percentTraffic")
    stage_variable_overrides: Optional[Mapping[str, str]] = Field(
        default=None, alias="stageVariableOverrides"
    )
    use_stage_cache: Optional[bool] = Field(default=None, alias="useStageCache")


class DocumentationPartLocationModel(BaseModel):
    type: Literal[
        "API",
        "AUTHORIZER",
        "METHOD",
        "MODEL",
        "PATH_PARAMETER",
        "QUERY_PARAMETER",
        "REQUEST_BODY",
        "REQUEST_HEADER",
        "RESOURCE",
        "RESPONSE",
        "RESPONSE_BODY",
        "RESPONSE_HEADER",
    ] = Field(alias="type")
    path: Optional[str] = Field(default=None, alias="path")
    method: Optional[str] = Field(default=None, alias="method")
    status_code: Optional[str] = Field(default=None, alias="statusCode")
    name: Optional[str] = Field(default=None, alias="name")


class CreateDocumentationVersionRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    documentation_version: str = Field(alias="documentationVersion")
    stage_name: Optional[str] = Field(default=None, alias="stageName")
    description: Optional[str] = Field(default=None, alias="description")


class EndpointConfigurationModel(BaseModel):
    types: Optional[Sequence[Literal["EDGE", "PRIVATE", "REGIONAL"]]] = Field(
        default=None, alias="types"
    )
    vpc_endpoint_ids: Optional[Sequence[str]] = Field(
        default=None, alias="vpcEndpointIds"
    )


class MutualTlsAuthenticationInputModel(BaseModel):
    truststore_uri: Optional[str] = Field(default=None, alias="truststoreUri")
    truststore_version: Optional[str] = Field(default=None, alias="truststoreVersion")


class CreateModelRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    name: str = Field(alias="name")
    content_type: str = Field(alias="contentType")
    description: Optional[str] = Field(default=None, alias="description")
    schema_: Optional[str] = Field(default=None, alias="schema")


class CreateRequestValidatorRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    name: Optional[str] = Field(default=None, alias="name")
    validate_request_body: Optional[bool] = Field(
        default=None, alias="validateRequestBody"
    )
    validate_request_parameters: Optional[bool] = Field(
        default=None, alias="validateRequestParameters"
    )


class CreateResourceRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    parent_id: str = Field(alias="parentId")
    path_part: str = Field(alias="pathPart")


class CreateUsagePlanKeyRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    key_id: str = Field(alias="keyId")
    key_type: str = Field(alias="keyType")


class QuotaSettingsModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="limit")
    offset: Optional[int] = Field(default=None, alias="offset")
    period: Optional[Literal["DAY", "MONTH", "WEEK"]] = Field(
        default=None, alias="period"
    )


class CreateVpcLinkRequestModel(BaseModel):
    name: str = Field(alias="name")
    target_arns: Sequence[str] = Field(alias="targetArns")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DeleteApiKeyRequestModel(BaseModel):
    api_key: str = Field(alias="apiKey")


class DeleteAuthorizerRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    authorizer_id: str = Field(alias="authorizerId")


class DeleteBasePathMappingRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    base_path: str = Field(alias="basePath")


class DeleteClientCertificateRequestModel(BaseModel):
    client_certificate_id: str = Field(alias="clientCertificateId")


class DeleteDeploymentRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    deployment_id: str = Field(alias="deploymentId")


class DeleteDocumentationPartRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    documentation_part_id: str = Field(alias="documentationPartId")


class DeleteDocumentationVersionRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    documentation_version: str = Field(alias="documentationVersion")


class DeleteDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class DeleteGatewayResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    response_type: Literal[
        "ACCESS_DENIED",
        "API_CONFIGURATION_ERROR",
        "AUTHORIZER_CONFIGURATION_ERROR",
        "AUTHORIZER_FAILURE",
        "BAD_REQUEST_BODY",
        "BAD_REQUEST_PARAMETERS",
        "DEFAULT_4XX",
        "DEFAULT_5XX",
        "EXPIRED_TOKEN",
        "INTEGRATION_FAILURE",
        "INTEGRATION_TIMEOUT",
        "INVALID_API_KEY",
        "INVALID_SIGNATURE",
        "MISSING_AUTHENTICATION_TOKEN",
        "QUOTA_EXCEEDED",
        "REQUEST_TOO_LARGE",
        "RESOURCE_NOT_FOUND",
        "THROTTLED",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE",
        "WAF_FILTERED",
    ] = Field(alias="responseType")


class DeleteIntegrationRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")


class DeleteIntegrationResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")


class DeleteMethodRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")


class DeleteMethodResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")


class DeleteModelRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    model_name: str = Field(alias="modelName")


class DeleteRequestValidatorRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    request_validator_id: str = Field(alias="requestValidatorId")


class DeleteResourceRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")


class DeleteRestApiRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")


class DeleteStageRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")


class DeleteUsagePlanKeyRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    key_id: str = Field(alias="keyId")


class DeleteUsagePlanRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")


class DeleteVpcLinkRequestModel(BaseModel):
    vpc_link_id: str = Field(alias="vpcLinkId")


class MethodSnapshotModel(BaseModel):
    authorization_type: Optional[str] = Field(default=None, alias="authorizationType")
    api_key_required: Optional[bool] = Field(default=None, alias="apiKeyRequired")


class DocumentationVersionModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="version")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")


class MutualTlsAuthenticationModel(BaseModel):
    truststore_uri: Optional[str] = Field(default=None, alias="truststoreUri")
    truststore_version: Optional[str] = Field(default=None, alias="truststoreVersion")
    truststore_warnings: Optional[List[str]] = Field(
        default=None, alias="truststoreWarnings"
    )


class FlushStageAuthorizersCacheRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")


class FlushStageCacheRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")


class GatewayResponseModel(BaseModel):
    response_type: Optional[
        Literal[
            "ACCESS_DENIED",
            "API_CONFIGURATION_ERROR",
            "AUTHORIZER_CONFIGURATION_ERROR",
            "AUTHORIZER_FAILURE",
            "BAD_REQUEST_BODY",
            "BAD_REQUEST_PARAMETERS",
            "DEFAULT_4XX",
            "DEFAULT_5XX",
            "EXPIRED_TOKEN",
            "INTEGRATION_FAILURE",
            "INTEGRATION_TIMEOUT",
            "INVALID_API_KEY",
            "INVALID_SIGNATURE",
            "MISSING_AUTHENTICATION_TOKEN",
            "QUOTA_EXCEEDED",
            "REQUEST_TOO_LARGE",
            "RESOURCE_NOT_FOUND",
            "THROTTLED",
            "UNAUTHORIZED",
            "UNSUPPORTED_MEDIA_TYPE",
            "WAF_FILTERED",
        ]
    ] = Field(default=None, alias="responseType")
    status_code: Optional[str] = Field(default=None, alias="statusCode")
    response_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="responseParameters"
    )
    response_templates: Optional[Dict[str, str]] = Field(
        default=None, alias="responseTemplates"
    )
    default_response: Optional[bool] = Field(default=None, alias="defaultResponse")


class GenerateClientCertificateRequestModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetApiKeyRequestModel(BaseModel):
    api_key: str = Field(alias="apiKey")
    include_value: Optional[bool] = Field(default=None, alias="includeValue")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetApiKeysRequestModel(BaseModel):
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")
    name_query: Optional[str] = Field(default=None, alias="nameQuery")
    customer_id: Optional[str] = Field(default=None, alias="customerId")
    include_values: Optional[bool] = Field(default=None, alias="includeValues")


class GetAuthorizerRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    authorizer_id: str = Field(alias="authorizerId")


class GetAuthorizersRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetBasePathMappingRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    base_path: str = Field(alias="basePath")


class GetBasePathMappingsRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetClientCertificateRequestModel(BaseModel):
    client_certificate_id: str = Field(alias="clientCertificateId")


class GetClientCertificatesRequestModel(BaseModel):
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetDeploymentRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    deployment_id: str = Field(alias="deploymentId")
    embed: Optional[Sequence[str]] = Field(default=None, alias="embed")


class GetDeploymentsRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetDocumentationPartRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    documentation_part_id: str = Field(alias="documentationPartId")


class GetDocumentationPartsRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    type: Optional[
        Literal[
            "API",
            "AUTHORIZER",
            "METHOD",
            "MODEL",
            "PATH_PARAMETER",
            "QUERY_PARAMETER",
            "REQUEST_BODY",
            "REQUEST_HEADER",
            "RESOURCE",
            "RESPONSE",
            "RESPONSE_BODY",
            "RESPONSE_HEADER",
        ]
    ] = Field(default=None, alias="type")
    name_query: Optional[str] = Field(default=None, alias="nameQuery")
    path: Optional[str] = Field(default=None, alias="path")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")
    location_status: Optional[Literal["DOCUMENTED", "UNDOCUMENTED"]] = Field(
        default=None, alias="locationStatus"
    )


class GetDocumentationVersionRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    documentation_version: str = Field(alias="documentationVersion")


class GetDocumentationVersionsRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class GetDomainNamesRequestModel(BaseModel):
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetExportRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")
    export_type: str = Field(alias="exportType")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")
    accepts: Optional[str] = Field(default=None, alias="accepts")


class GetGatewayResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    response_type: Literal[
        "ACCESS_DENIED",
        "API_CONFIGURATION_ERROR",
        "AUTHORIZER_CONFIGURATION_ERROR",
        "AUTHORIZER_FAILURE",
        "BAD_REQUEST_BODY",
        "BAD_REQUEST_PARAMETERS",
        "DEFAULT_4XX",
        "DEFAULT_5XX",
        "EXPIRED_TOKEN",
        "INTEGRATION_FAILURE",
        "INTEGRATION_TIMEOUT",
        "INVALID_API_KEY",
        "INVALID_SIGNATURE",
        "MISSING_AUTHENTICATION_TOKEN",
        "QUOTA_EXCEEDED",
        "REQUEST_TOO_LARGE",
        "RESOURCE_NOT_FOUND",
        "THROTTLED",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE",
        "WAF_FILTERED",
    ] = Field(alias="responseType")


class GetGatewayResponsesRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetIntegrationRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")


class GetIntegrationResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")


class GetMethodRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")


class GetMethodResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")


class GetModelRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    model_name: str = Field(alias="modelName")
    flatten: Optional[bool] = Field(default=None, alias="flatten")


class GetModelTemplateRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    model_name: str = Field(alias="modelName")


class GetModelsRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetRequestValidatorRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    request_validator_id: str = Field(alias="requestValidatorId")


class GetRequestValidatorsRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetResourceRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    embed: Optional[Sequence[str]] = Field(default=None, alias="embed")


class GetResourcesRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")
    embed: Optional[Sequence[str]] = Field(default=None, alias="embed")


class GetRestApiRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")


class GetRestApisRequestModel(BaseModel):
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetSdkRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")
    sdk_type: str = Field(alias="sdkType")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")


class GetSdkTypeRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetSdkTypesRequestModel(BaseModel):
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetStageRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")


class GetStagesRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")


class GetTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetUsagePlanKeyRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    key_id: str = Field(alias="keyId")


class GetUsagePlanKeysRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")
    name_query: Optional[str] = Field(default=None, alias="nameQuery")


class GetUsagePlanRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")


class GetUsagePlansRequestModel(BaseModel):
    position: Optional[str] = Field(default=None, alias="position")
    key_id: Optional[str] = Field(default=None, alias="keyId")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetUsageRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    key_id: Optional[str] = Field(default=None, alias="keyId")
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class GetVpcLinkRequestModel(BaseModel):
    vpc_link_id: str = Field(alias="vpcLinkId")


class GetVpcLinksRequestModel(BaseModel):
    position: Optional[str] = Field(default=None, alias="position")
    limit: Optional[int] = Field(default=None, alias="limit")


class ImportApiKeysRequestModel(BaseModel):
    body: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="body")
    format: Literal["csv"] = Field(alias="format")
    fail_on_warnings: Optional[bool] = Field(default=None, alias="failOnWarnings")


class ImportDocumentationPartsRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    body: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="body")
    mode: Optional[Literal["merge", "overwrite"]] = Field(default=None, alias="mode")
    fail_on_warnings: Optional[bool] = Field(default=None, alias="failOnWarnings")


class ImportRestApiRequestModel(BaseModel):
    body: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="body")
    fail_on_warnings: Optional[bool] = Field(default=None, alias="failOnWarnings")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")


class IntegrationResponseModel(BaseModel):
    status_code: Optional[str] = Field(default=None, alias="statusCode")
    selection_pattern: Optional[str] = Field(default=None, alias="selectionPattern")
    response_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="responseParameters"
    )
    response_templates: Optional[Dict[str, str]] = Field(
        default=None, alias="responseTemplates"
    )
    content_handling: Optional[Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]] = Field(
        default=None, alias="contentHandling"
    )


class TlsConfigModel(BaseModel):
    insecure_skip_verification: Optional[bool] = Field(
        default=None, alias="insecureSkipVerification"
    )


class MethodResponseModel(BaseModel):
    status_code: Optional[str] = Field(default=None, alias="statusCode")
    response_parameters: Optional[Dict[str, bool]] = Field(
        default=None, alias="responseParameters"
    )
    response_models: Optional[Dict[str, str]] = Field(
        default=None, alias="responseModels"
    )


class MethodSettingModel(BaseModel):
    metrics_enabled: Optional[bool] = Field(default=None, alias="metricsEnabled")
    logging_level: Optional[str] = Field(default=None, alias="loggingLevel")
    data_trace_enabled: Optional[bool] = Field(default=None, alias="dataTraceEnabled")
    throttling_burst_limit: Optional[int] = Field(
        default=None, alias="throttlingBurstLimit"
    )
    throttling_rate_limit: Optional[float] = Field(
        default=None, alias="throttlingRateLimit"
    )
    caching_enabled: Optional[bool] = Field(default=None, alias="cachingEnabled")
    cache_ttl_in_seconds: Optional[int] = Field(default=None, alias="cacheTtlInSeconds")
    cache_data_encrypted: Optional[bool] = Field(
        default=None, alias="cacheDataEncrypted"
    )
    require_authorization_for_cache_control: Optional[bool] = Field(
        default=None, alias="requireAuthorizationForCacheControl"
    )
    unauthorized_cache_control_header_strategy: Optional[
        Literal[
            "FAIL_WITH_403",
            "SUCCEED_WITHOUT_RESPONSE_HEADER",
            "SUCCEED_WITH_RESPONSE_HEADER",
        ]
    ] = Field(default=None, alias="unauthorizedCacheControlHeaderStrategy")


class ModelModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    schema_: Optional[str] = Field(default=None, alias="schema")
    content_type: Optional[str] = Field(default=None, alias="contentType")


class PatchOperationModel(BaseModel):
    op: Optional[Literal["add", "copy", "move", "remove", "replace", "test"]] = Field(
        default=None, alias="op"
    )
    path: Optional[str] = Field(default=None, alias="path")
    value: Optional[str] = Field(default=None, alias="value")
    from_: Optional[str] = Field(default=None, alias="from")


class PutGatewayResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    response_type: Literal[
        "ACCESS_DENIED",
        "API_CONFIGURATION_ERROR",
        "AUTHORIZER_CONFIGURATION_ERROR",
        "AUTHORIZER_FAILURE",
        "BAD_REQUEST_BODY",
        "BAD_REQUEST_PARAMETERS",
        "DEFAULT_4XX",
        "DEFAULT_5XX",
        "EXPIRED_TOKEN",
        "INTEGRATION_FAILURE",
        "INTEGRATION_TIMEOUT",
        "INVALID_API_KEY",
        "INVALID_SIGNATURE",
        "MISSING_AUTHENTICATION_TOKEN",
        "QUOTA_EXCEEDED",
        "REQUEST_TOO_LARGE",
        "RESOURCE_NOT_FOUND",
        "THROTTLED",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE",
        "WAF_FILTERED",
    ] = Field(alias="responseType")
    status_code: Optional[str] = Field(default=None, alias="statusCode")
    response_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="responseParameters"
    )
    response_templates: Optional[Mapping[str, str]] = Field(
        default=None, alias="responseTemplates"
    )


class PutIntegrationResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")
    selection_pattern: Optional[str] = Field(default=None, alias="selectionPattern")
    response_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="responseParameters"
    )
    response_templates: Optional[Mapping[str, str]] = Field(
        default=None, alias="responseTemplates"
    )
    content_handling: Optional[Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]] = Field(
        default=None, alias="contentHandling"
    )


class PutMethodRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    authorization_type: str = Field(alias="authorizationType")
    authorizer_id: Optional[str] = Field(default=None, alias="authorizerId")
    api_key_required: Optional[bool] = Field(default=None, alias="apiKeyRequired")
    operation_name: Optional[str] = Field(default=None, alias="operationName")
    request_parameters: Optional[Mapping[str, bool]] = Field(
        default=None, alias="requestParameters"
    )
    request_models: Optional[Mapping[str, str]] = Field(
        default=None, alias="requestModels"
    )
    request_validator_id: Optional[str] = Field(
        default=None, alias="requestValidatorId"
    )
    authorization_scopes: Optional[Sequence[str]] = Field(
        default=None, alias="authorizationScopes"
    )


class PutMethodResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")
    response_parameters: Optional[Mapping[str, bool]] = Field(
        default=None, alias="responseParameters"
    )
    response_models: Optional[Mapping[str, str]] = Field(
        default=None, alias="responseModels"
    )


class PutRestApiRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    body: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="body")
    mode: Optional[Literal["merge", "overwrite"]] = Field(default=None, alias="mode")
    fail_on_warnings: Optional[bool] = Field(default=None, alias="failOnWarnings")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")


class RequestValidatorModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    validate_request_body: Optional[bool] = Field(
        default=None, alias="validateRequestBody"
    )
    validate_request_parameters: Optional[bool] = Field(
        default=None, alias="validateRequestParameters"
    )


class SdkConfigurationPropertyModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    friendly_name: Optional[str] = Field(default=None, alias="friendlyName")
    description: Optional[str] = Field(default=None, alias="description")
    required: Optional[bool] = Field(default=None, alias="required")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TestInvokeAuthorizerRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    authorizer_id: str = Field(alias="authorizerId")
    headers: Optional[Mapping[str, str]] = Field(default=None, alias="headers")
    multi_value_headers: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="multiValueHeaders"
    )
    path_with_query_string: Optional[str] = Field(
        default=None, alias="pathWithQueryString"
    )
    body: Optional[str] = Field(default=None, alias="body")
    stage_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="stageVariables"
    )
    additional_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="additionalContext"
    )


class TestInvokeMethodRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    path_with_query_string: Optional[str] = Field(
        default=None, alias="pathWithQueryString"
    )
    body: Optional[str] = Field(default=None, alias="body")
    headers: Optional[Mapping[str, str]] = Field(default=None, alias="headers")
    multi_value_headers: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="multiValueHeaders"
    )
    client_certificate_id: Optional[str] = Field(
        default=None, alias="clientCertificateId"
    )
    stage_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="stageVariables"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UsagePlanKeyModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    type: Optional[str] = Field(default=None, alias="type")
    value: Optional[str] = Field(default=None, alias="value")
    name: Optional[str] = Field(default=None, alias="name")


class VpcLinkModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    target_arns: Optional[List[str]] = Field(default=None, alias="targetArns")
    status: Optional[Literal["AVAILABLE", "DELETING", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ApiKeyIdsModel(BaseModel):
    ids: List[str] = Field(alias="ids")
    warnings: List[str] = Field(alias="warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApiKeyResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    value: str = Field(alias="value")
    name: str = Field(alias="name")
    customer_id: str = Field(alias="customerId")
    description: str = Field(alias="description")
    enabled: bool = Field(alias="enabled")
    created_date: datetime = Field(alias="createdDate")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    stage_keys: List[str] = Field(alias="stageKeys")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthorizerResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    type: Literal["COGNITO_USER_POOLS", "REQUEST", "TOKEN"] = Field(alias="type")
    provider_arns: List[str] = Field(alias="providerARNs")
    auth_type: str = Field(alias="authType")
    authorizer_uri: str = Field(alias="authorizerUri")
    authorizer_credentials: str = Field(alias="authorizerCredentials")
    identity_source: str = Field(alias="identitySource")
    identity_validation_expression: str = Field(alias="identityValidationExpression")
    authorizer_result_ttl_in_seconds: int = Field(alias="authorizerResultTtlInSeconds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BasePathMappingResponseMetadataModel(BaseModel):
    base_path: str = Field(alias="basePath")
    rest_api_id: str = Field(alias="restApiId")
    stage: str = Field(alias="stage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClientCertificateResponseMetadataModel(BaseModel):
    client_certificate_id: str = Field(alias="clientCertificateId")
    description: str = Field(alias="description")
    pem_encoded_certificate: str = Field(alias="pemEncodedCertificate")
    created_date: datetime = Field(alias="createdDate")
    expiration_date: datetime = Field(alias="expirationDate")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentationPartIdsModel(BaseModel):
    ids: List[str] = Field(alias="ids")
    warnings: List[str] = Field(alias="warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentationVersionResponseMetadataModel(BaseModel):
    version: str = Field(alias="version")
    created_date: datetime = Field(alias="createdDate")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportResponseModel(BaseModel):
    content_type: str = Field(alias="contentType")
    content_disposition: str = Field(alias="contentDisposition")
    body: Type[StreamingBody] = Field(alias="body")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GatewayResponseResponseMetadataModel(BaseModel):
    response_type: Literal[
        "ACCESS_DENIED",
        "API_CONFIGURATION_ERROR",
        "AUTHORIZER_CONFIGURATION_ERROR",
        "AUTHORIZER_FAILURE",
        "BAD_REQUEST_BODY",
        "BAD_REQUEST_PARAMETERS",
        "DEFAULT_4XX",
        "DEFAULT_5XX",
        "EXPIRED_TOKEN",
        "INTEGRATION_FAILURE",
        "INTEGRATION_TIMEOUT",
        "INVALID_API_KEY",
        "INVALID_SIGNATURE",
        "MISSING_AUTHENTICATION_TOKEN",
        "QUOTA_EXCEEDED",
        "REQUEST_TOO_LARGE",
        "RESOURCE_NOT_FOUND",
        "THROTTLED",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE",
        "WAF_FILTERED",
    ] = Field(alias="responseType")
    status_code: str = Field(alias="statusCode")
    response_parameters: Dict[str, str] = Field(alias="responseParameters")
    response_templates: Dict[str, str] = Field(alias="responseTemplates")
    default_response: bool = Field(alias="defaultResponse")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IntegrationResponseResponseMetadataModel(BaseModel):
    status_code: str = Field(alias="statusCode")
    selection_pattern: str = Field(alias="selectionPattern")
    response_parameters: Dict[str, str] = Field(alias="responseParameters")
    response_templates: Dict[str, str] = Field(alias="responseTemplates")
    content_handling: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="contentHandling"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MethodResponseResponseMetadataModel(BaseModel):
    status_code: str = Field(alias="statusCode")
    response_parameters: Dict[str, bool] = Field(alias="responseParameters")
    response_models: Dict[str, str] = Field(alias="responseModels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModelResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    schema_: str = Field(alias="schema")
    content_type: str = Field(alias="contentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestValidatorResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    validate_request_body: bool = Field(alias="validateRequestBody")
    validate_request_parameters: bool = Field(alias="validateRequestParameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SdkResponseModel(BaseModel):
    content_type: str = Field(alias="contentType")
    content_disposition: str = Field(alias="contentDisposition")
    body: Type[StreamingBody] = Field(alias="body")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagsModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TemplateModel(BaseModel):
    value: str = Field(alias="value")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestInvokeAuthorizerResponseModel(BaseModel):
    client_status: int = Field(alias="clientStatus")
    log: str = Field(alias="log")
    latency: int = Field(alias="latency")
    principal_id: str = Field(alias="principalId")
    policy: str = Field(alias="policy")
    authorization: Dict[str, List[str]] = Field(alias="authorization")
    claims: Dict[str, str] = Field(alias="claims")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestInvokeMethodResponseModel(BaseModel):
    status: int = Field(alias="status")
    body: str = Field(alias="body")
    headers: Dict[str, str] = Field(alias="headers")
    multi_value_headers: Dict[str, List[str]] = Field(alias="multiValueHeaders")
    log: str = Field(alias="log")
    latency: int = Field(alias="latency")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsagePlanKeyResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    type: str = Field(alias="type")
    value: str = Field(alias="value")
    name: str = Field(alias="name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsageModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    position: str = Field(alias="position")
    items: Dict[str, List[List[int]]] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VpcLinkResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    target_arns: List[str] = Field(alias="targetArns")
    status: Literal["AVAILABLE", "DELETING", "FAILED", "PENDING"] = Field(
        alias="status"
    )
    status_message: str = Field(alias="statusMessage")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccountModel(BaseModel):
    cloudwatch_role_arn: str = Field(alias="cloudwatchRoleArn")
    throttle_settings: ThrottleSettingsModel = Field(alias="throttleSettings")
    features: List[str] = Field(alias="features")
    api_key_version: str = Field(alias="apiKeyVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApiStageModel(BaseModel):
    api_id: Optional[str] = Field(default=None, alias="apiId")
    stage: Optional[str] = Field(default=None, alias="stage")
    throttle: Optional[Mapping[str, ThrottleSettingsModel]] = Field(
        default=None, alias="throttle"
    )


class ApiKeysModel(BaseModel):
    warnings: List[str] = Field(alias="warnings")
    position: str = Field(alias="position")
    items: List[ApiKeyModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthorizersModel(BaseModel):
    position: str = Field(alias="position")
    items: List[AuthorizerModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BasePathMappingsModel(BaseModel):
    position: str = Field(alias="position")
    items: List[BasePathMappingModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStageRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")
    deployment_id: str = Field(alias="deploymentId")
    description: Optional[str] = Field(default=None, alias="description")
    cache_cluster_enabled: Optional[bool] = Field(
        default=None, alias="cacheClusterEnabled"
    )
    cache_cluster_size: Optional[
        Literal["0.5", "1.6", "118", "13.5", "237", "28.4", "58.2", "6.1"]
    ] = Field(default=None, alias="cacheClusterSize")
    variables: Optional[Mapping[str, str]] = Field(default=None, alias="variables")
    documentation_version: Optional[str] = Field(
        default=None, alias="documentationVersion"
    )
    canary_settings: Optional[CanarySettingsModel] = Field(
        default=None, alias="canarySettings"
    )
    tracing_enabled: Optional[bool] = Field(default=None, alias="tracingEnabled")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ClientCertificatesModel(BaseModel):
    position: str = Field(alias="position")
    items: List[ClientCertificateModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApiKeyRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    generate_distinct_id: Optional[bool] = Field(
        default=None, alias="generateDistinctId"
    )
    value: Optional[str] = Field(default=None, alias="value")
    stage_keys: Optional[Sequence[StageKeyModel]] = Field(
        default=None, alias="stageKeys"
    )
    customer_id: Optional[str] = Field(default=None, alias="customerId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateDeploymentRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: Optional[str] = Field(default=None, alias="stageName")
    stage_description: Optional[str] = Field(default=None, alias="stageDescription")
    description: Optional[str] = Field(default=None, alias="description")
    cache_cluster_enabled: Optional[bool] = Field(
        default=None, alias="cacheClusterEnabled"
    )
    cache_cluster_size: Optional[
        Literal["0.5", "1.6", "118", "13.5", "237", "28.4", "58.2", "6.1"]
    ] = Field(default=None, alias="cacheClusterSize")
    variables: Optional[Mapping[str, str]] = Field(default=None, alias="variables")
    canary_settings: Optional[DeploymentCanarySettingsModel] = Field(
        default=None, alias="canarySettings"
    )
    tracing_enabled: Optional[bool] = Field(default=None, alias="tracingEnabled")


class CreateDocumentationPartRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    location: DocumentationPartLocationModel = Field(alias="location")
    properties: str = Field(alias="properties")


class DocumentationPartResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    location: DocumentationPartLocationModel = Field(alias="location")
    properties: str = Field(alias="properties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DocumentationPartModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    location: Optional[DocumentationPartLocationModel] = Field(
        default=None, alias="location"
    )
    properties: Optional[str] = Field(default=None, alias="properties")


class CreateRestApiRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    version: Optional[str] = Field(default=None, alias="version")
    clone_from: Optional[str] = Field(default=None, alias="cloneFrom")
    binary_media_types: Optional[Sequence[str]] = Field(
        default=None, alias="binaryMediaTypes"
    )
    minimum_compression_size: Optional[int] = Field(
        default=None, alias="minimumCompressionSize"
    )
    api_key_source: Optional[Literal["AUTHORIZER", "HEADER"]] = Field(
        default=None, alias="apiKeySource"
    )
    endpoint_configuration: Optional[EndpointConfigurationModel] = Field(
        default=None, alias="endpointConfiguration"
    )
    policy: Optional[str] = Field(default=None, alias="policy")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    disable_execute_api_endpoint: Optional[bool] = Field(
        default=None, alias="disableExecuteApiEndpoint"
    )


class RestApiResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    created_date: datetime = Field(alias="createdDate")
    version: str = Field(alias="version")
    warnings: List[str] = Field(alias="warnings")
    binary_media_types: List[str] = Field(alias="binaryMediaTypes")
    minimum_compression_size: int = Field(alias="minimumCompressionSize")
    api_key_source: Literal["AUTHORIZER", "HEADER"] = Field(alias="apiKeySource")
    endpoint_configuration: EndpointConfigurationModel = Field(
        alias="endpointConfiguration"
    )
    policy: str = Field(alias="policy")
    tags: Dict[str, str] = Field(alias="tags")
    disable_execute_api_endpoint: bool = Field(alias="disableExecuteApiEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestApiModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    version: Optional[str] = Field(default=None, alias="version")
    warnings: Optional[List[str]] = Field(default=None, alias="warnings")
    binary_media_types: Optional[List[str]] = Field(
        default=None, alias="binaryMediaTypes"
    )
    minimum_compression_size: Optional[int] = Field(
        default=None, alias="minimumCompressionSize"
    )
    api_key_source: Optional[Literal["AUTHORIZER", "HEADER"]] = Field(
        default=None, alias="apiKeySource"
    )
    endpoint_configuration: Optional[EndpointConfigurationModel] = Field(
        default=None, alias="endpointConfiguration"
    )
    policy: Optional[str] = Field(default=None, alias="policy")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    disable_execute_api_endpoint: Optional[bool] = Field(
        default=None, alias="disableExecuteApiEndpoint"
    )


class CreateDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    certificate_name: Optional[str] = Field(default=None, alias="certificateName")
    certificate_body: Optional[str] = Field(default=None, alias="certificateBody")
    certificate_private_key: Optional[str] = Field(
        default=None, alias="certificatePrivateKey"
    )
    certificate_chain: Optional[str] = Field(default=None, alias="certificateChain")
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    regional_certificate_name: Optional[str] = Field(
        default=None, alias="regionalCertificateName"
    )
    regional_certificate_arn: Optional[str] = Field(
        default=None, alias="regionalCertificateArn"
    )
    endpoint_configuration: Optional[EndpointConfigurationModel] = Field(
        default=None, alias="endpointConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    security_policy: Optional[Literal["TLS_1_0", "TLS_1_2"]] = Field(
        default=None, alias="securityPolicy"
    )
    mutual_tls_authentication: Optional[MutualTlsAuthenticationInputModel] = Field(
        default=None, alias="mutualTlsAuthentication"
    )
    ownership_verification_certificate_arn: Optional[str] = Field(
        default=None, alias="ownershipVerificationCertificateArn"
    )


class DeploymentResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    description: str = Field(alias="description")
    created_date: datetime = Field(alias="createdDate")
    api_summary: Dict[str, Dict[str, MethodSnapshotModel]] = Field(alias="apiSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    api_summary: Optional[Dict[str, Dict[str, MethodSnapshotModel]]] = Field(
        default=None, alias="apiSummary"
    )


class DocumentationVersionsModel(BaseModel):
    position: str = Field(alias="position")
    items: List[DocumentationVersionModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainNameResponseMetadataModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    certificate_name: str = Field(alias="certificateName")
    certificate_arn: str = Field(alias="certificateArn")
    certificate_upload_date: datetime = Field(alias="certificateUploadDate")
    regional_domain_name: str = Field(alias="regionalDomainName")
    regional_hosted_zone_id: str = Field(alias="regionalHostedZoneId")
    regional_certificate_name: str = Field(alias="regionalCertificateName")
    regional_certificate_arn: str = Field(alias="regionalCertificateArn")
    distribution_domain_name: str = Field(alias="distributionDomainName")
    distribution_hosted_zone_id: str = Field(alias="distributionHostedZoneId")
    endpoint_configuration: EndpointConfigurationModel = Field(
        alias="endpointConfiguration"
    )
    domain_name_status: Literal[
        "AVAILABLE",
        "PENDING",
        "PENDING_CERTIFICATE_REIMPORT",
        "PENDING_OWNERSHIP_VERIFICATION",
        "UPDATING",
    ] = Field(alias="domainNameStatus")
    domain_name_status_message: str = Field(alias="domainNameStatusMessage")
    security_policy: Literal["TLS_1_0", "TLS_1_2"] = Field(alias="securityPolicy")
    tags: Dict[str, str] = Field(alias="tags")
    mutual_tls_authentication: MutualTlsAuthenticationModel = Field(
        alias="mutualTlsAuthentication"
    )
    ownership_verification_certificate_arn: str = Field(
        alias="ownershipVerificationCertificateArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainNameModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    certificate_name: Optional[str] = Field(default=None, alias="certificateName")
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_upload_date: Optional[datetime] = Field(
        default=None, alias="certificateUploadDate"
    )
    regional_domain_name: Optional[str] = Field(
        default=None, alias="regionalDomainName"
    )
    regional_hosted_zone_id: Optional[str] = Field(
        default=None, alias="regionalHostedZoneId"
    )
    regional_certificate_name: Optional[str] = Field(
        default=None, alias="regionalCertificateName"
    )
    regional_certificate_arn: Optional[str] = Field(
        default=None, alias="regionalCertificateArn"
    )
    distribution_domain_name: Optional[str] = Field(
        default=None, alias="distributionDomainName"
    )
    distribution_hosted_zone_id: Optional[str] = Field(
        default=None, alias="distributionHostedZoneId"
    )
    endpoint_configuration: Optional[EndpointConfigurationModel] = Field(
        default=None, alias="endpointConfiguration"
    )
    domain_name_status: Optional[
        Literal[
            "AVAILABLE",
            "PENDING",
            "PENDING_CERTIFICATE_REIMPORT",
            "PENDING_OWNERSHIP_VERIFICATION",
            "UPDATING",
        ]
    ] = Field(default=None, alias="domainNameStatus")
    domain_name_status_message: Optional[str] = Field(
        default=None, alias="domainNameStatusMessage"
    )
    security_policy: Optional[Literal["TLS_1_0", "TLS_1_2"]] = Field(
        default=None, alias="securityPolicy"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    mutual_tls_authentication: Optional[MutualTlsAuthenticationModel] = Field(
        default=None, alias="mutualTlsAuthentication"
    )
    ownership_verification_certificate_arn: Optional[str] = Field(
        default=None, alias="ownershipVerificationCertificateArn"
    )


class GatewayResponsesModel(BaseModel):
    position: str = Field(alias="position")
    items: List[GatewayResponseModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApiKeysRequestGetApiKeysPaginateModel(BaseModel):
    name_query: Optional[str] = Field(default=None, alias="nameQuery")
    customer_id: Optional[str] = Field(default=None, alias="customerId")
    include_values: Optional[bool] = Field(default=None, alias="includeValues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAuthorizersRequestGetAuthorizersPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBasePathMappingsRequestGetBasePathMappingsPaginateModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetClientCertificatesRequestGetClientCertificatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDeploymentsRequestGetDeploymentsPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDocumentationPartsRequestGetDocumentationPartsPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    type: Optional[
        Literal[
            "API",
            "AUTHORIZER",
            "METHOD",
            "MODEL",
            "PATH_PARAMETER",
            "QUERY_PARAMETER",
            "REQUEST_BODY",
            "REQUEST_HEADER",
            "RESOURCE",
            "RESPONSE",
            "RESPONSE_BODY",
            "RESPONSE_HEADER",
        ]
    ] = Field(default=None, alias="type")
    name_query: Optional[str] = Field(default=None, alias="nameQuery")
    path: Optional[str] = Field(default=None, alias="path")
    location_status: Optional[Literal["DOCUMENTED", "UNDOCUMENTED"]] = Field(
        default=None, alias="locationStatus"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDocumentationVersionsRequestGetDocumentationVersionsPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDomainNamesRequestGetDomainNamesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetGatewayResponsesRequestGetGatewayResponsesPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetModelsRequestGetModelsPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRequestValidatorsRequestGetRequestValidatorsPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourcesRequestGetResourcesPaginateModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    embed: Optional[Sequence[str]] = Field(default=None, alias="embed")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRestApisRequestGetRestApisPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetSdkTypesRequestGetSdkTypesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetUsagePlanKeysRequestGetUsagePlanKeysPaginateModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    name_query: Optional[str] = Field(default=None, alias="nameQuery")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetUsagePlansRequestGetUsagePlansPaginateModel(BaseModel):
    key_id: Optional[str] = Field(default=None, alias="keyId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetUsageRequestGetUsagePaginateModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    key_id: Optional[str] = Field(default=None, alias="keyId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetVpcLinksRequestGetVpcLinksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class IntegrationResponseMetadataModel(BaseModel):
    type: Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"] = Field(
        alias="type"
    )
    http_method: str = Field(alias="httpMethod")
    uri: str = Field(alias="uri")
    connection_type: Literal["INTERNET", "VPC_LINK"] = Field(alias="connectionType")
    connection_id: str = Field(alias="connectionId")
    credentials: str = Field(alias="credentials")
    request_parameters: Dict[str, str] = Field(alias="requestParameters")
    request_templates: Dict[str, str] = Field(alias="requestTemplates")
    passthrough_behavior: str = Field(alias="passthroughBehavior")
    content_handling: Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"] = Field(
        alias="contentHandling"
    )
    timeout_in_millis: int = Field(alias="timeoutInMillis")
    cache_namespace: str = Field(alias="cacheNamespace")
    cache_key_parameters: List[str] = Field(alias="cacheKeyParameters")
    integration_responses: Dict[str, IntegrationResponseModel] = Field(
        alias="integrationResponses"
    )
    tls_config: TlsConfigModel = Field(alias="tlsConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IntegrationModel(BaseModel):
    type: Optional[Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]] = Field(
        default=None, alias="type"
    )
    http_method: Optional[str] = Field(default=None, alias="httpMethod")
    uri: Optional[str] = Field(default=None, alias="uri")
    connection_type: Optional[Literal["INTERNET", "VPC_LINK"]] = Field(
        default=None, alias="connectionType"
    )
    connection_id: Optional[str] = Field(default=None, alias="connectionId")
    credentials: Optional[str] = Field(default=None, alias="credentials")
    request_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="requestParameters"
    )
    request_templates: Optional[Dict[str, str]] = Field(
        default=None, alias="requestTemplates"
    )
    passthrough_behavior: Optional[str] = Field(
        default=None, alias="passthroughBehavior"
    )
    content_handling: Optional[Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]] = Field(
        default=None, alias="contentHandling"
    )
    timeout_in_millis: Optional[int] = Field(default=None, alias="timeoutInMillis")
    cache_namespace: Optional[str] = Field(default=None, alias="cacheNamespace")
    cache_key_parameters: Optional[List[str]] = Field(
        default=None, alias="cacheKeyParameters"
    )
    integration_responses: Optional[Dict[str, IntegrationResponseModel]] = Field(
        default=None, alias="integrationResponses"
    )
    tls_config: Optional[TlsConfigModel] = Field(default=None, alias="tlsConfig")


class PutIntegrationRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    type: Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"] = Field(
        alias="type"
    )
    integration_http_method: Optional[str] = Field(
        default=None, alias="integrationHttpMethod"
    )
    uri: Optional[str] = Field(default=None, alias="uri")
    connection_type: Optional[Literal["INTERNET", "VPC_LINK"]] = Field(
        default=None, alias="connectionType"
    )
    connection_id: Optional[str] = Field(default=None, alias="connectionId")
    credentials: Optional[str] = Field(default=None, alias="credentials")
    request_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="requestParameters"
    )
    request_templates: Optional[Mapping[str, str]] = Field(
        default=None, alias="requestTemplates"
    )
    passthrough_behavior: Optional[str] = Field(
        default=None, alias="passthroughBehavior"
    )
    cache_namespace: Optional[str] = Field(default=None, alias="cacheNamespace")
    cache_key_parameters: Optional[Sequence[str]] = Field(
        default=None, alias="cacheKeyParameters"
    )
    content_handling: Optional[Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]] = Field(
        default=None, alias="contentHandling"
    )
    timeout_in_millis: Optional[int] = Field(default=None, alias="timeoutInMillis")
    tls_config: Optional[TlsConfigModel] = Field(default=None, alias="tlsConfig")


class StageResponseMetadataModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    client_certificate_id: str = Field(alias="clientCertificateId")
    stage_name: str = Field(alias="stageName")
    description: str = Field(alias="description")
    cache_cluster_enabled: bool = Field(alias="cacheClusterEnabled")
    cache_cluster_size: Literal[
        "0.5", "1.6", "118", "13.5", "237", "28.4", "58.2", "6.1"
    ] = Field(alias="cacheClusterSize")
    cache_cluster_status: Literal[
        "AVAILABLE",
        "CREATE_IN_PROGRESS",
        "DELETE_IN_PROGRESS",
        "FLUSH_IN_PROGRESS",
        "NOT_AVAILABLE",
    ] = Field(alias="cacheClusterStatus")
    method_settings: Dict[str, MethodSettingModel] = Field(alias="methodSettings")
    variables: Dict[str, str] = Field(alias="variables")
    documentation_version: str = Field(alias="documentationVersion")
    access_log_settings: AccessLogSettingsModel = Field(alias="accessLogSettings")
    canary_settings: CanarySettingsModel = Field(alias="canarySettings")
    tracing_enabled: bool = Field(alias="tracingEnabled")
    web_acl_arn: str = Field(alias="webAclArn")
    tags: Dict[str, str] = Field(alias="tags")
    created_date: datetime = Field(alias="createdDate")
    last_updated_date: datetime = Field(alias="lastUpdatedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StageModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    client_certificate_id: Optional[str] = Field(
        default=None, alias="clientCertificateId"
    )
    stage_name: Optional[str] = Field(default=None, alias="stageName")
    description: Optional[str] = Field(default=None, alias="description")
    cache_cluster_enabled: Optional[bool] = Field(
        default=None, alias="cacheClusterEnabled"
    )
    cache_cluster_size: Optional[
        Literal["0.5", "1.6", "118", "13.5", "237", "28.4", "58.2", "6.1"]
    ] = Field(default=None, alias="cacheClusterSize")
    cache_cluster_status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "FLUSH_IN_PROGRESS",
            "NOT_AVAILABLE",
        ]
    ] = Field(default=None, alias="cacheClusterStatus")
    method_settings: Optional[Dict[str, MethodSettingModel]] = Field(
        default=None, alias="methodSettings"
    )
    variables: Optional[Dict[str, str]] = Field(default=None, alias="variables")
    documentation_version: Optional[str] = Field(
        default=None, alias="documentationVersion"
    )
    access_log_settings: Optional[AccessLogSettingsModel] = Field(
        default=None, alias="accessLogSettings"
    )
    canary_settings: Optional[CanarySettingsModel] = Field(
        default=None, alias="canarySettings"
    )
    tracing_enabled: Optional[bool] = Field(default=None, alias="tracingEnabled")
    web_acl_arn: Optional[str] = Field(default=None, alias="webAclArn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    last_updated_date: Optional[datetime] = Field(default=None, alias="lastUpdatedDate")


class ModelsModel(BaseModel):
    position: str = Field(alias="position")
    items: List[ModelModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountRequestModel(BaseModel):
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateApiKeyRequestModel(BaseModel):
    api_key: str = Field(alias="apiKey")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateAuthorizerRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    authorizer_id: str = Field(alias="authorizerId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateBasePathMappingRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    base_path: str = Field(alias="basePath")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateClientCertificateRequestModel(BaseModel):
    client_certificate_id: str = Field(alias="clientCertificateId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateDeploymentRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    deployment_id: str = Field(alias="deploymentId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateDocumentationPartRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    documentation_part_id: str = Field(alias="documentationPartId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateDocumentationVersionRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    documentation_version: str = Field(alias="documentationVersion")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateGatewayResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    response_type: Literal[
        "ACCESS_DENIED",
        "API_CONFIGURATION_ERROR",
        "AUTHORIZER_CONFIGURATION_ERROR",
        "AUTHORIZER_FAILURE",
        "BAD_REQUEST_BODY",
        "BAD_REQUEST_PARAMETERS",
        "DEFAULT_4XX",
        "DEFAULT_5XX",
        "EXPIRED_TOKEN",
        "INTEGRATION_FAILURE",
        "INTEGRATION_TIMEOUT",
        "INVALID_API_KEY",
        "INVALID_SIGNATURE",
        "MISSING_AUTHENTICATION_TOKEN",
        "QUOTA_EXCEEDED",
        "REQUEST_TOO_LARGE",
        "RESOURCE_NOT_FOUND",
        "THROTTLED",
        "UNAUTHORIZED",
        "UNSUPPORTED_MEDIA_TYPE",
        "WAF_FILTERED",
    ] = Field(alias="responseType")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateIntegrationRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateIntegrationResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateMethodRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateMethodResponseRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    http_method: str = Field(alias="httpMethod")
    status_code: str = Field(alias="statusCode")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateModelRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    model_name: str = Field(alias="modelName")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateRequestValidatorRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    request_validator_id: str = Field(alias="requestValidatorId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateResourceRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    resource_id: str = Field(alias="resourceId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateRestApiRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateStageRequestModel(BaseModel):
    rest_api_id: str = Field(alias="restApiId")
    stage_name: str = Field(alias="stageName")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateUsagePlanRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateUsageRequestModel(BaseModel):
    usage_plan_id: str = Field(alias="usagePlanId")
    key_id: str = Field(alias="keyId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class UpdateVpcLinkRequestModel(BaseModel):
    vpc_link_id: str = Field(alias="vpcLinkId")
    patch_operations: Optional[Sequence[PatchOperationModel]] = Field(
        default=None, alias="patchOperations"
    )


class RequestValidatorsModel(BaseModel):
    position: str = Field(alias="position")
    items: List[RequestValidatorModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SdkTypeResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    friendly_name: str = Field(alias="friendlyName")
    description: str = Field(alias="description")
    configuration_properties: List[SdkConfigurationPropertyModel] = Field(
        alias="configurationProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SdkTypeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    friendly_name: Optional[str] = Field(default=None, alias="friendlyName")
    description: Optional[str] = Field(default=None, alias="description")
    configuration_properties: Optional[List[SdkConfigurationPropertyModel]] = Field(
        default=None, alias="configurationProperties"
    )


class UsagePlanKeysModel(BaseModel):
    position: str = Field(alias="position")
    items: List[UsagePlanKeyModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VpcLinksModel(BaseModel):
    position: str = Field(alias="position")
    items: List[VpcLinkModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUsagePlanRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    api_stages: Optional[Sequence[ApiStageModel]] = Field(
        default=None, alias="apiStages"
    )
    throttle: Optional[ThrottleSettingsModel] = Field(default=None, alias="throttle")
    quota: Optional[QuotaSettingsModel] = Field(default=None, alias="quota")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UsagePlanResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    api_stages: List[ApiStageModel] = Field(alias="apiStages")
    throttle: ThrottleSettingsModel = Field(alias="throttle")
    quota: QuotaSettingsModel = Field(alias="quota")
    product_code: str = Field(alias="productCode")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsagePlanModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    api_stages: Optional[List[ApiStageModel]] = Field(default=None, alias="apiStages")
    throttle: Optional[ThrottleSettingsModel] = Field(default=None, alias="throttle")
    quota: Optional[QuotaSettingsModel] = Field(default=None, alias="quota")
    product_code: Optional[str] = Field(default=None, alias="productCode")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class DocumentationPartsModel(BaseModel):
    position: str = Field(alias="position")
    items: List[DocumentationPartModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestApisModel(BaseModel):
    position: str = Field(alias="position")
    items: List[RestApiModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentsModel(BaseModel):
    position: str = Field(alias="position")
    items: List[DeploymentModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainNamesModel(BaseModel):
    position: str = Field(alias="position")
    items: List[DomainNameModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MethodResponseMetadataModel(BaseModel):
    http_method: str = Field(alias="httpMethod")
    authorization_type: str = Field(alias="authorizationType")
    authorizer_id: str = Field(alias="authorizerId")
    api_key_required: bool = Field(alias="apiKeyRequired")
    request_validator_id: str = Field(alias="requestValidatorId")
    operation_name: str = Field(alias="operationName")
    request_parameters: Dict[str, bool] = Field(alias="requestParameters")
    request_models: Dict[str, str] = Field(alias="requestModels")
    method_responses: Dict[str, MethodResponseModel] = Field(alias="methodResponses")
    method_integration: IntegrationModel = Field(alias="methodIntegration")
    authorization_scopes: List[str] = Field(alias="authorizationScopes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MethodModel(BaseModel):
    http_method: Optional[str] = Field(default=None, alias="httpMethod")
    authorization_type: Optional[str] = Field(default=None, alias="authorizationType")
    authorizer_id: Optional[str] = Field(default=None, alias="authorizerId")
    api_key_required: Optional[bool] = Field(default=None, alias="apiKeyRequired")
    request_validator_id: Optional[str] = Field(
        default=None, alias="requestValidatorId"
    )
    operation_name: Optional[str] = Field(default=None, alias="operationName")
    request_parameters: Optional[Dict[str, bool]] = Field(
        default=None, alias="requestParameters"
    )
    request_models: Optional[Dict[str, str]] = Field(
        default=None, alias="requestModels"
    )
    method_responses: Optional[Dict[str, MethodResponseModel]] = Field(
        default=None, alias="methodResponses"
    )
    method_integration: Optional[IntegrationModel] = Field(
        default=None, alias="methodIntegration"
    )
    authorization_scopes: Optional[List[str]] = Field(
        default=None, alias="authorizationScopes"
    )


class StagesModel(BaseModel):
    item: List[StageModel] = Field(alias="item")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SdkTypesModel(BaseModel):
    position: str = Field(alias="position")
    items: List[SdkTypeModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsagePlansModel(BaseModel):
    position: str = Field(alias="position")
    items: List[UsagePlanModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceResponseMetadataModel(BaseModel):
    id: str = Field(alias="id")
    parent_id: str = Field(alias="parentId")
    path_part: str = Field(alias="pathPart")
    path: str = Field(alias="path")
    resource_methods: Dict[str, MethodModel] = Field(alias="resourceMethods")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    parent_id: Optional[str] = Field(default=None, alias="parentId")
    path_part: Optional[str] = Field(default=None, alias="pathPart")
    path: Optional[str] = Field(default=None, alias="path")
    resource_methods: Optional[Dict[str, MethodModel]] = Field(
        default=None, alias="resourceMethods"
    )


class ResourcesModel(BaseModel):
    position: str = Field(alias="position")
    items: List[ResourceModel] = Field(alias="items")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
