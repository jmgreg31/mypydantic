# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BackendAPIAppSyncAuthSettingsModel(BaseModel):
    cognito_user_pool_id: Optional[str] = Field(default=None, alias="CognitoUserPoolId")
    description: Optional[str] = Field(default=None, alias="Description")
    expiration_time: Optional[float] = Field(default=None, alias="ExpirationTime")
    open_idauth_ttl: Optional[str] = Field(default=None, alias="OpenIDAuthTTL")
    open_idclient_id: Optional[str] = Field(default=None, alias="OpenIDClientId")
    open_idiat_ttl: Optional[str] = Field(default=None, alias="OpenIDIatTTL")
    open_idissue_url: Optional[str] = Field(default=None, alias="OpenIDIssueURL")
    open_idprovider_name: Optional[str] = Field(
        default=None, alias="OpenIDProviderName"
    )


class BackendAPIConflictResolutionModel(BaseModel):
    resolution_strategy: Optional[
        Literal["AUTOMERGE", "LAMBDA", "NONE", "OPTIMISTIC_CONCURRENCY"]
    ] = Field(default=None, alias="ResolutionStrategy")


class BackendAuthAppleProviderConfigModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    private_key: Optional[str] = Field(default=None, alias="PrivateKey")
    team_id: Optional[str] = Field(default=None, alias="TeamId")


class BackendAuthSocialProviderConfigModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="ClientId")
    client_secret: Optional[str] = Field(default=None, alias="ClientSecret")


class BackendJobRespObjModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    create_time: Optional[str] = Field(default=None, alias="CreateTime")
    error: Optional[str] = Field(default=None, alias="Error")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    operation: Optional[str] = Field(default=None, alias="Operation")
    status: Optional[str] = Field(default=None, alias="Status")
    update_time: Optional[str] = Field(default=None, alias="UpdateTime")


class BackendStoragePermissionsModel(BaseModel):
    authenticated: Sequence[Literal["CREATE_AND_UPDATE", "DELETE", "READ"]] = Field(
        alias="Authenticated"
    )
    un_authenticated: Optional[
        Sequence[Literal["CREATE_AND_UPDATE", "DELETE", "READ"]]
    ] = Field(default=None, alias="UnAuthenticated")


class CloneBackendRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    target_environment_name: str = Field(alias="TargetEnvironmentName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EmailSettingsModel(BaseModel):
    email_message: Optional[str] = Field(default=None, alias="EmailMessage")
    email_subject: Optional[str] = Field(default=None, alias="EmailSubject")


class SmsSettingsModel(BaseModel):
    sms_message: Optional[str] = Field(default=None, alias="SmsMessage")


class CreateBackendAuthIdentityPoolConfigModel(BaseModel):
    identity_pool_name: str = Field(alias="IdentityPoolName")
    unauthenticated_login: bool = Field(alias="UnauthenticatedLogin")


class SettingsModel(BaseModel):
    mfa_types: Optional[Sequence[Literal["SMS", "TOTP"]]] = Field(
        default=None, alias="MfaTypes"
    )
    sms_message: Optional[str] = Field(default=None, alias="SmsMessage")


class CreateBackendAuthPasswordPolicyConfigModel(BaseModel):
    minimum_length: float = Field(alias="MinimumLength")
    additional_constraints: Optional[
        Sequence[
            Literal[
                "REQUIRE_DIGIT",
                "REQUIRE_LOWERCASE",
                "REQUIRE_SYMBOL",
                "REQUIRE_UPPERCASE",
            ]
        ]
    ] = Field(default=None, alias="AdditionalConstraints")


class CreateBackendConfigRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_manager_app_id: Optional[str] = Field(
        default=None, alias="BackendManagerAppId"
    )


class CreateBackendRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    app_name: str = Field(alias="AppName")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_config: Optional[Mapping[str, Any]] = Field(
        default=None, alias="ResourceConfig"
    )
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class CreateTokenRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")


class DeleteBackendAuthRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")


class DeleteBackendRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")


class DeleteBackendStorageRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")
    service_name: Literal["S3"] = Field(alias="ServiceName")


class DeleteTokenRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    session_id: str = Field(alias="SessionId")


class GenerateBackendAPIModelsRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")


class GetBackendAPIModelsRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")


class GetBackendAuthRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")


class GetBackendJobRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: str = Field(alias="JobId")


class GetBackendRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: Optional[str] = Field(
        default=None, alias="BackendEnvironmentName"
    )


class GetBackendStorageRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")


class GetTokenRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    session_id: str = Field(alias="SessionId")


class ImportBackendAuthRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    native_client_id: str = Field(alias="NativeClientId")
    user_pool_id: str = Field(alias="UserPoolId")
    web_client_id: str = Field(alias="WebClientId")
    identity_pool_id: Optional[str] = Field(default=None, alias="IdentityPoolId")


class ImportBackendStorageRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    service_name: Literal["S3"] = Field(alias="ServiceName")
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBackendJobsRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    operation: Optional[str] = Field(default=None, alias="Operation")
    status: Optional[str] = Field(default=None, alias="Status")


class ListS3BucketsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class S3BucketInfoModel(BaseModel):
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    name: Optional[str] = Field(default=None, alias="Name")


class LoginAuthConfigReqObjModel(BaseModel):
    aws_cognito_identity_pool_id: Optional[str] = Field(
        default=None, alias="AwsCognitoIdentityPoolId"
    )
    aws_cognito_region: Optional[str] = Field(default=None, alias="AwsCognitoRegion")
    aws_user_pools_id: Optional[str] = Field(default=None, alias="AwsUserPoolsId")
    aws_user_pools_web_client_id: Optional[str] = Field(
        default=None, alias="AwsUserPoolsWebClientId"
    )


class RemoveAllBackendsRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    clean_amplify_app: Optional[bool] = Field(default=None, alias="CleanAmplifyApp")


class RemoveBackendConfigRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")


class UpdateBackendAuthIdentityPoolConfigModel(BaseModel):
    unauthenticated_login: Optional[bool] = Field(
        default=None, alias="UnauthenticatedLogin"
    )


class UpdateBackendAuthPasswordPolicyConfigModel(BaseModel):
    additional_constraints: Optional[
        Sequence[
            Literal[
                "REQUIRE_DIGIT",
                "REQUIRE_LOWERCASE",
                "REQUIRE_SYMBOL",
                "REQUIRE_UPPERCASE",
            ]
        ]
    ] = Field(default=None, alias="AdditionalConstraints")
    minimum_length: Optional[float] = Field(default=None, alias="MinimumLength")


class UpdateBackendJobRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: str = Field(alias="JobId")
    operation: Optional[str] = Field(default=None, alias="Operation")
    status: Optional[str] = Field(default=None, alias="Status")


class BackendAPIAuthTypeModel(BaseModel):
    mode: Optional[
        Literal["AMAZON_COGNITO_USER_POOLS", "API_KEY", "AWS_IAM", "OPENID_CONNECT"]
    ] = Field(default=None, alias="Mode")
    settings: Optional[BackendAPIAppSyncAuthSettingsModel] = Field(
        default=None, alias="Settings"
    )


class SocialProviderSettingsModel(BaseModel):
    facebook: Optional[BackendAuthSocialProviderConfigModel] = Field(
        default=None, alias="Facebook"
    )
    google: Optional[BackendAuthSocialProviderConfigModel] = Field(
        default=None, alias="Google"
    )
    login_with_amazon: Optional[BackendAuthSocialProviderConfigModel] = Field(
        default=None, alias="LoginWithAmazon"
    )
    sign_in_with_apple: Optional[BackendAuthAppleProviderConfigModel] = Field(
        default=None, alias="SignInWithApple"
    )


class CreateBackendStorageResourceConfigModel(BaseModel):
    permissions: BackendStoragePermissionsModel = Field(alias="Permissions")
    service_name: Literal["S3"] = Field(alias="ServiceName")
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")


class GetBackendStorageResourceConfigModel(BaseModel):
    imported: bool = Field(alias="Imported")
    service_name: Literal["S3"] = Field(alias="ServiceName")
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    permissions: Optional[BackendStoragePermissionsModel] = Field(
        default=None, alias="Permissions"
    )


class UpdateBackendStorageResourceConfigModel(BaseModel):
    permissions: BackendStoragePermissionsModel = Field(alias="Permissions")
    service_name: Literal["S3"] = Field(alias="ServiceName")


class CloneBackendResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackendAPIResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackendAuthResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackendConfigResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: str = Field(alias="JobId")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackendResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackendStorageResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: str = Field(alias="JobId")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTokenResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    challenge_code: str = Field(alias="ChallengeCode")
    session_id: str = Field(alias="SessionId")
    ttl: str = Field(alias="Ttl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBackendAPIResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBackendAuthResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBackendResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBackendStorageResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: str = Field(alias="JobId")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTokenResponseModel(BaseModel):
    is_success: bool = Field(alias="IsSuccess")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateBackendAPIModelsResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackendAPIModelsResponseModel(BaseModel):
    models: str = Field(alias="Models")
    status: Literal["LATEST", "STALE"] = Field(alias="Status")
    model_introspection_schema: str = Field(alias="ModelIntrospectionSchema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackendJobResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    create_time: str = Field(alias="CreateTime")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    update_time: str = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBackendResponseModel(BaseModel):
    amplify_feature_flags: str = Field(alias="AmplifyFeatureFlags")
    amplify_meta_config: str = Field(alias="AmplifyMetaConfig")
    app_id: str = Field(alias="AppId")
    app_name: str = Field(alias="AppName")
    backend_environment_list: List[str] = Field(alias="BackendEnvironmentList")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTokenResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    challenge_code: str = Field(alias="ChallengeCode")
    session_id: str = Field(alias="SessionId")
    ttl: str = Field(alias="Ttl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportBackendAuthResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportBackendStorageResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: str = Field(alias="JobId")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBackendJobsResponseModel(BaseModel):
    jobs: List[BackendJobRespObjModel] = Field(alias="Jobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveAllBackendsResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemoveBackendConfigResponseModel(BaseModel):
    error: str = Field(alias="Error")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendAPIResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendAuthResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendJobResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    create_time: str = Field(alias="CreateTime")
    error: str = Field(alias="Error")
    job_id: str = Field(alias="JobId")
    operation: str = Field(alias="Operation")
    status: str = Field(alias="Status")
    update_time: str = Field(alias="UpdateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendStorageResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: str = Field(alias="JobId")
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBackendAuthForgotPasswordConfigModel(BaseModel):
    delivery_method: Literal["EMAIL", "SMS"] = Field(alias="DeliveryMethod")
    email_settings: Optional[EmailSettingsModel] = Field(
        default=None, alias="EmailSettings"
    )
    sms_settings: Optional[SmsSettingsModel] = Field(default=None, alias="SmsSettings")


class CreateBackendAuthVerificationMessageConfigModel(BaseModel):
    delivery_method: Literal["EMAIL", "SMS"] = Field(alias="DeliveryMethod")
    email_settings: Optional[EmailSettingsModel] = Field(
        default=None, alias="EmailSettings"
    )
    sms_settings: Optional[SmsSettingsModel] = Field(default=None, alias="SmsSettings")


class UpdateBackendAuthForgotPasswordConfigModel(BaseModel):
    delivery_method: Optional[Literal["EMAIL", "SMS"]] = Field(
        default=None, alias="DeliveryMethod"
    )
    email_settings: Optional[EmailSettingsModel] = Field(
        default=None, alias="EmailSettings"
    )
    sms_settings: Optional[SmsSettingsModel] = Field(default=None, alias="SmsSettings")


class UpdateBackendAuthVerificationMessageConfigModel(BaseModel):
    delivery_method: Literal["EMAIL", "SMS"] = Field(alias="DeliveryMethod")
    email_settings: Optional[EmailSettingsModel] = Field(
        default=None, alias="EmailSettings"
    )
    sms_settings: Optional[SmsSettingsModel] = Field(default=None, alias="SmsSettings")


class CreateBackendAuthMFAConfigModel(BaseModel):
    mfamode: Literal["OFF", "ON", "OPTIONAL"] = Field(alias="MFAMode")
    settings: Optional[SettingsModel] = Field(default=None, alias="Settings")


class UpdateBackendAuthMFAConfigModel(BaseModel):
    mfamode: Optional[Literal["OFF", "ON", "OPTIONAL"]] = Field(
        default=None, alias="MFAMode"
    )
    settings: Optional[SettingsModel] = Field(default=None, alias="Settings")


class ListBackendJobsRequestListBackendJobsPaginateModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    operation: Optional[str] = Field(default=None, alias="Operation")
    status: Optional[str] = Field(default=None, alias="Status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListS3BucketsResponseModel(BaseModel):
    buckets: List[S3BucketInfoModel] = Field(alias="Buckets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendConfigRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    login_auth_config: Optional[LoginAuthConfigReqObjModel] = Field(
        default=None, alias="LoginAuthConfig"
    )


class UpdateBackendConfigResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_manager_app_id: str = Field(alias="BackendManagerAppId")
    error: str = Field(alias="Error")
    login_auth_config: LoginAuthConfigReqObjModel = Field(alias="LoginAuthConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BackendAPIResourceConfigModel(BaseModel):
    additional_auth_types: Optional[Sequence[BackendAPIAuthTypeModel]] = Field(
        default=None, alias="AdditionalAuthTypes"
    )
    api_name: Optional[str] = Field(default=None, alias="ApiName")
    conflict_resolution: Optional[BackendAPIConflictResolutionModel] = Field(
        default=None, alias="ConflictResolution"
    )
    default_auth_type: Optional[BackendAPIAuthTypeModel] = Field(
        default=None, alias="DefaultAuthType"
    )
    service: Optional[str] = Field(default=None, alias="Service")
    transform_schema: Optional[str] = Field(default=None, alias="TransformSchema")


class CreateBackendAuthOAuthConfigModel(BaseModel):
    oauth_grant_type: Literal["CODE", "IMPLICIT"] = Field(alias="OAuthGrantType")
    oauth_scopes: Sequence[
        Literal["AWS_COGNITO_SIGNIN_USER_ADMIN", "EMAIL", "OPENID", "PHONE", "PROFILE"]
    ] = Field(alias="OAuthScopes")
    redirect_sign_in_uris: Sequence[str] = Field(alias="RedirectSignInURIs")
    redirect_sign_out_uris: Sequence[str] = Field(alias="RedirectSignOutURIs")
    domain_prefix: Optional[str] = Field(default=None, alias="DomainPrefix")
    social_provider_settings: Optional[SocialProviderSettingsModel] = Field(
        default=None, alias="SocialProviderSettings"
    )


class UpdateBackendAuthOAuthConfigModel(BaseModel):
    domain_prefix: Optional[str] = Field(default=None, alias="DomainPrefix")
    oauth_grant_type: Optional[Literal["CODE", "IMPLICIT"]] = Field(
        default=None, alias="OAuthGrantType"
    )
    oauth_scopes: Optional[
        Sequence[
            Literal[
                "AWS_COGNITO_SIGNIN_USER_ADMIN", "EMAIL", "OPENID", "PHONE", "PROFILE"
            ]
        ]
    ] = Field(default=None, alias="OAuthScopes")
    redirect_sign_in_uris: Optional[Sequence[str]] = Field(
        default=None, alias="RedirectSignInURIs"
    )
    redirect_sign_out_uris: Optional[Sequence[str]] = Field(
        default=None, alias="RedirectSignOutURIs"
    )
    social_provider_settings: Optional[SocialProviderSettingsModel] = Field(
        default=None, alias="SocialProviderSettings"
    )


class CreateBackendStorageRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_config: CreateBackendStorageResourceConfigModel = Field(
        alias="ResourceConfig"
    )
    resource_name: str = Field(alias="ResourceName")


class GetBackendStorageResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_config: GetBackendStorageResourceConfigModel = Field(
        alias="ResourceConfig"
    )
    resource_name: str = Field(alias="ResourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendStorageRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_config: UpdateBackendStorageResourceConfigModel = Field(
        alias="ResourceConfig"
    )
    resource_name: str = Field(alias="ResourceName")


class CreateBackendAPIRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_config: BackendAPIResourceConfigModel = Field(alias="ResourceConfig")
    resource_name: str = Field(alias="ResourceName")


class DeleteBackendAPIRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")
    resource_config: Optional[BackendAPIResourceConfigModel] = Field(
        default=None, alias="ResourceConfig"
    )


class GetBackendAPIRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")
    resource_config: Optional[BackendAPIResourceConfigModel] = Field(
        default=None, alias="ResourceConfig"
    )


class GetBackendAPIResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    resource_config: BackendAPIResourceConfigModel = Field(alias="ResourceConfig")
    resource_name: str = Field(alias="ResourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendAPIRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_name: str = Field(alias="ResourceName")
    resource_config: Optional[BackendAPIResourceConfigModel] = Field(
        default=None, alias="ResourceConfig"
    )


class CreateBackendAuthUserPoolConfigModel(BaseModel):
    required_sign_up_attributes: Sequence[
        Literal[
            "ADDRESS",
            "BIRTHDATE",
            "EMAIL",
            "FAMILY_NAME",
            "GENDER",
            "GIVEN_NAME",
            "LOCALE",
            "MIDDLE_NAME",
            "NAME",
            "NICKNAME",
            "PHONE_NUMBER",
            "PICTURE",
            "PREFERRED_USERNAME",
            "PROFILE",
            "UPDATED_AT",
            "WEBSITE",
            "ZONE_INFO",
        ]
    ] = Field(alias="RequiredSignUpAttributes")
    sign_in_method: Literal[
        "EMAIL", "EMAIL_AND_PHONE_NUMBER", "PHONE_NUMBER", "USERNAME"
    ] = Field(alias="SignInMethod")
    user_pool_name: str = Field(alias="UserPoolName")
    forgot_password: Optional[CreateBackendAuthForgotPasswordConfigModel] = Field(
        default=None, alias="ForgotPassword"
    )
    mfa: Optional[CreateBackendAuthMFAConfigModel] = Field(default=None, alias="Mfa")
    oauth: Optional[CreateBackendAuthOAuthConfigModel] = Field(
        default=None, alias="OAuth"
    )
    password_policy: Optional[CreateBackendAuthPasswordPolicyConfigModel] = Field(
        default=None, alias="PasswordPolicy"
    )
    verification_message: Optional[
        CreateBackendAuthVerificationMessageConfigModel
    ] = Field(default=None, alias="VerificationMessage")


class UpdateBackendAuthUserPoolConfigModel(BaseModel):
    forgot_password: Optional[UpdateBackendAuthForgotPasswordConfigModel] = Field(
        default=None, alias="ForgotPassword"
    )
    mfa: Optional[UpdateBackendAuthMFAConfigModel] = Field(default=None, alias="Mfa")
    oauth: Optional[UpdateBackendAuthOAuthConfigModel] = Field(
        default=None, alias="OAuth"
    )
    password_policy: Optional[UpdateBackendAuthPasswordPolicyConfigModel] = Field(
        default=None, alias="PasswordPolicy"
    )
    verification_message: Optional[
        UpdateBackendAuthVerificationMessageConfigModel
    ] = Field(default=None, alias="VerificationMessage")


class CreateBackendAuthResourceConfigModel(BaseModel):
    auth_resources: Literal["IDENTITY_POOL_AND_USER_POOL", "USER_POOL_ONLY"] = Field(
        alias="AuthResources"
    )
    service: Literal["COGNITO"] = Field(alias="Service")
    user_pool_configs: CreateBackendAuthUserPoolConfigModel = Field(
        alias="UserPoolConfigs"
    )
    identity_pool_configs: Optional[CreateBackendAuthIdentityPoolConfigModel] = Field(
        default=None, alias="IdentityPoolConfigs"
    )


class UpdateBackendAuthResourceConfigModel(BaseModel):
    auth_resources: Literal["IDENTITY_POOL_AND_USER_POOL", "USER_POOL_ONLY"] = Field(
        alias="AuthResources"
    )
    service: Literal["COGNITO"] = Field(alias="Service")
    user_pool_configs: UpdateBackendAuthUserPoolConfigModel = Field(
        alias="UserPoolConfigs"
    )
    identity_pool_configs: Optional[UpdateBackendAuthIdentityPoolConfigModel] = Field(
        default=None, alias="IdentityPoolConfigs"
    )


class CreateBackendAuthRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_config: CreateBackendAuthResourceConfigModel = Field(
        alias="ResourceConfig"
    )
    resource_name: str = Field(alias="ResourceName")


class GetBackendAuthResponseModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    error: str = Field(alias="Error")
    resource_config: CreateBackendAuthResourceConfigModel = Field(
        alias="ResourceConfig"
    )
    resource_name: str = Field(alias="ResourceName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBackendAuthRequestModel(BaseModel):
    app_id: str = Field(alias="AppId")
    backend_environment_name: str = Field(alias="BackendEnvironmentName")
    resource_config: UpdateBackendAuthResourceConfigModel = Field(
        alias="ResourceConfig"
    )
    resource_name: str = Field(alias="ResourceName")
