# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AbortEnvironmentUpdateMessageRequestModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class LatencyModel(BaseModel):
    p999: Optional[float] = Field(default=None, alias="P999")
    p99: Optional[float] = Field(default=None, alias="P99")
    p95: Optional[float] = Field(default=None, alias="P95")
    p90: Optional[float] = Field(default=None, alias="P90")
    p85: Optional[float] = Field(default=None, alias="P85")
    p75: Optional[float] = Field(default=None, alias="P75")
    p50: Optional[float] = Field(default=None, alias="P50")
    p10: Optional[float] = Field(default=None, alias="P10")


class StatusCodesModel(BaseModel):
    status2xx: Optional[int] = Field(default=None, alias="Status2xx")
    status3xx: Optional[int] = Field(default=None, alias="Status3xx")
    status4xx: Optional[int] = Field(default=None, alias="Status4xx")
    status5xx: Optional[int] = Field(default=None, alias="Status5xx")


class S3LocationModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")


class SourceBuildInformationModel(BaseModel):
    source_type: Literal["Git", "Zip"] = Field(alias="SourceType")
    source_repository: Literal["CodeCommit", "S3"] = Field(alias="SourceRepository")
    source_location: str = Field(alias="SourceLocation")


class MaxAgeRuleModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    max_age_in_days: Optional[int] = Field(default=None, alias="MaxAgeInDays")
    delete_source_from_s3: Optional[bool] = Field(
        default=None, alias="DeleteSourceFromS3"
    )


class MaxCountRuleModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    max_count: Optional[int] = Field(default=None, alias="MaxCount")
    delete_source_from_s3: Optional[bool] = Field(
        default=None, alias="DeleteSourceFromS3"
    )


class ApplyEnvironmentManagedActionRequestModel(BaseModel):
    action_id: str = Field(alias="ActionId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")


class AssociateEnvironmentOperationsRoleMessageRequestModel(BaseModel):
    environment_name: str = Field(alias="EnvironmentName")
    operations_role: str = Field(alias="OperationsRole")


class AutoScalingGroupModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class BuildConfigurationModel(BaseModel):
    code_build_service_role: str = Field(alias="CodeBuildServiceRole")
    image: str = Field(alias="Image")
    artifact_name: Optional[str] = Field(default=None, alias="ArtifactName")
    compute_type: Optional[
        Literal["BUILD_GENERAL1_LARGE", "BUILD_GENERAL1_MEDIUM", "BUILD_GENERAL1_SMALL"]
    ] = Field(default=None, alias="ComputeType")
    timeout_in_minutes: Optional[int] = Field(default=None, alias="TimeoutInMinutes")


class BuilderModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="ARN")


class CPUUtilizationModel(BaseModel):
    user: Optional[float] = Field(default=None, alias="User")
    nice: Optional[float] = Field(default=None, alias="Nice")
    system: Optional[float] = Field(default=None, alias="System")
    idle: Optional[float] = Field(default=None, alias="Idle")
    iowait: Optional[float] = Field(default=None, alias="IOWait")
    irq: Optional[float] = Field(default=None, alias="IRQ")
    soft_irq: Optional[float] = Field(default=None, alias="SoftIRQ")
    privileged: Optional[float] = Field(default=None, alias="Privileged")


class CheckDNSAvailabilityMessageRequestModel(BaseModel):
    cnameprefix: str = Field(alias="CNAMEPrefix")


class ComposeEnvironmentsMessageRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    version_labels: Optional[Sequence[str]] = Field(default=None, alias="VersionLabels")


class OptionRestrictionRegexModel(BaseModel):
    pattern: Optional[str] = Field(default=None, alias="Pattern")
    label: Optional[str] = Field(default=None, alias="Label")


class ConfigurationOptionSettingModel(BaseModel):
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    option_name: Optional[str] = Field(default=None, alias="OptionName")
    value: Optional[str] = Field(default=None, alias="Value")


class ValidationMessageModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="Message")
    severity: Optional[Literal["error", "warning"]] = Field(
        default=None, alias="Severity"
    )
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    option_name: Optional[str] = Field(default=None, alias="OptionName")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class SourceConfigurationModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")


class EnvironmentTierModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    version: Optional[str] = Field(default=None, alias="Version")


class OptionSpecificationModel(BaseModel):
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    option_name: Optional[str] = Field(default=None, alias="OptionName")


