# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ApplicationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    args: Optional[List[str]] = Field(default=None, alias="Args")
    additional_info: Optional[Dict[str, str]] = Field(
        default=None, alias="AdditionalInfo"
    )


class ScalingConstraintsModel(BaseModel):
    min_capacity: int = Field(alias="MinCapacity")
    max_capacity: int = Field(alias="MaxCapacity")


class AutoScalingPolicyStateChangeReasonModel(BaseModel):
    code: Optional[
        Literal["CLEANUP_FAILURE", "PROVISION_FAILURE", "USER_REQUEST"]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class AutoTerminationPolicyModel(BaseModel):
    idle_timeout: Optional[int] = Field(default=None, alias="IdleTimeout")


class BlockPublicAccessConfigurationMetadataModel(BaseModel):
    creation_date_time: datetime = Field(alias="CreationDateTime")
    created_by_arn: str = Field(alias="CreatedByArn")


class PortRangeModel(BaseModel):
    min_range: int = Field(alias="MinRange")
    max_range: Optional[int] = Field(default=None, alias="MaxRange")


class ScriptBootstrapActionConfigModel(BaseModel):
    path: str = Field(alias="Path")
    args: Optional[List[str]] = Field(default=None, alias="Args")


class CancelStepsInfoModel(BaseModel):
    step_id: Optional[str] = Field(default=None, alias="StepId")
    status: Optional[Literal["FAILED", "SUBMITTED"]] = Field(
        default=None, alias="Status"
    )
    reason: Optional[str] = Field(default=None, alias="Reason")


class CancelStepsInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    step_ids: Sequence[str] = Field(alias="StepIds")
    step_cancellation_option: Optional[
        Literal["SEND_INTERRUPT", "TERMINATE_PROCESS"]
    ] = Field(default=None, alias="StepCancellationOption")


class MetricDimensionModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ClusterStateChangeReasonModel(BaseModel):
    code: Optional[
        Literal[
            "ALL_STEPS_COMPLETED",
            "BOOTSTRAP_FAILURE",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "INTERNAL_ERROR",
            "STEP_FAILURE",
            "USER_REQUEST",
            "VALIDATION_ERROR",
        ]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class ClusterTimelineModel(BaseModel):
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    ready_date_time: Optional[datetime] = Field(default=None, alias="ReadyDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")


class Ec2InstanceAttributesModel(BaseModel):
    ec2_key_name: Optional[str] = Field(default=None, alias="Ec2KeyName")
    ec2_subnet_id: Optional[str] = Field(default=None, alias="Ec2SubnetId")
    requested_ec2_subnet_ids: Optional[List[str]] = Field(
        default=None, alias="RequestedEc2SubnetIds"
    )
    ec2_availability_zone: Optional[str] = Field(
        default=None, alias="Ec2AvailabilityZone"
    )
    requested_ec2_availability_zones: Optional[List[str]] = Field(
        default=None, alias="RequestedEc2AvailabilityZones"
    )
    iam_instance_profile: Optional[str] = Field(
        default=None, alias="IamInstanceProfile"
    )
    emr_managed_master_security_group: Optional[str] = Field(
        default=None, alias="EmrManagedMasterSecurityGroup"
    )
    emr_managed_slave_security_group: Optional[str] = Field(
        default=None, alias="EmrManagedSlaveSecurityGroup"
    )
    service_access_security_group: Optional[str] = Field(
        default=None, alias="ServiceAccessSecurityGroup"
    )
    additional_master_security_groups: Optional[List[str]] = Field(
        default=None, alias="AdditionalMasterSecurityGroups"
    )
    additional_slave_security_groups: Optional[List[str]] = Field(
        default=None, alias="AdditionalSlaveSecurityGroups"
    )


class KerberosAttributesModel(BaseModel):
    realm: str = Field(alias="Realm")
    kdc_admin_password: str = Field(alias="KdcAdminPassword")
    cross_realm_trust_principal_password: Optional[str] = Field(
        default=None, alias="CrossRealmTrustPrincipalPassword"
    )
    addomain_join_user: Optional[str] = Field(default=None, alias="ADDomainJoinUser")
    addomain_join_password: Optional[str] = Field(
        default=None, alias="ADDomainJoinPassword"
    )


class PlacementGroupConfigModel(BaseModel):
    instance_role: Literal["CORE", "MASTER", "TASK"] = Field(alias="InstanceRole")
    placement_strategy: Optional[
        Literal["CLUSTER", "NONE", "PARTITION", "SPREAD"]
    ] = Field(default=None, alias="PlacementStrategy")


class CommandModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    script_path: Optional[str] = Field(default=None, alias="ScriptPath")
    args: Optional[List[str]] = Field(default=None, alias="Args")


class ComputeLimitsModel(BaseModel):
    unit_type: Literal["InstanceFleetUnits", "Instances", "VCPU"] = Field(
        alias="UnitType"
    )
    minimum_capacity_units: int = Field(alias="MinimumCapacityUnits")
    maximum_capacity_units: int = Field(alias="MaximumCapacityUnits")
    maximum_on_demand_capacity_units: Optional[int] = Field(
        default=None, alias="MaximumOnDemandCapacityUnits"
    )
    maximum_core_capacity_units: Optional[int] = Field(
        default=None, alias="MaximumCoreCapacityUnits"
    )


class ConfigurationModel(BaseModel):
    classification: Optional[str] = Field(default=None, alias="Classification")
    configurations: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="Configurations"
    )
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="Properties")


class CreateSecurityConfigurationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    security_configuration: str = Field(alias="SecurityConfiguration")


class CreateStudioSessionMappingInputRequestModel(BaseModel):
    studio_id: str = Field(alias="StudioId")
    identity_type: Literal["GROUP", "USER"] = Field(alias="IdentityType")
    session_policy_arn: str = Field(alias="SessionPolicyArn")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")


class UsernamePasswordModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    password: Optional[str] = Field(default=None, alias="Password")


class DeleteSecurityConfigurationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteStudioInputRequestModel(BaseModel):
    studio_id: str = Field(alias="StudioId")


class DeleteStudioSessionMappingInputRequestModel(BaseModel):
    studio_id: str = Field(alias="StudioId")
    identity_type: Literal["GROUP", "USER"] = Field(alias="IdentityType")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeClusterInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class DescribeJobFlowsInputRequestModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    job_flow_ids: Optional[Sequence[str]] = Field(default=None, alias="JobFlowIds")
    job_flow_states: Optional[
        Sequence[
            Literal[
                "BOOTSTRAPPING",
                "COMPLETED",
                "FAILED",
                "RUNNING",
                "SHUTTING_DOWN",
                "STARTING",
                "TERMINATED",
                "WAITING",
            ]
        ]
    ] = Field(default=None, alias="JobFlowStates")


class DescribeNotebookExecutionInputRequestModel(BaseModel):
    notebook_execution_id: str = Field(alias="NotebookExecutionId")


class DescribeReleaseLabelInputRequestModel(BaseModel):
    release_label: Optional[str] = Field(default=None, alias="ReleaseLabel")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class OSReleaseModel(BaseModel):
    label: Optional[str] = Field(default=None, alias="Label")


class SimplifiedApplicationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class DescribeSecurityConfigurationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeStepInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    step_id: str = Field(alias="StepId")


class DescribeStudioInputRequestModel(BaseModel):
    studio_id: str = Field(alias="StudioId")


class VolumeSpecificationModel(BaseModel):
    volume_type: str = Field(alias="VolumeType")
    size_in_gb: int = Field(alias="SizeInGB")
    iops: Optional[int] = Field(default=None, alias="Iops")
    throughput: Optional[int] = Field(default=None, alias="Throughput")


class EbsVolumeModel(BaseModel):
    device: Optional[str] = Field(default=None, alias="Device")
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")


