# Model Generated: Thu Mar  2 21:56:20 2023

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


class AccountLimitModel(BaseModel):
    total_code_size: Optional[int] = Field(default=None, alias="TotalCodeSize")
    code_size_unzipped: Optional[int] = Field(default=None, alias="CodeSizeUnzipped")
    code_size_zipped: Optional[int] = Field(default=None, alias="CodeSizeZipped")
    concurrent_executions: Optional[int] = Field(
        default=None, alias="ConcurrentExecutions"
    )
    unreserved_concurrent_executions: Optional[int] = Field(
        default=None, alias="UnreservedConcurrentExecutions"
    )


class AccountUsageModel(BaseModel):
    total_code_size: Optional[int] = Field(default=None, alias="TotalCodeSize")
    function_count: Optional[int] = Field(default=None, alias="FunctionCount")


class AddLayerVersionPermissionRequestModel(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")
    statement_id: str = Field(alias="StatementId")
    action: str = Field(alias="Action")
    principal: str = Field(alias="Principal")
    organization_id: Optional[str] = Field(default=None, alias="OrganizationId")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AddPermissionRequestModel(BaseModel):
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


class AliasRoutingConfigurationModel(BaseModel):
    additional_version_weights: Optional[Mapping[str, float]] = Field(
        default=None, alias="AdditionalVersionWeights"
    )


class AllowedPublishersModel(BaseModel):
    signing_profile_version_arns: Sequence[str] = Field(
        alias="SigningProfileVersionArns"
    )


class AmazonManagedKafkaEventSourceConfigModel(BaseModel):
    consumer_group_id: Optional[str] = Field(default=None, alias="ConsumerGroupId")


class CodeSigningPoliciesModel(BaseModel):
    untrusted_artifact_on_deployment: Optional[Literal["Enforce", "Warn"]] = Field(
        default=None, alias="UntrustedArtifactOnDeployment"
    )


class ConcurrencyModel(BaseModel):
    reserved_concurrent_executions: Optional[int] = Field(
        default=None, alias="ReservedConcurrentExecutions"
    )


class CorsModel(BaseModel):
    allow_credentials: Optional[bool] = Field(default=None, alias="AllowCredentials")
    allow_headers: Optional[Sequence[str]] = Field(default=None, alias="AllowHeaders")
    allow_methods: Optional[Sequence[str]] = Field(default=None, alias="AllowMethods")
    allow_origins: Optional[Sequence[str]] = Field(default=None, alias="AllowOrigins")
    expose_headers: Optional[Sequence[str]] = Field(default=None, alias="ExposeHeaders")
    max_age: Optional[int] = Field(default=None, alias="MaxAge")


class DocumentDBEventSourceConfigModel(BaseModel):
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    collection_name: Optional[str] = Field(default=None, alias="CollectionName")
    full_document: Optional[Literal["Default", "UpdateLookup"]] = Field(
        default=None, alias="FullDocument"
    )


class ScalingConfigModel(BaseModel):
    maximum_concurrency: Optional[int] = Field(default=None, alias="MaximumConcurrency")


class SelfManagedEventSourceModel(BaseModel):
    endpoints: Optional[
        Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]
    ] = Field(default=None, alias="Endpoints")


class SelfManagedKafkaEventSourceConfigModel(BaseModel):
    consumer_group_id: Optional[str] = Field(default=None, alias="ConsumerGroupId")


class SourceAccessConfigurationModel(BaseModel):
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


class DeadLetterConfigModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")


class EnvironmentModel(BaseModel):
    variables: Optional[Mapping[str, str]] = Field(default=None, alias="Variables")


class EphemeralStorageModel(BaseModel):
    size: int = Field(alias="Size")


class FileSystemConfigModel(BaseModel):
    arn: str = Field(alias="Arn")
    local_mount_path: str = Field(alias="LocalMountPath")


class FunctionCodeModel(BaseModel):
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")
    s3_object_version: Optional[str] = Field(default=None, alias="S3ObjectVersion")
    image_uri: Optional[str] = Field(default=None, alias="ImageUri")


class ImageConfigModel(BaseModel):
    entry_point: Optional[Sequence[str]] = Field(default=None, alias="EntryPoint")
    command: Optional[Sequence[str]] = Field(default=None, alias="Command")
    working_directory: Optional[str] = Field(default=None, alias="WorkingDirectory")


