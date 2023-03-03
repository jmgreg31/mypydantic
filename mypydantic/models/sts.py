# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class PolicyDescriptorTypeModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class AssumedRoleUserModel(BaseModel):
    assumed_role_id: str = Field(alias="AssumedRoleId")
    arn: str = Field(alias="Arn")


class CredentialsModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")
    secret_access_key: str = Field(alias="SecretAccessKey")
    session_token: str = Field(alias="SessionToken")
    expiration: datetime = Field(alias="Expiration")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DecodeAuthorizationMessageRequestModel(BaseModel):
    encoded_message: str = Field(alias="EncodedMessage")


class FederatedUserModel(BaseModel):
    federated_user_id: str = Field(alias="FederatedUserId")
    arn: str = Field(alias="Arn")


class GetAccessKeyInfoRequestModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")


class GetSessionTokenRequestModel(BaseModel):
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")
    serial_number: Optional[str] = Field(default=None, alias="SerialNumber")
    token_code: Optional[str] = Field(default=None, alias="TokenCode")


class AssumeRoleWithSAMLRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    principal_arn: str = Field(alias="PrincipalArn")
    s_aml_assertion: str = Field(alias="SAMLAssertion")
    policy_arns: Optional[Sequence[PolicyDescriptorTypeModel]] = Field(
        default=None, alias="PolicyArns"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")


class AssumeRoleWithWebIdentityRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    role_session_name: str = Field(alias="RoleSessionName")
    web_identity_token: str = Field(alias="WebIdentityToken")
    provider_id: Optional[str] = Field(default=None, alias="ProviderId")
    policy_arns: Optional[Sequence[PolicyDescriptorTypeModel]] = Field(
        default=None, alias="PolicyArns"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")


class AssumeRoleRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    role_session_name: str = Field(alias="RoleSessionName")
    policy_arns: Optional[Sequence[PolicyDescriptorTypeModel]] = Field(
        default=None, alias="PolicyArns"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    transitive_tag_keys: Optional[Sequence[str]] = Field(
        default=None, alias="TransitiveTagKeys"
    )
    external_id: Optional[str] = Field(default=None, alias="ExternalId")
    serial_number: Optional[str] = Field(default=None, alias="SerialNumber")
    token_code: Optional[str] = Field(default=None, alias="TokenCode")
    source_identity: Optional[str] = Field(default=None, alias="SourceIdentity")


class GetFederationTokenRequestModel(BaseModel):
    name: str = Field(alias="Name")
    policy: Optional[str] = Field(default=None, alias="Policy")
    policy_arns: Optional[Sequence[PolicyDescriptorTypeModel]] = Field(
        default=None, alias="PolicyArns"
    )
    duration_seconds: Optional[int] = Field(default=None, alias="DurationSeconds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class AssumeRoleResponseModel(BaseModel):
    credentials: CredentialsModel = Field(alias="Credentials")
    assumed_role_user: AssumedRoleUserModel = Field(alias="AssumedRoleUser")
    packed_policy_size: int = Field(alias="PackedPolicySize")
    source_identity: str = Field(alias="SourceIdentity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssumeRoleWithSAMLResponseModel(BaseModel):
    credentials: CredentialsModel = Field(alias="Credentials")
    assumed_role_user: AssumedRoleUserModel = Field(alias="AssumedRoleUser")
    packed_policy_size: int = Field(alias="PackedPolicySize")
    subject: str = Field(alias="Subject")
    subject_type: str = Field(alias="SubjectType")
    issuer: str = Field(alias="Issuer")
    audience: str = Field(alias="Audience")
    name_qualifier: str = Field(alias="NameQualifier")
    source_identity: str = Field(alias="SourceIdentity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssumeRoleWithWebIdentityResponseModel(BaseModel):
    credentials: CredentialsModel = Field(alias="Credentials")
    subject_from_web_identity_token: str = Field(alias="SubjectFromWebIdentityToken")
    assumed_role_user: AssumedRoleUserModel = Field(alias="AssumedRoleUser")
    packed_policy_size: int = Field(alias="PackedPolicySize")
    provider: str = Field(alias="Provider")
    audience: str = Field(alias="Audience")
    source_identity: str = Field(alias="SourceIdentity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DecodeAuthorizationMessageResponseModel(BaseModel):
    decoded_message: str = Field(alias="DecodedMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessKeyInfoResponseModel(BaseModel):
    account: str = Field(alias="Account")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCallerIdentityResponseModel(BaseModel):
    user_id: str = Field(alias="UserId")
    account: str = Field(alias="Account")
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSessionTokenResponseModel(BaseModel):
    credentials: CredentialsModel = Field(alias="Credentials")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFederationTokenResponseModel(BaseModel):
    credentials: CredentialsModel = Field(alias="Credentials")
    federated_user: FederatedUserModel = Field(alias="FederatedUser")
    packed_policy_size: int = Field(alias="PackedPolicySize")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
