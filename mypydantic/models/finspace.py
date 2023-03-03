# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class FederationParametersModel(BaseModel):
    saml_metadata_document: Optional[str] = Field(
        default=None, alias="samlMetadataDocument"
    )
    saml_metadata_url: Optional[str] = Field(default=None, alias="samlMetadataURL")
    application_call_back_url: Optional[str] = Field(
        default=None, alias="applicationCallBackURL"
    )
    federation_urn: Optional[str] = Field(default=None, alias="federationURN")
    federation_provider_name: Optional[str] = Field(
        default=None, alias="federationProviderName"
    )
    attribute_map: Optional[Mapping[str, str]] = Field(
        default=None, alias="attributeMap"
    )


class SuperuserParametersModel(BaseModel):
    email_address: str = Field(alias="emailAddress")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")


class GetEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")


class ListEnvironmentsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class EnvironmentModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    environment_id: Optional[str] = Field(default=None, alias="environmentId")
    aws_account_id: Optional[str] = Field(default=None, alias="awsAccountId")
    status: Optional[
        Literal[
            "CREATED",
            "CREATE_REQUESTED",
            "CREATING",
            "DELETED",
            "DELETE_REQUESTED",
            "DELETING",
            "FAILED_CREATION",
            "FAILED_DELETION",
            "RETRY_DELETION",
            "SUSPENDED",
        ]
    ] = Field(default=None, alias="status")
    environment_url: Optional[str] = Field(default=None, alias="environmentUrl")
    description: Optional[str] = Field(default=None, alias="description")
    environment_arn: Optional[str] = Field(default=None, alias="environmentArn")
    sage_maker_studio_domain_url: Optional[str] = Field(
        default=None, alias="sageMakerStudioDomainUrl"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    dedicated_service_account_id: Optional[str] = Field(
        default=None, alias="dedicatedServiceAccountId"
    )
    federation_mode: Optional[Literal["FEDERATED", "LOCAL"]] = Field(
        default=None, alias="federationMode"
    )
    federation_parameters: Optional[FederationParametersModel] = Field(
        default=None, alias="federationParameters"
    )


class UpdateEnvironmentRequestModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    federation_mode: Optional[Literal["FEDERATED", "LOCAL"]] = Field(
        default=None, alias="federationMode"
    )
    federation_parameters: Optional[FederationParametersModel] = Field(
        default=None, alias="federationParameters"
    )


class CreateEnvironmentRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    federation_mode: Optional[Literal["FEDERATED", "LOCAL"]] = Field(
        default=None, alias="federationMode"
    )
    federation_parameters: Optional[FederationParametersModel] = Field(
        default=None, alias="federationParameters"
    )
    superuser_parameters: Optional[SuperuserParametersModel] = Field(
        default=None, alias="superuserParameters"
    )
    data_bundles: Optional[Sequence[str]] = Field(default=None, alias="dataBundles")


class CreateEnvironmentResponseModel(BaseModel):
    environment_id: str = Field(alias="environmentId")
    environment_arn: str = Field(alias="environmentArn")
    environment_url: str = Field(alias="environmentUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnvironmentResponseModel(BaseModel):
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnvironmentsResponseModel(BaseModel):
    environments: List[EnvironmentModel] = Field(alias="environments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEnvironmentResponseModel(BaseModel):
    environment: EnvironmentModel = Field(alias="environment")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
