# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class SystemsManagerAgentModel(BaseModel):
    uninstall_after_build: Optional[bool] = Field(
        default=None, alias="uninstallAfterBuild"
    )


class LaunchPermissionConfigurationModel(BaseModel):
    user_ids: Optional[Sequence[str]] = Field(default=None, alias="userIds")
    user_groups: Optional[Sequence[str]] = Field(default=None, alias="userGroups")
    organization_arns: Optional[Sequence[str]] = Field(
        default=None, alias="organizationArns"
    )
    organizational_unit_arns: Optional[Sequence[str]] = Field(
        default=None, alias="organizationalUnitArns"
    )


class ImageStateModel(BaseModel):
    status: Optional[
        Literal[
            "AVAILABLE",
            "BUILDING",
            "CANCELLED",
            "CREATING",
            "DELETED",
            "DEPRECATED",
            "DISTRIBUTING",
            "FAILED",
            "INTEGRATING",
            "PENDING",
            "TESTING",
        ]
    ] = Field(default=None, alias="status")
    reason: Optional[str] = Field(default=None, alias="reason")


class CancelImageCreationRequestModel(BaseModel):
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")
    client_token: str = Field(alias="clientToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ComponentParameterModel(BaseModel):
    name: str = Field(alias="name")
    value: Sequence[str] = Field(alias="value")


class ComponentParameterDetailModel(BaseModel):
    name: str = Field(alias="name")
    type: str = Field(alias="type")
    default_value: Optional[List[str]] = Field(default=None, alias="defaultValue")
    description: Optional[str] = Field(default=None, alias="description")


class ComponentStateModel(BaseModel):
    status: Optional[Literal["DEPRECATED"]] = Field(default=None, alias="status")
    reason: Optional[str] = Field(default=None, alias="reason")


class ComponentVersionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")
    description: Optional[str] = Field(default=None, alias="description")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    supported_os_versions: Optional[List[str]] = Field(
        default=None, alias="supportedOsVersions"
    )
    type: Optional[Literal["BUILD", "TEST"]] = Field(default=None, alias="type")
    owner: Optional[str] = Field(default=None, alias="owner")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")


class TargetContainerRepositoryModel(BaseModel):
    service: Literal["ECR"] = Field(alias="service")
    repository_name: str = Field(alias="repositoryName")


class ContainerRecipeSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    container_type: Optional[Literal["DOCKER"]] = Field(
        default=None, alias="containerType"
    )
    name: Optional[str] = Field(default=None, alias="name")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    owner: Optional[str] = Field(default=None, alias="owner")
    parent_image: Optional[str] = Field(default=None, alias="parentImage")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ContainerModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="region")
    image_uris: Optional[List[str]] = Field(default=None, alias="imageUris")


class CreateComponentRequestModel(BaseModel):
    name: str = Field(alias="name")
    semantic_version: str = Field(alias="semanticVersion")
    platform: Literal["Linux", "Windows"] = Field(alias="platform")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    change_description: Optional[str] = Field(default=None, alias="changeDescription")
    supported_os_versions: Optional[Sequence[str]] = Field(
        default=None, alias="supportedOsVersions"
    )
    data: Optional[str] = Field(default=None, alias="data")
    uri: Optional[str] = Field(default=None, alias="uri")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ImageTestsConfigurationModel(BaseModel):
    image_tests_enabled: Optional[bool] = Field(default=None, alias="imageTestsEnabled")
    timeout_minutes: Optional[int] = Field(default=None, alias="timeoutMinutes")


class ScheduleModel(BaseModel):
    schedule_expression: Optional[str] = Field(default=None, alias="scheduleExpression")
    timezone: Optional[str] = Field(default=None, alias="timezone")
    pipeline_execution_start_condition: Optional[
        Literal[
            "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE", "EXPRESSION_MATCH_ONLY"
        ]
    ] = Field(default=None, alias="pipelineExecutionStartCondition")


class InstanceMetadataOptionsModel(BaseModel):
    http_tokens: Optional[str] = Field(default=None, alias="httpTokens")
    http_put_response_hop_limit: Optional[int] = Field(
        default=None, alias="httpPutResponseHopLimit"
    )


class DeleteComponentRequestModel(BaseModel):
    component_build_version_arn: str = Field(alias="componentBuildVersionArn")


