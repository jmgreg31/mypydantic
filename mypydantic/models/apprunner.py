# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateCustomDomainRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")
    domain_name: str = Field(alias="DomainName")
    enable_wwwsubdomain: Optional[bool] = Field(
        default=None, alias="EnableWWWSubdomain"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class VpcDNSTargetModel(BaseModel):
    vpc_ingress_connection_arn: Optional[str] = Field(
        default=None, alias="VpcIngressConnectionArn"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")


class AuthenticationConfigurationModel(BaseModel):
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    access_role_arn: Optional[str] = Field(default=None, alias="AccessRoleArn")


class AutoScalingConfigurationSummaryModel(BaseModel):
    auto_scaling_configuration_arn: Optional[str] = Field(
        default=None, alias="AutoScalingConfigurationArn"
    )
    auto_scaling_configuration_name: Optional[str] = Field(
        default=None, alias="AutoScalingConfigurationName"
    )
    auto_scaling_configuration_revision: Optional[int] = Field(
        default=None, alias="AutoScalingConfigurationRevision"
    )


class AutoScalingConfigurationModel(BaseModel):
    auto_scaling_configuration_arn: Optional[str] = Field(
        default=None, alias="AutoScalingConfigurationArn"
    )
    auto_scaling_configuration_name: Optional[str] = Field(
        default=None, alias="AutoScalingConfigurationName"
    )
    auto_scaling_configuration_revision: Optional[int] = Field(
        default=None, alias="AutoScalingConfigurationRevision"
    )
    latest: Optional[bool] = Field(default=None, alias="Latest")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    max_concurrency: Optional[int] = Field(default=None, alias="MaxConcurrency")
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    max_size: Optional[int] = Field(default=None, alias="MaxSize")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="DeletedAt")


class CertificateValidationRecordModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")
    status: Optional[Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]] = Field(
        default=None, alias="Status"
    )


class CodeConfigurationValuesModel(BaseModel):
    runtime: Literal[
        "CORRETTO_11",
        "CORRETTO_8",
        "DOTNET_6",
        "GO_1",
        "NODEJS_12",
        "NODEJS_14",
        "NODEJS_16",
        "PHP_81",
        "PYTHON_3",
        "RUBY_31",
    ] = Field(alias="Runtime")
    build_command: Optional[str] = Field(default=None, alias="BuildCommand")
    start_command: Optional[str] = Field(default=None, alias="StartCommand")
    port: Optional[str] = Field(default=None, alias="Port")
    runtime_environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="RuntimeEnvironmentVariables"
    )
    runtime_environment_secrets: Optional[Mapping[str, str]] = Field(
        default=None, alias="RuntimeEnvironmentSecrets"
    )


class SourceCodeVersionModel(BaseModel):
    type: Literal["BRANCH"] = Field(alias="Type")
    value: str = Field(alias="Value")


class ConnectionSummaryModel(BaseModel):
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    provider_type: Optional[Literal["GITHUB"]] = Field(
        default=None, alias="ProviderType"
    )
    status: Optional[
        Literal["AVAILABLE", "DELETED", "ERROR", "PENDING_HANDSHAKE"]
    ] = Field(default=None, alias="Status")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class ConnectionModel(BaseModel):
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    connection_arn: Optional[str] = Field(default=None, alias="ConnectionArn")
    provider_type: Optional[Literal["GITHUB"]] = Field(
        default=None, alias="ProviderType"
    )
    status: Optional[
        Literal["AVAILABLE", "DELETED", "ERROR", "PENDING_HANDSHAKE"]
    ] = Field(default=None, alias="Status")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class TraceConfigurationModel(BaseModel):
    vendor: Literal["AWSXRAY"] = Field(alias="Vendor")


class EncryptionConfigurationModel(BaseModel):
    kms_key: str = Field(alias="KmsKey")