class PlatformSummaryModel(BaseModel):
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    platform_owner: Optional[str] = Field(default=None, alias="PlatformOwner")
    platform_status: Optional[
        Literal["Creating", "Deleted", "Deleting", "Failed", "Ready"]
    ] = Field(default=None, alias="PlatformStatus")
    platform_category: Optional[str] = Field(default=None, alias="PlatformCategory")
    operating_system_name: Optional[str] = Field(
        default=None, alias="OperatingSystemName"
    )
    operating_system_version: Optional[str] = Field(
        default=None, alias="OperatingSystemVersion"
    )
    supported_tier_list: Optional[List[str]] = Field(
        default=None, alias="SupportedTierList"
    )
    supported_addon_list: Optional[List[str]] = Field(
        default=None, alias="SupportedAddonList"
    )
    platform_lifecycle_state: Optional[str] = Field(
        default=None, alias="PlatformLifecycleState"
    )
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    platform_branch_name: Optional[str] = Field(
        default=None, alias="PlatformBranchName"
    )
    platform_branch_lifecycle_state: Optional[str] = Field(
        default=None, alias="PlatformBranchLifecycleState"
    )


class CustomAmiModel(BaseModel):
    virtualization_type: Optional[str] = Field(default=None, alias="VirtualizationType")
    image_id: Optional[str] = Field(default=None, alias="ImageId")


class DeleteApplicationMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    terminate_env_by_force: Optional[bool] = Field(
        default=None, alias="TerminateEnvByForce"
    )


class DeleteApplicationVersionMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    version_label: str = Field(alias="VersionLabel")
    delete_source_bundle: Optional[bool] = Field(
        default=None, alias="DeleteSourceBundle"
    )


class DeleteConfigurationTemplateMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    template_name: str = Field(alias="TemplateName")


class DeleteEnvironmentConfigurationMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    environment_name: str = Field(alias="EnvironmentName")


class DeletePlatformVersionRequestModel(BaseModel):
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")


class DeploymentModel(BaseModel):
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    deployment_id: Optional[int] = Field(default=None, alias="DeploymentId")
    status: Optional[str] = Field(default=None, alias="Status")
    deployment_time: Optional[datetime] = Field(default=None, alias="DeploymentTime")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeApplicationVersionsMessageRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_labels: Optional[Sequence[str]] = Field(default=None, alias="VersionLabels")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeApplicationsMessageRequestModel(BaseModel):
    application_names: Optional[Sequence[str]] = Field(
        default=None, alias="ApplicationNames"
    )


class DescribeConfigurationSettingsMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class DescribeEnvironmentHealthRequestModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    attribute_names: Optional[
        Sequence[
            Literal[
                "All",
                "ApplicationMetrics",
                "Causes",
                "Color",
                "HealthStatus",
                "InstancesHealth",
                "RefreshedAt",
                "Status",
            ]
        ]
    ] = Field(default=None, alias="AttributeNames")


class InstanceHealthSummaryModel(BaseModel):
    no_data: Optional[int] = Field(default=None, alias="NoData")
    unknown: Optional[int] = Field(default=None, alias="Unknown")
    pending: Optional[int] = Field(default=None, alias="Pending")
    ok: Optional[int] = Field(default=None, alias="Ok")
    info: Optional[int] = Field(default=None, alias="Info")
    warning: Optional[int] = Field(default=None, alias="Warning")
    degraded: Optional[int] = Field(default=None, alias="Degraded")
    severe: Optional[int] = Field(default=None, alias="Severe")


class DescribeEnvironmentManagedActionHistoryRequestModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_items: Optional[int] = Field(default=None, alias="MaxItems")


class ManagedActionHistoryItemModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="ActionId")
    action_type: Optional[
        Literal["InstanceRefresh", "PlatformUpdate", "Unknown"]
    ] = Field(default=None, alias="ActionType")
    action_description: Optional[str] = Field(default=None, alias="ActionDescription")
    failure_type: Optional[
        Literal[
            "CancellationFailed",
            "InternalFailure",
            "InvalidEnvironmentState",
            "PermissionsError",
            "RollbackFailed",
            "RollbackSuccessful",
            "UpdateCancelled",
        ]
    ] = Field(default=None, alias="FailureType")
    status: Optional[Literal["Completed", "Failed", "Unknown"]] = Field(
        default=None, alias="Status"
    )
    failure_description: Optional[str] = Field(default=None, alias="FailureDescription")
    executed_time: Optional[datetime] = Field(default=None, alias="ExecutedTime")
    finished_time: Optional[datetime] = Field(default=None, alias="FinishedTime")


class DescribeEnvironmentManagedActionsRequestModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    status: Optional[Literal["Pending", "Running", "Scheduled", "Unknown"]] = Field(
        default=None, alias="Status"
    )


class ManagedActionModel(BaseModel):
    action_id: Optional[str] = Field(default=None, alias="ActionId")
    action_description: Optional[str] = Field(default=None, alias="ActionDescription")
    action_type: Optional[
        Literal["InstanceRefresh", "PlatformUpdate", "Unknown"]
    ] = Field(default=None, alias="ActionType")
    status: Optional[Literal["Pending", "Running", "Scheduled", "Unknown"]] = Field(
        default=None, alias="Status"
    )
    window_start_time: Optional[datetime] = Field(default=None, alias="WindowStartTime")


