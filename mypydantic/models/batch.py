# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ArrayPropertiesDetailModel(BaseModel):
    status_summary: Optional[Dict[str, int]] = Field(
        default=None, alias="statusSummary"
    )
    size: Optional[int] = Field(default=None, alias="size")
    index: Optional[int] = Field(default=None, alias="index")


class ArrayPropertiesSummaryModel(BaseModel):
    size: Optional[int] = Field(default=None, alias="size")
    index: Optional[int] = Field(default=None, alias="index")


class ArrayPropertiesModel(BaseModel):
    size: Optional[int] = Field(default=None, alias="size")


class NetworkInterfaceModel(BaseModel):
    attachment_id: Optional[str] = Field(default=None, alias="attachmentId")
    ipv6_address: Optional[str] = Field(default=None, alias="ipv6Address")
    private_ipv4_address: Optional[str] = Field(
        default=None, alias="privateIpv4Address"
    )


class CancelJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    reason: str = Field(alias="reason")


class EksConfigurationModel(BaseModel):
    eks_cluster_arn: str = Field(alias="eksClusterArn")
    kubernetes_namespace: str = Field(alias="kubernetesNamespace")


class UpdatePolicyModel(BaseModel):
    terminate_jobs_on_update: Optional[bool] = Field(
        default=None, alias="terminateJobsOnUpdate"
    )
    job_execution_timeout_minutes: Optional[int] = Field(
        default=None, alias="jobExecutionTimeoutMinutes"
    )


class ComputeEnvironmentOrderModel(BaseModel):
    order: int = Field(alias="order")
    compute_environment: str = Field(alias="computeEnvironment")


class Ec2ConfigurationModel(BaseModel):
    image_type: str = Field(alias="imageType")
    image_id_override: Optional[str] = Field(default=None, alias="imageIdOverride")
    image_kubernetes_version: Optional[str] = Field(
        default=None, alias="imageKubernetesVersion"
    )


class LaunchTemplateSpecificationModel(BaseModel):
    launch_template_id: Optional[str] = Field(default=None, alias="launchTemplateId")
    launch_template_name: Optional[str] = Field(
        default=None, alias="launchTemplateName"
    )
    version: Optional[str] = Field(default=None, alias="version")


class FargatePlatformConfigurationModel(BaseModel):
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")


class KeyValuePairModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class MountPointModel(BaseModel):
    container_path: Optional[str] = Field(default=None, alias="containerPath")
    read_only: Optional[bool] = Field(default=None, alias="readOnly")
    source_volume: Optional[str] = Field(default=None, alias="sourceVolume")


class NetworkConfigurationModel(BaseModel):
    assign_public_ip: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="assignPublicIp"
    )


class ResourceRequirementModel(BaseModel):
    value: str = Field(alias="value")
    type: Literal["GPU", "MEMORY", "VCPU"] = Field(alias="type")


class SecretModel(BaseModel):
    name: str = Field(alias="name")
    value_from: str = Field(alias="valueFrom")


class UlimitModel(BaseModel):
    hard_limit: int = Field(alias="hardLimit")
    name: str = Field(alias="name")
    soft_limit: int = Field(alias="softLimit")


class ContainerSummaryModel(BaseModel):
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    reason: Optional[str] = Field(default=None, alias="reason")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteComputeEnvironmentRequestModel(BaseModel):
    compute_environment: str = Field(alias="computeEnvironment")


class DeleteJobQueueRequestModel(BaseModel):
    job_queue: str = Field(alias="jobQueue")


class DeleteSchedulingPolicyRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeregisterJobDefinitionRequestModel(BaseModel):
    job_definition: str = Field(alias="jobDefinition")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeComputeEnvironmentsRequestModel(BaseModel):
    compute_environments: Optional[Sequence[str]] = Field(
        default=None, alias="computeEnvironments"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeJobDefinitionsRequestModel(BaseModel):
    job_definitions: Optional[Sequence[str]] = Field(
        default=None, alias="jobDefinitions"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    job_definition_name: Optional[str] = Field(default=None, alias="jobDefinitionName")
    status: Optional[str] = Field(default=None, alias="status")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeJobQueuesRequestModel(BaseModel):
    job_queues: Optional[Sequence[str]] = Field(default=None, alias="jobQueues")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeJobsRequestModel(BaseModel):
    jobs: Sequence[str] = Field(alias="jobs")


class DescribeSchedulingPoliciesRequestModel(BaseModel):
    arns: Sequence[str] = Field(alias="arns")


class DeviceModel(BaseModel):
    host_path: str = Field(alias="hostPath")
    container_path: Optional[str] = Field(default=None, alias="containerPath")
    permissions: Optional[List[Literal["MKNOD", "READ", "WRITE"]]] = Field(
        default=None, alias="permissions"
    )


class EFSAuthorizationConfigModel(BaseModel):
    access_point_id: Optional[str] = Field(default=None, alias="accessPointId")
    iam: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="iam")


class EksAttemptContainerDetailModel(BaseModel):
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    reason: Optional[str] = Field(default=None, alias="reason")


class EksContainerEnvironmentVariableModel(BaseModel):
    name: str = Field(alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class EksContainerResourceRequirementsModel(BaseModel):
    limits: Optional[Dict[str, str]] = Field(default=None, alias="limits")
    requests: Optional[Dict[str, str]] = Field(default=None, alias="requests")


class EksContainerSecurityContextModel(BaseModel):
    run_as_user: Optional[int] = Field(default=None, alias="runAsUser")
    run_as_group: Optional[int] = Field(default=None, alias="runAsGroup")
    privileged: Optional[bool] = Field(default=None, alias="privileged")
    read_only_root_filesystem: Optional[bool] = Field(
        default=None, alias="readOnlyRootFilesystem"
    )
    run_as_non_root: Optional[bool] = Field(default=None, alias="runAsNonRoot")


class EksContainerVolumeMountModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    mount_path: Optional[str] = Field(default=None, alias="mountPath")
    read_only: Optional[bool] = Field(default=None, alias="readOnly")


class EksEmptyDirModel(BaseModel):
    medium: Optional[str] = Field(default=None, alias="medium")
    size_limit: Optional[str] = Field(default=None, alias="sizeLimit")


class EksHostPathModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="path")


class EksSecretModel(BaseModel):
    secret_name: str = Field(alias="secretName")
    optional: Optional[bool] = Field(default=None, alias="optional")


class EvaluateOnExitModel(BaseModel):
    action: Literal["EXIT", "RETRY"] = Field(alias="action")
    on_status_reason: Optional[str] = Field(default=None, alias="onStatusReason")
    on_reason: Optional[str] = Field(default=None, alias="onReason")
    on_exit_code: Optional[str] = Field(default=None, alias="onExitCode")


class ShareAttributesModel(BaseModel):
    share_identifier: str = Field(alias="shareIdentifier")
    weight_factor: Optional[float] = Field(default=None, alias="weightFactor")


class HostModel(BaseModel):
    source_path: Optional[str] = Field(default=None, alias="sourcePath")


class JobTimeoutModel(BaseModel):
    attempt_duration_seconds: Optional[int] = Field(
        default=None, alias="attemptDurationSeconds"
    )


class JobDependencyModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    type: Optional[Literal["N_TO_N", "SEQUENTIAL"]] = Field(default=None, alias="type")


class NodeDetailsModel(BaseModel):
    node_index: Optional[int] = Field(default=None, alias="nodeIndex")
    is_main_node: Optional[bool] = Field(default=None, alias="isMainNode")


class NodePropertiesSummaryModel(BaseModel):
    is_main_node: Optional[bool] = Field(default=None, alias="isMainNode")
    num_nodes: Optional[int] = Field(default=None, alias="numNodes")
    node_index: Optional[int] = Field(default=None, alias="nodeIndex")


class KeyValuesPairModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class TmpfsModel(BaseModel):
    container_path: str = Field(alias="containerPath")
    size: int = Field(alias="size")
    mount_options: Optional[List[str]] = Field(default=None, alias="mountOptions")


class ListSchedulingPoliciesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SchedulingPolicyListingDetailModel(BaseModel):
    arn: str = Field(alias="arn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TerminateJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    reason: str = Field(alias="reason")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class AttemptContainerDetailModel(BaseModel):
    container_instance_arn: Optional[str] = Field(
        default=None, alias="containerInstanceArn"
    )
    task_arn: Optional[str] = Field(default=None, alias="taskArn")
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    reason: Optional[str] = Field(default=None, alias="reason")
    log_stream_name: Optional[str] = Field(default=None, alias="logStreamName")
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )


class CreateJobQueueRequestModel(BaseModel):
    job_queue_name: str = Field(alias="jobQueueName")
    priority: int = Field(alias="priority")
    compute_environment_order: Sequence[ComputeEnvironmentOrderModel] = Field(
        alias="computeEnvironmentOrder"
    )
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="state")
    scheduling_policy_arn: Optional[str] = Field(
        default=None, alias="schedulingPolicyArn"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class JobQueueDetailModel(BaseModel):
    job_queue_name: str = Field(alias="jobQueueName")
    job_queue_arn: str = Field(alias="jobQueueArn")
    state: Literal["DISABLED", "ENABLED"] = Field(alias="state")
    priority: int = Field(alias="priority")
    compute_environment_order: List[ComputeEnvironmentOrderModel] = Field(
        alias="computeEnvironmentOrder"
    )
    scheduling_policy_arn: Optional[str] = Field(
        default=None, alias="schedulingPolicyArn"
    )
    status: Optional[
        Literal["CREATING", "DELETED", "DELETING", "INVALID", "UPDATING", "VALID"]
    ] = Field(default=None, alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateJobQueueRequestModel(BaseModel):
    job_queue: str = Field(alias="jobQueue")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="state")
    scheduling_policy_arn: Optional[str] = Field(
        default=None, alias="schedulingPolicyArn"
    )
    priority: Optional[int] = Field(default=None, alias="priority")
    compute_environment_order: Optional[Sequence[ComputeEnvironmentOrderModel]] = Field(
        default=None, alias="computeEnvironmentOrder"
    )


class ComputeResourceModel(BaseModel):
    type: Literal["EC2", "FARGATE", "FARGATE_SPOT", "SPOT"] = Field(alias="type")
    maxv_cpus: int = Field(alias="maxvCpus")
    subnets: Sequence[str] = Field(alias="subnets")
    allocation_strategy: Optional[
        Literal["BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"]
    ] = Field(default=None, alias="allocationStrategy")
    minv_cpus: Optional[int] = Field(default=None, alias="minvCpus")
    desiredv_cpus: Optional[int] = Field(default=None, alias="desiredvCpus")
    instance_types: Optional[Sequence[str]] = Field(default=None, alias="instanceTypes")
    image_id: Optional[str] = Field(default=None, alias="imageId")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    ec2_key_pair: Optional[str] = Field(default=None, alias="ec2KeyPair")
    instance_role: Optional[str] = Field(default=None, alias="instanceRole")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    placement_group: Optional[str] = Field(default=None, alias="placementGroup")
    bid_percentage: Optional[int] = Field(default=None, alias="bidPercentage")
    spot_iam_fleet_role: Optional[str] = Field(default=None, alias="spotIamFleetRole")
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="launchTemplate"
    )
    ec2_configuration: Optional[Sequence[Ec2ConfigurationModel]] = Field(
        default=None, alias="ec2Configuration"
    )


