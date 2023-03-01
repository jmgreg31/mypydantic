# Model Generated: Wed Mar  1 11:15:21 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    IO,
    Any,
    Dict,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Union,
    Type,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountLimit(BaseModel):
    total_code_size: Optional[int] = Field(default=None, alias="TotalCodeSize")
    code_size_unzipped: Optional[int] = Field(default=None, alias="CodeSizeUnzipped")
    code_size_zipped: Optional[int] = Field(default=None, alias="CodeSizeZipped")
    concurrent_executions: Optional[int] = Field(
        default=None, alias="ConcurrentExecutions"
    )
    unreserved_concurrent_executions: Optional[int] = Field(
        default=None, alias="UnreservedConcurrentExecutions"
    )


class AccountUsage(BaseModel):
    total_code_size: Optional[int] = Field(default=None, alias="TotalCodeSize")
    function_count: Optional[int] = Field(default=None, alias="FunctionCount")


class AddLayerVersionPermissionRequest(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")
    statement_id: str = Field(alias="StatementId")
    action: str = Field(alias="Action")
    principal: str = Field(alias="Principal")
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class ResponseMetadata(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AddPermissionRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    statement_id: str = Field(alias="StatementId")
    action: str = Field(alias="Action")
    principal: str = Field(alias="Principal")
    source_arn: Optional[str] = Field(default=None, alias="SourceArn")
    source_account: Optional[str] = Field(default=None, alias="SourceAccount")
    event_source_token: Optional[str] = Field(default=None, alias="EventSourceToken")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    principal_org_id: Optional[str] = Field(default=None, alias="PrincipalOrgID")
    function_url_auth_type: Optional[Literal["AWS_IAM", "NONE"]] = Field(
        default=None, alias="FunctionUrlAuthType"
    )


class AliasRoutingConfiguration(BaseModel):
    additional_version_weights: Optional[Mapping[str, float]] = Field(
        default=None, alias="AdditionalVersionWeights"
    )


class AllowedPublishers(BaseModel):
    signing_profile_version_arns: Sequence[str] = Field(
        alias="SigningProfileVersionArns"
    )


class AmazonManagedKafkaEventSourceConfig(BaseModel):
    consumer_group_id: Optional[str] = Field(default=None, alias="ConsumerGroupId")


class CodeSigningPolicies(BaseModel):
    untrusted_artifact_on_deployment: Optional[Literal["Enforce", "Warn"]] = Field(
        default=None, alias="UntrustedArtifactOnDeployment"
    )


class Concurrency(BaseModel):
    reserved_concurrent_executions: Optional[int] = Field(
        default=None, alias="ReservedConcurrentExecutions"
    )


class Cors(BaseModel):
    allow_credentials: Optional[bool] = Field(default=None, alias="AllowCredentials")
    allow_headers: Optional[Sequence[str]] = Field(default=None, alias="AllowHeaders")
    allow_methods: Optional[Sequence[str]] = Field(default=None, alias="AllowMethods")
    allow_origins: Optional[Sequence[str]] = Field(default=None, alias="AllowOrigins")
    expose_headers: Optional[Sequence[str]] = Field(default=None, alias="ExposeHeaders")
    max_age: Optional[int] = Field(default=None, alias="MaxAge")


class DocumentDBEventSourceConfig(BaseModel):
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    collection_name: Optional[str] = Field(default=None, alias="CollectionName")
    full_document: Optional[Literal["Default", "UpdateLookup"]] = Field(
        default=None, alias="FullDocument"
    )


class ScalingConfig(BaseModel):
    maximum_concurrency: Optional[int] = Field(default=None, alias="MaximumConcurrency")


class SelfManagedEventSource(BaseModel):
    endpoints: Optional[
        Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]
    ] = Field(default=None, alias="Endpoints")


class SelfManagedKafkaEventSourceConfig(BaseModel):
    consumer_group_id: Optional[str] = Field(default=None, alias="ConsumerGroupId")


class SourceAccessConfiguration(BaseModel):
    type: Optional[
        Literal[
            "BASIC_AUTH",
            "CLIENT_CERTIFICATE_TLS_AUTH",
            "SASL_SCRAM_256_AUTH",
            "SASL_SCRAM_512_AUTH",
            "SERVER_ROOT_CA_CERTIFICATE",
            "VIRTUAL_HOST",
            "VPC_SECURITY_GROUP",
            "VPC_SUBNET",
        ]
    ] = Field(default=None, alias="Type")
    uri: Optional[str] = Field(default=None, alias="URI")


class DeadLetterConfig(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")


class Environment(BaseModel):
    variables: Optional[Mapping[str, str]] = Field(default=None, alias="Variables")


class EphemeralStorage(BaseModel):
    size: int = Field(alias="Size")


class FileSystemConfig(BaseModel):
    arn: str = Field(alias="Arn")
    local_mount_path: str = Field(alias="LocalMountPath")


class FunctionCode(BaseModel):
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")
    s3_object_version: Optional[str] = Field(default=None, alias="S3ObjectVersion")
    image_uri: Optional[str] = Field(default=None, alias="ImageUri")


class ImageConfig(BaseModel):
    entry_point: Optional[Sequence[str]] = Field(default=None, alias="EntryPoint")
    command: Optional[Sequence[str]] = Field(default=None, alias="Command")
    working_directory: Optional[str] = Field(default=None, alias="WorkingDirectory")


class SnapStart(BaseModel):
    apply_on: Optional[Literal["None", "PublishedVersions"]] = Field(
        default=None, alias="ApplyOn"
    )


class TracingConfig(BaseModel):
    mode: Optional[Literal["Active", "PassThrough"]] = Field(default=None, alias="Mode")


class VpcConfig(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class DeleteAliasRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")


class DeleteCodeSigningConfigRequest(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")


class DeleteEventSourceMappingRequest(BaseModel):
    uuid: str = Field(alias="UUID")


class DeleteFunctionCodeSigningConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")


class DeleteFunctionConcurrencyRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")


class DeleteFunctionEventInvokeConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class DeleteFunctionRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class DeleteFunctionUrlConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class DeleteLayerVersionRequest(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")


class DeleteProvisionedConcurrencyConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: str = Field(alias="Qualifier")


class OnFailure(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")


class OnSuccess(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")


class EnvironmentError(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class Filter(BaseModel):
    pattern: Optional[str] = Field(default=None, alias="Pattern")


class FunctionCodeLocation(BaseModel):
    repository_type: Optional[str] = Field(default=None, alias="RepositoryType")
    location: Optional[str] = Field(default=None, alias="Location")
    image_uri: Optional[str] = Field(default=None, alias="ImageUri")
    resolved_image_uri: Optional[str] = Field(default=None, alias="ResolvedImageUri")


class Layer(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")
    signing_profile_version_arn: Optional[str] = Field(
        default=None, alias="SigningProfileVersionArn"
    )
    signing_job_arn: Optional[str] = Field(default=None, alias="SigningJobArn")


class SnapStartResponse(BaseModel):
    apply_on: Optional[Literal["None", "PublishedVersions"]] = Field(
        default=None, alias="ApplyOn"
    )
    optimization_status: Optional[Literal["Off", "On"]] = Field(
        default=None, alias="OptimizationStatus"
    )


class TracingConfigResponse(BaseModel):
    mode: Optional[Literal["Active", "PassThrough"]] = Field(default=None, alias="Mode")


class VpcConfigResponse(BaseModel):
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class GetAliasRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")


class GetCodeSigningConfigRequest(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")


class GetEventSourceMappingRequest(BaseModel):
    uuid: str = Field(alias="UUID")


class GetFunctionCodeSigningConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")


class GetFunctionConcurrencyRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")


class WaiterConfig(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetFunctionConfigurationRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetFunctionEventInvokeConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetFunctionRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetFunctionUrlConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetLayerVersionByArnRequest(BaseModel):
    arn: str = Field(alias="Arn")


class GetLayerVersionPolicyRequest(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")


class GetLayerVersionRequest(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")


class LayerVersionContentOutput(BaseModel):
    location: Optional[str] = Field(default=None, alias="Location")
    code_sha256: Optional[str] = Field(default=None, alias="CodeSha256")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")
    signing_profile_version_arn: Optional[str] = Field(
        default=None, alias="SigningProfileVersionArn"
    )
    signing_job_arn: Optional[str] = Field(default=None, alias="SigningJobArn")


class GetPolicyRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetProvisionedConcurrencyConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: str = Field(alias="Qualifier")


class GetRuntimeManagementConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class ImageConfigError(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class InvocationRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    invocation_type: Optional[Literal["DryRun", "Event", "RequestResponse"]] = Field(
        default=None, alias="InvocationType"
    )
    log_type: Optional[Literal["None", "Tail"]] = Field(default=None, alias="LogType")
    client_context: Optional[str] = Field(default=None, alias="ClientContext")
    payload: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Payload"
    )
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class InvokeAsyncRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    invoke_args: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="InvokeArgs"
    )


class LayerVersionContentInput(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")
    s3_object_version: Optional[str] = Field(default=None, alias="S3ObjectVersion")
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )


class LayerVersionsListItem(BaseModel):
    layer_version_arn: Optional[str] = Field(default=None, alias="LayerVersionArn")
    version: Optional[int] = Field(default=None, alias="Version")
    description: Optional[str] = Field(default=None, alias="Description")
    created_date: Optional[str] = Field(default=None, alias="CreatedDate")
    compatible_runtimes: Optional[
        List[
            Literal[
                "dotnet6",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "dotnetcore3.1",
                "go1.x",
                "java11",
                "java8",
                "java8.al2",
                "nodejs",
                "nodejs10.x",
                "nodejs12.x",
                "nodejs14.x",
                "nodejs16.x",
                "nodejs18.x",
                "nodejs4.3",
                "nodejs4.3-edge",
                "nodejs6.10",
                "nodejs8.10",
                "provided",
                "provided.al2",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "python3.9",
                "ruby2.5",
                "ruby2.7",
            ]
        ]
    ] = Field(default=None, alias="CompatibleRuntimes")
    license_info: Optional[str] = Field(default=None, alias="LicenseInfo")
    compatible_architectures: Optional[List[Literal["arm64", "x86_64"]]] = Field(
        default=None, alias="CompatibleArchitectures"
    )


class PaginatorConfig(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAliasesRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListCodeSigningConfigsRequest(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListEventSourceMappingsRequest(BaseModel):
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionEventInvokeConfigsRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionUrlConfigsRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionsByCodeSigningConfigRequest(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionsRequest(BaseModel):
    master_region: Optional[str] = Field(default=None, alias="MasterRegion")
    function_version: Optional[Literal["ALL"]] = Field(
        default=None, alias="FunctionVersion"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListLayerVersionsRequest(BaseModel):
    layer_name: str = Field(alias="LayerName")
    compatible_runtime: Optional[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(default=None, alias="CompatibleRuntime")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    compatible_architecture: Optional[Literal["arm64", "x86_64"]] = Field(
        default=None, alias="CompatibleArchitecture"
    )


class ListLayersRequest(BaseModel):
    compatible_runtime: Optional[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(default=None, alias="CompatibleRuntime")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    compatible_architecture: Optional[Literal["arm64", "x86_64"]] = Field(
        default=None, alias="CompatibleArchitecture"
    )


class ListProvisionedConcurrencyConfigsRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ProvisionedConcurrencyConfigListItem(BaseModel):
    function_arn: Optional[str] = Field(default=None, alias="FunctionArn")
    requested_provisioned_concurrent_executions: Optional[int] = Field(
        default=None, alias="RequestedProvisionedConcurrentExecutions"
    )
    available_provisioned_concurrent_executions: Optional[int] = Field(
        default=None, alias="AvailableProvisionedConcurrentExecutions"
    )
    allocated_provisioned_concurrent_executions: Optional[int] = Field(
        default=None, alias="AllocatedProvisionedConcurrentExecutions"
    )
    status: Optional[Literal["FAILED", "IN_PROGRESS", "READY"]] = Field(
        default=None, alias="Status"
    )
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    last_modified: Optional[str] = Field(default=None, alias="LastModified")


class ListTagsRequest(BaseModel):
    resource: str = Field(alias="Resource")


class ListVersionsByFunctionRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class PublishVersionRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    code_sha256: Optional[str] = Field(default=None, alias="CodeSha256")
    description: Optional[str] = Field(default=None, alias="Description")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class PutFunctionCodeSigningConfigRequest(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    function_name: str = Field(alias="FunctionName")


class PutFunctionConcurrencyRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    reserved_concurrent_executions: int = Field(alias="ReservedConcurrentExecutions")


class PutProvisionedConcurrencyConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: str = Field(alias="Qualifier")
    provisioned_concurrent_executions: int = Field(
        alias="ProvisionedConcurrentExecutions"
    )


class PutRuntimeManagementConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    update_runtime_on: Literal["Auto", "FunctionUpdate", "Manual"] = Field(
        alias="UpdateRuntimeOn"
    )
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    runtime_version_arn: Optional[str] = Field(default=None, alias="RuntimeVersionArn")


class RemoveLayerVersionPermissionRequest(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")
    statement_id: str = Field(alias="StatementId")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class RemovePermissionRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    statement_id: str = Field(alias="StatementId")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class RuntimeVersionError(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class TagResourceRequest(BaseModel):
    resource: str = Field(alias="Resource")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequest(BaseModel):
    resource: str = Field(alias="Resource")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateFunctionCodeRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")
    s3_object_version: Optional[str] = Field(default=None, alias="S3ObjectVersion")
    image_uri: Optional[str] = Field(default=None, alias="ImageUri")
    publish: Optional[bool] = Field(default=None, alias="Publish")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    architectures: Optional[Sequence[Literal["arm64", "x86_64"]]] = Field(
        default=None, alias="Architectures"
    )


class AddLayerVersionPermissionResponse(BaseModel):
    statement: str = Field(alias="Statement")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class AddPermissionResponse(BaseModel):
    statement: str = Field(alias="Statement")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ConcurrencyResponseMetadata(BaseModel):
    reserved_concurrent_executions: int = Field(alias="ReservedConcurrentExecutions")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class EmptyResponseMetadata(BaseModel):
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetAccountSettingsResponse(BaseModel):
    account_limit: AccountLimit = Field(alias="AccountLimit")
    account_usage: AccountUsage = Field(alias="AccountUsage")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetFunctionCodeSigningConfigResponse(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    function_name: str = Field(alias="FunctionName")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetFunctionConcurrencyResponse(BaseModel):
    reserved_concurrent_executions: int = Field(alias="ReservedConcurrentExecutions")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetLayerVersionPolicyResponse(BaseModel):
    policy: str = Field(alias="Policy")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetPolicyResponse(BaseModel):
    policy: str = Field(alias="Policy")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetProvisionedConcurrencyConfigResponse(BaseModel):
    requested_provisioned_concurrent_executions: int = Field(
        alias="RequestedProvisionedConcurrentExecutions"
    )
    available_provisioned_concurrent_executions: int = Field(
        alias="AvailableProvisionedConcurrentExecutions"
    )
    allocated_provisioned_concurrent_executions: int = Field(
        alias="AllocatedProvisionedConcurrentExecutions"
    )
    status: Literal["FAILED", "IN_PROGRESS", "READY"] = Field(alias="Status")
    status_reason: str = Field(alias="StatusReason")
    last_modified: str = Field(alias="LastModified")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetRuntimeManagementConfigResponse(BaseModel):
    update_runtime_on: Literal["Auto", "FunctionUpdate", "Manual"] = Field(
        alias="UpdateRuntimeOn"
    )
    runtime_version_arn: str = Field(alias="RuntimeVersionArn")
    function_arn: str = Field(alias="FunctionArn")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class InvocationResponse(BaseModel):
    status_code: int = Field(alias="StatusCode")
    function_error: str = Field(alias="FunctionError")
    log_result: str = Field(alias="LogResult")
    payload: Type[StreamingBody] = Field(alias="Payload")
    executed_version: str = Field(alias="ExecutedVersion")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class InvokeAsyncResponse(BaseModel):
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListFunctionsByCodeSigningConfigResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    function_arns: List[str] = Field(alias="FunctionArns")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListTagsResponse(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class PutFunctionCodeSigningConfigResponse(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    function_name: str = Field(alias="FunctionName")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class PutProvisionedConcurrencyConfigResponse(BaseModel):
    requested_provisioned_concurrent_executions: int = Field(
        alias="RequestedProvisionedConcurrentExecutions"
    )
    available_provisioned_concurrent_executions: int = Field(
        alias="AvailableProvisionedConcurrentExecutions"
    )
    allocated_provisioned_concurrent_executions: int = Field(
        alias="AllocatedProvisionedConcurrentExecutions"
    )
    status: Literal["FAILED", "IN_PROGRESS", "READY"] = Field(alias="Status")
    status_reason: str = Field(alias="StatusReason")
    last_modified: str = Field(alias="LastModified")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class PutRuntimeManagementConfigResponse(BaseModel):
    update_runtime_on: Literal["Auto", "FunctionUpdate", "Manual"] = Field(
        alias="UpdateRuntimeOn"
    )
    function_arn: str = Field(alias="FunctionArn")
    runtime_version_arn: str = Field(alias="RuntimeVersionArn")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class AliasConfigurationResponseMetadata(BaseModel):
    alias_arn: str = Field(alias="AliasArn")
    name: str = Field(alias="Name")
    function_version: str = Field(alias="FunctionVersion")
    description: str = Field(alias="Description")
    routing_config: AliasRoutingConfiguration = Field(alias="RoutingConfig")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class AliasConfiguration(BaseModel):
    alias_arn: Optional[str] = Field(default=None, alias="AliasArn")
    name: Optional[str] = Field(default=None, alias="Name")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_config: Optional[AliasRoutingConfiguration] = Field(
        default=None, alias="RoutingConfig"
    )
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class CreateAliasRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")
    function_version: str = Field(alias="FunctionVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_config: Optional[AliasRoutingConfiguration] = Field(
        default=None, alias="RoutingConfig"
    )


class UpdateAliasRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_config: Optional[AliasRoutingConfiguration] = Field(
        default=None, alias="RoutingConfig"
    )
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class CodeSigningConfig(BaseModel):
    code_signing_config_id: str = Field(alias="CodeSigningConfigId")
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    allowed_publishers: AllowedPublishers = Field(alias="AllowedPublishers")
    code_signing_policies: CodeSigningPolicies = Field(alias="CodeSigningPolicies")
    last_modified: str = Field(alias="LastModified")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateCodeSigningConfigRequest(BaseModel):
    allowed_publishers: AllowedPublishers = Field(alias="AllowedPublishers")
    description: Optional[str] = Field(default=None, alias="Description")
    code_signing_policies: Optional[CodeSigningPolicies] = Field(
        default=None, alias="CodeSigningPolicies"
    )


class UpdateCodeSigningConfigRequest(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    description: Optional[str] = Field(default=None, alias="Description")
    allowed_publishers: Optional[AllowedPublishers] = Field(
        default=None, alias="AllowedPublishers"
    )
    code_signing_policies: Optional[CodeSigningPolicies] = Field(
        default=None, alias="CodeSigningPolicies"
    )


class CreateFunctionUrlConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    cors: Optional[Cors] = Field(default=None, alias="Cors")


class CreateFunctionUrlConfigResponse(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: Cors = Field(alias="Cors")
    creation_time: str = Field(alias="CreationTime")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class FunctionUrlConfig(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    creation_time: str = Field(alias="CreationTime")
    last_modified_time: str = Field(alias="LastModifiedTime")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: Optional[Cors] = Field(default=None, alias="Cors")


class GetFunctionUrlConfigResponse(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: Cors = Field(alias="Cors")
    creation_time: str = Field(alias="CreationTime")
    last_modified_time: str = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateFunctionUrlConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    auth_type: Optional[Literal["AWS_IAM", "NONE"]] = Field(
        default=None, alias="AuthType"
    )
    cors: Optional[Cors] = Field(default=None, alias="Cors")


class UpdateFunctionUrlConfigResponse(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: Cors = Field(alias="Cors")
    creation_time: str = Field(alias="CreationTime")
    last_modified_time: str = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateFunctionRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    role: str = Field(alias="Role")
    code: FunctionCode = Field(alias="Code")
    runtime: Optional[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(default=None, alias="Runtime")
    handler: Optional[str] = Field(default=None, alias="Handler")
    description: Optional[str] = Field(default=None, alias="Description")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    memory_size: Optional[int] = Field(default=None, alias="MemorySize")
    publish: Optional[bool] = Field(default=None, alias="Publish")
    vpc_config: Optional[VpcConfig] = Field(default=None, alias="VpcConfig")
    package_type: Optional[Literal["Image", "Zip"]] = Field(
        default=None, alias="PackageType"
    )
    dead_letter_config: Optional[DeadLetterConfig] = Field(
        default=None, alias="DeadLetterConfig"
    )
    environment: Optional[Environment] = Field(default=None, alias="Environment")
    kms_key_arn: Optional[str] = Field(default=None, alias="KMSKeyArn")
    tracing_config: Optional[TracingConfig] = Field(default=None, alias="TracingConfig")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    layers: Optional[Sequence[str]] = Field(default=None, alias="Layers")
    file_system_configs: Optional[Sequence[FileSystemConfig]] = Field(
        default=None, alias="FileSystemConfigs"
    )
    image_config: Optional[ImageConfig] = Field(default=None, alias="ImageConfig")
    code_signing_config_arn: Optional[str] = Field(
        default=None, alias="CodeSigningConfigArn"
    )
    architectures: Optional[Sequence[Literal["arm64", "x86_64"]]] = Field(
        default=None, alias="Architectures"
    )
    ephemeral_storage: Optional[EphemeralStorage] = Field(
        default=None, alias="EphemeralStorage"
    )
    snap_start: Optional[SnapStart] = Field(default=None, alias="SnapStart")


class UpdateFunctionConfigurationRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    role: Optional[str] = Field(default=None, alias="Role")
    handler: Optional[str] = Field(default=None, alias="Handler")
    description: Optional[str] = Field(default=None, alias="Description")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    memory_size: Optional[int] = Field(default=None, alias="MemorySize")
    vpc_config: Optional[VpcConfig] = Field(default=None, alias="VpcConfig")
    environment: Optional[Environment] = Field(default=None, alias="Environment")
    runtime: Optional[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(default=None, alias="Runtime")
    dead_letter_config: Optional[DeadLetterConfig] = Field(
        default=None, alias="DeadLetterConfig"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KMSKeyArn")
    tracing_config: Optional[TracingConfig] = Field(default=None, alias="TracingConfig")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    layers: Optional[Sequence[str]] = Field(default=None, alias="Layers")
    file_system_configs: Optional[Sequence[FileSystemConfig]] = Field(
        default=None, alias="FileSystemConfigs"
    )
    image_config: Optional[ImageConfig] = Field(default=None, alias="ImageConfig")
    ephemeral_storage: Optional[EphemeralStorage] = Field(
        default=None, alias="EphemeralStorage"
    )
    snap_start: Optional[SnapStart] = Field(default=None, alias="SnapStart")


class DestinationConfig(BaseModel):
    on_success: Optional[OnSuccess] = Field(default=None, alias="OnSuccess")
    on_failure: Optional[OnFailure] = Field(default=None, alias="OnFailure")


class EnvironmentResponse(BaseModel):
    variables: Optional[Dict[str, str]] = Field(default=None, alias="Variables")
    error: Optional[EnvironmentError] = Field(default=None, alias="Error")


class FilterCriteria(BaseModel):
    filters: Optional[Sequence[Filter]] = Field(default=None, alias="Filters")


class GetFunctionConfigurationRequestFunctionActiveWait(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class GetFunctionConfigurationRequestFunctionUpdatedWait(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class GetFunctionConfigurationRequestPublishedVersionActiveWait(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class GetFunctionRequestFunctionActiveV2Wait(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class GetFunctionRequestFunctionExistsWait(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class GetFunctionRequestFunctionUpdatedV2Wait(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfig] = Field(default=None, alias="WaiterConfig")


class GetLayerVersionResponse(BaseModel):
    content: LayerVersionContentOutput = Field(alias="Content")
    layer_arn: str = Field(alias="LayerArn")
    layer_version_arn: str = Field(alias="LayerVersionArn")
    description: str = Field(alias="Description")
    created_date: str = Field(alias="CreatedDate")
    version: int = Field(alias="Version")
    compatible_runtimes: List[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(alias="CompatibleRuntimes")
    license_info: str = Field(alias="LicenseInfo")
    compatible_architectures: List[Literal["arm64", "x86_64"]] = Field(
        alias="CompatibleArchitectures"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class PublishLayerVersionResponse(BaseModel):
    content: LayerVersionContentOutput = Field(alias="Content")
    layer_arn: str = Field(alias="LayerArn")
    layer_version_arn: str = Field(alias="LayerVersionArn")
    description: str = Field(alias="Description")
    created_date: str = Field(alias="CreatedDate")
    version: int = Field(alias="Version")
    compatible_runtimes: List[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(alias="CompatibleRuntimes")
    license_info: str = Field(alias="LicenseInfo")
    compatible_architectures: List[Literal["arm64", "x86_64"]] = Field(
        alias="CompatibleArchitectures"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ImageConfigResponse(BaseModel):
    image_config: Optional[ImageConfig] = Field(default=None, alias="ImageConfig")
    error: Optional[ImageConfigError] = Field(default=None, alias="Error")


class PublishLayerVersionRequest(BaseModel):
    layer_name: str = Field(alias="LayerName")
    content: LayerVersionContentInput = Field(alias="Content")
    description: Optional[str] = Field(default=None, alias="Description")
    compatible_runtimes: Optional[
        Sequence[
            Literal[
                "dotnet6",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "dotnetcore3.1",
                "go1.x",
                "java11",
                "java8",
                "java8.al2",
                "nodejs",
                "nodejs10.x",
                "nodejs12.x",
                "nodejs14.x",
                "nodejs16.x",
                "nodejs18.x",
                "nodejs4.3",
                "nodejs4.3-edge",
                "nodejs6.10",
                "nodejs8.10",
                "provided",
                "provided.al2",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "python3.9",
                "ruby2.5",
                "ruby2.7",
            ]
        ]
    ] = Field(default=None, alias="CompatibleRuntimes")
    license_info: Optional[str] = Field(default=None, alias="LicenseInfo")
    compatible_architectures: Optional[Sequence[Literal["arm64", "x86_64"]]] = Field(
        default=None, alias="CompatibleArchitectures"
    )


class LayersListItem(BaseModel):
    layer_name: Optional[str] = Field(default=None, alias="LayerName")
    layer_arn: Optional[str] = Field(default=None, alias="LayerArn")
    latest_matching_version: Optional[LayerVersionsListItem] = Field(
        default=None, alias="LatestMatchingVersion"
    )


class ListLayerVersionsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    layer_versions: List[LayerVersionsListItem] = Field(alias="LayerVersions")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListAliasesRequestListAliasesPaginate(BaseModel):
    function_name: str = Field(alias="FunctionName")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCodeSigningConfigsRequestListCodeSigningConfigsPaginate(BaseModel):
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEventSourceMappingsRequestListEventSourceMappingsPaginate(BaseModel):
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionEventInvokeConfigsRequestListFunctionEventInvokeConfigsPaginate(
    BaseModel
):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionUrlConfigsRequestListFunctionUrlConfigsPaginate(BaseModel):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionsByCodeSigningConfigRequestListFunctionsByCodeSigningConfigPaginate(
    BaseModel
):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionsRequestListFunctionsPaginate(BaseModel):
    master_region: Optional[str] = Field(default=None, alias="MasterRegion")
    function_version: Optional[Literal["ALL"]] = Field(
        default=None, alias="FunctionVersion"
    )
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLayerVersionsRequestListLayerVersionsPaginate(BaseModel):
    layer_name: str = Field(alias="LayerName")
    compatible_runtime: Optional[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(default=None, alias="CompatibleRuntime")
    compatible_architecture: Optional[Literal["arm64", "x86_64"]] = Field(
        default=None, alias="CompatibleArchitecture"
    )
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLayersRequestListLayersPaginate(BaseModel):
    compatible_runtime: Optional[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(default=None, alias="CompatibleRuntime")
    compatible_architecture: Optional[Literal["arm64", "x86_64"]] = Field(
        default=None, alias="CompatibleArchitecture"
    )
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisionedConcurrencyConfigsRequestListProvisionedConcurrencyConfigsPaginate(
    BaseModel
):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVersionsByFunctionRequestListVersionsByFunctionPaginate(BaseModel):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfig] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisionedConcurrencyConfigsResponse(BaseModel):
    provisioned_concurrency_configs: List[ProvisionedConcurrencyConfigListItem] = Field(
        alias="ProvisionedConcurrencyConfigs"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class RuntimeVersionConfig(BaseModel):
    runtime_version_arn: Optional[str] = Field(default=None, alias="RuntimeVersionArn")
    error: Optional[RuntimeVersionError] = Field(default=None, alias="Error")


class ListAliasesResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    aliases: List[AliasConfiguration] = Field(alias="Aliases")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class CreateCodeSigningConfigResponse(BaseModel):
    code_signing_config: CodeSigningConfig = Field(alias="CodeSigningConfig")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetCodeSigningConfigResponse(BaseModel):
    code_signing_config: CodeSigningConfig = Field(alias="CodeSigningConfig")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListCodeSigningConfigsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    code_signing_configs: List[CodeSigningConfig] = Field(alias="CodeSigningConfigs")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class UpdateCodeSigningConfigResponse(BaseModel):
    code_signing_config: CodeSigningConfig = Field(alias="CodeSigningConfig")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListFunctionUrlConfigsResponse(BaseModel):
    function_url_configs: List[FunctionUrlConfig] = Field(alias="FunctionUrlConfigs")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class FunctionEventInvokeConfigResponseMetadata(BaseModel):
    last_modified: datetime = Field(alias="LastModified")
    function_arn: str = Field(alias="FunctionArn")
    maximum_retry_attempts: int = Field(alias="MaximumRetryAttempts")
    maximum_event_age_in_seconds: int = Field(alias="MaximumEventAgeInSeconds")
    destination_config: DestinationConfig = Field(alias="DestinationConfig")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class FunctionEventInvokeConfig(BaseModel):
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    function_arn: Optional[str] = Field(default=None, alias="FunctionArn")
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )
    destination_config: Optional[DestinationConfig] = Field(
        default=None, alias="DestinationConfig"
    )


class PutFunctionEventInvokeConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )
    destination_config: Optional[DestinationConfig] = Field(
        default=None, alias="DestinationConfig"
    )


class UpdateFunctionEventInvokeConfigRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )
    destination_config: Optional[DestinationConfig] = Field(
        default=None, alias="DestinationConfig"
    )


class CreateEventSourceMappingRequest(BaseModel):
    function_name: str = Field(alias="FunctionName")
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    filter_criteria: Optional[FilterCriteria] = Field(
        default=None, alias="FilterCriteria"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    parallelization_factor: Optional[int] = Field(
        default=None, alias="ParallelizationFactor"
    )
    starting_position: Optional[
        Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"]
    ] = Field(default=None, alias="StartingPosition")
    starting_position_timestamp: Optional[Union[datetime, str]] = Field(
        default=None, alias="StartingPositionTimestamp"
    )
    destination_config: Optional[DestinationConfig] = Field(
        default=None, alias="DestinationConfig"
    )
    maximum_record_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumRecordAgeInSeconds"
    )
    bisect_batch_on_function_error: Optional[bool] = Field(
        default=None, alias="BisectBatchOnFunctionError"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    tumbling_window_in_seconds: Optional[int] = Field(
        default=None, alias="TumblingWindowInSeconds"
    )
    topics: Optional[Sequence[str]] = Field(default=None, alias="Topics")
    queues: Optional[Sequence[str]] = Field(default=None, alias="Queues")
    source_access_configurations: Optional[Sequence[SourceAccessConfiguration]] = Field(
        default=None, alias="SourceAccessConfigurations"
    )
    self_managed_event_source: Optional[SelfManagedEventSource] = Field(
        default=None, alias="SelfManagedEventSource"
    )
    function_response_types: Optional[
        Sequence[Literal["ReportBatchItemFailures"]]
    ] = Field(default=None, alias="FunctionResponseTypes")
    amazon_managed_kafka_event_source_config: Optional[
        AmazonManagedKafkaEventSourceConfig
    ] = Field(default=None, alias="AmazonManagedKafkaEventSourceConfig")
    self_managed_kafka_event_source_config: Optional[
        SelfManagedKafkaEventSourceConfig
    ] = Field(default=None, alias="SelfManagedKafkaEventSourceConfig")
    scaling_config: Optional[ScalingConfig] = Field(default=None, alias="ScalingConfig")
    document_dbevent_source_config: Optional[DocumentDBEventSourceConfig] = Field(
        default=None, alias="DocumentDBEventSourceConfig"
    )


class EventSourceMappingConfigurationResponseMetadata(BaseModel):
    uuid: str = Field(alias="UUID")
    starting_position: Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"] = Field(
        alias="StartingPosition"
    )
    starting_position_timestamp: datetime = Field(alias="StartingPositionTimestamp")
    batch_size: int = Field(alias="BatchSize")
    maximum_batching_window_in_seconds: int = Field(
        alias="MaximumBatchingWindowInSeconds"
    )
    parallelization_factor: int = Field(alias="ParallelizationFactor")
    event_source_arn: str = Field(alias="EventSourceArn")
    filter_criteria: FilterCriteria = Field(alias="FilterCriteria")
    function_arn: str = Field(alias="FunctionArn")
    last_modified: datetime = Field(alias="LastModified")
    last_processing_result: str = Field(alias="LastProcessingResult")
    state: str = Field(alias="State")
    state_transition_reason: str = Field(alias="StateTransitionReason")
    destination_config: DestinationConfig = Field(alias="DestinationConfig")
    topics: List[str] = Field(alias="Topics")
    queues: List[str] = Field(alias="Queues")
    source_access_configurations: List[SourceAccessConfiguration] = Field(
        alias="SourceAccessConfigurations"
    )
    self_managed_event_source: SelfManagedEventSource = Field(
        alias="SelfManagedEventSource"
    )
    maximum_record_age_in_seconds: int = Field(alias="MaximumRecordAgeInSeconds")
    bisect_batch_on_function_error: bool = Field(alias="BisectBatchOnFunctionError")
    maximum_retry_attempts: int = Field(alias="MaximumRetryAttempts")
    tumbling_window_in_seconds: int = Field(alias="TumblingWindowInSeconds")
    function_response_types: List[Literal["ReportBatchItemFailures"]] = Field(
        alias="FunctionResponseTypes"
    )
    amazon_managed_kafka_event_source_config: AmazonManagedKafkaEventSourceConfig = (
        Field(alias="AmazonManagedKafkaEventSourceConfig")
    )
    self_managed_kafka_event_source_config: SelfManagedKafkaEventSourceConfig = Field(
        alias="SelfManagedKafkaEventSourceConfig"
    )
    scaling_config: ScalingConfig = Field(alias="ScalingConfig")
    document_dbevent_source_config: DocumentDBEventSourceConfig = Field(
        alias="DocumentDBEventSourceConfig"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class EventSourceMappingConfiguration(BaseModel):
    uuid: Optional[str] = Field(default=None, alias="UUID")
    starting_position: Optional[
        Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"]
    ] = Field(default=None, alias="StartingPosition")
    starting_position_timestamp: Optional[datetime] = Field(
        default=None, alias="StartingPositionTimestamp"
    )
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    parallelization_factor: Optional[int] = Field(
        default=None, alias="ParallelizationFactor"
    )
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    filter_criteria: Optional[FilterCriteria] = Field(
        default=None, alias="FilterCriteria"
    )
    function_arn: Optional[str] = Field(default=None, alias="FunctionArn")
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    last_processing_result: Optional[str] = Field(
        default=None, alias="LastProcessingResult"
    )
    state: Optional[str] = Field(default=None, alias="State")
    state_transition_reason: Optional[str] = Field(
        default=None, alias="StateTransitionReason"
    )
    destination_config: Optional[DestinationConfig] = Field(
        default=None, alias="DestinationConfig"
    )
    topics: Optional[List[str]] = Field(default=None, alias="Topics")
    queues: Optional[List[str]] = Field(default=None, alias="Queues")
    source_access_configurations: Optional[List[SourceAccessConfiguration]] = Field(
        default=None, alias="SourceAccessConfigurations"
    )
    self_managed_event_source: Optional[SelfManagedEventSource] = Field(
        default=None, alias="SelfManagedEventSource"
    )
    maximum_record_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumRecordAgeInSeconds"
    )
    bisect_batch_on_function_error: Optional[bool] = Field(
        default=None, alias="BisectBatchOnFunctionError"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    tumbling_window_in_seconds: Optional[int] = Field(
        default=None, alias="TumblingWindowInSeconds"
    )
    function_response_types: Optional[List[Literal["ReportBatchItemFailures"]]] = Field(
        default=None, alias="FunctionResponseTypes"
    )
    amazon_managed_kafka_event_source_config: Optional[
        AmazonManagedKafkaEventSourceConfig
    ] = Field(default=None, alias="AmazonManagedKafkaEventSourceConfig")
    self_managed_kafka_event_source_config: Optional[
        SelfManagedKafkaEventSourceConfig
    ] = Field(default=None, alias="SelfManagedKafkaEventSourceConfig")
    scaling_config: Optional[ScalingConfig] = Field(default=None, alias="ScalingConfig")
    document_dbevent_source_config: Optional[DocumentDBEventSourceConfig] = Field(
        default=None, alias="DocumentDBEventSourceConfig"
    )


class UpdateEventSourceMappingRequest(BaseModel):
    uuid: str = Field(alias="UUID")
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    filter_criteria: Optional[FilterCriteria] = Field(
        default=None, alias="FilterCriteria"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    destination_config: Optional[DestinationConfig] = Field(
        default=None, alias="DestinationConfig"
    )
    maximum_record_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumRecordAgeInSeconds"
    )
    bisect_batch_on_function_error: Optional[bool] = Field(
        default=None, alias="BisectBatchOnFunctionError"
    )
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    parallelization_factor: Optional[int] = Field(
        default=None, alias="ParallelizationFactor"
    )
    source_access_configurations: Optional[Sequence[SourceAccessConfiguration]] = Field(
        default=None, alias="SourceAccessConfigurations"
    )
    tumbling_window_in_seconds: Optional[int] = Field(
        default=None, alias="TumblingWindowInSeconds"
    )
    function_response_types: Optional[
        Sequence[Literal["ReportBatchItemFailures"]]
    ] = Field(default=None, alias="FunctionResponseTypes")
    scaling_config: Optional[ScalingConfig] = Field(default=None, alias="ScalingConfig")
    document_dbevent_source_config: Optional[DocumentDBEventSourceConfig] = Field(
        default=None, alias="DocumentDBEventSourceConfig"
    )


class ListLayersResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    layers: List[LayersListItem] = Field(alias="Layers")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class FunctionConfigurationResponseMetadata(BaseModel):
    function_name: str = Field(alias="FunctionName")
    function_arn: str = Field(alias="FunctionArn")
    runtime: Literal[
        "dotnet6",
        "dotnetcore1.0",
        "dotnetcore2.0",
        "dotnetcore2.1",
        "dotnetcore3.1",
        "go1.x",
        "java11",
        "java8",
        "java8.al2",
        "nodejs",
        "nodejs10.x",
        "nodejs12.x",
        "nodejs14.x",
        "nodejs16.x",
        "nodejs18.x",
        "nodejs4.3",
        "nodejs4.3-edge",
        "nodejs6.10",
        "nodejs8.10",
        "provided",
        "provided.al2",
        "python2.7",
        "python3.6",
        "python3.7",
        "python3.8",
        "python3.9",
        "ruby2.5",
        "ruby2.7",
    ] = Field(alias="Runtime")
    role: str = Field(alias="Role")
    handler: str = Field(alias="Handler")
    code_size: int = Field(alias="CodeSize")
    description: str = Field(alias="Description")
    timeout: int = Field(alias="Timeout")
    memory_size: int = Field(alias="MemorySize")
    last_modified: str = Field(alias="LastModified")
    code_sha256: str = Field(alias="CodeSha256")
    version: str = Field(alias="Version")
    vpc_config: VpcConfigResponse = Field(alias="VpcConfig")
    dead_letter_config: DeadLetterConfig = Field(alias="DeadLetterConfig")
    environment: EnvironmentResponse = Field(alias="Environment")
    kms_key_arn: str = Field(alias="KMSKeyArn")
    tracing_config: TracingConfigResponse = Field(alias="TracingConfig")
    master_arn: str = Field(alias="MasterArn")
    revision_id: str = Field(alias="RevisionId")
    layers: List[Layer] = Field(alias="Layers")
    state: Literal["Active", "Failed", "Inactive", "Pending"] = Field(alias="State")
    state_reason: str = Field(alias="StateReason")
    state_reason_code: Literal[
        "Creating",
        "DisabledKMSKey",
        "EFSIOError",
        "EFSMountConnectivityError",
        "EFSMountFailure",
        "EFSMountTimeout",
        "EniLimitExceeded",
        "FunctionError",
        "Idle",
        "ImageAccessDenied",
        "ImageDeleted",
        "InsufficientRolePermissions",
        "InternalError",
        "InvalidConfiguration",
        "InvalidImage",
        "InvalidRuntime",
        "InvalidSecurityGroup",
        "InvalidStateKMSKey",
        "InvalidSubnet",
        "InvalidZipFileException",
        "KMSKeyAccessDenied",
        "KMSKeyNotFound",
        "Restoring",
        "SubnetOutOfIPAddresses",
    ] = Field(alias="StateReasonCode")
    last_update_status: Literal["Failed", "InProgress", "Successful"] = Field(
        alias="LastUpdateStatus"
    )
    last_update_status_reason: str = Field(alias="LastUpdateStatusReason")
    last_update_status_reason_code: Literal[
        "DisabledKMSKey",
        "EFSIOError",
        "EFSMountConnectivityError",
        "EFSMountFailure",
        "EFSMountTimeout",
        "EniLimitExceeded",
        "FunctionError",
        "ImageAccessDenied",
        "ImageDeleted",
        "InsufficientRolePermissions",
        "InternalError",
        "InvalidConfiguration",
        "InvalidImage",
        "InvalidRuntime",
        "InvalidSecurityGroup",
        "InvalidStateKMSKey",
        "InvalidSubnet",
        "InvalidZipFileException",
        "KMSKeyAccessDenied",
        "KMSKeyNotFound",
        "SubnetOutOfIPAddresses",
    ] = Field(alias="LastUpdateStatusReasonCode")
    file_system_configs: List[FileSystemConfig] = Field(alias="FileSystemConfigs")
    package_type: Literal["Image", "Zip"] = Field(alias="PackageType")
    image_config_response: ImageConfigResponse = Field(alias="ImageConfigResponse")
    signing_profile_version_arn: str = Field(alias="SigningProfileVersionArn")
    signing_job_arn: str = Field(alias="SigningJobArn")
    architectures: List[Literal["arm64", "x86_64"]] = Field(alias="Architectures")
    ephemeral_storage: EphemeralStorage = Field(alias="EphemeralStorage")
    snap_start: SnapStartResponse = Field(alias="SnapStart")
    runtime_version_config: RuntimeVersionConfig = Field(alias="RuntimeVersionConfig")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class FunctionConfiguration(BaseModel):
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    function_arn: Optional[str] = Field(default=None, alias="FunctionArn")
    runtime: Optional[
        Literal[
            "dotnet6",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "go1.x",
            "java11",
            "java8",
            "java8.al2",
            "nodejs",
            "nodejs10.x",
            "nodejs12.x",
            "nodejs14.x",
            "nodejs16.x",
            "nodejs18.x",
            "nodejs4.3",
            "nodejs4.3-edge",
            "nodejs6.10",
            "nodejs8.10",
            "provided",
            "provided.al2",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "python3.9",
            "ruby2.5",
            "ruby2.7",
        ]
    ] = Field(default=None, alias="Runtime")
    role: Optional[str] = Field(default=None, alias="Role")
    handler: Optional[str] = Field(default=None, alias="Handler")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")
    description: Optional[str] = Field(default=None, alias="Description")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    memory_size: Optional[int] = Field(default=None, alias="MemorySize")
    last_modified: Optional[str] = Field(default=None, alias="LastModified")
    code_sha256: Optional[str] = Field(default=None, alias="CodeSha256")
    version: Optional[str] = Field(default=None, alias="Version")
    vpc_config: Optional[VpcConfigResponse] = Field(default=None, alias="VpcConfig")
    dead_letter_config: Optional[DeadLetterConfig] = Field(
        default=None, alias="DeadLetterConfig"
    )
    environment: Optional[EnvironmentResponse] = Field(
        default=None, alias="Environment"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KMSKeyArn")
    tracing_config: Optional[TracingConfigResponse] = Field(
        default=None, alias="TracingConfig"
    )
    master_arn: Optional[str] = Field(default=None, alias="MasterArn")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    layers: Optional[List[Layer]] = Field(default=None, alias="Layers")
    state: Optional[Literal["Active", "Failed", "Inactive", "Pending"]] = Field(
        default=None, alias="State"
    )
    state_reason: Optional[str] = Field(default=None, alias="StateReason")
    state_reason_code: Optional[
        Literal[
            "Creating",
            "DisabledKMSKey",
            "EFSIOError",
            "EFSMountConnectivityError",
            "EFSMountFailure",
            "EFSMountTimeout",
            "EniLimitExceeded",
            "FunctionError",
            "Idle",
            "ImageAccessDenied",
            "ImageDeleted",
            "InsufficientRolePermissions",
            "InternalError",
            "InvalidConfiguration",
            "InvalidImage",
            "InvalidRuntime",
            "InvalidSecurityGroup",
            "InvalidStateKMSKey",
            "InvalidSubnet",
            "InvalidZipFileException",
            "KMSKeyAccessDenied",
            "KMSKeyNotFound",
            "Restoring",
            "SubnetOutOfIPAddresses",
        ]
    ] = Field(default=None, alias="StateReasonCode")
    last_update_status: Optional[Literal["Failed", "InProgress", "Successful"]] = Field(
        default=None, alias="LastUpdateStatus"
    )
    last_update_status_reason: Optional[str] = Field(
        default=None, alias="LastUpdateStatusReason"
    )
    last_update_status_reason_code: Optional[
        Literal[
            "DisabledKMSKey",
            "EFSIOError",
            "EFSMountConnectivityError",
            "EFSMountFailure",
            "EFSMountTimeout",
            "EniLimitExceeded",
            "FunctionError",
            "ImageAccessDenied",
            "ImageDeleted",
            "InsufficientRolePermissions",
            "InternalError",
            "InvalidConfiguration",
            "InvalidImage",
            "InvalidRuntime",
            "InvalidSecurityGroup",
            "InvalidStateKMSKey",
            "InvalidSubnet",
            "InvalidZipFileException",
            "KMSKeyAccessDenied",
            "KMSKeyNotFound",
            "SubnetOutOfIPAddresses",
        ]
    ] = Field(default=None, alias="LastUpdateStatusReasonCode")
    file_system_configs: Optional[List[FileSystemConfig]] = Field(
        default=None, alias="FileSystemConfigs"
    )
    package_type: Optional[Literal["Image", "Zip"]] = Field(
        default=None, alias="PackageType"
    )
    image_config_response: Optional[ImageConfigResponse] = Field(
        default=None, alias="ImageConfigResponse"
    )
    signing_profile_version_arn: Optional[str] = Field(
        default=None, alias="SigningProfileVersionArn"
    )
    signing_job_arn: Optional[str] = Field(default=None, alias="SigningJobArn")
    architectures: Optional[List[Literal["arm64", "x86_64"]]] = Field(
        default=None, alias="Architectures"
    )
    ephemeral_storage: Optional[EphemeralStorage] = Field(
        default=None, alias="EphemeralStorage"
    )
    snap_start: Optional[SnapStartResponse] = Field(default=None, alias="SnapStart")
    runtime_version_config: Optional[RuntimeVersionConfig] = Field(
        default=None, alias="RuntimeVersionConfig"
    )


class ListFunctionEventInvokeConfigsResponse(BaseModel):
    function_event_invoke_configs: List[FunctionEventInvokeConfig] = Field(
        alias="FunctionEventInvokeConfigs"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListEventSourceMappingsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    event_source_mappings: List[EventSourceMappingConfiguration] = Field(
        alias="EventSourceMappings"
    )
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class GetFunctionResponse(BaseModel):
    configuration: FunctionConfiguration = Field(alias="Configuration")
    code: FunctionCodeLocation = Field(alias="Code")
    tags: Dict[str, str] = Field(alias="Tags")
    concurrency: Concurrency = Field(alias="Concurrency")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListFunctionsResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    functions: List[FunctionConfiguration] = Field(alias="Functions")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")


class ListVersionsByFunctionResponse(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    versions: List[FunctionConfiguration] = Field(alias="Versions")
    response_metadata: ResponseMetadata = Field(alias="ResponseMetadata")