class DeleteContainerRecipeRequestModel(BaseModel):
    container_recipe_arn: str = Field(alias="containerRecipeArn")


class DeleteDistributionConfigurationRequestModel(BaseModel):
    distribution_configuration_arn: str = Field(alias="distributionConfigurationArn")


class DeleteImagePipelineRequestModel(BaseModel):
    image_pipeline_arn: str = Field(alias="imagePipelineArn")


class DeleteImageRecipeRequestModel(BaseModel):
    image_recipe_arn: str = Field(alias="imageRecipeArn")


class DeleteImageRequestModel(BaseModel):
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")


class DeleteInfrastructureConfigurationRequestModel(BaseModel):
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )


class DistributionConfigurationSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    date_updated: Optional[str] = Field(default=None, alias="dateUpdated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    regions: Optional[List[str]] = Field(default=None, alias="regions")


class LaunchTemplateConfigurationModel(BaseModel):
    launch_template_id: str = Field(alias="launchTemplateId")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    set_default_version: Optional[bool] = Field(default=None, alias="setDefaultVersion")


class S3ExportConfigurationModel(BaseModel):
    role_name: str = Field(alias="roleName")
    disk_image_format: Literal["RAW", "VHD", "VMDK"] = Field(alias="diskImageFormat")
    s3_bucket: str = Field(alias="s3Bucket")
    s3_prefix: Optional[str] = Field(default=None, alias="s3Prefix")


class EbsInstanceBlockDeviceSpecificationModel(BaseModel):
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="deleteOnTermination"
    )
    iops: Optional[int] = Field(default=None, alias="iops")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    snapshot_id: Optional[str] = Field(default=None, alias="snapshotId")
    volume_size: Optional[int] = Field(default=None, alias="volumeSize")
    volume_type: Optional[
        Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
    ] = Field(default=None, alias="volumeType")
    throughput: Optional[int] = Field(default=None, alias="throughput")


class FastLaunchLaunchTemplateSpecificationModel(BaseModel):
    launch_template_id: Optional[str] = Field(default=None, alias="launchTemplateId")
    launch_template_name: Optional[str] = Field(
        default=None, alias="launchTemplateName"
    )
    launch_template_version: Optional[str] = Field(
        default=None, alias="launchTemplateVersion"
    )


class FastLaunchSnapshotConfigurationModel(BaseModel):
    target_resource_count: Optional[int] = Field(
        default=None, alias="targetResourceCount"
    )


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class GetComponentPolicyRequestModel(BaseModel):
    component_arn: str = Field(alias="componentArn")


class GetComponentRequestModel(BaseModel):
    component_build_version_arn: str = Field(alias="componentBuildVersionArn")


class GetContainerRecipePolicyRequestModel(BaseModel):
    container_recipe_arn: str = Field(alias="containerRecipeArn")


class GetContainerRecipeRequestModel(BaseModel):
    container_recipe_arn: str = Field(alias="containerRecipeArn")


class GetDistributionConfigurationRequestModel(BaseModel):
    distribution_configuration_arn: str = Field(alias="distributionConfigurationArn")


class GetImagePipelineRequestModel(BaseModel):
    image_pipeline_arn: str = Field(alias="imagePipelineArn")


class GetImagePolicyRequestModel(BaseModel):
    image_arn: str = Field(alias="imageArn")


class GetImageRecipePolicyRequestModel(BaseModel):
    image_recipe_arn: str = Field(alias="imageRecipeArn")


class GetImageRecipeRequestModel(BaseModel):
    image_recipe_arn: str = Field(alias="imageRecipeArn")


class GetImageRequestModel(BaseModel):
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")


class GetInfrastructureConfigurationRequestModel(BaseModel):
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )


class ImagePackageModel(BaseModel):
    package_name: Optional[str] = Field(default=None, alias="packageName")
    package_version: Optional[str] = Field(default=None, alias="packageVersion")


class ImageRecipeSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    owner: Optional[str] = Field(default=None, alias="owner")
    parent_image: Optional[str] = Field(default=None, alias="parentImage")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ImageVersionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["AMI", "DOCKER"]] = Field(default=None, alias="type")
    version: Optional[str] = Field(default=None, alias="version")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    os_version: Optional[str] = Field(default=None, alias="osVersion")
    owner: Optional[str] = Field(default=None, alias="owner")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    build_type: Optional[Literal["IMPORT", "SCHEDULED", "USER_INITIATED"]] = Field(
        default=None, alias="buildType"
    )
    image_source: Optional[
        Literal["AMAZON_MANAGED", "AWS_MARKETPLACE", "CUSTOM", "IMPORTED"]
    ] = Field(default=None, alias="imageSource")


