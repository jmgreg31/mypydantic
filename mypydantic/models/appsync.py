# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

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


class CognitoUserPoolConfigModel(BaseModel):
    user_pool_id: str = Field(alias="userPoolId")
    aws_region: str = Field(alias="awsRegion")
    app_id_client_regex: Optional[str] = Field(default=None, alias="appIdClientRegex")


class LambdaAuthorizerConfigModel(BaseModel):
    authorizer_uri: str = Field(alias="authorizerUri")
    authorizer_result_ttl_in_seconds: Optional[int] = Field(
        default=None, alias="authorizerResultTtlInSeconds"
    )
    identity_validation_expression: Optional[str] = Field(
        default=None, alias="identityValidationExpression"
    )


class OpenIDConnectConfigModel(BaseModel):
    issuer: str = Field(alias="issuer")
    client_id: Optional[str] = Field(default=None, alias="clientId")
    iat_ttl: Optional[int] = Field(default=None, alias="iatTTL")
    auth_ttl: Optional[int] = Field(default=None, alias="authTTL")


class ApiAssociationModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    api_id: Optional[str] = Field(default=None, alias="apiId")
    association_status: Optional[Literal["FAILED", "PROCESSING", "SUCCESS"]] = Field(
        default=None, alias="associationStatus"
    )
    deployment_detail: Optional[str] = Field(default=None, alias="deploymentDetail")


class ApiCacheModel(BaseModel):
    ttl: Optional[int] = Field(default=None, alias="ttl")
    api_caching_behavior: Optional[
        Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"]
    ] = Field(default=None, alias="apiCachingBehavior")
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="transitEncryptionEnabled"
    )
    at_rest_encryption_enabled: Optional[bool] = Field(
        default=None, alias="atRestEncryptionEnabled"
    )
    type: Optional[
        Literal[
            "LARGE",
            "LARGE_12X",
            "LARGE_2X",
            "LARGE_4X",
            "LARGE_8X",
            "MEDIUM",
            "R4_2XLARGE",
            "R4_4XLARGE",
            "R4_8XLARGE",
            "R4_LARGE",
            "R4_XLARGE",
            "SMALL",
            "T2_MEDIUM",
            "T2_SMALL",
            "XLARGE",
        ]
    ] = Field(default=None, alias="type")
    status: Optional[
        Literal["AVAILABLE", "CREATING", "DELETING", "FAILED", "MODIFYING"]
    ] = Field(default=None, alias="status")


class ApiKeyModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    expires: Optional[int] = Field(default=None, alias="expires")
    deletes: Optional[int] = Field(default=None, alias="deletes")


class AppSyncRuntimeModel(BaseModel):
    name: Literal["APPSYNC_JS"] = Field(alias="name")
    runtime_version: str = Field(alias="runtimeVersion")


class AssociateApiRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    api_id: str = Field(alias="apiId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AwsIamConfigModel(BaseModel):
    signing_region: Optional[str] = Field(default=None, alias="signingRegion")
    signing_service_name: Optional[str] = Field(
        default=None, alias="signingServiceName"
    )


class CachingConfigModel(BaseModel):
    ttl: int = Field(alias="ttl")
    caching_keys: Optional[Sequence[str]] = Field(default=None, alias="cachingKeys")


class CodeErrorLocationModel(BaseModel):
    line: Optional[int] = Field(default=None, alias="line")
    column: Optional[int] = Field(default=None, alias="column")
    span: Optional[int] = Field(default=None, alias="span")


class CreateApiCacheRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    ttl: int = Field(alias="ttl")
    api_caching_behavior: Literal[
        "FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"
    ] = Field(alias="apiCachingBehavior")
    type: Literal[
        "LARGE",
        "LARGE_12X",
        "LARGE_2X",
        "LARGE_4X",
        "LARGE_8X",
        "MEDIUM",
        "R4_2XLARGE",
        "R4_4XLARGE",
        "R4_8XLARGE",
        "R4_LARGE",
        "R4_XLARGE",
        "SMALL",
        "T2_MEDIUM",
        "T2_SMALL",
        "XLARGE",
    ] = Field(alias="type")
    transit_encryption_enabled: Optional[bool] = Field(
        default=None, alias="transitEncryptionEnabled"
    )
    at_rest_encryption_enabled: Optional[bool] = Field(
        default=None, alias="atRestEncryptionEnabled"
    )


class CreateApiKeyRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    description: Optional[str] = Field(default=None, alias="description")
    expires: Optional[int] = Field(default=None, alias="expires")


class ElasticsearchDataSourceConfigModel(BaseModel):
    endpoint: str = Field(alias="endpoint")
    aws_region: str = Field(alias="awsRegion")


class EventBridgeDataSourceConfigModel(BaseModel):
    event_bus_arn: str = Field(alias="eventBusArn")


class LambdaDataSourceConfigModel(BaseModel):
    lambda_function_arn: str = Field(alias="lambdaFunctionArn")


class OpenSearchServiceDataSourceConfigModel(BaseModel):
    endpoint: str = Field(alias="endpoint")
    aws_region: str = Field(alias="awsRegion")


class CreateDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    certificate_arn: str = Field(alias="certificateArn")
    description: Optional[str] = Field(default=None, alias="description")


class DomainNameConfigModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    description: Optional[str] = Field(default=None, alias="description")
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    appsync_domain_name: Optional[str] = Field(default=None, alias="appsyncDomainName")
    hosted_zone_id: Optional[str] = Field(default=None, alias="hostedZoneId")


class LogConfigModel(BaseModel):
    field_log_level: Literal["ALL", "ERROR", "NONE"] = Field(alias="fieldLogLevel")
    cloud_watch_logs_role_arn: str = Field(alias="cloudWatchLogsRoleArn")
    exclude_verbose_content: Optional[bool] = Field(
        default=None, alias="excludeVerboseContent"
    )


class UserPoolConfigModel(BaseModel):
    user_pool_id: str = Field(alias="userPoolId")
    aws_region: str = Field(alias="awsRegion")
    default_action: Literal["ALLOW", "DENY"] = Field(alias="defaultAction")
    app_id_client_regex: Optional[str] = Field(default=None, alias="appIdClientRegex")


class PipelineConfigModel(BaseModel):
    functions: Optional[Sequence[str]] = Field(default=None, alias="functions")


class CreateTypeRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    definition: str = Field(alias="definition")
    format: Literal["JSON", "SDL"] = Field(alias="format")


class TypeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    arn: Optional[str] = Field(default=None, alias="arn")
    definition: Optional[str] = Field(default=None, alias="definition")
    format: Optional[Literal["JSON", "SDL"]] = Field(default=None, alias="format")


class DeleteApiCacheRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")


class DeleteApiKeyRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    id: str = Field(alias="id")


class DeleteDataSourceRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    name: str = Field(alias="name")


class DeleteDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class DeleteFunctionRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    function_id: str = Field(alias="functionId")


class DeleteGraphqlApiRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")


class DeleteResolverRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    field_name: str = Field(alias="fieldName")


class DeleteTypeRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")


class DeltaSyncConfigModel(BaseModel):
    base_table_ttl: Optional[int] = Field(default=None, alias="baseTableTTL")
    delta_sync_table_name: Optional[str] = Field(
        default=None, alias="deltaSyncTableName"
    )
    delta_sync_table_ttl: Optional[int] = Field(default=None, alias="deltaSyncTableTTL")


class DisassociateApiRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class ErrorDetailModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class EvaluateMappingTemplateRequestModel(BaseModel):
    template: str = Field(alias="template")
    context: str = Field(alias="context")


class FlushApiCacheRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")


class GetApiAssociationRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class GetApiCacheRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")


class GetDataSourceRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    name: str = Field(alias="name")


class GetDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class GetFunctionRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    function_id: str = Field(alias="functionId")


class GetGraphqlApiRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")


class GetIntrospectionSchemaRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    format: Literal["JSON", "SDL"] = Field(alias="format")
    include_directives: Optional[bool] = Field(default=None, alias="includeDirectives")


class GetResolverRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    field_name: str = Field(alias="fieldName")


class GetSchemaCreationStatusRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")


class GetTypeRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    format: Literal["JSON", "SDL"] = Field(alias="format")


class LambdaConflictHandlerConfigModel(BaseModel):
    lambda_conflict_handler_arn: Optional[str] = Field(
        default=None, alias="lambdaConflictHandlerArn"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApiKeysRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDataSourcesRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDomainNamesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListFunctionsRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListGraphqlApisRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListResolversByFunctionRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    function_id: str = Field(alias="functionId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListResolversRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListTypesRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    format: Literal["JSON", "SDL"] = Field(alias="format")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class RdsHttpEndpointConfigModel(BaseModel):
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    db_cluster_identifier: Optional[str] = Field(
        default=None, alias="dbClusterIdentifier"
    )
    database_name: Optional[str] = Field(default=None, alias="databaseName")
    schema_: Optional[str] = Field(default=None, alias="schema")
    aws_secret_store_arn: Optional[str] = Field(default=None, alias="awsSecretStoreArn")


class StartSchemaCreationRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    definition: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="definition"
    )


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateApiCacheRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    ttl: int = Field(alias="ttl")
    api_caching_behavior: Literal[
        "FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"
    ] = Field(alias="apiCachingBehavior")
    type: Literal[
        "LARGE",
        "LARGE_12X",
        "LARGE_2X",
        "LARGE_4X",
        "LARGE_8X",
        "MEDIUM",
        "R4_2XLARGE",
        "R4_4XLARGE",
        "R4_8XLARGE",
        "R4_LARGE",
        "R4_XLARGE",
        "SMALL",
        "T2_MEDIUM",
        "T2_SMALL",
        "XLARGE",
    ] = Field(alias="type")


class UpdateApiKeyRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    id: str = Field(alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    expires: Optional[int] = Field(default=None, alias="expires")


class UpdateDomainNameRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateTypeRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    format: Literal["JSON", "SDL"] = Field(alias="format")
    definition: Optional[str] = Field(default=None, alias="definition")


class AdditionalAuthenticationProviderModel(BaseModel):
    authentication_type: Optional[
        Literal[
            "AMAZON_COGNITO_USER_POOLS",
            "API_KEY",
            "AWS_IAM",
            "AWS_LAMBDA",
            "OPENID_CONNECT",
        ]
    ] = Field(default=None, alias="authenticationType")
    open_idconnect_config: Optional[OpenIDConnectConfigModel] = Field(
        default=None, alias="openIDConnectConfig"
    )
    user_pool_config: Optional[CognitoUserPoolConfigModel] = Field(
        default=None, alias="userPoolConfig"
    )
    lambda_authorizer_config: Optional[LambdaAuthorizerConfigModel] = Field(
        default=None, alias="lambdaAuthorizerConfig"
    )


class EvaluateCodeRequestModel(BaseModel):
    runtime: AppSyncRuntimeModel = Field(alias="runtime")
    code: str = Field(alias="code")
    context: str = Field(alias="context")
    function: Optional[str] = Field(default=None, alias="function")


class AssociateApiResponseModel(BaseModel):
    api_association: ApiAssociationModel = Field(alias="apiAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApiCacheResponseModel(BaseModel):
    api_cache: ApiCacheModel = Field(alias="apiCache")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApiKeyResponseModel(BaseModel):
    api_key: ApiKeyModel = Field(alias="apiKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApiAssociationResponseModel(BaseModel):
    api_association: ApiAssociationModel = Field(alias="apiAssociation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApiCacheResponseModel(BaseModel):
    api_cache: ApiCacheModel = Field(alias="apiCache")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIntrospectionSchemaResponseModel(BaseModel):
    schema_: Type[StreamingBody] = Field(alias="schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaCreationStatusResponseModel(BaseModel):
    status: Literal[
        "ACTIVE", "DELETING", "FAILED", "NOT_APPLICABLE", "PROCESSING", "SUCCESS"
    ] = Field(alias="status")
    details: str = Field(alias="details")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApiKeysResponseModel(BaseModel):
    api_keys: List[ApiKeyModel] = Field(alias="apiKeys")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSchemaCreationResponseModel(BaseModel):
    status: Literal[
        "ACTIVE", "DELETING", "FAILED", "NOT_APPLICABLE", "PROCESSING", "SUCCESS"
    ] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApiCacheResponseModel(BaseModel):
    api_cache: ApiCacheModel = Field(alias="apiCache")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateApiKeyResponseModel(BaseModel):
    api_key: ApiKeyModel = Field(alias="apiKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthorizationConfigModel(BaseModel):
    authorization_type: Literal["AWS_IAM"] = Field(alias="authorizationType")
    aws_iam_config: Optional[AwsIamConfigModel] = Field(
        default=None, alias="awsIamConfig"
    )


class CodeErrorModel(BaseModel):
    error_type: Optional[str] = Field(default=None, alias="errorType")
    value: Optional[str] = Field(default=None, alias="value")
    location: Optional[CodeErrorLocationModel] = Field(default=None, alias="location")


class CreateDomainNameResponseModel(BaseModel):
    domain_name_config: DomainNameConfigModel = Field(alias="domainNameConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainNameResponseModel(BaseModel):
    domain_name_config: DomainNameConfigModel = Field(alias="domainNameConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainNamesResponseModel(BaseModel):
    domain_name_configs: List[DomainNameConfigModel] = Field(alias="domainNameConfigs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainNameResponseModel(BaseModel):
    domain_name_config: DomainNameConfigModel = Field(alias="domainNameConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTypeResponseModel(BaseModel):
    type: TypeModel = Field(alias="type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTypeResponseModel(BaseModel):
    type: TypeModel = Field(alias="type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTypesResponseModel(BaseModel):
    types: List[TypeModel] = Field(alias="types")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTypeResponseModel(BaseModel):
    type: TypeModel = Field(alias="type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DynamodbDataSourceConfigModel(BaseModel):
    table_name: str = Field(alias="tableName")
    aws_region: str = Field(alias="awsRegion")
    use_caller_credentials: Optional[bool] = Field(
        default=None, alias="useCallerCredentials"
    )
    delta_sync_config: Optional[DeltaSyncConfigModel] = Field(
        default=None, alias="deltaSyncConfig"
    )
    versioned: Optional[bool] = Field(default=None, alias="versioned")


class EvaluateMappingTemplateResponseModel(BaseModel):
    evaluation_result: str = Field(alias="evaluationResult")
    error: ErrorDetailModel = Field(alias="error")
    logs: List[str] = Field(alias="logs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SyncConfigModel(BaseModel):
    conflict_handler: Optional[
        Literal["AUTOMERGE", "LAMBDA", "NONE", "OPTIMISTIC_CONCURRENCY"]
    ] = Field(default=None, alias="conflictHandler")
    conflict_detection: Optional[Literal["NONE", "VERSION"]] = Field(
        default=None, alias="conflictDetection"
    )
    lambda_conflict_handler_config: Optional[LambdaConflictHandlerConfigModel] = Field(
        default=None, alias="lambdaConflictHandlerConfig"
    )


class ListApiKeysRequestListApiKeysPaginateModel(BaseModel):
    api_id: str = Field(alias="apiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataSourcesRequestListDataSourcesPaginateModel(BaseModel):
    api_id: str = Field(alias="apiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionsRequestListFunctionsPaginateModel(BaseModel):
    api_id: str = Field(alias="apiId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGraphqlApisRequestListGraphqlApisPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolversByFunctionRequestListResolversByFunctionPaginateModel(BaseModel):
    api_id: str = Field(alias="apiId")
    function_id: str = Field(alias="functionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResolversRequestListResolversPaginateModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTypesRequestListTypesPaginateModel(BaseModel):
    api_id: str = Field(alias="apiId")
    format: Literal["JSON", "SDL"] = Field(alias="format")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class RelationalDatabaseDataSourceConfigModel(BaseModel):
    relational_database_source_type: Optional[Literal["RDS_HTTP_ENDPOINT"]] = Field(
        default=None, alias="relationalDatabaseSourceType"
    )
    rds_http_endpoint_config: Optional[RdsHttpEndpointConfigModel] = Field(
        default=None, alias="rdsHttpEndpointConfig"
    )


class CreateGraphqlApiRequestModel(BaseModel):
    name: str = Field(alias="name")
    authentication_type: Literal[
        "AMAZON_COGNITO_USER_POOLS",
        "API_KEY",
        "AWS_IAM",
        "AWS_LAMBDA",
        "OPENID_CONNECT",
    ] = Field(alias="authenticationType")
    log_config: Optional[LogConfigModel] = Field(default=None, alias="logConfig")
    user_pool_config: Optional[UserPoolConfigModel] = Field(
        default=None, alias="userPoolConfig"
    )
    open_idconnect_config: Optional[OpenIDConnectConfigModel] = Field(
        default=None, alias="openIDConnectConfig"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    additional_authentication_providers: Optional[
        Sequence[AdditionalAuthenticationProviderModel]
    ] = Field(default=None, alias="additionalAuthenticationProviders")
    xray_enabled: Optional[bool] = Field(default=None, alias="xrayEnabled")
    lambda_authorizer_config: Optional[LambdaAuthorizerConfigModel] = Field(
        default=None, alias="lambdaAuthorizerConfig"
    )


class GraphqlApiModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    api_id: Optional[str] = Field(default=None, alias="apiId")
    authentication_type: Optional[
        Literal[
            "AMAZON_COGNITO_USER_POOLS",
            "API_KEY",
            "AWS_IAM",
            "AWS_LAMBDA",
            "OPENID_CONNECT",
        ]
    ] = Field(default=None, alias="authenticationType")
    log_config: Optional[LogConfigModel] = Field(default=None, alias="logConfig")
    user_pool_config: Optional[UserPoolConfigModel] = Field(
        default=None, alias="userPoolConfig"
    )
    open_idconnect_config: Optional[OpenIDConnectConfigModel] = Field(
        default=None, alias="openIDConnectConfig"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    uris: Optional[Dict[str, str]] = Field(default=None, alias="uris")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    additional_authentication_providers: Optional[
        List[AdditionalAuthenticationProviderModel]
    ] = Field(default=None, alias="additionalAuthenticationProviders")
    xray_enabled: Optional[bool] = Field(default=None, alias="xrayEnabled")
    waf_web_acl_arn: Optional[str] = Field(default=None, alias="wafWebAclArn")
    lambda_authorizer_config: Optional[LambdaAuthorizerConfigModel] = Field(
        default=None, alias="lambdaAuthorizerConfig"
    )


class UpdateGraphqlApiRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    name: str = Field(alias="name")
    log_config: Optional[LogConfigModel] = Field(default=None, alias="logConfig")
    authentication_type: Optional[
        Literal[
            "AMAZON_COGNITO_USER_POOLS",
            "API_KEY",
            "AWS_IAM",
            "AWS_LAMBDA",
            "OPENID_CONNECT",
        ]
    ] = Field(default=None, alias="authenticationType")
    user_pool_config: Optional[UserPoolConfigModel] = Field(
        default=None, alias="userPoolConfig"
    )
    open_idconnect_config: Optional[OpenIDConnectConfigModel] = Field(
        default=None, alias="openIDConnectConfig"
    )
    additional_authentication_providers: Optional[
        Sequence[AdditionalAuthenticationProviderModel]
    ] = Field(default=None, alias="additionalAuthenticationProviders")
    xray_enabled: Optional[bool] = Field(default=None, alias="xrayEnabled")
    lambda_authorizer_config: Optional[LambdaAuthorizerConfigModel] = Field(
        default=None, alias="lambdaAuthorizerConfig"
    )


class HttpDataSourceConfigModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="endpoint")
    authorization_config: Optional[AuthorizationConfigModel] = Field(
        default=None, alias="authorizationConfig"
    )


class EvaluateCodeErrorDetailModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")
    code_errors: Optional[List[CodeErrorModel]] = Field(
        default=None, alias="codeErrors"
    )


class CreateFunctionRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    name: str = Field(alias="name")
    data_source_name: str = Field(alias="dataSourceName")
    description: Optional[str] = Field(default=None, alias="description")
    request_mapping_template: Optional[str] = Field(
        default=None, alias="requestMappingTemplate"
    )
    response_mapping_template: Optional[str] = Field(
        default=None, alias="responseMappingTemplate"
    )
    function_version: Optional[str] = Field(default=None, alias="functionVersion")
    sync_config: Optional[SyncConfigModel] = Field(default=None, alias="syncConfig")
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")
    runtime: Optional[AppSyncRuntimeModel] = Field(default=None, alias="runtime")
    code: Optional[str] = Field(default=None, alias="code")


class CreateResolverRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    field_name: str = Field(alias="fieldName")
    data_source_name: Optional[str] = Field(default=None, alias="dataSourceName")
    request_mapping_template: Optional[str] = Field(
        default=None, alias="requestMappingTemplate"
    )
    response_mapping_template: Optional[str] = Field(
        default=None, alias="responseMappingTemplate"
    )
    kind: Optional[Literal["PIPELINE", "UNIT"]] = Field(default=None, alias="kind")
    pipeline_config: Optional[PipelineConfigModel] = Field(
        default=None, alias="pipelineConfig"
    )
    sync_config: Optional[SyncConfigModel] = Field(default=None, alias="syncConfig")
    caching_config: Optional[CachingConfigModel] = Field(
        default=None, alias="cachingConfig"
    )
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")
    runtime: Optional[AppSyncRuntimeModel] = Field(default=None, alias="runtime")
    code: Optional[str] = Field(default=None, alias="code")


class FunctionConfigurationModel(BaseModel):
    function_id: Optional[str] = Field(default=None, alias="functionId")
    function_arn: Optional[str] = Field(default=None, alias="functionArn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    data_source_name: Optional[str] = Field(default=None, alias="dataSourceName")
    request_mapping_template: Optional[str] = Field(
        default=None, alias="requestMappingTemplate"
    )
    response_mapping_template: Optional[str] = Field(
        default=None, alias="responseMappingTemplate"
    )
    function_version: Optional[str] = Field(default=None, alias="functionVersion")
    sync_config: Optional[SyncConfigModel] = Field(default=None, alias="syncConfig")
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")
    runtime: Optional[AppSyncRuntimeModel] = Field(default=None, alias="runtime")
    code: Optional[str] = Field(default=None, alias="code")


class ResolverModel(BaseModel):
    type_name: Optional[str] = Field(default=None, alias="typeName")
    field_name: Optional[str] = Field(default=None, alias="fieldName")
    data_source_name: Optional[str] = Field(default=None, alias="dataSourceName")
    resolver_arn: Optional[str] = Field(default=None, alias="resolverArn")
    request_mapping_template: Optional[str] = Field(
        default=None, alias="requestMappingTemplate"
    )
    response_mapping_template: Optional[str] = Field(
        default=None, alias="responseMappingTemplate"
    )
    kind: Optional[Literal["PIPELINE", "UNIT"]] = Field(default=None, alias="kind")
    pipeline_config: Optional[PipelineConfigModel] = Field(
        default=None, alias="pipelineConfig"
    )
    sync_config: Optional[SyncConfigModel] = Field(default=None, alias="syncConfig")
    caching_config: Optional[CachingConfigModel] = Field(
        default=None, alias="cachingConfig"
    )
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")
    runtime: Optional[AppSyncRuntimeModel] = Field(default=None, alias="runtime")
    code: Optional[str] = Field(default=None, alias="code")


class UpdateFunctionRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    name: str = Field(alias="name")
    function_id: str = Field(alias="functionId")
    data_source_name: str = Field(alias="dataSourceName")
    description: Optional[str] = Field(default=None, alias="description")
    request_mapping_template: Optional[str] = Field(
        default=None, alias="requestMappingTemplate"
    )
    response_mapping_template: Optional[str] = Field(
        default=None, alias="responseMappingTemplate"
    )
    function_version: Optional[str] = Field(default=None, alias="functionVersion")
    sync_config: Optional[SyncConfigModel] = Field(default=None, alias="syncConfig")
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")
    runtime: Optional[AppSyncRuntimeModel] = Field(default=None, alias="runtime")
    code: Optional[str] = Field(default=None, alias="code")


class UpdateResolverRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    type_name: str = Field(alias="typeName")
    field_name: str = Field(alias="fieldName")
    data_source_name: Optional[str] = Field(default=None, alias="dataSourceName")
    request_mapping_template: Optional[str] = Field(
        default=None, alias="requestMappingTemplate"
    )
    response_mapping_template: Optional[str] = Field(
        default=None, alias="responseMappingTemplate"
    )
    kind: Optional[Literal["PIPELINE", "UNIT"]] = Field(default=None, alias="kind")
    pipeline_config: Optional[PipelineConfigModel] = Field(
        default=None, alias="pipelineConfig"
    )
    sync_config: Optional[SyncConfigModel] = Field(default=None, alias="syncConfig")
    caching_config: Optional[CachingConfigModel] = Field(
        default=None, alias="cachingConfig"
    )
    max_batch_size: Optional[int] = Field(default=None, alias="maxBatchSize")
    runtime: Optional[AppSyncRuntimeModel] = Field(default=None, alias="runtime")
    code: Optional[str] = Field(default=None, alias="code")


class CreateGraphqlApiResponseModel(BaseModel):
    graphql_api: GraphqlApiModel = Field(alias="graphqlApi")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGraphqlApiResponseModel(BaseModel):
    graphql_api: GraphqlApiModel = Field(alias="graphqlApi")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGraphqlApisResponseModel(BaseModel):
    graphql_apis: List[GraphqlApiModel] = Field(alias="graphqlApis")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGraphqlApiResponseModel(BaseModel):
    graphql_api: GraphqlApiModel = Field(alias="graphqlApi")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    name: str = Field(alias="name")
    type: Literal[
        "AMAZON_DYNAMODB",
        "AMAZON_ELASTICSEARCH",
        "AMAZON_EVENTBRIDGE",
        "AMAZON_OPENSEARCH_SERVICE",
        "AWS_LAMBDA",
        "HTTP",
        "NONE",
        "RELATIONAL_DATABASE",
    ] = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    service_role_arn: Optional[str] = Field(default=None, alias="serviceRoleArn")
    dynamodb_config: Optional[DynamodbDataSourceConfigModel] = Field(
        default=None, alias="dynamodbConfig"
    )
    lambda_config: Optional[LambdaDataSourceConfigModel] = Field(
        default=None, alias="lambdaConfig"
    )
    elasticsearch_config: Optional[ElasticsearchDataSourceConfigModel] = Field(
        default=None, alias="elasticsearchConfig"
    )
    open_search_service_config: Optional[
        OpenSearchServiceDataSourceConfigModel
    ] = Field(default=None, alias="openSearchServiceConfig")
    http_config: Optional[HttpDataSourceConfigModel] = Field(
        default=None, alias="httpConfig"
    )
    relational_database_config: Optional[
        RelationalDatabaseDataSourceConfigModel
    ] = Field(default=None, alias="relationalDatabaseConfig")
    event_bridge_config: Optional[EventBridgeDataSourceConfigModel] = Field(
        default=None, alias="eventBridgeConfig"
    )


class DataSourceModel(BaseModel):
    data_source_arn: Optional[str] = Field(default=None, alias="dataSourceArn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[
        Literal[
            "AMAZON_DYNAMODB",
            "AMAZON_ELASTICSEARCH",
            "AMAZON_EVENTBRIDGE",
            "AMAZON_OPENSEARCH_SERVICE",
            "AWS_LAMBDA",
            "HTTP",
            "NONE",
            "RELATIONAL_DATABASE",
        ]
    ] = Field(default=None, alias="type")
    service_role_arn: Optional[str] = Field(default=None, alias="serviceRoleArn")
    dynamodb_config: Optional[DynamodbDataSourceConfigModel] = Field(
        default=None, alias="dynamodbConfig"
    )
    lambda_config: Optional[LambdaDataSourceConfigModel] = Field(
        default=None, alias="lambdaConfig"
    )
    elasticsearch_config: Optional[ElasticsearchDataSourceConfigModel] = Field(
        default=None, alias="elasticsearchConfig"
    )
    open_search_service_config: Optional[
        OpenSearchServiceDataSourceConfigModel
    ] = Field(default=None, alias="openSearchServiceConfig")
    http_config: Optional[HttpDataSourceConfigModel] = Field(
        default=None, alias="httpConfig"
    )
    relational_database_config: Optional[
        RelationalDatabaseDataSourceConfigModel
    ] = Field(default=None, alias="relationalDatabaseConfig")
    event_bridge_config: Optional[EventBridgeDataSourceConfigModel] = Field(
        default=None, alias="eventBridgeConfig"
    )


class UpdateDataSourceRequestModel(BaseModel):
    api_id: str = Field(alias="apiId")
    name: str = Field(alias="name")
    type: Literal[
        "AMAZON_DYNAMODB",
        "AMAZON_ELASTICSEARCH",
        "AMAZON_EVENTBRIDGE",
        "AMAZON_OPENSEARCH_SERVICE",
        "AWS_LAMBDA",
        "HTTP",
        "NONE",
        "RELATIONAL_DATABASE",
    ] = Field(alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    service_role_arn: Optional[str] = Field(default=None, alias="serviceRoleArn")
    dynamodb_config: Optional[DynamodbDataSourceConfigModel] = Field(
        default=None, alias="dynamodbConfig"
    )
    lambda_config: Optional[LambdaDataSourceConfigModel] = Field(
        default=None, alias="lambdaConfig"
    )
    elasticsearch_config: Optional[ElasticsearchDataSourceConfigModel] = Field(
        default=None, alias="elasticsearchConfig"
    )
    open_search_service_config: Optional[
        OpenSearchServiceDataSourceConfigModel
    ] = Field(default=None, alias="openSearchServiceConfig")
    http_config: Optional[HttpDataSourceConfigModel] = Field(
        default=None, alias="httpConfig"
    )
    relational_database_config: Optional[
        RelationalDatabaseDataSourceConfigModel
    ] = Field(default=None, alias="relationalDatabaseConfig")
    event_bridge_config: Optional[EventBridgeDataSourceConfigModel] = Field(
        default=None, alias="eventBridgeConfig"
    )


class EvaluateCodeResponseModel(BaseModel):
    evaluation_result: str = Field(alias="evaluationResult")
    error: EvaluateCodeErrorDetailModel = Field(alias="error")
    logs: List[str] = Field(alias="logs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFunctionResponseModel(BaseModel):
    function_configuration: FunctionConfigurationModel = Field(
        alias="functionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFunctionResponseModel(BaseModel):
    function_configuration: FunctionConfigurationModel = Field(
        alias="functionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFunctionsResponseModel(BaseModel):
    functions: List[FunctionConfigurationModel] = Field(alias="functions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFunctionResponseModel(BaseModel):
    function_configuration: FunctionConfigurationModel = Field(
        alias="functionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResolverResponseModel(BaseModel):
    resolver: ResolverModel = Field(alias="resolver")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResolverResponseModel(BaseModel):
    resolver: ResolverModel = Field(alias="resolver")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolversByFunctionResponseModel(BaseModel):
    resolvers: List[ResolverModel] = Field(alias="resolvers")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResolversResponseModel(BaseModel):
    resolvers: List[ResolverModel] = Field(alias="resolvers")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResolverResponseModel(BaseModel):
    resolver: ResolverModel = Field(alias="resolver")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceResponseModel(BaseModel):
    data_source: DataSourceModel = Field(alias="dataSource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataSourceResponseModel(BaseModel):
    data_source: DataSourceModel = Field(alias="dataSource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataSourcesResponseModel(BaseModel):
    data_sources: List[DataSourceModel] = Field(alias="dataSources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSourceResponseModel(BaseModel):
    data_source: DataSourceModel = Field(alias="dataSource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