class DescribeEnvironmentResourcesMessageRequestModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeEnvironmentsMessageRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    environment_ids: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentIds"
    )
    environment_names: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentNames"
    )
    include_deleted: Optional[bool] = Field(default=None, alias="IncludeDeleted")
    included_deleted_back_to: Optional[Union[datetime, str]] = Field(
        default=None, alias="IncludedDeletedBackTo"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeEventsMessageRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    severity: Optional[
        Literal["DEBUG", "ERROR", "FATAL", "INFO", "TRACE", "WARN"]
    ] = Field(default=None, alias="Severity")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeInstancesHealthRequestModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    attribute_names: Optional[
        Sequence[
            Literal[
                "All",
                "ApplicationMetrics",
                "AvailabilityZone",
                "Causes",
                "Color",
                "Deployment",
                "HealthStatus",
                "InstanceType",
                "LaunchedAt",
                "RefreshedAt",
                "System",
            ]
        ]
    ] = Field(default=None, alias="AttributeNames")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePlatformVersionRequestModel(BaseModel):
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")


class DisassociateEnvironmentOperationsRoleMessageRequestModel(BaseModel):
    environment_name: str = Field(alias="EnvironmentName")


class EnvironmentLinkModel(BaseModel):
    link_name: Optional[str] = Field(default=None, alias="LinkName")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class EnvironmentInfoDescriptionModel(BaseModel):
    info_type: Optional[Literal["bundle", "tail"]] = Field(
        default=None, alias="InfoType"
    )
    ec2_instance_id: Optional[str] = Field(default=None, alias="Ec2InstanceId")
    sample_timestamp: Optional[datetime] = Field(default=None, alias="SampleTimestamp")
    message: Optional[str] = Field(default=None, alias="Message")


class InstanceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class LaunchConfigurationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class LaunchTemplateModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class LoadBalancerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class QueueModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    url: Optional[str] = Field(default=None, alias="URL")


class TriggerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class EventDescriptionModel(BaseModel):
    event_date: Optional[datetime] = Field(default=None, alias="EventDate")
    message: Optional[str] = Field(default=None, alias="Message")
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    severity: Optional[
        Literal["DEBUG", "ERROR", "FATAL", "INFO", "TRACE", "WARN"]
    ] = Field(default=None, alias="Severity")


class SolutionStackDescriptionModel(BaseModel):
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    permitted_file_types: Optional[List[str]] = Field(
        default=None, alias="PermittedFileTypes"
    )


class SearchFilterModel(BaseModel):
    attribute: Optional[str] = Field(default=None, alias="Attribute")
    operator: Optional[str] = Field(default=None, alias="Operator")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class PlatformBranchSummaryModel(BaseModel):
    platform_name: Optional[str] = Field(default=None, alias="PlatformName")
    branch_name: Optional[str] = Field(default=None, alias="BranchName")
    lifecycle_state: Optional[str] = Field(default=None, alias="LifecycleState")
    branch_order: Optional[int] = Field(default=None, alias="BranchOrder")
    supported_tier_list: Optional[List[str]] = Field(
        default=None, alias="SupportedTierList"
    )


class PlatformFilterModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    operator: Optional[str] = Field(default=None, alias="Operator")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class ListTagsForResourceMessageRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListenerModel(BaseModel):
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    port: Optional[int] = Field(default=None, alias="Port")


class PlatformFrameworkModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class PlatformProgrammingLanguageModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class RebuildEnvironmentMessageRequestModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class RequestEnvironmentInfoMessageRequestModel(BaseModel):
    info_type: Literal["bundle", "tail"] = Field(alias="InfoType")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class ResourceQuotaModel(BaseModel):
    maximum: Optional[int] = Field(default=None, alias="Maximum")


class RestartAppServerMessageRequestModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class RetrieveEnvironmentInfoMessageRequestModel(BaseModel):
    info_type: Literal["bundle", "tail"] = Field(alias="InfoType")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class SwapEnvironmentCNAMEsMessageRequestModel(BaseModel):
    source_environment_id: Optional[str] = Field(
        default=None, alias="SourceEnvironmentId"
    )
    source_environment_name: Optional[str] = Field(
        default=None, alias="SourceEnvironmentName"
    )
    destination_environment_id: Optional[str] = Field(
        default=None, alias="DestinationEnvironmentId"
    )
    destination_environment_name: Optional[str] = Field(
        default=None, alias="DestinationEnvironmentName"
    )


class TerminateEnvironmentMessageRequestModel(BaseModel):
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    terminate_resources: Optional[bool] = Field(
        default=None, alias="TerminateResources"
    )
    force_terminate: Optional[bool] = Field(default=None, alias="ForceTerminate")


class UpdateApplicationMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateApplicationVersionMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    version_label: str = Field(alias="VersionLabel")
    description: Optional[str] = Field(default=None, alias="Description")


class ApplyEnvironmentManagedActionResultModel(BaseModel):
    action_id: str = Field(alias="ActionId")
    action_description: str = Field(alias="ActionDescription")
    action_type: Literal["InstanceRefresh", "PlatformUpdate", "Unknown"] = Field(
        alias="ActionType"
    )
    status: str = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CheckDNSAvailabilityResultMessageModel(BaseModel):
    available: bool = Field(alias="Available")
    fully_qualified_cname: str = Field(alias="FullyQualifiedCNAME")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStorageLocationResultMessageModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplicationMetricsModel(BaseModel):
    duration: Optional[int] = Field(default=None, alias="Duration")
    request_count: Optional[int] = Field(default=None, alias="RequestCount")
    status_codes: Optional[StatusCodesModel] = Field(default=None, alias="StatusCodes")
    latency: Optional[LatencyModel] = Field(default=None, alias="Latency")


class ApplicationVersionDescriptionModel(BaseModel):
    application_version_arn: Optional[str] = Field(
        default=None, alias="ApplicationVersionArn"
    )
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    description: Optional[str] = Field(default=None, alias="Description")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    source_build_information: Optional[SourceBuildInformationModel] = Field(
        default=None, alias="SourceBuildInformation"
    )
    build_arn: Optional[str] = Field(default=None, alias="BuildArn")
    source_bundle: Optional[S3LocationModel] = Field(default=None, alias="SourceBundle")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_updated: Optional[datetime] = Field(default=None, alias="DateUpdated")
    status: Optional[
        Literal["Building", "Failed", "Processed", "Processing", "Unprocessed"]
    ] = Field(default=None, alias="Status")


class ApplicationVersionLifecycleConfigModel(BaseModel):
    max_count_rule: Optional[MaxCountRuleModel] = Field(
        default=None, alias="MaxCountRule"
    )
    max_age_rule: Optional[MaxAgeRuleModel] = Field(default=None, alias="MaxAgeRule")


class SystemStatusModel(BaseModel):
    cp_uutilization: Optional[CPUUtilizationModel] = Field(
        default=None, alias="CPUUtilization"
    )
    load_average: Optional[List[float]] = Field(default=None, alias="LoadAverage")


class ConfigurationOptionDescriptionModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    name: Optional[str] = Field(default=None, alias="Name")
    default_value: Optional[str] = Field(default=None, alias="DefaultValue")
    change_severity: Optional[str] = Field(default=None, alias="ChangeSeverity")
    user_defined: Optional[bool] = Field(default=None, alias="UserDefined")
    value_type: Optional[Literal["List", "Scalar"]] = Field(
        default=None, alias="ValueType"
    )
    value_options: Optional[List[str]] = Field(default=None, alias="ValueOptions")
    min_value: Optional[int] = Field(default=None, alias="MinValue")
    max_value: Optional[int] = Field(default=None, alias="MaxValue")
    max_length: Optional[int] = Field(default=None, alias="MaxLength")
    regex: Optional[OptionRestrictionRegexModel] = Field(default=None, alias="Regex")


class ConfigurationSettingsDescriptionResponseMetadataModel(BaseModel):
    solution_stack_name: str = Field(alias="SolutionStackName")
    platform_arn: str = Field(alias="PlatformArn")
    application_name: str = Field(alias="ApplicationName")
    template_name: str = Field(alias="TemplateName")
    description: str = Field(alias="Description")
    environment_name: str = Field(alias="EnvironmentName")
    deployment_status: Literal["deployed", "failed", "pending"] = Field(
        alias="DeploymentStatus"
    )
    date_created: datetime = Field(alias="DateCreated")
    date_updated: datetime = Field(alias="DateUpdated")
    option_settings: List[ConfigurationOptionSettingModel] = Field(
        alias="OptionSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationSettingsDescriptionModel(BaseModel):
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    description: Optional[str] = Field(default=None, alias="Description")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    deployment_status: Optional[Literal["deployed", "failed", "pending"]] = Field(
        default=None, alias="DeploymentStatus"
    )
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_updated: Optional[datetime] = Field(default=None, alias="DateUpdated")
    option_settings: Optional[List[ConfigurationOptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )


class ValidateConfigurationSettingsMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    option_settings: Sequence[ConfigurationOptionSettingModel] = Field(
        alias="OptionSettings"
    )
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")


class ConfigurationSettingsValidationMessagesModel(BaseModel):
    messages: List[ValidationMessageModel] = Field(alias="Messages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationVersionMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    version_label: str = Field(alias="VersionLabel")
    description: Optional[str] = Field(default=None, alias="Description")
    source_build_information: Optional[SourceBuildInformationModel] = Field(
        default=None, alias="SourceBuildInformation"
    )
    source_bundle: Optional[S3LocationModel] = Field(default=None, alias="SourceBundle")
    build_configuration: Optional[BuildConfigurationModel] = Field(
        default=None, alias="BuildConfiguration"
    )
    auto_create_application: Optional[bool] = Field(
        default=None, alias="AutoCreateApplication"
    )
    process: Optional[bool] = Field(default=None, alias="Process")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreatePlatformVersionRequestModel(BaseModel):
    platform_name: str = Field(alias="PlatformName")
    platform_version: str = Field(alias="PlatformVersion")
    platform_definition_bundle: S3LocationModel = Field(
        alias="PlatformDefinitionBundle"
    )
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    option_settings: Optional[Sequence[ConfigurationOptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ResourceTagsDescriptionMessageModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    resource_tags: List[TagModel] = Field(alias="ResourceTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTagsForResourceMessageRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags_to_add: Optional[Sequence[TagModel]] = Field(default=None, alias="TagsToAdd")
    tags_to_remove: Optional[Sequence[str]] = Field(default=None, alias="TagsToRemove")


class CreateConfigurationTemplateMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    template_name: str = Field(alias="TemplateName")
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    source_configuration: Optional[SourceConfigurationModel] = Field(
        default=None, alias="SourceConfiguration"
    )
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    description: Optional[str] = Field(default=None, alias="Description")
    option_settings: Optional[Sequence[ConfigurationOptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateEnvironmentMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    cnameprefix: Optional[str] = Field(default=None, alias="CNAMEPrefix")
    tier: Optional[EnvironmentTierModel] = Field(default=None, alias="Tier")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    option_settings: Optional[Sequence[ConfigurationOptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )
    options_to_remove: Optional[Sequence[OptionSpecificationModel]] = Field(
        default=None, alias="OptionsToRemove"
    )
    operations_role: Optional[str] = Field(default=None, alias="OperationsRole")


class DescribeConfigurationOptionsMessageRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    options: Optional[Sequence[OptionSpecificationModel]] = Field(
        default=None, alias="Options"
    )


class UpdateConfigurationTemplateMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    template_name: str = Field(alias="TemplateName")
    description: Optional[str] = Field(default=None, alias="Description")
    option_settings: Optional[Sequence[ConfigurationOptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )
    options_to_remove: Optional[Sequence[OptionSpecificationModel]] = Field(
        default=None, alias="OptionsToRemove"
    )


class UpdateEnvironmentMessageRequestModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    tier: Optional[EnvironmentTierModel] = Field(default=None, alias="Tier")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    option_settings: Optional[Sequence[ConfigurationOptionSettingModel]] = Field(
        default=None, alias="OptionSettings"
    )
    options_to_remove: Optional[Sequence[OptionSpecificationModel]] = Field(
        default=None, alias="OptionsToRemove"
    )


class CreatePlatformVersionResultModel(BaseModel):
    platform_summary: PlatformSummaryModel = Field(alias="PlatformSummary")
    builder: BuilderModel = Field(alias="Builder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePlatformVersionResultModel(BaseModel):
    platform_summary: PlatformSummaryModel = Field(alias="PlatformSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPlatformVersionsResultModel(BaseModel):
    platform_summary_list: List[PlatformSummaryModel] = Field(
        alias="PlatformSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationVersionsMessageDescribeApplicationVersionsPaginateModel(
    BaseModel
):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_labels: Optional[Sequence[str]] = Field(default=None, alias="VersionLabels")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEnvironmentManagedActionHistoryRequestDescribeEnvironmentManagedActionHistoryPaginateModel(
    BaseModel
):
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEnvironmentsMessageDescribeEnvironmentsPaginateModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    environment_ids: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentIds"
    )
    environment_names: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentNames"
    )
    include_deleted: Optional[bool] = Field(default=None, alias="IncludeDeleted")
    included_deleted_back_to: Optional[Union[datetime, str]] = Field(
        default=None, alias="IncludedDeletedBackTo"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEventsMessageDescribeEventsPaginateModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    severity: Optional[
        Literal["DEBUG", "ERROR", "FATAL", "INFO", "TRACE", "WARN"]
    ] = Field(default=None, alias="Severity")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEnvironmentManagedActionHistoryResultModel(BaseModel):
    managed_action_history_items: List[ManagedActionHistoryItemModel] = Field(
        alias="ManagedActionHistoryItems"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEnvironmentManagedActionsResultModel(BaseModel):
    managed_actions: List[ManagedActionModel] = Field(alias="ManagedActions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEnvironmentsMessageEnvironmentExistsWaitModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    environment_ids: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentIds"
    )
    environment_names: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentNames"
    )
    include_deleted: Optional[bool] = Field(default=None, alias="IncludeDeleted")
    included_deleted_back_to: Optional[Union[datetime, str]] = Field(
        default=None, alias="IncludedDeletedBackTo"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEnvironmentsMessageEnvironmentTerminatedWaitModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    environment_ids: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentIds"
    )
    environment_names: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentNames"
    )
    include_deleted: Optional[bool] = Field(default=None, alias="IncludeDeleted")
    included_deleted_back_to: Optional[Union[datetime, str]] = Field(
        default=None, alias="IncludedDeletedBackTo"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeEnvironmentsMessageEnvironmentUpdatedWaitModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    environment_ids: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentIds"
    )
    environment_names: Optional[Sequence[str]] = Field(
        default=None, alias="EnvironmentNames"
    )
    include_deleted: Optional[bool] = Field(default=None, alias="IncludeDeleted")
    included_deleted_back_to: Optional[Union[datetime, str]] = Field(
        default=None, alias="IncludedDeletedBackTo"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class RetrieveEnvironmentInfoResultMessageModel(BaseModel):
    environment_info: List[EnvironmentInfoDescriptionModel] = Field(
        alias="EnvironmentInfo"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentResourceDescriptionModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    auto_scaling_groups: Optional[List[AutoScalingGroupModel]] = Field(
        default=None, alias="AutoScalingGroups"
    )
    instances: Optional[List[InstanceModel]] = Field(default=None, alias="Instances")
    launch_configurations: Optional[List[LaunchConfigurationModel]] = Field(
        default=None, alias="LaunchConfigurations"
    )
    launch_templates: Optional[List[LaunchTemplateModel]] = Field(
        default=None, alias="LaunchTemplates"
    )
    load_balancers: Optional[List[LoadBalancerModel]] = Field(
        default=None, alias="LoadBalancers"
    )
    triggers: Optional[List[TriggerModel]] = Field(default=None, alias="Triggers")
    queues: Optional[List[QueueModel]] = Field(default=None, alias="Queues")


class EventDescriptionsMessageModel(BaseModel):
    events: List[EventDescriptionModel] = Field(alias="Events")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAvailableSolutionStacksResultMessageModel(BaseModel):
    solution_stacks: List[str] = Field(alias="SolutionStacks")
    solution_stack_details: List[SolutionStackDescriptionModel] = Field(
        alias="SolutionStackDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPlatformBranchesRequestModel(BaseModel):
    filters: Optional[Sequence[SearchFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPlatformBranchesResultModel(BaseModel):
    platform_branch_summary_list: List[PlatformBranchSummaryModel] = Field(
        alias="PlatformBranchSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPlatformVersionsRequestListPlatformVersionsPaginateModel(BaseModel):
    filters: Optional[Sequence[PlatformFilterModel]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPlatformVersionsRequestModel(BaseModel):
    filters: Optional[Sequence[PlatformFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_records: Optional[int] = Field(default=None, alias="MaxRecords")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class LoadBalancerDescriptionModel(BaseModel):
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    domain: Optional[str] = Field(default=None, alias="Domain")
    listeners: Optional[List[ListenerModel]] = Field(default=None, alias="Listeners")


class PlatformDescriptionModel(BaseModel):
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    platform_owner: Optional[str] = Field(default=None, alias="PlatformOwner")
    platform_name: Optional[str] = Field(default=None, alias="PlatformName")
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    platform_status: Optional[
        Literal["Creating", "Deleted", "Deleting", "Failed", "Ready"]
    ] = Field(default=None, alias="PlatformStatus")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_updated: Optional[datetime] = Field(default=None, alias="DateUpdated")
    platform_category: Optional[str] = Field(default=None, alias="PlatformCategory")
    description: Optional[str] = Field(default=None, alias="Description")
    maintainer: Optional[str] = Field(default=None, alias="Maintainer")
    operating_system_name: Optional[str] = Field(
        default=None, alias="OperatingSystemName"
    )
    operating_system_version: Optional[str] = Field(
        default=None, alias="OperatingSystemVersion"
    )
    programming_languages: Optional[List[PlatformProgrammingLanguageModel]] = Field(
        default=None, alias="ProgrammingLanguages"
    )
    frameworks: Optional[List[PlatformFrameworkModel]] = Field(
        default=None, alias="Frameworks"
    )
    custom_ami_list: Optional[List[CustomAmiModel]] = Field(
        default=None, alias="CustomAmiList"
    )
    supported_tier_list: Optional[List[str]] = Field(
        default=None, alias="SupportedTierList"
    )
    supported_addon_list: Optional[List[str]] = Field(
        default=None, alias="SupportedAddonList"
    )
    platform_lifecycle_state: Optional[str] = Field(
        default=None, alias="PlatformLifecycleState"
    )
    platform_branch_name: Optional[str] = Field(
        default=None, alias="PlatformBranchName"
    )
    platform_branch_lifecycle_state: Optional[str] = Field(
        default=None, alias="PlatformBranchLifecycleState"
    )


class ResourceQuotasModel(BaseModel):
    application_quota: Optional[ResourceQuotaModel] = Field(
        default=None, alias="ApplicationQuota"
    )
    application_version_quota: Optional[ResourceQuotaModel] = Field(
        default=None, alias="ApplicationVersionQuota"
    )
    environment_quota: Optional[ResourceQuotaModel] = Field(
        default=None, alias="EnvironmentQuota"
    )
    configuration_template_quota: Optional[ResourceQuotaModel] = Field(
        default=None, alias="ConfigurationTemplateQuota"
    )
    custom_platform_quota: Optional[ResourceQuotaModel] = Field(
        default=None, alias="CustomPlatformQuota"
    )


class DescribeEnvironmentHealthResultModel(BaseModel):
    environment_name: str = Field(alias="EnvironmentName")
    health_status: str = Field(alias="HealthStatus")
    status: Literal["Green", "Grey", "Red", "Yellow"] = Field(alias="Status")
    color: str = Field(alias="Color")
    causes: List[str] = Field(alias="Causes")
    application_metrics: ApplicationMetricsModel = Field(alias="ApplicationMetrics")
    instances_health: InstanceHealthSummaryModel = Field(alias="InstancesHealth")
    refreshed_at: datetime = Field(alias="RefreshedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplicationVersionDescriptionMessageModel(BaseModel):
    application_version: ApplicationVersionDescriptionModel = Field(
        alias="ApplicationVersion"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplicationVersionDescriptionsMessageModel(BaseModel):
    application_versions: List[ApplicationVersionDescriptionModel] = Field(
        alias="ApplicationVersions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplicationResourceLifecycleConfigModel(BaseModel):
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    version_lifecycle_config: Optional[ApplicationVersionLifecycleConfigModel] = Field(
        default=None, alias="VersionLifecycleConfig"
    )


class SingleInstanceHealthModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    health_status: Optional[str] = Field(default=None, alias="HealthStatus")
    color: Optional[str] = Field(default=None, alias="Color")
    causes: Optional[List[str]] = Field(default=None, alias="Causes")
    launched_at: Optional[datetime] = Field(default=None, alias="LaunchedAt")
    application_metrics: Optional[ApplicationMetricsModel] = Field(
        default=None, alias="ApplicationMetrics"
    )
    system: Optional[SystemStatusModel] = Field(default=None, alias="System")
    deployment: Optional[DeploymentModel] = Field(default=None, alias="Deployment")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")


class ConfigurationOptionsDescriptionModel(BaseModel):
    solution_stack_name: str = Field(alias="SolutionStackName")
    platform_arn: str = Field(alias="PlatformArn")
    options: List[ConfigurationOptionDescriptionModel] = Field(alias="Options")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationSettingsDescriptionsModel(BaseModel):
    configuration_settings: List[ConfigurationSettingsDescriptionModel] = Field(
        alias="ConfigurationSettings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentResourceDescriptionsMessageModel(BaseModel):
    environment_resources: EnvironmentResourceDescriptionModel = Field(
        alias="EnvironmentResources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentResourcesDescriptionModel(BaseModel):
    load_balancer: Optional[LoadBalancerDescriptionModel] = Field(
        default=None, alias="LoadBalancer"
    )


class DescribePlatformVersionResultModel(BaseModel):
    platform_description: PlatformDescriptionModel = Field(alias="PlatformDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountAttributesResultModel(BaseModel):
    resource_quotas: ResourceQuotasModel = Field(alias="ResourceQuotas")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplicationDescriptionModel(BaseModel):
    application_arn: Optional[str] = Field(default=None, alias="ApplicationArn")
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    description: Optional[str] = Field(default=None, alias="Description")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_updated: Optional[datetime] = Field(default=None, alias="DateUpdated")
    versions: Optional[List[str]] = Field(default=None, alias="Versions")
    configuration_templates: Optional[List[str]] = Field(
        default=None, alias="ConfigurationTemplates"
    )
    resource_lifecycle_config: Optional[
        ApplicationResourceLifecycleConfigModel
    ] = Field(default=None, alias="ResourceLifecycleConfig")


class ApplicationResourceLifecycleDescriptionMessageModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    resource_lifecycle_config: ApplicationResourceLifecycleConfigModel = Field(
        alias="ResourceLifecycleConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    description: Optional[str] = Field(default=None, alias="Description")
    resource_lifecycle_config: Optional[
        ApplicationResourceLifecycleConfigModel
    ] = Field(default=None, alias="ResourceLifecycleConfig")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateApplicationResourceLifecycleMessageRequestModel(BaseModel):
    application_name: str = Field(alias="ApplicationName")
    resource_lifecycle_config: ApplicationResourceLifecycleConfigModel = Field(
        alias="ResourceLifecycleConfig"
    )


class DescribeInstancesHealthResultModel(BaseModel):
    instance_health_list: List[SingleInstanceHealthModel] = Field(
        alias="InstanceHealthList"
    )
    refreshed_at: datetime = Field(alias="RefreshedAt")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentDescriptionResponseMetadataModel(BaseModel):
    environment_name: str = Field(alias="EnvironmentName")
    environment_id: str = Field(alias="EnvironmentId")
    application_name: str = Field(alias="ApplicationName")
    version_label: str = Field(alias="VersionLabel")
    solution_stack_name: str = Field(alias="SolutionStackName")
    platform_arn: str = Field(alias="PlatformArn")
    template_name: str = Field(alias="TemplateName")
    description: str = Field(alias="Description")
    endpoint_url: str = Field(alias="EndpointURL")
    cname: str = Field(alias="CNAME")
    date_created: datetime = Field(alias="DateCreated")
    date_updated: datetime = Field(alias="DateUpdated")
    status: Literal[
        "Aborting",
        "Launching",
        "LinkingFrom",
        "LinkingTo",
        "Ready",
        "Terminated",
        "Terminating",
        "Updating",
    ] = Field(alias="Status")
    abortable_operation_in_progress: bool = Field(alias="AbortableOperationInProgress")
    health: Literal["Green", "Grey", "Red", "Yellow"] = Field(alias="Health")
    health_status: Literal[
        "Degraded",
        "Info",
        "NoData",
        "Ok",
        "Pending",
        "Severe",
        "Suspended",
        "Unknown",
        "Warning",
    ] = Field(alias="HealthStatus")
    resources: EnvironmentResourcesDescriptionModel = Field(alias="Resources")
    tier: EnvironmentTierModel = Field(alias="Tier")
    environment_links: List[EnvironmentLinkModel] = Field(alias="EnvironmentLinks")
    environment_arn: str = Field(alias="EnvironmentArn")
    operations_role: str = Field(alias="OperationsRole")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentDescriptionModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    template_name: Optional[str] = Field(default=None, alias="TemplateName")
    description: Optional[str] = Field(default=None, alias="Description")
    endpoint_url: Optional[str] = Field(default=None, alias="EndpointURL")
    cname: Optional[str] = Field(default=None, alias="CNAME")
    date_created: Optional[datetime] = Field(default=None, alias="DateCreated")
    date_updated: Optional[datetime] = Field(default=None, alias="DateUpdated")
    status: Optional[
        Literal[
            "Aborting",
            "Launching",
            "LinkingFrom",
            "LinkingTo",
            "Ready",
            "Terminated",
            "Terminating",
            "Updating",
        ]
    ] = Field(default=None, alias="Status")
    abortable_operation_in_progress: Optional[bool] = Field(
        default=None, alias="AbortableOperationInProgress"
    )
    health: Optional[Literal["Green", "Grey", "Red", "Yellow"]] = Field(
        default=None, alias="Health"
    )
    health_status: Optional[
        Literal[
            "Degraded",
            "Info",
            "NoData",
            "Ok",
            "Pending",
            "Severe",
            "Suspended",
            "Unknown",
            "Warning",
        ]
    ] = Field(default=None, alias="HealthStatus")
    resources: Optional[EnvironmentResourcesDescriptionModel] = Field(
        default=None, alias="Resources"
    )
    tier: Optional[EnvironmentTierModel] = Field(default=None, alias="Tier")
    environment_links: Optional[List[EnvironmentLinkModel]] = Field(
        default=None, alias="EnvironmentLinks"
    )
    environment_arn: Optional[str] = Field(default=None, alias="EnvironmentArn")
    operations_role: Optional[str] = Field(default=None, alias="OperationsRole")


class ApplicationDescriptionMessageModel(BaseModel):
    application: ApplicationDescriptionModel = Field(alias="Application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplicationDescriptionsMessageModel(BaseModel):
    applications: List[ApplicationDescriptionModel] = Field(alias="Applications")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentDescriptionsMessageModel(BaseModel):
    environments: List[EnvironmentDescriptionModel] = Field(alias="Environments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