class ComputeResourceUpdateModel(BaseModel):
    minv_cpus: Optional[int] = Field(default=None, alias="minvCpus")
    maxv_cpus: Optional[int] = Field(default=None, alias="maxvCpus")
    desiredv_cpus: Optional[int] = Field(default=None, alias="desiredvCpus")
    subnets: Optional[Sequence[str]] = Field(default=None, alias="subnets")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    allocation_strategy: Optional[
        Literal["BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"]
    ] = Field(default=None, alias="allocationStrategy")
    instance_types: Optional[Sequence[str]] = Field(default=None, alias="instanceTypes")
    ec2_key_pair: Optional[str] = Field(default=None, alias="ec2KeyPair")
    instance_role: Optional[str] = Field(default=None, alias="instanceRole")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    placement_group: Optional[str] = Field(default=None, alias="placementGroup")
    bid_percentage: Optional[int] = Field(default=None, alias="bidPercentage")
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="launchTemplate"
    )
    ec2_configuration: Optional[Sequence[Ec2ConfigurationModel]] = Field(
        default=None, alias="ec2Configuration"
    )
    update_to_latest_image_version: Optional[bool] = Field(
        default=None, alias="updateToLatestImageVersion"
    )
    type: Optional[Literal["EC2", "FARGATE", "FARGATE_SPOT", "SPOT"]] = Field(
        default=None, alias="type"
    )
    image_id: Optional[str] = Field(default=None, alias="imageId")


class ContainerOverridesModel(BaseModel):
    vcpus: Optional[int] = Field(default=None, alias="vcpus")
    memory: Optional[int] = Field(default=None, alias="memory")
    command: Optional[Sequence[str]] = Field(default=None, alias="command")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    environment: Optional[Sequence[KeyValuePairModel]] = Field(
        default=None, alias="environment"
    )
    resource_requirements: Optional[Sequence[ResourceRequirementModel]] = Field(
        default=None, alias="resourceRequirements"
    )


class LogConfigurationModel(BaseModel):
    log_driver: Literal[
        "awslogs", "fluentd", "gelf", "journald", "json-file", "splunk", "syslog"
    ] = Field(alias="logDriver")
    options: Optional[Dict[str, str]] = Field(default=None, alias="options")
    secret_options: Optional[List[SecretModel]] = Field(
        default=None, alias="secretOptions"
    )


