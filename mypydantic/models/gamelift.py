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


class AcceptMatchInputRequestModel(BaseModel):
    ticket_id: str = Field(alias="TicketId")
    player_ids: Sequence[str] = Field(alias="PlayerIds")
    acceptance_type: Literal["ACCEPT", "REJECT"] = Field(alias="AcceptanceType")


class RoutingStrategyModel(BaseModel):
    type: Optional[Literal["SIMPLE", "TERMINAL"]] = Field(default=None, alias="Type")
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    message: Optional[str] = Field(default=None, alias="Message")


class AnywhereConfigurationModel(BaseModel):
    cost: str = Field(alias="Cost")


class AttributeValueModel(BaseModel):
    s: Optional[str] = Field(default=None, alias="S")
    n: Optional[float] = Field(default=None, alias="N")
    s_l: Optional[List[str]] = Field(default=None, alias="SL")
    s_dm: Optional[Dict[str, float]] = Field(default=None, alias="SDM")


class AwsCredentialsModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="AccessKeyId")
    secret_access_key: Optional[str] = Field(default=None, alias="SecretAccessKey")
    session_token: Optional[str] = Field(default=None, alias="SessionToken")


class BuildModel(BaseModel):
    build_id: Optional[str] = Field(default=None, alias="BuildId")
    build_arn: Optional[str] = Field(default=None, alias="BuildArn")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    status: Optional[Literal["FAILED", "INITIALIZED", "READY"]] = Field(
        default=None, alias="Status"
    )
    size_on_disk: Optional[int] = Field(default=None, alias="SizeOnDisk")
    operating_system: Optional[
        Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
    ] = Field(default=None, alias="OperatingSystem")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    server_sdk_version: Optional[str] = Field(default=None, alias="ServerSdkVersion")


class CertificateConfigurationModel(BaseModel):
    certificate_type: Literal["DISABLED", "GENERATED"] = Field(alias="CertificateType")


class ClaimGameServerInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    game_server_id: Optional[str] = Field(default=None, alias="GameServerId")
    game_server_data: Optional[str] = Field(default=None, alias="GameServerData")


