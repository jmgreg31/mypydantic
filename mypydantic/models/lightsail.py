# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessKeyLastUsedModel(BaseModel):
    last_used_date: Optional[datetime] = Field(default=None, alias="lastUsedDate")
    region: Optional[str] = Field(default=None, alias="region")
    service_name: Optional[str] = Field(default=None, alias="serviceName")


class AccessRulesModel(BaseModel):
    get_object: Optional[Literal["private", "public"]] = Field(
        default=None, alias="getObject"
    )
    allow_public_overrides: Optional[bool] = Field(
        default=None, alias="allowPublicOverrides"
    )


class AccountLevelBpaSyncModel(BaseModel):
    status: Optional[Literal["Defaulted", "Failed", "InSync", "NeverSynced"]] = Field(
        default=None, alias="status"
    )
    last_synced_at: Optional[datetime] = Field(default=None, alias="lastSyncedAt")
    message: Optional[
        Literal[
            "DEFAULTED_FOR_SLR_MISSING",
            "DEFAULTED_FOR_SLR_MISSING_ON_HOLD",
            "SYNC_ON_HOLD",
            "Unknown",
        ]
    ] = Field(default=None, alias="message")
    bpa_impacts_lightsail: Optional[bool] = Field(
        default=None, alias="bpaImpactsLightsail"
    )


class AutoSnapshotAddOnRequestModel(BaseModel):
    snapshot_time_of_day: Optional[str] = Field(default=None, alias="snapshotTimeOfDay")


class StopInstanceOnIdleRequestModel(BaseModel):
    threshold: Optional[str] = Field(default=None, alias="threshold")
    duration: Optional[str] = Field(default=None, alias="duration")


class AddOnModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[str] = Field(default=None, alias="status")
    snapshot_time_of_day: Optional[str] = Field(default=None, alias="snapshotTimeOfDay")
    next_snapshot_time_of_day: Optional[str] = Field(
        default=None, alias="nextSnapshotTimeOfDay"
    )
    threshold: Optional[str] = Field(default=None, alias="threshold")
    duration: Optional[str] = Field(default=None, alias="duration")


class MonitoredResourceInfoModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")


class ResourceLocationModel(BaseModel):
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    region_name: Optional[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "eu-central-1",
            "eu-north-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="regionName")


class AllocateStaticIpRequestModel(BaseModel):
    static_ip_name: str = Field(alias="staticIpName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AttachCertificateToDistributionRequestModel(BaseModel):
    distribution_name: str = Field(alias="distributionName")
    certificate_name: str = Field(alias="certificateName")


class AttachDiskRequestModel(BaseModel):
    disk_name: str = Field(alias="diskName")
    instance_name: str = Field(alias="instanceName")
    disk_path: str = Field(alias="diskPath")
    auto_mounting: Optional[bool] = Field(default=None, alias="autoMounting")


class AttachInstancesToLoadBalancerRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    instance_names: Sequence[str] = Field(alias="instanceNames")


class AttachLoadBalancerTlsCertificateRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    certificate_name: str = Field(alias="certificateName")


class AttachStaticIpRequestModel(BaseModel):
    static_ip_name: str = Field(alias="staticIpName")
    instance_name: str = Field(alias="instanceName")


class AttachedDiskModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="path")
    size_in_gb: Optional[int] = Field(default=None, alias="sizeInGb")


class AvailabilityZoneModel(BaseModel):
    zone_name: Optional[str] = Field(default=None, alias="zoneName")
    state: Optional[str] = Field(default=None, alias="state")


class BlueprintModel(BaseModel):
    blueprint_id: Optional[str] = Field(default=None, alias="blueprintId")
    name: Optional[str] = Field(default=None, alias="name")
    group: Optional[str] = Field(default=None, alias="group")
    type: Optional[Literal["app", "os"]] = Field(default=None, alias="type")
    description: Optional[str] = Field(default=None, alias="description")
    is_active: Optional[bool] = Field(default=None, alias="isActive")
    min_power: Optional[int] = Field(default=None, alias="minPower")
    version: Optional[str] = Field(default=None, alias="version")
    version_code: Optional[str] = Field(default=None, alias="versionCode")
    product_url: Optional[str] = Field(default=None, alias="productUrl")
    license_url: Optional[str] = Field(default=None, alias="licenseUrl")
    platform: Optional[Literal["LINUX_UNIX", "WINDOWS"]] = Field(
        default=None, alias="platform"
    )
    app_category: Optional[Literal["LfR"]] = Field(default=None, alias="appCategory")


class BucketAccessLogConfigModel(BaseModel):
    enabled: bool = Field(alias="enabled")
    destination: Optional[str] = Field(default=None, alias="destination")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class BucketBundleModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    name: Optional[str] = Field(default=None, alias="name")
    price: Optional[float] = Field(default=None, alias="price")
    storage_per_month_in_gb: Optional[int] = Field(
        default=None, alias="storagePerMonthInGb"
    )
    transfer_per_month_in_gb: Optional[int] = Field(
        default=None, alias="transferPerMonthInGb"
    )
    is_active: Optional[bool] = Field(default=None, alias="isActive")


class BucketStateModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class ResourceReceivingAccessModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class BundleModel(BaseModel):
    price: Optional[float] = Field(default=None, alias="price")
    cpu_count: Optional[int] = Field(default=None, alias="cpuCount")
    disk_size_in_gb: Optional[int] = Field(default=None, alias="diskSizeInGb")
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    instance_type: Optional[str] = Field(default=None, alias="instanceType")
    is_active: Optional[bool] = Field(default=None, alias="isActive")
    name: Optional[str] = Field(default=None, alias="name")
    power: Optional[int] = Field(default=None, alias="power")
    ram_size_in_gb: Optional[float] = Field(default=None, alias="ramSizeInGb")
    transfer_per_month_in_gb: Optional[int] = Field(
        default=None, alias="transferPerMonthInGb"
    )
    supported_platforms: Optional[List[Literal["LINUX_UNIX", "WINDOWS"]]] = Field(
        default=None, alias="supportedPlatforms"
    )
    supported_app_categories: Optional[List[Literal["LfR"]]] = Field(
        default=None, alias="supportedAppCategories"
    )


class CacheBehaviorPerPathModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="path")
    behavior: Optional[Literal["cache", "dont-cache"]] = Field(
        default=None, alias="behavior"
    )


class CacheBehaviorModel(BaseModel):
    behavior: Optional[Literal["cache", "dont-cache"]] = Field(
        default=None, alias="behavior"
    )


class CookieObjectModel(BaseModel):
    option: Optional[Literal["all", "allow-list", "none"]] = Field(
        default=None, alias="option"
    )
    cookies_allow_list: Optional[Sequence[str]] = Field(
        default=None, alias="cookiesAllowList"
    )


class HeaderObjectModel(BaseModel):
    option: Optional[Literal["all", "allow-list", "none"]] = Field(
        default=None, alias="option"
    )
    headers_allow_list: Optional[
        Sequence[
            Literal[
                "Accept",
                "Accept-Charset",
                "Accept-Datetime",
                "Accept-Encoding",
                "Accept-Language",
                "Authorization",
                "CloudFront-Forwarded-Proto",
                "CloudFront-Is-Desktop-Viewer",
                "CloudFront-Is-Mobile-Viewer",
                "CloudFront-Is-SmartTV-Viewer",
                "CloudFront-Is-Tablet-Viewer",
                "CloudFront-Viewer-Country",
                "Host",
                "Origin",
                "Referer",
            ]
        ]
    ] = Field(default=None, alias="headersAllowList")


class QueryStringObjectModel(BaseModel):
    option: Optional[bool] = Field(default=None, alias="option")
    query_strings_allow_list: Optional[Sequence[str]] = Field(
        default=None, alias="queryStringsAllowList"
    )


class PortInfoModel(BaseModel):
    from_port: Optional[int] = Field(default=None, alias="fromPort")
    to_port: Optional[int] = Field(default=None, alias="toPort")
    protocol: Optional[Literal["all", "icmp", "tcp", "udp"]] = Field(
        default=None, alias="protocol"
    )
    cidrs: Optional[Sequence[str]] = Field(default=None, alias="cidrs")
    ipv6_cidrs: Optional[Sequence[str]] = Field(default=None, alias="ipv6Cidrs")
    cidr_list_aliases: Optional[Sequence[str]] = Field(
        default=None, alias="cidrListAliases"
    )


class CloudFormationStackRecordSourceInfoModel(BaseModel):
    resource_type: Optional[Literal["ExportSnapshotRecord"]] = Field(
        default=None, alias="resourceType"
    )
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")


class DestinationInfoModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    service: Optional[str] = Field(default=None, alias="service")


class ContainerImageModel(BaseModel):
    image: Optional[str] = Field(default=None, alias="image")
    digest: Optional[str] = Field(default=None, alias="digest")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class ContainerModel(BaseModel):
    image: Optional[str] = Field(default=None, alias="image")
    command: Optional[Sequence[str]] = Field(default=None, alias="command")
    environment: Optional[Mapping[str, str]] = Field(default=None, alias="environment")
    ports: Optional[Mapping[str, Literal["HTTP", "HTTPS", "TCP", "UDP"]]] = Field(
        default=None, alias="ports"
    )


class ContainerServiceECRImagePullerRoleRequestModel(BaseModel):
    is_active: Optional[bool] = Field(default=None, alias="isActive")


class ContainerServiceECRImagePullerRoleModel(BaseModel):
    is_active: Optional[bool] = Field(default=None, alias="isActive")
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")


class ContainerServiceHealthCheckConfigModel(BaseModel):
    healthy_threshold: Optional[int] = Field(default=None, alias="healthyThreshold")
    unhealthy_threshold: Optional[int] = Field(default=None, alias="unhealthyThreshold")
    timeout_seconds: Optional[int] = Field(default=None, alias="timeoutSeconds")
    interval_seconds: Optional[int] = Field(default=None, alias="intervalSeconds")
    path: Optional[str] = Field(default=None, alias="path")
    success_codes: Optional[str] = Field(default=None, alias="successCodes")


class ContainerServiceLogEventModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    message: Optional[str] = Field(default=None, alias="message")


class ContainerServicePowerModel(BaseModel):
    power_id: Optional[str] = Field(default=None, alias="powerId")
    price: Optional[float] = Field(default=None, alias="price")
    cpu_count: Optional[float] = Field(default=None, alias="cpuCount")
    ram_size_in_gb: Optional[float] = Field(default=None, alias="ramSizeInGb")
    name: Optional[str] = Field(default=None, alias="name")
    is_active: Optional[bool] = Field(default=None, alias="isActive")


class ContainerServiceRegistryLoginModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="username")
    password: Optional[str] = Field(default=None, alias="password")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")
    registry: Optional[str] = Field(default=None, alias="registry")