class SnapStartModel(BaseModel):
    apply_on: Optional[Literal["None", "PublishedVersions"]] = Field(
        default=None, alias="ApplyOn"
    )


class TracingConfigModel(BaseModel):
    mode: Optional[Literal["Active", "PassThrough"]] = Field(default=None, alias="Mode")


class VpcConfigModel(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class DeleteAliasRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")


class DeleteCodeSigningConfigRequestModel(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")


class DeleteEventSourceMappingRequestModel(BaseModel):
    uuid: str = Field(alias="UUID")


class DeleteFunctionCodeSigningConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")


class DeleteFunctionConcurrencyRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")


class DeleteFunctionEventInvokeConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class DeleteFunctionRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class DeleteFunctionUrlConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class DeleteLayerVersionRequestModel(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")


class DeleteProvisionedConcurrencyConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: str = Field(alias="Qualifier")


class OnFailureModel(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")


class OnSuccessModel(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")


class EnvironmentErrorModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class FilterModel(BaseModel):
    pattern: Optional[str] = Field(default=None, alias="Pattern")


class FunctionCodeLocationModel(BaseModel):
    repository_type: Optional[str] = Field(default=None, alias="RepositoryType")
    location: Optional[str] = Field(default=None, alias="Location")
    image_uri: Optional[str] = Field(default=None, alias="ImageUri")
    resolved_image_uri: Optional[str] = Field(default=None, alias="ResolvedImageUri")


class LayerModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")
    signing_profile_version_arn: Optional[str] = Field(
        default=None, alias="SigningProfileVersionArn"
    )
    signing_job_arn: Optional[str] = Field(default=None, alias="SigningJobArn")


class SnapStartResponseModel(BaseModel):
    apply_on: Optional[Literal["None", "PublishedVersions"]] = Field(
        default=None, alias="ApplyOn"
    )
    optimization_status: Optional[Literal["Off", "On"]] = Field(
        default=None, alias="OptimizationStatus"
    )


class TracingConfigResponseModel(BaseModel):
    mode: Optional[Literal["Active", "PassThrough"]] = Field(default=None, alias="Mode")


class VpcConfigResponseModel(BaseModel):
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class GetAliasRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")


class GetCodeSigningConfigRequestModel(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")


class GetEventSourceMappingRequestModel(BaseModel):
    uuid: str = Field(alias="UUID")


class GetFunctionCodeSigningConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")


class GetFunctionConcurrencyRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetFunctionConfigurationRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetFunctionEventInvokeConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetFunctionRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetFunctionUrlConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetLayerVersionByArnRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class GetLayerVersionPolicyRequestModel(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")


class GetLayerVersionRequestModel(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")


class LayerVersionContentOutputModel(BaseModel):
    location: Optional[str] = Field(default=None, alias="Location")
    code_sha256: Optional[str] = Field(default=None, alias="CodeSha256")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")
    signing_profile_version_arn: Optional[str] = Field(
        default=None, alias="SigningProfileVersionArn"
    )
    signing_job_arn: Optional[str] = Field(default=None, alias="SigningJobArn")


class GetPolicyRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class GetProvisionedConcurrencyConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: str = Field(alias="Qualifier")


class GetRuntimeManagementConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")


class ImageConfigErrorModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class InvocationRequestModel(BaseModel):
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


class InvokeAsyncRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    invoke_args: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="InvokeArgs"
    )


class LayerVersionContentInputModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")
    s3_object_version: Optional[str] = Field(default=None, alias="S3ObjectVersion")
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )


class LayerVersionsListItemModel(BaseModel):
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


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAliasesRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListCodeSigningConfigsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListEventSourceMappingsRequestModel(BaseModel):
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionEventInvokeConfigsRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionUrlConfigsRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionsByCodeSigningConfigRequestModel(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListFunctionsRequestModel(BaseModel):
    master_region: Optional[str] = Field(default=None, alias="MasterRegion")
    function_version: Optional[Literal["ALL"]] = Field(
        default=None, alias="FunctionVersion"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ListLayerVersionsRequestModel(BaseModel):
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


class ListLayersRequestModel(BaseModel):
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


class ListProvisionedConcurrencyConfigsRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ProvisionedConcurrencyConfigListItemModel(BaseModel):
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


class ListTagsRequestModel(BaseModel):
    resource: str = Field(alias="Resource")


class ListVersionsByFunctionRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class PublishVersionRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    code_sha256: Optional[str] = Field(default=None, alias="CodeSha256")
    description: Optional[str] = Field(default=None, alias="Description")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class PutFunctionCodeSigningConfigRequestModel(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    function_name: str = Field(alias="FunctionName")


class PutFunctionConcurrencyRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    reserved_concurrent_executions: int = Field(alias="ReservedConcurrentExecutions")


class PutProvisionedConcurrencyConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: str = Field(alias="Qualifier")
    provisioned_concurrent_executions: int = Field(
        alias="ProvisionedConcurrentExecutions"
    )


class PutRuntimeManagementConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    update_runtime_on: Literal["Auto", "FunctionUpdate", "Manual"] = Field(
        alias="UpdateRuntimeOn"
    )
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    runtime_version_arn: Optional[str] = Field(default=None, alias="RuntimeVersionArn")


class RemoveLayerVersionPermissionRequestModel(BaseModel):
    layer_name: str = Field(alias="LayerName")
    version_number: int = Field(alias="VersionNumber")
    statement_id: str = Field(alias="StatementId")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class RemovePermissionRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    statement_id: str = Field(alias="StatementId")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class RuntimeVersionErrorModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class TagResourceRequestModel(BaseModel):
    resource: str = Field(alias="Resource")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource: str = Field(alias="Resource")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateFunctionCodeRequestModel(BaseModel):
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


class AddLayerVersionPermissionResponseModel(BaseModel):
    statement: str = Field(alias="Statement")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddPermissionResponseModel(BaseModel):
    statement: str = Field(alias="Statement")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConcurrencyResponseMetadataModel(BaseModel):
    reserved_concurrent_executions: int = Field(alias="ReservedConcurrentExecutions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountSettingsResponseModel(BaseModel):
    account_limit: AccountLimitModel = Field(alias="AccountLimit")
    account_usage: AccountUsageModel = Field(alias="AccountUsage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFunctionCodeSigningConfigResponseModel(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    function_name: str = Field(alias="FunctionName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFunctionConcurrencyResponseModel(BaseModel):
    reserved_concurrent_executions: int = Field(alias="ReservedConcurrentExecutions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLayerVersionPolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProvisionedConcurrencyConfigResponseModel(BaseModel):
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
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRuntimeManagementConfigResponseModel(BaseModel):
    update_runtime_on: Literal["Auto", "FunctionUpdate", "Manual"] = Field(
        alias="UpdateRuntimeOn"
    )
    runtime_version_arn: str = Field(alias="RuntimeVersionArn")
    function_arn: str = Field(alias="FunctionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvocationResponseModel(BaseModel):
    status_code: int = Field(alias="StatusCode")
    function_error: str = Field(alias="FunctionError")
    log_result: str = Field(alias="LogResult")
    payload: Type[StreamingBody] = Field(alias="Payload")
    executed_version: str = Field(alias="ExecutedVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvokeAsyncResponseModel(BaseModel):
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFunctionsByCodeSigningConfigResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    function_arns: List[str] = Field(alias="FunctionArns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutFunctionCodeSigningConfigResponseModel(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    function_name: str = Field(alias="FunctionName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutProvisionedConcurrencyConfigResponseModel(BaseModel):
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
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRuntimeManagementConfigResponseModel(BaseModel):
    update_runtime_on: Literal["Auto", "FunctionUpdate", "Manual"] = Field(
        alias="UpdateRuntimeOn"
    )
    function_arn: str = Field(alias="FunctionArn")
    runtime_version_arn: str = Field(alias="RuntimeVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AliasConfigurationResponseMetadataModel(BaseModel):
    alias_arn: str = Field(alias="AliasArn")
    name: str = Field(alias="Name")
    function_version: str = Field(alias="FunctionVersion")
    description: str = Field(alias="Description")
    routing_config: AliasRoutingConfigurationModel = Field(alias="RoutingConfig")
    revision_id: str = Field(alias="RevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AliasConfigurationModel(BaseModel):
    alias_arn: Optional[str] = Field(default=None, alias="AliasArn")
    name: Optional[str] = Field(default=None, alias="Name")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_config: Optional[AliasRoutingConfigurationModel] = Field(
        default=None, alias="RoutingConfig"
    )
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class CreateAliasRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")
    function_version: str = Field(alias="FunctionVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_config: Optional[AliasRoutingConfigurationModel] = Field(
        default=None, alias="RoutingConfig"
    )


class UpdateAliasRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    name: str = Field(alias="Name")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_config: Optional[AliasRoutingConfigurationModel] = Field(
        default=None, alias="RoutingConfig"
    )
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class CodeSigningConfigModel(BaseModel):
    code_signing_config_id: str = Field(alias="CodeSigningConfigId")
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    allowed_publishers: AllowedPublishersModel = Field(alias="AllowedPublishers")
    code_signing_policies: CodeSigningPoliciesModel = Field(alias="CodeSigningPolicies")
    last_modified: str = Field(alias="LastModified")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateCodeSigningConfigRequestModel(BaseModel):
    allowed_publishers: AllowedPublishersModel = Field(alias="AllowedPublishers")
    description: Optional[str] = Field(default=None, alias="Description")
    code_signing_policies: Optional[CodeSigningPoliciesModel] = Field(
        default=None, alias="CodeSigningPolicies"
    )


class UpdateCodeSigningConfigRequestModel(BaseModel):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    description: Optional[str] = Field(default=None, alias="Description")
    allowed_publishers: Optional[AllowedPublishersModel] = Field(
        default=None, alias="AllowedPublishers"
    )
    code_signing_policies: Optional[CodeSigningPoliciesModel] = Field(
        default=None, alias="CodeSigningPolicies"
    )


class CreateFunctionUrlConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    cors: Optional[CorsModel] = Field(default=None, alias="Cors")


class CreateFunctionUrlConfigResponseModel(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: CorsModel = Field(alias="Cors")
    creation_time: str = Field(alias="CreationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionUrlConfigModel(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    creation_time: str = Field(alias="CreationTime")
    last_modified_time: str = Field(alias="LastModifiedTime")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: Optional[CorsModel] = Field(default=None, alias="Cors")


class GetFunctionUrlConfigResponseModel(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: CorsModel = Field(alias="Cors")
    creation_time: str = Field(alias="CreationTime")
    last_modified_time: str = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFunctionUrlConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    auth_type: Optional[Literal["AWS_IAM", "NONE"]] = Field(
        default=None, alias="AuthType"
    )
    cors: Optional[CorsModel] = Field(default=None, alias="Cors")


class UpdateFunctionUrlConfigResponseModel(BaseModel):
    function_url: str = Field(alias="FunctionUrl")
    function_arn: str = Field(alias="FunctionArn")
    auth_type: Literal["AWS_IAM", "NONE"] = Field(alias="AuthType")
    cors: CorsModel = Field(alias="Cors")
    creation_time: str = Field(alias="CreationTime")
    last_modified_time: str = Field(alias="LastModifiedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFunctionRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    role: str = Field(alias="Role")
    code: FunctionCodeModel = Field(alias="Code")
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
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    package_type: Optional[Literal["Image", "Zip"]] = Field(
        default=None, alias="PackageType"
    )
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    environment: Optional[EnvironmentModel] = Field(default=None, alias="Environment")
    kms_key_arn: Optional[str] = Field(default=None, alias="KMSKeyArn")
    tracing_config: Optional[TracingConfigModel] = Field(
        default=None, alias="TracingConfig"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    layers: Optional[Sequence[str]] = Field(default=None, alias="Layers")
    file_system_configs: Optional[Sequence[FileSystemConfigModel]] = Field(
        default=None, alias="FileSystemConfigs"
    )
    image_config: Optional[ImageConfigModel] = Field(default=None, alias="ImageConfig")
    code_signing_config_arn: Optional[str] = Field(
        default=None, alias="CodeSigningConfigArn"
    )
    architectures: Optional[Sequence[Literal["arm64", "x86_64"]]] = Field(
        default=None, alias="Architectures"
    )
    ephemeral_storage: Optional[EphemeralStorageModel] = Field(
        default=None, alias="EphemeralStorage"
    )
    snap_start: Optional[SnapStartModel] = Field(default=None, alias="SnapStart")


class UpdateFunctionConfigurationRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    role: Optional[str] = Field(default=None, alias="Role")
    handler: Optional[str] = Field(default=None, alias="Handler")
    description: Optional[str] = Field(default=None, alias="Description")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    memory_size: Optional[int] = Field(default=None, alias="MemorySize")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    environment: Optional[EnvironmentModel] = Field(default=None, alias="Environment")
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
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KMSKeyArn")
    tracing_config: Optional[TracingConfigModel] = Field(
        default=None, alias="TracingConfig"
    )
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    layers: Optional[Sequence[str]] = Field(default=None, alias="Layers")
    file_system_configs: Optional[Sequence[FileSystemConfigModel]] = Field(
        default=None, alias="FileSystemConfigs"
    )
    image_config: Optional[ImageConfigModel] = Field(default=None, alias="ImageConfig")
    ephemeral_storage: Optional[EphemeralStorageModel] = Field(
        default=None, alias="EphemeralStorage"
    )
    snap_start: Optional[SnapStartModel] = Field(default=None, alias="SnapStart")


class DestinationConfigModel(BaseModel):
    on_success: Optional[OnSuccessModel] = Field(default=None, alias="OnSuccess")
    on_failure: Optional[OnFailureModel] = Field(default=None, alias="OnFailure")


class EnvironmentResponseModel(BaseModel):
    variables: Optional[Dict[str, str]] = Field(default=None, alias="Variables")
    error: Optional[EnvironmentErrorModel] = Field(default=None, alias="Error")


class FilterCriteriaModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class GetFunctionConfigurationRequestFunctionActiveWaitModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetFunctionConfigurationRequestFunctionUpdatedWaitModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetFunctionConfigurationRequestPublishedVersionActiveWaitModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetFunctionRequestFunctionActiveV2WaitModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetFunctionRequestFunctionExistsWaitModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetFunctionRequestFunctionUpdatedV2WaitModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetLayerVersionResponseModel(BaseModel):
    content: LayerVersionContentOutputModel = Field(alias="Content")
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
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishLayerVersionResponseModel(BaseModel):
    content: LayerVersionContentOutputModel = Field(alias="Content")
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
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImageConfigResponseModel(BaseModel):
    image_config: Optional[ImageConfigModel] = Field(default=None, alias="ImageConfig")
    error: Optional[ImageConfigErrorModel] = Field(default=None, alias="Error")


class PublishLayerVersionRequestModel(BaseModel):
    layer_name: str = Field(alias="LayerName")
    content: LayerVersionContentInputModel = Field(alias="Content")
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


class LayersListItemModel(BaseModel):
    layer_name: Optional[str] = Field(default=None, alias="LayerName")
    layer_arn: Optional[str] = Field(default=None, alias="LayerArn")
    latest_matching_version: Optional[LayerVersionsListItemModel] = Field(
        default=None, alias="LatestMatchingVersion"
    )


class ListLayerVersionsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    layer_versions: List[LayerVersionsListItemModel] = Field(alias="LayerVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAliasesRequestListAliasesPaginateModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    function_version: Optional[str] = Field(default=None, alias="FunctionVersion")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCodeSigningConfigsRequestListCodeSigningConfigsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEventSourceMappingsRequestListEventSourceMappingsPaginateModel(BaseModel):
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionEventInvokeConfigsRequestListFunctionEventInvokeConfigsPaginateModel(
    BaseModel
):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionUrlConfigsRequestListFunctionUrlConfigsPaginateModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionsByCodeSigningConfigRequestListFunctionsByCodeSigningConfigPaginateModel(
    BaseModel
):
    code_signing_config_arn: str = Field(alias="CodeSigningConfigArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionsRequestListFunctionsPaginateModel(BaseModel):
    master_region: Optional[str] = Field(default=None, alias="MasterRegion")
    function_version: Optional[Literal["ALL"]] = Field(
        default=None, alias="FunctionVersion"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLayerVersionsRequestListLayerVersionsPaginateModel(BaseModel):
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
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLayersRequestListLayersPaginateModel(BaseModel):
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
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisionedConcurrencyConfigsRequestListProvisionedConcurrencyConfigsPaginateModel(
    BaseModel
):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVersionsByFunctionRequestListVersionsByFunctionPaginateModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisionedConcurrencyConfigsResponseModel(BaseModel):
    provisioned_concurrency_configs: List[
        ProvisionedConcurrencyConfigListItemModel
    ] = Field(alias="ProvisionedConcurrencyConfigs")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuntimeVersionConfigModel(BaseModel):
    runtime_version_arn: Optional[str] = Field(default=None, alias="RuntimeVersionArn")
    error: Optional[RuntimeVersionErrorModel] = Field(default=None, alias="Error")


class ListAliasesResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    aliases: List[AliasConfigurationModel] = Field(alias="Aliases")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCodeSigningConfigResponseModel(BaseModel):
    code_signing_config: CodeSigningConfigModel = Field(alias="CodeSigningConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCodeSigningConfigResponseModel(BaseModel):
    code_signing_config: CodeSigningConfigModel = Field(alias="CodeSigningConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCodeSigningConfigsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    code_signing_configs: List[CodeSigningConfigModel] = Field(
        alias="CodeSigningConfigs"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCodeSigningConfigResponseModel(BaseModel):
    code_signing_config: CodeSigningConfigModel = Field(alias="CodeSigningConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFunctionUrlConfigsResponseModel(BaseModel):
    function_url_configs: List[FunctionUrlConfigModel] = Field(
        alias="FunctionUrlConfigs"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionEventInvokeConfigResponseMetadataModel(BaseModel):
    last_modified: datetime = Field(alias="LastModified")
    function_arn: str = Field(alias="FunctionArn")
    maximum_retry_attempts: int = Field(alias="MaximumRetryAttempts")
    maximum_event_age_in_seconds: int = Field(alias="MaximumEventAgeInSeconds")
    destination_config: DestinationConfigModel = Field(alias="DestinationConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionEventInvokeConfigModel(BaseModel):
    last_modified: Optional[datetime] = Field(default=None, alias="LastModified")
    function_arn: Optional[str] = Field(default=None, alias="FunctionArn")
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )
    destination_config: Optional[DestinationConfigModel] = Field(
        default=None, alias="DestinationConfig"
    )


class PutFunctionEventInvokeConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )
    destination_config: Optional[DestinationConfigModel] = Field(
        default=None, alias="DestinationConfig"
    )


class UpdateFunctionEventInvokeConfigRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    qualifier: Optional[str] = Field(default=None, alias="Qualifier")
    maximum_retry_attempts: Optional[int] = Field(
        default=None, alias="MaximumRetryAttempts"
    )
    maximum_event_age_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumEventAgeInSeconds"
    )
    destination_config: Optional[DestinationConfigModel] = Field(
        default=None, alias="DestinationConfig"
    )


class CreateEventSourceMappingRequestModel(BaseModel):
    function_name: str = Field(alias="FunctionName")
    event_source_arn: Optional[str] = Field(default=None, alias="EventSourceArn")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
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
    destination_config: Optional[DestinationConfigModel] = Field(
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
    source_access_configurations: Optional[
        Sequence[SourceAccessConfigurationModel]
    ] = Field(default=None, alias="SourceAccessConfigurations")
    self_managed_event_source: Optional[SelfManagedEventSourceModel] = Field(
        default=None, alias="SelfManagedEventSource"
    )
    function_response_types: Optional[
        Sequence[Literal["ReportBatchItemFailures"]]
    ] = Field(default=None, alias="FunctionResponseTypes")
    amazon_managed_kafka_event_source_config: Optional[
        AmazonManagedKafkaEventSourceConfigModel
    ] = Field(default=None, alias="AmazonManagedKafkaEventSourceConfig")
    self_managed_kafka_event_source_config: Optional[
        SelfManagedKafkaEventSourceConfigModel
    ] = Field(default=None, alias="SelfManagedKafkaEventSourceConfig")
    scaling_config: Optional[ScalingConfigModel] = Field(
        default=None, alias="ScalingConfig"
    )
    document_dbevent_source_config: Optional[DocumentDBEventSourceConfigModel] = Field(
        default=None, alias="DocumentDBEventSourceConfig"
    )


class EventSourceMappingConfigurationResponseMetadataModel(BaseModel):
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
    filter_criteria: FilterCriteriaModel = Field(alias="FilterCriteria")
    function_arn: str = Field(alias="FunctionArn")
    last_modified: datetime = Field(alias="LastModified")
    last_processing_result: str = Field(alias="LastProcessingResult")
    state: str = Field(alias="State")
    state_transition_reason: str = Field(alias="StateTransitionReason")
    destination_config: DestinationConfigModel = Field(alias="DestinationConfig")
    topics: List[str] = Field(alias="Topics")
    queues: List[str] = Field(alias="Queues")
    source_access_configurations: List[SourceAccessConfigurationModel] = Field(
        alias="SourceAccessConfigurations"
    )
    self_managed_event_source: SelfManagedEventSourceModel = Field(
        alias="SelfManagedEventSource"
    )
    maximum_record_age_in_seconds: int = Field(alias="MaximumRecordAgeInSeconds")
    bisect_batch_on_function_error: bool = Field(alias="BisectBatchOnFunctionError")
    maximum_retry_attempts: int = Field(alias="MaximumRetryAttempts")
    tumbling_window_in_seconds: int = Field(alias="TumblingWindowInSeconds")
    function_response_types: List[Literal["ReportBatchItemFailures"]] = Field(
        alias="FunctionResponseTypes"
    )
    amazon_managed_kafka_event_source_config: AmazonManagedKafkaEventSourceConfigModel = Field(
        alias="AmazonManagedKafkaEventSourceConfig"
    )
    self_managed_kafka_event_source_config: SelfManagedKafkaEventSourceConfigModel = (
        Field(alias="SelfManagedKafkaEventSourceConfig")
    )
    scaling_config: ScalingConfigModel = Field(alias="ScalingConfig")
    document_dbevent_source_config: DocumentDBEventSourceConfigModel = Field(
        alias="DocumentDBEventSourceConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventSourceMappingConfigurationModel(BaseModel):
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
    filter_criteria: Optional[FilterCriteriaModel] = Field(
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
    destination_config: Optional[DestinationConfigModel] = Field(
        default=None, alias="DestinationConfig"
    )
    topics: Optional[List[str]] = Field(default=None, alias="Topics")
    queues: Optional[List[str]] = Field(default=None, alias="Queues")
    source_access_configurations: Optional[
        List[SourceAccessConfigurationModel]
    ] = Field(default=None, alias="SourceAccessConfigurations")
    self_managed_event_source: Optional[SelfManagedEventSourceModel] = Field(
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
        AmazonManagedKafkaEventSourceConfigModel
    ] = Field(default=None, alias="AmazonManagedKafkaEventSourceConfig")
    self_managed_kafka_event_source_config: Optional[
        SelfManagedKafkaEventSourceConfigModel
    ] = Field(default=None, alias="SelfManagedKafkaEventSourceConfig")
    scaling_config: Optional[ScalingConfigModel] = Field(
        default=None, alias="ScalingConfig"
    )
    document_dbevent_source_config: Optional[DocumentDBEventSourceConfigModel] = Field(
        default=None, alias="DocumentDBEventSourceConfig"
    )


class UpdateEventSourceMappingRequestModel(BaseModel):
    uuid: str = Field(alias="UUID")
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    batch_size: Optional[int] = Field(default=None, alias="BatchSize")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="FilterCriteria"
    )
    maximum_batching_window_in_seconds: Optional[int] = Field(
        default=None, alias="MaximumBatchingWindowInSeconds"
    )
    destination_config: Optional[DestinationConfigModel] = Field(
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
    source_access_configurations: Optional[
        Sequence[SourceAccessConfigurationModel]
    ] = Field(default=None, alias="SourceAccessConfigurations")
    tumbling_window_in_seconds: Optional[int] = Field(
        default=None, alias="TumblingWindowInSeconds"
    )
    function_response_types: Optional[
        Sequence[Literal["ReportBatchItemFailures"]]
    ] = Field(default=None, alias="FunctionResponseTypes")
    scaling_config: Optional[ScalingConfigModel] = Field(
        default=None, alias="ScalingConfig"
    )
    document_dbevent_source_config: Optional[DocumentDBEventSourceConfigModel] = Field(
        default=None, alias="DocumentDBEventSourceConfig"
    )


class ListLayersResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    layers: List[LayersListItemModel] = Field(alias="Layers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionConfigurationResponseMetadataModel(BaseModel):
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
    vpc_config: VpcConfigResponseModel = Field(alias="VpcConfig")
    dead_letter_config: DeadLetterConfigModel = Field(alias="DeadLetterConfig")
    environment: EnvironmentResponseModel = Field(alias="Environment")
    kms_key_arn: str = Field(alias="KMSKeyArn")
    tracing_config: TracingConfigResponseModel = Field(alias="TracingConfig")
    master_arn: str = Field(alias="MasterArn")
    revision_id: str = Field(alias="RevisionId")
    layers: List[LayerModel] = Field(alias="Layers")
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
    file_system_configs: List[FileSystemConfigModel] = Field(alias="FileSystemConfigs")
    package_type: Literal["Image", "Zip"] = Field(alias="PackageType")
    image_config_response: ImageConfigResponseModel = Field(alias="ImageConfigResponse")
    signing_profile_version_arn: str = Field(alias="SigningProfileVersionArn")
    signing_job_arn: str = Field(alias="SigningJobArn")
    architectures: List[Literal["arm64", "x86_64"]] = Field(alias="Architectures")
    ephemeral_storage: EphemeralStorageModel = Field(alias="EphemeralStorage")
    snap_start: SnapStartResponseModel = Field(alias="SnapStart")
    runtime_version_config: RuntimeVersionConfigModel = Field(
        alias="RuntimeVersionConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionConfigurationModel(BaseModel):
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
    vpc_config: Optional[VpcConfigResponseModel] = Field(
        default=None, alias="VpcConfig"
    )
    dead_letter_config: Optional[DeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    environment: Optional[EnvironmentResponseModel] = Field(
        default=None, alias="Environment"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KMSKeyArn")
    tracing_config: Optional[TracingConfigResponseModel] = Field(
        default=None, alias="TracingConfig"
    )
    master_arn: Optional[str] = Field(default=None, alias="MasterArn")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    layers: Optional[List[LayerModel]] = Field(default=None, alias="Layers")
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
    file_system_configs: Optional[List[FileSystemConfigModel]] = Field(
        default=None, alias="FileSystemConfigs"
    )
    package_type: Optional[Literal["Image", "Zip"]] = Field(
        default=None, alias="PackageType"
    )
    image_config_response: Optional[ImageConfigResponseModel] = Field(
        default=None, alias="ImageConfigResponse"
    )
    signing_profile_version_arn: Optional[str] = Field(
        default=None, alias="SigningProfileVersionArn"
    )
    signing_job_arn: Optional[str] = Field(default=None, alias="SigningJobArn")
    architectures: Optional[List[Literal["arm64", "x86_64"]]] = Field(
        default=None, alias="Architectures"
    )
    ephemeral_storage: Optional[EphemeralStorageModel] = Field(
        default=None, alias="EphemeralStorage"
    )
    snap_start: Optional[SnapStartResponseModel] = Field(
        default=None, alias="SnapStart"
    )
    runtime_version_config: Optional[RuntimeVersionConfigModel] = Field(
        default=None, alias="RuntimeVersionConfig"
    )


class ListFunctionEventInvokeConfigsResponseModel(BaseModel):
    function_event_invoke_configs: List[FunctionEventInvokeConfigModel] = Field(
        alias="FunctionEventInvokeConfigs"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEventSourceMappingsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    event_source_mappings: List[EventSourceMappingConfigurationModel] = Field(
        alias="EventSourceMappings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFunctionResponseModel(BaseModel):
    configuration: FunctionConfigurationModel = Field(alias="Configuration")
    code: FunctionCodeLocationModel = Field(alias="Code")
    tags: Dict[str, str] = Field(alias="Tags")
    concurrency: ConcurrencyModel = Field(alias="Concurrency")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFunctionsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    functions: List[FunctionConfigurationModel] = Field(alias="Functions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVersionsByFunctionResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    versions: List[FunctionConfigurationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
