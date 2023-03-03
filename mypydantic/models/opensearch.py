# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AWSDomainInformationModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    region: Optional[str] = Field(default=None, alias="Region")


class AcceptInboundConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class OptionStatusModel(BaseModel):
    creation_date: datetime = Field(alias="CreationDate")
    update_date: datetime = Field(alias="UpdateDate")
    state: Literal["Active", "Processing", "RequiresIndexDocuments"] = Field(
        alias="State"
    )
    update_version: Optional[int] = Field(default=None, alias="UpdateVersion")
    pending_deletion: Optional[bool] = Field(default=None, alias="PendingDeletion")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class AdditionalLimitModel(BaseModel):
    limit_name: Optional[str] = Field(default=None, alias="LimitName")
    limit_values: Optional[List[str]] = Field(default=None, alias="LimitValues")


class MasterUserOptionsModel(BaseModel):
    master_user_arn: Optional[str] = Field(default=None, alias="MasterUserARN")
    master_user_name: Optional[str] = Field(default=None, alias="MasterUserName")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )


class AssociatePackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    domain_name: str = Field(alias="DomainName")


class AuthorizeVpcEndpointAccessRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    account: str = Field(alias="Account")


class AuthorizedPrincipalModel(BaseModel):
    principal_type: Optional[Literal["AWS_ACCOUNT", "AWS_SERVICE"]] = Field(
        default=None, alias="PrincipalType"
    )
    principal: Optional[str] = Field(default=None, alias="Principal")


class ScheduledAutoTuneDetailsModel(BaseModel):
    date: Optional[datetime] = Field(default=None, alias="Date")
    action_type: Optional[
        Literal["JVM_HEAP_SIZE_TUNING", "JVM_YOUNG_GEN_TUNING"]
    ] = Field(default=None, alias="ActionType")
    action: Optional[str] = Field(default=None, alias="Action")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="Severity"
    )


class DurationModel(BaseModel):
    value: Optional[int] = Field(default=None, alias="Value")
    unit: Optional[Literal["HOURS"]] = Field(default=None, alias="Unit")


class AutoTuneOptionsOutputModel(BaseModel):
    state: Optional[
        Literal[
            "DISABLED",
            "DISABLED_AND_ROLLBACK_COMPLETE",
            "DISABLED_AND_ROLLBACK_ERROR",
            "DISABLED_AND_ROLLBACK_IN_PROGRESS",
            "DISABLED_AND_ROLLBACK_SCHEDULED",
            "DISABLE_IN_PROGRESS",
            "ENABLED",
            "ENABLE_IN_PROGRESS",
            "ERROR",
        ]
    ] = Field(default=None, alias="State")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    use_off_peak_window: Optional[bool] = Field(default=None, alias="UseOffPeakWindow")


class AutoTuneStatusModel(BaseModel):
    creation_date: datetime = Field(alias="CreationDate")
    update_date: datetime = Field(alias="UpdateDate")
    state: Literal[
        "DISABLED",
        "DISABLED_AND_ROLLBACK_COMPLETE",
        "DISABLED_AND_ROLLBACK_ERROR",
        "DISABLED_AND_ROLLBACK_IN_PROGRESS",
        "DISABLED_AND_ROLLBACK_SCHEDULED",
        "DISABLE_IN_PROGRESS",
        "ENABLED",
        "ENABLE_IN_PROGRESS",
        "ERROR",
    ] = Field(alias="State")
    update_version: Optional[int] = Field(default=None, alias="UpdateVersion")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    pending_deletion: Optional[bool] = Field(default=None, alias="PendingDeletion")


class CancelServiceSoftwareUpdateRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class ServiceSoftwareOptionsModel(BaseModel):
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")
    new_version: Optional[str] = Field(default=None, alias="NewVersion")
    update_available: Optional[bool] = Field(default=None, alias="UpdateAvailable")
    cancellable: Optional[bool] = Field(default=None, alias="Cancellable")
    update_status: Optional[
        Literal[
            "COMPLETED", "ELIGIBLE", "IN_PROGRESS", "NOT_ELIGIBLE", "PENDING_UPDATE"
        ]
    ] = Field(default=None, alias="UpdateStatus")
    description: Optional[str] = Field(default=None, alias="Description")
    automated_update_date: Optional[datetime] = Field(
        default=None, alias="AutomatedUpdateDate"
    )
    optional_deployment: Optional[bool] = Field(
        default=None, alias="OptionalDeployment"
    )


class ChangeProgressDetailsModel(BaseModel):
    change_id: Optional[str] = Field(default=None, alias="ChangeId")
    message: Optional[str] = Field(default=None, alias="Message")


class ChangeProgressStageModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[str] = Field(default=None, alias="Status")
    description: Optional[str] = Field(default=None, alias="Description")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")


class ColdStorageOptionsModel(BaseModel):
    enabled: bool = Field(alias="Enabled")


class ZoneAwarenessConfigModel(BaseModel):
    availability_zone_count: Optional[int] = Field(
        default=None, alias="AvailabilityZoneCount"
    )


class CognitoOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    identity_pool_id: Optional[str] = Field(default=None, alias="IdentityPoolId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class CompatibleVersionsMapModel(BaseModel):
    source_version: Optional[str] = Field(default=None, alias="SourceVersion")
    target_versions: Optional[List[str]] = Field(default=None, alias="TargetVersions")


class ConnectionPropertiesModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")


class DomainEndpointOptionsModel(BaseModel):
    enforce_http_s: Optional[bool] = Field(default=None, alias="EnforceHTTPS")
    tl_s_security_policy: Optional[
        Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"]
    ] = Field(default=None, alias="TLSSecurityPolicy")
    custom_endpoint_enabled: Optional[bool] = Field(
        default=None, alias="CustomEndpointEnabled"
    )
    custom_endpoint: Optional[str] = Field(default=None, alias="CustomEndpoint")
    custom_endpoint_certificate_arn: Optional[str] = Field(
        default=None, alias="CustomEndpointCertificateArn"
    )


class EBSOptionsModel(BaseModel):
    ebs_enabled: Optional[bool] = Field(default=None, alias="EBSEnabled")
    volume_type: Optional[Literal["gp2", "gp3", "io1", "standard"]] = Field(
        default=None, alias="VolumeType"
    )
    volume_size: Optional[int] = Field(default=None, alias="VolumeSize")
    iops: Optional[int] = Field(default=None, alias="Iops")
    throughput: Optional[int] = Field(default=None, alias="Throughput")


class EncryptionAtRestOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class LogPublishingOptionModel(BaseModel):
    cloud_watch_logs_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsLogGroupArn"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class NodeToNodeEncryptionOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class SnapshotOptionsModel(BaseModel):
    automated_snapshot_start_hour: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotStartHour"
    )


class SoftwareUpdateOptionsModel(BaseModel):
    auto_software_update_enabled: Optional[bool] = Field(
        default=None, alias="AutoSoftwareUpdateEnabled"
    )


class VPCOptionsModel(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class OutboundConnectionStatusModel(BaseModel):
    status_code: Optional[
        Literal[
            "ACTIVE",
            "APPROVED",
            "DELETED",
            "DELETING",
            "PENDING_ACCEPTANCE",
            "PROVISIONING",
            "REJECTED",
            "REJECTING",
            "VALIDATING",
            "VALIDATION_FAILED",
        ]
    ] = Field(default=None, alias="StatusCode")
    message: Optional[str] = Field(default=None, alias="Message")


class PackageSourceModel(BaseModel):
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")


class DeleteDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DeleteInboundConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")


class DeleteOutboundConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")


class DeletePackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageID")


class DeleteVpcEndpointRequestModel(BaseModel):
    vpc_endpoint_id: str = Field(alias="VpcEndpointId")


class VpcEndpointSummaryModel(BaseModel):
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")
    vpc_endpoint_owner: Optional[str] = Field(default=None, alias="VpcEndpointOwner")
    domain_arn: Optional[str] = Field(default=None, alias="DomainArn")
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATE_FAILED",
            "CREATING",
            "DELETE_FAILED",
            "DELETING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")


class DescribeDomainAutoTunesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeDomainChangeProgressRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    change_id: Optional[str] = Field(default=None, alias="ChangeId")


class DescribeDomainConfigRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DescribeDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DescribeDomainsRequestModel(BaseModel):
    domain_names: Sequence[str] = Field(alias="DomainNames")


class DescribeDryRunProgressRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    dry_run_id: Optional[str] = Field(default=None, alias="DryRunId")
    load_dry_run_config: Optional[bool] = Field(default=None, alias="LoadDryRunConfig")