class ImportComponentRequestModel(BaseModel):
    name: str = Field(alias="name")
    semantic_version: str = Field(alias="semanticVersion")
    type: Literal["BUILD", "TEST"] = Field(alias="type")
    format: Literal["SHELL"] = Field(alias="format")
    platform: Literal["Linux", "Windows"] = Field(alias="platform")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    change_description: Optional[str] = Field(default=None, alias="changeDescription")
    data: Optional[str] = Field(default=None, alias="data")
    uri: Optional[str] = Field(default=None, alias="uri")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ImportVmImageRequestModel(BaseModel):
    name: str = Field(alias="name")
    semantic_version: str = Field(alias="semanticVersion")
    platform: Literal["Linux", "Windows"] = Field(alias="platform")
    vm_import_task_id: str = Field(alias="vmImportTaskId")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    os_version: Optional[str] = Field(default=None, alias="osVersion")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class InfrastructureConfigurationSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    date_updated: Optional[str] = Field(default=None, alias="dateUpdated")
    resource_tags: Optional[Dict[str, str]] = Field(default=None, alias="resourceTags")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    instance_types: Optional[List[str]] = Field(default=None, alias="instanceTypes")
    instance_profile_name: Optional[str] = Field(
        default=None, alias="instanceProfileName"
    )


