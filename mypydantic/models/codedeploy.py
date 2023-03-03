# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AlarmModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")


class AppSpecContentModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="content")
    sha256: Optional[str] = Field(default=None, alias="sha256")


class ApplicationInfoModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="applicationId")
    application_name: Optional[str] = Field(default=None, alias="applicationName")
    create_time: Optional[datetime] = Field(default=None, alias="createTime")
    linked_to_git_hub: Optional[bool] = Field(default=None, alias="linkedToGitHub")
    git_hub_account_name: Optional[str] = Field(default=None, alias="gitHubAccountName")
    compute_platform: Optional[Literal["ECS", "Lambda", "Server"]] = Field(
        default=None, alias="computePlatform"
    )


class AutoRollbackConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    events: Optional[
        List[
            Literal[
                "DEPLOYMENT_FAILURE",
                "DEPLOYMENT_STOP_ON_ALARM",
                "DEPLOYMENT_STOP_ON_REQUEST",
            ]
        ]
    ] = Field(default=None, alias="events")


class AutoScalingGroupModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    hook: Optional[str] = Field(default=None, alias="hook")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchGetApplicationsInputRequestModel(BaseModel):
    application_names: Sequence[str] = Field(alias="applicationNames")


class BatchGetDeploymentGroupsInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    deployment_group_names: Sequence[str] = Field(alias="deploymentGroupNames")


class BatchGetDeploymentInstancesInputRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    instance_ids: Sequence[str] = Field(alias="instanceIds")


class BatchGetDeploymentTargetsInputRequestModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    target_ids: Optional[Sequence[str]] = Field(default=None, alias="targetIds")


class BatchGetDeploymentsInputRequestModel(BaseModel):
    deployment_ids: Sequence[str] = Field(alias="deploymentIds")


class BatchGetOnPremisesInstancesInputRequestModel(BaseModel):
    instance_names: Sequence[str] = Field(alias="instanceNames")


class BlueInstanceTerminationOptionModel(BaseModel):
    action: Optional[Literal["KEEP_ALIVE", "TERMINATE"]] = Field(
        default=None, alias="action"
    )
    termination_wait_time_in_minutes: Optional[int] = Field(
        default=None, alias="terminationWaitTimeInMinutes"
    )


class DeploymentReadyOptionModel(BaseModel):
    action_on_timeout: Optional[
        Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"]
    ] = Field(default=None, alias="actionOnTimeout")
    wait_time_in_minutes: Optional[int] = Field(default=None, alias="waitTimeInMinutes")


class GreenFleetProvisioningOptionModel(BaseModel):
    action: Optional[Literal["COPY_AUTO_SCALING_GROUP", "DISCOVER_EXISTING"]] = Field(
        default=None, alias="action"
    )


class ContinueDeploymentInputRequestModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    deployment_wait_type: Optional[Literal["READY_WAIT", "TERMINATION_WAIT"]] = Field(
        default=None, alias="deploymentWaitType"
    )


class MinimumHealthyHostsModel(BaseModel):
    type: Optional[Literal["FLEET_PERCENT", "HOST_COUNT"]] = Field(
        default=None, alias="type"
    )
    value: Optional[int] = Field(default=None, alias="value")


class DeploymentStyleModel(BaseModel):
    deployment_type: Optional[Literal["BLUE_GREEN", "IN_PLACE"]] = Field(
        default=None, alias="deploymentType"
    )
    deployment_option: Optional[
        Literal["WITHOUT_TRAFFIC_CONTROL", "WITH_TRAFFIC_CONTROL"]
    ] = Field(default=None, alias="deploymentOption")


class EC2TagFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    type: Optional[Literal["KEY_AND_VALUE", "KEY_ONLY", "VALUE_ONLY"]] = Field(
        default=None, alias="Type"
    )


class ECSServiceModel(BaseModel):
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    cluster_name: Optional[str] = Field(default=None, alias="clusterName")


class TagFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    type: Optional[Literal["KEY_AND_VALUE", "KEY_ONLY", "VALUE_ONLY"]] = Field(
        default=None, alias="Type"
    )


class TriggerConfigModel(BaseModel):
    trigger_name: Optional[str] = Field(default=None, alias="triggerName")
    trigger_target_arn: Optional[str] = Field(default=None, alias="triggerTargetArn")
    trigger_events: Optional[
        List[
            Literal[
                "DeploymentFailure",
                "DeploymentReady",
                "DeploymentRollback",
                "DeploymentStart",
                "DeploymentStop",
                "DeploymentSuccess",
                "InstanceFailure",
                "InstanceReady",
                "InstanceStart",
                "InstanceSuccess",
            ]
        ]
    ] = Field(default=None, alias="triggerEvents")


class DeleteApplicationInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")


class DeleteDeploymentConfigInputRequestModel(BaseModel):
    deployment_config_name: str = Field(alias="deploymentConfigName")


class DeleteDeploymentGroupInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    deployment_group_name: str = Field(alias="deploymentGroupName")


class DeleteGitHubAccountTokenInputRequestModel(BaseModel):
    token_name: Optional[str] = Field(default=None, alias="tokenName")


class DeleteResourcesByExternalIdInputRequestModel(BaseModel):
    external_id: Optional[str] = Field(default=None, alias="externalId")


class LastDeploymentInfoModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    status: Optional[
        Literal[
            "Baking",
            "Created",
            "Failed",
            "InProgress",
            "Queued",
            "Ready",
            "Stopped",
            "Succeeded",
        ]
    ] = Field(default=None, alias="status")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    create_time: Optional[datetime] = Field(default=None, alias="createTime")


