# Model Generated: Thu Mar  2 21:56:19 2023

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


class AssociateClientDeviceWithCoreDeviceEntryModel(BaseModel):
    thing_name: str = Field(alias="thingName")


class AssociateClientDeviceWithCoreDeviceErrorEntryModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class AssociateServiceRoleToAccountRequestModel(BaseModel):
    role_arn: str = Field(alias="roleArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociatedClientDeviceModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    association_timestamp: Optional[datetime] = Field(
        default=None, alias="associationTimestamp"
    )


class DisassociateClientDeviceFromCoreDeviceEntryModel(BaseModel):
    thing_name: str = Field(alias="thingName")


class DisassociateClientDeviceFromCoreDeviceErrorEntryModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class CancelDeploymentRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")


class CloudComponentStatusModel(BaseModel):
    component_state: Optional[
        Literal["DEPLOYABLE", "DEPRECATED", "FAILED", "INITIATED", "REQUESTED"]
    ] = Field(default=None, alias="componentState")
    message: Optional[str] = Field(default=None, alias="message")
    errors: Optional[Dict[str, str]] = Field(default=None, alias="errors")
    vendor_guidance: Optional[Literal["ACTIVE", "DELETED", "DISCONTINUED"]] = Field(
        default=None, alias="vendorGuidance"
    )
    vendor_guidance_message: Optional[str] = Field(
        default=None, alias="vendorGuidanceMessage"
    )


class ComponentCandidateModel(BaseModel):
    component_name: Optional[str] = Field(default=None, alias="componentName")
    component_version: Optional[str] = Field(default=None, alias="componentVersion")
    version_requirements: Optional[Mapping[str, str]] = Field(
        default=None, alias="versionRequirements"
    )


class ComponentConfigurationUpdateModel(BaseModel):
    merge: Optional[str] = Field(default=None, alias="merge")
    reset: Optional[Sequence[str]] = Field(default=None, alias="reset")


class ComponentDependencyRequirementModel(BaseModel):
    version_requirement: Optional[str] = Field(default=None, alias="versionRequirement")
    dependency_type: Optional[Literal["HARD", "SOFT"]] = Field(
        default=None, alias="dependencyType"
    )


class ComponentPlatformModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")


class SystemResourceLimitsModel(BaseModel):
    memory: Optional[int] = Field(default=None, alias="memory")
    cpus: Optional[float] = Field(default=None, alias="cpus")


class ComponentVersionListItemModel(BaseModel):
    component_name: Optional[str] = Field(default=None, alias="componentName")
    component_version: Optional[str] = Field(default=None, alias="componentVersion")
    arn: Optional[str] = Field(default=None, alias="arn")


class ConnectivityInfoModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    host_address: Optional[str] = Field(default=None, alias="hostAddress")
    port_number: Optional[int] = Field(default=None, alias="portNumber")
    metadata: Optional[str] = Field(default=None, alias="metadata")


class CoreDeviceModel(BaseModel):
    core_device_thing_name: Optional[str] = Field(
        default=None, alias="coreDeviceThingName"
    )
    status: Optional[Literal["HEALTHY", "UNHEALTHY"]] = Field(
        default=None, alias="status"
    )
    last_status_update_timestamp: Optional[datetime] = Field(
        default=None, alias="lastStatusUpdateTimestamp"
    )


class DeleteComponentRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteCoreDeviceRequestModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")


class DeleteDeploymentRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")


class DeploymentComponentUpdatePolicyModel(BaseModel):
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")
    action: Optional[Literal["NOTIFY_COMPONENTS", "SKIP_NOTIFY_COMPONENTS"]] = Field(
        default=None, alias="action"
    )


class DeploymentConfigurationValidationPolicyModel(BaseModel):
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")


class IoTJobTimeoutConfigModel(BaseModel):
    in_progress_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="inProgressTimeoutInMinutes"
    )


class DeploymentModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    revision_id: Optional[str] = Field(default=None, alias="revisionId")
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    deployment_name: Optional[str] = Field(default=None, alias="deploymentName")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="creationTimestamp"
    )
    deployment_status: Optional[
        Literal["ACTIVE", "CANCELED", "COMPLETED", "FAILED", "INACTIVE"]
    ] = Field(default=None, alias="deploymentStatus")
    is_latest_for_target: Optional[bool] = Field(
        default=None, alias="isLatestForTarget"
    )
    parent_target_arn: Optional[str] = Field(default=None, alias="parentTargetArn")


class DescribeComponentRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class EffectiveDeploymentStatusDetailsModel(BaseModel):
    error_stack: Optional[List[str]] = Field(default=None, alias="errorStack")
    error_types: Optional[List[str]] = Field(default=None, alias="errorTypes")


class GetComponentRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    recipe_output_format: Optional[Literal["JSON", "YAML"]] = Field(
        default=None, alias="recipeOutputFormat"
    )


class GetComponentVersionArtifactRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    artifact_name: str = Field(alias="artifactName")


class GetConnectivityInfoRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")


class GetCoreDeviceRequestModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")


class GetDeploymentRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")


class InstalledComponentModel(BaseModel):
    component_name: Optional[str] = Field(default=None, alias="componentName")
    component_version: Optional[str] = Field(default=None, alias="componentVersion")
    lifecycle_state: Optional[
        Literal[
            "BROKEN",
            "ERRORED",
            "FINISHED",
            "INSTALLED",
            "NEW",
            "RUNNING",
            "STARTING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="lifecycleState")
    lifecycle_state_details: Optional[str] = Field(
        default=None, alias="lifecycleStateDetails"
    )
    is_root: Optional[bool] = Field(default=None, alias="isRoot")
    last_status_change_timestamp: Optional[datetime] = Field(
        default=None, alias="lastStatusChangeTimestamp"
    )
    last_reported_timestamp: Optional[datetime] = Field(
        default=None, alias="lastReportedTimestamp"
    )
    last_installation_source: Optional[str] = Field(
        default=None, alias="lastInstallationSource"
    )
    lifecycle_status_codes: Optional[List[str]] = Field(
        default=None, alias="lifecycleStatusCodes"
    )


class IoTJobAbortCriteriaModel(BaseModel):
    failure_type: Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"] = Field(
        alias="failureType"
    )
    action: Literal["CANCEL"] = Field(alias="action")
    threshold_percentage: float = Field(alias="thresholdPercentage")
    min_number_of_executed_things: int = Field(alias="minNumberOfExecutedThings")


class IoTJobRateIncreaseCriteriaModel(BaseModel):
    number_of_notified_things: Optional[int] = Field(
        default=None, alias="numberOfNotifiedThings"
    )
    number_of_succeeded_things: Optional[int] = Field(
        default=None, alias="numberOfSucceededThings"
    )


class LambdaDeviceMountModel(BaseModel):
    path: str = Field(alias="path")
    permission: Optional[Literal["ro", "rw"]] = Field(default=None, alias="permission")
    add_group_owner: Optional[bool] = Field(default=None, alias="addGroupOwner")


class LambdaVolumeMountModel(BaseModel):
    source_path: str = Field(alias="sourcePath")
    destination_path: str = Field(alias="destinationPath")
    permission: Optional[Literal["ro", "rw"]] = Field(default=None, alias="permission")
    add_group_owner: Optional[bool] = Field(default=None, alias="addGroupOwner")


class LambdaEventSourceModel(BaseModel):
    topic: str = Field(alias="topic")
    type: Literal["IOT_CORE", "PUB_SUB"] = Field(alias="type")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListClientDevicesAssociatedWithCoreDeviceRequestModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListComponentVersionsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListComponentsRequestModel(BaseModel):
    scope: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(default=None, alias="scope")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListCoreDevicesRequestModel(BaseModel):
    thing_group_arn: Optional[str] = Field(default=None, alias="thingGroupArn")
    status: Optional[Literal["HEALTHY", "UNHEALTHY"]] = Field(
        default=None, alias="status"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDeploymentsRequestModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    history_filter: Optional[Literal["ALL", "LATEST_ONLY"]] = Field(
        default=None, alias="historyFilter"
    )
    parent_target_arn: Optional[str] = Field(default=None, alias="parentTargetArn")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEffectiveDeploymentsRequestModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListInstalledComponentsRequestModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    topology_filter: Optional[Literal["ALL", "ROOT"]] = Field(
        default=None, alias="topologyFilter"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ResolvedComponentVersionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    component_name: Optional[str] = Field(default=None, alias="componentName")
    component_version: Optional[str] = Field(default=None, alias="componentVersion")
    recipe: Optional[bytes] = Field(default=None, alias="recipe")
    vendor_guidance: Optional[Literal["ACTIVE", "DELETED", "DISCONTINUED"]] = Field(
        default=None, alias="vendorGuidance"
    )
    message: Optional[str] = Field(default=None, alias="message")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class BatchAssociateClientDeviceWithCoreDeviceRequestModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    entries: Optional[Sequence[AssociateClientDeviceWithCoreDeviceEntryModel]] = Field(
        default=None, alias="entries"
    )


class AssociateServiceRoleToAccountResponseModel(BaseModel):
    associated_at: str = Field(alias="associatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchAssociateClientDeviceWithCoreDeviceResponseModel(BaseModel):
    error_entries: List[AssociateClientDeviceWithCoreDeviceErrorEntryModel] = Field(
        alias="errorEntries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelDeploymentResponseModel(BaseModel):
    message: str = Field(alias="message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentResponseModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    iot_job_id: str = Field(alias="iotJobId")
    iot_job_arn: str = Field(alias="iotJobArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateServiceRoleFromAccountResponseModel(BaseModel):
    disassociated_at: str = Field(alias="disassociatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentResponseModel(BaseModel):
    recipe_output_format: Literal["JSON", "YAML"] = Field(alias="recipeOutputFormat")
    recipe: bytes = Field(alias="recipe")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentVersionArtifactResponseModel(BaseModel):
    pre_signed_url: str = Field(alias="preSignedUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCoreDeviceResponseModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    core_version: str = Field(alias="coreVersion")
    platform: str = Field(alias="platform")
    architecture: str = Field(alias="architecture")
    status: Literal["HEALTHY", "UNHEALTHY"] = Field(alias="status")
    last_status_update_timestamp: datetime = Field(alias="lastStatusUpdateTimestamp")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceRoleForAccountResponseModel(BaseModel):
    associated_at: str = Field(alias="associatedAt")
    role_arn: str = Field(alias="roleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectivityInfoResponseModel(BaseModel):
    version: str = Field(alias="version")
    message: str = Field(alias="message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClientDevicesAssociatedWithCoreDeviceResponseModel(BaseModel):
    associated_client_devices: List[AssociatedClientDeviceModel] = Field(
        alias="associatedClientDevices"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateClientDeviceFromCoreDeviceRequestModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    entries: Optional[
        Sequence[DisassociateClientDeviceFromCoreDeviceEntryModel]
    ] = Field(default=None, alias="entries")


class BatchDisassociateClientDeviceFromCoreDeviceResponseModel(BaseModel):
    error_entries: List[DisassociateClientDeviceFromCoreDeviceErrorEntryModel] = Field(
        alias="errorEntries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateComponentVersionResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    component_name: str = Field(alias="componentName")
    component_version: str = Field(alias="componentVersion")
    creation_timestamp: datetime = Field(alias="creationTimestamp")
    status: CloudComponentStatusModel = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComponentLatestVersionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    component_version: Optional[str] = Field(default=None, alias="componentVersion")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="creationTimestamp"
    )
    description: Optional[str] = Field(default=None, alias="description")
    publisher: Optional[str] = Field(default=None, alias="publisher")
    platforms: Optional[List[ComponentPlatformModel]] = Field(
        default=None, alias="platforms"
    )


class DescribeComponentResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    component_name: str = Field(alias="componentName")
    component_version: str = Field(alias="componentVersion")
    creation_timestamp: datetime = Field(alias="creationTimestamp")
    publisher: str = Field(alias="publisher")
    description: str = Field(alias="description")
    status: CloudComponentStatusModel = Field(alias="status")
    platforms: List[ComponentPlatformModel] = Field(alias="platforms")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResolveComponentCandidatesRequestModel(BaseModel):
    platform: Optional[ComponentPlatformModel] = Field(default=None, alias="platform")
    component_candidates: Optional[Sequence[ComponentCandidateModel]] = Field(
        default=None, alias="componentCandidates"
    )


class ComponentRunWithModel(BaseModel):
    posix_user: Optional[str] = Field(default=None, alias="posixUser")
    system_resource_limits: Optional[SystemResourceLimitsModel] = Field(
        default=None, alias="systemResourceLimits"
    )
    windows_user: Optional[str] = Field(default=None, alias="windowsUser")


class ListComponentVersionsResponseModel(BaseModel):
    component_versions: List[ComponentVersionListItemModel] = Field(
        alias="componentVersions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectivityInfoResponseModel(BaseModel):
    connectivity_info: List[ConnectivityInfoModel] = Field(alias="connectivityInfo")
    message: str = Field(alias="message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectivityInfoRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    connectivity_info: Sequence[ConnectivityInfoModel] = Field(alias="connectivityInfo")


class ListCoreDevicesResponseModel(BaseModel):
    core_devices: List[CoreDeviceModel] = Field(alias="coreDevices")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentPoliciesModel(BaseModel):
    failure_handling_policy: Optional[Literal["DO_NOTHING", "ROLLBACK"]] = Field(
        default=None, alias="failureHandlingPolicy"
    )
    component_update_policy: Optional[DeploymentComponentUpdatePolicyModel] = Field(
        default=None, alias="componentUpdatePolicy"
    )
    configuration_validation_policy: Optional[
        DeploymentConfigurationValidationPolicyModel
    ] = Field(default=None, alias="configurationValidationPolicy")


class ListDeploymentsResponseModel(BaseModel):
    deployments: List[DeploymentModel] = Field(alias="deployments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EffectiveDeploymentModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    deployment_name: str = Field(alias="deploymentName")
    target_arn: str = Field(alias="targetArn")
    core_device_execution_status: Literal[
        "CANCELED",
        "COMPLETED",
        "FAILED",
        "IN_PROGRESS",
        "QUEUED",
        "REJECTED",
        "TIMED_OUT",
    ] = Field(alias="coreDeviceExecutionStatus")
    creation_timestamp: datetime = Field(alias="creationTimestamp")
    modified_timestamp: datetime = Field(alias="modifiedTimestamp")
    iot_job_id: Optional[str] = Field(default=None, alias="iotJobId")
    iot_job_arn: Optional[str] = Field(default=None, alias="iotJobArn")
    description: Optional[str] = Field(default=None, alias="description")
    reason: Optional[str] = Field(default=None, alias="reason")
    status_details: Optional[EffectiveDeploymentStatusDetailsModel] = Field(
        default=None, alias="statusDetails"
    )


class ListInstalledComponentsResponseModel(BaseModel):
    installed_components: List[InstalledComponentModel] = Field(
        alias="installedComponents"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IoTJobAbortConfigModel(BaseModel):
    criteria_list: Sequence[IoTJobAbortCriteriaModel] = Field(alias="criteriaList")


class IoTJobExponentialRolloutRateModel(BaseModel):
    base_rate_per_minute: int = Field(alias="baseRatePerMinute")
    increment_factor: float = Field(alias="incrementFactor")
    rate_increase_criteria: IoTJobRateIncreaseCriteriaModel = Field(
        alias="rateIncreaseCriteria"
    )


class LambdaContainerParamsModel(BaseModel):
    memory_size_in_kb: Optional[int] = Field(default=None, alias="memorySizeInKB")
    mount_rosysfs: Optional[bool] = Field(default=None, alias="mountROSysfs")
    volumes: Optional[Sequence[LambdaVolumeMountModel]] = Field(
        default=None, alias="volumes"
    )
    devices: Optional[Sequence[LambdaDeviceMountModel]] = Field(
        default=None, alias="devices"
    )


class ListClientDevicesAssociatedWithCoreDeviceRequestListClientDevicesAssociatedWithCoreDevicePaginateModel(
    BaseModel
):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComponentVersionsRequestListComponentVersionsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComponentsRequestListComponentsPaginateModel(BaseModel):
    scope: Optional[Literal["PRIVATE", "PUBLIC"]] = Field(default=None, alias="scope")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCoreDevicesRequestListCoreDevicesPaginateModel(BaseModel):
    thing_group_arn: Optional[str] = Field(default=None, alias="thingGroupArn")
    status: Optional[Literal["HEALTHY", "UNHEALTHY"]] = Field(
        default=None, alias="status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentsRequestListDeploymentsPaginateModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    history_filter: Optional[Literal["ALL", "LATEST_ONLY"]] = Field(
        default=None, alias="historyFilter"
    )
    parent_target_arn: Optional[str] = Field(default=None, alias="parentTargetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEffectiveDeploymentsRequestListEffectiveDeploymentsPaginateModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstalledComponentsRequestListInstalledComponentsPaginateModel(BaseModel):
    core_device_thing_name: str = Field(alias="coreDeviceThingName")
    topology_filter: Optional[Literal["ALL", "ROOT"]] = Field(
        default=None, alias="topologyFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ResolveComponentCandidatesResponseModel(BaseModel):
    resolved_component_versions: List[ResolvedComponentVersionModel] = Field(
        alias="resolvedComponentVersions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComponentModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    component_name: Optional[str] = Field(default=None, alias="componentName")
    latest_version: Optional[ComponentLatestVersionModel] = Field(
        default=None, alias="latestVersion"
    )


class ComponentDeploymentSpecificationModel(BaseModel):
    component_version: Optional[str] = Field(default=None, alias="componentVersion")
    configuration_update: Optional[ComponentConfigurationUpdateModel] = Field(
        default=None, alias="configurationUpdate"
    )
    run_with: Optional[ComponentRunWithModel] = Field(default=None, alias="runWith")


class ListEffectiveDeploymentsResponseModel(BaseModel):
    effective_deployments: List[EffectiveDeploymentModel] = Field(
        alias="effectiveDeployments"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IoTJobExecutionsRolloutConfigModel(BaseModel):
    exponential_rate: Optional[IoTJobExponentialRolloutRateModel] = Field(
        default=None, alias="exponentialRate"
    )
    maximum_per_minute: Optional[int] = Field(default=None, alias="maximumPerMinute")


class LambdaLinuxProcessParamsModel(BaseModel):
    isolation_mode: Optional[Literal["GreengrassContainer", "NoContainer"]] = Field(
        default=None, alias="isolationMode"
    )
    container_params: Optional[LambdaContainerParamsModel] = Field(
        default=None, alias="containerParams"
    )


class ListComponentsResponseModel(BaseModel):
    components: List[ComponentModel] = Field(alias="components")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentIoTJobConfigurationModel(BaseModel):
    job_executions_rollout_config: Optional[IoTJobExecutionsRolloutConfigModel] = Field(
        default=None, alias="jobExecutionsRolloutConfig"
    )
    abort_config: Optional[IoTJobAbortConfigModel] = Field(
        default=None, alias="abortConfig"
    )
    timeout_config: Optional[IoTJobTimeoutConfigModel] = Field(
        default=None, alias="timeoutConfig"
    )


class LambdaExecutionParametersModel(BaseModel):
    event_sources: Optional[Sequence[LambdaEventSourceModel]] = Field(
        default=None, alias="eventSources"
    )
    max_queue_size: Optional[int] = Field(default=None, alias="maxQueueSize")
    max_instances_count: Optional[int] = Field(default=None, alias="maxInstancesCount")
    max_idle_time_in_seconds: Optional[int] = Field(
        default=None, alias="maxIdleTimeInSeconds"
    )
    timeout_in_seconds: Optional[int] = Field(default=None, alias="timeoutInSeconds")
    status_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="statusTimeoutInSeconds"
    )
    pinned: Optional[bool] = Field(default=None, alias="pinned")
    input_payload_encoding_type: Optional[Literal["binary", "json"]] = Field(
        default=None, alias="inputPayloadEncodingType"
    )
    exec_args: Optional[Sequence[str]] = Field(default=None, alias="execArgs")
    environment_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="environmentVariables"
    )
    linux_process_params: Optional[LambdaLinuxProcessParamsModel] = Field(
        default=None, alias="linuxProcessParams"
    )


class CreateDeploymentRequestModel(BaseModel):
    target_arn: str = Field(alias="targetArn")
    deployment_name: Optional[str] = Field(default=None, alias="deploymentName")
    components: Optional[Mapping[str, ComponentDeploymentSpecificationModel]] = Field(
        default=None, alias="components"
    )
    iot_job_configuration: Optional[DeploymentIoTJobConfigurationModel] = Field(
        default=None, alias="iotJobConfiguration"
    )
    deployment_policies: Optional[DeploymentPoliciesModel] = Field(
        default=None, alias="deploymentPolicies"
    )
    parent_target_arn: Optional[str] = Field(default=None, alias="parentTargetArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GetDeploymentResponseModel(BaseModel):
    target_arn: str = Field(alias="targetArn")
    revision_id: str = Field(alias="revisionId")
    deployment_id: str = Field(alias="deploymentId")
    deployment_name: str = Field(alias="deploymentName")
    deployment_status: Literal[
        "ACTIVE", "CANCELED", "COMPLETED", "FAILED", "INACTIVE"
    ] = Field(alias="deploymentStatus")
    iot_job_id: str = Field(alias="iotJobId")
    iot_job_arn: str = Field(alias="iotJobArn")
    components: Dict[str, ComponentDeploymentSpecificationModel] = Field(
        alias="components"
    )
    deployment_policies: DeploymentPoliciesModel = Field(alias="deploymentPolicies")
    iot_job_configuration: DeploymentIoTJobConfigurationModel = Field(
        alias="iotJobConfiguration"
    )
    creation_timestamp: datetime = Field(alias="creationTimestamp")
    is_latest_for_target: bool = Field(alias="isLatestForTarget")
    parent_target_arn: str = Field(alias="parentTargetArn")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LambdaFunctionRecipeSourceModel(BaseModel):
    lambda_arn: str = Field(alias="lambdaArn")
    component_name: Optional[str] = Field(default=None, alias="componentName")
    component_version: Optional[str] = Field(default=None, alias="componentVersion")
    component_platforms: Optional[Sequence[ComponentPlatformModel]] = Field(
        default=None, alias="componentPlatforms"
    )
    component_dependencies: Optional[
        Mapping[str, ComponentDependencyRequirementModel]
    ] = Field(default=None, alias="componentDependencies")
    component_lambda_parameters: Optional[LambdaExecutionParametersModel] = Field(
        default=None, alias="componentLambdaParameters"
    )


class CreateComponentVersionRequestModel(BaseModel):
    inline_recipe: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="inlineRecipe")
    lambda_function: Optional[LambdaFunctionRecipeSourceModel] = Field(
        default=None, alias="lambdaFunction"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