class ListComponentBuildVersionsRequestModel(BaseModel):
    component_version_arn: str = Field(alias="componentVersionArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImagePackagesRequestModel(BaseModel):
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class S3LogsModel(BaseModel):
    s3_bucket_name: Optional[str] = Field(default=None, alias="s3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="s3KeyPrefix")


class PutComponentPolicyRequestModel(BaseModel):
    component_arn: str = Field(alias="componentArn")
    policy: str = Field(alias="policy")


class PutContainerRecipePolicyRequestModel(BaseModel):
    container_recipe_arn: str = Field(alias="containerRecipeArn")
    policy: str = Field(alias="policy")


class PutImagePolicyRequestModel(BaseModel):
    image_arn: str = Field(alias="imageArn")
    policy: str = Field(alias="policy")


class PutImageRecipePolicyRequestModel(BaseModel):
    image_recipe_arn: str = Field(alias="imageRecipeArn")
    policy: str = Field(alias="policy")


class StartImagePipelineExecutionRequestModel(BaseModel):
    image_pipeline_arn: str = Field(alias="imagePipelineArn")
    client_token: str = Field(alias="clientToken")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class AdditionalInstanceConfigurationModel(BaseModel):
    systems_manager_agent: Optional[SystemsManagerAgentModel] = Field(
        default=None, alias="systemsManagerAgent"
    )
    user_data_override: Optional[str] = Field(default=None, alias="userDataOverride")


class AmiDistributionConfigurationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    target_account_ids: Optional[Sequence[str]] = Field(
        default=None, alias="targetAccountIds"
    )
    ami_tags: Optional[Mapping[str, str]] = Field(default=None, alias="amiTags")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    launch_permission: Optional[LaunchPermissionConfigurationModel] = Field(
        default=None, alias="launchPermission"
    )


class AmiModel(BaseModel):
    region: Optional[str] = Field(default=None, alias="region")
    image: Optional[str] = Field(default=None, alias="image")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    state: Optional[ImageStateModel] = Field(default=None, alias="state")
    account_id: Optional[str] = Field(default=None, alias="accountId")


class CancelImageCreationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateComponentResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    component_build_version_arn: str = Field(alias="componentBuildVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContainerRecipeResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    container_recipe_arn: str = Field(alias="containerRecipeArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDistributionConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    distribution_configuration_arn: str = Field(alias="distributionConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImagePipelineResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    image_pipeline_arn: str = Field(alias="imagePipelineArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageRecipeResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    image_recipe_arn: str = Field(alias="imageRecipeArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInfrastructureConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteComponentResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    component_build_version_arn: str = Field(alias="componentBuildVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteContainerRecipeResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    container_recipe_arn: str = Field(alias="containerRecipeArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDistributionConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    distribution_configuration_arn: str = Field(alias="distributionConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteImagePipelineResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_pipeline_arn: str = Field(alias="imagePipelineArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteImageRecipeResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_recipe_arn: str = Field(alias="imageRecipeArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteImageResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInfrastructureConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentPolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    policy: str = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContainerRecipePolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    policy: str = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImagePolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    policy: str = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImageRecipePolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    policy: str = Field(alias="policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportComponentResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    component_build_version_arn: str = Field(alias="componentBuildVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportVmImageResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_arn: str = Field(alias="imageArn")
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutComponentPolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    component_arn: str = Field(alias="componentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutContainerRecipePolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    container_recipe_arn: str = Field(alias="containerRecipeArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutImagePolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_arn: str = Field(alias="imageArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutImageRecipePolicyResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_recipe_arn: str = Field(alias="imageRecipeArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImagePipelineExecutionResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    image_build_version_arn: str = Field(alias="imageBuildVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDistributionConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    distribution_configuration_arn: str = Field(alias="distributionConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateImagePipelineResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    image_pipeline_arn: str = Field(alias="imagePipelineArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInfrastructureConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    client_token: str = Field(alias="clientToken")
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComponentConfigurationModel(BaseModel):
    component_arn: str = Field(alias="componentArn")
    parameters: Optional[Sequence[ComponentParameterModel]] = Field(
        default=None, alias="parameters"
    )


class ComponentSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    supported_os_versions: Optional[List[str]] = Field(
        default=None, alias="supportedOsVersions"
    )
    state: Optional[ComponentStateModel] = Field(default=None, alias="state")
    type: Optional[Literal["BUILD", "TEST"]] = Field(default=None, alias="type")
    owner: Optional[str] = Field(default=None, alias="owner")
    description: Optional[str] = Field(default=None, alias="description")
    change_description: Optional[str] = Field(default=None, alias="changeDescription")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    publisher: Optional[str] = Field(default=None, alias="publisher")
    obfuscate: Optional[bool] = Field(default=None, alias="obfuscate")


class ComponentModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")
    description: Optional[str] = Field(default=None, alias="description")
    change_description: Optional[str] = Field(default=None, alias="changeDescription")
    type: Optional[Literal["BUILD", "TEST"]] = Field(default=None, alias="type")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    supported_os_versions: Optional[List[str]] = Field(
        default=None, alias="supportedOsVersions"
    )
    state: Optional[ComponentStateModel] = Field(default=None, alias="state")
    parameters: Optional[List[ComponentParameterDetailModel]] = Field(
        default=None, alias="parameters"
    )
    owner: Optional[str] = Field(default=None, alias="owner")
    data: Optional[str] = Field(default=None, alias="data")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    publisher: Optional[str] = Field(default=None, alias="publisher")
    obfuscate: Optional[bool] = Field(default=None, alias="obfuscate")


class ListComponentsResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    component_version_list: List[ComponentVersionModel] = Field(
        alias="componentVersionList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContainerDistributionConfigurationModel(BaseModel):
    target_repository: TargetContainerRepositoryModel = Field(alias="targetRepository")
    description: Optional[str] = Field(default=None, alias="description")
    container_tags: Optional[Sequence[str]] = Field(default=None, alias="containerTags")


class ListContainerRecipesResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    container_recipe_summary_list: List[ContainerRecipeSummaryModel] = Field(
        alias="containerRecipeSummaryList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageRequestModel(BaseModel):
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )
    client_token: str = Field(alias="clientToken")
    image_recipe_arn: Optional[str] = Field(default=None, alias="imageRecipeArn")
    container_recipe_arn: Optional[str] = Field(
        default=None, alias="containerRecipeArn"
    )
    distribution_configuration_arn: Optional[str] = Field(
        default=None, alias="distributionConfigurationArn"
    )
    image_tests_configuration: Optional[ImageTestsConfigurationModel] = Field(
        default=None, alias="imageTestsConfiguration"
    )
    enhanced_image_metadata_enabled: Optional[bool] = Field(
        default=None, alias="enhancedImageMetadataEnabled"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateImagePipelineRequestModel(BaseModel):
    name: str = Field(alias="name")
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    image_recipe_arn: Optional[str] = Field(default=None, alias="imageRecipeArn")
    container_recipe_arn: Optional[str] = Field(
        default=None, alias="containerRecipeArn"
    )
    distribution_configuration_arn: Optional[str] = Field(
        default=None, alias="distributionConfigurationArn"
    )
    image_tests_configuration: Optional[ImageTestsConfigurationModel] = Field(
        default=None, alias="imageTestsConfiguration"
    )
    enhanced_image_metadata_enabled: Optional[bool] = Field(
        default=None, alias="enhancedImageMetadataEnabled"
    )
    schedule: Optional[ScheduleModel] = Field(default=None, alias="schedule")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="status"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ImagePipelineModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    enhanced_image_metadata_enabled: Optional[bool] = Field(
        default=None, alias="enhancedImageMetadataEnabled"
    )
    image_recipe_arn: Optional[str] = Field(default=None, alias="imageRecipeArn")
    container_recipe_arn: Optional[str] = Field(
        default=None, alias="containerRecipeArn"
    )
    infrastructure_configuration_arn: Optional[str] = Field(
        default=None, alias="infrastructureConfigurationArn"
    )
    distribution_configuration_arn: Optional[str] = Field(
        default=None, alias="distributionConfigurationArn"
    )
    image_tests_configuration: Optional[ImageTestsConfigurationModel] = Field(
        default=None, alias="imageTestsConfiguration"
    )
    schedule: Optional[ScheduleModel] = Field(default=None, alias="schedule")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="status"
    )
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    date_updated: Optional[str] = Field(default=None, alias="dateUpdated")
    date_last_run: Optional[str] = Field(default=None, alias="dateLastRun")
    date_next_run: Optional[str] = Field(default=None, alias="dateNextRun")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateImagePipelineRequestModel(BaseModel):
    image_pipeline_arn: str = Field(alias="imagePipelineArn")
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    image_recipe_arn: Optional[str] = Field(default=None, alias="imageRecipeArn")
    container_recipe_arn: Optional[str] = Field(
        default=None, alias="containerRecipeArn"
    )
    distribution_configuration_arn: Optional[str] = Field(
        default=None, alias="distributionConfigurationArn"
    )
    image_tests_configuration: Optional[ImageTestsConfigurationModel] = Field(
        default=None, alias="imageTestsConfiguration"
    )
    enhanced_image_metadata_enabled: Optional[bool] = Field(
        default=None, alias="enhancedImageMetadataEnabled"
    )
    schedule: Optional[ScheduleModel] = Field(default=None, alias="schedule")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="status"
    )


class ListDistributionConfigurationsResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    distribution_configuration_summary_list: List[
        DistributionConfigurationSummaryModel
    ] = Field(alias="distributionConfigurationSummaryList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceBlockDeviceMappingModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="deviceName")
    ebs: Optional[EbsInstanceBlockDeviceSpecificationModel] = Field(
        default=None, alias="ebs"
    )
    virtual_name: Optional[str] = Field(default=None, alias="virtualName")
    no_device: Optional[str] = Field(default=None, alias="noDevice")


class FastLaunchConfigurationModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    snapshot_configuration: Optional[FastLaunchSnapshotConfigurationModel] = Field(
        default=None, alias="snapshotConfiguration"
    )
    max_parallel_launches: Optional[int] = Field(
        default=None, alias="maxParallelLaunches"
    )
    launch_template: Optional[FastLaunchLaunchTemplateSpecificationModel] = Field(
        default=None, alias="launchTemplate"
    )
    account_id: Optional[str] = Field(default=None, alias="accountId")


class ListComponentsRequestModel(BaseModel):
    owner: Optional[Literal["Amazon", "Self", "Shared", "ThirdParty"]] = Field(
        default=None, alias="owner"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    by_name: Optional[bool] = Field(default=None, alias="byName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListContainerRecipesRequestModel(BaseModel):
    owner: Optional[Literal["Amazon", "Self", "Shared", "ThirdParty"]] = Field(
        default=None, alias="owner"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDistributionConfigurationsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImageBuildVersionsRequestModel(BaseModel):
    image_version_arn: str = Field(alias="imageVersionArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImagePipelineImagesRequestModel(BaseModel):
    image_pipeline_arn: str = Field(alias="imagePipelineArn")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImagePipelinesRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImageRecipesRequestModel(BaseModel):
    owner: Optional[Literal["Amazon", "Self", "Shared", "ThirdParty"]] = Field(
        default=None, alias="owner"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImagesRequestModel(BaseModel):
    owner: Optional[Literal["Amazon", "Self", "Shared", "ThirdParty"]] = Field(
        default=None, alias="owner"
    )
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    by_name: Optional[bool] = Field(default=None, alias="byName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    include_deprecated: Optional[bool] = Field(default=None, alias="includeDeprecated")


class ListInfrastructureConfigurationsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImagePackagesResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_package_list: List[ImagePackageModel] = Field(alias="imagePackageList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImageRecipesResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_recipe_summary_list: List[ImageRecipeSummaryModel] = Field(
        alias="imageRecipeSummaryList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImagesResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_version_list: List[ImageVersionModel] = Field(alias="imageVersionList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInfrastructureConfigurationsResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    infrastructure_configuration_summary_list: List[
        InfrastructureConfigurationSummaryModel
    ] = Field(alias="infrastructureConfigurationSummaryList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoggingModel(BaseModel):
    s3_logs: Optional[S3LogsModel] = Field(default=None, alias="s3Logs")


class OutputResourcesModel(BaseModel):
    amis: Optional[List[AmiModel]] = Field(default=None, alias="amis")
    containers: Optional[List[ContainerModel]] = Field(default=None, alias="containers")


class ListComponentBuildVersionsResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    component_summary_list: List[ComponentSummaryModel] = Field(
        alias="componentSummaryList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    component: ComponentModel = Field(alias="component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImagePipelineResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_pipeline: ImagePipelineModel = Field(alias="imagePipeline")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImagePipelinesResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_pipeline_list: List[ImagePipelineModel] = Field(alias="imagePipelineList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageRecipeRequestModel(BaseModel):
    name: str = Field(alias="name")
    semantic_version: str = Field(alias="semanticVersion")
    components: Sequence[ComponentConfigurationModel] = Field(alias="components")
    parent_image: str = Field(alias="parentImage")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    block_device_mappings: Optional[Sequence[InstanceBlockDeviceMappingModel]] = Field(
        default=None, alias="blockDeviceMappings"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    working_directory: Optional[str] = Field(default=None, alias="workingDirectory")
    additional_instance_configuration: Optional[
        AdditionalInstanceConfigurationModel
    ] = Field(default=None, alias="additionalInstanceConfiguration")


class ImageRecipeModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    type: Optional[Literal["AMI", "DOCKER"]] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    owner: Optional[str] = Field(default=None, alias="owner")
    version: Optional[str] = Field(default=None, alias="version")
    components: Optional[List[ComponentConfigurationModel]] = Field(
        default=None, alias="components"
    )
    parent_image: Optional[str] = Field(default=None, alias="parentImage")
    block_device_mappings: Optional[List[InstanceBlockDeviceMappingModel]] = Field(
        default=None, alias="blockDeviceMappings"
    )
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    working_directory: Optional[str] = Field(default=None, alias="workingDirectory")
    additional_instance_configuration: Optional[
        AdditionalInstanceConfigurationModel
    ] = Field(default=None, alias="additionalInstanceConfiguration")


class InstanceConfigurationModel(BaseModel):
    image: Optional[str] = Field(default=None, alias="image")
    block_device_mappings: Optional[Sequence[InstanceBlockDeviceMappingModel]] = Field(
        default=None, alias="blockDeviceMappings"
    )


class DistributionModel(BaseModel):
    region: str = Field(alias="region")
    ami_distribution_configuration: Optional[AmiDistributionConfigurationModel] = Field(
        default=None, alias="amiDistributionConfiguration"
    )
    container_distribution_configuration: Optional[
        ContainerDistributionConfigurationModel
    ] = Field(default=None, alias="containerDistributionConfiguration")
    license_configuration_arns: Optional[Sequence[str]] = Field(
        default=None, alias="licenseConfigurationArns"
    )
    launch_template_configurations: Optional[
        Sequence[LaunchTemplateConfigurationModel]
    ] = Field(default=None, alias="launchTemplateConfigurations")
    s3_export_configuration: Optional[S3ExportConfigurationModel] = Field(
        default=None, alias="s3ExportConfiguration"
    )
    fast_launch_configurations: Optional[
        Sequence[FastLaunchConfigurationModel]
    ] = Field(default=None, alias="fastLaunchConfigurations")


class CreateInfrastructureConfigurationRequestModel(BaseModel):
    name: str = Field(alias="name")
    instance_profile_name: str = Field(alias="instanceProfileName")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    instance_types: Optional[Sequence[str]] = Field(default=None, alias="instanceTypes")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")
    logging: Optional[LoggingModel] = Field(default=None, alias="logging")
    key_pair: Optional[str] = Field(default=None, alias="keyPair")
    terminate_instance_on_failure: Optional[bool] = Field(
        default=None, alias="terminateInstanceOnFailure"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="snsTopicArn")
    resource_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="resourceTags"
    )
    instance_metadata_options: Optional[InstanceMetadataOptionsModel] = Field(
        default=None, alias="instanceMetadataOptions"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class InfrastructureConfigurationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    instance_types: Optional[List[str]] = Field(default=None, alias="instanceTypes")
    instance_profile_name: Optional[str] = Field(
        default=None, alias="instanceProfileName"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")
    logging: Optional[LoggingModel] = Field(default=None, alias="logging")
    key_pair: Optional[str] = Field(default=None, alias="keyPair")
    terminate_instance_on_failure: Optional[bool] = Field(
        default=None, alias="terminateInstanceOnFailure"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="snsTopicArn")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    date_updated: Optional[str] = Field(default=None, alias="dateUpdated")
    resource_tags: Optional[Dict[str, str]] = Field(default=None, alias="resourceTags")
    instance_metadata_options: Optional[InstanceMetadataOptionsModel] = Field(
        default=None, alias="instanceMetadataOptions"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateInfrastructureConfigurationRequestModel(BaseModel):
    infrastructure_configuration_arn: str = Field(
        alias="infrastructureConfigurationArn"
    )
    instance_profile_name: str = Field(alias="instanceProfileName")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    instance_types: Optional[Sequence[str]] = Field(default=None, alias="instanceTypes")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    subnet_id: Optional[str] = Field(default=None, alias="subnetId")
    logging: Optional[LoggingModel] = Field(default=None, alias="logging")
    key_pair: Optional[str] = Field(default=None, alias="keyPair")
    terminate_instance_on_failure: Optional[bool] = Field(
        default=None, alias="terminateInstanceOnFailure"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="snsTopicArn")
    resource_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="resourceTags"
    )
    instance_metadata_options: Optional[InstanceMetadataOptionsModel] = Field(
        default=None, alias="instanceMetadataOptions"
    )


class ImageSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["AMI", "DOCKER"]] = Field(default=None, alias="type")
    version: Optional[str] = Field(default=None, alias="version")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    os_version: Optional[str] = Field(default=None, alias="osVersion")
    state: Optional[ImageStateModel] = Field(default=None, alias="state")
    owner: Optional[str] = Field(default=None, alias="owner")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    output_resources: Optional[OutputResourcesModel] = Field(
        default=None, alias="outputResources"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    build_type: Optional[Literal["IMPORT", "SCHEDULED", "USER_INITIATED"]] = Field(
        default=None, alias="buildType"
    )
    image_source: Optional[
        Literal["AMAZON_MANAGED", "AWS_MARKETPLACE", "CUSTOM", "IMPORTED"]
    ] = Field(default=None, alias="imageSource")


class GetImageRecipeResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_recipe: ImageRecipeModel = Field(alias="imageRecipe")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContainerRecipeModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    container_type: Optional[Literal["DOCKER"]] = Field(
        default=None, alias="containerType"
    )
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    owner: Optional[str] = Field(default=None, alias="owner")
    version: Optional[str] = Field(default=None, alias="version")
    components: Optional[List[ComponentConfigurationModel]] = Field(
        default=None, alias="components"
    )
    instance_configuration: Optional[InstanceConfigurationModel] = Field(
        default=None, alias="instanceConfiguration"
    )
    dockerfile_template_data: Optional[str] = Field(
        default=None, alias="dockerfileTemplateData"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")
    encrypted: Optional[bool] = Field(default=None, alias="encrypted")
    parent_image: Optional[str] = Field(default=None, alias="parentImage")
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    working_directory: Optional[str] = Field(default=None, alias="workingDirectory")
    target_repository: Optional[TargetContainerRepositoryModel] = Field(
        default=None, alias="targetRepository"
    )


class CreateContainerRecipeRequestModel(BaseModel):
    container_type: Literal["DOCKER"] = Field(alias="containerType")
    name: str = Field(alias="name")
    semantic_version: str = Field(alias="semanticVersion")
    components: Sequence[ComponentConfigurationModel] = Field(alias="components")
    parent_image: str = Field(alias="parentImage")
    target_repository: TargetContainerRepositoryModel = Field(alias="targetRepository")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    instance_configuration: Optional[InstanceConfigurationModel] = Field(
        default=None, alias="instanceConfiguration"
    )
    dockerfile_template_data: Optional[str] = Field(
        default=None, alias="dockerfileTemplateData"
    )
    dockerfile_template_uri: Optional[str] = Field(
        default=None, alias="dockerfileTemplateUri"
    )
    platform_override: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platformOverride"
    )
    image_os_version_override: Optional[str] = Field(
        default=None, alias="imageOsVersionOverride"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    working_directory: Optional[str] = Field(default=None, alias="workingDirectory")
    kms_key_id: Optional[str] = Field(default=None, alias="kmsKeyId")


class CreateDistributionConfigurationRequestModel(BaseModel):
    name: str = Field(alias="name")
    distributions: Sequence[DistributionModel] = Field(alias="distributions")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DistributionConfigurationModel(BaseModel):
    timeout_minutes: int = Field(alias="timeoutMinutes")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    distributions: Optional[List[DistributionModel]] = Field(
        default=None, alias="distributions"
    )
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    date_updated: Optional[str] = Field(default=None, alias="dateUpdated")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateDistributionConfigurationRequestModel(BaseModel):
    distribution_configuration_arn: str = Field(alias="distributionConfigurationArn")
    distributions: Sequence[DistributionModel] = Field(alias="distributions")
    client_token: str = Field(alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")


class GetInfrastructureConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    infrastructure_configuration: InfrastructureConfigurationModel = Field(
        alias="infrastructureConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImageBuildVersionsResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_summary_list: List[ImageSummaryModel] = Field(alias="imageSummaryList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListImagePipelineImagesResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image_summary_list: List[ImageSummaryModel] = Field(alias="imageSummaryList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContainerRecipeResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    container_recipe: ContainerRecipeModel = Field(alias="containerRecipe")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDistributionConfigurationResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    distribution_configuration: DistributionConfigurationModel = Field(
        alias="distributionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImageModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    type: Optional[Literal["AMI", "DOCKER"]] = Field(default=None, alias="type")
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")
    platform: Optional[Literal["Linux", "Windows"]] = Field(
        default=None, alias="platform"
    )
    enhanced_image_metadata_enabled: Optional[bool] = Field(
        default=None, alias="enhancedImageMetadataEnabled"
    )
    os_version: Optional[str] = Field(default=None, alias="osVersion")
    state: Optional[ImageStateModel] = Field(default=None, alias="state")
    image_recipe: Optional[ImageRecipeModel] = Field(default=None, alias="imageRecipe")
    container_recipe: Optional[ContainerRecipeModel] = Field(
        default=None, alias="containerRecipe"
    )
    source_pipeline_name: Optional[str] = Field(
        default=None, alias="sourcePipelineName"
    )
    source_pipeline_arn: Optional[str] = Field(default=None, alias="sourcePipelineArn")
    infrastructure_configuration: Optional[InfrastructureConfigurationModel] = Field(
        default=None, alias="infrastructureConfiguration"
    )
    distribution_configuration: Optional[DistributionConfigurationModel] = Field(
        default=None, alias="distributionConfiguration"
    )
    image_tests_configuration: Optional[ImageTestsConfigurationModel] = Field(
        default=None, alias="imageTestsConfiguration"
    )
    date_created: Optional[str] = Field(default=None, alias="dateCreated")
    output_resources: Optional[OutputResourcesModel] = Field(
        default=None, alias="outputResources"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    build_type: Optional[Literal["IMPORT", "SCHEDULED", "USER_INITIATED"]] = Field(
        default=None, alias="buildType"
    )
    image_source: Optional[
        Literal["AMAZON_MANAGED", "AWS_MARKETPLACE", "CUSTOM", "IMPORTED"]
    ] = Field(default=None, alias="imageSource")


class GetImageResponseModel(BaseModel):
    request_id: str = Field(alias="requestId")
    image: ImageModel = Field(alias="image")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