class DryRunResultsModel(BaseModel):
    deployment_type: Optional[str] = Field(default=None, alias="DeploymentType")
    message: Optional[str] = Field(default=None, alias="Message")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class DescribeInstanceTypeLimitsRequestModel(BaseModel):
    instance_type: Literal[
        "c4.2xlarge.search",
        "c4.4xlarge.search",
        "c4.8xlarge.search",
        "c4.large.search",
        "c4.xlarge.search",
        "c5.18xlarge.search",
        "c5.2xlarge.search",
        "c5.4xlarge.search",
        "c5.9xlarge.search",
        "c5.large.search",
        "c5.xlarge.search",
        "c6g.12xlarge.search",
        "c6g.2xlarge.search",
        "c6g.4xlarge.search",
        "c6g.8xlarge.search",
        "c6g.large.search",
        "c6g.xlarge.search",
        "d2.2xlarge.search",
        "d2.4xlarge.search",
        "d2.8xlarge.search",
        "d2.xlarge.search",
        "i2.2xlarge.search",
        "i2.xlarge.search",
        "i3.16xlarge.search",
        "i3.2xlarge.search",
        "i3.4xlarge.search",
        "i3.8xlarge.search",
        "i3.large.search",
        "i3.xlarge.search",
        "m3.2xlarge.search",
        "m3.large.search",
        "m3.medium.search",
        "m3.xlarge.search",
        "m4.10xlarge.search",
        "m4.2xlarge.search",
        "m4.4xlarge.search",
        "m4.large.search",
        "m4.xlarge.search",
        "m5.12xlarge.search",
        "m5.24xlarge.search",
        "m5.2xlarge.search",
        "m5.4xlarge.search",
        "m5.large.search",
        "m5.xlarge.search",
        "m6g.12xlarge.search",
        "m6g.2xlarge.search",
        "m6g.4xlarge.search",
        "m6g.8xlarge.search",
        "m6g.large.search",
        "m6g.xlarge.search",
        "r3.2xlarge.search",
        "r3.4xlarge.search",
        "r3.8xlarge.search",
        "r3.large.search",
        "r3.xlarge.search",
        "r4.16xlarge.search",
        "r4.2xlarge.search",
        "r4.4xlarge.search",
        "r4.8xlarge.search",
        "r4.large.search",
        "r4.xlarge.search",
        "r5.12xlarge.search",
        "r5.24xlarge.search",
        "r5.2xlarge.search",
        "r5.4xlarge.search",
        "r5.large.search",
        "r5.xlarge.search",
        "r6g.12xlarge.search",
        "r6g.2xlarge.search",
        "r6g.4xlarge.search",
        "r6g.8xlarge.search",
        "r6g.large.search",
        "r6g.xlarge.search",
        "r6gd.12xlarge.search",
        "r6gd.16xlarge.search",
        "r6gd.2xlarge.search",
        "r6gd.4xlarge.search",
        "r6gd.8xlarge.search",
        "r6gd.large.search",
        "r6gd.xlarge.search",
        "t2.medium.search",
        "t2.micro.search",
        "t2.small.search",
        "t3.2xlarge.search",
        "t3.large.search",
        "t3.medium.search",
        "t3.micro.search",
        "t3.nano.search",
        "t3.small.search",
        "t3.xlarge.search",
        "t4g.medium.search",
        "t4g.small.search",
        "ultrawarm1.large.search",
        "ultrawarm1.medium.search",
        "ultrawarm1.xlarge.search",
    ] = Field(alias="InstanceType")
    engine_version: str = Field(alias="EngineVersion")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")


class DescribePackagesFilterModel(BaseModel):
    name: Optional[Literal["PackageID", "PackageName", "PackageStatus"]] = Field(
        default=None, alias="Name"
    )
    value: Optional[Sequence[str]] = Field(default=None, alias="Value")


