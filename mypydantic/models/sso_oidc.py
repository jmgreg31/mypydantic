# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from typing import Dict, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CreateTokenRequestModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    grant_type: str = Field(alias="grantType")
    device_code: Optional[str] = Field(default=None, alias="deviceCode")
    code: Optional[str] = Field(default=None, alias="code")
    refresh_token: Optional[str] = Field(default=None, alias="refreshToken")
    scope: Optional[Sequence[str]] = Field(default=None, alias="scope")
    redirect_uri: Optional[str] = Field(default=None, alias="redirectUri")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class RegisterClientRequestModel(BaseModel):
    client_name: str = Field(alias="clientName")
    client_type: str = Field(alias="clientType")
    scopes: Optional[Sequence[str]] = Field(default=None, alias="scopes")


class StartDeviceAuthorizationRequestModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    start_url: str = Field(alias="startUrl")


class CreateTokenResponseModel(BaseModel):
    access_token: str = Field(alias="accessToken")
    token_type: str = Field(alias="tokenType")
    expires_in: int = Field(alias="expiresIn")
    refresh_token: str = Field(alias="refreshToken")
    id_token: str = Field(alias="idToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterClientResponseModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    client_id_issued_at: int = Field(alias="clientIdIssuedAt")
    client_secret_expires_at: int = Field(alias="clientSecretExpiresAt")
    authorization_endpoint: str = Field(alias="authorizationEndpoint")
    token_endpoint: str = Field(alias="tokenEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDeviceAuthorizationResponseModel(BaseModel):
    device_code: str = Field(alias="deviceCode")
    user_code: str = Field(alias="userCode")
    verification_uri: str = Field(alias="verificationUri")
    verification_uri_complete: str = Field(alias="verificationUriComplete")
    expires_in: int = Field(alias="expiresIn")
    interval: int = Field(alias="interval")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
