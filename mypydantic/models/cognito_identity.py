# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CognitoIdentityProviderModel(BaseModel):
    provider_name: Optional[str] = Field(default=None, alias="ProviderName")
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    server_side_token_check: Optional[bool] = Field(
        default=None, alias="ServerSideTokenCheck"
    )


class CredentialsModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="AccessKeyId")
    secret_key: Optional[str] = Field(default=None, alias="SecretKey")
    session_token: Optional[str] = Field(default=None, alias="SessionToken")
    expiration: Optional[datetime] = Field(default=None, alias="Expiration")


class DeleteIdentitiesInputRequestModel(BaseModel):
    identity_ids_to_delete: Sequence[str] = Field(alias="IdentityIdsToDelete")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class UnprocessedIdentityIdModel(BaseModel):
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    error_code: Optional[Literal["AccessDenied", "InternalServerError"]] = Field(
        default=None, alias="ErrorCode"
    )


class DeleteIdentityPoolInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class DescribeIdentityInputRequestModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")


class DescribeIdentityPoolInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class GetCredentialsForIdentityInputRequestModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    logins: Optional[Mapping[str, str]] = Field(default=None, alias="Logins")
    custom_role_arn: Optional[str] = Field(default=None, alias="CustomRoleArn")


class GetIdInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    logins: Optional[Mapping[str, str]] = Field(default=None, alias="Logins")


class GetIdentityPoolRolesInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")


class GetOpenIdTokenForDeveloperIdentityInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    logins: Mapping[str, str] = Field(alias="Logins")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    principal_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="PrincipalTags"
    )
    token_duration: Optional[int] = Field(default=None, alias="TokenDuration")


class GetOpenIdTokenInputRequestModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    logins: Optional[Mapping[str, str]] = Field(default=None, alias="Logins")


class GetPrincipalTagAttributeMapInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_provider_name: str = Field(alias="IdentityProviderName")


class IdentityDescriptionModel(BaseModel):
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    logins: Optional[List[str]] = Field(default=None, alias="Logins")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )


class IdentityPoolShortDescriptionModel(BaseModel):
    identity_pool_id: Optional[str] = Field(default=None, alias="IdentityPoolId")
    identity_pool_name: Optional[str] = Field(default=None, alias="IdentityPoolName")


class ListIdentitiesInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    max_results: int = Field(alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    hide_disabled: Optional[bool] = Field(default=None, alias="HideDisabled")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListIdentityPoolsInputRequestModel(BaseModel):
    max_results: int = Field(alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class LookupDeveloperIdentityInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    developer_user_identifier: Optional[str] = Field(
        default=None, alias="DeveloperUserIdentifier"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MappingRuleModel(BaseModel):
    claim: str = Field(alias="Claim")
    match_type: Literal["Contains", "Equals", "NotEqual", "StartsWith"] = Field(
        alias="MatchType"
    )
    value: str = Field(alias="Value")
    role_arn: str = Field(alias="RoleARN")


class MergeDeveloperIdentitiesInputRequestModel(BaseModel):
    source_user_identifier: str = Field(alias="SourceUserIdentifier")
    destination_user_identifier: str = Field(alias="DestinationUserIdentifier")
    developer_provider_name: str = Field(alias="DeveloperProviderName")
    identity_pool_id: str = Field(alias="IdentityPoolId")


class SetPrincipalTagAttributeMapInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_provider_name: str = Field(alias="IdentityProviderName")
    use_defaults: Optional[bool] = Field(default=None, alias="UseDefaults")
    principal_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="PrincipalTags"
    )


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UnlinkDeveloperIdentityInputRequestModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    identity_pool_id: str = Field(alias="IdentityPoolId")
    developer_provider_name: str = Field(alias="DeveloperProviderName")
    developer_user_identifier: str = Field(alias="DeveloperUserIdentifier")


class UnlinkIdentityInputRequestModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    logins: Mapping[str, str] = Field(alias="Logins")
    logins_to_remove: Sequence[str] = Field(alias="LoginsToRemove")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class CreateIdentityPoolInputRequestModel(BaseModel):
    identity_pool_name: str = Field(alias="IdentityPoolName")
    allow_unauthenticated_identities: bool = Field(
        alias="AllowUnauthenticatedIdentities"
    )
    allow_classic_flow: Optional[bool] = Field(default=None, alias="AllowClassicFlow")
    supported_login_providers: Optional[Mapping[str, str]] = Field(
        default=None, alias="SupportedLoginProviders"
    )
    developer_provider_name: Optional[str] = Field(
        default=None, alias="DeveloperProviderName"
    )
    open_id_connect_provider_arns: Optional[Sequence[str]] = Field(
        default=None, alias="OpenIdConnectProviderARNs"
    )
    cognito_identity_providers: Optional[
        Sequence[CognitoIdentityProviderModel]
    ] = Field(default=None, alias="CognitoIdentityProviders")
    saml_provider_arns: Optional[Sequence[str]] = Field(
        default=None, alias="SamlProviderARNs"
    )
    identity_pool_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="IdentityPoolTags"
    )


class IdentityPoolRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_pool_name: str = Field(alias="IdentityPoolName")
    allow_unauthenticated_identities: bool = Field(
        alias="AllowUnauthenticatedIdentities"
    )
    allow_classic_flow: Optional[bool] = Field(default=None, alias="AllowClassicFlow")
    supported_login_providers: Optional[Mapping[str, str]] = Field(
        default=None, alias="SupportedLoginProviders"
    )
    developer_provider_name: Optional[str] = Field(
        default=None, alias="DeveloperProviderName"
    )
    open_id_connect_provider_arns: Optional[Sequence[str]] = Field(
        default=None, alias="OpenIdConnectProviderARNs"
    )
    cognito_identity_providers: Optional[
        Sequence[CognitoIdentityProviderModel]
    ] = Field(default=None, alias="CognitoIdentityProviders")
    saml_provider_arns: Optional[Sequence[str]] = Field(
        default=None, alias="SamlProviderARNs"
    )
    identity_pool_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="IdentityPoolTags"
    )


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCredentialsForIdentityResponseModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    credentials: CredentialsModel = Field(alias="Credentials")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIdResponseModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOpenIdTokenForDeveloperIdentityResponseModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    token: str = Field(alias="Token")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOpenIdTokenResponseModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    token: str = Field(alias="Token")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPrincipalTagAttributeMapResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_provider_name: str = Field(alias="IdentityProviderName")
    use_defaults: bool = Field(alias="UseDefaults")
    principal_tags: Dict[str, str] = Field(alias="PrincipalTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IdentityDescriptionResponseMetadataModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    logins: List[str] = Field(alias="Logins")
    creation_date: datetime = Field(alias="CreationDate")
    last_modified_date: datetime = Field(alias="LastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IdentityPoolModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_pool_name: str = Field(alias="IdentityPoolName")
    allow_unauthenticated_identities: bool = Field(
        alias="AllowUnauthenticatedIdentities"
    )
    allow_classic_flow: bool = Field(alias="AllowClassicFlow")
    supported_login_providers: Dict[str, str] = Field(alias="SupportedLoginProviders")
    developer_provider_name: str = Field(alias="DeveloperProviderName")
    open_id_connect_provider_arns: List[str] = Field(alias="OpenIdConnectProviderARNs")
    cognito_identity_providers: List[CognitoIdentityProviderModel] = Field(
        alias="CognitoIdentityProviders"
    )
    saml_provider_arns: List[str] = Field(alias="SamlProviderARNs")
    identity_pool_tags: Dict[str, str] = Field(alias="IdentityPoolTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LookupDeveloperIdentityResponseModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    developer_user_identifier_list: List[str] = Field(
        alias="DeveloperUserIdentifierList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergeDeveloperIdentitiesResponseModel(BaseModel):
    identity_id: str = Field(alias="IdentityId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetPrincipalTagAttributeMapResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identity_provider_name: str = Field(alias="IdentityProviderName")
    use_defaults: bool = Field(alias="UseDefaults")
    principal_tags: Dict[str, str] = Field(alias="PrincipalTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteIdentitiesResponseModel(BaseModel):
    unprocessed_identity_ids: List[UnprocessedIdentityIdModel] = Field(
        alias="UnprocessedIdentityIds"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentitiesResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    identities: List[IdentityDescriptionModel] = Field(alias="Identities")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityPoolsResponseModel(BaseModel):
    identity_pools: List[IdentityPoolShortDescriptionModel] = Field(
        alias="IdentityPools"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityPoolsInputListIdentityPoolsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class RulesConfigurationTypeModel(BaseModel):
    rules: List[MappingRuleModel] = Field(alias="Rules")


class RoleMappingModel(BaseModel):
    type: Literal["Rules", "Token"] = Field(alias="Type")
    ambiguous_role_resolution: Optional[Literal["AuthenticatedRole", "Deny"]] = Field(
        default=None, alias="AmbiguousRoleResolution"
    )
    rules_configuration: Optional[RulesConfigurationTypeModel] = Field(
        default=None, alias="RulesConfiguration"
    )


class GetIdentityPoolRolesResponseModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    roles: Dict[str, str] = Field(alias="Roles")
    role_mappings: Dict[str, RoleMappingModel] = Field(alias="RoleMappings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetIdentityPoolRolesInputRequestModel(BaseModel):
    identity_pool_id: str = Field(alias="IdentityPoolId")
    roles: Mapping[str, str] = Field(alias="Roles")
    role_mappings: Optional[Mapping[str, RoleMappingModel]] = Field(
        default=None, alias="RoleMappings"
    )