class ExecutionEngineConfigModel(BaseModel):
    id: str = Field(alias="Id")
    type: Optional[Literal["EMR"]] = Field(default=None, alias="Type")
    master_instance_security_group_id: Optional[str] = Field(
        default=None, alias="MasterInstanceSecurityGroupId"
    )


class FailureDetailsModel(BaseModel):
    reason: Optional[str] = Field(default=None, alias="Reason")
    message: Optional[str] = Field(default=None, alias="Message")
    log_file: Optional[str] = Field(default=None, alias="LogFile")


class GetAutoTerminationPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class GetClusterSessionCredentialsInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")


class GetManagedScalingPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class GetStudioSessionMappingInputRequestModel(BaseModel):
    studio_id: str = Field(alias="StudioId")
    identity_type: Literal["GROUP", "USER"] = Field(alias="IdentityType")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")


class SessionMappingDetailModel(BaseModel):
    studio_id: Optional[str] = Field(default=None, alias="StudioId")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")
    identity_type: Optional[Literal["GROUP", "USER"]] = Field(
        default=None, alias="IdentityType"
    )
    session_policy_arn: Optional[str] = Field(default=None, alias="SessionPolicyArn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class KeyValueModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class HadoopStepConfigModel(BaseModel):
    jar: Optional[str] = Field(default=None, alias="Jar")
    properties: Optional[Dict[str, str]] = Field(default=None, alias="Properties")
    main_class: Optional[str] = Field(default=None, alias="MainClass")
    args: Optional[List[str]] = Field(default=None, alias="Args")


class SpotProvisioningSpecificationModel(BaseModel):
    timeout_duration_minutes: int = Field(alias="TimeoutDurationMinutes")
    timeout_action: Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"] = Field(
        alias="TimeoutAction"
    )
    block_duration_minutes: Optional[int] = Field(
        default=None, alias="BlockDurationMinutes"
    )
    allocation_strategy: Optional[Literal["capacity-optimized"]] = Field(
        default=None, alias="AllocationStrategy"
    )


class OnDemandResizingSpecificationModel(BaseModel):
    timeout_duration_minutes: int = Field(alias="TimeoutDurationMinutes")


class SpotResizingSpecificationModel(BaseModel):
    timeout_duration_minutes: int = Field(alias="TimeoutDurationMinutes")