class ContainerServiceStateDetailModel(BaseModel):
    code: Optional[
        Literal[
            "ACTIVATING_DEPLOYMENT",
            "CERTIFICATE_LIMIT_EXCEEDED",
            "CREATING_DEPLOYMENT",
            "CREATING_NETWORK_INFRASTRUCTURE",
            "CREATING_SYSTEM_RESOURCES",
            "EVALUATING_HEALTH_CHECK",
            "PROVISIONING_CERTIFICATE",
            "PROVISIONING_SERVICE",
            "UNKNOWN_ERROR",
        ]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class CopySnapshotRequestModel(BaseModel):
    target_snapshot_name: str = Field(alias="targetSnapshotName")
    source_region: Literal[
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ca-central-1",
        "eu-central-1",
        "eu-north-1",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
    ] = Field(alias="sourceRegion")
    source_snapshot_name: Optional[str] = Field(
        default=None, alias="sourceSnapshotName"
    )
    source_resource_name: Optional[str] = Field(
        default=None, alias="sourceResourceName"
    )
    restore_date: Optional[str] = Field(default=None, alias="restoreDate")
    use_latest_restorable_auto_snapshot: Optional[bool] = Field(
        default=None, alias="useLatestRestorableAutoSnapshot"
    )


class CreateBucketAccessKeyRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")


class InstanceEntryModel(BaseModel):
    source_name: str = Field(alias="sourceName")
    instance_type: str = Field(alias="instanceType")
    port_info_source: Literal["CLOSED", "DEFAULT", "INSTANCE", "NONE"] = Field(
        alias="portInfoSource"
    )
    availability_zone: str = Field(alias="availabilityZone")
    user_data: Optional[str] = Field(default=None, alias="userData")


class CreateContactMethodRequestModel(BaseModel):
    protocol: Literal["Email", "SMS"] = Field(alias="protocol")
    contact_endpoint: str = Field(alias="contactEndpoint")


class InputOriginModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    region_name: Optional[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "eu-central-1",
            "eu-north-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="regionName")
    protocol_policy: Optional[Literal["http-only", "https-only"]] = Field(
        default=None, alias="protocolPolicy"
    )


class DomainEntryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    target: Optional[str] = Field(default=None, alias="target")
    is_alias: Optional[bool] = Field(default=None, alias="isAlias")
    type: Optional[str] = Field(default=None, alias="type")
    options: Optional[Mapping[str, str]] = Field(default=None, alias="options")


class CreateGUISessionAccessDetailsRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")


class SessionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    url: Optional[str] = Field(default=None, alias="url")
    is_primary: Optional[bool] = Field(default=None, alias="isPrimary")


class DiskMapModel(BaseModel):
    original_disk_path: Optional[str] = Field(default=None, alias="originalDiskPath")
    new_disk_name: Optional[str] = Field(default=None, alias="newDiskName")


class DeleteAlarmRequestModel(BaseModel):
    alarm_name: str = Field(alias="alarmName")


class DeleteAutoSnapshotRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    date: str = Field(alias="date")


class DeleteBucketAccessKeyRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    access_key_id: str = Field(alias="accessKeyId")


class DeleteBucketRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    force_delete: Optional[bool] = Field(default=None, alias="forceDelete")


class DeleteCertificateRequestModel(BaseModel):
    certificate_name: str = Field(alias="certificateName")


class DeleteContactMethodRequestModel(BaseModel):
    protocol: Literal["Email", "SMS"] = Field(alias="protocol")


class DeleteContainerImageRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    image: str = Field(alias="image")


class DeleteContainerServiceRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")


class DeleteDiskRequestModel(BaseModel):
    disk_name: str = Field(alias="diskName")
    force_delete_add_ons: Optional[bool] = Field(
        default=None, alias="forceDeleteAddOns"
    )


class DeleteDiskSnapshotRequestModel(BaseModel):
    disk_snapshot_name: str = Field(alias="diskSnapshotName")


class DeleteDistributionRequestModel(BaseModel):
    distribution_name: Optional[str] = Field(default=None, alias="distributionName")


class DeleteDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class DeleteInstanceRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")
    force_delete_add_ons: Optional[bool] = Field(
        default=None, alias="forceDeleteAddOns"
    )


class DeleteInstanceSnapshotRequestModel(BaseModel):
    instance_snapshot_name: str = Field(alias="instanceSnapshotName")


class DeleteKeyPairRequestModel(BaseModel):
    key_pair_name: str = Field(alias="keyPairName")
    expected_fingerprint: Optional[str] = Field(
        default=None, alias="expectedFingerprint"
    )


class DeleteKnownHostKeysRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class DeleteLoadBalancerRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")


class DeleteLoadBalancerTlsCertificateRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    certificate_name: str = Field(alias="certificateName")
    force: Optional[bool] = Field(default=None, alias="force")


class DeleteRelationalDatabaseRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    skip_final_snapshot: Optional[bool] = Field(default=None, alias="skipFinalSnapshot")
    final_relational_database_snapshot_name: Optional[str] = Field(
        default=None, alias="finalRelationalDatabaseSnapshotName"
    )


class DeleteRelationalDatabaseSnapshotRequestModel(BaseModel):
    relational_database_snapshot_name: str = Field(
        alias="relationalDatabaseSnapshotName"
    )


class DetachCertificateFromDistributionRequestModel(BaseModel):
    distribution_name: str = Field(alias="distributionName")


class DetachDiskRequestModel(BaseModel):
    disk_name: str = Field(alias="diskName")


class DetachInstancesFromLoadBalancerRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    instance_names: Sequence[str] = Field(alias="instanceNames")


class DetachStaticIpRequestModel(BaseModel):
    static_ip_name: str = Field(alias="staticIpName")


class DisableAddOnRequestModel(BaseModel):
    add_on_type: Literal["AutoSnapshot", "StopInstanceOnIdle"] = Field(
        alias="addOnType"
    )
    resource_name: str = Field(alias="resourceName")


class DiskInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    path: Optional[str] = Field(default=None, alias="path")
    size_in_gb: Optional[int] = Field(default=None, alias="sizeInGb")
    is_system_disk: Optional[bool] = Field(default=None, alias="isSystemDisk")


class DiskSnapshotInfoModel(BaseModel):
    size_in_gb: Optional[int] = Field(default=None, alias="sizeInGb")


class DistributionBundleModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    name: Optional[str] = Field(default=None, alias="name")
    price: Optional[float] = Field(default=None, alias="price")
    transfer_per_month_in_gb: Optional[int] = Field(
        default=None, alias="transferPerMonthInGb"
    )
    is_active: Optional[bool] = Field(default=None, alias="isActive")


class DnsRecordCreationStateModel(BaseModel):
    code: Optional[Literal["FAILED", "STARTED", "SUCCEEDED"]] = Field(
        default=None, alias="code"
    )
    message: Optional[str] = Field(default=None, alias="message")


class ResourceRecordModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")
    value: Optional[str] = Field(default=None, alias="value")


class TimePeriodModel(BaseModel):
    start: Optional[datetime] = Field(default=None, alias="start")
    end: Optional[datetime] = Field(default=None, alias="end")


class ExportSnapshotRequestModel(BaseModel):
    source_snapshot_name: str = Field(alias="sourceSnapshotName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetActiveNamesRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetAlarmsRequestModel(BaseModel):
    alarm_name: Optional[str] = Field(default=None, alias="alarmName")
    page_token: Optional[str] = Field(default=None, alias="pageToken")
    monitored_resource_name: Optional[str] = Field(
        default=None, alias="monitoredResourceName"
    )


class GetAutoSnapshotsRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")


class GetBlueprintsRequestModel(BaseModel):
    include_inactive: Optional[bool] = Field(default=None, alias="includeInactive")
    page_token: Optional[str] = Field(default=None, alias="pageToken")
    app_category: Optional[Literal["LfR"]] = Field(default=None, alias="appCategory")


class GetBucketAccessKeysRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")


class GetBucketBundlesRequestModel(BaseModel):
    include_inactive: Optional[bool] = Field(default=None, alias="includeInactive")


class GetBucketMetricDataRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    metric_name: Literal["BucketSizeBytes", "NumberOfObjects"] = Field(
        alias="metricName"
    )
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    period: int = Field(alias="period")
    statistics: Sequence[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(alias="statistics")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="unit")


class MetricDatapointModel(BaseModel):
    average: Optional[float] = Field(default=None, alias="average")
    maximum: Optional[float] = Field(default=None, alias="maximum")
    minimum: Optional[float] = Field(default=None, alias="minimum")
    sample_count: Optional[float] = Field(default=None, alias="sampleCount")
    sum: Optional[float] = Field(default=None, alias="sum")
    timestamp: Optional[datetime] = Field(default=None, alias="timestamp")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="unit")


class GetBucketsRequestModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")
    page_token: Optional[str] = Field(default=None, alias="pageToken")
    include_connected_resources: Optional[bool] = Field(
        default=None, alias="includeConnectedResources"
    )


class GetBundlesRequestModel(BaseModel):
    include_inactive: Optional[bool] = Field(default=None, alias="includeInactive")
    page_token: Optional[str] = Field(default=None, alias="pageToken")
    app_category: Optional[Literal["LfR"]] = Field(default=None, alias="appCategory")


class GetCertificatesRequestModel(BaseModel):
    certificate_statuses: Optional[
        Sequence[
            Literal[
                "EXPIRED",
                "FAILED",
                "INACTIVE",
                "ISSUED",
                "PENDING_VALIDATION",
                "REVOKED",
                "VALIDATION_TIMED_OUT",
            ]
        ]
    ] = Field(default=None, alias="certificateStatuses")
    include_certificate_details: Optional[bool] = Field(
        default=None, alias="includeCertificateDetails"
    )
    certificate_name: Optional[str] = Field(default=None, alias="certificateName")


class GetCloudFormationStackRecordsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetContactMethodsRequestModel(BaseModel):
    protocols: Optional[Sequence[Literal["Email", "SMS"]]] = Field(
        default=None, alias="protocols"
    )


class GetContainerImagesRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")


class GetContainerLogRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    container_name: str = Field(alias="containerName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    filter_pattern: Optional[str] = Field(default=None, alias="filterPattern")
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetContainerServiceDeploymentsRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")


class GetContainerServiceMetricDataRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    metric_name: Literal["CPUUtilization", "MemoryUtilization"] = Field(
        alias="metricName"
    )
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    period: int = Field(alias="period")
    statistics: Sequence[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(alias="statistics")


class GetContainerServicesRequestModel(BaseModel):
    service_name: Optional[str] = Field(default=None, alias="serviceName")


class GetCostEstimateRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")


class GetDiskRequestModel(BaseModel):
    disk_name: str = Field(alias="diskName")


class GetDiskSnapshotRequestModel(BaseModel):
    disk_snapshot_name: str = Field(alias="diskSnapshotName")


class GetDiskSnapshotsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetDisksRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetDistributionLatestCacheResetRequestModel(BaseModel):
    distribution_name: Optional[str] = Field(default=None, alias="distributionName")


class GetDistributionMetricDataRequestModel(BaseModel):
    distribution_name: str = Field(alias="distributionName")
    metric_name: Literal[
        "BytesDownloaded",
        "BytesUploaded",
        "Http4xxErrorRate",
        "Http5xxErrorRate",
        "Requests",
        "TotalErrorRate",
    ] = Field(alias="metricName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    period: int = Field(alias="period")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="unit")
    statistics: Sequence[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(alias="statistics")


class GetDistributionsRequestModel(BaseModel):
    distribution_name: Optional[str] = Field(default=None, alias="distributionName")
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")


class GetDomainsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetExportSnapshotRecordsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetInstanceAccessDetailsRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")
    protocol: Optional[Literal["rdp", "ssh"]] = Field(default=None, alias="protocol")


class GetInstanceMetricDataRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")
    metric_name: Literal[
        "BurstCapacityPercentage",
        "BurstCapacityTime",
        "CPUUtilization",
        "MetadataNoToken",
        "NetworkIn",
        "NetworkOut",
        "StatusCheckFailed",
        "StatusCheckFailed_Instance",
        "StatusCheckFailed_System",
    ] = Field(alias="metricName")
    period: int = Field(alias="period")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="unit")
    statistics: Sequence[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(alias="statistics")


class GetInstancePortStatesRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class InstancePortStateModel(BaseModel):
    from_port: Optional[int] = Field(default=None, alias="fromPort")
    to_port: Optional[int] = Field(default=None, alias="toPort")
    protocol: Optional[Literal["all", "icmp", "tcp", "udp"]] = Field(
        default=None, alias="protocol"
    )
    state: Optional[Literal["closed", "open"]] = Field(default=None, alias="state")
    cidrs: Optional[List[str]] = Field(default=None, alias="cidrs")
    ipv6_cidrs: Optional[List[str]] = Field(default=None, alias="ipv6Cidrs")
    cidr_list_aliases: Optional[List[str]] = Field(
        default=None, alias="cidrListAliases"
    )


class GetInstanceRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class GetInstanceSnapshotRequestModel(BaseModel):
    instance_snapshot_name: str = Field(alias="instanceSnapshotName")


class GetInstanceSnapshotsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetInstanceStateRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class InstanceStateModel(BaseModel):
    code: Optional[int] = Field(default=None, alias="code")
    name: Optional[str] = Field(default=None, alias="name")


class GetInstancesRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetKeyPairRequestModel(BaseModel):
    key_pair_name: str = Field(alias="keyPairName")


class GetKeyPairsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")
    include_default_key_pair: Optional[bool] = Field(
        default=None, alias="includeDefaultKeyPair"
    )


class GetLoadBalancerMetricDataRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    metric_name: Literal[
        "ClientTLSNegotiationErrorCount",
        "HTTPCode_Instance_2XX_Count",
        "HTTPCode_Instance_3XX_Count",
        "HTTPCode_Instance_4XX_Count",
        "HTTPCode_Instance_5XX_Count",
        "HTTPCode_LB_4XX_Count",
        "HTTPCode_LB_5XX_Count",
        "HealthyHostCount",
        "InstanceResponseTime",
        "RejectedConnectionCount",
        "RequestCount",
        "UnhealthyHostCount",
    ] = Field(alias="metricName")
    period: int = Field(alias="period")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="unit")
    statistics: Sequence[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(alias="statistics")


class GetLoadBalancerRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")


class GetLoadBalancerTlsCertificatesRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")


class GetLoadBalancerTlsPoliciesRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class LoadBalancerTlsPolicyModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    is_default: Optional[bool] = Field(default=None, alias="isDefault")
    description: Optional[str] = Field(default=None, alias="description")
    protocols: Optional[List[str]] = Field(default=None, alias="protocols")
    ciphers: Optional[List[str]] = Field(default=None, alias="ciphers")


class GetLoadBalancersRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetOperationRequestModel(BaseModel):
    operation_id: str = Field(alias="operationId")


class GetOperationsForResourceRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetOperationsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetRegionsRequestModel(BaseModel):
    include_availability_zones: Optional[bool] = Field(
        default=None, alias="includeAvailabilityZones"
    )
    include_relational_database_availability_zones: Optional[bool] = Field(
        default=None, alias="includeRelationalDatabaseAvailabilityZones"
    )


class GetRelationalDatabaseBlueprintsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class RelationalDatabaseBlueprintModel(BaseModel):
    blueprint_id: Optional[str] = Field(default=None, alias="blueprintId")
    engine: Optional[Literal["mysql"]] = Field(default=None, alias="engine")
    engine_version: Optional[str] = Field(default=None, alias="engineVersion")
    engine_description: Optional[str] = Field(default=None, alias="engineDescription")
    engine_version_description: Optional[str] = Field(
        default=None, alias="engineVersionDescription"
    )
    is_engine_default: Optional[bool] = Field(default=None, alias="isEngineDefault")


class GetRelationalDatabaseBundlesRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")
    include_inactive: Optional[bool] = Field(default=None, alias="includeInactive")


class RelationalDatabaseBundleModel(BaseModel):
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    name: Optional[str] = Field(default=None, alias="name")
    price: Optional[float] = Field(default=None, alias="price")
    ram_size_in_gb: Optional[float] = Field(default=None, alias="ramSizeInGb")
    disk_size_in_gb: Optional[int] = Field(default=None, alias="diskSizeInGb")
    transfer_per_month_in_gb: Optional[int] = Field(
        default=None, alias="transferPerMonthInGb"
    )
    cpu_count: Optional[int] = Field(default=None, alias="cpuCount")
    is_encrypted: Optional[bool] = Field(default=None, alias="isEncrypted")
    is_active: Optional[bool] = Field(default=None, alias="isActive")


class GetRelationalDatabaseEventsRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    duration_in_minutes: Optional[int] = Field(default=None, alias="durationInMinutes")
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class RelationalDatabaseEventModel(BaseModel):
    resource: Optional[str] = Field(default=None, alias="resource")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    message: Optional[str] = Field(default=None, alias="message")
    event_categories: Optional[List[str]] = Field(default=None, alias="eventCategories")


class GetRelationalDatabaseLogEventsRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    log_stream_name: str = Field(alias="logStreamName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    start_from_head: Optional[bool] = Field(default=None, alias="startFromHead")
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class LogEventModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    message: Optional[str] = Field(default=None, alias="message")


class GetRelationalDatabaseLogStreamsRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")


class GetRelationalDatabaseMasterUserPasswordRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    password_version: Optional[Literal["CURRENT", "PENDING", "PREVIOUS"]] = Field(
        default=None, alias="passwordVersion"
    )


class GetRelationalDatabaseMetricDataRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    metric_name: Literal[
        "CPUUtilization",
        "DatabaseConnections",
        "DiskQueueDepth",
        "FreeStorageSpace",
        "NetworkReceiveThroughput",
        "NetworkTransmitThroughput",
    ] = Field(alias="metricName")
    period: int = Field(alias="period")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="unit")
    statistics: Sequence[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(alias="statistics")


class GetRelationalDatabaseParametersRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class RelationalDatabaseParameterModel(BaseModel):
    allowed_values: Optional[str] = Field(default=None, alias="allowedValues")
    apply_method: Optional[str] = Field(default=None, alias="applyMethod")
    apply_type: Optional[str] = Field(default=None, alias="applyType")
    data_type: Optional[str] = Field(default=None, alias="dataType")
    description: Optional[str] = Field(default=None, alias="description")
    is_modifiable: Optional[bool] = Field(default=None, alias="isModifiable")
    parameter_name: Optional[str] = Field(default=None, alias="parameterName")
    parameter_value: Optional[str] = Field(default=None, alias="parameterValue")


class GetRelationalDatabaseRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")


class GetRelationalDatabaseSnapshotRequestModel(BaseModel):
    relational_database_snapshot_name: str = Field(
        alias="relationalDatabaseSnapshotName"
    )


class GetRelationalDatabaseSnapshotsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetRelationalDatabasesRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class GetStaticIpRequestModel(BaseModel):
    static_ip_name: str = Field(alias="staticIpName")


class GetStaticIpsRequestModel(BaseModel):
    page_token: Optional[str] = Field(default=None, alias="pageToken")


class HostKeyAttributesModel(BaseModel):
    algorithm: Optional[str] = Field(default=None, alias="algorithm")
    public_key: Optional[str] = Field(default=None, alias="publicKey")
    witnessed_at: Optional[datetime] = Field(default=None, alias="witnessedAt")
    fingerprint_s_ha1: Optional[str] = Field(default=None, alias="fingerprintSHA1")
    fingerprint_s_ha256: Optional[str] = Field(default=None, alias="fingerprintSHA256")
    not_valid_before: Optional[datetime] = Field(default=None, alias="notValidBefore")
    not_valid_after: Optional[datetime] = Field(default=None, alias="notValidAfter")


class ImportKeyPairRequestModel(BaseModel):
    key_pair_name: str = Field(alias="keyPairName")
    public_key_base64: str = Field(alias="publicKeyBase64")


class PasswordDataModel(BaseModel):
    ciphertext: Optional[str] = Field(default=None, alias="ciphertext")
    key_pair_name: Optional[str] = Field(default=None, alias="keyPairName")


class InstanceHealthSummaryModel(BaseModel):
    instance_name: Optional[str] = Field(default=None, alias="instanceName")
    instance_health: Optional[
        Literal["draining", "healthy", "initial", "unavailable", "unhealthy", "unused"]
    ] = Field(default=None, alias="instanceHealth")
    instance_health_reason: Optional[
        Literal[
            "Instance.DeregistrationInProgress",
            "Instance.FailedHealthChecks",
            "Instance.InvalidState",
            "Instance.IpUnusable",
            "Instance.NotInUse",
            "Instance.NotRegistered",
            "Instance.ResponseCodeMismatch",
            "Instance.Timeout",
            "Lb.InitialHealthChecking",
            "Lb.InternalError",
            "Lb.RegistrationInProgress",
        ]
    ] = Field(default=None, alias="instanceHealthReason")


class InstanceMetadataOptionsModel(BaseModel):
    state: Optional[Literal["applied", "pending"]] = Field(default=None, alias="state")
    http_tokens: Optional[Literal["optional", "required"]] = Field(
        default=None, alias="httpTokens"
    )
    http_endpoint: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="httpEndpoint"
    )
    http_put_response_hop_limit: Optional[int] = Field(
        default=None, alias="httpPutResponseHopLimit"
    )
    http_protocol_ipv6: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="httpProtocolIpv6"
    )


class InstancePortInfoModel(BaseModel):
    from_port: Optional[int] = Field(default=None, alias="fromPort")
    to_port: Optional[int] = Field(default=None, alias="toPort")
    protocol: Optional[Literal["all", "icmp", "tcp", "udp"]] = Field(
        default=None, alias="protocol"
    )
    access_from: Optional[str] = Field(default=None, alias="accessFrom")
    access_type: Optional[Literal["Private", "Public"]] = Field(
        default=None, alias="accessType"
    )
    common_name: Optional[str] = Field(default=None, alias="commonName")
    access_direction: Optional[Literal["inbound", "outbound"]] = Field(
        default=None, alias="accessDirection"
    )
    cidrs: Optional[List[str]] = Field(default=None, alias="cidrs")
    ipv6_cidrs: Optional[List[str]] = Field(default=None, alias="ipv6Cidrs")
    cidr_list_aliases: Optional[List[str]] = Field(
        default=None, alias="cidrListAliases"
    )


class MonthlyTransferModel(BaseModel):
    gb_per_month_allocated: Optional[int] = Field(
        default=None, alias="gbPerMonthAllocated"
    )


class OriginModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    region_name: Optional[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "eu-central-1",
            "eu-north-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="regionName")
    protocol_policy: Optional[Literal["http-only", "https-only"]] = Field(
        default=None, alias="protocolPolicy"
    )


class LoadBalancerTlsCertificateDnsRecordCreationStateModel(BaseModel):
    code: Optional[Literal["FAILED", "STARTED", "SUCCEEDED"]] = Field(
        default=None, alias="code"
    )
    message: Optional[str] = Field(default=None, alias="message")


class LoadBalancerTlsCertificateDomainValidationOptionModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    validation_status: Optional[
        Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
    ] = Field(default=None, alias="validationStatus")


class LoadBalancerTlsCertificateSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    is_attached: Optional[bool] = Field(default=None, alias="isAttached")


class NameServersUpdateStateModel(BaseModel):
    code: Optional[Literal["FAILED", "PENDING", "STARTED", "SUCCEEDED"]] = Field(
        default=None, alias="code"
    )
    message: Optional[str] = Field(default=None, alias="message")


class PendingMaintenanceActionModel(BaseModel):
    action: Optional[str] = Field(default=None, alias="action")
    description: Optional[str] = Field(default=None, alias="description")
    current_apply_date: Optional[datetime] = Field(
        default=None, alias="currentApplyDate"
    )


class PendingModifiedRelationalDatabaseValuesModel(BaseModel):
    master_user_password: Optional[str] = Field(
        default=None, alias="masterUserPassword"
    )
    engine_version: Optional[str] = Field(default=None, alias="engineVersion")
    backup_retention_enabled: Optional[bool] = Field(
        default=None, alias="backupRetentionEnabled"
    )


class PutAlarmRequestModel(BaseModel):
    alarm_name: str = Field(alias="alarmName")
    metric_name: Literal[
        "BurstCapacityPercentage",
        "BurstCapacityTime",
        "CPUUtilization",
        "ClientTLSNegotiationErrorCount",
        "DatabaseConnections",
        "DiskQueueDepth",
        "FreeStorageSpace",
        "HTTPCode_Instance_2XX_Count",
        "HTTPCode_Instance_3XX_Count",
        "HTTPCode_Instance_4XX_Count",
        "HTTPCode_Instance_5XX_Count",
        "HTTPCode_LB_4XX_Count",
        "HTTPCode_LB_5XX_Count",
        "HealthyHostCount",
        "InstanceResponseTime",
        "NetworkIn",
        "NetworkOut",
        "NetworkReceiveThroughput",
        "NetworkTransmitThroughput",
        "RejectedConnectionCount",
        "RequestCount",
        "StatusCheckFailed",
        "StatusCheckFailed_Instance",
        "StatusCheckFailed_System",
        "UnhealthyHostCount",
    ] = Field(alias="metricName")
    monitored_resource_name: str = Field(alias="monitoredResourceName")
    comparison_operator: Literal[
        "GreaterThanOrEqualToThreshold",
        "GreaterThanThreshold",
        "LessThanOrEqualToThreshold",
        "LessThanThreshold",
    ] = Field(alias="comparisonOperator")
    threshold: float = Field(alias="threshold")
    evaluation_periods: int = Field(alias="evaluationPeriods")
    datapoints_to_alarm: Optional[int] = Field(default=None, alias="datapointsToAlarm")
    treat_missing_data: Optional[
        Literal["breaching", "ignore", "missing", "notBreaching"]
    ] = Field(default=None, alias="treatMissingData")
    contact_protocols: Optional[Sequence[Literal["Email", "SMS"]]] = Field(
        default=None, alias="contactProtocols"
    )
    notification_triggers: Optional[
        Sequence[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]]
    ] = Field(default=None, alias="notificationTriggers")
    notification_enabled: Optional[bool] = Field(
        default=None, alias="notificationEnabled"
    )


class R53HostedZoneDeletionStateModel(BaseModel):
    code: Optional[Literal["FAILED", "PENDING", "STARTED", "SUCCEEDED"]] = Field(
        default=None, alias="code"
    )
    message: Optional[str] = Field(default=None, alias="message")


class RebootInstanceRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class RebootRelationalDatabaseRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")


class RegisterContainerImageRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    label: str = Field(alias="label")
    digest: str = Field(alias="digest")


class RelationalDatabaseEndpointModel(BaseModel):
    port: Optional[int] = Field(default=None, alias="port")
    address: Optional[str] = Field(default=None, alias="address")


class RelationalDatabaseHardwareModel(BaseModel):
    cpu_count: Optional[int] = Field(default=None, alias="cpuCount")
    disk_size_in_gb: Optional[int] = Field(default=None, alias="diskSizeInGb")
    ram_size_in_gb: Optional[float] = Field(default=None, alias="ramSizeInGb")


class ReleaseStaticIpRequestModel(BaseModel):
    static_ip_name: str = Field(alias="staticIpName")


class ResetDistributionCacheRequestModel(BaseModel):
    distribution_name: Optional[str] = Field(default=None, alias="distributionName")


class SendContactMethodVerificationRequestModel(BaseModel):
    protocol: Literal["Email"] = Field(alias="protocol")


class SetIpAddressTypeRequestModel(BaseModel):
    resource_type: Literal[
        "Alarm",
        "Bucket",
        "Certificate",
        "CloudFormationStackRecord",
        "ContactMethod",
        "ContainerService",
        "Disk",
        "DiskSnapshot",
        "Distribution",
        "Domain",
        "ExportSnapshotRecord",
        "Instance",
        "InstanceSnapshot",
        "KeyPair",
        "LoadBalancer",
        "LoadBalancerTlsCertificate",
        "PeeredVpc",
        "RelationalDatabase",
        "RelationalDatabaseSnapshot",
        "StaticIp",
    ] = Field(alias="resourceType")
    resource_name: str = Field(alias="resourceName")
    ip_address_type: Literal["dualstack", "ipv4"] = Field(alias="ipAddressType")


class SetResourceAccessForBucketRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    bucket_name: str = Field(alias="bucketName")
    access: Literal["allow", "deny"] = Field(alias="access")


class StartGUISessionRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")


class StartInstanceRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")


class StartRelationalDatabaseRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")


class StopGUISessionRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")


class StopInstanceRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")
    force: Optional[bool] = Field(default=None, alias="force")


class StopRelationalDatabaseRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    relational_database_snapshot_name: Optional[str] = Field(
        default=None, alias="relationalDatabaseSnapshotName"
    )


class TestAlarmRequestModel(BaseModel):
    alarm_name: str = Field(alias="alarmName")
    state: Literal["ALARM", "INSUFFICIENT_DATA", "OK"] = Field(alias="state")


class UntagResourceRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    tag_keys: Sequence[str] = Field(alias="tagKeys")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")


class UpdateBucketBundleRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    bundle_id: str = Field(alias="bundleId")


class UpdateDistributionBundleRequestModel(BaseModel):
    distribution_name: Optional[str] = Field(default=None, alias="distributionName")
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")


class UpdateInstanceMetadataOptionsRequestModel(BaseModel):
    instance_name: str = Field(alias="instanceName")
    http_tokens: Optional[Literal["optional", "required"]] = Field(
        default=None, alias="httpTokens"
    )
    http_endpoint: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="httpEndpoint"
    )
    http_put_response_hop_limit: Optional[int] = Field(
        default=None, alias="httpPutResponseHopLimit"
    )
    http_protocol_ipv6: Optional[Literal["disabled", "enabled"]] = Field(
        default=None, alias="httpProtocolIpv6"
    )


class UpdateLoadBalancerAttributeRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    attribute_name: Literal[
        "HealthCheckPath",
        "HttpsRedirectionEnabled",
        "SessionStickinessEnabled",
        "SessionStickiness_LB_CookieDurationSeconds",
        "TlsPolicyName",
    ] = Field(alias="attributeName")
    attribute_value: str = Field(alias="attributeValue")


class UpdateRelationalDatabaseRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    master_user_password: Optional[str] = Field(
        default=None, alias="masterUserPassword"
    )
    rotate_master_user_password: Optional[bool] = Field(
        default=None, alias="rotateMasterUserPassword"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="preferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="preferredMaintenanceWindow"
    )
    enable_backup_retention: Optional[bool] = Field(
        default=None, alias="enableBackupRetention"
    )
    disable_backup_retention: Optional[bool] = Field(
        default=None, alias="disableBackupRetention"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    apply_immediately: Optional[bool] = Field(default=None, alias="applyImmediately")
    ca_certificate_identifier: Optional[str] = Field(
        default=None, alias="caCertificateIdentifier"
    )


class AccessKeyModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="accessKeyId")
    secret_access_key: Optional[str] = Field(default=None, alias="secretAccessKey")
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="status"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_used: Optional[AccessKeyLastUsedModel] = Field(default=None, alias="lastUsed")


class AddOnRequestModel(BaseModel):
    add_on_type: Literal["AutoSnapshot", "StopInstanceOnIdle"] = Field(
        alias="addOnType"
    )
    auto_snapshot_add_on_request: Optional[AutoSnapshotAddOnRequestModel] = Field(
        default=None, alias="autoSnapshotAddOnRequest"
    )
    stop_instance_on_idle_request: Optional[StopInstanceOnIdleRequestModel] = Field(
        default=None, alias="stopInstanceOnIdleRequest"
    )


class AlarmModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    monitored_resource_info: Optional[MonitoredResourceInfoModel] = Field(
        default=None, alias="monitoredResourceInfo"
    )
    comparison_operator: Optional[
        Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanOrEqualToThreshold",
            "LessThanThreshold",
        ]
    ] = Field(default=None, alias="comparisonOperator")
    evaluation_periods: Optional[int] = Field(default=None, alias="evaluationPeriods")
    period: Optional[int] = Field(default=None, alias="period")
    threshold: Optional[float] = Field(default=None, alias="threshold")
    datapoints_to_alarm: Optional[int] = Field(default=None, alias="datapointsToAlarm")
    treat_missing_data: Optional[
        Literal["breaching", "ignore", "missing", "notBreaching"]
    ] = Field(default=None, alias="treatMissingData")
    statistic: Optional[
        Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
    ] = Field(default=None, alias="statistic")
    metric_name: Optional[
        Literal[
            "BurstCapacityPercentage",
            "BurstCapacityTime",
            "CPUUtilization",
            "ClientTLSNegotiationErrorCount",
            "DatabaseConnections",
            "DiskQueueDepth",
            "FreeStorageSpace",
            "HTTPCode_Instance_2XX_Count",
            "HTTPCode_Instance_3XX_Count",
            "HTTPCode_Instance_4XX_Count",
            "HTTPCode_Instance_5XX_Count",
            "HTTPCode_LB_4XX_Count",
            "HTTPCode_LB_5XX_Count",
            "HealthyHostCount",
            "InstanceResponseTime",
            "NetworkIn",
            "NetworkOut",
            "NetworkReceiveThroughput",
            "NetworkTransmitThroughput",
            "RejectedConnectionCount",
            "RequestCount",
            "StatusCheckFailed",
            "StatusCheckFailed_Instance",
            "StatusCheckFailed_System",
            "UnhealthyHostCount",
        ]
    ] = Field(default=None, alias="metricName")
    state: Optional[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]] = Field(
        default=None, alias="state"
    )
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="unit")
    contact_protocols: Optional[List[Literal["Email", "SMS"]]] = Field(
        default=None, alias="contactProtocols"
    )
    notification_triggers: Optional[
        List[Literal["ALARM", "INSUFFICIENT_DATA", "OK"]]
    ] = Field(default=None, alias="notificationTriggers")
    notification_enabled: Optional[bool] = Field(
        default=None, alias="notificationEnabled"
    )


class ContactMethodModel(BaseModel):
    contact_endpoint: Optional[str] = Field(default=None, alias="contactEndpoint")
    status: Optional[Literal["Invalid", "PendingVerification", "Valid"]] = Field(
        default=None, alias="status"
    )
    protocol: Optional[Literal["Email", "SMS"]] = Field(default=None, alias="protocol")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    support_code: Optional[str] = Field(default=None, alias="supportCode")


class OperationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    is_terminal: Optional[bool] = Field(default=None, alias="isTerminal")
    operation_details: Optional[str] = Field(default=None, alias="operationDetails")
    operation_type: Optional[
        Literal[
            "AllocateStaticIp",
            "AttachCertificateToDistribution",
            "AttachDisk",
            "AttachInstancesToLoadBalancer",
            "AttachLoadBalancerTlsCertificate",
            "AttachStaticIp",
            "CloseInstancePublicPorts",
            "CreateBucket",
            "CreateBucketAccessKey",
            "CreateCertificate",
            "CreateContactMethod",
            "CreateContainerService",
            "CreateContainerServiceDeployment",
            "CreateContainerServiceRegistryLogin",
            "CreateDisk",
            "CreateDiskFromSnapshot",
            "CreateDiskSnapshot",
            "CreateDistribution",
            "CreateDomain",
            "CreateInstance",
            "CreateInstanceSnapshot",
            "CreateInstancesFromSnapshot",
            "CreateLoadBalancer",
            "CreateLoadBalancerTlsCertificate",
            "CreateRelationalDatabase",
            "CreateRelationalDatabaseFromSnapshot",
            "CreateRelationalDatabaseSnapshot",
            "DeleteAlarm",
            "DeleteBucket",
            "DeleteBucketAccessKey",
            "DeleteCertificate",
            "DeleteContactMethod",
            "DeleteContainerImage",
            "DeleteContainerService",
            "DeleteDisk",
            "DeleteDiskSnapshot",
            "DeleteDistribution",
            "DeleteDomain",
            "DeleteDomainEntry",
            "DeleteInstance",
            "DeleteInstanceSnapshot",
            "DeleteKnownHostKeys",
            "DeleteLoadBalancer",
            "DeleteLoadBalancerTlsCertificate",
            "DeleteRelationalDatabase",
            "DeleteRelationalDatabaseSnapshot",
            "DetachCertificateFromDistribution",
            "DetachDisk",
            "DetachInstancesFromLoadBalancer",
            "DetachStaticIp",
            "DisableAddOn",
            "EnableAddOn",
            "GetAlarms",
            "GetContactMethods",
            "OpenInstancePublicPorts",
            "PutAlarm",
            "PutInstancePublicPorts",
            "RebootInstance",
            "RebootRelationalDatabase",
            "RegisterContainerImage",
            "ReleaseStaticIp",
            "ResetDistributionCache",
            "SendContactMethodVerification",
            "SetIpAddressType",
            "SetResourceAccessForBucket",
            "StartGUISession",
            "StartInstance",
            "StartRelationalDatabase",
            "StopGUISession",
            "StopInstance",
            "StopRelationalDatabase",
            "TestAlarm",
            "UpdateBucket",
            "UpdateBucketBundle",
            "UpdateContainerService",
            "UpdateDistribution",
            "UpdateDistributionBundle",
            "UpdateDomainEntry",
            "UpdateInstanceMetadataOptions",
            "UpdateLoadBalancerAttribute",
            "UpdateRelationalDatabase",
            "UpdateRelationalDatabaseParameters",
        ]
    ] = Field(default=None, alias="operationType")
    status: Optional[
        Literal["Completed", "Failed", "NotStarted", "Started", "Succeeded"]
    ] = Field(default=None, alias="status")
    status_changed_at: Optional[datetime] = Field(default=None, alias="statusChangedAt")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_details: Optional[str] = Field(default=None, alias="errorDetails")


class StaticIpModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    ip_address: Optional[str] = Field(default=None, alias="ipAddress")
    attached_to: Optional[str] = Field(default=None, alias="attachedTo")
    is_attached: Optional[bool] = Field(default=None, alias="isAttached")


class DownloadDefaultKeyPairResultModel(BaseModel):
    public_key_base64: str = Field(alias="publicKeyBase64")
    private_key_base64: str = Field(alias="privateKeyBase64")
    created_at: datetime = Field(alias="createdAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetActiveNamesResultModel(BaseModel):
    active_names: List[str] = Field(alias="activeNames")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContainerAPIMetadataResultModel(BaseModel):
    metadata: List[Dict[str, str]] = Field(alias="metadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDistributionLatestCacheResetResultModel(BaseModel):
    status: str = Field(alias="status")
    create_time: datetime = Field(alias="createTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseLogStreamsResultModel(BaseModel):
    log_streams: List[str] = Field(alias="logStreams")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseMasterUserPasswordResultModel(BaseModel):
    master_user_password: str = Field(alias="masterUserPassword")
    created_at: datetime = Field(alias="createdAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IsVpcPeeredResultModel(BaseModel):
    is_peered: bool = Field(alias="isPeered")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AutoSnapshotDetailsModel(BaseModel):
    date: Optional[str] = Field(default=None, alias="date")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    status: Optional[Literal["Failed", "InProgress", "NotFound", "Success"]] = Field(
        default=None, alias="status"
    )
    from_attached_disks: Optional[List[AttachedDiskModel]] = Field(
        default=None, alias="fromAttachedDisks"
    )


class RegionModel(BaseModel):
    continent_code: Optional[str] = Field(default=None, alias="continentCode")
    description: Optional[str] = Field(default=None, alias="description")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    name: Optional[
        Literal[
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "eu-central-1",
            "eu-north-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="name")
    availability_zones: Optional[List[AvailabilityZoneModel]] = Field(
        default=None, alias="availabilityZones"
    )
    relational_database_availability_zones: Optional[
        List[AvailabilityZoneModel]
    ] = Field(default=None, alias="relationalDatabaseAvailabilityZones")


class GetBlueprintsResultModel(BaseModel):
    blueprints: List[BlueprintModel] = Field(alias="blueprints")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBucketRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    access_rules: Optional[AccessRulesModel] = Field(default=None, alias="accessRules")
    versioning: Optional[str] = Field(default=None, alias="versioning")
    readonly_access_accounts: Optional[Sequence[str]] = Field(
        default=None, alias="readonlyAccessAccounts"
    )
    access_log_config: Optional[BucketAccessLogConfigModel] = Field(
        default=None, alias="accessLogConfig"
    )


class GetBucketBundlesResultModel(BaseModel):
    bundles: List[BucketBundleModel] = Field(alias="bundles")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BucketModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    access_rules: Optional[AccessRulesModel] = Field(default=None, alias="accessRules")
    arn: Optional[str] = Field(default=None, alias="arn")
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    url: Optional[str] = Field(default=None, alias="url")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    name: Optional[str] = Field(default=None, alias="name")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    object_versioning: Optional[str] = Field(default=None, alias="objectVersioning")
    able_to_update_bundle: Optional[bool] = Field(
        default=None, alias="ableToUpdateBundle"
    )
    readonly_access_accounts: Optional[List[str]] = Field(
        default=None, alias="readonlyAccessAccounts"
    )
    resources_receiving_access: Optional[List[ResourceReceivingAccessModel]] = Field(
        default=None, alias="resourcesReceivingAccess"
    )
    state: Optional[BucketStateModel] = Field(default=None, alias="state")
    access_log_config: Optional[BucketAccessLogConfigModel] = Field(
        default=None, alias="accessLogConfig"
    )


class CreateBucketRequestModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    bundle_id: str = Field(alias="bundleId")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    enable_object_versioning: Optional[bool] = Field(
        default=None, alias="enableObjectVersioning"
    )


class CreateCertificateRequestModel(BaseModel):
    certificate_name: str = Field(alias="certificateName")
    domain_name: str = Field(alias="domainName")
    subject_alternative_names: Optional[Sequence[str]] = Field(
        default=None, alias="subjectAlternativeNames"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateDiskSnapshotRequestModel(BaseModel):
    disk_snapshot_name: str = Field(alias="diskSnapshotName")
    disk_name: Optional[str] = Field(default=None, alias="diskName")
    instance_name: Optional[str] = Field(default=None, alias="instanceName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateInstanceSnapshotRequestModel(BaseModel):
    instance_snapshot_name: str = Field(alias="instanceSnapshotName")
    instance_name: str = Field(alias="instanceName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateKeyPairRequestModel(BaseModel):
    key_pair_name: str = Field(alias="keyPairName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateLoadBalancerRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    instance_port: int = Field(alias="instancePort")
    health_check_path: Optional[str] = Field(default=None, alias="healthCheckPath")
    certificate_name: Optional[str] = Field(default=None, alias="certificateName")
    certificate_domain_name: Optional[str] = Field(
        default=None, alias="certificateDomainName"
    )
    certificate_alternative_names: Optional[Sequence[str]] = Field(
        default=None, alias="certificateAlternativeNames"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="ipAddressType"
    )
    tls_policy_name: Optional[str] = Field(default=None, alias="tlsPolicyName")


class CreateLoadBalancerTlsCertificateRequestModel(BaseModel):
    load_balancer_name: str = Field(alias="loadBalancerName")
    certificate_name: str = Field(alias="certificateName")
    certificate_domain_name: str = Field(alias="certificateDomainName")
    certificate_alternative_names: Optional[Sequence[str]] = Field(
        default=None, alias="certificateAlternativeNames"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateRelationalDatabaseFromSnapshotRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    relational_database_snapshot_name: Optional[str] = Field(
        default=None, alias="relationalDatabaseSnapshotName"
    )
    relational_database_bundle_id: Optional[str] = Field(
        default=None, alias="relationalDatabaseBundleId"
    )
    source_relational_database_name: Optional[str] = Field(
        default=None, alias="sourceRelationalDatabaseName"
    )
    restore_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="restoreTime"
    )
    use_latest_restorable_time: Optional[bool] = Field(
        default=None, alias="useLatestRestorableTime"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateRelationalDatabaseRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    relational_database_blueprint_id: str = Field(alias="relationalDatabaseBlueprintId")
    relational_database_bundle_id: str = Field(alias="relationalDatabaseBundleId")
    master_database_name: str = Field(alias="masterDatabaseName")
    master_username: str = Field(alias="masterUsername")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    master_user_password: Optional[str] = Field(
        default=None, alias="masterUserPassword"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="preferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="preferredMaintenanceWindow"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateRelationalDatabaseSnapshotRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    relational_database_snapshot_name: str = Field(
        alias="relationalDatabaseSnapshotName"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class DiskSnapshotModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    size_in_gb: Optional[int] = Field(default=None, alias="sizeInGb")
    state: Optional[Literal["completed", "error", "pending", "unknown"]] = Field(
        default=None, alias="state"
    )
    progress: Optional[str] = Field(default=None, alias="progress")
    from_disk_name: Optional[str] = Field(default=None, alias="fromDiskName")
    from_disk_arn: Optional[str] = Field(default=None, alias="fromDiskArn")
    from_instance_name: Optional[str] = Field(default=None, alias="fromInstanceName")
    from_instance_arn: Optional[str] = Field(default=None, alias="fromInstanceArn")
    is_from_auto_snapshot: Optional[bool] = Field(
        default=None, alias="isFromAutoSnapshot"
    )


class DiskModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    add_ons: Optional[List[AddOnModel]] = Field(default=None, alias="addOns")
    size_in_gb: Optional[int] = Field(default=None, alias="sizeInGb")
    is_system_disk: Optional[bool] = Field(default=None, alias="isSystemDisk")
    iops: Optional[int] = Field(default=None, alias="iops")
    path: Optional[str] = Field(default=None, alias="path")
    state: Optional[
        Literal["available", "error", "in-use", "pending", "unknown"]
    ] = Field(default=None, alias="state")
    attached_to: Optional[str] = Field(default=None, alias="attachedTo")
    is_attached: Optional[bool] = Field(default=None, alias="isAttached")
    attachment_state: Optional[str] = Field(default=None, alias="attachmentState")
    gb_in_use: Optional[int] = Field(default=None, alias="gbInUse")
    auto_mount_status: Optional[
        Literal["Failed", "Mounted", "NotMounted", "Pending"]
    ] = Field(default=None, alias="autoMountStatus")


class KeyPairModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    fingerprint: Optional[str] = Field(default=None, alias="fingerprint")


class RelationalDatabaseSnapshotModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    engine: Optional[str] = Field(default=None, alias="engine")
    engine_version: Optional[str] = Field(default=None, alias="engineVersion")
    size_in_gb: Optional[int] = Field(default=None, alias="sizeInGb")
    state: Optional[str] = Field(default=None, alias="state")
    from_relational_database_name: Optional[str] = Field(
        default=None, alias="fromRelationalDatabaseName"
    )
    from_relational_database_arn: Optional[str] = Field(
        default=None, alias="fromRelationalDatabaseArn"
    )
    from_relational_database_bundle_id: Optional[str] = Field(
        default=None, alias="fromRelationalDatabaseBundleId"
    )
    from_relational_database_blueprint_id: Optional[str] = Field(
        default=None, alias="fromRelationalDatabaseBlueprintId"
    )


class TagResourceRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    tags: Sequence[TagModel] = Field(alias="tags")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")


class GetBundlesResultModel(BaseModel):
    bundles: List[BundleModel] = Field(alias="bundles")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CacheSettingsModel(BaseModel):
    default_ttl: Optional[int] = Field(default=None, alias="defaultTTL")
    minimum_ttl: Optional[int] = Field(default=None, alias="minimumTTL")
    maximum_ttl: Optional[int] = Field(default=None, alias="maximumTTL")
    allowed_http_methods: Optional[str] = Field(
        default=None, alias="allowedHTTPMethods"
    )
    cached_http_methods: Optional[str] = Field(default=None, alias="cachedHTTPMethods")
    forwarded_cookies: Optional[CookieObjectModel] = Field(
        default=None, alias="forwardedCookies"
    )
    forwarded_headers: Optional[HeaderObjectModel] = Field(
        default=None, alias="forwardedHeaders"
    )
    forwarded_query_strings: Optional[QueryStringObjectModel] = Field(
        default=None, alias="forwardedQueryStrings"
    )


class CloseInstancePublicPortsRequestModel(BaseModel):
    port_info: PortInfoModel = Field(alias="portInfo")
    instance_name: str = Field(alias="instanceName")


class OpenInstancePublicPortsRequestModel(BaseModel):
    port_info: PortInfoModel = Field(alias="portInfo")
    instance_name: str = Field(alias="instanceName")


class PutInstancePublicPortsRequestModel(BaseModel):
    port_infos: Sequence[PortInfoModel] = Field(alias="portInfos")
    instance_name: str = Field(alias="instanceName")


class CloudFormationStackRecordModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    state: Optional[Literal["Failed", "Started", "Succeeded"]] = Field(
        default=None, alias="state"
    )
    source_info: Optional[List[CloudFormationStackRecordSourceInfoModel]] = Field(
        default=None, alias="sourceInfo"
    )
    destination_info: Optional[DestinationInfoModel] = Field(
        default=None, alias="destinationInfo"
    )


class GetContainerImagesResultModel(BaseModel):
    container_images: List[ContainerImageModel] = Field(alias="containerImages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterContainerImageResultModel(BaseModel):
    container_image: ContainerImageModel = Field(alias="containerImage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PrivateRegistryAccessRequestModel(BaseModel):
    ecr_image_puller_role: Optional[
        ContainerServiceECRImagePullerRoleRequestModel
    ] = Field(default=None, alias="ecrImagePullerRole")


class PrivateRegistryAccessModel(BaseModel):
    ecr_image_puller_role: Optional[ContainerServiceECRImagePullerRoleModel] = Field(
        default=None, alias="ecrImagePullerRole"
    )


class ContainerServiceEndpointModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="containerName")
    container_port: Optional[int] = Field(default=None, alias="containerPort")
    health_check: Optional[ContainerServiceHealthCheckConfigModel] = Field(
        default=None, alias="healthCheck"
    )


class EndpointRequestModel(BaseModel):
    container_name: str = Field(alias="containerName")
    container_port: int = Field(alias="containerPort")
    health_check: Optional[ContainerServiceHealthCheckConfigModel] = Field(
        default=None, alias="healthCheck"
    )


class GetContainerLogResultModel(BaseModel):
    log_events: List[ContainerServiceLogEventModel] = Field(alias="logEvents")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContainerServicePowersResultModel(BaseModel):
    powers: List[ContainerServicePowerModel] = Field(alias="powers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContainerServiceRegistryLoginResultModel(BaseModel):
    registry_login: ContainerServiceRegistryLoginModel = Field(alias="registryLogin")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCloudFormationStackRequestModel(BaseModel):
    instances: Sequence[InstanceEntryModel] = Field(alias="instances")


class CreateDomainEntryRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    domain_entry: DomainEntryModel = Field(alias="domainEntry")


class DeleteDomainEntryRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    domain_entry: DomainEntryModel = Field(alias="domainEntry")


class UpdateDomainEntryRequestModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    domain_entry: DomainEntryModel = Field(alias="domainEntry")


class CreateGUISessionAccessDetailsResultModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    status: Literal[
        "failedInstanceCreation",
        "failedStartingGUISession",
        "failedStoppingGUISession",
        "notStarted",
        "settingUpInstance",
        "startExpired",
        "started",
        "starting",
        "stopped",
        "stopping",
    ] = Field(alias="status")
    percentage_complete: int = Field(alias="percentageComplete")
    failure_reason: str = Field(alias="failureReason")
    sessions: List[SessionModel] = Field(alias="sessions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceSnapshotInfoModel(BaseModel):
    from_bundle_id: Optional[str] = Field(default=None, alias="fromBundleId")
    from_blueprint_id: Optional[str] = Field(default=None, alias="fromBlueprintId")
    from_disk_info: Optional[List[DiskInfoModel]] = Field(
        default=None, alias="fromDiskInfo"
    )


class GetDistributionBundlesResultModel(BaseModel):
    bundles: List[DistributionBundleModel] = Field(alias="bundles")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainValidationRecordModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    resource_record: Optional[ResourceRecordModel] = Field(
        default=None, alias="resourceRecord"
    )
    dns_record_creation_state: Optional[DnsRecordCreationStateModel] = Field(
        default=None, alias="dnsRecordCreationState"
    )
    validation_status: Optional[
        Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
    ] = Field(default=None, alias="validationStatus")


class EstimateByTimeModel(BaseModel):
    usage_cost: Optional[float] = Field(default=None, alias="usageCost")
    pricing_unit: Optional[Literal["Bundles", "GB", "GB-Mo", "Hrs", "Queries"]] = Field(
        default=None, alias="pricingUnit"
    )
    unit: Optional[float] = Field(default=None, alias="unit")
    currency: Optional[Literal["USD"]] = Field(default=None, alias="currency")
    time_period: Optional[TimePeriodModel] = Field(default=None, alias="timePeriod")


class GetActiveNamesRequestGetActiveNamesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBlueprintsRequestGetBlueprintsPaginateModel(BaseModel):
    include_inactive: Optional[bool] = Field(default=None, alias="includeInactive")
    app_category: Optional[Literal["LfR"]] = Field(default=None, alias="appCategory")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBundlesRequestGetBundlesPaginateModel(BaseModel):
    include_inactive: Optional[bool] = Field(default=None, alias="includeInactive")
    app_category: Optional[Literal["LfR"]] = Field(default=None, alias="appCategory")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetCloudFormationStackRecordsRequestGetCloudFormationStackRecordsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDiskSnapshotsRequestGetDiskSnapshotsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDisksRequestGetDisksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetDomainsRequestGetDomainsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetExportSnapshotRecordsRequestGetExportSnapshotRecordsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetInstanceSnapshotsRequestGetInstanceSnapshotsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetInstancesRequestGetInstancesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetKeyPairsRequestGetKeyPairsPaginateModel(BaseModel):
    include_default_key_pair: Optional[bool] = Field(
        default=None, alias="includeDefaultKeyPair"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetLoadBalancersRequestGetLoadBalancersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetOperationsRequestGetOperationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRelationalDatabaseBlueprintsRequestGetRelationalDatabaseBlueprintsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRelationalDatabaseBundlesRequestGetRelationalDatabaseBundlesPaginateModel(
    BaseModel
):
    include_inactive: Optional[bool] = Field(default=None, alias="includeInactive")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRelationalDatabaseEventsRequestGetRelationalDatabaseEventsPaginateModel(
    BaseModel
):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    duration_in_minutes: Optional[int] = Field(default=None, alias="durationInMinutes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRelationalDatabaseParametersRequestGetRelationalDatabaseParametersPaginateModel(
    BaseModel
):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRelationalDatabaseSnapshotsRequestGetRelationalDatabaseSnapshotsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetRelationalDatabasesRequestGetRelationalDatabasesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetStaticIpsRequestGetStaticIpsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetBucketMetricDataResultModel(BaseModel):
    metric_name: Literal["BucketSizeBytes", "NumberOfObjects"] = Field(
        alias="metricName"
    )
    metric_data: List[MetricDatapointModel] = Field(alias="metricData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContainerServiceMetricDataResultModel(BaseModel):
    metric_name: Literal["CPUUtilization", "MemoryUtilization"] = Field(
        alias="metricName"
    )
    metric_data: List[MetricDatapointModel] = Field(alias="metricData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDistributionMetricDataResultModel(BaseModel):
    metric_name: Literal[
        "BytesDownloaded",
        "BytesUploaded",
        "Http4xxErrorRate",
        "Http5xxErrorRate",
        "Requests",
        "TotalErrorRate",
    ] = Field(alias="metricName")
    metric_data: List[MetricDatapointModel] = Field(alias="metricData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceMetricDataResultModel(BaseModel):
    metric_name: Literal[
        "BurstCapacityPercentage",
        "BurstCapacityTime",
        "CPUUtilization",
        "MetadataNoToken",
        "NetworkIn",
        "NetworkOut",
        "StatusCheckFailed",
        "StatusCheckFailed_Instance",
        "StatusCheckFailed_System",
    ] = Field(alias="metricName")
    metric_data: List[MetricDatapointModel] = Field(alias="metricData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLoadBalancerMetricDataResultModel(BaseModel):
    metric_name: Literal[
        "ClientTLSNegotiationErrorCount",
        "HTTPCode_Instance_2XX_Count",
        "HTTPCode_Instance_3XX_Count",
        "HTTPCode_Instance_4XX_Count",
        "HTTPCode_Instance_5XX_Count",
        "HTTPCode_LB_4XX_Count",
        "HTTPCode_LB_5XX_Count",
        "HealthyHostCount",
        "InstanceResponseTime",
        "RejectedConnectionCount",
        "RequestCount",
        "UnhealthyHostCount",
    ] = Field(alias="metricName")
    metric_data: List[MetricDatapointModel] = Field(alias="metricData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseMetricDataResultModel(BaseModel):
    metric_name: Literal[
        "CPUUtilization",
        "DatabaseConnections",
        "DiskQueueDepth",
        "FreeStorageSpace",
        "NetworkReceiveThroughput",
        "NetworkTransmitThroughput",
    ] = Field(alias="metricName")
    metric_data: List[MetricDatapointModel] = Field(alias="metricData")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstancePortStatesResultModel(BaseModel):
    port_states: List[InstancePortStateModel] = Field(alias="portStates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceStateResultModel(BaseModel):
    state: InstanceStateModel = Field(alias="state")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLoadBalancerTlsPoliciesResultModel(BaseModel):
    tls_policies: List[LoadBalancerTlsPolicyModel] = Field(alias="tlsPolicies")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseBlueprintsResultModel(BaseModel):
    blueprints: List[RelationalDatabaseBlueprintModel] = Field(alias="blueprints")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseBundlesResultModel(BaseModel):
    bundles: List[RelationalDatabaseBundleModel] = Field(alias="bundles")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseEventsResultModel(BaseModel):
    relational_database_events: List[RelationalDatabaseEventModel] = Field(
        alias="relationalDatabaseEvents"
    )
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseLogEventsResultModel(BaseModel):
    resource_log_events: List[LogEventModel] = Field(alias="resourceLogEvents")
    next_backward_token: str = Field(alias="nextBackwardToken")
    next_forward_token: str = Field(alias="nextForwardToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseParametersResultModel(BaseModel):
    parameters: List[RelationalDatabaseParameterModel] = Field(alias="parameters")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRelationalDatabaseParametersRequestModel(BaseModel):
    relational_database_name: str = Field(alias="relationalDatabaseName")
    parameters: Sequence[RelationalDatabaseParameterModel] = Field(alias="parameters")


class InstanceAccessDetailsModel(BaseModel):
    cert_key: Optional[str] = Field(default=None, alias="certKey")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")
    ip_address: Optional[str] = Field(default=None, alias="ipAddress")
    password: Optional[str] = Field(default=None, alias="password")
    password_data: Optional[PasswordDataModel] = Field(
        default=None, alias="passwordData"
    )
    private_key: Optional[str] = Field(default=None, alias="privateKey")
    protocol: Optional[Literal["rdp", "ssh"]] = Field(default=None, alias="protocol")
    instance_name: Optional[str] = Field(default=None, alias="instanceName")
    username: Optional[str] = Field(default=None, alias="username")
    host_keys: Optional[List[HostKeyAttributesModel]] = Field(
        default=None, alias="hostKeys"
    )


class InstanceNetworkingModel(BaseModel):
    monthly_transfer: Optional[MonthlyTransferModel] = Field(
        default=None, alias="monthlyTransfer"
    )
    ports: Optional[List[InstancePortInfoModel]] = Field(default=None, alias="ports")


class LoadBalancerTlsCertificateDomainValidationRecordModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")
    value: Optional[str] = Field(default=None, alias="value")
    validation_status: Optional[
        Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
    ] = Field(default=None, alias="validationStatus")
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    dns_record_creation_state: Optional[
        LoadBalancerTlsCertificateDnsRecordCreationStateModel
    ] = Field(default=None, alias="dnsRecordCreationState")


class LoadBalancerTlsCertificateRenewalSummaryModel(BaseModel):
    renewal_status: Optional[
        Literal["FAILED", "PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS"]
    ] = Field(default=None, alias="renewalStatus")
    domain_validation_options: Optional[
        List[LoadBalancerTlsCertificateDomainValidationOptionModel]
    ] = Field(default=None, alias="domainValidationOptions")


class LoadBalancerModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    dns_name: Optional[str] = Field(default=None, alias="dnsName")
    state: Optional[
        Literal["active", "active_impaired", "failed", "provisioning", "unknown"]
    ] = Field(default=None, alias="state")
    protocol: Optional[Literal["HTTP", "HTTP_HTTPS"]] = Field(
        default=None, alias="protocol"
    )
    public_ports: Optional[List[int]] = Field(default=None, alias="publicPorts")
    health_check_path: Optional[str] = Field(default=None, alias="healthCheckPath")
    instance_port: Optional[int] = Field(default=None, alias="instancePort")
    instance_health_summary: Optional[List[InstanceHealthSummaryModel]] = Field(
        default=None, alias="instanceHealthSummary"
    )
    tls_certificate_summaries: Optional[
        List[LoadBalancerTlsCertificateSummaryModel]
    ] = Field(default=None, alias="tlsCertificateSummaries")
    configuration_options: Optional[
        Dict[
            Literal[
                "HealthCheckPath",
                "HttpsRedirectionEnabled",
                "SessionStickinessEnabled",
                "SessionStickiness_LB_CookieDurationSeconds",
                "TlsPolicyName",
            ],
            str,
        ]
    ] = Field(default=None, alias="configurationOptions")
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="ipAddressType"
    )
    https_redirection_enabled: Optional[bool] = Field(
        default=None, alias="httpsRedirectionEnabled"
    )
    tls_policy_name: Optional[str] = Field(default=None, alias="tlsPolicyName")


class RegisteredDomainDelegationInfoModel(BaseModel):
    name_servers_update_state: Optional[NameServersUpdateStateModel] = Field(
        default=None, alias="nameServersUpdateState"
    )
    r53_hosted_zone_deletion_state: Optional[R53HostedZoneDeletionStateModel] = Field(
        default=None, alias="r53HostedZoneDeletionState"
    )


class RelationalDatabaseModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    relational_database_blueprint_id: Optional[str] = Field(
        default=None, alias="relationalDatabaseBlueprintId"
    )
    relational_database_bundle_id: Optional[str] = Field(
        default=None, alias="relationalDatabaseBundleId"
    )
    master_database_name: Optional[str] = Field(
        default=None, alias="masterDatabaseName"
    )
    hardware: Optional[RelationalDatabaseHardwareModel] = Field(
        default=None, alias="hardware"
    )
    state: Optional[str] = Field(default=None, alias="state")
    secondary_availability_zone: Optional[str] = Field(
        default=None, alias="secondaryAvailabilityZone"
    )
    backup_retention_enabled: Optional[bool] = Field(
        default=None, alias="backupRetentionEnabled"
    )
    pending_modified_values: Optional[
        PendingModifiedRelationalDatabaseValuesModel
    ] = Field(default=None, alias="pendingModifiedValues")
    engine: Optional[str] = Field(default=None, alias="engine")
    engine_version: Optional[str] = Field(default=None, alias="engineVersion")
    latest_restorable_time: Optional[datetime] = Field(
        default=None, alias="latestRestorableTime"
    )
    master_username: Optional[str] = Field(default=None, alias="masterUsername")
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="parameterApplyStatus"
    )
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="preferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="preferredMaintenanceWindow"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="publiclyAccessible"
    )
    master_endpoint: Optional[RelationalDatabaseEndpointModel] = Field(
        default=None, alias="masterEndpoint"
    )
    pending_maintenance_actions: Optional[List[PendingMaintenanceActionModel]] = Field(
        default=None, alias="pendingMaintenanceActions"
    )
    ca_certificate_identifier: Optional[str] = Field(
        default=None, alias="caCertificateIdentifier"
    )


class GetBucketAccessKeysResultModel(BaseModel):
    access_keys: List[AccessKeyModel] = Field(alias="accessKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDiskFromSnapshotRequestModel(BaseModel):
    disk_name: str = Field(alias="diskName")
    availability_zone: str = Field(alias="availabilityZone")
    size_in_gb: int = Field(alias="sizeInGb")
    disk_snapshot_name: Optional[str] = Field(default=None, alias="diskSnapshotName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    add_ons: Optional[Sequence[AddOnRequestModel]] = Field(default=None, alias="addOns")
    source_disk_name: Optional[str] = Field(default=None, alias="sourceDiskName")
    restore_date: Optional[str] = Field(default=None, alias="restoreDate")
    use_latest_restorable_auto_snapshot: Optional[bool] = Field(
        default=None, alias="useLatestRestorableAutoSnapshot"
    )


class CreateDiskRequestModel(BaseModel):
    disk_name: str = Field(alias="diskName")
    availability_zone: str = Field(alias="availabilityZone")
    size_in_gb: int = Field(alias="sizeInGb")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    add_ons: Optional[Sequence[AddOnRequestModel]] = Field(default=None, alias="addOns")


class CreateInstancesFromSnapshotRequestModel(BaseModel):
    instance_names: Sequence[str] = Field(alias="instanceNames")
    availability_zone: str = Field(alias="availabilityZone")
    bundle_id: str = Field(alias="bundleId")
    attached_disk_mapping: Optional[Mapping[str, Sequence[DiskMapModel]]] = Field(
        default=None, alias="attachedDiskMapping"
    )
    instance_snapshot_name: Optional[str] = Field(
        default=None, alias="instanceSnapshotName"
    )
    user_data: Optional[str] = Field(default=None, alias="userData")
    key_pair_name: Optional[str] = Field(default=None, alias="keyPairName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    add_ons: Optional[Sequence[AddOnRequestModel]] = Field(default=None, alias="addOns")
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="ipAddressType"
    )
    source_instance_name: Optional[str] = Field(
        default=None, alias="sourceInstanceName"
    )
    restore_date: Optional[str] = Field(default=None, alias="restoreDate")
    use_latest_restorable_auto_snapshot: Optional[bool] = Field(
        default=None, alias="useLatestRestorableAutoSnapshot"
    )


class CreateInstancesRequestModel(BaseModel):
    instance_names: Sequence[str] = Field(alias="instanceNames")
    availability_zone: str = Field(alias="availabilityZone")
    blueprint_id: str = Field(alias="blueprintId")
    bundle_id: str = Field(alias="bundleId")
    custom_image_name: Optional[str] = Field(default=None, alias="customImageName")
    user_data: Optional[str] = Field(default=None, alias="userData")
    key_pair_name: Optional[str] = Field(default=None, alias="keyPairName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    add_ons: Optional[Sequence[AddOnRequestModel]] = Field(default=None, alias="addOns")
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="ipAddressType"
    )


class EnableAddOnRequestModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    add_on_request: AddOnRequestModel = Field(alias="addOnRequest")


class GetAlarmsResultModel(BaseModel):
    alarms: List[AlarmModel] = Field(alias="alarms")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetContactMethodsResultModel(BaseModel):
    contact_methods: List[ContactMethodModel] = Field(alias="contactMethods")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AllocateStaticIpResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachCertificateToDistributionResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachDiskResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachInstancesToLoadBalancerResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachLoadBalancerTlsCertificateResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachStaticIpResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CloseInstancePublicPortsResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopySnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBucketAccessKeyResultModel(BaseModel):
    access_key: AccessKeyModel = Field(alias="accessKey")
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCloudFormationStackResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContactMethodResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDiskFromSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDiskResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDiskSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainEntryResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstanceSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstancesFromSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstancesResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoadBalancerResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoadBalancerTlsCertificateResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRelationalDatabaseFromSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRelationalDatabaseResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRelationalDatabaseSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAlarmResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAutoSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBucketAccessKeyResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBucketResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCertificateResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteContactMethodResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDiskResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDiskSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDistributionResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainEntryResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInstanceResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInstanceSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteKeyPairResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteKnownHostKeysResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteLoadBalancerResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteLoadBalancerTlsCertificateResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRelationalDatabaseResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRelationalDatabaseSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachCertificateFromDistributionResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachDiskResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachInstancesFromLoadBalancerResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachStaticIpResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableAddOnResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableAddOnResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportSnapshotResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOperationResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOperationsForResourceResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    next_page_count: str = Field(alias="nextPageCount")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOperationsResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportKeyPairResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OpenInstancePublicPortsResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PeerVpcResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAlarmResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutInstancePublicPortsResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootInstanceResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RebootRelationalDatabaseResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReleaseStaticIpResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetDistributionCacheResultModel(BaseModel):
    status: str = Field(alias="status")
    create_time: datetime = Field(alias="createTime")
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendContactMethodVerificationResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetIpAddressTypeResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetResourceAccessForBucketResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartGUISessionResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartInstanceResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRelationalDatabaseResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopGUISessionResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopInstanceResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopRelationalDatabaseResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestAlarmResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UnpeerVpcResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UntagResourceResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBucketBundleResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDistributionBundleResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDistributionResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainEntryResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInstanceMetadataOptionsResultModel(BaseModel):
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLoadBalancerAttributeResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRelationalDatabaseParametersResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRelationalDatabaseResultModel(BaseModel):
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStaticIpResultModel(BaseModel):
    static_ip: StaticIpModel = Field(alias="staticIp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStaticIpsResultModel(BaseModel):
    static_ips: List[StaticIpModel] = Field(alias="staticIps")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAutoSnapshotsResultModel(BaseModel):
    resource_name: str = Field(alias="resourceName")
    resource_type: Literal[
        "Alarm",
        "Bucket",
        "Certificate",
        "CloudFormationStackRecord",
        "ContactMethod",
        "ContainerService",
        "Disk",
        "DiskSnapshot",
        "Distribution",
        "Domain",
        "ExportSnapshotRecord",
        "Instance",
        "InstanceSnapshot",
        "KeyPair",
        "LoadBalancer",
        "LoadBalancerTlsCertificate",
        "PeeredVpc",
        "RelationalDatabase",
        "RelationalDatabaseSnapshot",
        "StaticIp",
    ] = Field(alias="resourceType")
    auto_snapshots: List[AutoSnapshotDetailsModel] = Field(alias="autoSnapshots")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegionsResultModel(BaseModel):
    regions: List[RegionModel] = Field(alias="regions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBucketResultModel(BaseModel):
    bucket: BucketModel = Field(alias="bucket")
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBucketsResultModel(BaseModel):
    buckets: List[BucketModel] = Field(alias="buckets")
    next_page_token: str = Field(alias="nextPageToken")
    account_level_bpa_sync: AccountLevelBpaSyncModel = Field(
        alias="accountLevelBpaSync"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBucketResultModel(BaseModel):
    bucket: BucketModel = Field(alias="bucket")
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDiskSnapshotResultModel(BaseModel):
    disk_snapshot: DiskSnapshotModel = Field(alias="diskSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDiskSnapshotsResultModel(BaseModel):
    disk_snapshots: List[DiskSnapshotModel] = Field(alias="diskSnapshots")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDiskResultModel(BaseModel):
    disk: DiskModel = Field(alias="disk")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDisksResultModel(BaseModel):
    disks: List[DiskModel] = Field(alias="disks")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceHardwareModel(BaseModel):
    cpu_count: Optional[int] = Field(default=None, alias="cpuCount")
    disks: Optional[List[DiskModel]] = Field(default=None, alias="disks")
    ram_size_in_gb: Optional[float] = Field(default=None, alias="ramSizeInGb")


class InstanceSnapshotModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    state: Optional[Literal["available", "error", "pending"]] = Field(
        default=None, alias="state"
    )
    progress: Optional[str] = Field(default=None, alias="progress")
    from_attached_disks: Optional[List[DiskModel]] = Field(
        default=None, alias="fromAttachedDisks"
    )
    from_instance_name: Optional[str] = Field(default=None, alias="fromInstanceName")
    from_instance_arn: Optional[str] = Field(default=None, alias="fromInstanceArn")
    from_blueprint_id: Optional[str] = Field(default=None, alias="fromBlueprintId")
    from_bundle_id: Optional[str] = Field(default=None, alias="fromBundleId")
    is_from_auto_snapshot: Optional[bool] = Field(
        default=None, alias="isFromAutoSnapshot"
    )
    size_in_gb: Optional[int] = Field(default=None, alias="sizeInGb")


class CreateKeyPairResultModel(BaseModel):
    key_pair: KeyPairModel = Field(alias="keyPair")
    public_key_base64: str = Field(alias="publicKeyBase64")
    private_key_base64: str = Field(alias="privateKeyBase64")
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetKeyPairResultModel(BaseModel):
    key_pair: KeyPairModel = Field(alias="keyPair")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetKeyPairsResultModel(BaseModel):
    key_pairs: List[KeyPairModel] = Field(alias="keyPairs")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseSnapshotResultModel(BaseModel):
    relational_database_snapshot: RelationalDatabaseSnapshotModel = Field(
        alias="relationalDatabaseSnapshot"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabaseSnapshotsResultModel(BaseModel):
    relational_database_snapshots: List[RelationalDatabaseSnapshotModel] = Field(
        alias="relationalDatabaseSnapshots"
    )
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDistributionRequestModel(BaseModel):
    distribution_name: str = Field(alias="distributionName")
    origin: InputOriginModel = Field(alias="origin")
    default_cache_behavior: CacheBehaviorModel = Field(alias="defaultCacheBehavior")
    bundle_id: str = Field(alias="bundleId")
    cache_behavior_settings: Optional[CacheSettingsModel] = Field(
        default=None, alias="cacheBehaviorSettings"
    )
    cache_behaviors: Optional[Sequence[CacheBehaviorPerPathModel]] = Field(
        default=None, alias="cacheBehaviors"
    )
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="ipAddressType"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class LightsailDistributionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    alternative_domain_names: Optional[List[str]] = Field(
        default=None, alias="alternativeDomainNames"
    )
    status: Optional[str] = Field(default=None, alias="status")
    is_enabled: Optional[bool] = Field(default=None, alias="isEnabled")
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    certificate_name: Optional[str] = Field(default=None, alias="certificateName")
    origin: Optional[OriginModel] = Field(default=None, alias="origin")
    origin_public_dns: Optional[str] = Field(default=None, alias="originPublicDNS")
    default_cache_behavior: Optional[CacheBehaviorModel] = Field(
        default=None, alias="defaultCacheBehavior"
    )
    cache_behavior_settings: Optional[CacheSettingsModel] = Field(
        default=None, alias="cacheBehaviorSettings"
    )
    cache_behaviors: Optional[List[CacheBehaviorPerPathModel]] = Field(
        default=None, alias="cacheBehaviors"
    )
    able_to_update_bundle: Optional[bool] = Field(
        default=None, alias="ableToUpdateBundle"
    )
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="ipAddressType"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class UpdateDistributionRequestModel(BaseModel):
    distribution_name: str = Field(alias="distributionName")
    origin: Optional[InputOriginModel] = Field(default=None, alias="origin")
    default_cache_behavior: Optional[CacheBehaviorModel] = Field(
        default=None, alias="defaultCacheBehavior"
    )
    cache_behavior_settings: Optional[CacheSettingsModel] = Field(
        default=None, alias="cacheBehaviorSettings"
    )
    cache_behaviors: Optional[Sequence[CacheBehaviorPerPathModel]] = Field(
        default=None, alias="cacheBehaviors"
    )
    is_enabled: Optional[bool] = Field(default=None, alias="isEnabled")


class GetCloudFormationStackRecordsResultModel(BaseModel):
    cloud_formation_stack_records: List[CloudFormationStackRecordModel] = Field(
        alias="cloudFormationStackRecords"
    )
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContainerServiceRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    power: Optional[
        Literal["large", "medium", "micro", "nano", "small", "xlarge"]
    ] = Field(default=None, alias="power")
    scale: Optional[int] = Field(default=None, alias="scale")
    is_disabled: Optional[bool] = Field(default=None, alias="isDisabled")
    public_domain_names: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="publicDomainNames"
    )
    private_registry_access: Optional[PrivateRegistryAccessRequestModel] = Field(
        default=None, alias="privateRegistryAccess"
    )


class ContainerServiceDeploymentModel(BaseModel):
    version: Optional[int] = Field(default=None, alias="version")
    state: Optional[Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"]] = Field(
        default=None, alias="state"
    )
    containers: Optional[Dict[str, ContainerModel]] = Field(
        default=None, alias="containers"
    )
    public_endpoint: Optional[ContainerServiceEndpointModel] = Field(
        default=None, alias="publicEndpoint"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class ContainerServiceDeploymentRequestModel(BaseModel):
    containers: Optional[Mapping[str, ContainerModel]] = Field(
        default=None, alias="containers"
    )
    public_endpoint: Optional[EndpointRequestModel] = Field(
        default=None, alias="publicEndpoint"
    )


class CreateContainerServiceDeploymentRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    containers: Optional[Mapping[str, ContainerModel]] = Field(
        default=None, alias="containers"
    )
    public_endpoint: Optional[EndpointRequestModel] = Field(
        default=None, alias="publicEndpoint"
    )


class ExportSnapshotRecordSourceInfoModel(BaseModel):
    resource_type: Optional[Literal["DiskSnapshot", "InstanceSnapshot"]] = Field(
        default=None, alias="resourceType"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    from_resource_name: Optional[str] = Field(default=None, alias="fromResourceName")
    from_resource_arn: Optional[str] = Field(default=None, alias="fromResourceArn")
    instance_snapshot_info: Optional[InstanceSnapshotInfoModel] = Field(
        default=None, alias="instanceSnapshotInfo"
    )
    disk_snapshot_info: Optional[DiskSnapshotInfoModel] = Field(
        default=None, alias="diskSnapshotInfo"
    )


class RenewalSummaryModel(BaseModel):
    domain_validation_records: Optional[List[DomainValidationRecordModel]] = Field(
        default=None, alias="domainValidationRecords"
    )
    renewal_status: Optional[
        Literal["Failed", "PendingAutoRenewal", "PendingValidation", "Success"]
    ] = Field(default=None, alias="renewalStatus")
    renewal_status_reason: Optional[str] = Field(
        default=None, alias="renewalStatusReason"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class CostEstimateModel(BaseModel):
    usage_type: Optional[str] = Field(default=None, alias="usageType")
    results_by_time: Optional[List[EstimateByTimeModel]] = Field(
        default=None, alias="resultsByTime"
    )


class GetInstanceAccessDetailsResultModel(BaseModel):
    access_details: InstanceAccessDetailsModel = Field(alias="accessDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LoadBalancerTlsCertificateModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    load_balancer_name: Optional[str] = Field(default=None, alias="loadBalancerName")
    is_attached: Optional[bool] = Field(default=None, alias="isAttached")
    status: Optional[
        Literal[
            "EXPIRED",
            "FAILED",
            "INACTIVE",
            "ISSUED",
            "PENDING_VALIDATION",
            "REVOKED",
            "UNKNOWN",
            "VALIDATION_TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    domain_validation_records: Optional[
        List[LoadBalancerTlsCertificateDomainValidationRecordModel]
    ] = Field(default=None, alias="domainValidationRecords")
    failure_reason: Optional[
        Literal[
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "NO_AVAILABLE_CONTACTS",
            "OTHER",
        ]
    ] = Field(default=None, alias="failureReason")
    issued_at: Optional[datetime] = Field(default=None, alias="issuedAt")
    issuer: Optional[str] = Field(default=None, alias="issuer")
    key_algorithm: Optional[str] = Field(default=None, alias="keyAlgorithm")
    not_after: Optional[datetime] = Field(default=None, alias="notAfter")
    not_before: Optional[datetime] = Field(default=None, alias="notBefore")
    renewal_summary: Optional[LoadBalancerTlsCertificateRenewalSummaryModel] = Field(
        default=None, alias="renewalSummary"
    )
    revocation_reason: Optional[
        Literal[
            "AFFILIATION_CHANGED",
            "A_A_COMPROMISE",
            "CA_COMPROMISE",
            "CERTIFICATE_HOLD",
            "CESSATION_OF_OPERATION",
            "KEY_COMPROMISE",
            "PRIVILEGE_WITHDRAWN",
            "REMOVE_FROM_CRL",
            "SUPERCEDED",
            "UNSPECIFIED",
        ]
    ] = Field(default=None, alias="revocationReason")
    revoked_at: Optional[datetime] = Field(default=None, alias="revokedAt")
    serial: Optional[str] = Field(default=None, alias="serial")
    signature_algorithm: Optional[str] = Field(default=None, alias="signatureAlgorithm")
    subject: Optional[str] = Field(default=None, alias="subject")
    subject_alternative_names: Optional[List[str]] = Field(
        default=None, alias="subjectAlternativeNames"
    )


class GetLoadBalancerResultModel(BaseModel):
    load_balancer: LoadBalancerModel = Field(alias="loadBalancer")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLoadBalancersResultModel(BaseModel):
    load_balancers: List[LoadBalancerModel] = Field(alias="loadBalancers")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DomainModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    domain_entries: Optional[List[DomainEntryModel]] = Field(
        default=None, alias="domainEntries"
    )
    registered_domain_delegation_info: Optional[
        RegisteredDomainDelegationInfoModel
    ] = Field(default=None, alias="registeredDomainDelegationInfo")


class GetRelationalDatabaseResultModel(BaseModel):
    relational_database: RelationalDatabaseModel = Field(alias="relationalDatabase")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRelationalDatabasesResultModel(BaseModel):
    relational_databases: List[RelationalDatabaseModel] = Field(
        alias="relationalDatabases"
    )
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    support_code: Optional[str] = Field(default=None, alias="supportCode")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    blueprint_id: Optional[str] = Field(default=None, alias="blueprintId")
    blueprint_name: Optional[str] = Field(default=None, alias="blueprintName")
    bundle_id: Optional[str] = Field(default=None, alias="bundleId")
    add_ons: Optional[List[AddOnModel]] = Field(default=None, alias="addOns")
    is_static_ip: Optional[bool] = Field(default=None, alias="isStaticIp")
    private_ip_address: Optional[str] = Field(default=None, alias="privateIpAddress")
    public_ip_address: Optional[str] = Field(default=None, alias="publicIpAddress")
    ipv6_addresses: Optional[List[str]] = Field(default=None, alias="ipv6Addresses")
    ip_address_type: Optional[Literal["dualstack", "ipv4"]] = Field(
        default=None, alias="ipAddressType"
    )
    hardware: Optional[InstanceHardwareModel] = Field(default=None, alias="hardware")
    networking: Optional[InstanceNetworkingModel] = Field(
        default=None, alias="networking"
    )
    state: Optional[InstanceStateModel] = Field(default=None, alias="state")
    username: Optional[str] = Field(default=None, alias="username")
    ssh_key_name: Optional[str] = Field(default=None, alias="sshKeyName")
    metadata_options: Optional[InstanceMetadataOptionsModel] = Field(
        default=None, alias="metadataOptions"
    )


class GetInstanceSnapshotResultModel(BaseModel):
    instance_snapshot: InstanceSnapshotModel = Field(alias="instanceSnapshot")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceSnapshotsResultModel(BaseModel):
    instance_snapshots: List[InstanceSnapshotModel] = Field(alias="instanceSnapshots")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDistributionResultModel(BaseModel):
    distribution: LightsailDistributionModel = Field(alias="distribution")
    operation: OperationModel = Field(alias="operation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDistributionsResultModel(BaseModel):
    distributions: List[LightsailDistributionModel] = Field(alias="distributions")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContainerServiceModel(BaseModel):
    container_service_name: Optional[str] = Field(
        default=None, alias="containerServiceName"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    power: Optional[
        Literal["large", "medium", "micro", "nano", "small", "xlarge"]
    ] = Field(default=None, alias="power")
    power_id: Optional[str] = Field(default=None, alias="powerId")
    state: Optional[
        Literal[
            "DELETING",
            "DEPLOYING",
            "DISABLED",
            "PENDING",
            "READY",
            "RUNNING",
            "UPDATING",
        ]
    ] = Field(default=None, alias="state")
    state_detail: Optional[ContainerServiceStateDetailModel] = Field(
        default=None, alias="stateDetail"
    )
    scale: Optional[int] = Field(default=None, alias="scale")
    current_deployment: Optional[ContainerServiceDeploymentModel] = Field(
        default=None, alias="currentDeployment"
    )
    next_deployment: Optional[ContainerServiceDeploymentModel] = Field(
        default=None, alias="nextDeployment"
    )
    is_disabled: Optional[bool] = Field(default=None, alias="isDisabled")
    principal_arn: Optional[str] = Field(default=None, alias="principalArn")
    private_domain_name: Optional[str] = Field(default=None, alias="privateDomainName")
    public_domain_names: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="publicDomainNames"
    )
    url: Optional[str] = Field(default=None, alias="url")
    private_registry_access: Optional[PrivateRegistryAccessModel] = Field(
        default=None, alias="privateRegistryAccess"
    )


class GetContainerServiceDeploymentsResultModel(BaseModel):
    deployments: List[ContainerServiceDeploymentModel] = Field(alias="deployments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContainerServiceRequestModel(BaseModel):
    service_name: str = Field(alias="serviceName")
    power: Literal["large", "medium", "micro", "nano", "small", "xlarge"] = Field(
        alias="power"
    )
    scale: int = Field(alias="scale")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    public_domain_names: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="publicDomainNames"
    )
    deployment: Optional[ContainerServiceDeploymentRequestModel] = Field(
        default=None, alias="deployment"
    )
    private_registry_access: Optional[PrivateRegistryAccessRequestModel] = Field(
        default=None, alias="privateRegistryAccess"
    )


class ExportSnapshotRecordModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    location: Optional[ResourceLocationModel] = Field(default=None, alias="location")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    state: Optional[Literal["Failed", "Started", "Succeeded"]] = Field(
        default=None, alias="state"
    )
    source_info: Optional[ExportSnapshotRecordSourceInfoModel] = Field(
        default=None, alias="sourceInfo"
    )
    destination_info: Optional[DestinationInfoModel] = Field(
        default=None, alias="destinationInfo"
    )


class CertificateModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    status: Optional[
        Literal[
            "EXPIRED",
            "FAILED",
            "INACTIVE",
            "ISSUED",
            "PENDING_VALIDATION",
            "REVOKED",
            "VALIDATION_TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    serial_number: Optional[str] = Field(default=None, alias="serialNumber")
    subject_alternative_names: Optional[List[str]] = Field(
        default=None, alias="subjectAlternativeNames"
    )
    domain_validation_records: Optional[List[DomainValidationRecordModel]] = Field(
        default=None, alias="domainValidationRecords"
    )
    request_failure_reason: Optional[str] = Field(
        default=None, alias="requestFailureReason"
    )
    in_use_resource_count: Optional[int] = Field(
        default=None, alias="inUseResourceCount"
    )
    key_algorithm: Optional[str] = Field(default=None, alias="keyAlgorithm")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    issued_at: Optional[datetime] = Field(default=None, alias="issuedAt")
    issuer_ca: Optional[str] = Field(default=None, alias="issuerCA")
    not_before: Optional[datetime] = Field(default=None, alias="notBefore")
    not_after: Optional[datetime] = Field(default=None, alias="notAfter")
    eligible_to_renew: Optional[str] = Field(default=None, alias="eligibleToRenew")
    renewal_summary: Optional[RenewalSummaryModel] = Field(
        default=None, alias="renewalSummary"
    )
    revoked_at: Optional[datetime] = Field(default=None, alias="revokedAt")
    revocation_reason: Optional[str] = Field(default=None, alias="revocationReason")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    support_code: Optional[str] = Field(default=None, alias="supportCode")


class ResourceBudgetEstimateModel(BaseModel):
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    resource_type: Optional[
        Literal[
            "Alarm",
            "Bucket",
            "Certificate",
            "CloudFormationStackRecord",
            "ContactMethod",
            "ContainerService",
            "Disk",
            "DiskSnapshot",
            "Distribution",
            "Domain",
            "ExportSnapshotRecord",
            "Instance",
            "InstanceSnapshot",
            "KeyPair",
            "LoadBalancer",
            "LoadBalancerTlsCertificate",
            "PeeredVpc",
            "RelationalDatabase",
            "RelationalDatabaseSnapshot",
            "StaticIp",
        ]
    ] = Field(default=None, alias="resourceType")
    cost_estimates: Optional[List[CostEstimateModel]] = Field(
        default=None, alias="costEstimates"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")


class GetLoadBalancerTlsCertificatesResultModel(BaseModel):
    tls_certificates: List[LoadBalancerTlsCertificateModel] = Field(
        alias="tlsCertificates"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainResultModel(BaseModel):
    domain: DomainModel = Field(alias="domain")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainsResultModel(BaseModel):
    domains: List[DomainModel] = Field(alias="domains")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstanceResultModel(BaseModel):
    instance: InstanceModel = Field(alias="instance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInstancesResultModel(BaseModel):
    instances: List[InstanceModel] = Field(alias="instances")
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContainerServicesListResultModel(BaseModel):
    container_services: List[ContainerServiceModel] = Field(alias="containerServices")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContainerServiceDeploymentResultModel(BaseModel):
    container_service: ContainerServiceModel = Field(alias="containerService")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateContainerServiceResultModel(BaseModel):
    container_service: ContainerServiceModel = Field(alias="containerService")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateContainerServiceResultModel(BaseModel):
    container_service: ContainerServiceModel = Field(alias="containerService")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetExportSnapshotRecordsResultModel(BaseModel):
    export_snapshot_records: List[ExportSnapshotRecordModel] = Field(
        alias="exportSnapshotRecords"
    )
    next_page_token: str = Field(alias="nextPageToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CertificateSummaryModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_name: Optional[str] = Field(default=None, alias="certificateName")
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    certificate_detail: Optional[CertificateModel] = Field(
        default=None, alias="certificateDetail"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")


class GetCostEstimateResultModel(BaseModel):
    resources_budget_estimate: List[ResourceBudgetEstimateModel] = Field(
        alias="resourcesBudgetEstimate"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCertificateResultModel(BaseModel):
    certificate: CertificateSummaryModel = Field(alias="certificate")
    operations: List[OperationModel] = Field(alias="operations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCertificatesResultModel(BaseModel):
    certificates: List[CertificateSummaryModel] = Field(alias="certificates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