class DescribeReservedInstanceOfferingsRequestModel(BaseModel):
    reserved_instance_offering_id: Optional[str] = Field(
        default=None, alias="ReservedInstanceOfferingId"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeReservedInstancesRequestModel(BaseModel):
    reserved_instance_id: Optional[str] = Field(
        default=None, alias="ReservedInstanceId"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeVpcEndpointsRequestModel(BaseModel):
    vpc_endpoint_ids: Sequence[str] = Field(alias="VpcEndpointIds")


class VpcEndpointErrorModel(BaseModel):
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")
    error_code: Optional[Literal["ENDPOINT_NOT_FOUND", "SERVER_ERROR"]] = Field(
        default=None, alias="ErrorCode"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class DissociatePackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    domain_name: str = Field(alias="DomainName")


class DomainInfoModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    engine_type: Optional[Literal["Elasticsearch", "OpenSearch"]] = Field(
        default=None, alias="EngineType"
    )


class ErrorDetailsModel(BaseModel):
    error_type: Optional[str] = Field(default=None, alias="ErrorType")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class VPCDerivedInfoModel(BaseModel):
    vp_cid: Optional[str] = Field(default=None, alias="VPCId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class ValidationFailureModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class GetCompatibleVersionsRequestModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")


class GetPackageVersionHistoryRequestModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PackageVersionHistoryModel(BaseModel):
    package_version: Optional[str] = Field(default=None, alias="PackageVersion")
    commit_message: Optional[str] = Field(default=None, alias="CommitMessage")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class GetUpgradeHistoryRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetUpgradeStatusRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class InboundConnectionStatusModel(BaseModel):
    status_code: Optional[
        Literal[
            "ACTIVE",
            "APPROVED",
            "DELETED",
            "DELETING",
            "PENDING_ACCEPTANCE",
            "PROVISIONING",
            "REJECTED",
            "REJECTING",
        ]
    ] = Field(default=None, alias="StatusCode")
    message: Optional[str] = Field(default=None, alias="Message")


class InstanceCountLimitsModel(BaseModel):
    minimum_instance_count: Optional[int] = Field(
        default=None, alias="MinimumInstanceCount"
    )
    maximum_instance_count: Optional[int] = Field(
        default=None, alias="MaximumInstanceCount"
    )


class InstanceTypeDetailsModel(BaseModel):
    instance_type: Optional[
        Literal[
            "c4.2xlarge.search",
            "c4.4xlarge.search",
            "c4.8xlarge.search",
            "c4.large.search",
            "c4.xlarge.search",
            "c5.18xlarge.search",
            "c5.2xlarge.search",
            "c5.4xlarge.search",
            "c5.9xlarge.search",
            "c5.large.search",
            "c5.xlarge.search",
            "c6g.12xlarge.search",
            "c6g.2xlarge.search",
            "c6g.4xlarge.search",
            "c6g.8xlarge.search",
            "c6g.large.search",
            "c6g.xlarge.search",
            "d2.2xlarge.search",
            "d2.4xlarge.search",
            "d2.8xlarge.search",
            "d2.xlarge.search",
            "i2.2xlarge.search",
            "i2.xlarge.search",
            "i3.16xlarge.search",
            "i3.2xlarge.search",
            "i3.4xlarge.search",
            "i3.8xlarge.search",
            "i3.large.search",
            "i3.xlarge.search",
            "m3.2xlarge.search",
            "m3.large.search",
            "m3.medium.search",
            "m3.xlarge.search",
            "m4.10xlarge.search",
            "m4.2xlarge.search",
            "m4.4xlarge.search",
            "m4.large.search",
            "m4.xlarge.search",
            "m5.12xlarge.search",
            "m5.24xlarge.search",
            "m5.2xlarge.search",
            "m5.4xlarge.search",
            "m5.large.search",
            "m5.xlarge.search",
            "m6g.12xlarge.search",
            "m6g.2xlarge.search",
            "m6g.4xlarge.search",
            "m6g.8xlarge.search",
            "m6g.large.search",
            "m6g.xlarge.search",
            "r3.2xlarge.search",
            "r3.4xlarge.search",
            "r3.8xlarge.search",
            "r3.large.search",
            "r3.xlarge.search",
            "r4.16xlarge.search",
            "r4.2xlarge.search",
            "r4.4xlarge.search",
            "r4.8xlarge.search",
            "r4.large.search",
            "r4.xlarge.search",
            "r5.12xlarge.search",
            "r5.24xlarge.search",
            "r5.2xlarge.search",
            "r5.4xlarge.search",
            "r5.large.search",
            "r5.xlarge.search",
            "r6g.12xlarge.search",
            "r6g.2xlarge.search",
            "r6g.4xlarge.search",
            "r6g.8xlarge.search",
            "r6g.large.search",
            "r6g.xlarge.search",
            "r6gd.12xlarge.search",
            "r6gd.16xlarge.search",
            "r6gd.2xlarge.search",
            "r6gd.4xlarge.search",
            "r6gd.8xlarge.search",
            "r6gd.large.search",
            "r6gd.xlarge.search",
            "t2.medium.search",
            "t2.micro.search",
            "t2.small.search",
            "t3.2xlarge.search",
            "t3.large.search",
            "t3.medium.search",
            "t3.micro.search",
            "t3.nano.search",
            "t3.small.search",
            "t3.xlarge.search",
            "t4g.medium.search",
            "t4g.small.search",
            "ultrawarm1.large.search",
            "ultrawarm1.medium.search",
            "ultrawarm1.xlarge.search",
        ]
    ] = Field(default=None, alias="InstanceType")
    encryption_enabled: Optional[bool] = Field(default=None, alias="EncryptionEnabled")
    cognito_enabled: Optional[bool] = Field(default=None, alias="CognitoEnabled")
    app_logs_enabled: Optional[bool] = Field(default=None, alias="AppLogsEnabled")
    advanced_security_enabled: Optional[bool] = Field(
        default=None, alias="AdvancedSecurityEnabled"
    )
    warm_enabled: Optional[bool] = Field(default=None, alias="WarmEnabled")
    instance_role: Optional[List[str]] = Field(default=None, alias="InstanceRole")


class ListDomainNamesRequestModel(BaseModel):
    engine_type: Optional[Literal["Elasticsearch", "OpenSearch"]] = Field(
        default=None, alias="EngineType"
    )


class ListDomainsForPackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInstanceTypeDetailsRequestModel(BaseModel):
    engine_version: str = Field(alias="EngineVersion")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPackagesForDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListScheduledActionsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ScheduledActionModel(BaseModel):
    id: str = Field(alias="Id")
    type: Literal[
        "JVM_HEAP_SIZE_TUNING", "JVM_YOUNG_GEN_TUNING", "SERVICE_SOFTWARE_UPDATE"
    ] = Field(alias="Type")
    severity: Literal["HIGH", "LOW", "MEDIUM"] = Field(alias="Severity")
    scheduled_time: int = Field(alias="ScheduledTime")
    description: Optional[str] = Field(default=None, alias="Description")
    scheduled_by: Optional[Literal["CUSTOMER", "SYSTEM"]] = Field(
        default=None, alias="ScheduledBy"
    )
    status: Optional[
        Literal[
            "COMPLETED",
            "ELIGIBLE",
            "FAILED",
            "IN_PROGRESS",
            "NOT_ELIGIBLE",
            "PENDING_UPDATE",
        ]
    ] = Field(default=None, alias="Status")
    mandatory: Optional[bool] = Field(default=None, alias="Mandatory")
    cancellable: Optional[bool] = Field(default=None, alias="Cancellable")


class ListTagsRequestModel(BaseModel):
    arn: str = Field(alias="ARN")


class ListVersionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVpcEndpointAccessRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVpcEndpointsForDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVpcEndpointsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class WindowStartTimeModel(BaseModel):
    hours: int = Field(alias="Hours")
    minutes: int = Field(alias="Minutes")


class PurchaseReservedInstanceOfferingRequestModel(BaseModel):
    reserved_instance_offering_id: str = Field(alias="ReservedInstanceOfferingId")
    reservation_name: str = Field(alias="ReservationName")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")


class RecurringChargeModel(BaseModel):
    recurring_charge_amount: Optional[float] = Field(
        default=None, alias="RecurringChargeAmount"
    )
    recurring_charge_frequency: Optional[str] = Field(
        default=None, alias="RecurringChargeFrequency"
    )


class RejectInboundConnectionRequestModel(BaseModel):
    connection_id: str = Field(alias="ConnectionId")


class RemoveTagsRequestModel(BaseModel):
    arn: str = Field(alias="ARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class RevokeVpcEndpointAccessRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    account: str = Field(alias="Account")


class SAMLIdpModel(BaseModel):
    metadata_content: str = Field(alias="MetadataContent")
    entity_id: str = Field(alias="EntityId")


class StartServiceSoftwareUpdateRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    schedule_at: Optional[Literal["NOW", "OFF_PEAK_WINDOW", "TIMESTAMP"]] = Field(
        default=None, alias="ScheduleAt"
    )
    desired_start_time: Optional[int] = Field(default=None, alias="DesiredStartTime")


class StorageTypeLimitModel(BaseModel):
    limit_name: Optional[str] = Field(default=None, alias="LimitName")
    limit_values: Optional[List[str]] = Field(default=None, alias="LimitValues")


class UpdateScheduledActionRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    action_id: str = Field(alias="ActionID")
    action_type: Literal[
        "JVM_HEAP_SIZE_TUNING", "JVM_YOUNG_GEN_TUNING", "SERVICE_SOFTWARE_UPDATE"
    ] = Field(alias="ActionType")
    schedule_at: Literal["NOW", "OFF_PEAK_WINDOW", "TIMESTAMP"] = Field(
        alias="ScheduleAt"
    )
    desired_start_time: Optional[int] = Field(default=None, alias="DesiredStartTime")


class UpgradeDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    target_version: str = Field(alias="TargetVersion")
    perform_check_only: Optional[bool] = Field(default=None, alias="PerformCheckOnly")
    advanced_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="AdvancedOptions"
    )


class UpgradeStepItemModel(BaseModel):
    upgrade_step: Optional[Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"]] = Field(
        default=None, alias="UpgradeStep"
    )
    upgrade_step_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES"]
    ] = Field(default=None, alias="UpgradeStepStatus")
    issues: Optional[List[str]] = Field(default=None, alias="Issues")
    progress_percent: Optional[float] = Field(default=None, alias="ProgressPercent")


class DomainInformationContainerModel(BaseModel):
    aws_domain_information: Optional[AWSDomainInformationModel] = Field(
        default=None, alias="AWSDomainInformation"
    )


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUpgradeStatusResponseModel(BaseModel):
    upgrade_step: Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"] = Field(
        alias="UpgradeStep"
    )
    step_status: Literal[
        "FAILED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES"
    ] = Field(alias="StepStatus")
    upgrade_name: str = Field(alias="UpgradeName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVersionsResponseModel(BaseModel):
    versions: List[str] = Field(alias="Versions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseReservedInstanceOfferingResponseModel(BaseModel):
    reserved_instance_id: str = Field(alias="ReservedInstanceId")
    reservation_name: str = Field(alias="ReservationName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccessPoliciesStatusModel(BaseModel):
    options: str = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class AdvancedOptionsStatusModel(BaseModel):
    options: Dict[str, str] = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class VersionStatusModel(BaseModel):
    options: str = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class AddTagsRequestModel(BaseModel):
    arn: str = Field(alias="ARN")
    tag_list: Sequence[TagModel] = Field(alias="TagList")


class ListTagsResponseModel(BaseModel):
    tag_list: List[TagModel] = Field(alias="TagList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthorizeVpcEndpointAccessResponseModel(BaseModel):
    authorized_principal: AuthorizedPrincipalModel = Field(alias="AuthorizedPrincipal")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVpcEndpointAccessResponseModel(BaseModel):
    authorized_principal_list: List[AuthorizedPrincipalModel] = Field(
        alias="AuthorizedPrincipalList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoTuneDetailsModel(BaseModel):
    scheduled_auto_tune_details: Optional[ScheduledAutoTuneDetailsModel] = Field(
        default=None, alias="ScheduledAutoTuneDetails"
    )


class AutoTuneMaintenanceScheduleModel(BaseModel):
    start_at: Optional[Union[datetime, str]] = Field(default=None, alias="StartAt")
    duration: Optional[DurationModel] = Field(default=None, alias="Duration")
    cron_expression_for_recurrence: Optional[str] = Field(
        default=None, alias="CronExpressionForRecurrence"
    )


class CancelServiceSoftwareUpdateResponseModel(BaseModel):
    service_software_options: ServiceSoftwareOptionsModel = Field(
        alias="ServiceSoftwareOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartServiceSoftwareUpdateResponseModel(BaseModel):
    service_software_options: ServiceSoftwareOptionsModel = Field(
        alias="ServiceSoftwareOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpgradeDomainResponseModel(BaseModel):
    upgrade_id: str = Field(alias="UpgradeId")
    domain_name: str = Field(alias="DomainName")
    target_version: str = Field(alias="TargetVersion")
    perform_check_only: bool = Field(alias="PerformCheckOnly")
    advanced_options: Dict[str, str] = Field(alias="AdvancedOptions")
    change_progress_details: ChangeProgressDetailsModel = Field(
        alias="ChangeProgressDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeProgressStatusDetailsModel(BaseModel):
    change_id: Optional[str] = Field(default=None, alias="ChangeId")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    status: Optional[Literal["COMPLETED", "FAILED", "PENDING", "PROCESSING"]] = Field(
        default=None, alias="Status"
    )
    pending_properties: Optional[List[str]] = Field(
        default=None, alias="PendingProperties"
    )
    completed_properties: Optional[List[str]] = Field(
        default=None, alias="CompletedProperties"
    )
    total_number_of_stages: Optional[int] = Field(
        default=None, alias="TotalNumberOfStages"
    )
    change_progress_stages: Optional[List[ChangeProgressStageModel]] = Field(
        default=None, alias="ChangeProgressStages"
    )


class ClusterConfigModel(BaseModel):
    instance_type: Optional[
        Literal[
            "c4.2xlarge.search",
            "c4.4xlarge.search",
            "c4.8xlarge.search",
            "c4.large.search",
            "c4.xlarge.search",
            "c5.18xlarge.search",
            "c5.2xlarge.search",
            "c5.4xlarge.search",
            "c5.9xlarge.search",
            "c5.large.search",
            "c5.xlarge.search",
            "c6g.12xlarge.search",
            "c6g.2xlarge.search",
            "c6g.4xlarge.search",
            "c6g.8xlarge.search",
            "c6g.large.search",
            "c6g.xlarge.search",
            "d2.2xlarge.search",
            "d2.4xlarge.search",
            "d2.8xlarge.search",
            "d2.xlarge.search",
            "i2.2xlarge.search",
            "i2.xlarge.search",
            "i3.16xlarge.search",
            "i3.2xlarge.search",
            "i3.4xlarge.search",
            "i3.8xlarge.search",
            "i3.large.search",
            "i3.xlarge.search",
            "m3.2xlarge.search",
            "m3.large.search",
            "m3.medium.search",
            "m3.xlarge.search",
            "m4.10xlarge.search",
            "m4.2xlarge.search",
            "m4.4xlarge.search",
            "m4.large.search",
            "m4.xlarge.search",
            "m5.12xlarge.search",
            "m5.24xlarge.search",
            "m5.2xlarge.search",
            "m5.4xlarge.search",
            "m5.large.search",
            "m5.xlarge.search",
            "m6g.12xlarge.search",
            "m6g.2xlarge.search",
            "m6g.4xlarge.search",
            "m6g.8xlarge.search",
            "m6g.large.search",
            "m6g.xlarge.search",
            "r3.2xlarge.search",
            "r3.4xlarge.search",
            "r3.8xlarge.search",
            "r3.large.search",
            "r3.xlarge.search",
            "r4.16xlarge.search",
            "r4.2xlarge.search",
            "r4.4xlarge.search",
            "r4.8xlarge.search",
            "r4.large.search",
            "r4.xlarge.search",
            "r5.12xlarge.search",
            "r5.24xlarge.search",
            "r5.2xlarge.search",
            "r5.4xlarge.search",
            "r5.large.search",
            "r5.xlarge.search",
            "r6g.12xlarge.search",
            "r6g.2xlarge.search",
            "r6g.4xlarge.search",
            "r6g.8xlarge.search",
            "r6g.large.search",
            "r6g.xlarge.search",
            "r6gd.12xlarge.search",
            "r6gd.16xlarge.search",
            "r6gd.2xlarge.search",
            "r6gd.4xlarge.search",
            "r6gd.8xlarge.search",
            "r6gd.large.search",
            "r6gd.xlarge.search",
            "t2.medium.search",
            "t2.micro.search",
            "t2.small.search",
            "t3.2xlarge.search",
            "t3.large.search",
            "t3.medium.search",
            "t3.micro.search",
            "t3.nano.search",
            "t3.small.search",
            "t3.xlarge.search",
            "t4g.medium.search",
            "t4g.small.search",
            "ultrawarm1.large.search",
            "ultrawarm1.medium.search",
            "ultrawarm1.xlarge.search",
        ]
    ] = Field(default=None, alias="InstanceType")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    dedicated_master_enabled: Optional[bool] = Field(
        default=None, alias="DedicatedMasterEnabled"
    )
    zone_awareness_enabled: Optional[bool] = Field(
        default=None, alias="ZoneAwarenessEnabled"
    )
    zone_awareness_config: Optional[ZoneAwarenessConfigModel] = Field(
        default=None, alias="ZoneAwarenessConfig"
    )
    dedicated_master_type: Optional[
        Literal[
            "c4.2xlarge.search",
            "c4.4xlarge.search",
            "c4.8xlarge.search",
            "c4.large.search",
            "c4.xlarge.search",
            "c5.18xlarge.search",
            "c5.2xlarge.search",
            "c5.4xlarge.search",
            "c5.9xlarge.search",
            "c5.large.search",
            "c5.xlarge.search",
            "c6g.12xlarge.search",
            "c6g.2xlarge.search",
            "c6g.4xlarge.search",
            "c6g.8xlarge.search",
            "c6g.large.search",
            "c6g.xlarge.search",
            "d2.2xlarge.search",
            "d2.4xlarge.search",
            "d2.8xlarge.search",
            "d2.xlarge.search",
            "i2.2xlarge.search",
            "i2.xlarge.search",
            "i3.16xlarge.search",
            "i3.2xlarge.search",
            "i3.4xlarge.search",
            "i3.8xlarge.search",
            "i3.large.search",
            "i3.xlarge.search",
            "m3.2xlarge.search",
            "m3.large.search",
            "m3.medium.search",
            "m3.xlarge.search",
            "m4.10xlarge.search",
            "m4.2xlarge.search",
            "m4.4xlarge.search",
            "m4.large.search",
            "m4.xlarge.search",
            "m5.12xlarge.search",
            "m5.24xlarge.search",
            "m5.2xlarge.search",
            "m5.4xlarge.search",
            "m5.large.search",
            "m5.xlarge.search",
            "m6g.12xlarge.search",
            "m6g.2xlarge.search",
            "m6g.4xlarge.search",
            "m6g.8xlarge.search",
            "m6g.large.search",
            "m6g.xlarge.search",
            "r3.2xlarge.search",
            "r3.4xlarge.search",
            "r3.8xlarge.search",
            "r3.large.search",
            "r3.xlarge.search",
            "r4.16xlarge.search",
            "r4.2xlarge.search",
            "r4.4xlarge.search",
            "r4.8xlarge.search",
            "r4.large.search",
            "r4.xlarge.search",
            "r5.12xlarge.search",
            "r5.24xlarge.search",
            "r5.2xlarge.search",
            "r5.4xlarge.search",
            "r5.large.search",
            "r5.xlarge.search",
            "r6g.12xlarge.search",
            "r6g.2xlarge.search",
            "r6g.4xlarge.search",
            "r6g.8xlarge.search",
            "r6g.large.search",
            "r6g.xlarge.search",
            "r6gd.12xlarge.search",
            "r6gd.16xlarge.search",
            "r6gd.2xlarge.search",
            "r6gd.4xlarge.search",
            "r6gd.8xlarge.search",
            "r6gd.large.search",
            "r6gd.xlarge.search",
            "t2.medium.search",
            "t2.micro.search",
            "t2.small.search",
            "t3.2xlarge.search",
            "t3.large.search",
            "t3.medium.search",
            "t3.micro.search",
            "t3.nano.search",
            "t3.small.search",
            "t3.xlarge.search",
            "t4g.medium.search",
            "t4g.small.search",
            "ultrawarm1.large.search",
            "ultrawarm1.medium.search",
            "ultrawarm1.xlarge.search",
        ]
    ] = Field(default=None, alias="DedicatedMasterType")
    dedicated_master_count: Optional[int] = Field(
        default=None, alias="DedicatedMasterCount"
    )
    warm_enabled: Optional[bool] = Field(default=None, alias="WarmEnabled")
    warm_type: Optional[
        Literal[
            "ultrawarm1.large.search",
            "ultrawarm1.medium.search",
            "ultrawarm1.xlarge.search",
        ]
    ] = Field(default=None, alias="WarmType")
    warm_count: Optional[int] = Field(default=None, alias="WarmCount")
    cold_storage_options: Optional[ColdStorageOptionsModel] = Field(
        default=None, alias="ColdStorageOptions"
    )


class CognitoOptionsStatusModel(BaseModel):
    options: CognitoOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class GetCompatibleVersionsResponseModel(BaseModel):
    compatible_versions: List[CompatibleVersionsMapModel] = Field(
        alias="CompatibleVersions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainEndpointOptionsStatusModel(BaseModel):
    options: DomainEndpointOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class EBSOptionsStatusModel(BaseModel):
    options: EBSOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class EncryptionAtRestOptionsStatusModel(BaseModel):
    options: EncryptionAtRestOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class LogPublishingOptionsStatusModel(BaseModel):
    options: Optional[
        Dict[
            Literal[
                "AUDIT_LOGS",
                "ES_APPLICATION_LOGS",
                "INDEX_SLOW_LOGS",
                "SEARCH_SLOW_LOGS",
            ],
            LogPublishingOptionModel,
        ]
    ] = Field(default=None, alias="Options")
    status: Optional[OptionStatusModel] = Field(default=None, alias="Status")


class NodeToNodeEncryptionOptionsStatusModel(BaseModel):
    options: NodeToNodeEncryptionOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class SnapshotOptionsStatusModel(BaseModel):
    options: SnapshotOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class SoftwareUpdateOptionsStatusModel(BaseModel):
    options: Optional[SoftwareUpdateOptionsModel] = Field(default=None, alias="Options")
    status: Optional[OptionStatusModel] = Field(default=None, alias="Status")


class CreateVpcEndpointRequestModel(BaseModel):
    domain_arn: str = Field(alias="DomainArn")
    vpc_options: VPCOptionsModel = Field(alias="VpcOptions")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class UpdateVpcEndpointRequestModel(BaseModel):
    vpc_endpoint_id: str = Field(alias="VpcEndpointId")
    vpc_options: VPCOptionsModel = Field(alias="VpcOptions")


class CreatePackageRequestModel(BaseModel):
    package_name: str = Field(alias="PackageName")
    package_type: Literal["TXT-DICTIONARY"] = Field(alias="PackageType")
    package_source: PackageSourceModel = Field(alias="PackageSource")
    package_description: Optional[str] = Field(default=None, alias="PackageDescription")


class UpdatePackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    package_source: PackageSourceModel = Field(alias="PackageSource")
    package_description: Optional[str] = Field(default=None, alias="PackageDescription")
    commit_message: Optional[str] = Field(default=None, alias="CommitMessage")


class DeleteVpcEndpointResponseModel(BaseModel):
    vpc_endpoint_summary: VpcEndpointSummaryModel = Field(alias="VpcEndpointSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVpcEndpointsForDomainResponseModel(BaseModel):
    vpc_endpoint_summary_list: List[VpcEndpointSummaryModel] = Field(
        alias="VpcEndpointSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVpcEndpointsResponseModel(BaseModel):
    vpc_endpoint_summary_list: List[VpcEndpointSummaryModel] = Field(
        alias="VpcEndpointSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInboundConnectionsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeOutboundConnectionsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePackagesRequestModel(BaseModel):
    filters: Optional[Sequence[DescribePackagesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDomainNamesResponseModel(BaseModel):
    domain_names: List[DomainInfoModel] = Field(alias="DomainNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainPackageDetailsModel(BaseModel):
    package_id: Optional[str] = Field(default=None, alias="PackageID")
    package_name: Optional[str] = Field(default=None, alias="PackageName")
    package_type: Optional[Literal["TXT-DICTIONARY"]] = Field(
        default=None, alias="PackageType"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    domain_package_status: Optional[
        Literal[
            "ACTIVE",
            "ASSOCIATING",
            "ASSOCIATION_FAILED",
            "DISSOCIATING",
            "DISSOCIATION_FAILED",
        ]
    ] = Field(default=None, alias="DomainPackageStatus")
    package_version: Optional[str] = Field(default=None, alias="PackageVersion")
    reference_path: Optional[str] = Field(default=None, alias="ReferencePath")
    error_details: Optional[ErrorDetailsModel] = Field(
        default=None, alias="ErrorDetails"
    )


class PackageDetailsModel(BaseModel):
    package_id: Optional[str] = Field(default=None, alias="PackageID")
    package_name: Optional[str] = Field(default=None, alias="PackageName")
    package_type: Optional[Literal["TXT-DICTIONARY"]] = Field(
        default=None, alias="PackageType"
    )
    package_description: Optional[str] = Field(default=None, alias="PackageDescription")
    package_status: Optional[
        Literal[
            "AVAILABLE",
            "COPYING",
            "COPY_FAILED",
            "DELETED",
            "DELETE_FAILED",
            "DELETING",
            "VALIDATING",
            "VALIDATION_FAILED",
        ]
    ] = Field(default=None, alias="PackageStatus")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    available_package_version: Optional[str] = Field(
        default=None, alias="AvailablePackageVersion"
    )
    error_details: Optional[ErrorDetailsModel] = Field(
        default=None, alias="ErrorDetails"
    )


class VPCDerivedInfoStatusModel(BaseModel):
    options: VPCDerivedInfoModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class VpcEndpointModel(BaseModel):
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")
    vpc_endpoint_owner: Optional[str] = Field(default=None, alias="VpcEndpointOwner")
    domain_arn: Optional[str] = Field(default=None, alias="DomainArn")
    vpc_options: Optional[VPCDerivedInfoModel] = Field(default=None, alias="VpcOptions")
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATE_FAILED",
            "CREATING",
            "DELETE_FAILED",
            "DELETING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")


class DryRunProgressStatusModel(BaseModel):
    dry_run_id: str = Field(alias="DryRunId")
    dry_run_status: str = Field(alias="DryRunStatus")
    creation_date: str = Field(alias="CreationDate")
    update_date: str = Field(alias="UpdateDate")
    validation_failures: Optional[List[ValidationFailureModel]] = Field(
        default=None, alias="ValidationFailures"
    )


class GetPackageVersionHistoryResponseModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    package_version_history_list: List[PackageVersionHistoryModel] = Field(
        alias="PackageVersionHistoryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceLimitsModel(BaseModel):
    instance_count_limits: Optional[InstanceCountLimitsModel] = Field(
        default=None, alias="InstanceCountLimits"
    )


class ListInstanceTypeDetailsResponseModel(BaseModel):
    instance_type_details: List[InstanceTypeDetailsModel] = Field(
        alias="InstanceTypeDetails"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListScheduledActionsResponseModel(BaseModel):
    scheduled_actions: List[ScheduledActionModel] = Field(alias="ScheduledActions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateScheduledActionResponseModel(BaseModel):
    scheduled_action: ScheduledActionModel = Field(alias="ScheduledAction")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OffPeakWindowModel(BaseModel):
    window_start_time: Optional[WindowStartTimeModel] = Field(
        default=None, alias="WindowStartTime"
    )


class ReservedInstanceOfferingModel(BaseModel):
    reserved_instance_offering_id: Optional[str] = Field(
        default=None, alias="ReservedInstanceOfferingId"
    )
    instance_type: Optional[
        Literal[
            "c4.2xlarge.search",
            "c4.4xlarge.search",
            "c4.8xlarge.search",
            "c4.large.search",
            "c4.xlarge.search",
            "c5.18xlarge.search",
            "c5.2xlarge.search",
            "c5.4xlarge.search",
            "c5.9xlarge.search",
            "c5.large.search",
            "c5.xlarge.search",
            "c6g.12xlarge.search",
            "c6g.2xlarge.search",
            "c6g.4xlarge.search",
            "c6g.8xlarge.search",
            "c6g.large.search",
            "c6g.xlarge.search",
            "d2.2xlarge.search",
            "d2.4xlarge.search",
            "d2.8xlarge.search",
            "d2.xlarge.search",
            "i2.2xlarge.search",
            "i2.xlarge.search",
            "i3.16xlarge.search",
            "i3.2xlarge.search",
            "i3.4xlarge.search",
            "i3.8xlarge.search",
            "i3.large.search",
            "i3.xlarge.search",
            "m3.2xlarge.search",
            "m3.large.search",
            "m3.medium.search",
            "m3.xlarge.search",
            "m4.10xlarge.search",
            "m4.2xlarge.search",
            "m4.4xlarge.search",
            "m4.large.search",
            "m4.xlarge.search",
            "m5.12xlarge.search",
            "m5.24xlarge.search",
            "m5.2xlarge.search",
            "m5.4xlarge.search",
            "m5.large.search",
            "m5.xlarge.search",
            "m6g.12xlarge.search",
            "m6g.2xlarge.search",
            "m6g.4xlarge.search",
            "m6g.8xlarge.search",
            "m6g.large.search",
            "m6g.xlarge.search",
            "r3.2xlarge.search",
            "r3.4xlarge.search",
            "r3.8xlarge.search",
            "r3.large.search",
            "r3.xlarge.search",
            "r4.16xlarge.search",
            "r4.2xlarge.search",
            "r4.4xlarge.search",
            "r4.8xlarge.search",
            "r4.large.search",
            "r4.xlarge.search",
            "r5.12xlarge.search",
            "r5.24xlarge.search",
            "r5.2xlarge.search",
            "r5.4xlarge.search",
            "r5.large.search",
            "r5.xlarge.search",
            "r6g.12xlarge.search",
            "r6g.2xlarge.search",
            "r6g.4xlarge.search",
            "r6g.8xlarge.search",
            "r6g.large.search",
            "r6g.xlarge.search",
            "r6gd.12xlarge.search",
            "r6gd.16xlarge.search",
            "r6gd.2xlarge.search",
            "r6gd.4xlarge.search",
            "r6gd.8xlarge.search",
            "r6gd.large.search",
            "r6gd.xlarge.search",
            "t2.medium.search",
            "t2.micro.search",
            "t2.small.search",
            "t3.2xlarge.search",
            "t3.large.search",
            "t3.medium.search",
            "t3.micro.search",
            "t3.nano.search",
            "t3.small.search",
            "t3.xlarge.search",
            "t4g.medium.search",
            "t4g.small.search",
            "ultrawarm1.large.search",
            "ultrawarm1.medium.search",
            "ultrawarm1.xlarge.search",
        ]
    ] = Field(default=None, alias="InstanceType")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    payment_option: Optional[
        Literal["ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"]
    ] = Field(default=None, alias="PaymentOption")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )


class ReservedInstanceModel(BaseModel):
    reservation_name: Optional[str] = Field(default=None, alias="ReservationName")
    reserved_instance_id: Optional[str] = Field(
        default=None, alias="ReservedInstanceId"
    )
    billing_subscription_id: Optional[int] = Field(
        default=None, alias="BillingSubscriptionId"
    )
    reserved_instance_offering_id: Optional[str] = Field(
        default=None, alias="ReservedInstanceOfferingId"
    )
    instance_type: Optional[
        Literal[
            "c4.2xlarge.search",
            "c4.4xlarge.search",
            "c4.8xlarge.search",
            "c4.large.search",
            "c4.xlarge.search",
            "c5.18xlarge.search",
            "c5.2xlarge.search",
            "c5.4xlarge.search",
            "c5.9xlarge.search",
            "c5.large.search",
            "c5.xlarge.search",
            "c6g.12xlarge.search",
            "c6g.2xlarge.search",
            "c6g.4xlarge.search",
            "c6g.8xlarge.search",
            "c6g.large.search",
            "c6g.xlarge.search",
            "d2.2xlarge.search",
            "d2.4xlarge.search",
            "d2.8xlarge.search",
            "d2.xlarge.search",
            "i2.2xlarge.search",
            "i2.xlarge.search",
            "i3.16xlarge.search",
            "i3.2xlarge.search",
            "i3.4xlarge.search",
            "i3.8xlarge.search",
            "i3.large.search",
            "i3.xlarge.search",
            "m3.2xlarge.search",
            "m3.large.search",
            "m3.medium.search",
            "m3.xlarge.search",
            "m4.10xlarge.search",
            "m4.2xlarge.search",
            "m4.4xlarge.search",
            "m4.large.search",
            "m4.xlarge.search",
            "m5.12xlarge.search",
            "m5.24xlarge.search",
            "m5.2xlarge.search",
            "m5.4xlarge.search",
            "m5.large.search",
            "m5.xlarge.search",
            "m6g.12xlarge.search",
            "m6g.2xlarge.search",
            "m6g.4xlarge.search",
            "m6g.8xlarge.search",
            "m6g.large.search",
            "m6g.xlarge.search",
            "r3.2xlarge.search",
            "r3.4xlarge.search",
            "r3.8xlarge.search",
            "r3.large.search",
            "r3.xlarge.search",
            "r4.16xlarge.search",
            "r4.2xlarge.search",
            "r4.4xlarge.search",
            "r4.8xlarge.search",
            "r4.large.search",
            "r4.xlarge.search",
            "r5.12xlarge.search",
            "r5.24xlarge.search",
            "r5.2xlarge.search",
            "r5.4xlarge.search",
            "r5.large.search",
            "r5.xlarge.search",
            "r6g.12xlarge.search",
            "r6g.2xlarge.search",
            "r6g.4xlarge.search",
            "r6g.8xlarge.search",
            "r6g.large.search",
            "r6g.xlarge.search",
            "r6gd.12xlarge.search",
            "r6gd.16xlarge.search",
            "r6gd.2xlarge.search",
            "r6gd.4xlarge.search",
            "r6gd.8xlarge.search",
            "r6gd.large.search",
            "r6gd.xlarge.search",
            "t2.medium.search",
            "t2.micro.search",
            "t2.small.search",
            "t3.2xlarge.search",
            "t3.large.search",
            "t3.medium.search",
            "t3.micro.search",
            "t3.nano.search",
            "t3.small.search",
            "t3.xlarge.search",
            "t4g.medium.search",
            "t4g.small.search",
            "ultrawarm1.large.search",
            "ultrawarm1.medium.search",
            "ultrawarm1.xlarge.search",
        ]
    ] = Field(default=None, alias="InstanceType")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    state: Optional[str] = Field(default=None, alias="State")
    payment_option: Optional[
        Literal["ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"]
    ] = Field(default=None, alias="PaymentOption")
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="RecurringCharges"
    )


class SAMLOptionsInputModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    idp: Optional[SAMLIdpModel] = Field(default=None, alias="Idp")
    master_user_name: Optional[str] = Field(default=None, alias="MasterUserName")
    master_backend_role: Optional[str] = Field(default=None, alias="MasterBackendRole")
    subject_key: Optional[str] = Field(default=None, alias="SubjectKey")
    roles_key: Optional[str] = Field(default=None, alias="RolesKey")
    session_timeout_minutes: Optional[int] = Field(
        default=None, alias="SessionTimeoutMinutes"
    )


class SAMLOptionsOutputModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    idp: Optional[SAMLIdpModel] = Field(default=None, alias="Idp")
    subject_key: Optional[str] = Field(default=None, alias="SubjectKey")
    roles_key: Optional[str] = Field(default=None, alias="RolesKey")
    session_timeout_minutes: Optional[int] = Field(
        default=None, alias="SessionTimeoutMinutes"
    )


class StorageTypeModel(BaseModel):
    storage_type_name: Optional[str] = Field(default=None, alias="StorageTypeName")
    storage_sub_type_name: Optional[str] = Field(
        default=None, alias="StorageSubTypeName"
    )
    storage_type_limits: Optional[List[StorageTypeLimitModel]] = Field(
        default=None, alias="StorageTypeLimits"
    )


class UpgradeHistoryModel(BaseModel):
    upgrade_name: Optional[str] = Field(default=None, alias="UpgradeName")
    start_timestamp: Optional[datetime] = Field(default=None, alias="StartTimestamp")
    upgrade_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES"]
    ] = Field(default=None, alias="UpgradeStatus")
    steps_list: Optional[List[UpgradeStepItemModel]] = Field(
        default=None, alias="StepsList"
    )


class CreateOutboundConnectionRequestModel(BaseModel):
    local_domain_info: DomainInformationContainerModel = Field(alias="LocalDomainInfo")
    remote_domain_info: DomainInformationContainerModel = Field(
        alias="RemoteDomainInfo"
    )
    connection_alias: str = Field(alias="ConnectionAlias")
    connection_mode: Optional[Literal["DIRECT", "VPC_ENDPOINT"]] = Field(
        default=None, alias="ConnectionMode"
    )


class CreateOutboundConnectionResponseModel(BaseModel):
    local_domain_info: DomainInformationContainerModel = Field(alias="LocalDomainInfo")
    remote_domain_info: DomainInformationContainerModel = Field(
        alias="RemoteDomainInfo"
    )
    connection_alias: str = Field(alias="ConnectionAlias")
    connection_status: OutboundConnectionStatusModel = Field(alias="ConnectionStatus")
    connection_id: str = Field(alias="ConnectionId")
    connection_mode: Literal["DIRECT", "VPC_ENDPOINT"] = Field(alias="ConnectionMode")
    connection_properties: ConnectionPropertiesModel = Field(
        alias="ConnectionProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InboundConnectionModel(BaseModel):
    local_domain_info: Optional[DomainInformationContainerModel] = Field(
        default=None, alias="LocalDomainInfo"
    )
    remote_domain_info: Optional[DomainInformationContainerModel] = Field(
        default=None, alias="RemoteDomainInfo"
    )
    connection_id: Optional[str] = Field(default=None, alias="ConnectionId")
    connection_status: Optional[InboundConnectionStatusModel] = Field(
        default=None, alias="ConnectionStatus"
    )
    connection_mode: Optional[Literal["DIRECT", "VPC_ENDPOINT"]] = Field(
        default=None, alias="ConnectionMode"
    )


class OutboundConnectionModel(BaseModel):
    local_domain_info: Optional[DomainInformationContainerModel] = Field(
        default=None, alias="LocalDomainInfo"
    )
    remote_domain_info: Optional[DomainInformationContainerModel] = Field(
        default=None, alias="RemoteDomainInfo"
    )
    connection_id: Optional[str] = Field(default=None, alias="ConnectionId")
    connection_alias: Optional[str] = Field(default=None, alias="ConnectionAlias")
    connection_status: Optional[OutboundConnectionStatusModel] = Field(
        default=None, alias="ConnectionStatus"
    )
    connection_mode: Optional[Literal["DIRECT", "VPC_ENDPOINT"]] = Field(
        default=None, alias="ConnectionMode"
    )
    connection_properties: Optional[ConnectionPropertiesModel] = Field(
        default=None, alias="ConnectionProperties"
    )


class AutoTuneModel(BaseModel):
    auto_tune_type: Optional[Literal["SCHEDULED_ACTION"]] = Field(
        default=None, alias="AutoTuneType"
    )
    auto_tune_details: Optional[AutoTuneDetailsModel] = Field(
        default=None, alias="AutoTuneDetails"
    )


class AutoTuneOptionsInputModel(BaseModel):
    desired_state: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DesiredState"
    )
    maintenance_schedules: Optional[Sequence[AutoTuneMaintenanceScheduleModel]] = Field(
        default=None, alias="MaintenanceSchedules"
    )
    use_off_peak_window: Optional[bool] = Field(default=None, alias="UseOffPeakWindow")


class AutoTuneOptionsModel(BaseModel):
    desired_state: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DesiredState"
    )
    rollback_on_disable: Optional[Literal["DEFAULT_ROLLBACK", "NO_ROLLBACK"]] = Field(
        default=None, alias="RollbackOnDisable"
    )
    maintenance_schedules: Optional[List[AutoTuneMaintenanceScheduleModel]] = Field(
        default=None, alias="MaintenanceSchedules"
    )
    use_off_peak_window: Optional[bool] = Field(default=None, alias="UseOffPeakWindow")


class DescribeDomainChangeProgressResponseModel(BaseModel):
    change_progress_status: ChangeProgressStatusDetailsModel = Field(
        alias="ChangeProgressStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ClusterConfigStatusModel(BaseModel):
    options: ClusterConfigModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class AssociatePackageResponseModel(BaseModel):
    domain_package_details: DomainPackageDetailsModel = Field(
        alias="DomainPackageDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DissociatePackageResponseModel(BaseModel):
    domain_package_details: DomainPackageDetailsModel = Field(
        alias="DomainPackageDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsForPackageResponseModel(BaseModel):
    domain_package_details_list: List[DomainPackageDetailsModel] = Field(
        alias="DomainPackageDetailsList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPackagesForDomainResponseModel(BaseModel):
    domain_package_details_list: List[DomainPackageDetailsModel] = Field(
        alias="DomainPackageDetailsList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePackageResponseModel(BaseModel):
    package_details: PackageDetailsModel = Field(alias="PackageDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeletePackageResponseModel(BaseModel):
    package_details: PackageDetailsModel = Field(alias="PackageDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePackagesResponseModel(BaseModel):
    package_details_list: List[PackageDetailsModel] = Field(alias="PackageDetailsList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePackageResponseModel(BaseModel):
    package_details: PackageDetailsModel = Field(alias="PackageDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVpcEndpointResponseModel(BaseModel):
    vpc_endpoint: VpcEndpointModel = Field(alias="VpcEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeVpcEndpointsResponseModel(BaseModel):
    vpc_endpoints: List[VpcEndpointModel] = Field(alias="VpcEndpoints")
    vpc_endpoint_errors: List[VpcEndpointErrorModel] = Field(alias="VpcEndpointErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVpcEndpointResponseModel(BaseModel):
    vpc_endpoint: VpcEndpointModel = Field(alias="VpcEndpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OffPeakWindowOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    off_peak_window: Optional[OffPeakWindowModel] = Field(
        default=None, alias="OffPeakWindow"
    )


class DescribeReservedInstanceOfferingsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reserved_instance_offerings: List[ReservedInstanceOfferingModel] = Field(
        alias="ReservedInstanceOfferings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReservedInstancesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reserved_instances: List[ReservedInstanceModel] = Field(alias="ReservedInstances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AdvancedSecurityOptionsInputModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    internal_user_database_enabled: Optional[bool] = Field(
        default=None, alias="InternalUserDatabaseEnabled"
    )
    master_user_options: Optional[MasterUserOptionsModel] = Field(
        default=None, alias="MasterUserOptions"
    )
    s_aml_options: Optional[SAMLOptionsInputModel] = Field(
        default=None, alias="SAMLOptions"
    )
    anonymous_auth_enabled: Optional[bool] = Field(
        default=None, alias="AnonymousAuthEnabled"
    )


class AdvancedSecurityOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    internal_user_database_enabled: Optional[bool] = Field(
        default=None, alias="InternalUserDatabaseEnabled"
    )
    s_aml_options: Optional[SAMLOptionsOutputModel] = Field(
        default=None, alias="SAMLOptions"
    )
    anonymous_auth_disable_date: Optional[datetime] = Field(
        default=None, alias="AnonymousAuthDisableDate"
    )
    anonymous_auth_enabled: Optional[bool] = Field(
        default=None, alias="AnonymousAuthEnabled"
    )


class LimitsModel(BaseModel):
    storage_types: Optional[List[StorageTypeModel]] = Field(
        default=None, alias="StorageTypes"
    )
    instance_limits: Optional[InstanceLimitsModel] = Field(
        default=None, alias="InstanceLimits"
    )
    additional_limits: Optional[List[AdditionalLimitModel]] = Field(
        default=None, alias="AdditionalLimits"
    )


class GetUpgradeHistoryResponseModel(BaseModel):
    upgrade_histories: List[UpgradeHistoryModel] = Field(alias="UpgradeHistories")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AcceptInboundConnectionResponseModel(BaseModel):
    connection: InboundConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInboundConnectionResponseModel(BaseModel):
    connection: InboundConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInboundConnectionsResponseModel(BaseModel):
    connections: List[InboundConnectionModel] = Field(alias="Connections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectInboundConnectionResponseModel(BaseModel):
    connection: InboundConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteOutboundConnectionResponseModel(BaseModel):
    connection: OutboundConnectionModel = Field(alias="Connection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOutboundConnectionsResponseModel(BaseModel):
    connections: List[OutboundConnectionModel] = Field(alias="Connections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainAutoTunesResponseModel(BaseModel):
    auto_tunes: List[AutoTuneModel] = Field(alias="AutoTunes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoTuneOptionsStatusModel(BaseModel):
    options: Optional[AutoTuneOptionsModel] = Field(default=None, alias="Options")
    status: Optional[AutoTuneStatusModel] = Field(default=None, alias="Status")


class OffPeakWindowOptionsStatusModel(BaseModel):
    options: Optional[OffPeakWindowOptionsModel] = Field(default=None, alias="Options")
    status: Optional[OptionStatusModel] = Field(default=None, alias="Status")


class CreateDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    cluster_config: Optional[ClusterConfigModel] = Field(
        default=None, alias="ClusterConfig"
    )
    ebs_options: Optional[EBSOptionsModel] = Field(default=None, alias="EBSOptions")
    access_policies: Optional[str] = Field(default=None, alias="AccessPolicies")
    snapshot_options: Optional[SnapshotOptionsModel] = Field(
        default=None, alias="SnapshotOptions"
    )
    vp_coptions: Optional[VPCOptionsModel] = Field(default=None, alias="VPCOptions")
    cognito_options: Optional[CognitoOptionsModel] = Field(
        default=None, alias="CognitoOptions"
    )
    encryption_at_rest_options: Optional[EncryptionAtRestOptionsModel] = Field(
        default=None, alias="EncryptionAtRestOptions"
    )
    node_to_node_encryption_options: Optional[NodeToNodeEncryptionOptionsModel] = Field(
        default=None, alias="NodeToNodeEncryptionOptions"
    )
    advanced_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="AdvancedOptions"
    )
    log_publishing_options: Optional[
        Mapping[
            Literal[
                "AUDIT_LOGS",
                "ES_APPLICATION_LOGS",
                "INDEX_SLOW_LOGS",
                "SEARCH_SLOW_LOGS",
            ],
            LogPublishingOptionModel,
        ]
    ] = Field(default=None, alias="LogPublishingOptions")
    domain_endpoint_options: Optional[DomainEndpointOptionsModel] = Field(
        default=None, alias="DomainEndpointOptions"
    )
    advanced_security_options: Optional[AdvancedSecurityOptionsInputModel] = Field(
        default=None, alias="AdvancedSecurityOptions"
    )
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")
    auto_tune_options: Optional[AutoTuneOptionsInputModel] = Field(
        default=None, alias="AutoTuneOptions"
    )
    off_peak_window_options: Optional[OffPeakWindowOptionsModel] = Field(
        default=None, alias="OffPeakWindowOptions"
    )
    software_update_options: Optional[SoftwareUpdateOptionsModel] = Field(
        default=None, alias="SoftwareUpdateOptions"
    )


class UpdateDomainConfigRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    cluster_config: Optional[ClusterConfigModel] = Field(
        default=None, alias="ClusterConfig"
    )
    ebs_options: Optional[EBSOptionsModel] = Field(default=None, alias="EBSOptions")
    snapshot_options: Optional[SnapshotOptionsModel] = Field(
        default=None, alias="SnapshotOptions"
    )
    vp_coptions: Optional[VPCOptionsModel] = Field(default=None, alias="VPCOptions")
    cognito_options: Optional[CognitoOptionsModel] = Field(
        default=None, alias="CognitoOptions"
    )
    advanced_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="AdvancedOptions"
    )
    access_policies: Optional[str] = Field(default=None, alias="AccessPolicies")
    log_publishing_options: Optional[
        Mapping[
            Literal[
                "AUDIT_LOGS",
                "ES_APPLICATION_LOGS",
                "INDEX_SLOW_LOGS",
                "SEARCH_SLOW_LOGS",
            ],
            LogPublishingOptionModel,
        ]
    ] = Field(default=None, alias="LogPublishingOptions")
    encryption_at_rest_options: Optional[EncryptionAtRestOptionsModel] = Field(
        default=None, alias="EncryptionAtRestOptions"
    )
    domain_endpoint_options: Optional[DomainEndpointOptionsModel] = Field(
        default=None, alias="DomainEndpointOptions"
    )
    node_to_node_encryption_options: Optional[NodeToNodeEncryptionOptionsModel] = Field(
        default=None, alias="NodeToNodeEncryptionOptions"
    )
    advanced_security_options: Optional[AdvancedSecurityOptionsInputModel] = Field(
        default=None, alias="AdvancedSecurityOptions"
    )
    auto_tune_options: Optional[AutoTuneOptionsModel] = Field(
        default=None, alias="AutoTuneOptions"
    )
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")
    dry_run_mode: Optional[Literal["Basic", "Verbose"]] = Field(
        default=None, alias="DryRunMode"
    )
    off_peak_window_options: Optional[OffPeakWindowOptionsModel] = Field(
        default=None, alias="OffPeakWindowOptions"
    )
    software_update_options: Optional[SoftwareUpdateOptionsModel] = Field(
        default=None, alias="SoftwareUpdateOptions"
    )


class AdvancedSecurityOptionsStatusModel(BaseModel):
    options: AdvancedSecurityOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class DomainStatusModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    domain_name: str = Field(alias="DomainName")
    arn: str = Field(alias="ARN")
    cluster_config: ClusterConfigModel = Field(alias="ClusterConfig")
    created: Optional[bool] = Field(default=None, alias="Created")
    deleted: Optional[bool] = Field(default=None, alias="Deleted")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    endpoints: Optional[Dict[str, str]] = Field(default=None, alias="Endpoints")
    processing: Optional[bool] = Field(default=None, alias="Processing")
    upgrade_processing: Optional[bool] = Field(default=None, alias="UpgradeProcessing")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    ebs_options: Optional[EBSOptionsModel] = Field(default=None, alias="EBSOptions")
    access_policies: Optional[str] = Field(default=None, alias="AccessPolicies")
    snapshot_options: Optional[SnapshotOptionsModel] = Field(
        default=None, alias="SnapshotOptions"
    )
    vp_coptions: Optional[VPCDerivedInfoModel] = Field(default=None, alias="VPCOptions")
    cognito_options: Optional[CognitoOptionsModel] = Field(
        default=None, alias="CognitoOptions"
    )
    encryption_at_rest_options: Optional[EncryptionAtRestOptionsModel] = Field(
        default=None, alias="EncryptionAtRestOptions"
    )
    node_to_node_encryption_options: Optional[NodeToNodeEncryptionOptionsModel] = Field(
        default=None, alias="NodeToNodeEncryptionOptions"
    )
    advanced_options: Optional[Dict[str, str]] = Field(
        default=None, alias="AdvancedOptions"
    )
    log_publishing_options: Optional[
        Dict[
            Literal[
                "AUDIT_LOGS",
                "ES_APPLICATION_LOGS",
                "INDEX_SLOW_LOGS",
                "SEARCH_SLOW_LOGS",
            ],
            LogPublishingOptionModel,
        ]
    ] = Field(default=None, alias="LogPublishingOptions")
    service_software_options: Optional[ServiceSoftwareOptionsModel] = Field(
        default=None, alias="ServiceSoftwareOptions"
    )
    domain_endpoint_options: Optional[DomainEndpointOptionsModel] = Field(
        default=None, alias="DomainEndpointOptions"
    )
    advanced_security_options: Optional[AdvancedSecurityOptionsModel] = Field(
        default=None, alias="AdvancedSecurityOptions"
    )
    auto_tune_options: Optional[AutoTuneOptionsOutputModel] = Field(
        default=None, alias="AutoTuneOptions"
    )
    change_progress_details: Optional[ChangeProgressDetailsModel] = Field(
        default=None, alias="ChangeProgressDetails"
    )
    off_peak_window_options: Optional[OffPeakWindowOptionsModel] = Field(
        default=None, alias="OffPeakWindowOptions"
    )
    software_update_options: Optional[SoftwareUpdateOptionsModel] = Field(
        default=None, alias="SoftwareUpdateOptions"
    )


class DescribeInstanceTypeLimitsResponseModel(BaseModel):
    limits_by_role: Dict[str, LimitsModel] = Field(alias="LimitsByRole")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainConfigModel(BaseModel):
    engine_version: Optional[VersionStatusModel] = Field(
        default=None, alias="EngineVersion"
    )
    cluster_config: Optional[ClusterConfigStatusModel] = Field(
        default=None, alias="ClusterConfig"
    )
    ebs_options: Optional[EBSOptionsStatusModel] = Field(
        default=None, alias="EBSOptions"
    )
    access_policies: Optional[AccessPoliciesStatusModel] = Field(
        default=None, alias="AccessPolicies"
    )
    snapshot_options: Optional[SnapshotOptionsStatusModel] = Field(
        default=None, alias="SnapshotOptions"
    )
    vp_coptions: Optional[VPCDerivedInfoStatusModel] = Field(
        default=None, alias="VPCOptions"
    )
    cognito_options: Optional[CognitoOptionsStatusModel] = Field(
        default=None, alias="CognitoOptions"
    )
    encryption_at_rest_options: Optional[EncryptionAtRestOptionsStatusModel] = Field(
        default=None, alias="EncryptionAtRestOptions"
    )
    node_to_node_encryption_options: Optional[
        NodeToNodeEncryptionOptionsStatusModel
    ] = Field(default=None, alias="NodeToNodeEncryptionOptions")
    advanced_options: Optional[AdvancedOptionsStatusModel] = Field(
        default=None, alias="AdvancedOptions"
    )
    log_publishing_options: Optional[LogPublishingOptionsStatusModel] = Field(
        default=None, alias="LogPublishingOptions"
    )
    domain_endpoint_options: Optional[DomainEndpointOptionsStatusModel] = Field(
        default=None, alias="DomainEndpointOptions"
    )
    advanced_security_options: Optional[AdvancedSecurityOptionsStatusModel] = Field(
        default=None, alias="AdvancedSecurityOptions"
    )
    auto_tune_options: Optional[AutoTuneOptionsStatusModel] = Field(
        default=None, alias="AutoTuneOptions"
    )
    change_progress_details: Optional[ChangeProgressDetailsModel] = Field(
        default=None, alias="ChangeProgressDetails"
    )
    off_peak_window_options: Optional[OffPeakWindowOptionsStatusModel] = Field(
        default=None, alias="OffPeakWindowOptions"
    )
    software_update_options: Optional[SoftwareUpdateOptionsStatusModel] = Field(
        default=None, alias="SoftwareUpdateOptions"
    )


class CreateDomainResponseModel(BaseModel):
    domain_status: DomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainResponseModel(BaseModel):
    domain_status: DomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainResponseModel(BaseModel):
    domain_status: DomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainsResponseModel(BaseModel):
    domain_status_list: List[DomainStatusModel] = Field(alias="DomainStatusList")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDryRunProgressResponseModel(BaseModel):
    dry_run_progress_status: DryRunProgressStatusModel = Field(
        alias="DryRunProgressStatus"
    )
    dry_run_config: DomainStatusModel = Field(alias="DryRunConfig")
    dry_run_results: DryRunResultsModel = Field(alias="DryRunResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDomainConfigResponseModel(BaseModel):
    domain_config: DomainConfigModel = Field(alias="DomainConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainConfigResponseModel(BaseModel):
    domain_config: DomainConfigModel = Field(alias="DomainConfig")
    dry_run_results: DryRunResultsModel = Field(alias="DryRunResults")
    dry_run_progress_status: DryRunProgressStatusModel = Field(
        alias="DryRunProgressStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