class HealthCheckConfigurationModel(BaseModel):
    protocol: Optional[Literal["HTTP", "TCP"]] = Field(default=None, alias="Protocol")
    path: Optional[str] = Field(default=None, alias="Path")
    interval: Optional[int] = Field(default=None, alias="Interval")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    healthy_threshold: Optional[int] = Field(default=None, alias="HealthyThreshold")
    unhealthy_threshold: Optional[int] = Field(default=None, alias="UnhealthyThreshold")


class InstanceConfigurationModel(BaseModel):
    cpu: Optional[str] = Field(default=None, alias="Cpu")
    memory: Optional[str] = Field(default=None, alias="Memory")
    instance_role_arn: Optional[str] = Field(default=None, alias="InstanceRoleArn")


class ServiceObservabilityConfigurationModel(BaseModel):
    observability_enabled: bool = Field(alias="ObservabilityEnabled")
    observability_configuration_arn: Optional[str] = Field(
        default=None, alias="ObservabilityConfigurationArn"
    )


class VpcConnectorModel(BaseModel):
    vpc_connector_name: Optional[str] = Field(default=None, alias="VpcConnectorName")
    vpc_connector_arn: Optional[str] = Field(default=None, alias="VpcConnectorArn")
    vpc_connector_revision: Optional[int] = Field(
        default=None, alias="VpcConnectorRevision"
    )
    subnets: Optional[List[str]] = Field(default=None, alias="Subnets")
    security_groups: Optional[List[str]] = Field(default=None, alias="SecurityGroups")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="DeletedAt")


class IngressVpcConfigurationModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")


class DeleteAutoScalingConfigurationRequestModel(BaseModel):
    auto_scaling_configuration_arn: str = Field(alias="AutoScalingConfigurationArn")


class DeleteConnectionRequestModel(BaseModel):
    connection_arn: str = Field(alias="ConnectionArn")


class DeleteObservabilityConfigurationRequestModel(BaseModel):
    observability_configuration_arn: str = Field(alias="ObservabilityConfigurationArn")


class DeleteServiceRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")


class DeleteVpcConnectorRequestModel(BaseModel):
    vpc_connector_arn: str = Field(alias="VpcConnectorArn")


class DeleteVpcIngressConnectionRequestModel(BaseModel):
    vpc_ingress_connection_arn: str = Field(alias="VpcIngressConnectionArn")


class DescribeAutoScalingConfigurationRequestModel(BaseModel):
    auto_scaling_configuration_arn: str = Field(alias="AutoScalingConfigurationArn")


class DescribeCustomDomainsRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeObservabilityConfigurationRequestModel(BaseModel):
    observability_configuration_arn: str = Field(alias="ObservabilityConfigurationArn")


class DescribeServiceRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")


class DescribeVpcConnectorRequestModel(BaseModel):
    vpc_connector_arn: str = Field(alias="VpcConnectorArn")


class DescribeVpcIngressConnectionRequestModel(BaseModel):
    vpc_ingress_connection_arn: str = Field(alias="VpcIngressConnectionArn")


class DisassociateCustomDomainRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")
    domain_name: str = Field(alias="DomainName")


class EgressConfigurationModel(BaseModel):
    egress_type: Optional[Literal["DEFAULT", "VPC"]] = Field(
        default=None, alias="EgressType"
    )
    vpc_connector_arn: Optional[str] = Field(default=None, alias="VpcConnectorArn")


class ImageConfigurationModel(BaseModel):
    runtime_environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="RuntimeEnvironmentVariables"
    )
    start_command: Optional[str] = Field(default=None, alias="StartCommand")
    port: Optional[str] = Field(default=None, alias="Port")
    runtime_environment_secrets: Optional[Mapping[str, str]] = Field(
        default=None, alias="RuntimeEnvironmentSecrets"
    )


class IngressConfigurationModel(BaseModel):
    is_publicly_accessible: Optional[bool] = Field(
        default=None, alias="IsPubliclyAccessible"
    )