class DeploymentOverviewModel(BaseModel):
    pending: Optional[int] = Field(default=None, alias="Pending")
    in_progress: Optional[int] = Field(default=None, alias="InProgress")
    succeeded: Optional[int] = Field(default=None, alias="Succeeded")
    failed: Optional[int] = Field(default=None, alias="Failed")
    skipped: Optional[int] = Field(default=None, alias="Skipped")
    ready: Optional[int] = Field(default=None, alias="Ready")


class ErrorInformationModel(BaseModel):
    code: Optional[
        Literal[
            "AGENT_ISSUE",
            "ALARM_ACTIVE",
            "APPLICATION_MISSING",
            "AUTOSCALING_VALIDATION_ERROR",
            "AUTO_SCALING_CONFIGURATION",
            "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
            "CLOUDFORMATION_STACK_FAILURE",
            "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
            "CUSTOMER_APPLICATION_UNHEALTHY",
            "DEPLOYMENT_GROUP_MISSING",
            "ECS_UPDATE_ERROR",
            "ELASTIC_LOAD_BALANCING_INVALID",
            "ELB_INVALID_INSTANCE",
            "HEALTH_CONSTRAINTS",
            "HEALTH_CONSTRAINTS_INVALID",
            "HOOK_EXECUTION_FAILURE",
            "IAM_ROLE_MISSING",
            "IAM_ROLE_PERMISSIONS",
            "INTERNAL_ERROR",
            "INVALID_ECS_SERVICE",
            "INVALID_LAMBDA_CONFIGURATION",
            "INVALID_LAMBDA_FUNCTION",
            "INVALID_REVISION",
            "MANUAL_STOP",
            "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
            "MISSING_ELB_INFORMATION",
            "MISSING_GITHUB_TOKEN",
            "NO_EC2_SUBSCRIPTION",
            "NO_INSTANCES",
            "OVER_MAX_INSTANCES",
            "RESOURCE_LIMIT_EXCEEDED",
            "REVISION_MISSING",
            "THROTTLED",
            "TIMEOUT",
        ]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class RelatedDeploymentsModel(BaseModel):
    auto_update_outdated_instances_root_deployment_id: Optional[str] = Field(
        default=None, alias="autoUpdateOutdatedInstancesRootDeploymentId"
    )
    auto_update_outdated_instances_deployment_ids: Optional[List[str]] = Field(
        default=None, alias="autoUpdateOutdatedInstancesDeploymentIds"
    )


class RollbackInfoModel(BaseModel):
    rollback_deployment_id: Optional[str] = Field(
        default=None, alias="rollbackDeploymentId"
    )
    rollback_triggering_deployment_id: Optional[str] = Field(
        default=None, alias="rollbackTriggeringDeploymentId"
    )
    rollback_message: Optional[str] = Field(default=None, alias="rollbackMessage")


class DeregisterOnPremisesInstanceInputRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class DiagnosticsModel(BaseModel):
    error_code: Optional[
        Literal[
            "ScriptFailed",
            "ScriptMissing",
            "ScriptNotExecutable",
            "ScriptTimedOut",
            "Success",
            "UnknownError",
        ]
    ] = Field(default=None, alias="errorCode")
    script_name: Optional[str] = Field(default=None, alias="scriptName")
    message: Optional[str] = Field(default=None, alias="message")
    log_tail: Optional[str] = Field(default=None, alias="logTail")


class TargetGroupInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")


class ELBInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")


class GenericRevisionInfoModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    deployment_groups: Optional[List[str]] = Field(
        default=None, alias="deploymentGroups"
    )
    first_used_time: Optional[datetime] = Field(default=None, alias="firstUsedTime")
    last_used_time: Optional[datetime] = Field(default=None, alias="lastUsedTime")
    register_time: Optional[datetime] = Field(default=None, alias="registerTime")


class GetApplicationInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")


class GetDeploymentConfigInputRequestModel(BaseModel):
    deployment_config_name: str = Field(alias="deploymentConfigName")


class GetDeploymentGroupInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    deployment_group_name: str = Field(alias="deploymentGroupName")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetDeploymentInputRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")


class GetDeploymentInstanceInputRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    instance_id: str = Field(alias="instanceId")


class GetDeploymentTargetInputRequestModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    target_id: Optional[str] = Field(default=None, alias="targetId")


class GetOnPremisesInstanceInputRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class GitHubLocationModel(BaseModel):
    repository: Optional[str] = Field(default=None, alias="repository")
    commit_id: Optional[str] = Field(default=None, alias="commitId")


class LambdaFunctionInfoModel(BaseModel):
    function_name: Optional[str] = Field(default=None, alias="functionName")
    function_alias: Optional[str] = Field(default=None, alias="functionAlias")
    current_version: Optional[str] = Field(default=None, alias="currentVersion")
    target_version: Optional[str] = Field(default=None, alias="targetVersion")
    target_version_weight: Optional[float] = Field(
        default=None, alias="targetVersionWeight"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationRevisionsInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    sort_by: Optional[Literal["firstUsedTime", "lastUsedTime", "registerTime"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ascending", "descending"]] = Field(
        default=None, alias="sortOrder"
    )
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3_key_prefix: Optional[str] = Field(default=None, alias="s3KeyPrefix")
    deployed: Optional[Literal["exclude", "ignore", "include"]] = Field(
        default=None, alias="deployed"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListApplicationsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDeploymentConfigsInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDeploymentGroupsInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDeploymentInstancesInputRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    instance_status_filter: Optional[
        Sequence[
            Literal[
                "Failed",
                "InProgress",
                "Pending",
                "Ready",
                "Skipped",
                "Succeeded",
                "Unknown",
            ]
        ]
    ] = Field(default=None, alias="instanceStatusFilter")
    instance_type_filter: Optional[Sequence[Literal["Blue", "Green"]]] = Field(
        default=None, alias="instanceTypeFilter"
    )


class ListDeploymentTargetsInputRequestModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    target_filters: Optional[
        Mapping[Literal["ServerInstanceLabel", "TargetStatus"], Sequence[str]]
    ] = Field(default=None, alias="targetFilters")


class TimeRangeModel(BaseModel):
    start: Optional[Union[datetime, str]] = Field(default=None, alias="start")
    end: Optional[Union[datetime, str]] = Field(default=None, alias="end")


class ListGitHubAccountTokenNamesInputRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PutLifecycleEventHookExecutionStatusInputRequestModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    lifecycle_event_hook_execution_id: Optional[str] = Field(
        default=None, alias="lifecycleEventHookExecutionId"
    )
    status: Optional[
        Literal["Failed", "InProgress", "Pending", "Skipped", "Succeeded", "Unknown"]
    ] = Field(default=None, alias="status")


class RawStringModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="content")
    sha256: Optional[str] = Field(default=None, alias="sha256")


class RegisterOnPremisesInstanceInputRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")
    iam_session_arn: Optional[str] = Field(default=None, alias="iamSessionArn")
    iam_user_arn: Optional[str] = Field(default=None, alias="iamUserArn")


class S3LocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key: Optional[str] = Field(default=None, alias="key")
    bundle_type: Optional[Literal["JSON", "YAML", "tar", "tgz", "zip"]] = Field(
        default=None, alias="bundleType"
    )
    version: Optional[str] = Field(default=None, alias="version")
    etag: Optional[str] = Field(default=None, alias="eTag")


class SkipWaitTimeForInstanceTerminationInputRequestModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")


class StopDeploymentInputRequestModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    auto_rollback_enabled: Optional[bool] = Field(
        default=None, alias="autoRollbackEnabled"
    )


class TrafficRouteModel(BaseModel):
    listener_arns: Optional[List[str]] = Field(default=None, alias="listenerArns")


class TimeBasedCanaryModel(BaseModel):
    canary_percentage: Optional[int] = Field(default=None, alias="canaryPercentage")
    canary_interval: Optional[int] = Field(default=None, alias="canaryInterval")


class TimeBasedLinearModel(BaseModel):
    linear_percentage: Optional[int] = Field(default=None, alias="linearPercentage")
    linear_interval: Optional[int] = Field(default=None, alias="linearInterval")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateApplicationInputRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="applicationName")
    new_application_name: Optional[str] = Field(
        default=None, alias="newApplicationName"
    )


class AddTagsToOnPremisesInstancesInputRequestModel(BaseModel):
    tags: Sequence[TagModel] = Field(alias="tags")
    instance_names: Sequence[str] = Field(alias="instanceNames")


class CreateApplicationInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    compute_platform: Optional[Literal["ECS", "Lambda", "Server"]] = Field(
        default=None, alias="computePlatform"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class InstanceInfoModel(BaseModel):
    instance_name: Optional[str] = Field(default=None, alias="instanceName")
    iam_session_arn: Optional[str] = Field(default=None, alias="iamSessionArn")
    iam_user_arn: Optional[str] = Field(default=None, alias="iamUserArn")
    instance_arn: Optional[str] = Field(default=None, alias="instanceArn")
    register_time: Optional[datetime] = Field(default=None, alias="registerTime")
    deregister_time: Optional[datetime] = Field(default=None, alias="deregisterTime")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class RemoveTagsFromOnPremisesInstancesInputRequestModel(BaseModel):
    tags: Sequence[TagModel] = Field(alias="tags")
    instance_names: Sequence[str] = Field(alias="instanceNames")


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class AlarmConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    ignore_poll_alarm_failure: Optional[bool] = Field(
        default=None, alias="ignorePollAlarmFailure"
    )
    alarms: Optional[List[AlarmModel]] = Field(default=None, alias="alarms")


class BatchGetApplicationsOutputModel(BaseModel):
    applications_info: List[ApplicationInfoModel] = Field(alias="applicationsInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationOutputModel(BaseModel):
    application_id: str = Field(alias="applicationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentConfigOutputModel(BaseModel):
    deployment_config_id: str = Field(alias="deploymentConfigId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentGroupOutputModel(BaseModel):
    deployment_group_id: str = Field(alias="deploymentGroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentOutputModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDeploymentGroupOutputModel(BaseModel):
    hooks_not_cleaned_up: List[AutoScalingGroupModel] = Field(alias="hooksNotCleanedUp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGitHubAccountTokenOutputModel(BaseModel):
    token_name: str = Field(alias="tokenName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationOutputModel(BaseModel):
    application: ApplicationInfoModel = Field(alias="application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationsOutputModel(BaseModel):
    applications: List[str] = Field(alias="applications")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentConfigsOutputModel(BaseModel):
    deployment_configs_list: List[str] = Field(alias="deploymentConfigsList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentGroupsOutputModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    deployment_groups: List[str] = Field(alias="deploymentGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentInstancesOutputModel(BaseModel):
    instances_list: List[str] = Field(alias="instancesList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentTargetsOutputModel(BaseModel):
    target_ids: List[str] = Field(alias="targetIds")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentsOutputModel(BaseModel):
    deployments: List[str] = Field(alias="deployments")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGitHubAccountTokenNamesOutputModel(BaseModel):
    token_name_list: List[str] = Field(alias="tokenNameList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOnPremisesInstancesOutputModel(BaseModel):
    instance_names: List[str] = Field(alias="instanceNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLifecycleEventHookExecutionStatusOutputModel(BaseModel):
    lifecycle_event_hook_execution_id: str = Field(
        alias="lifecycleEventHookExecutionId"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDeploymentOutputModel(BaseModel):
    status: Literal["Pending", "Succeeded"] = Field(alias="status")
    status_message: str = Field(alias="statusMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDeploymentGroupOutputModel(BaseModel):
    hooks_not_cleaned_up: List[AutoScalingGroupModel] = Field(alias="hooksNotCleanedUp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BlueGreenDeploymentConfigurationModel(BaseModel):
    terminate_blue_instances_on_deployment_success: Optional[
        BlueInstanceTerminationOptionModel
    ] = Field(default=None, alias="terminateBlueInstancesOnDeploymentSuccess")
    deployment_ready_option: Optional[DeploymentReadyOptionModel] = Field(
        default=None, alias="deploymentReadyOption"
    )
    green_fleet_provisioning_option: Optional[
        GreenFleetProvisioningOptionModel
    ] = Field(default=None, alias="greenFleetProvisioningOption")


class EC2TagSetModel(BaseModel):
    ec2_tag_set_list: Optional[List[List[EC2TagFilterModel]]] = Field(
        default=None, alias="ec2TagSetList"
    )


class ListOnPremisesInstancesInputRequestModel(BaseModel):
    registration_status: Optional[Literal["Deregistered", "Registered"]] = Field(
        default=None, alias="registrationStatus"
    )
    tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="tagFilters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class OnPremisesTagSetModel(BaseModel):
    on_premises_tag_set_list: Optional[List[List[TagFilterModel]]] = Field(
        default=None, alias="onPremisesTagSetList"
    )


class LifecycleEventModel(BaseModel):
    lifecycle_event_name: Optional[str] = Field(
        default=None, alias="lifecycleEventName"
    )
    diagnostics: Optional[DiagnosticsModel] = Field(default=None, alias="diagnostics")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    status: Optional[
        Literal["Failed", "InProgress", "Pending", "Skipped", "Succeeded", "Unknown"]
    ] = Field(default=None, alias="status")


class ECSTaskSetModel(BaseModel):
    identifer: Optional[str] = Field(default=None, alias="identifer")
    desired_count: Optional[int] = Field(default=None, alias="desiredCount")
    pending_count: Optional[int] = Field(default=None, alias="pendingCount")
    running_count: Optional[int] = Field(default=None, alias="runningCount")
    status: Optional[str] = Field(default=None, alias="status")
    traffic_weight: Optional[float] = Field(default=None, alias="trafficWeight")
    target_group: Optional[TargetGroupInfoModel] = Field(
        default=None, alias="targetGroup"
    )
    task_set_label: Optional[Literal["Blue", "Green"]] = Field(
        default=None, alias="taskSetLabel"
    )


class GetDeploymentInputDeploymentSuccessfulWaitModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ListApplicationRevisionsInputListApplicationRevisionsPaginateModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    sort_by: Optional[Literal["firstUsedTime", "lastUsedTime", "registerTime"]] = Field(
        default=None, alias="sortBy"
    )
    sort_order: Optional[Literal["ascending", "descending"]] = Field(
        default=None, alias="sortOrder"
    )
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3_key_prefix: Optional[str] = Field(default=None, alias="s3KeyPrefix")
    deployed: Optional[Literal["exclude", "ignore", "include"]] = Field(
        default=None, alias="deployed"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationsInputListApplicationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentConfigsInputListDeploymentConfigsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentGroupsInputListDeploymentGroupsPaginateModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentInstancesInputListDeploymentInstancesPaginateModel(BaseModel):
    deployment_id: str = Field(alias="deploymentId")
    instance_status_filter: Optional[
        Sequence[
            Literal[
                "Failed",
                "InProgress",
                "Pending",
                "Ready",
                "Skipped",
                "Succeeded",
                "Unknown",
            ]
        ]
    ] = Field(default=None, alias="instanceStatusFilter")
    instance_type_filter: Optional[Sequence[Literal["Blue", "Green"]]] = Field(
        default=None, alias="instanceTypeFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentTargetsInputListDeploymentTargetsPaginateModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    target_filters: Optional[
        Mapping[Literal["ServerInstanceLabel", "TargetStatus"], Sequence[str]]
    ] = Field(default=None, alias="targetFilters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGitHubAccountTokenNamesInputListGitHubAccountTokenNamesPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOnPremisesInstancesInputListOnPremisesInstancesPaginateModel(BaseModel):
    registration_status: Optional[Literal["Deregistered", "Registered"]] = Field(
        default=None, alias="registrationStatus"
    )
    tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="tagFilters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentsInputListDeploymentsPaginateModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="applicationName")
    deployment_group_name: Optional[str] = Field(
        default=None, alias="deploymentGroupName"
    )
    external_id: Optional[str] = Field(default=None, alias="externalId")
    include_only_statuses: Optional[
        Sequence[
            Literal[
                "Baking",
                "Created",
                "Failed",
                "InProgress",
                "Queued",
                "Ready",
                "Stopped",
                "Succeeded",
            ]
        ]
    ] = Field(default=None, alias="includeOnlyStatuses")
    create_time_range: Optional[TimeRangeModel] = Field(
        default=None, alias="createTimeRange"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentsInputRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="applicationName")
    deployment_group_name: Optional[str] = Field(
        default=None, alias="deploymentGroupName"
    )
    external_id: Optional[str] = Field(default=None, alias="externalId")
    include_only_statuses: Optional[
        Sequence[
            Literal[
                "Baking",
                "Created",
                "Failed",
                "InProgress",
                "Queued",
                "Ready",
                "Stopped",
                "Succeeded",
            ]
        ]
    ] = Field(default=None, alias="includeOnlyStatuses")
    create_time_range: Optional[TimeRangeModel] = Field(
        default=None, alias="createTimeRange"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class RevisionLocationModel(BaseModel):
    revision_type: Optional[
        Literal["AppSpecContent", "GitHub", "S3", "String"]
    ] = Field(default=None, alias="revisionType")
    s3_location: Optional[S3LocationModel] = Field(default=None, alias="s3Location")
    git_hub_location: Optional[GitHubLocationModel] = Field(
        default=None, alias="gitHubLocation"
    )
    string: Optional[RawStringModel] = Field(default=None, alias="string")
    app_spec_content: Optional[AppSpecContentModel] = Field(
        default=None, alias="appSpecContent"
    )


class TargetGroupPairInfoModel(BaseModel):
    target_groups: Optional[List[TargetGroupInfoModel]] = Field(
        default=None, alias="targetGroups"
    )
    prod_traffic_route: Optional[TrafficRouteModel] = Field(
        default=None, alias="prodTrafficRoute"
    )
    test_traffic_route: Optional[TrafficRouteModel] = Field(
        default=None, alias="testTrafficRoute"
    )


class TrafficRoutingConfigModel(BaseModel):
    type: Optional[Literal["AllAtOnce", "TimeBasedCanary", "TimeBasedLinear"]] = Field(
        default=None, alias="type"
    )
    time_based_canary: Optional[TimeBasedCanaryModel] = Field(
        default=None, alias="timeBasedCanary"
    )
    time_based_linear: Optional[TimeBasedLinearModel] = Field(
        default=None, alias="timeBasedLinear"
    )


class BatchGetOnPremisesInstancesOutputModel(BaseModel):
    instance_infos: List[InstanceInfoModel] = Field(alias="instanceInfos")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOnPremisesInstanceOutputModel(BaseModel):
    instance_info: InstanceInfoModel = Field(alias="instanceInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TargetInstancesModel(BaseModel):
    tag_filters: Optional[List[EC2TagFilterModel]] = Field(
        default=None, alias="tagFilters"
    )
    auto_scaling_groups: Optional[List[str]] = Field(
        default=None, alias="autoScalingGroups"
    )
    ec2_tag_set: Optional[EC2TagSetModel] = Field(default=None, alias="ec2TagSet")


class CloudFormationTargetModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    target_id: Optional[str] = Field(default=None, alias="targetId")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    lifecycle_events: Optional[List[LifecycleEventModel]] = Field(
        default=None, alias="lifecycleEvents"
    )
    status: Optional[
        Literal[
            "Failed",
            "InProgress",
            "Pending",
            "Ready",
            "Skipped",
            "Succeeded",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    target_version_weight: Optional[float] = Field(
        default=None, alias="targetVersionWeight"
    )


class InstanceSummaryModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    instance_id: Optional[str] = Field(default=None, alias="instanceId")
    status: Optional[
        Literal[
            "Failed",
            "InProgress",
            "Pending",
            "Ready",
            "Skipped",
            "Succeeded",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    lifecycle_events: Optional[List[LifecycleEventModel]] = Field(
        default=None, alias="lifecycleEvents"
    )
    instance_type: Optional[Literal["Blue", "Green"]] = Field(
        default=None, alias="instanceType"
    )


class InstanceTargetModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    target_id: Optional[str] = Field(default=None, alias="targetId")
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    status: Optional[
        Literal[
            "Failed",
            "InProgress",
            "Pending",
            "Ready",
            "Skipped",
            "Succeeded",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    lifecycle_events: Optional[List[LifecycleEventModel]] = Field(
        default=None, alias="lifecycleEvents"
    )
    instance_label: Optional[Literal["Blue", "Green"]] = Field(
        default=None, alias="instanceLabel"
    )


class LambdaTargetModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    target_id: Optional[str] = Field(default=None, alias="targetId")
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    status: Optional[
        Literal[
            "Failed",
            "InProgress",
            "Pending",
            "Ready",
            "Skipped",
            "Succeeded",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    lifecycle_events: Optional[List[LifecycleEventModel]] = Field(
        default=None, alias="lifecycleEvents"
    )
    lambda_function_info: Optional[LambdaFunctionInfoModel] = Field(
        default=None, alias="lambdaFunctionInfo"
    )


class ECSTargetModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    target_id: Optional[str] = Field(default=None, alias="targetId")
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    lifecycle_events: Optional[List[LifecycleEventModel]] = Field(
        default=None, alias="lifecycleEvents"
    )
    status: Optional[
        Literal[
            "Failed",
            "InProgress",
            "Pending",
            "Ready",
            "Skipped",
            "Succeeded",
            "Unknown",
        ]
    ] = Field(default=None, alias="status")
    task_sets_info: Optional[List[ECSTaskSetModel]] = Field(
        default=None, alias="taskSetsInfo"
    )


class BatchGetApplicationRevisionsInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    revisions: Sequence[RevisionLocationModel] = Field(alias="revisions")


class GetApplicationRevisionInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    revision: RevisionLocationModel = Field(alias="revision")


class GetApplicationRevisionOutputModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    revision: RevisionLocationModel = Field(alias="revision")
    revision_info: GenericRevisionInfoModel = Field(alias="revisionInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationRevisionsOutputModel(BaseModel):
    revisions: List[RevisionLocationModel] = Field(alias="revisions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterApplicationRevisionInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    revision: RevisionLocationModel = Field(alias="revision")
    description: Optional[str] = Field(default=None, alias="description")


class RevisionInfoModel(BaseModel):
    revision_location: Optional[RevisionLocationModel] = Field(
        default=None, alias="revisionLocation"
    )
    generic_revision_info: Optional[GenericRevisionInfoModel] = Field(
        default=None, alias="genericRevisionInfo"
    )


class LoadBalancerInfoModel(BaseModel):
    elb_info_list: Optional[List[ELBInfoModel]] = Field(
        default=None, alias="elbInfoList"
    )
    target_group_info_list: Optional[List[TargetGroupInfoModel]] = Field(
        default=None, alias="targetGroupInfoList"
    )
    target_group_pair_info_list: Optional[List[TargetGroupPairInfoModel]] = Field(
        default=None, alias="targetGroupPairInfoList"
    )


class CreateDeploymentConfigInputRequestModel(BaseModel):
    deployment_config_name: str = Field(alias="deploymentConfigName")
    minimum_healthy_hosts: Optional[MinimumHealthyHostsModel] = Field(
        default=None, alias="minimumHealthyHosts"
    )
    traffic_routing_config: Optional[TrafficRoutingConfigModel] = Field(
        default=None, alias="trafficRoutingConfig"
    )
    compute_platform: Optional[Literal["ECS", "Lambda", "Server"]] = Field(
        default=None, alias="computePlatform"
    )


class DeploymentConfigInfoModel(BaseModel):
    deployment_config_id: Optional[str] = Field(
        default=None, alias="deploymentConfigId"
    )
    deployment_config_name: Optional[str] = Field(
        default=None, alias="deploymentConfigName"
    )
    minimum_healthy_hosts: Optional[MinimumHealthyHostsModel] = Field(
        default=None, alias="minimumHealthyHosts"
    )
    create_time: Optional[datetime] = Field(default=None, alias="createTime")
    compute_platform: Optional[Literal["ECS", "Lambda", "Server"]] = Field(
        default=None, alias="computePlatform"
    )
    traffic_routing_config: Optional[TrafficRoutingConfigModel] = Field(
        default=None, alias="trafficRoutingConfig"
    )


class CreateDeploymentInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    deployment_group_name: Optional[str] = Field(
        default=None, alias="deploymentGroupName"
    )
    revision: Optional[RevisionLocationModel] = Field(default=None, alias="revision")
    deployment_config_name: Optional[str] = Field(
        default=None, alias="deploymentConfigName"
    )
    description: Optional[str] = Field(default=None, alias="description")
    ignore_application_stop_failures: Optional[bool] = Field(
        default=None, alias="ignoreApplicationStopFailures"
    )
    target_instances: Optional[TargetInstancesModel] = Field(
        default=None, alias="targetInstances"
    )
    auto_rollback_configuration: Optional[AutoRollbackConfigurationModel] = Field(
        default=None, alias="autoRollbackConfiguration"
    )
    update_outdated_instances_only: Optional[bool] = Field(
        default=None, alias="updateOutdatedInstancesOnly"
    )
    file_exists_behavior: Optional[Literal["DISALLOW", "OVERWRITE", "RETAIN"]] = Field(
        default=None, alias="fileExistsBehavior"
    )
    override_alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="overrideAlarmConfiguration"
    )


class BatchGetDeploymentInstancesOutputModel(BaseModel):
    instances_summary: List[InstanceSummaryModel] = Field(alias="instancesSummary")
    error_message: str = Field(alias="errorMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentInstanceOutputModel(BaseModel):
    instance_summary: InstanceSummaryModel = Field(alias="instanceSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentTargetModel(BaseModel):
    deployment_target_type: Optional[
        Literal["CloudFormationTarget", "ECSTarget", "InstanceTarget", "LambdaTarget"]
    ] = Field(default=None, alias="deploymentTargetType")
    instance_target: Optional[InstanceTargetModel] = Field(
        default=None, alias="instanceTarget"
    )
    lambda_target: Optional[LambdaTargetModel] = Field(
        default=None, alias="lambdaTarget"
    )
    ecs_target: Optional[ECSTargetModel] = Field(default=None, alias="ecsTarget")
    cloud_formation_target: Optional[CloudFormationTargetModel] = Field(
        default=None, alias="cloudFormationTarget"
    )


class BatchGetApplicationRevisionsOutputModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    error_message: str = Field(alias="errorMessage")
    revisions: List[RevisionInfoModel] = Field(alias="revisions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentGroupInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    deployment_group_name: str = Field(alias="deploymentGroupName")
    service_role_arn: str = Field(alias="serviceRoleArn")
    deployment_config_name: Optional[str] = Field(
        default=None, alias="deploymentConfigName"
    )
    ec2_tag_filters: Optional[Sequence[EC2TagFilterModel]] = Field(
        default=None, alias="ec2TagFilters"
    )
    on_premises_instance_tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="onPremisesInstanceTagFilters"
    )
    auto_scaling_groups: Optional[Sequence[str]] = Field(
        default=None, alias="autoScalingGroups"
    )
    trigger_configurations: Optional[Sequence[TriggerConfigModel]] = Field(
        default=None, alias="triggerConfigurations"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="alarmConfiguration"
    )
    auto_rollback_configuration: Optional[AutoRollbackConfigurationModel] = Field(
        default=None, alias="autoRollbackConfiguration"
    )
    outdated_instances_strategy: Optional[Literal["IGNORE", "UPDATE"]] = Field(
        default=None, alias="outdatedInstancesStrategy"
    )
    deployment_style: Optional[DeploymentStyleModel] = Field(
        default=None, alias="deploymentStyle"
    )
    blue_green_deployment_configuration: Optional[
        BlueGreenDeploymentConfigurationModel
    ] = Field(default=None, alias="blueGreenDeploymentConfiguration")
    load_balancer_info: Optional[LoadBalancerInfoModel] = Field(
        default=None, alias="loadBalancerInfo"
    )
    ec2_tag_set: Optional[EC2TagSetModel] = Field(default=None, alias="ec2TagSet")
    ecs_services: Optional[Sequence[ECSServiceModel]] = Field(
        default=None, alias="ecsServices"
    )
    on_premises_tag_set: Optional[OnPremisesTagSetModel] = Field(
        default=None, alias="onPremisesTagSet"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class DeploymentGroupInfoModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="applicationName")
    deployment_group_id: Optional[str] = Field(default=None, alias="deploymentGroupId")
    deployment_group_name: Optional[str] = Field(
        default=None, alias="deploymentGroupName"
    )
    deployment_config_name: Optional[str] = Field(
        default=None, alias="deploymentConfigName"
    )
    ec2_tag_filters: Optional[List[EC2TagFilterModel]] = Field(
        default=None, alias="ec2TagFilters"
    )
    on_premises_instance_tag_filters: Optional[List[TagFilterModel]] = Field(
        default=None, alias="onPremisesInstanceTagFilters"
    )
    auto_scaling_groups: Optional[List[AutoScalingGroupModel]] = Field(
        default=None, alias="autoScalingGroups"
    )
    service_role_arn: Optional[str] = Field(default=None, alias="serviceRoleArn")
    target_revision: Optional[RevisionLocationModel] = Field(
        default=None, alias="targetRevision"
    )
    trigger_configurations: Optional[List[TriggerConfigModel]] = Field(
        default=None, alias="triggerConfigurations"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="alarmConfiguration"
    )
    auto_rollback_configuration: Optional[AutoRollbackConfigurationModel] = Field(
        default=None, alias="autoRollbackConfiguration"
    )
    deployment_style: Optional[DeploymentStyleModel] = Field(
        default=None, alias="deploymentStyle"
    )
    outdated_instances_strategy: Optional[Literal["IGNORE", "UPDATE"]] = Field(
        default=None, alias="outdatedInstancesStrategy"
    )
    blue_green_deployment_configuration: Optional[
        BlueGreenDeploymentConfigurationModel
    ] = Field(default=None, alias="blueGreenDeploymentConfiguration")
    load_balancer_info: Optional[LoadBalancerInfoModel] = Field(
        default=None, alias="loadBalancerInfo"
    )
    last_successful_deployment: Optional[LastDeploymentInfoModel] = Field(
        default=None, alias="lastSuccessfulDeployment"
    )
    last_attempted_deployment: Optional[LastDeploymentInfoModel] = Field(
        default=None, alias="lastAttemptedDeployment"
    )
    ec2_tag_set: Optional[EC2TagSetModel] = Field(default=None, alias="ec2TagSet")
    on_premises_tag_set: Optional[OnPremisesTagSetModel] = Field(
        default=None, alias="onPremisesTagSet"
    )
    compute_platform: Optional[Literal["ECS", "Lambda", "Server"]] = Field(
        default=None, alias="computePlatform"
    )
    ecs_services: Optional[List[ECSServiceModel]] = Field(
        default=None, alias="ecsServices"
    )


class DeploymentInfoModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="applicationName")
    deployment_group_name: Optional[str] = Field(
        default=None, alias="deploymentGroupName"
    )
    deployment_config_name: Optional[str] = Field(
        default=None, alias="deploymentConfigName"
    )
    deployment_id: Optional[str] = Field(default=None, alias="deploymentId")
    previous_revision: Optional[RevisionLocationModel] = Field(
        default=None, alias="previousRevision"
    )
    revision: Optional[RevisionLocationModel] = Field(default=None, alias="revision")
    status: Optional[
        Literal[
            "Baking",
            "Created",
            "Failed",
            "InProgress",
            "Queued",
            "Ready",
            "Stopped",
            "Succeeded",
        ]
    ] = Field(default=None, alias="status")
    error_information: Optional[ErrorInformationModel] = Field(
        default=None, alias="errorInformation"
    )
    create_time: Optional[datetime] = Field(default=None, alias="createTime")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    complete_time: Optional[datetime] = Field(default=None, alias="completeTime")
    deployment_overview: Optional[DeploymentOverviewModel] = Field(
        default=None, alias="deploymentOverview"
    )
    description: Optional[str] = Field(default=None, alias="description")
    creator: Optional[
        Literal[
            "CloudFormation",
            "CloudFormationRollback",
            "CodeDeploy",
            "CodeDeployAutoUpdate",
            "autoscaling",
            "codeDeployRollback",
            "user",
        ]
    ] = Field(default=None, alias="creator")
    ignore_application_stop_failures: Optional[bool] = Field(
        default=None, alias="ignoreApplicationStopFailures"
    )
    auto_rollback_configuration: Optional[AutoRollbackConfigurationModel] = Field(
        default=None, alias="autoRollbackConfiguration"
    )
    update_outdated_instances_only: Optional[bool] = Field(
        default=None, alias="updateOutdatedInstancesOnly"
    )
    rollback_info: Optional[RollbackInfoModel] = Field(
        default=None, alias="rollbackInfo"
    )
    deployment_style: Optional[DeploymentStyleModel] = Field(
        default=None, alias="deploymentStyle"
    )
    target_instances: Optional[TargetInstancesModel] = Field(
        default=None, alias="targetInstances"
    )
    instance_termination_wait_time_started: Optional[bool] = Field(
        default=None, alias="instanceTerminationWaitTimeStarted"
    )
    blue_green_deployment_configuration: Optional[
        BlueGreenDeploymentConfigurationModel
    ] = Field(default=None, alias="blueGreenDeploymentConfiguration")
    load_balancer_info: Optional[LoadBalancerInfoModel] = Field(
        default=None, alias="loadBalancerInfo"
    )
    additional_deployment_status_info: Optional[str] = Field(
        default=None, alias="additionalDeploymentStatusInfo"
    )
    file_exists_behavior: Optional[Literal["DISALLOW", "OVERWRITE", "RETAIN"]] = Field(
        default=None, alias="fileExistsBehavior"
    )
    deployment_status_messages: Optional[List[str]] = Field(
        default=None, alias="deploymentStatusMessages"
    )
    compute_platform: Optional[Literal["ECS", "Lambda", "Server"]] = Field(
        default=None, alias="computePlatform"
    )
    external_id: Optional[str] = Field(default=None, alias="externalId")
    related_deployments: Optional[RelatedDeploymentsModel] = Field(
        default=None, alias="relatedDeployments"
    )
    override_alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="overrideAlarmConfiguration"
    )


class UpdateDeploymentGroupInputRequestModel(BaseModel):
    application_name: str = Field(alias="applicationName")
    current_deployment_group_name: str = Field(alias="currentDeploymentGroupName")
    new_deployment_group_name: Optional[str] = Field(
        default=None, alias="newDeploymentGroupName"
    )
    deployment_config_name: Optional[str] = Field(
        default=None, alias="deploymentConfigName"
    )
    ec2_tag_filters: Optional[Sequence[EC2TagFilterModel]] = Field(
        default=None, alias="ec2TagFilters"
    )
    on_premises_instance_tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="onPremisesInstanceTagFilters"
    )
    auto_scaling_groups: Optional[Sequence[str]] = Field(
        default=None, alias="autoScalingGroups"
    )
    service_role_arn: Optional[str] = Field(default=None, alias="serviceRoleArn")
    trigger_configurations: Optional[Sequence[TriggerConfigModel]] = Field(
        default=None, alias="triggerConfigurations"
    )
    alarm_configuration: Optional[AlarmConfigurationModel] = Field(
        default=None, alias="alarmConfiguration"
    )
    auto_rollback_configuration: Optional[AutoRollbackConfigurationModel] = Field(
        default=None, alias="autoRollbackConfiguration"
    )
    outdated_instances_strategy: Optional[Literal["IGNORE", "UPDATE"]] = Field(
        default=None, alias="outdatedInstancesStrategy"
    )
    deployment_style: Optional[DeploymentStyleModel] = Field(
        default=None, alias="deploymentStyle"
    )
    blue_green_deployment_configuration: Optional[
        BlueGreenDeploymentConfigurationModel
    ] = Field(default=None, alias="blueGreenDeploymentConfiguration")
    load_balancer_info: Optional[LoadBalancerInfoModel] = Field(
        default=None, alias="loadBalancerInfo"
    )
    ec2_tag_set: Optional[EC2TagSetModel] = Field(default=None, alias="ec2TagSet")
    ecs_services: Optional[Sequence[ECSServiceModel]] = Field(
        default=None, alias="ecsServices"
    )
    on_premises_tag_set: Optional[OnPremisesTagSetModel] = Field(
        default=None, alias="onPremisesTagSet"
    )


class GetDeploymentConfigOutputModel(BaseModel):
    deployment_config_info: DeploymentConfigInfoModel = Field(
        alias="deploymentConfigInfo"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetDeploymentTargetsOutputModel(BaseModel):
    deployment_targets: List[DeploymentTargetModel] = Field(alias="deploymentTargets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentTargetOutputModel(BaseModel):
    deployment_target: DeploymentTargetModel = Field(alias="deploymentTarget")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetDeploymentGroupsOutputModel(BaseModel):
    deployment_groups_info: List[DeploymentGroupInfoModel] = Field(
        alias="deploymentGroupsInfo"
    )
    error_message: str = Field(alias="errorMessage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentGroupOutputModel(BaseModel):
    deployment_group_info: DeploymentGroupInfoModel = Field(alias="deploymentGroupInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetDeploymentsOutputModel(BaseModel):
    deployments_info: List[DeploymentInfoModel] = Field(alias="deploymentsInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentOutputModel(BaseModel):
    deployment_info: DeploymentInfoModel = Field(alias="deploymentInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