class CreateComputeEnvironmentResponseModel(BaseModel):
    compute_environment_name: str = Field(alias="computeEnvironmentName")
    compute_environment_arn: str = Field(alias="computeEnvironmentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobQueueResponseModel(BaseModel):
    job_queue_name: str = Field(alias="jobQueueName")
    job_queue_arn: str = Field(alias="jobQueueArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSchedulingPolicyResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterJobDefinitionResponseModel(BaseModel):
    job_definition_name: str = Field(alias="jobDefinitionName")
    job_definition_arn: str = Field(alias="jobDefinitionArn")
    revision: int = Field(alias="revision")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubmitJobResponseModel(BaseModel):
    job_arn: str = Field(alias="jobArn")
    job_name: str = Field(alias="jobName")
    job_id: str = Field(alias="jobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateComputeEnvironmentResponseModel(BaseModel):
    compute_environment_name: str = Field(alias="computeEnvironmentName")
    compute_environment_arn: str = Field(alias="computeEnvironmentArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobQueueResponseModel(BaseModel):
    job_queue_name: str = Field(alias="jobQueueName")
    job_queue_arn: str = Field(alias="jobQueueArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateModel(
    BaseModel
):
    compute_environments: Optional[Sequence[str]] = Field(
        default=None, alias="computeEnvironments"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateModel(BaseModel):
    job_definitions: Optional[Sequence[str]] = Field(
        default=None, alias="jobDefinitions"
    )
    job_definition_name: Optional[str] = Field(default=None, alias="jobDefinitionName")
    status: Optional[str] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeJobQueuesRequestDescribeJobQueuesPaginateModel(BaseModel):
    job_queues: Optional[Sequence[str]] = Field(default=None, alias="jobQueues")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class EFSVolumeConfigurationModel(BaseModel):
    file_system_id: str = Field(alias="fileSystemId")
    root_directory: Optional[str] = Field(default=None, alias="rootDirectory")
    transit_encryption: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="transitEncryption"
    )
    transit_encryption_port: Optional[int] = Field(
        default=None, alias="transitEncryptionPort"
    )
    authorization_config: Optional[EFSAuthorizationConfigModel] = Field(
        default=None, alias="authorizationConfig"
    )


class EksAttemptDetailModel(BaseModel):
    containers: Optional[List[EksAttemptContainerDetailModel]] = Field(
        default=None, alias="containers"
    )
    pod_name: Optional[str] = Field(default=None, alias="podName")
    node_name: Optional[str] = Field(default=None, alias="nodeName")
    started_at: Optional[int] = Field(default=None, alias="startedAt")
    stopped_at: Optional[int] = Field(default=None, alias="stoppedAt")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class EksContainerOverrideModel(BaseModel):
    image: Optional[str] = Field(default=None, alias="image")
    command: Optional[Sequence[str]] = Field(default=None, alias="command")
    args: Optional[Sequence[str]] = Field(default=None, alias="args")
    env: Optional[Sequence[EksContainerEnvironmentVariableModel]] = Field(
        default=None, alias="env"
    )
    resources: Optional[EksContainerResourceRequirementsModel] = Field(
        default=None, alias="resources"
    )


class EksContainerDetailModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    image: Optional[str] = Field(default=None, alias="image")
    image_pull_policy: Optional[str] = Field(default=None, alias="imagePullPolicy")
    command: Optional[List[str]] = Field(default=None, alias="command")
    args: Optional[List[str]] = Field(default=None, alias="args")
    env: Optional[List[EksContainerEnvironmentVariableModel]] = Field(
        default=None, alias="env"
    )
    resources: Optional[EksContainerResourceRequirementsModel] = Field(
        default=None, alias="resources"
    )
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    reason: Optional[str] = Field(default=None, alias="reason")
    volume_mounts: Optional[List[EksContainerVolumeMountModel]] = Field(
        default=None, alias="volumeMounts"
    )
    security_context: Optional[EksContainerSecurityContextModel] = Field(
        default=None, alias="securityContext"
    )


class EksContainerModel(BaseModel):
    image: str = Field(alias="image")
    name: Optional[str] = Field(default=None, alias="name")
    image_pull_policy: Optional[str] = Field(default=None, alias="imagePullPolicy")
    command: Optional[List[str]] = Field(default=None, alias="command")
    args: Optional[List[str]] = Field(default=None, alias="args")
    env: Optional[List[EksContainerEnvironmentVariableModel]] = Field(
        default=None, alias="env"
    )
    resources: Optional[EksContainerResourceRequirementsModel] = Field(
        default=None, alias="resources"
    )
    volume_mounts: Optional[List[EksContainerVolumeMountModel]] = Field(
        default=None, alias="volumeMounts"
    )
    security_context: Optional[EksContainerSecurityContextModel] = Field(
        default=None, alias="securityContext"
    )


class EksVolumeModel(BaseModel):
    name: str = Field(alias="name")
    host_path: Optional[EksHostPathModel] = Field(default=None, alias="hostPath")
    empty_dir: Optional[EksEmptyDirModel] = Field(default=None, alias="emptyDir")
    secret: Optional[EksSecretModel] = Field(default=None, alias="secret")


class RetryStrategyModel(BaseModel):
    attempts: Optional[int] = Field(default=None, alias="attempts")
    evaluate_on_exit: Optional[List[EvaluateOnExitModel]] = Field(
        default=None, alias="evaluateOnExit"
    )


class FairsharePolicyModel(BaseModel):
    share_decay_seconds: Optional[int] = Field(default=None, alias="shareDecaySeconds")
    compute_reservation: Optional[int] = Field(default=None, alias="computeReservation")
    share_distribution: Optional[Sequence[ShareAttributesModel]] = Field(
        default=None, alias="shareDistribution"
    )


class JobSummaryModel(BaseModel):
    job_id: str = Field(alias="jobId")
    job_name: str = Field(alias="jobName")
    job_arn: Optional[str] = Field(default=None, alias="jobArn")
    created_at: Optional[int] = Field(default=None, alias="createdAt")
    status: Optional[
        Literal[
            "FAILED",
            "PENDING",
            "RUNNABLE",
            "RUNNING",
            "STARTING",
            "SUBMITTED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    started_at: Optional[int] = Field(default=None, alias="startedAt")
    stopped_at: Optional[int] = Field(default=None, alias="stoppedAt")
    container: Optional[ContainerSummaryModel] = Field(default=None, alias="container")
    array_properties: Optional[ArrayPropertiesSummaryModel] = Field(
        default=None, alias="arrayProperties"
    )
    node_properties: Optional[NodePropertiesSummaryModel] = Field(
        default=None, alias="nodeProperties"
    )
    job_definition: Optional[str] = Field(default=None, alias="jobDefinition")


class ListJobsRequestListJobsPaginateModel(BaseModel):
    job_queue: Optional[str] = Field(default=None, alias="jobQueue")
    array_job_id: Optional[str] = Field(default=None, alias="arrayJobId")
    multi_node_job_id: Optional[str] = Field(default=None, alias="multiNodeJobId")
    job_status: Optional[
        Literal[
            "FAILED",
            "PENDING",
            "RUNNABLE",
            "RUNNING",
            "STARTING",
            "SUBMITTED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="jobStatus")
    filters: Optional[Sequence[KeyValuesPairModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestModel(BaseModel):
    job_queue: Optional[str] = Field(default=None, alias="jobQueue")
    array_job_id: Optional[str] = Field(default=None, alias="arrayJobId")
    multi_node_job_id: Optional[str] = Field(default=None, alias="multiNodeJobId")
    job_status: Optional[
        Literal[
            "FAILED",
            "PENDING",
            "RUNNABLE",
            "RUNNING",
            "STARTING",
            "SUBMITTED",
            "SUCCEEDED",
        ]
    ] = Field(default=None, alias="jobStatus")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    filters: Optional[Sequence[KeyValuesPairModel]] = Field(
        default=None, alias="filters"
    )


class LinuxParametersModel(BaseModel):
    devices: Optional[List[DeviceModel]] = Field(default=None, alias="devices")
    init_process_enabled: Optional[bool] = Field(
        default=None, alias="initProcessEnabled"
    )
    shared_memory_size: Optional[int] = Field(default=None, alias="sharedMemorySize")
    tmpfs: Optional[List[TmpfsModel]] = Field(default=None, alias="tmpfs")
    max_swap: Optional[int] = Field(default=None, alias="maxSwap")
    swappiness: Optional[int] = Field(default=None, alias="swappiness")


class ListSchedulingPoliciesResponseModel(BaseModel):
    scheduling_policies: List[SchedulingPolicyListingDetailModel] = Field(
        alias="schedulingPolicies"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttemptDetailModel(BaseModel):
    container: Optional[AttemptContainerDetailModel] = Field(
        default=None, alias="container"
    )
    started_at: Optional[int] = Field(default=None, alias="startedAt")
    stopped_at: Optional[int] = Field(default=None, alias="stoppedAt")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")


class DescribeJobQueuesResponseModel(BaseModel):
    job_queues: List[JobQueueDetailModel] = Field(alias="jobQueues")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComputeEnvironmentDetailModel(BaseModel):
    compute_environment_name: str = Field(alias="computeEnvironmentName")
    compute_environment_arn: str = Field(alias="computeEnvironmentArn")
    unmanagedv_cpus: Optional[int] = Field(default=None, alias="unmanagedvCpus")
    ecs_cluster_arn: Optional[str] = Field(default=None, alias="ecsClusterArn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    type: Optional[Literal["MANAGED", "UNMANAGED"]] = Field(default=None, alias="type")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="state")
    status: Optional[
        Literal["CREATING", "DELETED", "DELETING", "INVALID", "UPDATING", "VALID"]
    ] = Field(default=None, alias="status")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    compute_resources: Optional[ComputeResourceModel] = Field(
        default=None, alias="computeResources"
    )
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    update_policy: Optional[UpdatePolicyModel] = Field(
        default=None, alias="updatePolicy"
    )
    eks_configuration: Optional[EksConfigurationModel] = Field(
        default=None, alias="eksConfiguration"
    )
    container_orchestration_type: Optional[Literal["ECS", "EKS"]] = Field(
        default=None, alias="containerOrchestrationType"
    )
    uuid: Optional[str] = Field(default=None, alias="uuid")


class CreateComputeEnvironmentRequestModel(BaseModel):
    compute_environment_name: str = Field(alias="computeEnvironmentName")
    type: Literal["MANAGED", "UNMANAGED"] = Field(alias="type")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="state")
    unmanagedv_cpus: Optional[int] = Field(default=None, alias="unmanagedvCpus")
    compute_resources: Optional[ComputeResourceModel] = Field(
        default=None, alias="computeResources"
    )
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    eks_configuration: Optional[EksConfigurationModel] = Field(
        default=None, alias="eksConfiguration"
    )


class UpdateComputeEnvironmentRequestModel(BaseModel):
    compute_environment: str = Field(alias="computeEnvironment")
    state: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="state")
    unmanagedv_cpus: Optional[int] = Field(default=None, alias="unmanagedvCpus")
    compute_resources: Optional[ComputeResourceUpdateModel] = Field(
        default=None, alias="computeResources"
    )
    service_role: Optional[str] = Field(default=None, alias="serviceRole")
    update_policy: Optional[UpdatePolicyModel] = Field(
        default=None, alias="updatePolicy"
    )


class NodePropertyOverrideModel(BaseModel):
    target_nodes: str = Field(alias="targetNodes")
    container_overrides: Optional[ContainerOverridesModel] = Field(
        default=None, alias="containerOverrides"
    )


class VolumeModel(BaseModel):
    host: Optional[HostModel] = Field(default=None, alias="host")
    name: Optional[str] = Field(default=None, alias="name")
    efs_volume_configuration: Optional[EFSVolumeConfigurationModel] = Field(
        default=None, alias="efsVolumeConfiguration"
    )


class EksPodPropertiesOverrideModel(BaseModel):
    containers: Optional[Sequence[EksContainerOverrideModel]] = Field(
        default=None, alias="containers"
    )


class EksPodPropertiesDetailModel(BaseModel):
    service_account_name: Optional[str] = Field(
        default=None, alias="serviceAccountName"
    )
    host_network: Optional[bool] = Field(default=None, alias="hostNetwork")
    dns_policy: Optional[str] = Field(default=None, alias="dnsPolicy")
    containers: Optional[List[EksContainerDetailModel]] = Field(
        default=None, alias="containers"
    )
    volumes: Optional[List[EksVolumeModel]] = Field(default=None, alias="volumes")
    pod_name: Optional[str] = Field(default=None, alias="podName")
    node_name: Optional[str] = Field(default=None, alias="nodeName")


class EksPodPropertiesModel(BaseModel):
    service_account_name: Optional[str] = Field(
        default=None, alias="serviceAccountName"
    )
    host_network: Optional[bool] = Field(default=None, alias="hostNetwork")
    dns_policy: Optional[str] = Field(default=None, alias="dnsPolicy")
    containers: Optional[List[EksContainerModel]] = Field(
        default=None, alias="containers"
    )
    volumes: Optional[List[EksVolumeModel]] = Field(default=None, alias="volumes")


class CreateSchedulingPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    fairshare_policy: Optional[FairsharePolicyModel] = Field(
        default=None, alias="fairsharePolicy"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class SchedulingPolicyDetailModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    fairshare_policy: Optional[FairsharePolicyModel] = Field(
        default=None, alias="fairsharePolicy"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateSchedulingPolicyRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    fairshare_policy: Optional[FairsharePolicyModel] = Field(
        default=None, alias="fairsharePolicy"
    )


class ListJobsResponseModel(BaseModel):
    job_summary_list: List[JobSummaryModel] = Field(alias="jobSummaryList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComputeEnvironmentsResponseModel(BaseModel):
    compute_environments: List[ComputeEnvironmentDetailModel] = Field(
        alias="computeEnvironments"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NodeOverridesModel(BaseModel):
    num_nodes: Optional[int] = Field(default=None, alias="numNodes")
    node_property_overrides: Optional[Sequence[NodePropertyOverrideModel]] = Field(
        default=None, alias="nodePropertyOverrides"
    )


class ContainerDetailModel(BaseModel):
    image: Optional[str] = Field(default=None, alias="image")
    vcpus: Optional[int] = Field(default=None, alias="vcpus")
    memory: Optional[int] = Field(default=None, alias="memory")
    command: Optional[List[str]] = Field(default=None, alias="command")
    job_role_arn: Optional[str] = Field(default=None, alias="jobRoleArn")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    volumes: Optional[List[VolumeModel]] = Field(default=None, alias="volumes")
    environment: Optional[List[KeyValuePairModel]] = Field(
        default=None, alias="environment"
    )
    mount_points: Optional[List[MountPointModel]] = Field(
        default=None, alias="mountPoints"
    )
    readonly_root_filesystem: Optional[bool] = Field(
        default=None, alias="readonlyRootFilesystem"
    )
    ulimits: Optional[List[UlimitModel]] = Field(default=None, alias="ulimits")
    privileged: Optional[bool] = Field(default=None, alias="privileged")
    user: Optional[str] = Field(default=None, alias="user")
    exit_code: Optional[int] = Field(default=None, alias="exitCode")
    reason: Optional[str] = Field(default=None, alias="reason")
    container_instance_arn: Optional[str] = Field(
        default=None, alias="containerInstanceArn"
    )
    task_arn: Optional[str] = Field(default=None, alias="taskArn")
    log_stream_name: Optional[str] = Field(default=None, alias="logStreamName")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )
    resource_requirements: Optional[List[ResourceRequirementModel]] = Field(
        default=None, alias="resourceRequirements"
    )
    linux_parameters: Optional[LinuxParametersModel] = Field(
        default=None, alias="linuxParameters"
    )
    log_configuration: Optional[LogConfigurationModel] = Field(
        default=None, alias="logConfiguration"
    )
    secrets: Optional[List[SecretModel]] = Field(default=None, alias="secrets")
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    fargate_platform_configuration: Optional[FargatePlatformConfigurationModel] = Field(
        default=None, alias="fargatePlatformConfiguration"
    )


class ContainerPropertiesModel(BaseModel):
    image: Optional[str] = Field(default=None, alias="image")
    vcpus: Optional[int] = Field(default=None, alias="vcpus")
    memory: Optional[int] = Field(default=None, alias="memory")
    command: Optional[List[str]] = Field(default=None, alias="command")
    job_role_arn: Optional[str] = Field(default=None, alias="jobRoleArn")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    volumes: Optional[List[VolumeModel]] = Field(default=None, alias="volumes")
    environment: Optional[List[KeyValuePairModel]] = Field(
        default=None, alias="environment"
    )
    mount_points: Optional[List[MountPointModel]] = Field(
        default=None, alias="mountPoints"
    )
    readonly_root_filesystem: Optional[bool] = Field(
        default=None, alias="readonlyRootFilesystem"
    )
    privileged: Optional[bool] = Field(default=None, alias="privileged")
    ulimits: Optional[List[UlimitModel]] = Field(default=None, alias="ulimits")
    user: Optional[str] = Field(default=None, alias="user")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    resource_requirements: Optional[List[ResourceRequirementModel]] = Field(
        default=None, alias="resourceRequirements"
    )
    linux_parameters: Optional[LinuxParametersModel] = Field(
        default=None, alias="linuxParameters"
    )
    log_configuration: Optional[LogConfigurationModel] = Field(
        default=None, alias="logConfiguration"
    )
    secrets: Optional[List[SecretModel]] = Field(default=None, alias="secrets")
    network_configuration: Optional[NetworkConfigurationModel] = Field(
        default=None, alias="networkConfiguration"
    )
    fargate_platform_configuration: Optional[FargatePlatformConfigurationModel] = Field(
        default=None, alias="fargatePlatformConfiguration"
    )


class EksPropertiesOverrideModel(BaseModel):
    pod_properties: Optional[EksPodPropertiesOverrideModel] = Field(
        default=None, alias="podProperties"
    )


class EksPropertiesDetailModel(BaseModel):
    pod_properties: Optional[EksPodPropertiesDetailModel] = Field(
        default=None, alias="podProperties"
    )


class EksPropertiesModel(BaseModel):
    pod_properties: Optional[EksPodPropertiesModel] = Field(
        default=None, alias="podProperties"
    )


class DescribeSchedulingPoliciesResponseModel(BaseModel):
    scheduling_policies: List[SchedulingPolicyDetailModel] = Field(
        alias="schedulingPolicies"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NodeRangePropertyModel(BaseModel):
    target_nodes: str = Field(alias="targetNodes")
    container: Optional[ContainerPropertiesModel] = Field(
        default=None, alias="container"
    )


class SubmitJobRequestModel(BaseModel):
    job_name: str = Field(alias="jobName")
    job_queue: str = Field(alias="jobQueue")
    job_definition: str = Field(alias="jobDefinition")
    share_identifier: Optional[str] = Field(default=None, alias="shareIdentifier")
    scheduling_priority_override: Optional[int] = Field(
        default=None, alias="schedulingPriorityOverride"
    )
    array_properties: Optional[ArrayPropertiesModel] = Field(
        default=None, alias="arrayProperties"
    )
    depends_on: Optional[Sequence[JobDependencyModel]] = Field(
        default=None, alias="dependsOn"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")
    container_overrides: Optional[ContainerOverridesModel] = Field(
        default=None, alias="containerOverrides"
    )
    node_overrides: Optional[NodeOverridesModel] = Field(
        default=None, alias="nodeOverrides"
    )
    retry_strategy: Optional[RetryStrategyModel] = Field(
        default=None, alias="retryStrategy"
    )
    propagate_tags: Optional[bool] = Field(default=None, alias="propagateTags")
    timeout: Optional[JobTimeoutModel] = Field(default=None, alias="timeout")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    eks_properties_override: Optional[EksPropertiesOverrideModel] = Field(
        default=None, alias="eksPropertiesOverride"
    )


class NodePropertiesModel(BaseModel):
    num_nodes: int = Field(alias="numNodes")
    main_node: int = Field(alias="mainNode")
    node_range_properties: List[NodeRangePropertyModel] = Field(
        alias="nodeRangeProperties"
    )


class JobDefinitionModel(BaseModel):
    job_definition_name: str = Field(alias="jobDefinitionName")
    job_definition_arn: str = Field(alias="jobDefinitionArn")
    revision: int = Field(alias="revision")
    type: str = Field(alias="type")
    status: Optional[str] = Field(default=None, alias="status")
    scheduling_priority: Optional[int] = Field(default=None, alias="schedulingPriority")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="parameters")
    retry_strategy: Optional[RetryStrategyModel] = Field(
        default=None, alias="retryStrategy"
    )
    container_properties: Optional[ContainerPropertiesModel] = Field(
        default=None, alias="containerProperties"
    )
    timeout: Optional[JobTimeoutModel] = Field(default=None, alias="timeout")
    node_properties: Optional[NodePropertiesModel] = Field(
        default=None, alias="nodeProperties"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    propagate_tags: Optional[bool] = Field(default=None, alias="propagateTags")
    platform_capabilities: Optional[List[Literal["EC2", "FARGATE"]]] = Field(
        default=None, alias="platformCapabilities"
    )
    eks_properties: Optional[EksPropertiesModel] = Field(
        default=None, alias="eksProperties"
    )
    container_orchestration_type: Optional[Literal["ECS", "EKS"]] = Field(
        default=None, alias="containerOrchestrationType"
    )


class JobDetailModel(BaseModel):
    job_name: str = Field(alias="jobName")
    job_id: str = Field(alias="jobId")
    job_queue: str = Field(alias="jobQueue")
    status: Literal[
        "FAILED", "PENDING", "RUNNABLE", "RUNNING", "STARTING", "SUBMITTED", "SUCCEEDED"
    ] = Field(alias="status")
    started_at: int = Field(alias="startedAt")
    job_definition: str = Field(alias="jobDefinition")
    job_arn: Optional[str] = Field(default=None, alias="jobArn")
    share_identifier: Optional[str] = Field(default=None, alias="shareIdentifier")
    scheduling_priority: Optional[int] = Field(default=None, alias="schedulingPriority")
    attempts: Optional[List[AttemptDetailModel]] = Field(default=None, alias="attempts")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    created_at: Optional[int] = Field(default=None, alias="createdAt")
    retry_strategy: Optional[RetryStrategyModel] = Field(
        default=None, alias="retryStrategy"
    )
    stopped_at: Optional[int] = Field(default=None, alias="stoppedAt")
    depends_on: Optional[List[JobDependencyModel]] = Field(
        default=None, alias="dependsOn"
    )
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="parameters")
    container: Optional[ContainerDetailModel] = Field(default=None, alias="container")
    node_details: Optional[NodeDetailsModel] = Field(default=None, alias="nodeDetails")
    node_properties: Optional[NodePropertiesModel] = Field(
        default=None, alias="nodeProperties"
    )
    array_properties: Optional[ArrayPropertiesDetailModel] = Field(
        default=None, alias="arrayProperties"
    )
    timeout: Optional[JobTimeoutModel] = Field(default=None, alias="timeout")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    propagate_tags: Optional[bool] = Field(default=None, alias="propagateTags")
    platform_capabilities: Optional[List[Literal["EC2", "FARGATE"]]] = Field(
        default=None, alias="platformCapabilities"
    )
    eks_properties: Optional[EksPropertiesDetailModel] = Field(
        default=None, alias="eksProperties"
    )
    eks_attempts: Optional[List[EksAttemptDetailModel]] = Field(
        default=None, alias="eksAttempts"
    )
    is_cancelled: Optional[bool] = Field(default=None, alias="isCancelled")
    is_terminated: Optional[bool] = Field(default=None, alias="isTerminated")


class RegisterJobDefinitionRequestModel(BaseModel):
    job_definition_name: str = Field(alias="jobDefinitionName")
    type: Literal["container", "multinode"] = Field(alias="type")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")
    scheduling_priority: Optional[int] = Field(default=None, alias="schedulingPriority")
    container_properties: Optional[ContainerPropertiesModel] = Field(
        default=None, alias="containerProperties"
    )
    node_properties: Optional[NodePropertiesModel] = Field(
        default=None, alias="nodeProperties"
    )
    retry_strategy: Optional[RetryStrategyModel] = Field(
        default=None, alias="retryStrategy"
    )
    propagate_tags: Optional[bool] = Field(default=None, alias="propagateTags")
    timeout: Optional[JobTimeoutModel] = Field(default=None, alias="timeout")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    platform_capabilities: Optional[Sequence[Literal["EC2", "FARGATE"]]] = Field(
        default=None, alias="platformCapabilities"
    )
    eks_properties: Optional[EksPropertiesModel] = Field(
        default=None, alias="eksProperties"
    )


class DescribeJobDefinitionsResponseModel(BaseModel):
    job_definitions: List[JobDefinitionModel] = Field(alias="jobDefinitions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeJobsResponseModel(BaseModel):
    jobs: List[JobDetailModel] = Field(alias="jobs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