class GameServerModel(BaseModel):
    game_server_group_name: Optional[str] = Field(
        default=None, alias="GameServerGroupName"
    )
    game_server_group_arn: Optional[str] = Field(
        default=None, alias="GameServerGroupArn"
    )
    game_server_id: Optional[str] = Field(default=None, alias="GameServerId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    connection_info: Optional[str] = Field(default=None, alias="ConnectionInfo")
    game_server_data: Optional[str] = Field(default=None, alias="GameServerData")
    claim_status: Optional[Literal["CLAIMED"]] = Field(
        default=None, alias="ClaimStatus"
    )
    utilization_status: Optional[Literal["AVAILABLE", "UTILIZED"]] = Field(
        default=None, alias="UtilizationStatus"
    )
    registration_time: Optional[datetime] = Field(
        default=None, alias="RegistrationTime"
    )
    last_claim_time: Optional[datetime] = Field(default=None, alias="LastClaimTime")
    last_health_check_time: Optional[datetime] = Field(
        default=None, alias="LastHealthCheckTime"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ComputeModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    compute_name: Optional[str] = Field(default=None, alias="ComputeName")
    compute_arn: Optional[str] = Field(default=None, alias="ComputeArn")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    compute_status: Optional[Literal["ACTIVE", "PENDING", "TERMINATING"]] = Field(
        default=None, alias="ComputeStatus"
    )
    location: Optional[str] = Field(default=None, alias="Location")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    operating_system: Optional[
        Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
    ] = Field(default=None, alias="OperatingSystem")
    type: Optional[
        Literal[
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c3.large",
            "c3.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.large",
            "c5.xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.large",
            "c5a.xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c6a.12xlarge",
            "c6a.16xlarge",
            "c6a.24xlarge",
            "c6a.2xlarge",
            "c6a.4xlarge",
            "c6a.8xlarge",
            "c6a.large",
            "c6a.xlarge",
            "c6i.12xlarge",
            "c6i.16xlarge",
            "c6i.24xlarge",
            "c6i.2xlarge",
            "c6i.4xlarge",
            "c6i.8xlarge",
            "c6i.large",
            "c6i.xlarge",
            "m3.2xlarge",
            "m3.large",
            "m3.medium",
            "m3.xlarge",
            "m4.10xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.large",
            "m4.xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.large",
            "m5.xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.large",
            "m5a.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r4.16xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.large",
            "r5.xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.large",
            "r5a.xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.large",
            "r5d.xlarge",
            "t2.large",
            "t2.medium",
            "t2.micro",
            "t2.small",
        ]
    ] = Field(default=None, alias="Type")
    game_lift_service_sdk_endpoint: Optional[str] = Field(
        default=None, alias="GameLiftServiceSdkEndpoint"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class S3LocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    key: Optional[str] = Field(default=None, alias="Key")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    object_version: Optional[str] = Field(default=None, alias="ObjectVersion")


class IpPermissionModel(BaseModel):
    from_port: int = Field(alias="FromPort")
    to_port: int = Field(alias="ToPort")
    ip_range: str = Field(alias="IpRange")
    protocol: Literal["TCP", "UDP"] = Field(alias="Protocol")


class LocationConfigurationModel(BaseModel):
    location: str = Field(alias="Location")


class ResourceCreationLimitPolicyModel(BaseModel):
    new_game_sessions_per_creator: Optional[int] = Field(
        default=None, alias="NewGameSessionsPerCreator"
    )
    policy_period_in_minutes: Optional[int] = Field(
        default=None, alias="PolicyPeriodInMinutes"
    )


class LocationStateModel(BaseModel):
    location: Optional[str] = Field(default=None, alias="Location")
    status: Optional[
        Literal[
            "ACTIVATING",
            "ACTIVE",
            "BUILDING",
            "DELETING",
            "DOWNLOADING",
            "ERROR",
            "NEW",
            "NOT_FOUND",
            "TERMINATED",
            "VALIDATING",
        ]
    ] = Field(default=None, alias="Status")


class InstanceDefinitionModel(BaseModel):
    instance_type: Literal[
        "c4.2xlarge",
        "c4.4xlarge",
        "c4.8xlarge",
        "c4.large",
        "c4.xlarge",
        "c5.12xlarge",
        "c5.18xlarge",
        "c5.24xlarge",
        "c5.2xlarge",
        "c5.4xlarge",
        "c5.9xlarge",
        "c5.large",
        "c5.xlarge",
        "c5a.12xlarge",
        "c5a.16xlarge",
        "c5a.24xlarge",
        "c5a.2xlarge",
        "c5a.4xlarge",
        "c5a.8xlarge",
        "c5a.large",
        "c5a.xlarge",
        "c6g.12xlarge",
        "c6g.16xlarge",
        "c6g.2xlarge",
        "c6g.4xlarge",
        "c6g.8xlarge",
        "c6g.large",
        "c6g.medium",
        "c6g.xlarge",
        "m4.10xlarge",
        "m4.2xlarge",
        "m4.4xlarge",
        "m4.large",
        "m4.xlarge",
        "m5.12xlarge",
        "m5.16xlarge",
        "m5.24xlarge",
        "m5.2xlarge",
        "m5.4xlarge",
        "m5.8xlarge",
        "m5.large",
        "m5.xlarge",
        "m5a.12xlarge",
        "m5a.16xlarge",
        "m5a.24xlarge",
        "m5a.2xlarge",
        "m5a.4xlarge",
        "m5a.8xlarge",
        "m5a.large",
        "m5a.xlarge",
        "m6g.12xlarge",
        "m6g.16xlarge",
        "m6g.2xlarge",
        "m6g.4xlarge",
        "m6g.8xlarge",
        "m6g.large",
        "m6g.medium",
        "m6g.xlarge",
        "r4.16xlarge",
        "r4.2xlarge",
        "r4.4xlarge",
        "r4.8xlarge",
        "r4.large",
        "r4.xlarge",
        "r5.12xlarge",
        "r5.16xlarge",
        "r5.24xlarge",
        "r5.2xlarge",
        "r5.4xlarge",
        "r5.8xlarge",
        "r5.large",
        "r5.xlarge",
        "r5a.12xlarge",
        "r5a.16xlarge",
        "r5a.24xlarge",
        "r5a.2xlarge",
        "r5a.4xlarge",
        "r5a.8xlarge",
        "r5a.large",
        "r5a.xlarge",
        "r6g.12xlarge",
        "r6g.16xlarge",
        "r6g.2xlarge",
        "r6g.4xlarge",
        "r6g.8xlarge",
        "r6g.large",
        "r6g.medium",
        "r6g.xlarge",
    ] = Field(alias="InstanceType")
    weighted_capacity: Optional[str] = Field(default=None, alias="WeightedCapacity")


class LaunchTemplateSpecificationModel(BaseModel):
    launch_template_id: Optional[str] = Field(default=None, alias="LaunchTemplateId")
    launch_template_name: Optional[str] = Field(
        default=None, alias="LaunchTemplateName"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class GamePropertyModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class FilterConfigurationModel(BaseModel):
    allowed_locations: Optional[Sequence[str]] = Field(
        default=None, alias="AllowedLocations"
    )


class GameSessionQueueDestinationModel(BaseModel):
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")


class PlayerLatencyPolicyModel(BaseModel):
    maximum_individual_player_latency_milliseconds: Optional[int] = Field(
        default=None, alias="MaximumIndividualPlayerLatencyMilliseconds"
    )
    policy_duration_seconds: Optional[int] = Field(
        default=None, alias="PolicyDurationSeconds"
    )


class PriorityConfigurationModel(BaseModel):
    priority_order: Optional[
        Sequence[Literal["COST", "DESTINATION", "LATENCY", "LOCATION"]]
    ] = Field(default=None, alias="PriorityOrder")
    location_order: Optional[Sequence[str]] = Field(default=None, alias="LocationOrder")


class LocationModelModel(BaseModel):
    location_name: Optional[str] = Field(default=None, alias="LocationName")
    location_arn: Optional[str] = Field(default=None, alias="LocationArn")


class MatchmakingRuleSetModel(BaseModel):
    rule_set_body: str = Field(alias="RuleSetBody")
    rule_set_name: Optional[str] = Field(default=None, alias="RuleSetName")
    rule_set_arn: Optional[str] = Field(default=None, alias="RuleSetArn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class CreatePlayerSessionInputRequestModel(BaseModel):
    game_session_id: str = Field(alias="GameSessionId")
    player_id: str = Field(alias="PlayerId")
    player_data: Optional[str] = Field(default=None, alias="PlayerData")


class PlayerSessionModel(BaseModel):
    player_session_id: Optional[str] = Field(default=None, alias="PlayerSessionId")
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    termination_time: Optional[datetime] = Field(default=None, alias="TerminationTime")
    status: Optional[Literal["ACTIVE", "COMPLETED", "RESERVED", "TIMEDOUT"]] = Field(
        default=None, alias="Status"
    )
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    port: Optional[int] = Field(default=None, alias="Port")
    player_data: Optional[str] = Field(default=None, alias="PlayerData")


class CreatePlayerSessionsInputRequestModel(BaseModel):
    game_session_id: str = Field(alias="GameSessionId")
    player_ids: Sequence[str] = Field(alias="PlayerIds")
    player_data_map: Optional[Mapping[str, str]] = Field(
        default=None, alias="PlayerDataMap"
    )


class CreateVpcPeeringAuthorizationInputRequestModel(BaseModel):
    game_lift_aws_account_id: str = Field(alias="GameLiftAwsAccountId")
    peer_vpc_id: str = Field(alias="PeerVpcId")


class VpcPeeringAuthorizationModel(BaseModel):
    game_lift_aws_account_id: Optional[str] = Field(
        default=None, alias="GameLiftAwsAccountId"
    )
    peer_vpc_aws_account_id: Optional[str] = Field(
        default=None, alias="PeerVpcAwsAccountId"
    )
    peer_vpc_id: Optional[str] = Field(default=None, alias="PeerVpcId")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    expiration_time: Optional[datetime] = Field(default=None, alias="ExpirationTime")


class CreateVpcPeeringConnectionInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    peer_vpc_aws_account_id: str = Field(alias="PeerVpcAwsAccountId")
    peer_vpc_id: str = Field(alias="PeerVpcId")


class DeleteAliasInputRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")


class DeleteBuildInputRequestModel(BaseModel):
    build_id: str = Field(alias="BuildId")


class DeleteFleetInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")


class DeleteFleetLocationsInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    locations: Sequence[str] = Field(alias="Locations")


class DeleteGameServerGroupInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    delete_option: Optional[Literal["FORCE_DELETE", "RETAIN", "SAFE_DELETE"]] = Field(
        default=None, alias="DeleteOption"
    )


class DeleteGameSessionQueueInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteLocationInputRequestModel(BaseModel):
    location_name: str = Field(alias="LocationName")


class DeleteMatchmakingConfigurationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteMatchmakingRuleSetInputRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteScalingPolicyInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    fleet_id: str = Field(alias="FleetId")


class DeleteScriptInputRequestModel(BaseModel):
    script_id: str = Field(alias="ScriptId")


class DeleteVpcPeeringAuthorizationInputRequestModel(BaseModel):
    game_lift_aws_account_id: str = Field(alias="GameLiftAwsAccountId")
    peer_vpc_id: str = Field(alias="PeerVpcId")


class DeleteVpcPeeringConnectionInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    vpc_peering_connection_id: str = Field(alias="VpcPeeringConnectionId")


class DeregisterComputeInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    compute_name: str = Field(alias="ComputeName")


class DeregisterGameServerInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    game_server_id: str = Field(alias="GameServerId")


class DescribeAliasInputRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")


class DescribeBuildInputRequestModel(BaseModel):
    build_id: str = Field(alias="BuildId")


class DescribeComputeInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    compute_name: str = Field(alias="ComputeName")


class DescribeEC2InstanceLimitsInputRequestModel(BaseModel):
    ec2_instance_type: Optional[
        Literal[
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c3.large",
            "c3.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.large",
            "c5.xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.large",
            "c5a.xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c6a.12xlarge",
            "c6a.16xlarge",
            "c6a.24xlarge",
            "c6a.2xlarge",
            "c6a.4xlarge",
            "c6a.8xlarge",
            "c6a.large",
            "c6a.xlarge",
            "c6i.12xlarge",
            "c6i.16xlarge",
            "c6i.24xlarge",
            "c6i.2xlarge",
            "c6i.4xlarge",
            "c6i.8xlarge",
            "c6i.large",
            "c6i.xlarge",
            "m3.2xlarge",
            "m3.large",
            "m3.medium",
            "m3.xlarge",
            "m4.10xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.large",
            "m4.xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.large",
            "m5.xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.large",
            "m5a.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r4.16xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.large",
            "r5.xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.large",
            "r5a.xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.large",
            "r5d.xlarge",
            "t2.large",
            "t2.medium",
            "t2.micro",
            "t2.small",
        ]
    ] = Field(default=None, alias="EC2InstanceType")
    location: Optional[str] = Field(default=None, alias="Location")


class EC2InstanceLimitModel(BaseModel):
    ec2_instance_type: Optional[
        Literal[
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c3.large",
            "c3.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.large",
            "c5.xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.large",
            "c5a.xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c6a.12xlarge",
            "c6a.16xlarge",
            "c6a.24xlarge",
            "c6a.2xlarge",
            "c6a.4xlarge",
            "c6a.8xlarge",
            "c6a.large",
            "c6a.xlarge",
            "c6i.12xlarge",
            "c6i.16xlarge",
            "c6i.24xlarge",
            "c6i.2xlarge",
            "c6i.4xlarge",
            "c6i.8xlarge",
            "c6i.large",
            "c6i.xlarge",
            "m3.2xlarge",
            "m3.large",
            "m3.medium",
            "m3.xlarge",
            "m4.10xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.large",
            "m4.xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.large",
            "m5.xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.large",
            "m5a.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r4.16xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.large",
            "r5.xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.large",
            "r5a.xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.large",
            "r5d.xlarge",
            "t2.large",
            "t2.medium",
            "t2.micro",
            "t2.small",
        ]
    ] = Field(default=None, alias="EC2InstanceType")
    current_instances: Optional[int] = Field(default=None, alias="CurrentInstances")
    instance_limit: Optional[int] = Field(default=None, alias="InstanceLimit")
    location: Optional[str] = Field(default=None, alias="Location")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeFleetAttributesInputRequestModel(BaseModel):
    fleet_ids: Optional[Sequence[str]] = Field(default=None, alias="FleetIds")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFleetCapacityInputRequestModel(BaseModel):
    fleet_ids: Optional[Sequence[str]] = Field(default=None, alias="FleetIds")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFleetEventsInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class EventModel(BaseModel):
    event_id: Optional[str] = Field(default=None, alias="EventId")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    event_code: Optional[
        Literal[
            "FLEET_ACTIVATION_FAILED",
            "FLEET_ACTIVATION_FAILED_NO_INSTANCES",
            "FLEET_BINARY_DOWNLOAD_FAILED",
            "FLEET_CREATED",
            "FLEET_CREATION_EXTRACTING_BUILD",
            "FLEET_CREATION_RUNNING_INSTALLER",
            "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG",
            "FLEET_DELETED",
            "FLEET_INITIALIZATION_FAILED",
            "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED",
            "FLEET_SCALING_EVENT",
            "FLEET_STATE_ACTIVATING",
            "FLEET_STATE_ACTIVE",
            "FLEET_STATE_BUILDING",
            "FLEET_STATE_DOWNLOADING",
            "FLEET_STATE_ERROR",
            "FLEET_STATE_VALIDATING",
            "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE",
            "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND",
            "FLEET_VALIDATION_TIMED_OUT",
            "FLEET_VPC_PEERING_DELETED",
            "FLEET_VPC_PEERING_FAILED",
            "FLEET_VPC_PEERING_SUCCEEDED",
            "GAME_SESSION_ACTIVATION_TIMEOUT",
            "GENERIC_EVENT",
            "INSTANCE_INTERRUPTED",
            "INSTANCE_RECYCLED",
            "SERVER_PROCESS_CRASHED",
            "SERVER_PROCESS_FORCE_TERMINATED",
            "SERVER_PROCESS_INVALID_PATH",
            "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT",
            "SERVER_PROCESS_PROCESS_READY_TIMEOUT",
            "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT",
            "SERVER_PROCESS_TERMINATED_UNHEALTHY",
        ]
    ] = Field(default=None, alias="EventCode")
    message: Optional[str] = Field(default=None, alias="Message")
    event_time: Optional[datetime] = Field(default=None, alias="EventTime")
    pre_signed_log_url: Optional[str] = Field(default=None, alias="PreSignedLogUrl")


class DescribeFleetLocationAttributesInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    locations: Optional[Sequence[str]] = Field(default=None, alias="Locations")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeFleetLocationCapacityInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    location: str = Field(alias="Location")


class DescribeFleetLocationUtilizationInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    location: str = Field(alias="Location")


class FleetUtilizationModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    active_server_process_count: Optional[int] = Field(
        default=None, alias="ActiveServerProcessCount"
    )
    active_game_session_count: Optional[int] = Field(
        default=None, alias="ActiveGameSessionCount"
    )
    current_player_session_count: Optional[int] = Field(
        default=None, alias="CurrentPlayerSessionCount"
    )
    maximum_player_session_count: Optional[int] = Field(
        default=None, alias="MaximumPlayerSessionCount"
    )
    location: Optional[str] = Field(default=None, alias="Location")


class DescribeFleetPortSettingsInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    location: Optional[str] = Field(default=None, alias="Location")


class DescribeFleetUtilizationInputRequestModel(BaseModel):
    fleet_ids: Optional[Sequence[str]] = Field(default=None, alias="FleetIds")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeGameServerGroupInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")


class DescribeGameServerInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    game_server_id: str = Field(alias="GameServerId")


class DescribeGameServerInstancesInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GameServerInstanceModel(BaseModel):
    game_server_group_name: Optional[str] = Field(
        default=None, alias="GameServerGroupName"
    )
    game_server_group_arn: Optional[str] = Field(
        default=None, alias="GameServerGroupArn"
    )
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    instance_status: Optional[
        Literal["ACTIVE", "DRAINING", "SPOT_TERMINATING"]
    ] = Field(default=None, alias="InstanceStatus")


class DescribeGameSessionDetailsInputRequestModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    location: Optional[str] = Field(default=None, alias="Location")
    status_filter: Optional[str] = Field(default=None, alias="StatusFilter")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeGameSessionPlacementInputRequestModel(BaseModel):
    placement_id: str = Field(alias="PlacementId")


class DescribeGameSessionQueuesInputRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeGameSessionsInputRequestModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    location: Optional[str] = Field(default=None, alias="Location")
    status_filter: Optional[str] = Field(default=None, alias="StatusFilter")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeInstancesInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    location: Optional[str] = Field(default=None, alias="Location")


class InstanceModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    operating_system: Optional[
        Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
    ] = Field(default=None, alias="OperatingSystem")
    type: Optional[
        Literal[
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c3.large",
            "c3.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.large",
            "c5.xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.large",
            "c5a.xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c6a.12xlarge",
            "c6a.16xlarge",
            "c6a.24xlarge",
            "c6a.2xlarge",
            "c6a.4xlarge",
            "c6a.8xlarge",
            "c6a.large",
            "c6a.xlarge",
            "c6i.12xlarge",
            "c6i.16xlarge",
            "c6i.24xlarge",
            "c6i.2xlarge",
            "c6i.4xlarge",
            "c6i.8xlarge",
            "c6i.large",
            "c6i.xlarge",
            "m3.2xlarge",
            "m3.large",
            "m3.medium",
            "m3.xlarge",
            "m4.10xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.large",
            "m4.xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.large",
            "m5.xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.large",
            "m5a.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r4.16xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.large",
            "r5.xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.large",
            "r5a.xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.large",
            "r5d.xlarge",
            "t2.large",
            "t2.medium",
            "t2.micro",
            "t2.small",
        ]
    ] = Field(default=None, alias="Type")
    status: Optional[Literal["ACTIVE", "PENDING", "TERMINATING"]] = Field(
        default=None, alias="Status"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    location: Optional[str] = Field(default=None, alias="Location")


class DescribeMatchmakingConfigurationsInputRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    rule_set_name: Optional[str] = Field(default=None, alias="RuleSetName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeMatchmakingInputRequestModel(BaseModel):
    ticket_ids: Sequence[str] = Field(alias="TicketIds")


class DescribeMatchmakingRuleSetsInputRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePlayerSessionsInputRequestModel(BaseModel):
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    player_session_id: Optional[str] = Field(default=None, alias="PlayerSessionId")
    player_session_status_filter: Optional[str] = Field(
        default=None, alias="PlayerSessionStatusFilter"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeRuntimeConfigurationInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")


class DescribeScalingPoliciesInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    status_filter: Optional[
        Literal[
            "ACTIVE",
            "DELETED",
            "DELETE_REQUESTED",
            "DELETING",
            "ERROR",
            "UPDATE_REQUESTED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="StatusFilter")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    location: Optional[str] = Field(default=None, alias="Location")


class DescribeScriptInputRequestModel(BaseModel):
    script_id: str = Field(alias="ScriptId")


class DescribeVpcPeeringConnectionsInputRequestModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")


class DesiredPlayerSessionModel(BaseModel):
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    player_data: Optional[str] = Field(default=None, alias="PlayerData")


class EC2InstanceCountsModel(BaseModel):
    des_ired: Optional[int] = Field(default=None, alias="DESIRED")
    minimum: Optional[int] = Field(default=None, alias="MINIMUM")
    maximum: Optional[int] = Field(default=None, alias="MAXIMUM")
    p_ending: Optional[int] = Field(default=None, alias="PENDING")
    active: Optional[int] = Field(default=None, alias="ACTIVE")
    idl_e: Optional[int] = Field(default=None, alias="IDLE")
    terminating: Optional[int] = Field(default=None, alias="TERMINATING")


class TargetTrackingConfigurationModel(BaseModel):
    target_value: float = Field(alias="TargetValue")


class MatchedPlayerSessionModel(BaseModel):
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    player_session_id: Optional[str] = Field(default=None, alias="PlayerSessionId")


class PlacedPlayerSessionModel(BaseModel):
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    player_session_id: Optional[str] = Field(default=None, alias="PlayerSessionId")


class PlayerLatencyModel(BaseModel):
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    region_identifier: Optional[str] = Field(default=None, alias="RegionIdentifier")
    latency_in_milliseconds: Optional[float] = Field(
        default=None, alias="LatencyInMilliseconds"
    )


class GetComputeAccessInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    compute_name: str = Field(alias="ComputeName")


class GetComputeAuthTokenInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    compute_name: str = Field(alias="ComputeName")


class GetGameSessionLogUrlInputRequestModel(BaseModel):
    game_session_id: str = Field(alias="GameSessionId")


class GetInstanceAccessInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    instance_id: str = Field(alias="InstanceId")


class InstanceCredentialsModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    secret: Optional[str] = Field(default=None, alias="Secret")


class ListAliasesInputRequestModel(BaseModel):
    routing_strategy_type: Optional[Literal["SIMPLE", "TERMINAL"]] = Field(
        default=None, alias="RoutingStrategyType"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListBuildsInputRequestModel(BaseModel):
    status: Optional[Literal["FAILED", "INITIALIZED", "READY"]] = Field(
        default=None, alias="Status"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListComputeInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    location: Optional[str] = Field(default=None, alias="Location")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFleetsInputRequestModel(BaseModel):
    build_id: Optional[str] = Field(default=None, alias="BuildId")
    script_id: Optional[str] = Field(default=None, alias="ScriptId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGameServerGroupsInputRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGameServersInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLocationsInputRequestModel(BaseModel):
    filters: Optional[Sequence[Literal["AWS", "CUSTOM"]]] = Field(
        default=None, alias="Filters"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListScriptsInputRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class TargetConfigurationModel(BaseModel):
    target_value: float = Field(alias="TargetValue")


class RegisterComputeInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    compute_name: str = Field(alias="ComputeName")
    certificate_path: Optional[str] = Field(default=None, alias="CertificatePath")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    location: Optional[str] = Field(default=None, alias="Location")


class RegisterGameServerInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    game_server_id: str = Field(alias="GameServerId")
    instance_id: str = Field(alias="InstanceId")
    connection_info: Optional[str] = Field(default=None, alias="ConnectionInfo")
    game_server_data: Optional[str] = Field(default=None, alias="GameServerData")


class RequestUploadCredentialsInputRequestModel(BaseModel):
    build_id: str = Field(alias="BuildId")


class ResolveAliasInputRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")


class ResumeGameServerGroupInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    resume_actions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]] = Field(
        alias="ResumeActions"
    )


class ServerProcessModel(BaseModel):
    launch_path: str = Field(alias="LaunchPath")
    concurrent_executions: int = Field(alias="ConcurrentExecutions")
    parameters: Optional[str] = Field(default=None, alias="Parameters")


class SearchGameSessionsInputRequestModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    location: Optional[str] = Field(default=None, alias="Location")
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    sort_expression: Optional[str] = Field(default=None, alias="SortExpression")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StartFleetActionsInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    actions: Sequence[Literal["AUTO_SCALING"]] = Field(alias="Actions")
    location: Optional[str] = Field(default=None, alias="Location")


class StopFleetActionsInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    actions: Sequence[Literal["AUTO_SCALING"]] = Field(alias="Actions")
    location: Optional[str] = Field(default=None, alias="Location")


class StopGameSessionPlacementInputRequestModel(BaseModel):
    placement_id: str = Field(alias="PlacementId")


class StopMatchmakingInputRequestModel(BaseModel):
    ticket_id: str = Field(alias="TicketId")


class SuspendGameServerGroupInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    suspend_actions: Sequence[Literal["REPLACE_INSTANCE_TYPES"]] = Field(
        alias="SuspendActions"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateBuildInputRequestModel(BaseModel):
    build_id: str = Field(alias="BuildId")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class UpdateFleetCapacityInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    desired_instances: Optional[int] = Field(default=None, alias="DesiredInstances")
    min_size: Optional[int] = Field(default=None, alias="MinSize")
    max_size: Optional[int] = Field(default=None, alias="MaxSize")
    location: Optional[str] = Field(default=None, alias="Location")


class UpdateGameServerInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    game_server_id: str = Field(alias="GameServerId")
    game_server_data: Optional[str] = Field(default=None, alias="GameServerData")
    utilization_status: Optional[Literal["AVAILABLE", "UTILIZED"]] = Field(
        default=None, alias="UtilizationStatus"
    )
    health_check: Optional[Literal["HEALTHY"]] = Field(
        default=None, alias="HealthCheck"
    )


class UpdateGameSessionInputRequestModel(BaseModel):
    game_session_id: str = Field(alias="GameSessionId")
    maximum_player_session_count: Optional[int] = Field(
        default=None, alias="MaximumPlayerSessionCount"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    player_session_creation_policy: Optional[Literal["ACCEPT_ALL", "DENY_ALL"]] = Field(
        default=None, alias="PlayerSessionCreationPolicy"
    )
    protection_policy: Optional[Literal["FullProtection", "NoProtection"]] = Field(
        default=None, alias="ProtectionPolicy"
    )


class ValidateMatchmakingRuleSetInputRequestModel(BaseModel):
    rule_set_body: str = Field(alias="RuleSetBody")


class VpcPeeringConnectionStatusModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class AliasModel(BaseModel):
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    name: Optional[str] = Field(default=None, alias="Name")
    alias_arn: Optional[str] = Field(default=None, alias="AliasArn")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_strategy: Optional[RoutingStrategyModel] = Field(
        default=None, alias="RoutingStrategy"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class UpdateAliasInputRequestModel(BaseModel):
    alias_id: str = Field(alias="AliasId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    routing_strategy: Optional[RoutingStrategyModel] = Field(
        default=None, alias="RoutingStrategy"
    )


class PlayerModel(BaseModel):
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    player_attributes: Optional[Dict[str, AttributeValueModel]] = Field(
        default=None, alias="PlayerAttributes"
    )
    team: Optional[str] = Field(default=None, alias="Team")
    latency_in_ms: Optional[Dict[str, int]] = Field(default=None, alias="LatencyInMs")


class ClaimGameServerOutputModel(BaseModel):
    game_server: GameServerModel = Field(alias="GameServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBuildOutputModel(BaseModel):
    build: BuildModel = Field(alias="Build")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGameServerOutputModel(BaseModel):
    game_server: GameServerModel = Field(alias="GameServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComputeAccessOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    compute_name: str = Field(alias="ComputeName")
    compute_arn: str = Field(alias="ComputeArn")
    credentials: AwsCredentialsModel = Field(alias="Credentials")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComputeAuthTokenOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    compute_name: str = Field(alias="ComputeName")
    compute_arn: str = Field(alias="ComputeArn")
    auth_token: str = Field(alias="AuthToken")
    expiration_timestamp: datetime = Field(alias="ExpirationTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGameSessionLogUrlOutputModel(BaseModel):
    pre_signed_url: str = Field(alias="PreSignedUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBuildsOutputModel(BaseModel):
    builds: List[BuildModel] = Field(alias="Builds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFleetsOutputModel(BaseModel):
    fleet_ids: List[str] = Field(alias="FleetIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGameServersOutputModel(BaseModel):
    game_servers: List[GameServerModel] = Field(alias="GameServers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutScalingPolicyOutputModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterGameServerOutputModel(BaseModel):
    game_server: GameServerModel = Field(alias="GameServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResolveAliasOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFleetActionsOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopFleetActionsOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBuildOutputModel(BaseModel):
    build: BuildModel = Field(alias="Build")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFleetAttributesOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFleetCapacityOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFleetPortSettingsOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGameServerOutputModel(BaseModel):
    game_server: GameServerModel = Field(alias="GameServer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidateMatchmakingRuleSetOutputModel(BaseModel):
    valid: bool = Field(alias="Valid")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComputeOutputModel(BaseModel):
    compute: ComputeModel = Field(alias="Compute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListComputeOutputModel(BaseModel):
    compute_list: List[ComputeModel] = Field(alias="ComputeList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterComputeOutputModel(BaseModel):
    compute: ComputeModel = Field(alias="Compute")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAliasInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    routing_strategy: RoutingStrategyModel = Field(alias="RoutingStrategy")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateLocationInputRequestModel(BaseModel):
    location_name: str = Field(alias="LocationName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateMatchmakingRuleSetInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    rule_set_body: str = Field(alias="RuleSetBody")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateBuildInputRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    storage_location: Optional[S3LocationModel] = Field(
        default=None, alias="StorageLocation"
    )
    operating_system: Optional[
        Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
    ] = Field(default=None, alias="OperatingSystem")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    server_sdk_version: Optional[str] = Field(default=None, alias="ServerSdkVersion")


class CreateBuildOutputModel(BaseModel):
    build: BuildModel = Field(alias="Build")
    upload_credentials: AwsCredentialsModel = Field(alias="UploadCredentials")
    storage_location: S3LocationModel = Field(alias="StorageLocation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScriptInputRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    storage_location: Optional[S3LocationModel] = Field(
        default=None, alias="StorageLocation"
    )
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class RequestUploadCredentialsOutputModel(BaseModel):
    upload_credentials: AwsCredentialsModel = Field(alias="UploadCredentials")
    storage_location: S3LocationModel = Field(alias="StorageLocation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScriptModel(BaseModel):
    script_id: Optional[str] = Field(default=None, alias="ScriptId")
    script_arn: Optional[str] = Field(default=None, alias="ScriptArn")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    size_on_disk: Optional[int] = Field(default=None, alias="SizeOnDisk")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    storage_location: Optional[S3LocationModel] = Field(
        default=None, alias="StorageLocation"
    )


class UpdateScriptInputRequestModel(BaseModel):
    script_id: str = Field(alias="ScriptId")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    storage_location: Optional[S3LocationModel] = Field(
        default=None, alias="StorageLocation"
    )
    zip_file: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="ZipFile"
    )


class DescribeFleetPortSettingsOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    inbound_permissions: List[IpPermissionModel] = Field(alias="InboundPermissions")
    update_status: Literal["PENDING_UPDATE"] = Field(alias="UpdateStatus")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFleetPortSettingsInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    inbound_permission_authorizations: Optional[Sequence[IpPermissionModel]] = Field(
        default=None, alias="InboundPermissionAuthorizations"
    )
    inbound_permission_revocations: Optional[Sequence[IpPermissionModel]] = Field(
        default=None, alias="InboundPermissionRevocations"
    )


class CreateFleetLocationsInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    locations: Sequence[LocationConfigurationModel] = Field(alias="Locations")


class FleetAttributesModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    fleet_type: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(
        default=None, alias="FleetType"
    )
    instance_type: Optional[
        Literal[
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c3.large",
            "c3.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.large",
            "c5.xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.large",
            "c5a.xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c6a.12xlarge",
            "c6a.16xlarge",
            "c6a.24xlarge",
            "c6a.2xlarge",
            "c6a.4xlarge",
            "c6a.8xlarge",
            "c6a.large",
            "c6a.xlarge",
            "c6i.12xlarge",
            "c6i.16xlarge",
            "c6i.24xlarge",
            "c6i.2xlarge",
            "c6i.4xlarge",
            "c6i.8xlarge",
            "c6i.large",
            "c6i.xlarge",
            "m3.2xlarge",
            "m3.large",
            "m3.medium",
            "m3.xlarge",
            "m4.10xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.large",
            "m4.xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.large",
            "m5.xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.large",
            "m5a.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r4.16xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.large",
            "r5.xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.large",
            "r5a.xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.large",
            "r5d.xlarge",
            "t2.large",
            "t2.medium",
            "t2.micro",
            "t2.small",
        ]
    ] = Field(default=None, alias="InstanceType")
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    termination_time: Optional[datetime] = Field(default=None, alias="TerminationTime")
    status: Optional[
        Literal[
            "ACTIVATING",
            "ACTIVE",
            "BUILDING",
            "DELETING",
            "DOWNLOADING",
            "ERROR",
            "NEW",
            "NOT_FOUND",
            "TERMINATED",
            "VALIDATING",
        ]
    ] = Field(default=None, alias="Status")
    build_id: Optional[str] = Field(default=None, alias="BuildId")
    build_arn: Optional[str] = Field(default=None, alias="BuildArn")
    script_id: Optional[str] = Field(default=None, alias="ScriptId")
    script_arn: Optional[str] = Field(default=None, alias="ScriptArn")
    server_launch_path: Optional[str] = Field(default=None, alias="ServerLaunchPath")
    server_launch_parameters: Optional[str] = Field(
        default=None, alias="ServerLaunchParameters"
    )
    log_paths: Optional[List[str]] = Field(default=None, alias="LogPaths")
    new_game_session_protection_policy: Optional[
        Literal["FullProtection", "NoProtection"]
    ] = Field(default=None, alias="NewGameSessionProtectionPolicy")
    operating_system: Optional[
        Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
    ] = Field(default=None, alias="OperatingSystem")
    resource_creation_limit_policy: Optional[ResourceCreationLimitPolicyModel] = Field(
        default=None, alias="ResourceCreationLimitPolicy"
    )
    metric_groups: Optional[List[str]] = Field(default=None, alias="MetricGroups")
    stopped_actions: Optional[List[Literal["AUTO_SCALING"]]] = Field(
        default=None, alias="StoppedActions"
    )
    instance_role_arn: Optional[str] = Field(default=None, alias="InstanceRoleArn")
    certificate_configuration: Optional[CertificateConfigurationModel] = Field(
        default=None, alias="CertificateConfiguration"
    )
    compute_type: Optional[Literal["ANYWHERE", "EC2"]] = Field(
        default=None, alias="ComputeType"
    )
    anywhere_configuration: Optional[AnywhereConfigurationModel] = Field(
        default=None, alias="AnywhereConfiguration"
    )


class UpdateFleetAttributesInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    new_game_session_protection_policy: Optional[
        Literal["FullProtection", "NoProtection"]
    ] = Field(default=None, alias="NewGameSessionProtectionPolicy")
    resource_creation_limit_policy: Optional[ResourceCreationLimitPolicyModel] = Field(
        default=None, alias="ResourceCreationLimitPolicy"
    )
    metric_groups: Optional[Sequence[str]] = Field(default=None, alias="MetricGroups")
    anywhere_configuration: Optional[AnywhereConfigurationModel] = Field(
        default=None, alias="AnywhereConfiguration"
    )


class CreateFleetLocationsOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    location_states: List[LocationStateModel] = Field(alias="LocationStates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFleetLocationsOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    location_states: List[LocationStateModel] = Field(alias="LocationStates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LocationAttributesModel(BaseModel):
    location_state: Optional[LocationStateModel] = Field(
        default=None, alias="LocationState"
    )
    stopped_actions: Optional[List[Literal["AUTO_SCALING"]]] = Field(
        default=None, alias="StoppedActions"
    )
    update_status: Optional[Literal["PENDING_UPDATE"]] = Field(
        default=None, alias="UpdateStatus"
    )


class GameServerGroupModel(BaseModel):
    game_server_group_name: Optional[str] = Field(
        default=None, alias="GameServerGroupName"
    )
    game_server_group_arn: Optional[str] = Field(
        default=None, alias="GameServerGroupArn"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    instance_definitions: Optional[List[InstanceDefinitionModel]] = Field(
        default=None, alias="InstanceDefinitions"
    )
    balancing_strategy: Optional[
        Literal["ON_DEMAND_ONLY", "SPOT_ONLY", "SPOT_PREFERRED"]
    ] = Field(default=None, alias="BalancingStrategy")
    game_server_protection_policy: Optional[
        Literal["FULL_PROTECTION", "NO_PROTECTION"]
    ] = Field(default=None, alias="GameServerProtectionPolicy")
    auto_scaling_group_arn: Optional[str] = Field(
        default=None, alias="AutoScalingGroupArn"
    )
    status: Optional[
        Literal[
            "ACTIVATING",
            "ACTIVE",
            "DELETED",
            "DELETE_SCHEDULED",
            "DELETING",
            "ERROR",
            "NEW",
        ]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    suspended_actions: Optional[List[Literal["REPLACE_INSTANCE_TYPES"]]] = Field(
        default=None, alias="SuspendedActions"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class UpdateGameServerGroupInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    instance_definitions: Optional[Sequence[InstanceDefinitionModel]] = Field(
        default=None, alias="InstanceDefinitions"
    )
    game_server_protection_policy: Optional[
        Literal["FULL_PROTECTION", "NO_PROTECTION"]
    ] = Field(default=None, alias="GameServerProtectionPolicy")
    balancing_strategy: Optional[
        Literal["ON_DEMAND_ONLY", "SPOT_ONLY", "SPOT_PREFERRED"]
    ] = Field(default=None, alias="BalancingStrategy")


class CreateGameSessionInputRequestModel(BaseModel):
    maximum_player_session_count: int = Field(alias="MaximumPlayerSessionCount")
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    name: Optional[str] = Field(default=None, alias="Name")
    game_properties: Optional[Sequence[GamePropertyModel]] = Field(
        default=None, alias="GameProperties"
    )
    creator_id: Optional[str] = Field(default=None, alias="CreatorId")
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    idempotency_token: Optional[str] = Field(default=None, alias="IdempotencyToken")
    game_session_data: Optional[str] = Field(default=None, alias="GameSessionData")
    location: Optional[str] = Field(default=None, alias="Location")


class CreateMatchmakingConfigurationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    request_timeout_seconds: int = Field(alias="RequestTimeoutSeconds")
    acceptance_required: bool = Field(alias="AcceptanceRequired")
    rule_set_name: str = Field(alias="RuleSetName")
    description: Optional[str] = Field(default=None, alias="Description")
    game_session_queue_arns: Optional[Sequence[str]] = Field(
        default=None, alias="GameSessionQueueArns"
    )
    acceptance_timeout_seconds: Optional[int] = Field(
        default=None, alias="AcceptanceTimeoutSeconds"
    )
    notification_target: Optional[str] = Field(default=None, alias="NotificationTarget")
    additional_player_count: Optional[int] = Field(
        default=None, alias="AdditionalPlayerCount"
    )
    custom_event_data: Optional[str] = Field(default=None, alias="CustomEventData")
    game_properties: Optional[Sequence[GamePropertyModel]] = Field(
        default=None, alias="GameProperties"
    )
    game_session_data: Optional[str] = Field(default=None, alias="GameSessionData")
    backfill_mode: Optional[Literal["AUTOMATIC", "MANUAL"]] = Field(
        default=None, alias="BackfillMode"
    )
    flex_match_mode: Optional[Literal["STANDALONE", "WITH_QUEUE"]] = Field(
        default=None, alias="FlexMatchMode"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GameSessionModel(BaseModel):
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    name: Optional[str] = Field(default=None, alias="Name")
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    termination_time: Optional[datetime] = Field(default=None, alias="TerminationTime")
    current_player_session_count: Optional[int] = Field(
        default=None, alias="CurrentPlayerSessionCount"
    )
    maximum_player_session_count: Optional[int] = Field(
        default=None, alias="MaximumPlayerSessionCount"
    )
    status: Optional[
        Literal["ACTIVATING", "ACTIVE", "ERROR", "TERMINATED", "TERMINATING"]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[Literal["INTERRUPTED"]] = Field(
        default=None, alias="StatusReason"
    )
    game_properties: Optional[List[GamePropertyModel]] = Field(
        default=None, alias="GameProperties"
    )
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    port: Optional[int] = Field(default=None, alias="Port")
    player_session_creation_policy: Optional[Literal["ACCEPT_ALL", "DENY_ALL"]] = Field(
        default=None, alias="PlayerSessionCreationPolicy"
    )
    creator_id: Optional[str] = Field(default=None, alias="CreatorId")
    game_session_data: Optional[str] = Field(default=None, alias="GameSessionData")
    matchmaker_data: Optional[str] = Field(default=None, alias="MatchmakerData")
    location: Optional[str] = Field(default=None, alias="Location")


class MatchmakingConfigurationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    configuration_arn: Optional[str] = Field(default=None, alias="ConfigurationArn")
    description: Optional[str] = Field(default=None, alias="Description")
    game_session_queue_arns: Optional[List[str]] = Field(
        default=None, alias="GameSessionQueueArns"
    )
    request_timeout_seconds: Optional[int] = Field(
        default=None, alias="RequestTimeoutSeconds"
    )
    acceptance_timeout_seconds: Optional[int] = Field(
        default=None, alias="AcceptanceTimeoutSeconds"
    )
    acceptance_required: Optional[bool] = Field(
        default=None, alias="AcceptanceRequired"
    )
    rule_set_name: Optional[str] = Field(default=None, alias="RuleSetName")
    rule_set_arn: Optional[str] = Field(default=None, alias="RuleSetArn")
    notification_target: Optional[str] = Field(default=None, alias="NotificationTarget")
    additional_player_count: Optional[int] = Field(
        default=None, alias="AdditionalPlayerCount"
    )
    custom_event_data: Optional[str] = Field(default=None, alias="CustomEventData")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    game_properties: Optional[List[GamePropertyModel]] = Field(
        default=None, alias="GameProperties"
    )
    game_session_data: Optional[str] = Field(default=None, alias="GameSessionData")
    backfill_mode: Optional[Literal["AUTOMATIC", "MANUAL"]] = Field(
        default=None, alias="BackfillMode"
    )
    flex_match_mode: Optional[Literal["STANDALONE", "WITH_QUEUE"]] = Field(
        default=None, alias="FlexMatchMode"
    )


class UpdateMatchmakingConfigurationInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    game_session_queue_arns: Optional[Sequence[str]] = Field(
        default=None, alias="GameSessionQueueArns"
    )
    request_timeout_seconds: Optional[int] = Field(
        default=None, alias="RequestTimeoutSeconds"
    )
    acceptance_timeout_seconds: Optional[int] = Field(
        default=None, alias="AcceptanceTimeoutSeconds"
    )
    acceptance_required: Optional[bool] = Field(
        default=None, alias="AcceptanceRequired"
    )
    rule_set_name: Optional[str] = Field(default=None, alias="RuleSetName")
    notification_target: Optional[str] = Field(default=None, alias="NotificationTarget")
    additional_player_count: Optional[int] = Field(
        default=None, alias="AdditionalPlayerCount"
    )
    custom_event_data: Optional[str] = Field(default=None, alias="CustomEventData")
    game_properties: Optional[Sequence[GamePropertyModel]] = Field(
        default=None, alias="GameProperties"
    )
    game_session_data: Optional[str] = Field(default=None, alias="GameSessionData")
    backfill_mode: Optional[Literal["AUTOMATIC", "MANUAL"]] = Field(
        default=None, alias="BackfillMode"
    )
    flex_match_mode: Optional[Literal["STANDALONE", "WITH_QUEUE"]] = Field(
        default=None, alias="FlexMatchMode"
    )


class CreateGameSessionQueueInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    timeout_in_seconds: Optional[int] = Field(default=None, alias="TimeoutInSeconds")
    player_latency_policies: Optional[Sequence[PlayerLatencyPolicyModel]] = Field(
        default=None, alias="PlayerLatencyPolicies"
    )
    destinations: Optional[Sequence[GameSessionQueueDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    filter_configuration: Optional[FilterConfigurationModel] = Field(
        default=None, alias="FilterConfiguration"
    )
    priority_configuration: Optional[PriorityConfigurationModel] = Field(
        default=None, alias="PriorityConfiguration"
    )
    custom_event_data: Optional[str] = Field(default=None, alias="CustomEventData")
    notification_target: Optional[str] = Field(default=None, alias="NotificationTarget")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class GameSessionQueueModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    game_session_queue_arn: Optional[str] = Field(
        default=None, alias="GameSessionQueueArn"
    )
    timeout_in_seconds: Optional[int] = Field(default=None, alias="TimeoutInSeconds")
    player_latency_policies: Optional[List[PlayerLatencyPolicyModel]] = Field(
        default=None, alias="PlayerLatencyPolicies"
    )
    destinations: Optional[List[GameSessionQueueDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    filter_configuration: Optional[FilterConfigurationModel] = Field(
        default=None, alias="FilterConfiguration"
    )
    priority_configuration: Optional[PriorityConfigurationModel] = Field(
        default=None, alias="PriorityConfiguration"
    )
    custom_event_data: Optional[str] = Field(default=None, alias="CustomEventData")
    notification_target: Optional[str] = Field(default=None, alias="NotificationTarget")


class UpdateGameSessionQueueInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    timeout_in_seconds: Optional[int] = Field(default=None, alias="TimeoutInSeconds")
    player_latency_policies: Optional[Sequence[PlayerLatencyPolicyModel]] = Field(
        default=None, alias="PlayerLatencyPolicies"
    )
    destinations: Optional[Sequence[GameSessionQueueDestinationModel]] = Field(
        default=None, alias="Destinations"
    )
    filter_configuration: Optional[FilterConfigurationModel] = Field(
        default=None, alias="FilterConfiguration"
    )
    priority_configuration: Optional[PriorityConfigurationModel] = Field(
        default=None, alias="PriorityConfiguration"
    )
    custom_event_data: Optional[str] = Field(default=None, alias="CustomEventData")
    notification_target: Optional[str] = Field(default=None, alias="NotificationTarget")


class CreateLocationOutputModel(BaseModel):
    location: LocationModelModel = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLocationsOutputModel(BaseModel):
    locations: List[LocationModelModel] = Field(alias="Locations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMatchmakingRuleSetOutputModel(BaseModel):
    rule_set: MatchmakingRuleSetModel = Field(alias="RuleSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMatchmakingRuleSetsOutputModel(BaseModel):
    rule_sets: List[MatchmakingRuleSetModel] = Field(alias="RuleSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePlayerSessionOutputModel(BaseModel):
    player_session: PlayerSessionModel = Field(alias="PlayerSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePlayerSessionsOutputModel(BaseModel):
    player_sessions: List[PlayerSessionModel] = Field(alias="PlayerSessions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePlayerSessionsOutputModel(BaseModel):
    player_sessions: List[PlayerSessionModel] = Field(alias="PlayerSessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVpcPeeringAuthorizationOutputModel(BaseModel):
    vpc_peering_authorization: VpcPeeringAuthorizationModel = Field(
        alias="VpcPeeringAuthorization"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVpcPeeringAuthorizationsOutputModel(BaseModel):
    vpc_peering_authorizations: List[VpcPeeringAuthorizationModel] = Field(
        alias="VpcPeeringAuthorizations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEC2InstanceLimitsOutputModel(BaseModel):
    ec2_instance_limits: List[EC2InstanceLimitModel] = Field(alias="EC2InstanceLimits")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetAttributesInputDescribeFleetAttributesPaginateModel(BaseModel):
    fleet_ids: Optional[Sequence[str]] = Field(default=None, alias="FleetIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFleetCapacityInputDescribeFleetCapacityPaginateModel(BaseModel):
    fleet_ids: Optional[Sequence[str]] = Field(default=None, alias="FleetIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFleetEventsInputDescribeFleetEventsPaginateModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFleetUtilizationInputDescribeFleetUtilizationPaginateModel(BaseModel):
    fleet_ids: Optional[Sequence[str]] = Field(default=None, alias="FleetIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGameServerInstancesInputDescribeGameServerInstancesPaginateModel(
    BaseModel
):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    instance_ids: Optional[Sequence[str]] = Field(default=None, alias="InstanceIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGameSessionDetailsInputDescribeGameSessionDetailsPaginateModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    location: Optional[str] = Field(default=None, alias="Location")
    status_filter: Optional[str] = Field(default=None, alias="StatusFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGameSessionQueuesInputDescribeGameSessionQueuesPaginateModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeGameSessionsInputDescribeGameSessionsPaginateModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    location: Optional[str] = Field(default=None, alias="Location")
    status_filter: Optional[str] = Field(default=None, alias="StatusFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeInstancesInputDescribeInstancesPaginateModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    location: Optional[str] = Field(default=None, alias="Location")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMatchmakingConfigurationsInputDescribeMatchmakingConfigurationsPaginateModel(
    BaseModel
):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    rule_set_name: Optional[str] = Field(default=None, alias="RuleSetName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMatchmakingRuleSetsInputDescribeMatchmakingRuleSetsPaginateModel(
    BaseModel
):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePlayerSessionsInputDescribePlayerSessionsPaginateModel(BaseModel):
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    player_id: Optional[str] = Field(default=None, alias="PlayerId")
    player_session_id: Optional[str] = Field(default=None, alias="PlayerSessionId")
    player_session_status_filter: Optional[str] = Field(
        default=None, alias="PlayerSessionStatusFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeScalingPoliciesInputDescribeScalingPoliciesPaginateModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    status_filter: Optional[
        Literal[
            "ACTIVE",
            "DELETED",
            "DELETE_REQUESTED",
            "DELETING",
            "ERROR",
            "UPDATE_REQUESTED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="StatusFilter")
    location: Optional[str] = Field(default=None, alias="Location")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAliasesInputListAliasesPaginateModel(BaseModel):
    routing_strategy_type: Optional[Literal["SIMPLE", "TERMINAL"]] = Field(
        default=None, alias="RoutingStrategyType"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBuildsInputListBuildsPaginateModel(BaseModel):
    status: Optional[Literal["FAILED", "INITIALIZED", "READY"]] = Field(
        default=None, alias="Status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComputeInputListComputePaginateModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    location: Optional[str] = Field(default=None, alias="Location")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFleetsInputListFleetsPaginateModel(BaseModel):
    build_id: Optional[str] = Field(default=None, alias="BuildId")
    script_id: Optional[str] = Field(default=None, alias="ScriptId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGameServerGroupsInputListGameServerGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGameServersInputListGameServersPaginateModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLocationsInputListLocationsPaginateModel(BaseModel):
    filters: Optional[Sequence[Literal["AWS", "CUSTOM"]]] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListScriptsInputListScriptsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchGameSessionsInputSearchGameSessionsPaginateModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    alias_id: Optional[str] = Field(default=None, alias="AliasId")
    location: Optional[str] = Field(default=None, alias="Location")
    filter_expression: Optional[str] = Field(default=None, alias="FilterExpression")
    sort_expression: Optional[str] = Field(default=None, alias="SortExpression")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFleetEventsOutputModel(BaseModel):
    events: List[EventModel] = Field(alias="Events")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetLocationUtilizationOutputModel(BaseModel):
    fleet_utilization: FleetUtilizationModel = Field(alias="FleetUtilization")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetUtilizationOutputModel(BaseModel):
    fleet_utilization: List[FleetUtilizationModel] = Field(alias="FleetUtilization")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGameServerInstancesOutputModel(BaseModel):
    game_server_instances: List[GameServerInstanceModel] = Field(
        alias="GameServerInstances"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInstancesOutputModel(BaseModel):
    instances: List[InstanceModel] = Field(alias="Instances")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FleetCapacityModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    instance_type: Optional[
        Literal[
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c3.large",
            "c3.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.large",
            "c5.xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.large",
            "c5a.xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c6a.12xlarge",
            "c6a.16xlarge",
            "c6a.24xlarge",
            "c6a.2xlarge",
            "c6a.4xlarge",
            "c6a.8xlarge",
            "c6a.large",
            "c6a.xlarge",
            "c6i.12xlarge",
            "c6i.16xlarge",
            "c6i.24xlarge",
            "c6i.2xlarge",
            "c6i.4xlarge",
            "c6i.8xlarge",
            "c6i.large",
            "c6i.xlarge",
            "m3.2xlarge",
            "m3.large",
            "m3.medium",
            "m3.xlarge",
            "m4.10xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.large",
            "m4.xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.large",
            "m5.xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.large",
            "m5a.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r4.16xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.large",
            "r5.xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.large",
            "r5a.xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.large",
            "r5d.xlarge",
            "t2.large",
            "t2.medium",
            "t2.micro",
            "t2.small",
        ]
    ] = Field(default=None, alias="InstanceType")
    instance_counts: Optional[EC2InstanceCountsModel] = Field(
        default=None, alias="InstanceCounts"
    )
    location: Optional[str] = Field(default=None, alias="Location")


class GameServerGroupAutoScalingPolicyModel(BaseModel):
    target_tracking_configuration: TargetTrackingConfigurationModel = Field(
        alias="TargetTrackingConfiguration"
    )
    estimated_instance_warmup: Optional[int] = Field(
        default=None, alias="EstimatedInstanceWarmup"
    )


class GameSessionConnectionInfoModel(BaseModel):
    game_session_arn: Optional[str] = Field(default=None, alias="GameSessionArn")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    port: Optional[int] = Field(default=None, alias="Port")
    matched_player_sessions: Optional[List[MatchedPlayerSessionModel]] = Field(
        default=None, alias="MatchedPlayerSessions"
    )


class GameSessionPlacementModel(BaseModel):
    placement_id: Optional[str] = Field(default=None, alias="PlacementId")
    game_session_queue_name: Optional[str] = Field(
        default=None, alias="GameSessionQueueName"
    )
    status: Optional[
        Literal["CANCELLED", "FAILED", "FULFILLED", "PENDING", "TIMED_OUT"]
    ] = Field(default=None, alias="Status")
    game_properties: Optional[List[GamePropertyModel]] = Field(
        default=None, alias="GameProperties"
    )
    maximum_player_session_count: Optional[int] = Field(
        default=None, alias="MaximumPlayerSessionCount"
    )
    game_session_name: Optional[str] = Field(default=None, alias="GameSessionName")
    game_session_id: Optional[str] = Field(default=None, alias="GameSessionId")
    game_session_arn: Optional[str] = Field(default=None, alias="GameSessionArn")
    game_session_region: Optional[str] = Field(default=None, alias="GameSessionRegion")
    player_latencies: Optional[List[PlayerLatencyModel]] = Field(
        default=None, alias="PlayerLatencies"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    port: Optional[int] = Field(default=None, alias="Port")
    placed_player_sessions: Optional[List[PlacedPlayerSessionModel]] = Field(
        default=None, alias="PlacedPlayerSessions"
    )
    game_session_data: Optional[str] = Field(default=None, alias="GameSessionData")
    matchmaker_data: Optional[str] = Field(default=None, alias="MatchmakerData")


class StartGameSessionPlacementInputRequestModel(BaseModel):
    placement_id: str = Field(alias="PlacementId")
    game_session_queue_name: str = Field(alias="GameSessionQueueName")
    maximum_player_session_count: int = Field(alias="MaximumPlayerSessionCount")
    game_properties: Optional[Sequence[GamePropertyModel]] = Field(
        default=None, alias="GameProperties"
    )
    game_session_name: Optional[str] = Field(default=None, alias="GameSessionName")
    player_latencies: Optional[Sequence[PlayerLatencyModel]] = Field(
        default=None, alias="PlayerLatencies"
    )
    desired_player_sessions: Optional[Sequence[DesiredPlayerSessionModel]] = Field(
        default=None, alias="DesiredPlayerSessions"
    )
    game_session_data: Optional[str] = Field(default=None, alias="GameSessionData")


class InstanceAccessModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")
    operating_system: Optional[
        Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
    ] = Field(default=None, alias="OperatingSystem")
    credentials: Optional[InstanceCredentialsModel] = Field(
        default=None, alias="Credentials"
    )


class PutScalingPolicyInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    fleet_id: str = Field(alias="FleetId")
    metric_name: Literal[
        "ActivatingGameSessions",
        "ActiveGameSessions",
        "ActiveInstances",
        "AvailableGameSessions",
        "AvailablePlayerSessions",
        "ConcurrentActivatableGameSessions",
        "CurrentPlayerSessions",
        "IdleInstances",
        "PercentAvailableGameSessions",
        "PercentIdleInstances",
        "QueueDepth",
        "WaitTime",
    ] = Field(alias="MetricName")
    scaling_adjustment: Optional[int] = Field(default=None, alias="ScalingAdjustment")
    scaling_adjustment_type: Optional[
        Literal["ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"]
    ] = Field(default=None, alias="ScalingAdjustmentType")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    comparison_operator: Optional[
        Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanThreshold",
        ]
    ] = Field(default=None, alias="ComparisonOperator")
    evaluation_periods: Optional[int] = Field(default=None, alias="EvaluationPeriods")
    policy_type: Optional[Literal["RuleBased", "TargetBased"]] = Field(
        default=None, alias="PolicyType"
    )
    target_configuration: Optional[TargetConfigurationModel] = Field(
        default=None, alias="TargetConfiguration"
    )


class ScalingPolicyModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal[
            "ACTIVE",
            "DELETED",
            "DELETE_REQUESTED",
            "DELETING",
            "ERROR",
            "UPDATE_REQUESTED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    scaling_adjustment: Optional[int] = Field(default=None, alias="ScalingAdjustment")
    scaling_adjustment_type: Optional[
        Literal["ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"]
    ] = Field(default=None, alias="ScalingAdjustmentType")
    comparison_operator: Optional[
        Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanThreshold",
        ]
    ] = Field(default=None, alias="ComparisonOperator")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    evaluation_periods: Optional[int] = Field(default=None, alias="EvaluationPeriods")
    metric_name: Optional[
        Literal[
            "ActivatingGameSessions",
            "ActiveGameSessions",
            "ActiveInstances",
            "AvailableGameSessions",
            "AvailablePlayerSessions",
            "ConcurrentActivatableGameSessions",
            "CurrentPlayerSessions",
            "IdleInstances",
            "PercentAvailableGameSessions",
            "PercentIdleInstances",
            "QueueDepth",
            "WaitTime",
        ]
    ] = Field(default=None, alias="MetricName")
    policy_type: Optional[Literal["RuleBased", "TargetBased"]] = Field(
        default=None, alias="PolicyType"
    )
    target_configuration: Optional[TargetConfigurationModel] = Field(
        default=None, alias="TargetConfiguration"
    )
    update_status: Optional[Literal["PENDING_UPDATE"]] = Field(
        default=None, alias="UpdateStatus"
    )
    location: Optional[str] = Field(default=None, alias="Location")


class RuntimeConfigurationModel(BaseModel):
    server_processes: Optional[Sequence[ServerProcessModel]] = Field(
        default=None, alias="ServerProcesses"
    )
    max_concurrent_game_session_activations: Optional[int] = Field(
        default=None, alias="MaxConcurrentGameSessionActivations"
    )
    game_session_activation_timeout_seconds: Optional[int] = Field(
        default=None, alias="GameSessionActivationTimeoutSeconds"
    )


class VpcPeeringConnectionModel(BaseModel):
    fleet_id: Optional[str] = Field(default=None, alias="FleetId")
    fleet_arn: Optional[str] = Field(default=None, alias="FleetArn")
    ip_v4_cidr_block: Optional[str] = Field(default=None, alias="IpV4CidrBlock")
    vpc_peering_connection_id: Optional[str] = Field(
        default=None, alias="VpcPeeringConnectionId"
    )
    status: Optional[VpcPeeringConnectionStatusModel] = Field(
        default=None, alias="Status"
    )
    peer_vpc_id: Optional[str] = Field(default=None, alias="PeerVpcId")
    game_lift_vpc_id: Optional[str] = Field(default=None, alias="GameLiftVpcId")


class CreateAliasOutputModel(BaseModel):
    alias: AliasModel = Field(alias="Alias")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAliasOutputModel(BaseModel):
    alias: AliasModel = Field(alias="Alias")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAliasesOutputModel(BaseModel):
    aliases: List[AliasModel] = Field(alias="Aliases")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAliasOutputModel(BaseModel):
    alias: AliasModel = Field(alias="Alias")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMatchBackfillInputRequestModel(BaseModel):
    configuration_name: str = Field(alias="ConfigurationName")
    players: Sequence[PlayerModel] = Field(alias="Players")
    ticket_id: Optional[str] = Field(default=None, alias="TicketId")
    game_session_arn: Optional[str] = Field(default=None, alias="GameSessionArn")


class StartMatchmakingInputRequestModel(BaseModel):
    configuration_name: str = Field(alias="ConfigurationName")
    players: Sequence[PlayerModel] = Field(alias="Players")
    ticket_id: Optional[str] = Field(default=None, alias="TicketId")


class CreateScriptOutputModel(BaseModel):
    script: ScriptModel = Field(alias="Script")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScriptOutputModel(BaseModel):
    script: ScriptModel = Field(alias="Script")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListScriptsOutputModel(BaseModel):
    scripts: List[ScriptModel] = Field(alias="Scripts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateScriptOutputModel(BaseModel):
    script: ScriptModel = Field(alias="Script")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFleetOutputModel(BaseModel):
    fleet_attributes: FleetAttributesModel = Field(alias="FleetAttributes")
    location_states: List[LocationStateModel] = Field(alias="LocationStates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetAttributesOutputModel(BaseModel):
    fleet_attributes: List[FleetAttributesModel] = Field(alias="FleetAttributes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetLocationAttributesOutputModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    fleet_arn: str = Field(alias="FleetArn")
    location_attributes: List[LocationAttributesModel] = Field(
        alias="LocationAttributes"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGameServerGroupOutputModel(BaseModel):
    game_server_group: GameServerGroupModel = Field(alias="GameServerGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGameServerGroupOutputModel(BaseModel):
    game_server_group: GameServerGroupModel = Field(alias="GameServerGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGameServerGroupOutputModel(BaseModel):
    game_server_group: GameServerGroupModel = Field(alias="GameServerGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGameServerGroupsOutputModel(BaseModel):
    game_server_groups: List[GameServerGroupModel] = Field(alias="GameServerGroups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResumeGameServerGroupOutputModel(BaseModel):
    game_server_group: GameServerGroupModel = Field(alias="GameServerGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SuspendGameServerGroupOutputModel(BaseModel):
    game_server_group: GameServerGroupModel = Field(alias="GameServerGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGameServerGroupOutputModel(BaseModel):
    game_server_group: GameServerGroupModel = Field(alias="GameServerGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGameSessionOutputModel(BaseModel):
    game_session: GameSessionModel = Field(alias="GameSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGameSessionsOutputModel(BaseModel):
    game_sessions: List[GameSessionModel] = Field(alias="GameSessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GameSessionDetailModel(BaseModel):
    game_session: Optional[GameSessionModel] = Field(default=None, alias="GameSession")
    protection_policy: Optional[Literal["FullProtection", "NoProtection"]] = Field(
        default=None, alias="ProtectionPolicy"
    )


class SearchGameSessionsOutputModel(BaseModel):
    game_sessions: List[GameSessionModel] = Field(alias="GameSessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGameSessionOutputModel(BaseModel):
    game_session: GameSessionModel = Field(alias="GameSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMatchmakingConfigurationOutputModel(BaseModel):
    configuration: MatchmakingConfigurationModel = Field(alias="Configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMatchmakingConfigurationsOutputModel(BaseModel):
    configurations: List[MatchmakingConfigurationModel] = Field(alias="Configurations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMatchmakingConfigurationOutputModel(BaseModel):
    configuration: MatchmakingConfigurationModel = Field(alias="Configuration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGameSessionQueueOutputModel(BaseModel):
    game_session_queue: GameSessionQueueModel = Field(alias="GameSessionQueue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGameSessionQueuesOutputModel(BaseModel):
    game_session_queues: List[GameSessionQueueModel] = Field(alias="GameSessionQueues")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGameSessionQueueOutputModel(BaseModel):
    game_session_queue: GameSessionQueueModel = Field(alias="GameSessionQueue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetCapacityOutputModel(BaseModel):
    fleet_capacity: List[FleetCapacityModel] = Field(alias="FleetCapacity")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetLocationCapacityOutputModel(BaseModel):
    fleet_capacity: FleetCapacityModel = Field(alias="FleetCapacity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGameServerGroupInputRequestModel(BaseModel):
    game_server_group_name: str = Field(alias="GameServerGroupName")
    role_arn: str = Field(alias="RoleArn")
    min_size: int = Field(alias="MinSize")
    max_size: int = Field(alias="MaxSize")
    launch_template: LaunchTemplateSpecificationModel = Field(alias="LaunchTemplate")
    instance_definitions: Sequence[InstanceDefinitionModel] = Field(
        alias="InstanceDefinitions"
    )
    auto_scaling_policy: Optional[GameServerGroupAutoScalingPolicyModel] = Field(
        default=None, alias="AutoScalingPolicy"
    )
    balancing_strategy: Optional[
        Literal["ON_DEMAND_ONLY", "SPOT_ONLY", "SPOT_PREFERRED"]
    ] = Field(default=None, alias="BalancingStrategy")
    game_server_protection_policy: Optional[
        Literal["FULL_PROTECTION", "NO_PROTECTION"]
    ] = Field(default=None, alias="GameServerProtectionPolicy")
    vpc_subnets: Optional[Sequence[str]] = Field(default=None, alias="VpcSubnets")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class MatchmakingTicketModel(BaseModel):
    ticket_id: Optional[str] = Field(default=None, alias="TicketId")
    configuration_name: Optional[str] = Field(default=None, alias="ConfigurationName")
    configuration_arn: Optional[str] = Field(default=None, alias="ConfigurationArn")
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "FAILED",
            "PLACING",
            "QUEUED",
            "REQUIRES_ACCEPTANCE",
            "SEARCHING",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    players: Optional[List[PlayerModel]] = Field(default=None, alias="Players")
    game_session_connection_info: Optional[GameSessionConnectionInfoModel] = Field(
        default=None, alias="GameSessionConnectionInfo"
    )
    estimated_wait_time: Optional[int] = Field(default=None, alias="EstimatedWaitTime")


class DescribeGameSessionPlacementOutputModel(BaseModel):
    game_session_placement: GameSessionPlacementModel = Field(
        alias="GameSessionPlacement"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartGameSessionPlacementOutputModel(BaseModel):
    game_session_placement: GameSessionPlacementModel = Field(
        alias="GameSessionPlacement"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopGameSessionPlacementOutputModel(BaseModel):
    game_session_placement: GameSessionPlacementModel = Field(
        alias="GameSessionPlacement"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceAccessOutputModel(BaseModel):
    instance_access: InstanceAccessModel = Field(alias="InstanceAccess")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScalingPoliciesOutputModel(BaseModel):
    scaling_policies: List[ScalingPolicyModel] = Field(alias="ScalingPolicies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFleetInputRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    build_id: Optional[str] = Field(default=None, alias="BuildId")
    script_id: Optional[str] = Field(default=None, alias="ScriptId")
    server_launch_path: Optional[str] = Field(default=None, alias="ServerLaunchPath")
    server_launch_parameters: Optional[str] = Field(
        default=None, alias="ServerLaunchParameters"
    )
    log_paths: Optional[Sequence[str]] = Field(default=None, alias="LogPaths")
    ec2_instance_type: Optional[
        Literal[
            "c3.2xlarge",
            "c3.4xlarge",
            "c3.8xlarge",
            "c3.large",
            "c3.xlarge",
            "c4.2xlarge",
            "c4.4xlarge",
            "c4.8xlarge",
            "c4.large",
            "c4.xlarge",
            "c5.12xlarge",
            "c5.18xlarge",
            "c5.24xlarge",
            "c5.2xlarge",
            "c5.4xlarge",
            "c5.9xlarge",
            "c5.large",
            "c5.xlarge",
            "c5a.12xlarge",
            "c5a.16xlarge",
            "c5a.24xlarge",
            "c5a.2xlarge",
            "c5a.4xlarge",
            "c5a.8xlarge",
            "c5a.large",
            "c5a.xlarge",
            "c5d.12xlarge",
            "c5d.18xlarge",
            "c5d.24xlarge",
            "c5d.2xlarge",
            "c5d.4xlarge",
            "c5d.9xlarge",
            "c5d.large",
            "c5d.xlarge",
            "c6a.12xlarge",
            "c6a.16xlarge",
            "c6a.24xlarge",
            "c6a.2xlarge",
            "c6a.4xlarge",
            "c6a.8xlarge",
            "c6a.large",
            "c6a.xlarge",
            "c6i.12xlarge",
            "c6i.16xlarge",
            "c6i.24xlarge",
            "c6i.2xlarge",
            "c6i.4xlarge",
            "c6i.8xlarge",
            "c6i.large",
            "c6i.xlarge",
            "m3.2xlarge",
            "m3.large",
            "m3.medium",
            "m3.xlarge",
            "m4.10xlarge",
            "m4.2xlarge",
            "m4.4xlarge",
            "m4.large",
            "m4.xlarge",
            "m5.12xlarge",
            "m5.16xlarge",
            "m5.24xlarge",
            "m5.2xlarge",
            "m5.4xlarge",
            "m5.8xlarge",
            "m5.large",
            "m5.xlarge",
            "m5a.12xlarge",
            "m5a.16xlarge",
            "m5a.24xlarge",
            "m5a.2xlarge",
            "m5a.4xlarge",
            "m5a.8xlarge",
            "m5a.large",
            "m5a.xlarge",
            "r3.2xlarge",
            "r3.4xlarge",
            "r3.8xlarge",
            "r3.large",
            "r3.xlarge",
            "r4.16xlarge",
            "r4.2xlarge",
            "r4.4xlarge",
            "r4.8xlarge",
            "r4.large",
            "r4.xlarge",
            "r5.12xlarge",
            "r5.16xlarge",
            "r5.24xlarge",
            "r5.2xlarge",
            "r5.4xlarge",
            "r5.8xlarge",
            "r5.large",
            "r5.xlarge",
            "r5a.12xlarge",
            "r5a.16xlarge",
            "r5a.24xlarge",
            "r5a.2xlarge",
            "r5a.4xlarge",
            "r5a.8xlarge",
            "r5a.large",
            "r5a.xlarge",
            "r5d.12xlarge",
            "r5d.16xlarge",
            "r5d.24xlarge",
            "r5d.2xlarge",
            "r5d.4xlarge",
            "r5d.8xlarge",
            "r5d.large",
            "r5d.xlarge",
            "t2.large",
            "t2.medium",
            "t2.micro",
            "t2.small",
        ]
    ] = Field(default=None, alias="EC2InstanceType")
    ec2_inbound_permissions: Optional[Sequence[IpPermissionModel]] = Field(
        default=None, alias="EC2InboundPermissions"
    )
    new_game_session_protection_policy: Optional[
        Literal["FullProtection", "NoProtection"]
    ] = Field(default=None, alias="NewGameSessionProtectionPolicy")
    runtime_configuration: Optional[RuntimeConfigurationModel] = Field(
        default=None, alias="RuntimeConfiguration"
    )
    resource_creation_limit_policy: Optional[ResourceCreationLimitPolicyModel] = Field(
        default=None, alias="ResourceCreationLimitPolicy"
    )
    metric_groups: Optional[Sequence[str]] = Field(default=None, alias="MetricGroups")
    peer_vpc_aws_account_id: Optional[str] = Field(
        default=None, alias="PeerVpcAwsAccountId"
    )
    peer_vpc_id: Optional[str] = Field(default=None, alias="PeerVpcId")
    fleet_type: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(
        default=None, alias="FleetType"
    )
    instance_role_arn: Optional[str] = Field(default=None, alias="InstanceRoleArn")
    certificate_configuration: Optional[CertificateConfigurationModel] = Field(
        default=None, alias="CertificateConfiguration"
    )
    locations: Optional[Sequence[LocationConfigurationModel]] = Field(
        default=None, alias="Locations"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    compute_type: Optional[Literal["ANYWHERE", "EC2"]] = Field(
        default=None, alias="ComputeType"
    )
    anywhere_configuration: Optional[AnywhereConfigurationModel] = Field(
        default=None, alias="AnywhereConfiguration"
    )


class DescribeRuntimeConfigurationOutputModel(BaseModel):
    runtime_configuration: RuntimeConfigurationModel = Field(
        alias="RuntimeConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRuntimeConfigurationInputRequestModel(BaseModel):
    fleet_id: str = Field(alias="FleetId")
    runtime_configuration: RuntimeConfigurationModel = Field(
        alias="RuntimeConfiguration"
    )


class UpdateRuntimeConfigurationOutputModel(BaseModel):
    runtime_configuration: RuntimeConfigurationModel = Field(
        alias="RuntimeConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVpcPeeringConnectionsOutputModel(BaseModel):
    vpc_peering_connections: List[VpcPeeringConnectionModel] = Field(
        alias="VpcPeeringConnections"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGameSessionDetailsOutputModel(BaseModel):
    game_session_details: List[GameSessionDetailModel] = Field(
        alias="GameSessionDetails"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeMatchmakingOutputModel(BaseModel):
    ticket_list: List[MatchmakingTicketModel] = Field(alias="TicketList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMatchBackfillOutputModel(BaseModel):
    matchmaking_ticket: MatchmakingTicketModel = Field(alias="MatchmakingTicket")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMatchmakingOutputModel(BaseModel):
    matchmaking_ticket: MatchmakingTicketModel = Field(alias="MatchmakingTicket")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