class ListAutoScalingConfigurationsRequestModel(BaseModel):
    auto_scaling_configuration_name: Optional[str] = Field(
        default=None, alias="AutoScalingConfigurationName"
    )
    latest_only: Optional[bool] = Field(default=None, alias="LatestOnly")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConnectionsRequestModel(BaseModel):
    connection_name: Optional[str] = Field(default=None, alias="ConnectionName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListObservabilityConfigurationsRequestModel(BaseModel):
    observability_configuration_name: Optional[str] = Field(
        default=None, alias="ObservabilityConfigurationName"
    )
    latest_only: Optional[bool] = Field(default=None, alias="LatestOnly")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ObservabilityConfigurationSummaryModel(BaseModel):
    observability_configuration_arn: Optional[str] = Field(
        default=None, alias="ObservabilityConfigurationArn"
    )
    observability_configuration_name: Optional[str] = Field(
        default=None, alias="ObservabilityConfigurationName"
    )
    observability_configuration_revision: Optional[int] = Field(
        default=None, alias="ObservabilityConfigurationRevision"
    )


class ListOperationsRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OperationSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[
        Literal[
            "CREATE_SERVICE",
            "DELETE_SERVICE",
            "PAUSE_SERVICE",
            "RESUME_SERVICE",
            "START_DEPLOYMENT",
            "UPDATE_SERVICE",
        ]
    ] = Field(default=None, alias="Type")
    status: Optional[
        Literal[
            "FAILED",
            "IN_PROGRESS",
            "PENDING",
            "ROLLBACK_FAILED",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_SUCCEEDED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="Status")
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")
    started_at: Optional[datetime] = Field(default=None, alias="StartedAt")
    ended_at: Optional[datetime] = Field(default=None, alias="EndedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class ListServicesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ServiceSummaryModel(BaseModel):
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    service_id: Optional[str] = Field(default=None, alias="ServiceId")
    service_arn: Optional[str] = Field(default=None, alias="ServiceArn")
    service_url: Optional[str] = Field(default=None, alias="ServiceUrl")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    status: Optional[
        Literal[
            "CREATE_FAILED",
            "DELETED",
            "DELETE_FAILED",
            "OPERATION_IN_PROGRESS",
            "PAUSED",
            "RUNNING",
        ]
    ] = Field(default=None, alias="Status")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListVpcConnectorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVpcIngressConnectionsFilterModel(BaseModel):
    service_arn: Optional[str] = Field(default=None, alias="ServiceArn")
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")


class VpcIngressConnectionSummaryModel(BaseModel):
    vpc_ingress_connection_arn: Optional[str] = Field(
        default=None, alias="VpcIngressConnectionArn"
    )
    service_arn: Optional[str] = Field(default=None, alias="ServiceArn")


class PauseServiceRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")


class ResumeServiceRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")


class StartDeploymentRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class StartDeploymentResponseModel(BaseModel):
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAutoScalingConfigurationsResponseModel(BaseModel):
    auto_scaling_configuration_summary_list: List[
        AutoScalingConfigurationSummaryModel
    ] = Field(alias="AutoScalingConfigurationSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAutoScalingConfigurationResponseModel(BaseModel):
    auto_scaling_configuration: AutoScalingConfigurationModel = Field(
        alias="AutoScalingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAutoScalingConfigurationResponseModel(BaseModel):
    auto_scaling_configuration: AutoScalingConfigurationModel = Field(
        alias="AutoScalingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAutoScalingConfigurationResponseModel(BaseModel):
    auto_scaling_configuration: AutoScalingConfigurationModel = Field(
        alias="AutoScalingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomDomainModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    enable_wwwsubdomain: bool = Field(alias="EnableWWWSubdomain")
    status: Literal[
        "ACTIVE",
        "BINDING_CERTIFICATE",
        "CREATE_FAILED",
        "CREATING",
        "DELETE_FAILED",
        "DELETING",
        "PENDING_CERTIFICATE_DNS_VALIDATION",
    ] = Field(alias="Status")
    certificate_validation_records: Optional[
        List[CertificateValidationRecordModel]
    ] = Field(default=None, alias="CertificateValidationRecords")


class CodeConfigurationModel(BaseModel):
    configuration_source: Literal["API", "REPOSITORY"] = Field(
        alias="ConfigurationSource"
    )
    code_configuration_values: Optional[CodeConfigurationValuesModel] = Field(
        default=None, alias="CodeConfigurationValues"
    )


class ListConnectionsResponseModel(BaseModel):
    connection_summary_list: List[ConnectionSummaryModel] = Field(
        alias="ConnectionSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteConnectionResponseModel(BaseModel):
    connection: ConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAutoScalingConfigurationRequestModel(BaseModel):
    auto_scaling_configuration_name: str = Field(alias="AutoScalingConfigurationName")
    max_concurrency: Optional[int] = Field(default=None, alias="MaxConcurrency")
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    max_size: Optional[int] = Field(default=None, alias="MaxSize")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateConnectionRequestModel(BaseModel):
    connection_name: str = Field(alias="ConnectionName")
    provider_type: Literal["GITHUB"] = Field(alias="ProviderType")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateVpcConnectorRequestModel(BaseModel):
    vpc_connector_name: str = Field(alias="VpcConnectorName")
    subnets: Sequence[str] = Field(alias="Subnets")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateObservabilityConfigurationRequestModel(BaseModel):
    observability_configuration_name: str = Field(
        alias="ObservabilityConfigurationName"
    )
    trace_configuration: Optional[TraceConfigurationModel] = Field(
        default=None, alias="TraceConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ObservabilityConfigurationModel(BaseModel):
    observability_configuration_arn: Optional[str] = Field(
        default=None, alias="ObservabilityConfigurationArn"
    )
    observability_configuration_name: Optional[str] = Field(
        default=None, alias="ObservabilityConfigurationName"
    )
    trace_configuration: Optional[TraceConfigurationModel] = Field(
        default=None, alias="TraceConfiguration"
    )
    observability_configuration_revision: Optional[int] = Field(
        default=None, alias="ObservabilityConfigurationRevision"
    )
    latest: Optional[bool] = Field(default=None, alias="Latest")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="DeletedAt")


class CreateVpcConnectorResponseModel(BaseModel):
    vpc_connector: VpcConnectorModel = Field(alias="VpcConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVpcConnectorResponseModel(BaseModel):
    vpc_connector: VpcConnectorModel = Field(alias="VpcConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVpcConnectorResponseModel(BaseModel):
    vpc_connector: VpcConnectorModel = Field(alias="VpcConnector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVpcConnectorsResponseModel(BaseModel):
    vpc_connectors: List[VpcConnectorModel] = Field(alias="VpcConnectors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVpcIngressConnectionRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")
    vpc_ingress_connection_name: str = Field(alias="VpcIngressConnectionName")
    ingress_vpc_configuration: IngressVpcConfigurationModel = Field(
        alias="IngressVpcConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateVpcIngressConnectionRequestModel(BaseModel):
    vpc_ingress_connection_arn: str = Field(alias="VpcIngressConnectionArn")
    ingress_vpc_configuration: IngressVpcConfigurationModel = Field(
        alias="IngressVpcConfiguration"
    )


class VpcIngressConnectionModel(BaseModel):
    vpc_ingress_connection_arn: Optional[str] = Field(
        default=None, alias="VpcIngressConnectionArn"
    )
    vpc_ingress_connection_name: Optional[str] = Field(
        default=None, alias="VpcIngressConnectionName"
    )
    service_arn: Optional[str] = Field(default=None, alias="ServiceArn")
    status: Optional[
        Literal[
            "AVAILABLE",
            "DELETED",
            "FAILED_CREATION",
            "FAILED_DELETION",
            "FAILED_UPDATE",
            "PENDING_CREATION",
            "PENDING_DELETION",
            "PENDING_UPDATE",
        ]
    ] = Field(default=None, alias="Status")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    ingress_vpc_configuration: Optional[IngressVpcConfigurationModel] = Field(
        default=None, alias="IngressVpcConfiguration"
    )
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="DeletedAt")


class ImageRepositoryModel(BaseModel):
    image_identifier: str = Field(alias="ImageIdentifier")
    image_repository_type: Literal["ECR", "ECR_PUBLIC"] = Field(
        alias="ImageRepositoryType"
    )
    image_configuration: Optional[ImageConfigurationModel] = Field(
        default=None, alias="ImageConfiguration"
    )


class NetworkConfigurationModel(BaseModel):
    egress_configuration: Optional[EgressConfigurationModel] = Field(
        default=None, alias="EgressConfiguration"
    )
    ingress_configuration: Optional[IngressConfigurationModel] = Field(
        default=None, alias="IngressConfiguration"
    )


class ListObservabilityConfigurationsResponseModel(BaseModel):
    observability_configuration_summary_list: List[
        ObservabilityConfigurationSummaryModel
    ] = Field(alias="ObservabilityConfigurationSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOperationsResponseModel(BaseModel):
    operation_summary_list: List[OperationSummaryModel] = Field(
        alias="OperationSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServicesResponseModel(BaseModel):
    service_summary_list: List[ServiceSummaryModel] = Field(alias="ServiceSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVpcIngressConnectionsRequestModel(BaseModel):
    filter: Optional[ListVpcIngressConnectionsFilterModel] = Field(
        default=None, alias="Filter"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVpcIngressConnectionsResponseModel(BaseModel):
    vpc_ingress_connection_summary_list: List[VpcIngressConnectionSummaryModel] = Field(
        alias="VpcIngressConnectionSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateCustomDomainResponseModel(BaseModel):
    dns_target: str = Field(alias="DNSTarget")
    service_arn: str = Field(alias="ServiceArn")
    custom_domain: CustomDomainModel = Field(alias="CustomDomain")
    vpc_dns_targets: List[VpcDNSTargetModel] = Field(alias="VpcDNSTargets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomDomainsResponseModel(BaseModel):
    dns_target: str = Field(alias="DNSTarget")
    service_arn: str = Field(alias="ServiceArn")
    custom_domains: List[CustomDomainModel] = Field(alias="CustomDomains")
    vpc_dns_targets: List[VpcDNSTargetModel] = Field(alias="VpcDNSTargets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateCustomDomainResponseModel(BaseModel):
    dns_target: str = Field(alias="DNSTarget")
    service_arn: str = Field(alias="ServiceArn")
    custom_domain: CustomDomainModel = Field(alias="CustomDomain")
    vpc_dns_targets: List[VpcDNSTargetModel] = Field(alias="VpcDNSTargets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CodeRepositoryModel(BaseModel):
    repository_url: str = Field(alias="RepositoryUrl")
    source_code_version: SourceCodeVersionModel = Field(alias="SourceCodeVersion")
    code_configuration: Optional[CodeConfigurationModel] = Field(
        default=None, alias="CodeConfiguration"
    )


class CreateObservabilityConfigurationResponseModel(BaseModel):
    observability_configuration: ObservabilityConfigurationModel = Field(
        alias="ObservabilityConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteObservabilityConfigurationResponseModel(BaseModel):
    observability_configuration: ObservabilityConfigurationModel = Field(
        alias="ObservabilityConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeObservabilityConfigurationResponseModel(BaseModel):
    observability_configuration: ObservabilityConfigurationModel = Field(
        alias="ObservabilityConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVpcIngressConnectionResponseModel(BaseModel):
    vpc_ingress_connection: VpcIngressConnectionModel = Field(
        alias="VpcIngressConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVpcIngressConnectionResponseModel(BaseModel):
    vpc_ingress_connection: VpcIngressConnectionModel = Field(
        alias="VpcIngressConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVpcIngressConnectionResponseModel(BaseModel):
    vpc_ingress_connection: VpcIngressConnectionModel = Field(
        alias="VpcIngressConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVpcIngressConnectionResponseModel(BaseModel):
    vpc_ingress_connection: VpcIngressConnectionModel = Field(
        alias="VpcIngressConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceConfigurationModel(BaseModel):
    code_repository: Optional[CodeRepositoryModel] = Field(
        default=None, alias="CodeRepository"
    )
    image_repository: Optional[ImageRepositoryModel] = Field(
        default=None, alias="ImageRepository"
    )
    auto_deployments_enabled: Optional[bool] = Field(
        default=None, alias="AutoDeploymentsEnabled"
    )
    authentication_configuration: Optional[AuthenticationConfigurationModel] = Field(
        default=None, alias="AuthenticationConfiguration"
    )


class CreateServiceRequestModel(BaseModel):
    service_name: str = Field(alias="ServiceName")
    source_configuration: SourceConfigurationModel = Field(alias="SourceConfiguration")
    instance_configuration: Optional[InstanceConfigurationModel] = Field(
        default=None, alias="InstanceConfiguration"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    health_check_configuration: Optional[HealthCheckConfigurationModel] = Field(
        default=None, alias="HealthCheckConfiguration"
    )
    auto_scaling_configuration_arn: Optional[str] = Field(
        default=None, alias="AutoScalingConfigurationArn"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="NetworkConfiguration"
    )
    observability_configuration: Optional[
        ServiceObservabilityConfigurationModel
    ] = Field(default=None, alias="ObservabilityConfiguration")


class ServiceModel(BaseModel):
    service_name: str = Field(alias="ServiceName")
    service_id: str = Field(alias="ServiceId")
    service_arn: str = Field(alias="ServiceArn")
    created_at: datetime = Field(alias="CreatedAt")
    updated_at: datetime = Field(alias="UpdatedAt")
    status: Literal[
        "CREATE_FAILED",
        "DELETED",
        "DELETE_FAILED",
        "OPERATION_IN_PROGRESS",
        "PAUSED",
        "RUNNING",
    ] = Field(alias="Status")
    source_configuration: SourceConfigurationModel = Field(alias="SourceConfiguration")
    instance_configuration: InstanceConfigurationModel = Field(
        alias="InstanceConfiguration"
    )
    auto_scaling_configuration_summary: AutoScalingConfigurationSummaryModel = Field(
        alias="AutoScalingConfigurationSummary"
    )
    network_configuration: NetworkConfigurationModel = Field(
        alias="NetworkConfiguration"
    )
    service_url: Optional[str] = Field(default=None, alias="ServiceUrl")
    deleted_at: Optional[datetime] = Field(default=None, alias="DeletedAt")
    encryption_configuration: Optional[EncryptionConfigurationModel] = Field(
        default=None, alias="EncryptionConfiguration"
    )
    health_check_configuration: Optional[HealthCheckConfigurationModel] = Field(
        default=None, alias="HealthCheckConfiguration"
    )
    observability_configuration: Optional[
        ServiceObservabilityConfigurationModel
    ] = Field(default=None, alias="ObservabilityConfiguration")


class UpdateServiceRequestModel(BaseModel):
    service_arn: str = Field(alias="ServiceArn")
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="SourceConfiguration"
    )
    instance_configuration: Optional[InstanceConfigurationModel] = Field(
        default=None, alias="InstanceConfiguration"
    )
    auto_scaling_configuration_arn: Optional[str] = Field(
        default=None, alias="AutoScalingConfigurationArn"
    )
    health_check_configuration: Optional[HealthCheckConfigurationModel] = Field(
        default=None, alias="HealthCheckConfiguration"
    )
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="NetworkConfiguration"
    )
    observability_configuration: Optional[
        ServiceObservabilityConfigurationModel
    ] = Field(default=None, alias="ObservabilityConfiguration")


class CreateServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PauseServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResumeServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServiceResponseModel(BaseModel):
    service: ServiceModel = Field(alias="Service")
    operation_id: str = Field(alias="OperationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
