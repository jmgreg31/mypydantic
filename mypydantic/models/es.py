# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptInboundCrossClusterSearchConnectionRequestModel(BaseModel):
    cross_cluster_search_connection_id: str = Field(
        alias="CrossClusterSearchConnectionId"
    )


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


class CancelElasticsearchServiceSoftwareUpdateRequestModel(BaseModel):
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


class CognitoOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    user_pool_id: Optional[str] = Field(default=None, alias="UserPoolId")
    identity_pool_id: Optional[str] = Field(default=None, alias="IdentityPoolId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class ColdStorageOptionsModel(BaseModel):
    enabled: bool = Field(alias="Enabled")


class CompatibleVersionsMapModel(BaseModel):
    source_version: Optional[str] = Field(default=None, alias="SourceVersion")
    target_versions: Optional[List[str]] = Field(default=None, alias="TargetVersions")


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


class VPCOptionsModel(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class DomainInformationModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    region: Optional[str] = Field(default=None, alias="Region")


class OutboundCrossClusterSearchConnectionStatusModel(BaseModel):
    status_code: Optional[
        Literal[
            "ACTIVE",
            "DELETED",
            "DELETING",
            "PENDING_ACCEPTANCE",
            "PROVISIONING",
            "REJECTED",
            "VALIDATING",
            "VALIDATION_FAILED",
        ]
    ] = Field(default=None, alias="StatusCode")
    message: Optional[str] = Field(default=None, alias="Message")


class PackageSourceModel(BaseModel):
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")


class DeleteElasticsearchDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DeleteInboundCrossClusterSearchConnectionRequestModel(BaseModel):
    cross_cluster_search_connection_id: str = Field(
        alias="CrossClusterSearchConnectionId"
    )


class DeleteOutboundCrossClusterSearchConnectionRequestModel(BaseModel):
    cross_cluster_search_connection_id: str = Field(
        alias="CrossClusterSearchConnectionId"
    )


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


class DescribeElasticsearchDomainConfigRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DescribeElasticsearchDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DescribeElasticsearchDomainsRequestModel(BaseModel):
    domain_names: Sequence[str] = Field(alias="DomainNames")


class DescribeElasticsearchInstanceTypeLimitsRequestModel(BaseModel):
    instance_type: Literal[
        "c4.2xlarge.elasticsearch",
        "c4.4xlarge.elasticsearch",
        "c4.8xlarge.elasticsearch",
        "c4.large.elasticsearch",
        "c4.xlarge.elasticsearch",
        "c5.18xlarge.elasticsearch",
        "c5.2xlarge.elasticsearch",
        "c5.4xlarge.elasticsearch",
        "c5.9xlarge.elasticsearch",
        "c5.large.elasticsearch",
        "c5.xlarge.elasticsearch",
        "d2.2xlarge.elasticsearch",
        "d2.4xlarge.elasticsearch",
        "d2.8xlarge.elasticsearch",
        "d2.xlarge.elasticsearch",
        "i2.2xlarge.elasticsearch",
        "i2.xlarge.elasticsearch",
        "i3.16xlarge.elasticsearch",
        "i3.2xlarge.elasticsearch",
        "i3.4xlarge.elasticsearch",
        "i3.8xlarge.elasticsearch",
        "i3.large.elasticsearch",
        "i3.xlarge.elasticsearch",
        "m3.2xlarge.elasticsearch",
        "m3.large.elasticsearch",
        "m3.medium.elasticsearch",
        "m3.xlarge.elasticsearch",
        "m4.10xlarge.elasticsearch",
        "m4.2xlarge.elasticsearch",
        "m4.4xlarge.elasticsearch",
        "m4.large.elasticsearch",
        "m4.xlarge.elasticsearch",
        "m5.12xlarge.elasticsearch",
        "m5.2xlarge.elasticsearch",
        "m5.4xlarge.elasticsearch",
        "m5.large.elasticsearch",
        "m5.xlarge.elasticsearch",
        "r3.2xlarge.elasticsearch",
        "r3.4xlarge.elasticsearch",
        "r3.8xlarge.elasticsearch",
        "r3.large.elasticsearch",
        "r3.xlarge.elasticsearch",
        "r4.16xlarge.elasticsearch",
        "r4.2xlarge.elasticsearch",
        "r4.4xlarge.elasticsearch",
        "r4.8xlarge.elasticsearch",
        "r4.large.elasticsearch",
        "r4.xlarge.elasticsearch",
        "r5.12xlarge.elasticsearch",
        "r5.2xlarge.elasticsearch",
        "r5.4xlarge.elasticsearch",
        "r5.large.elasticsearch",
        "r5.xlarge.elasticsearch",
        "t2.medium.elasticsearch",
        "t2.micro.elasticsearch",
        "t2.small.elasticsearch",
        "ultrawarm1.large.elasticsearch",
        "ultrawarm1.medium.elasticsearch",
    ] = Field(alias="InstanceType")
    elasticsearch_version: str = Field(alias="ElasticsearchVersion")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")


class FilterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class DescribePackagesFilterModel(BaseModel):
    name: Optional[Literal["PackageID", "PackageName", "PackageStatus"]] = Field(
        default=None, alias="Name"
    )
    value: Optional[Sequence[str]] = Field(default=None, alias="Value")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeReservedElasticsearchInstanceOfferingsRequestModel(BaseModel):
    reserved_elasticsearch_instance_offering_id: Optional[str] = Field(
        default=None, alias="ReservedElasticsearchInstanceOfferingId"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeReservedElasticsearchInstancesRequestModel(BaseModel):
    reserved_elasticsearch_instance_id: Optional[str] = Field(
        default=None, alias="ReservedElasticsearchInstanceId"
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


class DryRunResultsModel(BaseModel):
    deployment_type: Optional[str] = Field(default=None, alias="DeploymentType")
    message: Optional[str] = Field(default=None, alias="Message")


class ZoneAwarenessConfigModel(BaseModel):
    availability_zone_count: Optional[int] = Field(
        default=None, alias="AvailabilityZoneCount"
    )


class VPCDerivedInfoModel(BaseModel):
    vp_cid: Optional[str] = Field(default=None, alias="VPCId")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="SubnetIds")
    availability_zones: Optional[List[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class GetCompatibleElasticsearchVersionsRequestModel(BaseModel):
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


class InboundCrossClusterSearchConnectionStatusModel(BaseModel):
    status_code: Optional[
        Literal[
            "APPROVED",
            "DELETED",
            "DELETING",
            "PENDING_ACCEPTANCE",
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


class ListDomainNamesRequestModel(BaseModel):
    engine_type: Optional[Literal["Elasticsearch", "OpenSearch"]] = Field(
        default=None, alias="EngineType"
    )


class ListDomainsForPackageRequestModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListElasticsearchInstanceTypesRequestModel(BaseModel):
    elasticsearch_version: str = Field(alias="ElasticsearchVersion")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListElasticsearchVersionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPackagesForDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsRequestModel(BaseModel):
    arn: str = Field(alias="ARN")


class ListVpcEndpointAccessRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVpcEndpointsForDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListVpcEndpointsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PurchaseReservedElasticsearchInstanceOfferingRequestModel(BaseModel):
    reserved_elasticsearch_instance_offering_id: str = Field(
        alias="ReservedElasticsearchInstanceOfferingId"
    )
    reservation_name: str = Field(alias="ReservationName")
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")


class RecurringChargeModel(BaseModel):
    recurring_charge_amount: Optional[float] = Field(
        default=None, alias="RecurringChargeAmount"
    )
    recurring_charge_frequency: Optional[str] = Field(
        default=None, alias="RecurringChargeFrequency"
    )


class RejectInboundCrossClusterSearchConnectionRequestModel(BaseModel):
    cross_cluster_search_connection_id: str = Field(
        alias="CrossClusterSearchConnectionId"
    )


class RemoveTagsRequestModel(BaseModel):
    arn: str = Field(alias="ARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class RevokeVpcEndpointAccessRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    account: str = Field(alias="Account")


class SAMLIdpModel(BaseModel):
    metadata_content: str = Field(alias="MetadataContent")
    entity_id: str = Field(alias="EntityId")


class StartElasticsearchServiceSoftwareUpdateRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class StorageTypeLimitModel(BaseModel):
    limit_name: Optional[str] = Field(default=None, alias="LimitName")
    limit_values: Optional[List[str]] = Field(default=None, alias="LimitValues")


class UpgradeElasticsearchDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    target_version: str = Field(alias="TargetVersion")
    perform_check_only: Optional[bool] = Field(default=None, alias="PerformCheckOnly")


class UpgradeStepItemModel(BaseModel):
    upgrade_step: Optional[Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"]] = Field(
        default=None, alias="UpgradeStep"
    )
    upgrade_step_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES"]
    ] = Field(default=None, alias="UpgradeStepStatus")
    issues: Optional[List[str]] = Field(default=None, alias="Issues")
    progress_percent: Optional[float] = Field(default=None, alias="ProgressPercent")


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


class ListElasticsearchInstanceTypesResponseModel(BaseModel):
    elasticsearch_instance_types: List[
        Literal[
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m3.large.elasticsearch",
            "m3.medium.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "t2.medium.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
        ]
    ] = Field(alias="ElasticsearchInstanceTypes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListElasticsearchVersionsResponseModel(BaseModel):
    elasticsearch_versions: List[str] = Field(alias="ElasticsearchVersions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseReservedElasticsearchInstanceOfferingResponseModel(BaseModel):
    reserved_elasticsearch_instance_id: str = Field(
        alias="ReservedElasticsearchInstanceId"
    )
    reservation_name: str = Field(alias="ReservationName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AccessPoliciesStatusModel(BaseModel):
    options: str = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class AdvancedOptionsStatusModel(BaseModel):
    options: Dict[str, str] = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class ElasticsearchVersionStatusModel(BaseModel):
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


class CancelElasticsearchServiceSoftwareUpdateResponseModel(BaseModel):
    service_software_options: ServiceSoftwareOptionsModel = Field(
        alias="ServiceSoftwareOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartElasticsearchServiceSoftwareUpdateResponseModel(BaseModel):
    service_software_options: ServiceSoftwareOptionsModel = Field(
        alias="ServiceSoftwareOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpgradeElasticsearchDomainResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    target_version: str = Field(alias="TargetVersion")
    perform_check_only: bool = Field(alias="PerformCheckOnly")
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


class CognitoOptionsStatusModel(BaseModel):
    options: CognitoOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class GetCompatibleElasticsearchVersionsResponseModel(BaseModel):
    compatible_elasticsearch_versions: List[CompatibleVersionsMapModel] = Field(
        alias="CompatibleElasticsearchVersions"
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


class CreateVpcEndpointRequestModel(BaseModel):
    domain_arn: str = Field(alias="DomainArn")
    vpc_options: VPCOptionsModel = Field(alias="VpcOptions")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class UpdateVpcEndpointRequestModel(BaseModel):
    vpc_endpoint_id: str = Field(alias="VpcEndpointId")
    vpc_options: VPCOptionsModel = Field(alias="VpcOptions")


class CreateOutboundCrossClusterSearchConnectionRequestModel(BaseModel):
    source_domain_info: DomainInformationModel = Field(alias="SourceDomainInfo")
    destination_domain_info: DomainInformationModel = Field(
        alias="DestinationDomainInfo"
    )
    connection_alias: str = Field(alias="ConnectionAlias")


class CreateOutboundCrossClusterSearchConnectionResponseModel(BaseModel):
    source_domain_info: DomainInformationModel = Field(alias="SourceDomainInfo")
    destination_domain_info: DomainInformationModel = Field(
        alias="DestinationDomainInfo"
    )
    connection_alias: str = Field(alias="ConnectionAlias")
    connection_status: OutboundCrossClusterSearchConnectionStatusModel = Field(
        alias="ConnectionStatus"
    )
    cross_cluster_search_connection_id: str = Field(
        alias="CrossClusterSearchConnectionId"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OutboundCrossClusterSearchConnectionModel(BaseModel):
    source_domain_info: Optional[DomainInformationModel] = Field(
        default=None, alias="SourceDomainInfo"
    )
    destination_domain_info: Optional[DomainInformationModel] = Field(
        default=None, alias="DestinationDomainInfo"
    )
    cross_cluster_search_connection_id: Optional[str] = Field(
        default=None, alias="CrossClusterSearchConnectionId"
    )
    connection_alias: Optional[str] = Field(default=None, alias="ConnectionAlias")
    connection_status: Optional[
        OutboundCrossClusterSearchConnectionStatusModel
    ] = Field(default=None, alias="ConnectionStatus")


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


class DescribeInboundCrossClusterSearchConnectionsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeOutboundCrossClusterSearchConnectionsRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePackagesRequestModel(BaseModel):
    filters: Optional[Sequence[DescribePackagesFilterModel]] = Field(
        default=None, alias="Filters"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeReservedElasticsearchInstanceOfferingsRequestDescribeReservedElasticsearchInstanceOfferingsPaginateModel(
    BaseModel
):
    reserved_elasticsearch_instance_offering_id: Optional[str] = Field(
        default=None, alias="ReservedElasticsearchInstanceOfferingId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeReservedElasticsearchInstancesRequestDescribeReservedElasticsearchInstancesPaginateModel(
    BaseModel
):
    reserved_elasticsearch_instance_id: Optional[str] = Field(
        default=None, alias="ReservedElasticsearchInstanceId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetUpgradeHistoryRequestGetUpgradeHistoryPaginateModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListElasticsearchInstanceTypesRequestListElasticsearchInstanceTypesPaginateModel(
    BaseModel
):
    elasticsearch_version: str = Field(alias="ElasticsearchVersion")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListElasticsearchVersionsRequestListElasticsearchVersionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


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


class ElasticsearchClusterConfigModel(BaseModel):
    instance_type: Optional[
        Literal[
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m3.large.elasticsearch",
            "m3.medium.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "t2.medium.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
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
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m3.large.elasticsearch",
            "m3.medium.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "t2.medium.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
        ]
    ] = Field(default=None, alias="DedicatedMasterType")
    dedicated_master_count: Optional[int] = Field(
        default=None, alias="DedicatedMasterCount"
    )
    warm_enabled: Optional[bool] = Field(default=None, alias="WarmEnabled")
    warm_type: Optional[
        Literal["ultrawarm1.large.elasticsearch", "ultrawarm1.medium.elasticsearch"]
    ] = Field(default=None, alias="WarmType")
    warm_count: Optional[int] = Field(default=None, alias="WarmCount")
    cold_storage_options: Optional[ColdStorageOptionsModel] = Field(
        default=None, alias="ColdStorageOptions"
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


class GetPackageVersionHistoryResponseModel(BaseModel):
    package_id: str = Field(alias="PackageID")
    package_version_history_list: List[PackageVersionHistoryModel] = Field(
        alias="PackageVersionHistoryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InboundCrossClusterSearchConnectionModel(BaseModel):
    source_domain_info: Optional[DomainInformationModel] = Field(
        default=None, alias="SourceDomainInfo"
    )
    destination_domain_info: Optional[DomainInformationModel] = Field(
        default=None, alias="DestinationDomainInfo"
    )
    cross_cluster_search_connection_id: Optional[str] = Field(
        default=None, alias="CrossClusterSearchConnectionId"
    )
    connection_status: Optional[InboundCrossClusterSearchConnectionStatusModel] = Field(
        default=None, alias="ConnectionStatus"
    )


class InstanceLimitsModel(BaseModel):
    instance_count_limits: Optional[InstanceCountLimitsModel] = Field(
        default=None, alias="InstanceCountLimits"
    )


class ReservedElasticsearchInstanceOfferingModel(BaseModel):
    reserved_elasticsearch_instance_offering_id: Optional[str] = Field(
        default=None, alias="ReservedElasticsearchInstanceOfferingId"
    )
    elasticsearch_instance_type: Optional[
        Literal[
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m3.large.elasticsearch",
            "m3.medium.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "t2.medium.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
        ]
    ] = Field(default=None, alias="ElasticsearchInstanceType")
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


class ReservedElasticsearchInstanceModel(BaseModel):
    reservation_name: Optional[str] = Field(default=None, alias="ReservationName")
    reserved_elasticsearch_instance_id: Optional[str] = Field(
        default=None, alias="ReservedElasticsearchInstanceId"
    )
    reserved_elasticsearch_instance_offering_id: Optional[str] = Field(
        default=None, alias="ReservedElasticsearchInstanceOfferingId"
    )
    elasticsearch_instance_type: Optional[
        Literal[
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m3.large.elasticsearch",
            "m3.medium.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "t2.medium.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
        ]
    ] = Field(default=None, alias="ElasticsearchInstanceType")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    duration: Optional[int] = Field(default=None, alias="Duration")
    fixed_price: Optional[float] = Field(default=None, alias="FixedPrice")
    usage_price: Optional[float] = Field(default=None, alias="UsagePrice")
    currency_code: Optional[str] = Field(default=None, alias="CurrencyCode")
    elasticsearch_instance_count: Optional[int] = Field(
        default=None, alias="ElasticsearchInstanceCount"
    )
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


class DescribeDomainChangeProgressResponseModel(BaseModel):
    change_progress_status: ChangeProgressStatusDetailsModel = Field(
        alias="ChangeProgressStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteOutboundCrossClusterSearchConnectionResponseModel(BaseModel):
    cross_cluster_search_connection: OutboundCrossClusterSearchConnectionModel = Field(
        alias="CrossClusterSearchConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOutboundCrossClusterSearchConnectionsResponseModel(BaseModel):
    cross_cluster_search_connections: List[
        OutboundCrossClusterSearchConnectionModel
    ] = Field(alias="CrossClusterSearchConnections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


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


class ElasticsearchClusterConfigStatusModel(BaseModel):
    options: ElasticsearchClusterConfigModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


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


class AcceptInboundCrossClusterSearchConnectionResponseModel(BaseModel):
    cross_cluster_search_connection: InboundCrossClusterSearchConnectionModel = Field(
        alias="CrossClusterSearchConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInboundCrossClusterSearchConnectionResponseModel(BaseModel):
    cross_cluster_search_connection: InboundCrossClusterSearchConnectionModel = Field(
        alias="CrossClusterSearchConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeInboundCrossClusterSearchConnectionsResponseModel(BaseModel):
    cross_cluster_search_connections: List[
        InboundCrossClusterSearchConnectionModel
    ] = Field(alias="CrossClusterSearchConnections")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectInboundCrossClusterSearchConnectionResponseModel(BaseModel):
    cross_cluster_search_connection: InboundCrossClusterSearchConnectionModel = Field(
        alias="CrossClusterSearchConnection"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReservedElasticsearchInstanceOfferingsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reserved_elasticsearch_instance_offerings: List[
        ReservedElasticsearchInstanceOfferingModel
    ] = Field(alias="ReservedElasticsearchInstanceOfferings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeReservedElasticsearchInstancesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    reserved_elasticsearch_instances: List[ReservedElasticsearchInstanceModel] = Field(
        alias="ReservedElasticsearchInstances"
    )
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


class DescribeDomainAutoTunesResponseModel(BaseModel):
    auto_tunes: List[AutoTuneModel] = Field(alias="AutoTunes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoTuneOptionsStatusModel(BaseModel):
    options: Optional[AutoTuneOptionsModel] = Field(default=None, alias="Options")
    status: Optional[AutoTuneStatusModel] = Field(default=None, alias="Status")


class CreateElasticsearchDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    elasticsearch_version: Optional[str] = Field(
        default=None, alias="ElasticsearchVersion"
    )
    elasticsearch_cluster_config: Optional[ElasticsearchClusterConfigModel] = Field(
        default=None, alias="ElasticsearchClusterConfig"
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
    auto_tune_options: Optional[AutoTuneOptionsInputModel] = Field(
        default=None, alias="AutoTuneOptions"
    )
    tag_list: Optional[Sequence[TagModel]] = Field(default=None, alias="TagList")


class UpdateElasticsearchDomainConfigRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    elasticsearch_cluster_config: Optional[ElasticsearchClusterConfigModel] = Field(
        default=None, alias="ElasticsearchClusterConfig"
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
    domain_endpoint_options: Optional[DomainEndpointOptionsModel] = Field(
        default=None, alias="DomainEndpointOptions"
    )
    advanced_security_options: Optional[AdvancedSecurityOptionsInputModel] = Field(
        default=None, alias="AdvancedSecurityOptions"
    )
    node_to_node_encryption_options: Optional[NodeToNodeEncryptionOptionsModel] = Field(
        default=None, alias="NodeToNodeEncryptionOptions"
    )
    encryption_at_rest_options: Optional[EncryptionAtRestOptionsModel] = Field(
        default=None, alias="EncryptionAtRestOptions"
    )
    auto_tune_options: Optional[AutoTuneOptionsModel] = Field(
        default=None, alias="AutoTuneOptions"
    )
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class AdvancedSecurityOptionsStatusModel(BaseModel):
    options: AdvancedSecurityOptionsModel = Field(alias="Options")
    status: OptionStatusModel = Field(alias="Status")


class ElasticsearchDomainStatusModel(BaseModel):
    domain_id: str = Field(alias="DomainId")
    domain_name: str = Field(alias="DomainName")
    arn: str = Field(alias="ARN")
    elasticsearch_cluster_config: ElasticsearchClusterConfigModel = Field(
        alias="ElasticsearchClusterConfig"
    )
    created: Optional[bool] = Field(default=None, alias="Created")
    deleted: Optional[bool] = Field(default=None, alias="Deleted")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    endpoints: Optional[Dict[str, str]] = Field(default=None, alias="Endpoints")
    processing: Optional[bool] = Field(default=None, alias="Processing")
    upgrade_processing: Optional[bool] = Field(default=None, alias="UpgradeProcessing")
    elasticsearch_version: Optional[str] = Field(
        default=None, alias="ElasticsearchVersion"
    )
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


class DescribeElasticsearchInstanceTypeLimitsResponseModel(BaseModel):
    limits_by_role: Dict[str, LimitsModel] = Field(alias="LimitsByRole")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ElasticsearchDomainConfigModel(BaseModel):
    elasticsearch_version: Optional[ElasticsearchVersionStatusModel] = Field(
        default=None, alias="ElasticsearchVersion"
    )
    elasticsearch_cluster_config: Optional[
        ElasticsearchClusterConfigStatusModel
    ] = Field(default=None, alias="ElasticsearchClusterConfig")
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


class CreateElasticsearchDomainResponseModel(BaseModel):
    domain_status: ElasticsearchDomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteElasticsearchDomainResponseModel(BaseModel):
    domain_status: ElasticsearchDomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeElasticsearchDomainResponseModel(BaseModel):
    domain_status: ElasticsearchDomainStatusModel = Field(alias="DomainStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeElasticsearchDomainsResponseModel(BaseModel):
    domain_status_list: List[ElasticsearchDomainStatusModel] = Field(
        alias="DomainStatusList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeElasticsearchDomainConfigResponseModel(BaseModel):
    domain_config: ElasticsearchDomainConfigModel = Field(alias="DomainConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateElasticsearchDomainConfigResponseModel(BaseModel):
    domain_config: ElasticsearchDomainConfigModel = Field(alias="DomainConfig")
    dry_run_results: DryRunResultsModel = Field(alias="DryRunResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