class InstanceFleetStateChangeReasonModel(BaseModel):
    code: Optional[
        Literal[
            "CLUSTER_TERMINATED",
            "INSTANCE_FAILURE",
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
        ]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class InstanceFleetTimelineModel(BaseModel):
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    ready_date_time: Optional[datetime] = Field(default=None, alias="ReadyDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")


class InstanceGroupDetailModel(BaseModel):
    market: Literal["ON_DEMAND", "SPOT"] = Field(alias="Market")
    instance_role: Literal["CORE", "MASTER", "TASK"] = Field(alias="InstanceRole")
    instance_type: str = Field(alias="InstanceType")
    instance_request_count: int = Field(alias="InstanceRequestCount")
    instance_running_count: int = Field(alias="InstanceRunningCount")
    state: Literal[
        "ARRESTED",
        "BOOTSTRAPPING",
        "ENDED",
        "PROVISIONING",
        "RECONFIGURING",
        "RESIZING",
        "RUNNING",
        "SHUTTING_DOWN",
        "SUSPENDED",
        "TERMINATED",
        "TERMINATING",
    ] = Field(alias="State")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    instance_group_id: Optional[str] = Field(default=None, alias="InstanceGroupId")
    name: Optional[str] = Field(default=None, alias="Name")
    bid_price: Optional[str] = Field(default=None, alias="BidPrice")
    last_state_change_reason: Optional[str] = Field(
        default=None, alias="LastStateChangeReason"
    )
    start_date_time: Optional[datetime] = Field(default=None, alias="StartDateTime")
    ready_date_time: Optional[datetime] = Field(default=None, alias="ReadyDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")
    custom_ami_id: Optional[str] = Field(default=None, alias="CustomAmiId")


class InstanceGroupStateChangeReasonModel(BaseModel):
    code: Optional[
        Literal[
            "CLUSTER_TERMINATED",
            "INSTANCE_FAILURE",
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
        ]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class InstanceGroupTimelineModel(BaseModel):
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    ready_date_time: Optional[datetime] = Field(default=None, alias="ReadyDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")


class InstanceResizePolicyModel(BaseModel):
    instances_to_terminate: Optional[List[str]] = Field(
        default=None, alias="InstancesToTerminate"
    )
    instances_to_protect: Optional[List[str]] = Field(
        default=None, alias="InstancesToProtect"
    )
    instance_termination_timeout: Optional[int] = Field(
        default=None, alias="InstanceTerminationTimeout"
    )


class InstanceStateChangeReasonModel(BaseModel):
    code: Optional[
        Literal[
            "BOOTSTRAP_FAILURE",
            "CLUSTER_TERMINATED",
            "INSTANCE_FAILURE",
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
        ]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class InstanceTimelineModel(BaseModel):
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    ready_date_time: Optional[datetime] = Field(default=None, alias="ReadyDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")


class JobFlowExecutionStatusDetailModel(BaseModel):
    state: Literal[
        "BOOTSTRAPPING",
        "COMPLETED",
        "FAILED",
        "RUNNING",
        "SHUTTING_DOWN",
        "STARTING",
        "TERMINATED",
        "WAITING",
    ] = Field(alias="State")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    start_date_time: Optional[datetime] = Field(default=None, alias="StartDateTime")
    ready_date_time: Optional[datetime] = Field(default=None, alias="ReadyDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")
    last_state_change_reason: Optional[str] = Field(
        default=None, alias="LastStateChangeReason"
    )


class PlacementTypeModel(BaseModel):
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBootstrapActionsInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListClustersInputRequestModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    cluster_states: Optional[
        Sequence[
            Literal[
                "BOOTSTRAPPING",
                "RUNNING",
                "STARTING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
                "TERMINATING",
                "WAITING",
            ]
        ]
    ] = Field(default=None, alias="ClusterStates")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListInstanceFleetsInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListInstanceGroupsInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListInstancesInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_group_id: Optional[str] = Field(default=None, alias="InstanceGroupId")
    instance_group_types: Optional[Sequence[Literal["CORE", "MASTER", "TASK"]]] = Field(
        default=None, alias="InstanceGroupTypes"
    )
    instance_fleet_id: Optional[str] = Field(default=None, alias="InstanceFleetId")
    instance_fleet_type: Optional[Literal["CORE", "MASTER", "TASK"]] = Field(
        default=None, alias="InstanceFleetType"
    )
    instance_states: Optional[
        Sequence[
            Literal[
                "AWAITING_FULFILLMENT",
                "BOOTSTRAPPING",
                "PROVISIONING",
                "RUNNING",
                "TERMINATED",
            ]
        ]
    ] = Field(default=None, alias="InstanceStates")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListNotebookExecutionsInputRequestModel(BaseModel):
    editor_id: Optional[str] = Field(default=None, alias="EditorId")
    status: Optional[
        Literal[
            "FAILED",
            "FAILING",
            "FINISHED",
            "FINISHING",
            "RUNNING",
            "STARTING",
            "START_PENDING",
            "STOPPED",
            "STOPPING",
            "STOP_PENDING",
        ]
    ] = Field(default=None, alias="Status")
    from_: Optional[Union[datetime, str]] = Field(default=None, alias="From")
    to: Optional[Union[datetime, str]] = Field(default=None, alias="To")
    marker: Optional[str] = Field(default=None, alias="Marker")


class NotebookExecutionSummaryModel(BaseModel):
    notebook_execution_id: Optional[str] = Field(
        default=None, alias="NotebookExecutionId"
    )
    editor_id: Optional[str] = Field(default=None, alias="EditorId")
    notebook_execution_name: Optional[str] = Field(
        default=None, alias="NotebookExecutionName"
    )
    status: Optional[
        Literal[
            "FAILED",
            "FAILING",
            "FINISHED",
            "FINISHING",
            "RUNNING",
            "STARTING",
            "START_PENDING",
            "STOPPED",
            "STOPPING",
            "STOP_PENDING",
        ]
    ] = Field(default=None, alias="Status")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")


class ReleaseLabelFilterModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    application: Optional[str] = Field(default=None, alias="Application")


class ListSecurityConfigurationsInputRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")


class SecurityConfigurationSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )


class ListStepsInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    step_states: Optional[
        Sequence[
            Literal[
                "CANCELLED",
                "CANCEL_PENDING",
                "COMPLETED",
                "FAILED",
                "INTERRUPTED",
                "PENDING",
                "RUNNING",
            ]
        ]
    ] = Field(default=None, alias="StepStates")
    step_ids: Optional[Sequence[str]] = Field(default=None, alias="StepIds")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListStudioSessionMappingsInputRequestModel(BaseModel):
    studio_id: Optional[str] = Field(default=None, alias="StudioId")
    identity_type: Optional[Literal["GROUP", "USER"]] = Field(
        default=None, alias="IdentityType"
    )
    marker: Optional[str] = Field(default=None, alias="Marker")


class SessionMappingSummaryModel(BaseModel):
    studio_id: Optional[str] = Field(default=None, alias="StudioId")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")
    identity_type: Optional[Literal["GROUP", "USER"]] = Field(
        default=None, alias="IdentityType"
    )
    session_policy_arn: Optional[str] = Field(default=None, alias="SessionPolicyArn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class ListStudiosInputRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")


class StudioSummaryModel(BaseModel):
    studio_id: Optional[str] = Field(default=None, alias="StudioId")
    name: Optional[str] = Field(default=None, alias="Name")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    description: Optional[str] = Field(default=None, alias="Description")
    url: Optional[str] = Field(default=None, alias="Url")
    auth_mode: Optional[Literal["IAM", "SSO"]] = Field(default=None, alias="AuthMode")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class ModifyClusterInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    step_concurrency_level: Optional[int] = Field(
        default=None, alias="StepConcurrencyLevel"
    )


class OnDemandCapacityReservationOptionsModel(BaseModel):
    usage_strategy: Optional[Literal["use-capacity-reservations-first"]] = Field(
        default=None, alias="UsageStrategy"
    )
    capacity_reservation_preference: Optional[Literal["none", "open"]] = Field(
        default=None, alias="CapacityReservationPreference"
    )
    capacity_reservation_resource_group_arn: Optional[str] = Field(
        default=None, alias="CapacityReservationResourceGroupArn"
    )


class RemoveAutoScalingPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_group_id: str = Field(alias="InstanceGroupId")


class RemoveAutoTerminationPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class RemoveManagedScalingPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")


class RemoveTagsInputRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class SupportedProductConfigModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    args: Optional[Sequence[str]] = Field(default=None, alias="Args")


class SimpleScalingPolicyConfigurationModel(BaseModel):
    scaling_adjustment: int = Field(alias="ScalingAdjustment")
    adjustment_type: Optional[
        Literal["CHANGE_IN_CAPACITY", "EXACT_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY"]
    ] = Field(default=None, alias="AdjustmentType")
    cool_down: Optional[int] = Field(default=None, alias="CoolDown")


class SetTerminationProtectionInputRequestModel(BaseModel):
    job_flow_ids: Sequence[str] = Field(alias="JobFlowIds")
    termination_protected: bool = Field(alias="TerminationProtected")


class SetVisibleToAllUsersInputRequestModel(BaseModel):
    job_flow_ids: Sequence[str] = Field(alias="JobFlowIds")
    visible_to_all_users: bool = Field(alias="VisibleToAllUsers")


class StepExecutionStatusDetailModel(BaseModel):
    state: Literal[
        "CANCELLED",
        "COMPLETED",
        "CONTINUE",
        "FAILED",
        "INTERRUPTED",
        "PENDING",
        "RUNNING",
    ] = Field(alias="State")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    start_date_time: Optional[datetime] = Field(default=None, alias="StartDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")
    last_state_change_reason: Optional[str] = Field(
        default=None, alias="LastStateChangeReason"
    )


class StepStateChangeReasonModel(BaseModel):
    code: Optional[Literal["NONE"]] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class StepTimelineModel(BaseModel):
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )
    start_date_time: Optional[datetime] = Field(default=None, alias="StartDateTime")
    end_date_time: Optional[datetime] = Field(default=None, alias="EndDateTime")


class StopNotebookExecutionInputRequestModel(BaseModel):
    notebook_execution_id: str = Field(alias="NotebookExecutionId")


class TerminateJobFlowsInputRequestModel(BaseModel):
    job_flow_ids: Sequence[str] = Field(alias="JobFlowIds")


class UpdateStudioInputRequestModel(BaseModel):
    studio_id: str = Field(alias="StudioId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    default_s3_location: Optional[str] = Field(default=None, alias="DefaultS3Location")


class UpdateStudioSessionMappingInputRequestModel(BaseModel):
    studio_id: str = Field(alias="StudioId")
    identity_type: Literal["GROUP", "USER"] = Field(alias="IdentityType")
    session_policy_arn: str = Field(alias="SessionPolicyArn")
    identity_id: Optional[str] = Field(default=None, alias="IdentityId")
    identity_name: Optional[str] = Field(default=None, alias="IdentityName")


class AddInstanceFleetOutputModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_fleet_id: str = Field(alias="InstanceFleetId")
    cluster_arn: str = Field(alias="ClusterArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddInstanceGroupsOutputModel(BaseModel):
    job_flow_id: str = Field(alias="JobFlowId")
    instance_group_ids: List[str] = Field(alias="InstanceGroupIds")
    cluster_arn: str = Field(alias="ClusterArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddJobFlowStepsOutputModel(BaseModel):
    step_ids: List[str] = Field(alias="StepIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSecurityConfigurationOutputModel(BaseModel):
    name: str = Field(alias="Name")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStudioOutputModel(BaseModel):
    studio_id: str = Field(alias="StudioId")
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSecurityConfigurationOutputModel(BaseModel):
    name: str = Field(alias="Name")
    security_configuration: str = Field(alias="SecurityConfiguration")
    creation_date_time: datetime = Field(alias="CreationDateTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReleaseLabelsOutputModel(BaseModel):
    release_labels: List[str] = Field(alias="ReleaseLabels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ModifyClusterOutputModel(BaseModel):
    step_concurrency_level: int = Field(alias="StepConcurrencyLevel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunJobFlowOutputModel(BaseModel):
    job_flow_id: str = Field(alias="JobFlowId")
    cluster_arn: str = Field(alias="ClusterArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartNotebookExecutionOutputModel(BaseModel):
    notebook_execution_id: str = Field(alias="NotebookExecutionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddTagsInputRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateStudioInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    auth_mode: Literal["IAM", "SSO"] = Field(alias="AuthMode")
    vpc_id: str = Field(alias="VpcId")
    subnet_ids: Sequence[str] = Field(alias="SubnetIds")
    service_role: str = Field(alias="ServiceRole")
    workspace_security_group_id: str = Field(alias="WorkspaceSecurityGroupId")
    engine_security_group_id: str = Field(alias="EngineSecurityGroupId")
    default_s3_location: str = Field(alias="DefaultS3Location")
    description: Optional[str] = Field(default=None, alias="Description")
    user_role: Optional[str] = Field(default=None, alias="UserRole")
    idp_auth_url: Optional[str] = Field(default=None, alias="IdpAuthUrl")
    idp_relay_state_parameter_name: Optional[str] = Field(
        default=None, alias="IdpRelayStateParameterName"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class StudioModel(BaseModel):
    studio_id: Optional[str] = Field(default=None, alias="StudioId")
    studio_arn: Optional[str] = Field(default=None, alias="StudioArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    auth_mode: Optional[Literal["IAM", "SSO"]] = Field(default=None, alias="AuthMode")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    user_role: Optional[str] = Field(default=None, alias="UserRole")
    workspace_security_group_id: Optional[str] = Field(
        default=None, alias="WorkspaceSecurityGroupId"
    )
    engine_security_group_id: Optional[str] = Field(
        default=None, alias="EngineSecurityGroupId"
    )
    url: Optional[str] = Field(default=None, alias="Url")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    default_s3_location: Optional[str] = Field(default=None, alias="DefaultS3Location")
    idp_auth_url: Optional[str] = Field(default=None, alias="IdpAuthUrl")
    idp_relay_state_parameter_name: Optional[str] = Field(
        default=None, alias="IdpRelayStateParameterName"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class AutoScalingPolicyStatusModel(BaseModel):
    state: Optional[
        Literal["ATTACHED", "ATTACHING", "DETACHED", "DETACHING", "FAILED", "PENDING"]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[AutoScalingPolicyStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )


class GetAutoTerminationPolicyOutputModel(BaseModel):
    auto_termination_policy: AutoTerminationPolicyModel = Field(
        alias="AutoTerminationPolicy"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAutoTerminationPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    auto_termination_policy: Optional[AutoTerminationPolicyModel] = Field(
        default=None, alias="AutoTerminationPolicy"
    )


class BlockPublicAccessConfigurationModel(BaseModel):
    block_public_security_group_rules: bool = Field(
        alias="BlockPublicSecurityGroupRules"
    )
    permitted_public_security_group_rule_ranges: Optional[List[PortRangeModel]] = Field(
        default=None, alias="PermittedPublicSecurityGroupRuleRanges"
    )


class BootstrapActionConfigModel(BaseModel):
    name: str = Field(alias="Name")
    script_bootstrap_action: ScriptBootstrapActionConfigModel = Field(
        alias="ScriptBootstrapAction"
    )


class CancelStepsOutputModel(BaseModel):
    cancel_steps_info_list: List[CancelStepsInfoModel] = Field(
        alias="CancelStepsInfoList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CloudWatchAlarmDefinitionModel(BaseModel):
    comparison_operator: Literal[
        "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
    ] = Field(alias="ComparisonOperator")
    metric_name: str = Field(alias="MetricName")
    period: int = Field(alias="Period")
    threshold: float = Field(alias="Threshold")
    evaluation_periods: Optional[int] = Field(default=None, alias="EvaluationPeriods")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    statistic: Optional[
        Literal["AVERAGE", "MAXIMUM", "MINIMUM", "SAMPLE_COUNT", "SUM"]
    ] = Field(default=None, alias="Statistic")
    unit: Optional[
        Literal[
            "BITS",
            "BITS_PER_SECOND",
            "BYTES",
            "BYTES_PER_SECOND",
            "COUNT",
            "COUNT_PER_SECOND",
            "GIGA_BITS",
            "GIGA_BITS_PER_SECOND",
            "GIGA_BYTES",
            "GIGA_BYTES_PER_SECOND",
            "KILO_BITS",
            "KILO_BITS_PER_SECOND",
            "KILO_BYTES",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BITS",
            "MEGA_BITS_PER_SECOND",
            "MEGA_BYTES",
            "MEGA_BYTES_PER_SECOND",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "NONE",
            "PERCENT",
            "SECONDS",
            "TERA_BITS",
            "TERA_BITS_PER_SECOND",
            "TERA_BYTES",
            "TERA_BYTES_PER_SECOND",
        ]
    ] = Field(default=None, alias="Unit")
    dimensions: Optional[Sequence[MetricDimensionModel]] = Field(
        default=None, alias="Dimensions"
    )


class ClusterStatusModel(BaseModel):
    state: Optional[
        Literal[
            "BOOTSTRAPPING",
            "RUNNING",
            "STARTING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
            "TERMINATING",
            "WAITING",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[ClusterStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )
    timeline: Optional[ClusterTimelineModel] = Field(default=None, alias="Timeline")


class ListBootstrapActionsOutputModel(BaseModel):
    bootstrap_actions: List[CommandModel] = Field(alias="BootstrapActions")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ManagedScalingPolicyModel(BaseModel):
    compute_limits: Optional[ComputeLimitsModel] = Field(
        default=None, alias="ComputeLimits"
    )


class CredentialsModel(BaseModel):
    username_password: Optional[UsernamePasswordModel] = Field(
        default=None, alias="UsernamePassword"
    )


class DescribeClusterInputClusterRunningWaitModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeClusterInputClusterTerminatedWaitModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeStepInputStepCompleteWaitModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    step_id: str = Field(alias="StepId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeReleaseLabelOutputModel(BaseModel):
    release_label: str = Field(alias="ReleaseLabel")
    applications: List[SimplifiedApplicationModel] = Field(alias="Applications")
    next_token: str = Field(alias="NextToken")
    available_os_releases: List[OSReleaseModel] = Field(alias="AvailableOSReleases")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EbsBlockDeviceConfigModel(BaseModel):
    volume_specification: VolumeSpecificationModel = Field(alias="VolumeSpecification")
    volumes_per_instance: Optional[int] = Field(
        default=None, alias="VolumesPerInstance"
    )


class EbsBlockDeviceModel(BaseModel):
    volume_specification: Optional[VolumeSpecificationModel] = Field(
        default=None, alias="VolumeSpecification"
    )
    device: Optional[str] = Field(default=None, alias="Device")


class NotebookExecutionModel(BaseModel):
    notebook_execution_id: Optional[str] = Field(
        default=None, alias="NotebookExecutionId"
    )
    editor_id: Optional[str] = Field(default=None, alias="EditorId")
    execution_engine: Optional[ExecutionEngineConfigModel] = Field(
        default=None, alias="ExecutionEngine"
    )
    notebook_execution_name: Optional[str] = Field(
        default=None, alias="NotebookExecutionName"
    )
    notebook_params: Optional[str] = Field(default=None, alias="NotebookParams")
    status: Optional[
        Literal[
            "FAILED",
            "FAILING",
            "FINISHED",
            "FINISHING",
            "RUNNING",
            "STARTING",
            "START_PENDING",
            "STOPPED",
            "STOPPING",
            "STOP_PENDING",
        ]
    ] = Field(default=None, alias="Status")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    arn: Optional[str] = Field(default=None, alias="Arn")
    output_notebook_uri: Optional[str] = Field(default=None, alias="OutputNotebookURI")
    last_state_change_reason: Optional[str] = Field(
        default=None, alias="LastStateChangeReason"
    )
    notebook_instance_security_group_id: Optional[str] = Field(
        default=None, alias="NotebookInstanceSecurityGroupId"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class StartNotebookExecutionInputRequestModel(BaseModel):
    editor_id: str = Field(alias="EditorId")
    relative_path: str = Field(alias="RelativePath")
    execution_engine: ExecutionEngineConfigModel = Field(alias="ExecutionEngine")
    service_role: str = Field(alias="ServiceRole")
    notebook_execution_name: Optional[str] = Field(
        default=None, alias="NotebookExecutionName"
    )
    notebook_params: Optional[str] = Field(default=None, alias="NotebookParams")
    notebook_instance_security_group_id: Optional[str] = Field(
        default=None, alias="NotebookInstanceSecurityGroupId"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GetStudioSessionMappingOutputModel(BaseModel):
    session_mapping: SessionMappingDetailModel = Field(alias="SessionMapping")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HadoopJarStepConfigModel(BaseModel):
    jar: str = Field(alias="Jar")
    properties: Optional[Sequence[KeyValueModel]] = Field(
        default=None, alias="Properties"
    )
    main_class: Optional[str] = Field(default=None, alias="MainClass")
    args: Optional[Sequence[str]] = Field(default=None, alias="Args")


class InstanceFleetResizingSpecificationsModel(BaseModel):
    spot_resize_specification: Optional[SpotResizingSpecificationModel] = Field(
        default=None, alias="SpotResizeSpecification"
    )
    on_demand_resize_specification: Optional[
        OnDemandResizingSpecificationModel
    ] = Field(default=None, alias="OnDemandResizeSpecification")


class InstanceFleetStatusModel(BaseModel):
    state: Optional[
        Literal[
            "BOOTSTRAPPING",
            "PROVISIONING",
            "RESIZING",
            "RUNNING",
            "SUSPENDED",
            "TERMINATED",
            "TERMINATING",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[InstanceFleetStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )
    timeline: Optional[InstanceFleetTimelineModel] = Field(
        default=None, alias="Timeline"
    )


class InstanceGroupStatusModel(BaseModel):
    state: Optional[
        Literal[
            "ARRESTED",
            "BOOTSTRAPPING",
            "ENDED",
            "PROVISIONING",
            "RECONFIGURING",
            "RESIZING",
            "RUNNING",
            "SHUTTING_DOWN",
            "SUSPENDED",
            "TERMINATED",
            "TERMINATING",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[InstanceGroupStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )
    timeline: Optional[InstanceGroupTimelineModel] = Field(
        default=None, alias="Timeline"
    )


class ShrinkPolicyModel(BaseModel):
    decommission_timeout: Optional[int] = Field(
        default=None, alias="DecommissionTimeout"
    )
    instance_resize_policy: Optional[InstanceResizePolicyModel] = Field(
        default=None, alias="InstanceResizePolicy"
    )


class InstanceStatusModel(BaseModel):
    state: Optional[
        Literal[
            "AWAITING_FULFILLMENT",
            "BOOTSTRAPPING",
            "PROVISIONING",
            "RUNNING",
            "TERMINATED",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[InstanceStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )
    timeline: Optional[InstanceTimelineModel] = Field(default=None, alias="Timeline")


class JobFlowInstancesDetailModel(BaseModel):
    master_instance_type: str = Field(alias="MasterInstanceType")
    slave_instance_type: str = Field(alias="SlaveInstanceType")
    instance_count: int = Field(alias="InstanceCount")
    master_public_dns_name: Optional[str] = Field(
        default=None, alias="MasterPublicDnsName"
    )
    master_instance_id: Optional[str] = Field(default=None, alias="MasterInstanceId")
    instance_groups: Optional[List[InstanceGroupDetailModel]] = Field(
        default=None, alias="InstanceGroups"
    )
    normalized_instance_hours: Optional[int] = Field(
        default=None, alias="NormalizedInstanceHours"
    )
    ec2_key_name: Optional[str] = Field(default=None, alias="Ec2KeyName")
    ec2_subnet_id: Optional[str] = Field(default=None, alias="Ec2SubnetId")
    placement: Optional[PlacementTypeModel] = Field(default=None, alias="Placement")
    keep_job_flow_alive_when_no_steps: Optional[bool] = Field(
        default=None, alias="KeepJobFlowAliveWhenNoSteps"
    )
    termination_protected: Optional[bool] = Field(
        default=None, alias="TerminationProtected"
    )
    hadoop_version: Optional[str] = Field(default=None, alias="HadoopVersion")


class ListBootstrapActionsInputListBootstrapActionsPaginateModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersInputListClustersPaginateModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="CreatedBefore"
    )
    cluster_states: Optional[
        Sequence[
            Literal[
                "BOOTSTRAPPING",
                "RUNNING",
                "STARTING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
                "TERMINATING",
                "WAITING",
            ]
        ]
    ] = Field(default=None, alias="ClusterStates")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstanceFleetsInputListInstanceFleetsPaginateModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstanceGroupsInputListInstanceGroupsPaginateModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstancesInputListInstancesPaginateModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_group_id: Optional[str] = Field(default=None, alias="InstanceGroupId")
    instance_group_types: Optional[Sequence[Literal["CORE", "MASTER", "TASK"]]] = Field(
        default=None, alias="InstanceGroupTypes"
    )
    instance_fleet_id: Optional[str] = Field(default=None, alias="InstanceFleetId")
    instance_fleet_type: Optional[Literal["CORE", "MASTER", "TASK"]] = Field(
        default=None, alias="InstanceFleetType"
    )
    instance_states: Optional[
        Sequence[
            Literal[
                "AWAITING_FULFILLMENT",
                "BOOTSTRAPPING",
                "PROVISIONING",
                "RUNNING",
                "TERMINATED",
            ]
        ]
    ] = Field(default=None, alias="InstanceStates")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNotebookExecutionsInputListNotebookExecutionsPaginateModel(BaseModel):
    editor_id: Optional[str] = Field(default=None, alias="EditorId")
    status: Optional[
        Literal[
            "FAILED",
            "FAILING",
            "FINISHED",
            "FINISHING",
            "RUNNING",
            "STARTING",
            "START_PENDING",
            "STOPPED",
            "STOPPING",
            "STOP_PENDING",
        ]
    ] = Field(default=None, alias="Status")
    from_: Optional[Union[datetime, str]] = Field(default=None, alias="From")
    to: Optional[Union[datetime, str]] = Field(default=None, alias="To")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityConfigurationsInputListSecurityConfigurationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStepsInputListStepsPaginateModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    step_states: Optional[
        Sequence[
            Literal[
                "CANCELLED",
                "CANCEL_PENDING",
                "COMPLETED",
                "FAILED",
                "INTERRUPTED",
                "PENDING",
                "RUNNING",
            ]
        ]
    ] = Field(default=None, alias="StepStates")
    step_ids: Optional[Sequence[str]] = Field(default=None, alias="StepIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStudioSessionMappingsInputListStudioSessionMappingsPaginateModel(BaseModel):
    studio_id: Optional[str] = Field(default=None, alias="StudioId")
    identity_type: Optional[Literal["GROUP", "USER"]] = Field(
        default=None, alias="IdentityType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStudiosInputListStudiosPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNotebookExecutionsOutputModel(BaseModel):
    notebook_executions: List[NotebookExecutionSummaryModel] = Field(
        alias="NotebookExecutions"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReleaseLabelsInputRequestModel(BaseModel):
    filters: Optional[ReleaseLabelFilterModel] = Field(default=None, alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListSecurityConfigurationsOutputModel(BaseModel):
    security_configurations: List[SecurityConfigurationSummaryModel] = Field(
        alias="SecurityConfigurations"
    )
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStudioSessionMappingsOutputModel(BaseModel):
    session_mappings: List[SessionMappingSummaryModel] = Field(alias="SessionMappings")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStudiosOutputModel(BaseModel):
    studios: List[StudioSummaryModel] = Field(alias="Studios")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OnDemandProvisioningSpecificationModel(BaseModel):
    allocation_strategy: Literal["lowest-price"] = Field(alias="AllocationStrategy")
    capacity_reservation_options: Optional[
        OnDemandCapacityReservationOptionsModel
    ] = Field(default=None, alias="CapacityReservationOptions")


class ScalingActionModel(BaseModel):
    simple_scaling_policy_configuration: SimpleScalingPolicyConfigurationModel = Field(
        alias="SimpleScalingPolicyConfiguration"
    )
    market: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(default=None, alias="Market")


class StepStatusModel(BaseModel):
    state: Optional[
        Literal[
            "CANCELLED",
            "CANCEL_PENDING",
            "COMPLETED",
            "FAILED",
            "INTERRUPTED",
            "PENDING",
            "RUNNING",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[StepStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )
    failure_details: Optional[FailureDetailsModel] = Field(
        default=None, alias="FailureDetails"
    )
    timeline: Optional[StepTimelineModel] = Field(default=None, alias="Timeline")


class DescribeStudioOutputModel(BaseModel):
    studio: StudioModel = Field(alias="Studio")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBlockPublicAccessConfigurationOutputModel(BaseModel):
    block_public_access_configuration: BlockPublicAccessConfigurationModel = Field(
        alias="BlockPublicAccessConfiguration"
    )
    block_public_access_configuration_metadata: BlockPublicAccessConfigurationMetadataModel = Field(
        alias="BlockPublicAccessConfigurationMetadata"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutBlockPublicAccessConfigurationInputRequestModel(BaseModel):
    block_public_access_configuration: BlockPublicAccessConfigurationModel = Field(
        alias="BlockPublicAccessConfiguration"
    )


class BootstrapActionDetailModel(BaseModel):
    bootstrap_action_config: Optional[BootstrapActionConfigModel] = Field(
        default=None, alias="BootstrapActionConfig"
    )


class ScalingTriggerModel(BaseModel):
    cloud_watch_alarm_definition: CloudWatchAlarmDefinitionModel = Field(
        alias="CloudWatchAlarmDefinition"
    )


class ClusterSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[ClusterStatusModel] = Field(default=None, alias="Status")
    normalized_instance_hours: Optional[int] = Field(
        default=None, alias="NormalizedInstanceHours"
    )
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    outpost_arn: Optional[str] = Field(default=None, alias="OutpostArn")


class ClusterModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[ClusterStatusModel] = Field(default=None, alias="Status")
    ec2_instance_attributes: Optional[Ec2InstanceAttributesModel] = Field(
        default=None, alias="Ec2InstanceAttributes"
    )
    instance_collection_type: Optional[
        Literal["INSTANCE_FLEET", "INSTANCE_GROUP"]
    ] = Field(default=None, alias="InstanceCollectionType")
    log_uri: Optional[str] = Field(default=None, alias="LogUri")
    log_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="LogEncryptionKmsKeyId"
    )
    requested_ami_version: Optional[str] = Field(
        default=None, alias="RequestedAmiVersion"
    )
    running_ami_version: Optional[str] = Field(default=None, alias="RunningAmiVersion")
    release_label: Optional[str] = Field(default=None, alias="ReleaseLabel")
    auto_terminate: Optional[bool] = Field(default=None, alias="AutoTerminate")
    termination_protected: Optional[bool] = Field(
        default=None, alias="TerminationProtected"
    )
    visible_to_all_users: Optional[bool] = Field(
        default=None, alias="VisibleToAllUsers"
    )
    applications: Optional[List[ApplicationModel]] = Field(
        default=None, alias="Applications"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    normalized_instance_hours: Optional[int] = Field(
        default=None, alias="NormalizedInstanceHours"
    )
    master_public_dns_name: Optional[str] = Field(
        default=None, alias="MasterPublicDnsName"
    )
    configurations: Optional[List[ConfigurationModel]] = Field(
        default=None, alias="Configurations"
    )
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    auto_scaling_role: Optional[str] = Field(default=None, alias="AutoScalingRole")
    scale_down_behavior: Optional[
        Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"]
    ] = Field(default=None, alias="ScaleDownBehavior")
    custom_ami_id: Optional[str] = Field(default=None, alias="CustomAmiId")
    ebs_root_volume_size: Optional[int] = Field(default=None, alias="EbsRootVolumeSize")
    repo_upgrade_on_boot: Optional[Literal["NONE", "SECURITY"]] = Field(
        default=None, alias="RepoUpgradeOnBoot"
    )
    kerberos_attributes: Optional[KerberosAttributesModel] = Field(
        default=None, alias="KerberosAttributes"
    )
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    outpost_arn: Optional[str] = Field(default=None, alias="OutpostArn")
    step_concurrency_level: Optional[int] = Field(
        default=None, alias="StepConcurrencyLevel"
    )
    placement_groups: Optional[List[PlacementGroupConfigModel]] = Field(
        default=None, alias="PlacementGroups"
    )
    os_release_label: Optional[str] = Field(default=None, alias="OSReleaseLabel")


class GetManagedScalingPolicyOutputModel(BaseModel):
    managed_scaling_policy: ManagedScalingPolicyModel = Field(
        alias="ManagedScalingPolicy"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutManagedScalingPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    managed_scaling_policy: ManagedScalingPolicyModel = Field(
        alias="ManagedScalingPolicy"
    )


class GetClusterSessionCredentialsOutputModel(BaseModel):
    credentials: CredentialsModel = Field(alias="Credentials")
    expires_at: datetime = Field(alias="ExpiresAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EbsConfigurationModel(BaseModel):
    ebs_block_device_configs: Optional[Sequence[EbsBlockDeviceConfigModel]] = Field(
        default=None, alias="EbsBlockDeviceConfigs"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")


class InstanceTypeSpecificationModel(BaseModel):
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    weighted_capacity: Optional[int] = Field(default=None, alias="WeightedCapacity")
    bid_price: Optional[str] = Field(default=None, alias="BidPrice")
    bid_price_as_percentage_of_on_demand_price: Optional[float] = Field(
        default=None, alias="BidPriceAsPercentageOfOnDemandPrice"
    )
    configurations: Optional[List[ConfigurationModel]] = Field(
        default=None, alias="Configurations"
    )
    ebs_block_devices: Optional[List[EbsBlockDeviceModel]] = Field(
        default=None, alias="EbsBlockDevices"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    custom_ami_id: Optional[str] = Field(default=None, alias="CustomAmiId")


class DescribeNotebookExecutionOutputModel(BaseModel):
    notebook_execution: NotebookExecutionModel = Field(alias="NotebookExecution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StepConfigModel(BaseModel):
    name: str = Field(alias="Name")
    hadoop_jar_step: HadoopJarStepConfigModel = Field(alias="HadoopJarStep")
    action_on_failure: Optional[
        Literal[
            "CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_CLUSTER", "TERMINATE_JOB_FLOW"
        ]
    ] = Field(default=None, alias="ActionOnFailure")


class InstanceFleetModifyConfigModel(BaseModel):
    instance_fleet_id: str = Field(alias="InstanceFleetId")
    target_on_demand_capacity: Optional[int] = Field(
        default=None, alias="TargetOnDemandCapacity"
    )
    target_spot_capacity: Optional[int] = Field(
        default=None, alias="TargetSpotCapacity"
    )
    resize_specifications: Optional[InstanceFleetResizingSpecificationsModel] = Field(
        default=None, alias="ResizeSpecifications"
    )


class InstanceGroupModifyConfigModel(BaseModel):
    instance_group_id: str = Field(alias="InstanceGroupId")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    ec2_instance_ids_to_terminate: Optional[Sequence[str]] = Field(
        default=None, alias="EC2InstanceIdsToTerminate"
    )
    shrink_policy: Optional[ShrinkPolicyModel] = Field(
        default=None, alias="ShrinkPolicy"
    )
    reconfiguration_type: Optional[Literal["MERGE", "OVERWRITE"]] = Field(
        default=None, alias="ReconfigurationType"
    )
    configurations: Optional[Sequence[ConfigurationModel]] = Field(
        default=None, alias="Configurations"
    )


class InstanceModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    ec2_instance_id: Optional[str] = Field(default=None, alias="Ec2InstanceId")
    public_dns_name: Optional[str] = Field(default=None, alias="PublicDnsName")
    public_ip_address: Optional[str] = Field(default=None, alias="PublicIpAddress")
    private_dns_name: Optional[str] = Field(default=None, alias="PrivateDnsName")
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")
    status: Optional[InstanceStatusModel] = Field(default=None, alias="Status")
    instance_group_id: Optional[str] = Field(default=None, alias="InstanceGroupId")
    instance_fleet_id: Optional[str] = Field(default=None, alias="InstanceFleetId")
    market: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(default=None, alias="Market")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    ebs_volumes: Optional[List[EbsVolumeModel]] = Field(
        default=None, alias="EbsVolumes"
    )


class InstanceFleetProvisioningSpecificationsModel(BaseModel):
    spot_specification: Optional[SpotProvisioningSpecificationModel] = Field(
        default=None, alias="SpotSpecification"
    )
    on_demand_specification: Optional[OnDemandProvisioningSpecificationModel] = Field(
        default=None, alias="OnDemandSpecification"
    )


class StepSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    config: Optional[HadoopStepConfigModel] = Field(default=None, alias="Config")
    action_on_failure: Optional[
        Literal[
            "CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_CLUSTER", "TERMINATE_JOB_FLOW"
        ]
    ] = Field(default=None, alias="ActionOnFailure")
    status: Optional[StepStatusModel] = Field(default=None, alias="Status")


class StepModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    config: Optional[HadoopStepConfigModel] = Field(default=None, alias="Config")
    action_on_failure: Optional[
        Literal[
            "CANCEL_AND_WAIT", "CONTINUE", "TERMINATE_CLUSTER", "TERMINATE_JOB_FLOW"
        ]
    ] = Field(default=None, alias="ActionOnFailure")
    status: Optional[StepStatusModel] = Field(default=None, alias="Status")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")


class ScalingRuleModel(BaseModel):
    name: str = Field(alias="Name")
    action: ScalingActionModel = Field(alias="Action")
    trigger: ScalingTriggerModel = Field(alias="Trigger")
    description: Optional[str] = Field(default=None, alias="Description")


class ListClustersOutputModel(BaseModel):
    clusters: List[ClusterSummaryModel] = Field(alias="Clusters")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClusterOutputModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceTypeConfigModel(BaseModel):
    instance_type: str = Field(alias="InstanceType")
    weighted_capacity: Optional[int] = Field(default=None, alias="WeightedCapacity")
    bid_price: Optional[str] = Field(default=None, alias="BidPrice")
    bid_price_as_percentage_of_on_demand_price: Optional[float] = Field(
        default=None, alias="BidPriceAsPercentageOfOnDemandPrice"
    )
    ebs_configuration: Optional[EbsConfigurationModel] = Field(
        default=None, alias="EbsConfiguration"
    )
    configurations: Optional[Sequence[ConfigurationModel]] = Field(
        default=None, alias="Configurations"
    )
    custom_ami_id: Optional[str] = Field(default=None, alias="CustomAmiId")


class AddJobFlowStepsInputRequestModel(BaseModel):
    job_flow_id: str = Field(alias="JobFlowId")
    steps: Sequence[StepConfigModel] = Field(alias="Steps")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")


class StepDetailModel(BaseModel):
    step_config: StepConfigModel = Field(alias="StepConfig")
    execution_status_detail: StepExecutionStatusDetailModel = Field(
        alias="ExecutionStatusDetail"
    )


class ModifyInstanceFleetInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_fleet: InstanceFleetModifyConfigModel = Field(alias="InstanceFleet")


class ModifyInstanceGroupsInputRequestModel(BaseModel):
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")
    instance_groups: Optional[Sequence[InstanceGroupModifyConfigModel]] = Field(
        default=None, alias="InstanceGroups"
    )


class ListInstancesOutputModel(BaseModel):
    instances: List[InstanceModel] = Field(alias="Instances")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceFleetModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[InstanceFleetStatusModel] = Field(default=None, alias="Status")
    instance_fleet_type: Optional[Literal["CORE", "MASTER", "TASK"]] = Field(
        default=None, alias="InstanceFleetType"
    )
    target_on_demand_capacity: Optional[int] = Field(
        default=None, alias="TargetOnDemandCapacity"
    )
    target_spot_capacity: Optional[int] = Field(
        default=None, alias="TargetSpotCapacity"
    )
    provisioned_on_demand_capacity: Optional[int] = Field(
        default=None, alias="ProvisionedOnDemandCapacity"
    )
    provisioned_spot_capacity: Optional[int] = Field(
        default=None, alias="ProvisionedSpotCapacity"
    )
    instance_type_specifications: Optional[
        List[InstanceTypeSpecificationModel]
    ] = Field(default=None, alias="InstanceTypeSpecifications")
    launch_specifications: Optional[
        InstanceFleetProvisioningSpecificationsModel
    ] = Field(default=None, alias="LaunchSpecifications")
    resize_specifications: Optional[InstanceFleetResizingSpecificationsModel] = Field(
        default=None, alias="ResizeSpecifications"
    )


class ListStepsOutputModel(BaseModel):
    steps: List[StepSummaryModel] = Field(alias="Steps")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStepOutputModel(BaseModel):
    step: StepModel = Field(alias="Step")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoScalingPolicyDescriptionModel(BaseModel):
    status: Optional[AutoScalingPolicyStatusModel] = Field(default=None, alias="Status")
    constraints: Optional[ScalingConstraintsModel] = Field(
        default=None, alias="Constraints"
    )
    rules: Optional[List[ScalingRuleModel]] = Field(default=None, alias="Rules")


class AutoScalingPolicyModel(BaseModel):
    constraints: ScalingConstraintsModel = Field(alias="Constraints")
    rules: Sequence[ScalingRuleModel] = Field(alias="Rules")


class InstanceFleetConfigModel(BaseModel):
    instance_fleet_type: Literal["CORE", "MASTER", "TASK"] = Field(
        alias="InstanceFleetType"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    target_on_demand_capacity: Optional[int] = Field(
        default=None, alias="TargetOnDemandCapacity"
    )
    target_spot_capacity: Optional[int] = Field(
        default=None, alias="TargetSpotCapacity"
    )
    instance_type_configs: Optional[Sequence[InstanceTypeConfigModel]] = Field(
        default=None, alias="InstanceTypeConfigs"
    )
    launch_specifications: Optional[
        InstanceFleetProvisioningSpecificationsModel
    ] = Field(default=None, alias="LaunchSpecifications")
    resize_specifications: Optional[InstanceFleetResizingSpecificationsModel] = Field(
        default=None, alias="ResizeSpecifications"
    )


class JobFlowDetailModel(BaseModel):
    job_flow_id: str = Field(alias="JobFlowId")
    name: str = Field(alias="Name")
    execution_status_detail: JobFlowExecutionStatusDetailModel = Field(
        alias="ExecutionStatusDetail"
    )
    instances: JobFlowInstancesDetailModel = Field(alias="Instances")
    log_uri: Optional[str] = Field(default=None, alias="LogUri")
    log_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="LogEncryptionKmsKeyId"
    )
    ami_version: Optional[str] = Field(default=None, alias="AmiVersion")
    steps: Optional[List[StepDetailModel]] = Field(default=None, alias="Steps")
    bootstrap_actions: Optional[List[BootstrapActionDetailModel]] = Field(
        default=None, alias="BootstrapActions"
    )
    supported_products: Optional[List[str]] = Field(
        default=None, alias="SupportedProducts"
    )
    visible_to_all_users: Optional[bool] = Field(
        default=None, alias="VisibleToAllUsers"
    )
    job_flow_role: Optional[str] = Field(default=None, alias="JobFlowRole")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    auto_scaling_role: Optional[str] = Field(default=None, alias="AutoScalingRole")
    scale_down_behavior: Optional[
        Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"]
    ] = Field(default=None, alias="ScaleDownBehavior")


class ListInstanceFleetsOutputModel(BaseModel):
    instance_fleets: List[InstanceFleetModel] = Field(alias="InstanceFleets")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceGroupModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    market: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(default=None, alias="Market")
    instance_group_type: Optional[Literal["CORE", "MASTER", "TASK"]] = Field(
        default=None, alias="InstanceGroupType"
    )
    bid_price: Optional[str] = Field(default=None, alias="BidPrice")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    requested_instance_count: Optional[int] = Field(
        default=None, alias="RequestedInstanceCount"
    )
    running_instance_count: Optional[int] = Field(
        default=None, alias="RunningInstanceCount"
    )
    status: Optional[InstanceGroupStatusModel] = Field(default=None, alias="Status")
    configurations: Optional[List[ConfigurationModel]] = Field(
        default=None, alias="Configurations"
    )
    configurations_version: Optional[int] = Field(
        default=None, alias="ConfigurationsVersion"
    )
    last_successfully_applied_configurations: Optional[
        List[ConfigurationModel]
    ] = Field(default=None, alias="LastSuccessfullyAppliedConfigurations")
    last_successfully_applied_configurations_version: Optional[int] = Field(
        default=None, alias="LastSuccessfullyAppliedConfigurationsVersion"
    )
    ebs_block_devices: Optional[List[EbsBlockDeviceModel]] = Field(
        default=None, alias="EbsBlockDevices"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    shrink_policy: Optional[ShrinkPolicyModel] = Field(
        default=None, alias="ShrinkPolicy"
    )
    auto_scaling_policy: Optional[AutoScalingPolicyDescriptionModel] = Field(
        default=None, alias="AutoScalingPolicy"
    )
    custom_ami_id: Optional[str] = Field(default=None, alias="CustomAmiId")


class PutAutoScalingPolicyOutputModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_group_id: str = Field(alias="InstanceGroupId")
    auto_scaling_policy: AutoScalingPolicyDescriptionModel = Field(
        alias="AutoScalingPolicy"
    )
    cluster_arn: str = Field(alias="ClusterArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceGroupConfigModel(BaseModel):
    instance_role: Literal["CORE", "MASTER", "TASK"] = Field(alias="InstanceRole")
    instance_type: str = Field(alias="InstanceType")
    instance_count: int = Field(alias="InstanceCount")
    name: Optional[str] = Field(default=None, alias="Name")
    market: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(default=None, alias="Market")
    bid_price: Optional[str] = Field(default=None, alias="BidPrice")
    configurations: Optional[Sequence[ConfigurationModel]] = Field(
        default=None, alias="Configurations"
    )
    ebs_configuration: Optional[EbsConfigurationModel] = Field(
        default=None, alias="EbsConfiguration"
    )
    auto_scaling_policy: Optional[AutoScalingPolicyModel] = Field(
        default=None, alias="AutoScalingPolicy"
    )
    custom_ami_id: Optional[str] = Field(default=None, alias="CustomAmiId")


class PutAutoScalingPolicyInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_group_id: str = Field(alias="InstanceGroupId")
    auto_scaling_policy: AutoScalingPolicyModel = Field(alias="AutoScalingPolicy")


class AddInstanceFleetInputRequestModel(BaseModel):
    cluster_id: str = Field(alias="ClusterId")
    instance_fleet: InstanceFleetConfigModel = Field(alias="InstanceFleet")


class DescribeJobFlowsOutputModel(BaseModel):
    job_flows: List[JobFlowDetailModel] = Field(alias="JobFlows")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstanceGroupsOutputModel(BaseModel):
    instance_groups: List[InstanceGroupModel] = Field(alias="InstanceGroups")
    marker: str = Field(alias="Marker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AddInstanceGroupsInputRequestModel(BaseModel):
    instance_groups: Sequence[InstanceGroupConfigModel] = Field(alias="InstanceGroups")
    job_flow_id: str = Field(alias="JobFlowId")


class JobFlowInstancesConfigModel(BaseModel):
    master_instance_type: Optional[str] = Field(
        default=None, alias="MasterInstanceType"
    )
    slave_instance_type: Optional[str] = Field(default=None, alias="SlaveInstanceType")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    instance_groups: Optional[Sequence[InstanceGroupConfigModel]] = Field(
        default=None, alias="InstanceGroups"
    )
    instance_fleets: Optional[Sequence[InstanceFleetConfigModel]] = Field(
        default=None, alias="InstanceFleets"
    )
    ec2_key_name: Optional[str] = Field(default=None, alias="Ec2KeyName")
    placement: Optional[PlacementTypeModel] = Field(default=None, alias="Placement")
    keep_job_flow_alive_when_no_steps: Optional[bool] = Field(
        default=None, alias="KeepJobFlowAliveWhenNoSteps"
    )
    termination_protected: Optional[bool] = Field(
        default=None, alias="TerminationProtected"
    )
    hadoop_version: Optional[str] = Field(default=None, alias="HadoopVersion")
    ec2_subnet_id: Optional[str] = Field(default=None, alias="Ec2SubnetId")
    ec2_subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="Ec2SubnetIds")
    emr_managed_master_security_group: Optional[str] = Field(
        default=None, alias="EmrManagedMasterSecurityGroup"
    )
    emr_managed_slave_security_group: Optional[str] = Field(
        default=None, alias="EmrManagedSlaveSecurityGroup"
    )
    service_access_security_group: Optional[str] = Field(
        default=None, alias="ServiceAccessSecurityGroup"
    )
    additional_master_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalMasterSecurityGroups"
    )
    additional_slave_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalSlaveSecurityGroups"
    )


class RunJobFlowInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    instances: JobFlowInstancesConfigModel = Field(alias="Instances")
    log_uri: Optional[str] = Field(default=None, alias="LogUri")
    log_encryption_kms_key_id: Optional[str] = Field(
        default=None, alias="LogEncryptionKmsKeyId"
    )
    additional_info: Optional[str] = Field(default=None, alias="AdditionalInfo")
    ami_version: Optional[str] = Field(default=None, alias="AmiVersion")
    release_label: Optional[str] = Field(default=None, alias="ReleaseLabel")
    steps: Optional[Sequence[StepConfigModel]] = Field(default=None, alias="Steps")
    bootstrap_actions: Optional[Sequence[BootstrapActionConfigModel]] = Field(
        default=None, alias="BootstrapActions"
    )
    supported_products: Optional[Sequence[str]] = Field(
        default=None, alias="SupportedProducts"
    )
    new_supported_products: Optional[Sequence[SupportedProductConfigModel]] = Field(
        default=None, alias="NewSupportedProducts"
    )
    applications: Optional[Sequence[ApplicationModel]] = Field(
        default=None, alias="Applications"
    )
    configurations: Optional[Sequence[ConfigurationModel]] = Field(
        default=None, alias="Configurations"
    )
    visible_to_all_users: Optional[bool] = Field(
        default=None, alias="VisibleToAllUsers"
    )
    job_flow_role: Optional[str] = Field(default=None, alias="JobFlowRole")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    security_configuration: Optional[str] = Field(
        default=None, alias="SecurityConfiguration"
    )
    auto_scaling_role: Optional[str] = Field(default=None, alias="AutoScalingRole")
    scale_down_behavior: Optional[
        Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"]
    ] = Field(default=None, alias="ScaleDownBehavior")
    custom_ami_id: Optional[str] = Field(default=None, alias="CustomAmiId")
    ebs_root_volume_size: Optional[int] = Field(default=None, alias="EbsRootVolumeSize")
    repo_upgrade_on_boot: Optional[Literal["NONE", "SECURITY"]] = Field(
        default=None, alias="RepoUpgradeOnBoot"
    )
    kerberos_attributes: Optional[KerberosAttributesModel] = Field(
        default=None, alias="KerberosAttributes"
    )
    step_concurrency_level: Optional[int] = Field(
        default=None, alias="StepConcurrencyLevel"
    )
    managed_scaling_policy: Optional[ManagedScalingPolicyModel] = Field(
        default=None, alias="ManagedScalingPolicy"
    )
    placement_group_configs: Optional[Sequence[PlacementGroupConfigModel]] = Field(
        default=None, alias="PlacementGroupConfigs"
    )
    auto_termination_policy: Optional[AutoTerminationPolicyModel] = Field(
        default=None, alias="AutoTerminationPolicy"
    )
    os_release_label: Optional[str] = Field(default=None, alias="OSReleaseLabel")
