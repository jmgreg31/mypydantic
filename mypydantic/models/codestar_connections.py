# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ConnectionModel(BaseModel):
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    provider_type: Optional[
        Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"]
    ] = Field(default=None, alias="ProviderType")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    connection_status: Optional[Literal["AVAILABLE", "ERROR", "PENDING"]] = Field(
        default=None, alias="ConnectionStatus"
    )
    host_arn: Optional[str] = Field(default=None, alias="HostArn")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class VpcConfigurationModel(BaseModel):
    vpc_id: str = Field(alias="VpcId")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    security_group_ids: Sequence[str] = Field(alias="SecurityGroupIds")
    tls_certificate: Optional[str] = Field(default=None, alias="TlsCertificate")


class DeleteConnectionInputRequestModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")


class DeleteHostInputRequestModel(BaseModel):
    host_arn: str = Field(alias="HostArn")


class GetConnectionInputRequestModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")


class GetHostInputRequestModel(BaseModel):
    host_arn: str = Field(alias="HostArn")


class ListConnectionsInputRequestModel(BaseModel):
    provider_type_filter: Optional[
        Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"]
    ] = Field(default=None, alias="ProviderTypeFilter")
    host_arn_filter: Optional[str] = Field(default=None, alias="HostArnFilter")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHostsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class CreateConnectionInputRequestModel(BaseModel):
    connection_name: str = Field(alias="ConnectionName")
    provider_type: Optional[
        Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"]
    ] = Field(default=None, alias="ProviderType")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    host_arn: Optional[str] = Field(default=None, alias="HostArn")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateConnectionOutputModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHostOutputModel(BaseModel):
    host_arn: str = Field(alias="HostArn")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectionOutputModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConnectionsOutputModel(BaseModel):
    connections: List[ConnectionModel] = Field(alias="Connections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHostInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    provider_type: Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"] = Field(
        alias="ProviderType"
    )
    provider_endpoint: str = Field(alias="ProviderEndpoint")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GetHostOutputModel(BaseModel):
    name: str = Field(alias="Name")
    status: str = Field(alias="Status")
    provider_type: Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"] = Field(
        alias="ProviderType"
    )
    provider_endpoint: str = Field(alias="ProviderEndpoint")
    vpc_configuration: VpcConfigurationModel = Field(alias="VpcConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HostModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    host_arn: Optional[str] = Field(default=None, alias="HostArn")
    provider_type: Optional[
        Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"]
    ] = Field(default=None, alias="ProviderType")
    provider_endpoint: Optional[str] = Field(default=None, alias="ProviderEndpoint")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class UpdateHostInputRequestModel(BaseModel):
    host_arn: str = Field(alias="HostArn")
    provider_endpoint: Optional[str] = Field(default=None, alias="ProviderEndpoint")
    vpc_configuration: Optional[VpcConfigurationModel] = Field(
        default=None, alias="VpcConfiguration"
    )


class ListHostsOutputModel(BaseModel):
    hosts: List[HostModel] = Field(alias="Hosts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
