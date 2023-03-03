# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptAdministratorInvitationRequestModel(BaseModel):
    administrator_id: str = Field(alias="AdministratorId")
    invitation_id: str = Field(alias="InvitationId")


class AcceptInvitationRequestModel(BaseModel):
    master_id: str = Field(alias="MasterId")
    invitation_id: str = Field(alias="InvitationId")


class AccountDetailsModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    email: Optional[str] = Field(default=None, alias="Email")


class ActionLocalIpDetailsModel(BaseModel):
    ip_address_v4: Optional[str] = Field(default=None, alias="IpAddressV4")


class ActionLocalPortDetailsModel(BaseModel):
    port: Optional[int] = Field(default=None, alias="Port")
    port_name: Optional[str] = Field(default=None, alias="PortName")


class CityModel(BaseModel):
    city_name: Optional[str] = Field(default=None, alias="CityName")


class CountryModel(BaseModel):
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    country_name: Optional[str] = Field(default=None, alias="CountryName")


class GeoLocationModel(BaseModel):
    lon: Optional[float] = Field(default=None, alias="Lon")
    lat: Optional[float] = Field(default=None, alias="Lat")


class IpOrganizationDetailsModel(BaseModel):
    asn: Optional[int] = Field(default=None, alias="Asn")
    asn_org: Optional[str] = Field(default=None, alias="AsnOrg")
    isp: Optional[str] = Field(default=None, alias="Isp")
    org: Optional[str] = Field(default=None, alias="Org")


class ActionRemotePortDetailsModel(BaseModel):
    port: Optional[int] = Field(default=None, alias="Port")
    port_name: Optional[str] = Field(default=None, alias="PortName")


class ActionTargetModel(BaseModel):
    action_target_arn: str = Field(alias="ActionTargetArn")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")


class DnsRequestActionModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    blocked: Optional[bool] = Field(default=None, alias="Blocked")


class AdjustmentModel(BaseModel):
    metric: Optional[str] = Field(default=None, alias="Metric")
    reason: Optional[str] = Field(default=None, alias="Reason")


class AdminAccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    status: Optional[Literal["DISABLE_IN_PROGRESS", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class AssociatedStandardModel(BaseModel):
    standards_id: Optional[str] = Field(default=None, alias="StandardsId")


class AvailabilityZoneModel(BaseModel):
    zone_name: Optional[str] = Field(default=None, alias="ZoneName")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")


class AwsApiCallActionDomainDetailsModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")


class AwsApiGatewayAccessLogSettingsModel(BaseModel):
    format: Optional[str] = Field(default=None, alias="Format")
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")


class AwsApiGatewayCanarySettingsModel(BaseModel):
    percent_traffic: Optional[float] = Field(default=None, alias="PercentTraffic")
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    stage_variable_overrides: Optional[Mapping[str, str]] = Field(
        default=None, alias="StageVariableOverrides"
    )
    use_stage_cache: Optional[bool] = Field(default=None, alias="UseStageCache")


class AwsApiGatewayEndpointConfigurationModel(BaseModel):
    types: Optional[Sequence[str]] = Field(default=None, alias="Types")


class AwsApiGatewayMethodSettingsModel(BaseModel):
    metrics_enabled: Optional[bool] = Field(default=None, alias="MetricsEnabled")
    logging_level: Optional[str] = Field(default=None, alias="LoggingLevel")
    data_trace_enabled: Optional[bool] = Field(default=None, alias="DataTraceEnabled")
    throttling_burst_limit: Optional[int] = Field(
        default=None, alias="ThrottlingBurstLimit"
    )
    throttling_rate_limit: Optional[float] = Field(
        default=None, alias="ThrottlingRateLimit"
    )
    caching_enabled: Optional[bool] = Field(default=None, alias="CachingEnabled")
    cache_ttl_in_seconds: Optional[int] = Field(default=None, alias="CacheTtlInSeconds")
    cache_data_encrypted: Optional[bool] = Field(
        default=None, alias="CacheDataEncrypted"
    )
    require_authorization_for_cache_control: Optional[bool] = Field(
        default=None, alias="RequireAuthorizationForCacheControl"
    )
    unauthorized_cache_control_header_strategy: Optional[str] = Field(
        default=None, alias="UnauthorizedCacheControlHeaderStrategy"
    )
    http_method: Optional[str] = Field(default=None, alias="HttpMethod")
    resource_path: Optional[str] = Field(default=None, alias="ResourcePath")


class AwsCorsConfigurationModel(BaseModel):
    allow_origins: Optional[Sequence[str]] = Field(default=None, alias="AllowOrigins")
    allow_credentials: Optional[bool] = Field(default=None, alias="AllowCredentials")
    expose_headers: Optional[Sequence[str]] = Field(default=None, alias="ExposeHeaders")
    max_age: Optional[int] = Field(default=None, alias="MaxAge")
    allow_methods: Optional[Sequence[str]] = Field(default=None, alias="AllowMethods")
    allow_headers: Optional[Sequence[str]] = Field(default=None, alias="AllowHeaders")


class AwsApiGatewayV2RouteSettingsModel(BaseModel):
    detailed_metrics_enabled: Optional[bool] = Field(
        default=None, alias="DetailedMetricsEnabled"
    )
    logging_level: Optional[str] = Field(default=None, alias="LoggingLevel")
    data_trace_enabled: Optional[bool] = Field(default=None, alias="DataTraceEnabled")
    throttling_burst_limit: Optional[int] = Field(
        default=None, alias="ThrottlingBurstLimit"
    )
    throttling_rate_limit: Optional[float] = Field(
        default=None, alias="ThrottlingRateLimit"
    )


class AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")


class AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationModel(
    BaseModel
):
    launch_template_id: Optional[str] = Field(default=None, alias="LaunchTemplateId")
    launch_template_name: Optional[str] = Field(
        default=None, alias="LaunchTemplateName"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsModel(
    BaseModel
):
    on_demand_allocation_strategy: Optional[str] = Field(
        default=None, alias="OnDemandAllocationStrategy"
    )
    on_demand_base_capacity: Optional[int] = Field(
        default=None, alias="OnDemandBaseCapacity"
    )
    on_demand_percentage_above_base_capacity: Optional[int] = Field(
        default=None, alias="OnDemandPercentageAboveBaseCapacity"
    )
    spot_allocation_strategy: Optional[str] = Field(
        default=None, alias="SpotAllocationStrategy"
    )
    spot_instance_pools: Optional[int] = Field(default=None, alias="SpotInstancePools")
    spot_max_price: Optional[str] = Field(default=None, alias="SpotMaxPrice")


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationModel(
    BaseModel
):
    launch_template_id: Optional[str] = Field(default=None, alias="LaunchTemplateId")
    launch_template_name: Optional[str] = Field(
        default=None, alias="LaunchTemplateName"
    )
    version: Optional[str] = Field(default=None, alias="Version")


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsModel(
    BaseModel
):
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    weighted_capacity: Optional[str] = Field(default=None, alias="WeightedCapacity")


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsModel(BaseModel):
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="DeleteOnTermination"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    iops: Optional[int] = Field(default=None, alias="Iops")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    volume_size: Optional[int] = Field(default=None, alias="VolumeSize")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")


class AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsAutoScalingLaunchConfigurationMetadataOptionsModel(BaseModel):
    http_endpoint: Optional[str] = Field(default=None, alias="HttpEndpoint")
    http_put_response_hop_limit: Optional[int] = Field(
        default=None, alias="HttpPutResponseHopLimit"
    )
    http_tokens: Optional[str] = Field(default=None, alias="HttpTokens")


class AwsBackupBackupPlanAdvancedBackupSettingsDetailsModel(BaseModel):
    backup_options: Optional[Mapping[str, str]] = Field(
        default=None, alias="BackupOptions"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class AwsBackupBackupPlanLifecycleDetailsModel(BaseModel):
    delete_after_days: Optional[int] = Field(default=None, alias="DeleteAfterDays")
    move_to_cold_storage_after_days: Optional[int] = Field(
        default=None, alias="MoveToColdStorageAfterDays"
    )


class AwsBackupBackupVaultNotificationsDetailsModel(BaseModel):
    backup_vault_events: Optional[Sequence[str]] = Field(
        default=None, alias="BackupVaultEvents"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")


class AwsBackupRecoveryPointCalculatedLifecycleDetailsModel(BaseModel):
    delete_at: Optional[str] = Field(default=None, alias="DeleteAt")
    move_to_cold_storage_at: Optional[str] = Field(
        default=None, alias="MoveToColdStorageAt"
    )


class AwsBackupRecoveryPointCreatedByDetailsModel(BaseModel):
    backup_plan_arn: Optional[str] = Field(default=None, alias="BackupPlanArn")
    backup_plan_id: Optional[str] = Field(default=None, alias="BackupPlanId")
    backup_plan_version: Optional[str] = Field(default=None, alias="BackupPlanVersion")
    backup_rule_id: Optional[str] = Field(default=None, alias="BackupRuleId")


class AwsBackupRecoveryPointLifecycleDetailsModel(BaseModel):
    delete_after_days: Optional[int] = Field(default=None, alias="DeleteAfterDays")
    move_to_cold_storage_after_days: Optional[int] = Field(
        default=None, alias="MoveToColdStorageAfterDays"
    )


class AwsCertificateManagerCertificateExtendedKeyUsageModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    oid: Optional[str] = Field(default=None, alias="OId")


class AwsCertificateManagerCertificateKeyUsageModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class AwsCertificateManagerCertificateOptionsModel(BaseModel):
    certificate_transparency_logging_preference: Optional[str] = Field(
        default=None, alias="CertificateTransparencyLoggingPreference"
    )


class AwsCertificateManagerCertificateResourceRecordModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsCloudFormationStackDriftInformationDetailsModel(BaseModel):
    stack_drift_status: Optional[str] = Field(default=None, alias="StackDriftStatus")


class AwsCloudFormationStackOutputsDetailsModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    output_key: Optional[str] = Field(default=None, alias="OutputKey")
    output_value: Optional[str] = Field(default=None, alias="OutputValue")


class AwsCloudFrontDistributionCacheBehaviorModel(BaseModel):
    viewer_protocol_policy: Optional[str] = Field(
        default=None, alias="ViewerProtocolPolicy"
    )


class AwsCloudFrontDistributionDefaultCacheBehaviorModel(BaseModel):
    viewer_protocol_policy: Optional[str] = Field(
        default=None, alias="ViewerProtocolPolicy"
    )


class AwsCloudFrontDistributionLoggingModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    include_cookies: Optional[bool] = Field(default=None, alias="IncludeCookies")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class AwsCloudFrontDistributionViewerCertificateModel(BaseModel):
    acm_certificate_arn: Optional[str] = Field(default=None, alias="AcmCertificateArn")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    certificate_source: Optional[str] = Field(default=None, alias="CertificateSource")
    cloud_front_default_certificate: Optional[bool] = Field(
        default=None, alias="CloudFrontDefaultCertificate"
    )
    iam_certificate_id: Optional[str] = Field(default=None, alias="IamCertificateId")
    minimum_protocol_version: Optional[str] = Field(
        default=None, alias="MinimumProtocolVersion"
    )
    ssl_support_method: Optional[str] = Field(default=None, alias="SslSupportMethod")


class AwsCloudFrontDistributionOriginSslProtocolsModel(BaseModel):
    items: Optional[Sequence[str]] = Field(default=None, alias="Items")
    quantity: Optional[int] = Field(default=None, alias="Quantity")


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesModel(BaseModel):
    items: Optional[Sequence[int]] = Field(default=None, alias="Items")
    quantity: Optional[int] = Field(default=None, alias="Quantity")


class AwsCloudFrontDistributionOriginS3OriginConfigModel(BaseModel):
    origin_access_identity: Optional[str] = Field(
        default=None, alias="OriginAccessIdentity"
    )


class AwsCloudTrailTrailDetailsModel(BaseModel):
    cloud_watch_logs_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsLogGroupArn"
    )
    cloud_watch_logs_role_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsRoleArn"
    )
    has_custom_event_selectors: Optional[bool] = Field(
        default=None, alias="HasCustomEventSelectors"
    )
    home_region: Optional[str] = Field(default=None, alias="HomeRegion")
    include_global_service_events: Optional[bool] = Field(
        default=None, alias="IncludeGlobalServiceEvents"
    )
    is_multi_region_trail: Optional[bool] = Field(
        default=None, alias="IsMultiRegionTrail"
    )
    is_organization_trail: Optional[bool] = Field(
        default=None, alias="IsOrganizationTrail"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    log_file_validation_enabled: Optional[bool] = Field(
        default=None, alias="LogFileValidationEnabled"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    sns_topic_name: Optional[str] = Field(default=None, alias="SnsTopicName")
    trail_arn: Optional[str] = Field(default=None, alias="TrailArn")


class AwsCloudWatchAlarmDimensionsDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsCodeBuildProjectArtifactsDetailsModel(BaseModel):
    artifact_identifier: Optional[str] = Field(default=None, alias="ArtifactIdentifier")
    encryption_disabled: Optional[bool] = Field(
        default=None, alias="EncryptionDisabled"
    )
    location: Optional[str] = Field(default=None, alias="Location")
    name: Optional[str] = Field(default=None, alias="Name")
    namespace_type: Optional[str] = Field(default=None, alias="NamespaceType")
    override_artifact_name: Optional[bool] = Field(
        default=None, alias="OverrideArtifactName"
    )
    packaging: Optional[str] = Field(default=None, alias="Packaging")
    path: Optional[str] = Field(default=None, alias="Path")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsCodeBuildProjectSourceModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    location: Optional[str] = Field(default=None, alias="Location")
    git_clone_depth: Optional[int] = Field(default=None, alias="GitCloneDepth")
    insecure_ssl: Optional[bool] = Field(default=None, alias="InsecureSsl")


class AwsCodeBuildProjectVpcConfigModel(BaseModel):
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsCodeBuildProjectEnvironmentRegistryCredentialModel(BaseModel):
    credential: Optional[str] = Field(default=None, alias="Credential")
    credential_provider: Optional[str] = Field(default=None, alias="CredentialProvider")


class AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    status: Optional[str] = Field(default=None, alias="Status")
    stream_name: Optional[str] = Field(default=None, alias="StreamName")


class AwsCodeBuildProjectLogsConfigS3LogsDetailsModel(BaseModel):
    encryption_disabled: Optional[bool] = Field(
        default=None, alias="EncryptionDisabled"
    )
    location: Optional[str] = Field(default=None, alias="Location")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsDynamoDbTableAttributeDefinitionModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    attribute_type: Optional[str] = Field(default=None, alias="AttributeType")


class AwsDynamoDbTableBillingModeSummaryModel(BaseModel):
    billing_mode: Optional[str] = Field(default=None, alias="BillingMode")
    last_update_to_pay_per_request_date_time: Optional[str] = Field(
        default=None, alias="LastUpdateToPayPerRequestDateTime"
    )


class AwsDynamoDbTableKeySchemaModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    key_type: Optional[str] = Field(default=None, alias="KeyType")


class AwsDynamoDbTableProvisionedThroughputModel(BaseModel):
    last_decrease_date_time: Optional[str] = Field(
        default=None, alias="LastDecreaseDateTime"
    )
    last_increase_date_time: Optional[str] = Field(
        default=None, alias="LastIncreaseDateTime"
    )
    number_of_decreases_today: Optional[int] = Field(
        default=None, alias="NumberOfDecreasesToday"
    )
    read_capacity_units: Optional[int] = Field(default=None, alias="ReadCapacityUnits")
    write_capacity_units: Optional[int] = Field(
        default=None, alias="WriteCapacityUnits"
    )


class AwsDynamoDbTableRestoreSummaryModel(BaseModel):
    source_backup_arn: Optional[str] = Field(default=None, alias="SourceBackupArn")
    source_table_arn: Optional[str] = Field(default=None, alias="SourceTableArn")
    restore_date_time: Optional[str] = Field(default=None, alias="RestoreDateTime")
    restore_in_progress: Optional[bool] = Field(default=None, alias="RestoreInProgress")


class AwsDynamoDbTableSseDescriptionModel(BaseModel):
    inaccessible_encryption_date_time: Optional[str] = Field(
        default=None, alias="InaccessibleEncryptionDateTime"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    sse_type: Optional[str] = Field(default=None, alias="SseType")
    kms_master_key_arn: Optional[str] = Field(default=None, alias="KmsMasterKeyArn")


class AwsDynamoDbTableStreamSpecificationModel(BaseModel):
    stream_enabled: Optional[bool] = Field(default=None, alias="StreamEnabled")
    stream_view_type: Optional[str] = Field(default=None, alias="StreamViewType")


class AwsDynamoDbTableProjectionModel(BaseModel):
    non_key_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="NonKeyAttributes"
    )
    projection_type: Optional[str] = Field(default=None, alias="ProjectionType")


class AwsDynamoDbTableProvisionedThroughputOverrideModel(BaseModel):
    read_capacity_units: Optional[int] = Field(default=None, alias="ReadCapacityUnits")


class AwsEc2EipDetailsModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    public_ip: Optional[str] = Field(default=None, alias="PublicIp")
    allocation_id: Optional[str] = Field(default=None, alias="AllocationId")
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    domain: Optional[str] = Field(default=None, alias="Domain")
    public_ipv4_pool: Optional[str] = Field(default=None, alias="PublicIpv4Pool")
    network_border_group: Optional[str] = Field(
        default=None, alias="NetworkBorderGroup"
    )
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    network_interface_owner_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceOwnerId"
    )
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")


class AwsEc2InstanceMetadataOptionsModel(BaseModel):
    http_endpoint: Optional[str] = Field(default=None, alias="HttpEndpoint")
    http_protocol_ipv6: Optional[str] = Field(default=None, alias="HttpProtocolIpv6")
    http_put_response_hop_limit: Optional[int] = Field(
        default=None, alias="HttpPutResponseHopLimit"
    )
    http_tokens: Optional[str] = Field(default=None, alias="HttpTokens")
    instance_metadata_tags: Optional[str] = Field(
        default=None, alias="InstanceMetadataTags"
    )


class AwsEc2InstanceNetworkInterfacesDetailsModel(BaseModel):
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsModel(BaseModel):
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="DeleteOnTermination"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    iops: Optional[int] = Field(default=None, alias="Iops")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    throughput: Optional[int] = Field(default=None, alias="Throughput")
    volume_size: Optional[int] = Field(default=None, alias="VolumeSize")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsModel(
    BaseModel
):
    capacity_reservation_id: Optional[str] = Field(
        default=None, alias="CapacityReservationId"
    )
    capacity_reservation_resource_group_arn: Optional[str] = Field(
        default=None, alias="CapacityReservationResourceGroupArn"
    )


class AwsEc2LaunchTemplateDataCpuOptionsDetailsModel(BaseModel):
    core_count: Optional[int] = Field(default=None, alias="CoreCount")
    threads_per_core: Optional[int] = Field(default=None, alias="ThreadsPerCore")


class AwsEc2LaunchTemplateDataCreditSpecificationDetailsModel(BaseModel):
    cpu_credits: Optional[str] = Field(default=None, alias="CpuCredits")


class AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEc2LaunchTemplateDataEnclaveOptionsDetailsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsEc2LaunchTemplateDataHibernationOptionsDetailsModel(BaseModel):
    configured: Optional[bool] = Field(default=None, alias="Configured")


class AwsEc2LaunchTemplateDataIamInstanceProfileDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class AwsEc2LaunchTemplateDataLicenseSetDetailsModel(BaseModel):
    license_configuration_arn: Optional[str] = Field(
        default=None, alias="LicenseConfigurationArn"
    )


class AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsModel(BaseModel):
    auto_recovery: Optional[str] = Field(default=None, alias="AutoRecovery")


class AwsEc2LaunchTemplateDataMetadataOptionsDetailsModel(BaseModel):
    http_endpoint: Optional[str] = Field(default=None, alias="HttpEndpoint")
    http_protocol_ipv6: Optional[str] = Field(default=None, alias="HttpProtocolIpv6")
    http_tokens: Optional[str] = Field(default=None, alias="HttpTokens")
    http_put_response_hop_limit: Optional[int] = Field(
        default=None, alias="HttpPutResponseHopLimit"
    )
    instance_metadata_tags: Optional[str] = Field(
        default=None, alias="InstanceMetadataTags"
    )


class AwsEc2LaunchTemplateDataMonitoringDetailsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsEc2LaunchTemplateDataPlacementDetailsModel(BaseModel):
    affinity: Optional[str] = Field(default=None, alias="Affinity")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    host_id: Optional[str] = Field(default=None, alias="HostId")
    host_resource_group_arn: Optional[str] = Field(
        default=None, alias="HostResourceGroupArn"
    )
    partition_number: Optional[int] = Field(default=None, alias="PartitionNumber")
    spread_domain: Optional[str] = Field(default=None, alias="SpreadDomain")
    tenancy: Optional[str] = Field(default=None, alias="Tenancy")


class AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsModel(BaseModel):
    enable_resource_name_dns_aaaarecord: Optional[bool] = Field(
        default=None, alias="EnableResourceNameDnsAAAARecord"
    )
    enable_resource_name_dns_arecord: Optional[bool] = Field(
        default=None, alias="EnableResourceNameDnsARecord"
    )
    hostname_type: Optional[str] = Field(default=None, alias="HostnameType")


class AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsModel(BaseModel):
    block_duration_minutes: Optional[int] = Field(
        default=None, alias="BlockDurationMinutes"
    )
    instance_interruption_behavior: Optional[str] = Field(
        default=None, alias="InstanceInterruptionBehavior"
    )
    max_price: Optional[str] = Field(default=None, alias="MaxPrice")
    spot_instance_type: Optional[str] = Field(default=None, alias="SpotInstanceType")
    valid_until: Optional[str] = Field(default=None, alias="ValidUntil")


class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsModel(
    BaseModel
):
    max: Optional[int] = Field(default=None, alias="Max")
    min: Optional[int] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsModel(
    BaseModel
):
    max: Optional[int] = Field(default=None, alias="Max")
    min: Optional[int] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsModel(
    BaseModel
):
    max: Optional[int] = Field(default=None, alias="Max")
    min: Optional[int] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsModel(
    BaseModel
):
    max: Optional[float] = Field(default=None, alias="Max")
    min: Optional[float] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsModel(BaseModel):
    max: Optional[int] = Field(default=None, alias="Max")
    min: Optional[int] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsModel(
    BaseModel
):
    max: Optional[int] = Field(default=None, alias="Max")
    min: Optional[int] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsModel(
    BaseModel
):
    max: Optional[float] = Field(default=None, alias="Max")
    min: Optional[float] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsModel(BaseModel):
    max: Optional[int] = Field(default=None, alias="Max")
    min: Optional[int] = Field(default=None, alias="Min")


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsModel(BaseModel):
    ipv4_prefix: Optional[str] = Field(default=None, alias="Ipv4Prefix")


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsModel(BaseModel):
    ipv6_address: Optional[str] = Field(default=None, alias="Ipv6Address")


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsModel(BaseModel):
    ipv6_prefix: Optional[str] = Field(default=None, alias="Ipv6Prefix")


class AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsModel(
    BaseModel
):
    primary: Optional[bool] = Field(default=None, alias="Primary")
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")


class AwsEc2NetworkAclAssociationModel(BaseModel):
    network_acl_association_id: Optional[str] = Field(
        default=None, alias="NetworkAclAssociationId"
    )
    network_acl_id: Optional[str] = Field(default=None, alias="NetworkAclId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")


class IcmpTypeCodeModel(BaseModel):
    code: Optional[int] = Field(default=None, alias="Code")
    type: Optional[int] = Field(default=None, alias="Type")


class PortRangeFromToModel(BaseModel):
    from_: Optional[int] = Field(default=None, alias="From")
    to: Optional[int] = Field(default=None, alias="To")


class AwsEc2NetworkInterfaceAttachmentModel(BaseModel):
    attach_time: Optional[str] = Field(default=None, alias="AttachTime")
    attachment_id: Optional[str] = Field(default=None, alias="AttachmentId")
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="DeleteOnTermination"
    )
    device_index: Optional[int] = Field(default=None, alias="DeviceIndex")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    instance_owner_id: Optional[str] = Field(default=None, alias="InstanceOwnerId")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsEc2NetworkInterfaceIpV6AddressDetailModel(BaseModel):
    ip_v6_address: Optional[str] = Field(default=None, alias="IpV6Address")


class AwsEc2NetworkInterfacePrivateIpAddressDetailModel(BaseModel):
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")
    private_dns_name: Optional[str] = Field(default=None, alias="PrivateDnsName")


class AwsEc2NetworkInterfaceSecurityGroupModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_id: Optional[str] = Field(default=None, alias="GroupId")


class AwsEc2SecurityGroupIpRangeModel(BaseModel):
    cidr_ip: Optional[str] = Field(default=None, alias="CidrIp")


class AwsEc2SecurityGroupIpv6RangeModel(BaseModel):
    cidr_ipv6: Optional[str] = Field(default=None, alias="CidrIpv6")


class AwsEc2SecurityGroupPrefixListIdModel(BaseModel):
    prefix_list_id: Optional[str] = Field(default=None, alias="PrefixListId")


class AwsEc2SecurityGroupUserIdGroupPairModel(BaseModel):
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    peering_status: Optional[str] = Field(default=None, alias="PeeringStatus")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    vpc_peering_connection_id: Optional[str] = Field(
        default=None, alias="VpcPeeringConnectionId"
    )


class Ipv6CidrBlockAssociationModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    ipv6_cidr_block: Optional[str] = Field(default=None, alias="Ipv6CidrBlock")
    cidr_block_state: Optional[str] = Field(default=None, alias="CidrBlockState")


class AwsEc2TransitGatewayDetailsModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    description: Optional[str] = Field(default=None, alias="Description")
    default_route_table_propagation: Optional[str] = Field(
        default=None, alias="DefaultRouteTablePropagation"
    )
    auto_accept_shared_attachments: Optional[str] = Field(
        default=None, alias="AutoAcceptSharedAttachments"
    )
    default_route_table_association: Optional[str] = Field(
        default=None, alias="DefaultRouteTableAssociation"
    )
    transit_gateway_cidr_blocks: Optional[Sequence[str]] = Field(
        default=None, alias="TransitGatewayCidrBlocks"
    )
    association_default_route_table_id: Optional[str] = Field(
        default=None, alias="AssociationDefaultRouteTableId"
    )
    propagation_default_route_table_id: Optional[str] = Field(
        default=None, alias="PropagationDefaultRouteTableId"
    )
    vpn_ecmp_support: Optional[str] = Field(default=None, alias="VpnEcmpSupport")
    dns_support: Optional[str] = Field(default=None, alias="DnsSupport")
    multicast_support: Optional[str] = Field(default=None, alias="MulticastSupport")
    amazon_side_asn: Optional[int] = Field(default=None, alias="AmazonSideAsn")


class AwsEc2VolumeAttachmentModel(BaseModel):
    attach_time: Optional[str] = Field(default=None, alias="AttachTime")
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="DeleteOnTermination"
    )
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    status: Optional[str] = Field(default=None, alias="Status")


class CidrBlockAssociationModel(BaseModel):
    association_id: Optional[str] = Field(default=None, alias="AssociationId")
    cidr_block: Optional[str] = Field(default=None, alias="CidrBlock")
    cidr_block_state: Optional[str] = Field(default=None, alias="CidrBlockState")


class AwsEc2VpcEndpointServiceServiceTypeDetailsModel(BaseModel):
    service_type: Optional[str] = Field(default=None, alias="ServiceType")


class AwsEc2VpcPeeringConnectionStatusDetailsModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class VpcInfoCidrBlockSetDetailsModel(BaseModel):
    cidr_block: Optional[str] = Field(default=None, alias="CidrBlock")


class VpcInfoIpv6CidrBlockSetDetailsModel(BaseModel):
    ipv6_cidr_block: Optional[str] = Field(default=None, alias="Ipv6CidrBlock")


class VpcInfoPeeringOptionsDetailsModel(BaseModel):
    allow_dns_resolution_from_remote_vpc: Optional[bool] = Field(
        default=None, alias="AllowDnsResolutionFromRemoteVpc"
    )
    allow_egress_from_local_classic_link_to_remote_vpc: Optional[bool] = Field(
        default=None, alias="AllowEgressFromLocalClassicLinkToRemoteVpc"
    )
    allow_egress_from_local_vpc_to_remote_classic_link: Optional[bool] = Field(
        default=None, alias="AllowEgressFromLocalVpcToRemoteClassicLink"
    )


class AwsEc2VpnConnectionRoutesDetailsModel(BaseModel):
    destination_cidr_block: Optional[str] = Field(
        default=None, alias="DestinationCidrBlock"
    )
    state: Optional[str] = Field(default=None, alias="State")


class AwsEc2VpnConnectionVgwTelemetryDetailsModel(BaseModel):
    accepted_route_count: Optional[int] = Field(
        default=None, alias="AcceptedRouteCount"
    )
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    last_status_change: Optional[str] = Field(default=None, alias="LastStatusChange")
    outside_ip_address: Optional[str] = Field(default=None, alias="OutsideIpAddress")
    status: Optional[str] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsModel(BaseModel):
    dpd_timeout_seconds: Optional[int] = Field(default=None, alias="DpdTimeoutSeconds")
    ike_versions: Optional[Sequence[str]] = Field(default=None, alias="IkeVersions")
    outside_ip_address: Optional[str] = Field(default=None, alias="OutsideIpAddress")
    phase1_dh_group_numbers: Optional[Sequence[int]] = Field(
        default=None, alias="Phase1DhGroupNumbers"
    )
    phase1_encryption_algorithms: Optional[Sequence[str]] = Field(
        default=None, alias="Phase1EncryptionAlgorithms"
    )
    phase1_integrity_algorithms: Optional[Sequence[str]] = Field(
        default=None, alias="Phase1IntegrityAlgorithms"
    )
    phase1_lifetime_seconds: Optional[int] = Field(
        default=None, alias="Phase1LifetimeSeconds"
    )
    phase2_dh_group_numbers: Optional[Sequence[int]] = Field(
        default=None, alias="Phase2DhGroupNumbers"
    )
    phase2_encryption_algorithms: Optional[Sequence[str]] = Field(
        default=None, alias="Phase2EncryptionAlgorithms"
    )
    phase2_integrity_algorithms: Optional[Sequence[str]] = Field(
        default=None, alias="Phase2IntegrityAlgorithms"
    )
    phase2_lifetime_seconds: Optional[int] = Field(
        default=None, alias="Phase2LifetimeSeconds"
    )
    pre_shared_key: Optional[str] = Field(default=None, alias="PreSharedKey")
    rekey_fuzz_percentage: Optional[int] = Field(
        default=None, alias="RekeyFuzzPercentage"
    )
    rekey_margin_time_seconds: Optional[int] = Field(
        default=None, alias="RekeyMarginTimeSeconds"
    )
    replay_window_size: Optional[int] = Field(default=None, alias="ReplayWindowSize")
    tunnel_inside_cidr: Optional[str] = Field(default=None, alias="TunnelInsideCidr")


class AwsEcrContainerImageDetailsModel(BaseModel):
    registry_id: Optional[str] = Field(default=None, alias="RegistryId")
    repository_name: Optional[str] = Field(default=None, alias="RepositoryName")
    architecture: Optional[str] = Field(default=None, alias="Architecture")
    image_digest: Optional[str] = Field(default=None, alias="ImageDigest")
    image_tags: Optional[Sequence[str]] = Field(default=None, alias="ImageTags")
    image_published_at: Optional[str] = Field(default=None, alias="ImagePublishedAt")


class AwsEcrRepositoryImageScanningConfigurationDetailsModel(BaseModel):
    scan_on_push: Optional[bool] = Field(default=None, alias="ScanOnPush")


class AwsEcrRepositoryLifecyclePolicyDetailsModel(BaseModel):
    lifecycle_policy_text: Optional[str] = Field(
        default=None, alias="LifecyclePolicyText"
    )
    registry_id: Optional[str] = Field(default=None, alias="RegistryId")


class AwsEcsClusterClusterSettingsDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsModel(
    BaseModel
):
    cloud_watch_encryption_enabled: Optional[bool] = Field(
        default=None, alias="CloudWatchEncryptionEnabled"
    )
    cloud_watch_log_group_name: Optional[str] = Field(
        default=None, alias="CloudWatchLogGroupName"
    )
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_encryption_enabled: Optional[bool] = Field(
        default=None, alias="S3EncryptionEnabled"
    )
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")


class AwsEcsClusterDefaultCapacityProviderStrategyDetailsModel(BaseModel):
    base: Optional[int] = Field(default=None, alias="Base")
    capacity_provider: Optional[str] = Field(default=None, alias="CapacityProvider")
    weight: Optional[int] = Field(default=None, alias="Weight")


class AwsMountPointModel(BaseModel):
    source_volume: Optional[str] = Field(default=None, alias="SourceVolume")
    container_path: Optional[str] = Field(default=None, alias="ContainerPath")


class AwsEcsServiceCapacityProviderStrategyDetailsModel(BaseModel):
    base: Optional[int] = Field(default=None, alias="Base")
    capacity_provider: Optional[str] = Field(default=None, alias="CapacityProvider")
    weight: Optional[int] = Field(default=None, alias="Weight")


class AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsModel(
    BaseModel
):
    enable: Optional[bool] = Field(default=None, alias="Enable")
    rollback: Optional[bool] = Field(default=None, alias="Rollback")


class AwsEcsServiceDeploymentControllerDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEcsServiceLoadBalancersDetailsModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="ContainerName")
    container_port: Optional[int] = Field(default=None, alias="ContainerPort")
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    target_group_arn: Optional[str] = Field(default=None, alias="TargetGroupArn")


class AwsEcsServicePlacementConstraintsDetailsModel(BaseModel):
    expression: Optional[str] = Field(default=None, alias="Expression")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEcsServicePlacementStrategiesDetailsModel(BaseModel):
    field: Optional[str] = Field(default=None, alias="Field")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEcsServiceServiceRegistriesDetailsModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="ContainerName")
    container_port: Optional[int] = Field(default=None, alias="ContainerPort")
    port: Optional[int] = Field(default=None, alias="Port")
    registry_arn: Optional[str] = Field(default=None, alias="RegistryArn")


class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsModel(BaseModel):
    assign_public_ip: Optional[str] = Field(default=None, alias="AssignPublicIp")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")


class AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsModel(BaseModel):
    condition: Optional[str] = Field(default=None, alias="Condition")
    container_name: Optional[str] = Field(default=None, alias="ContainerName")


class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsModel(BaseModel):
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")


class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsModel(
    BaseModel
):
    options: Optional[Mapping[str, str]] = Field(default=None, alias="Options")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsModel(BaseModel):
    command: Optional[Sequence[str]] = Field(default=None, alias="Command")
    interval: Optional[int] = Field(default=None, alias="Interval")
    retries: Optional[int] = Field(default=None, alias="Retries")
    start_period: Optional[int] = Field(default=None, alias="StartPeriod")
    timeout: Optional[int] = Field(default=None, alias="Timeout")


class AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsModel(BaseModel):
    container_path: Optional[str] = Field(default=None, alias="ContainerPath")
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    source_volume: Optional[str] = Field(default=None, alias="SourceVolume")


class AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsModel(BaseModel):
    container_port: Optional[int] = Field(default=None, alias="ContainerPort")
    host_port: Optional[int] = Field(default=None, alias="HostPort")
    protocol: Optional[str] = Field(default=None, alias="Protocol")


class AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsModel(
    BaseModel
):
    credentials_parameter: Optional[str] = Field(
        default=None, alias="CredentialsParameter"
    )


class AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsModel(
    BaseModel
):
    type: Optional[str] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value_from: Optional[str] = Field(default=None, alias="ValueFrom")


class AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsModel(BaseModel):
    hard_limit: Optional[int] = Field(default=None, alias="HardLimit")
    name: Optional[str] = Field(default=None, alias="Name")
    soft_limit: Optional[int] = Field(default=None, alias="SoftLimit")


class AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsModel(BaseModel):
    read_only: Optional[bool] = Field(default=None, alias="ReadOnly")
    source_container: Optional[str] = Field(default=None, alias="SourceContainer")


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsModel(
    BaseModel
):
    add: Optional[Sequence[str]] = Field(default=None, alias="Add")
    drop: Optional[Sequence[str]] = Field(default=None, alias="Drop")


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsModel(
    BaseModel
):
    container_path: Optional[str] = Field(default=None, alias="ContainerPath")
    host_path: Optional[str] = Field(default=None, alias="HostPath")
    permissions: Optional[Sequence[str]] = Field(default=None, alias="Permissions")


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsModel(
    BaseModel
):
    container_path: Optional[str] = Field(default=None, alias="ContainerPath")
    mount_options: Optional[Sequence[str]] = Field(default=None, alias="MountOptions")
    size: Optional[int] = Field(default=None, alias="Size")


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsModel(
    BaseModel
):
    name: Optional[str] = Field(default=None, alias="Name")
    value_from: Optional[str] = Field(default=None, alias="ValueFrom")


class AwsEcsTaskDefinitionInferenceAcceleratorsDetailsModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    device_type: Optional[str] = Field(default=None, alias="DeviceType")


class AwsEcsTaskDefinitionPlacementConstraintsDetailsModel(BaseModel):
    expression: Optional[str] = Field(default=None, alias="Expression")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsModel(
    BaseModel
):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsModel(BaseModel):
    autoprovision: Optional[bool] = Field(default=None, alias="Autoprovision")
    driver: Optional[str] = Field(default=None, alias="Driver")
    driver_opts: Optional[Mapping[str, str]] = Field(default=None, alias="DriverOpts")
    labels: Optional[Mapping[str, str]] = Field(default=None, alias="Labels")
    scope: Optional[str] = Field(default=None, alias="Scope")


class AwsEcsTaskDefinitionVolumesHostDetailsModel(BaseModel):
    source_path: Optional[str] = Field(default=None, alias="SourcePath")


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsModel(
    BaseModel
):
    access_point_id: Optional[str] = Field(default=None, alias="AccessPointId")
    iam: Optional[str] = Field(default=None, alias="Iam")


class AwsEcsTaskVolumeHostDetailsModel(BaseModel):
    source_path: Optional[str] = Field(default=None, alias="SourcePath")


class AwsEfsAccessPointPosixUserDetailsModel(BaseModel):
    gid: Optional[str] = Field(default=None, alias="Gid")
    secondary_gids: Optional[Sequence[str]] = Field(default=None, alias="SecondaryGids")
    uid: Optional[str] = Field(default=None, alias="Uid")


class AwsEfsAccessPointRootDirectoryCreationInfoDetailsModel(BaseModel):
    owner_gid: Optional[str] = Field(default=None, alias="OwnerGid")
    owner_uid: Optional[str] = Field(default=None, alias="OwnerUid")
    permissions: Optional[str] = Field(default=None, alias="Permissions")


class AwsEksClusterResourcesVpcConfigDetailsModel(BaseModel):
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")


class AwsEksClusterLoggingClusterLoggingDetailsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    types: Optional[Sequence[str]] = Field(default=None, alias="Types")


class AwsElasticBeanstalkEnvironmentEnvironmentLinkModel(BaseModel):
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    link_name: Optional[str] = Field(default=None, alias="LinkName")


class AwsElasticBeanstalkEnvironmentOptionSettingModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    option_name: Optional[str] = Field(default=None, alias="OptionName")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsElasticBeanstalkEnvironmentTierModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    version: Optional[str] = Field(default=None, alias="Version")


class AwsElasticsearchDomainDomainEndpointOptionsModel(BaseModel):
    enforce_http_s: Optional[bool] = Field(default=None, alias="EnforceHTTPS")
    tl_s_security_policy: Optional[str] = Field(default=None, alias="TLSSecurityPolicy")


class AwsElasticsearchDomainEncryptionAtRestOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class AwsElasticsearchDomainNodeToNodeEncryptionOptionsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsElasticsearchDomainServiceSoftwareOptionsModel(BaseModel):
    automated_update_date: Optional[str] = Field(
        default=None, alias="AutomatedUpdateDate"
    )
    cancellable: Optional[bool] = Field(default=None, alias="Cancellable")
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    new_version: Optional[str] = Field(default=None, alias="NewVersion")
    update_available: Optional[bool] = Field(default=None, alias="UpdateAvailable")
    update_status: Optional[str] = Field(default=None, alias="UpdateStatus")


class AwsElasticsearchDomainVPCOptionsModel(BaseModel):
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    vp_cid: Optional[str] = Field(default=None, alias="VPCId")


class AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsModel(
    BaseModel
):
    availability_zone_count: Optional[int] = Field(
        default=None, alias="AvailabilityZoneCount"
    )


class AwsElasticsearchDomainLogPublishingOptionsLogConfigModel(BaseModel):
    cloud_watch_logs_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsLogGroupArn"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsElbAppCookieStickinessPolicyModel(BaseModel):
    cookie_name: Optional[str] = Field(default=None, alias="CookieName")
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")


class AwsElbLbCookieStickinessPolicyModel(BaseModel):
    cookie_expiration_period: Optional[int] = Field(
        default=None, alias="CookieExpirationPeriod"
    )
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")


class AwsElbLoadBalancerAccessLogModel(BaseModel):
    emit_interval: Optional[int] = Field(default=None, alias="EmitInterval")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_bucket_prefix: Optional[str] = Field(default=None, alias="S3BucketPrefix")


class AwsElbLoadBalancerAdditionalAttributeModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsElbLoadBalancerConnectionDrainingModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    timeout: Optional[int] = Field(default=None, alias="Timeout")


class AwsElbLoadBalancerConnectionSettingsModel(BaseModel):
    idle_timeout: Optional[int] = Field(default=None, alias="IdleTimeout")


class AwsElbLoadBalancerCrossZoneLoadBalancingModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsElbLoadBalancerBackendServerDescriptionModel(BaseModel):
    instance_port: Optional[int] = Field(default=None, alias="InstancePort")
    policy_names: Optional[Sequence[str]] = Field(default=None, alias="PolicyNames")


class AwsElbLoadBalancerHealthCheckModel(BaseModel):
    healthy_threshold: Optional[int] = Field(default=None, alias="HealthyThreshold")
    interval: Optional[int] = Field(default=None, alias="Interval")
    target: Optional[str] = Field(default=None, alias="Target")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    unhealthy_threshold: Optional[int] = Field(default=None, alias="UnhealthyThreshold")


class AwsElbLoadBalancerInstanceModel(BaseModel):
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")


class AwsElbLoadBalancerSourceSecurityGroupModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    owner_alias: Optional[str] = Field(default=None, alias="OwnerAlias")


class AwsElbLoadBalancerListenerModel(BaseModel):
    instance_port: Optional[int] = Field(default=None, alias="InstancePort")
    instance_protocol: Optional[str] = Field(default=None, alias="InstanceProtocol")
    load_balancer_port: Optional[int] = Field(default=None, alias="LoadBalancerPort")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    ssl_certificate_id: Optional[str] = Field(default=None, alias="SslCertificateId")


class AwsElbv2LoadBalancerAttributeModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class LoadBalancerStateModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    reason: Optional[str] = Field(default=None, alias="Reason")


class AwsIamAccessKeySessionContextAttributesModel(BaseModel):
    mfa_authenticated: Optional[bool] = Field(default=None, alias="MfaAuthenticated")
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")


class AwsIamAccessKeySessionContextSessionIssuerModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class AwsIamAttachedManagedPolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")


class AwsIamGroupPolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")


class AwsIamInstanceProfileRoleModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    assume_role_policy_document: Optional[str] = Field(
        default=None, alias="AssumeRolePolicyDocument"
    )
    create_date: Optional[str] = Field(default=None, alias="CreateDate")
    path: Optional[str] = Field(default=None, alias="Path")
    role_id: Optional[str] = Field(default=None, alias="RoleId")
    role_name: Optional[str] = Field(default=None, alias="RoleName")


class AwsIamPermissionsBoundaryModel(BaseModel):
    permissions_boundary_arn: Optional[str] = Field(
        default=None, alias="PermissionsBoundaryArn"
    )
    permissions_boundary_type: Optional[str] = Field(
        default=None, alias="PermissionsBoundaryType"
    )


class AwsIamPolicyVersionModel(BaseModel):
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    is_default_version: Optional[bool] = Field(default=None, alias="IsDefaultVersion")
    create_date: Optional[str] = Field(default=None, alias="CreateDate")


class AwsIamRolePolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")


class AwsIamUserPolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")


class AwsKinesisStreamStreamEncryptionDetailsModel(BaseModel):
    encryption_type: Optional[str] = Field(default=None, alias="EncryptionType")
    key_id: Optional[str] = Field(default=None, alias="KeyId")


class AwsKmsKeyDetailsModel(BaseModel):
    aws_account_id: Optional[str] = Field(default=None, alias="AWSAccountId")
    creation_date: Optional[float] = Field(default=None, alias="CreationDate")
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    key_manager: Optional[str] = Field(default=None, alias="KeyManager")
    key_state: Optional[str] = Field(default=None, alias="KeyState")
    origin: Optional[str] = Field(default=None, alias="Origin")
    description: Optional[str] = Field(default=None, alias="Description")
    key_rotation_status: Optional[bool] = Field(default=None, alias="KeyRotationStatus")


class AwsLambdaFunctionCodeModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key: Optional[str] = Field(default=None, alias="S3Key")
    s3_object_version: Optional[str] = Field(default=None, alias="S3ObjectVersion")
    zip_file: Optional[str] = Field(default=None, alias="ZipFile")


class AwsLambdaFunctionDeadLetterConfigModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="TargetArn")


class AwsLambdaFunctionLayerModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    code_size: Optional[int] = Field(default=None, alias="CodeSize")


class AwsLambdaFunctionTracingConfigModel(BaseModel):
    mode: Optional[str] = Field(default=None, alias="Mode")


class AwsLambdaFunctionVpcConfigModel(BaseModel):
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class AwsLambdaFunctionEnvironmentErrorModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    message: Optional[str] = Field(default=None, alias="Message")


class AwsLambdaLayerVersionDetailsModel(BaseModel):
    version: Optional[int] = Field(default=None, alias="Version")
    compatible_runtimes: Optional[Sequence[str]] = Field(
        default=None, alias="CompatibleRuntimes"
    )
    created_date: Optional[str] = Field(default=None, alias="CreatedDate")


class AwsNetworkFirewallFirewallSubnetMappingsDetailsModel(BaseModel):
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")


class AwsOpenSearchServiceDomainMasterUserOptionsDetailsModel(BaseModel):
    master_user_arn: Optional[str] = Field(default=None, alias="MasterUserArn")
    master_user_name: Optional[str] = Field(default=None, alias="MasterUserName")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )


class AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsModel(BaseModel):
    availability_zone_count: Optional[int] = Field(
        default=None, alias="AvailabilityZoneCount"
    )


class AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsModel(BaseModel):
    custom_endpoint_certificate_arn: Optional[str] = Field(
        default=None, alias="CustomEndpointCertificateArn"
    )
    custom_endpoint_enabled: Optional[bool] = Field(
        default=None, alias="CustomEndpointEnabled"
    )
    enforce_http_s: Optional[bool] = Field(default=None, alias="EnforceHTTPS")
    custom_endpoint: Optional[str] = Field(default=None, alias="CustomEndpoint")
    tl_s_security_policy: Optional[str] = Field(default=None, alias="TLSSecurityPolicy")


class AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsModel(BaseModel):
    automated_update_date: Optional[str] = Field(
        default=None, alias="AutomatedUpdateDate"
    )
    cancellable: Optional[bool] = Field(default=None, alias="Cancellable")
    current_version: Optional[str] = Field(default=None, alias="CurrentVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    new_version: Optional[str] = Field(default=None, alias="NewVersion")
    update_available: Optional[bool] = Field(default=None, alias="UpdateAvailable")
    update_status: Optional[str] = Field(default=None, alias="UpdateStatus")
    optional_deployment: Optional[bool] = Field(
        default=None, alias="OptionalDeployment"
    )


class AwsOpenSearchServiceDomainVpcOptionsDetailsModel(BaseModel):
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")


class AwsOpenSearchServiceDomainLogPublishingOptionModel(BaseModel):
    cloud_watch_logs_log_group_arn: Optional[str] = Field(
        default=None, alias="CloudWatchLogsLogGroupArn"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class AwsRdsDbClusterAssociatedRoleModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRdsDbClusterMemberModel(BaseModel):
    is_cluster_writer: Optional[bool] = Field(default=None, alias="IsClusterWriter")
    promotion_tier: Optional[int] = Field(default=None, alias="PromotionTier")
    db_instance_identifier: Optional[str] = Field(
        default=None, alias="DbInstanceIdentifier"
    )
    db_cluster_parameter_group_status: Optional[str] = Field(
        default=None, alias="DbClusterParameterGroupStatus"
    )


class AwsRdsDbClusterOptionGroupMembershipModel(BaseModel):
    db_cluster_option_group_name: Optional[str] = Field(
        default=None, alias="DbClusterOptionGroupName"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRdsDbDomainMembershipModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    status: Optional[str] = Field(default=None, alias="Status")
    fqdn: Optional[str] = Field(default=None, alias="Fqdn")
    iam_role_name: Optional[str] = Field(default=None, alias="IamRoleName")


class AwsRdsDbInstanceVpcSecurityGroupModel(BaseModel):
    vpc_security_group_id: Optional[str] = Field(
        default=None, alias="VpcSecurityGroupId"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRdsDbClusterSnapshotDetailsModel(BaseModel):
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    snapshot_create_time: Optional[str] = Field(
        default=None, alias="SnapshotCreateTime"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    status: Optional[str] = Field(default=None, alias="Status")
    port: Optional[int] = Field(default=None, alias="Port")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    cluster_create_time: Optional[str] = Field(default=None, alias="ClusterCreateTime")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    percent_progress: Optional[int] = Field(default=None, alias="PercentProgress")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    db_cluster_identifier: Optional[str] = Field(
        default=None, alias="DbClusterIdentifier"
    )
    db_cluster_snapshot_identifier: Optional[str] = Field(
        default=None, alias="DbClusterSnapshotIdentifier"
    )
    iam_database_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IamDatabaseAuthenticationEnabled"
    )


class AwsRdsDbInstanceAssociatedRoleModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRdsDbInstanceEndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")


class AwsRdsDbOptionGroupMembershipModel(BaseModel):
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRdsDbParameterGroupModel(BaseModel):
    db_parameter_group_name: Optional[str] = Field(
        default=None, alias="DbParameterGroupName"
    )
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )


class AwsRdsDbProcessorFeatureModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsRdsDbStatusInfoModel(BaseModel):
    status_type: Optional[str] = Field(default=None, alias="StatusType")
    normal: Optional[bool] = Field(default=None, alias="Normal")
    status: Optional[str] = Field(default=None, alias="Status")
    message: Optional[str] = Field(default=None, alias="Message")


class AwsRdsPendingCloudWatchLogsExportsModel(BaseModel):
    log_types_to_enable: Optional[Sequence[str]] = Field(
        default=None, alias="LogTypesToEnable"
    )
    log_types_to_disable: Optional[Sequence[str]] = Field(
        default=None, alias="LogTypesToDisable"
    )


class AwsRdsDbSecurityGroupEc2SecurityGroupModel(BaseModel):
    ec2_security_group_id: Optional[str] = Field(
        default=None, alias="Ec2SecurityGroupId"
    )
    ec2_security_group_name: Optional[str] = Field(
        default=None, alias="Ec2SecurityGroupName"
    )
    ec2_security_group_owner_id: Optional[str] = Field(
        default=None, alias="Ec2SecurityGroupOwnerId"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRdsDbSecurityGroupIpRangeModel(BaseModel):
    cidr_ip: Optional[str] = Field(default=None, alias="CidrIp")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRdsDbSubnetGroupSubnetAvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class AwsRdsEventSubscriptionDetailsModel(BaseModel):
    cust_subscription_id: Optional[str] = Field(
        default=None, alias="CustSubscriptionId"
    )
    customer_aws_id: Optional[str] = Field(default=None, alias="CustomerAwsId")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    event_categories_list: Optional[Sequence[str]] = Field(
        default=None, alias="EventCategoriesList"
    )
    event_subscription_arn: Optional[str] = Field(
        default=None, alias="EventSubscriptionArn"
    )
    sns_topic_arn: Optional[str] = Field(default=None, alias="SnsTopicArn")
    source_ids_list: Optional[Sequence[str]] = Field(
        default=None, alias="SourceIdsList"
    )
    source_type: Optional[str] = Field(default=None, alias="SourceType")
    status: Optional[str] = Field(default=None, alias="Status")
    subscription_creation_time: Optional[str] = Field(
        default=None, alias="SubscriptionCreationTime"
    )


class AwsRedshiftClusterClusterNodeModel(BaseModel):
    node_role: Optional[str] = Field(default=None, alias="NodeRole")
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")
    public_ip_address: Optional[str] = Field(default=None, alias="PublicIpAddress")


class AwsRedshiftClusterClusterParameterStatusModel(BaseModel):
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )
    parameter_apply_error_description: Optional[str] = Field(
        default=None, alias="ParameterApplyErrorDescription"
    )


class AwsRedshiftClusterClusterSecurityGroupModel(BaseModel):
    cluster_security_group_name: Optional[str] = Field(
        default=None, alias="ClusterSecurityGroupName"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRedshiftClusterClusterSnapshotCopyStatusModel(BaseModel):
    destination_region: Optional[str] = Field(default=None, alias="DestinationRegion")
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    retention_period: Optional[int] = Field(default=None, alias="RetentionPeriod")
    snapshot_copy_grant_name: Optional[str] = Field(
        default=None, alias="SnapshotCopyGrantName"
    )


class AwsRedshiftClusterDeferredMaintenanceWindowModel(BaseModel):
    defer_maintenance_end_time: Optional[str] = Field(
        default=None, alias="DeferMaintenanceEndTime"
    )
    defer_maintenance_identifier: Optional[str] = Field(
        default=None, alias="DeferMaintenanceIdentifier"
    )
    defer_maintenance_start_time: Optional[str] = Field(
        default=None, alias="DeferMaintenanceStartTime"
    )


class AwsRedshiftClusterElasticIpStatusModel(BaseModel):
    elastic_ip: Optional[str] = Field(default=None, alias="ElasticIp")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRedshiftClusterEndpointModel(BaseModel):
    address: Optional[str] = Field(default=None, alias="Address")
    port: Optional[int] = Field(default=None, alias="Port")


class AwsRedshiftClusterHsmStatusModel(BaseModel):
    hsm_client_certificate_identifier: Optional[str] = Field(
        default=None, alias="HsmClientCertificateIdentifier"
    )
    hsm_configuration_identifier: Optional[str] = Field(
        default=None, alias="HsmConfigurationIdentifier"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRedshiftClusterIamRoleModel(BaseModel):
    apply_status: Optional[str] = Field(default=None, alias="ApplyStatus")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")


class AwsRedshiftClusterLoggingStatusModel(BaseModel):
    bucket_name: Optional[str] = Field(default=None, alias="BucketName")
    last_failure_message: Optional[str] = Field(
        default=None, alias="LastFailureMessage"
    )
    last_failure_time: Optional[str] = Field(default=None, alias="LastFailureTime")
    last_successful_delivery_time: Optional[str] = Field(
        default=None, alias="LastSuccessfulDeliveryTime"
    )
    logging_enabled: Optional[bool] = Field(default=None, alias="LoggingEnabled")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")


class AwsRedshiftClusterPendingModifiedValuesModel(BaseModel):
    automated_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotRetentionPeriod"
    )
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    cluster_type: Optional[str] = Field(default=None, alias="ClusterType")
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    encryption_type: Optional[str] = Field(default=None, alias="EncryptionType")
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )


class AwsRedshiftClusterResizeInfoModel(BaseModel):
    allow_cancel_resize: Optional[bool] = Field(default=None, alias="AllowCancelResize")
    resize_type: Optional[str] = Field(default=None, alias="ResizeType")


class AwsRedshiftClusterRestoreStatusModel(BaseModel):
    current_restore_rate_in_mega_bytes_per_second: Optional[float] = Field(
        default=None, alias="CurrentRestoreRateInMegaBytesPerSecond"
    )
    elapsed_time_in_seconds: Optional[int] = Field(
        default=None, alias="ElapsedTimeInSeconds"
    )
    estimated_time_to_completion_in_seconds: Optional[int] = Field(
        default=None, alias="EstimatedTimeToCompletionInSeconds"
    )
    progress_in_mega_bytes: Optional[int] = Field(
        default=None, alias="ProgressInMegaBytes"
    )
    snapshot_size_in_mega_bytes: Optional[int] = Field(
        default=None, alias="SnapshotSizeInMegaBytes"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class AwsRedshiftClusterVpcSecurityGroupModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    vpc_security_group_id: Optional[str] = Field(
        default=None, alias="VpcSecurityGroupId"
    )


class AwsS3AccountPublicAccessBlockDetailsModel(BaseModel):
    block_public_acls: Optional[bool] = Field(default=None, alias="BlockPublicAcls")
    block_public_policy: Optional[bool] = Field(default=None, alias="BlockPublicPolicy")
    ignore_public_acls: Optional[bool] = Field(default=None, alias="IgnorePublicAcls")
    restrict_public_buckets: Optional[bool] = Field(
        default=None, alias="RestrictPublicBuckets"
    )


class AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsModel(
    BaseModel
):
    days_after_initiation: Optional[int] = Field(
        default=None, alias="DaysAfterInitiation"
    )


class AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsModel(
    BaseModel
):
    days: Optional[int] = Field(default=None, alias="Days")
    storage_class: Optional[str] = Field(default=None, alias="StorageClass")


class AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsModel(BaseModel):
    date: Optional[str] = Field(default=None, alias="Date")
    days: Optional[int] = Field(default=None, alias="Days")
    storage_class: Optional[str] = Field(default=None, alias="StorageClass")


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsModel(
    BaseModel
):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsModel(
    BaseModel
):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsS3BucketBucketVersioningConfigurationModel(BaseModel):
    is_mfa_delete_enabled: Optional[bool] = Field(
        default=None, alias="IsMfaDeleteEnabled"
    )
    status: Optional[str] = Field(default=None, alias="Status")


class AwsS3BucketLoggingConfigurationModel(BaseModel):
    destination_bucket_name: Optional[str] = Field(
        default=None, alias="DestinationBucketName"
    )
    log_file_prefix: Optional[str] = Field(default=None, alias="LogFilePrefix")


class AwsS3BucketNotificationConfigurationS3KeyFilterRuleModel(BaseModel):
    name: Optional[Literal["Prefix", "Suffix"]] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsS3BucketServerSideEncryptionByDefaultModel(BaseModel):
    s_s_ealgorithm: Optional[str] = Field(default=None, alias="SSEAlgorithm")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KMSMasterKeyID")


class AwsS3BucketWebsiteConfigurationRedirectToModel(BaseModel):
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    protocol: Optional[str] = Field(default=None, alias="Protocol")


class AwsS3BucketWebsiteConfigurationRoutingRuleConditionModel(BaseModel):
    http_error_code_returned_equals: Optional[str] = Field(
        default=None, alias="HttpErrorCodeReturnedEquals"
    )
    key_prefix_equals: Optional[str] = Field(default=None, alias="KeyPrefixEquals")


class AwsS3BucketWebsiteConfigurationRoutingRuleRedirectModel(BaseModel):
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    http_redirect_code: Optional[str] = Field(default=None, alias="HttpRedirectCode")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    replace_key_prefix_with: Optional[str] = Field(
        default=None, alias="ReplaceKeyPrefixWith"
    )
    replace_key_with: Optional[str] = Field(default=None, alias="ReplaceKeyWith")


class AwsS3ObjectDetailsModel(BaseModel):
    last_modified: Optional[str] = Field(default=None, alias="LastModified")
    etag: Optional[str] = Field(default=None, alias="ETag")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    server_side_encryption: Optional[str] = Field(
        default=None, alias="ServerSideEncryption"
    )
    s_s_ekms_key_id: Optional[str] = Field(default=None, alias="SSEKMSKeyId")


class AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsModel(BaseModel):
    minimum_instance_metadata_service_version: Optional[str] = Field(
        default=None, alias="MinimumInstanceMetadataServiceVersion"
    )


class AwsSecretsManagerSecretRotationRulesModel(BaseModel):
    automatically_after_days: Optional[int] = Field(
        default=None, alias="AutomaticallyAfterDays"
    )


class BooleanFilterModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")


class IpFilterModel(BaseModel):
    cidr: Optional[str] = Field(default=None, alias="Cidr")


class KeywordFilterModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")


class MapFilterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")
    comparison: Optional[Literal["EQUALS", "NOT_EQUALS"]] = Field(
        default=None, alias="Comparison"
    )


class NumberFilterModel(BaseModel):
    gte: Optional[float] = Field(default=None, alias="Gte")
    lte: Optional[float] = Field(default=None, alias="Lte")
    eq: Optional[float] = Field(default=None, alias="Eq")


class StringFilterModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    comparison: Optional[
        Literal["EQUALS", "NOT_EQUALS", "PREFIX", "PREFIX_NOT_EQUALS"]
    ] = Field(default=None, alias="Comparison")


class AwsSecurityFindingIdentifierModel(BaseModel):
    id: str = Field(alias="Id")
    product_arn: str = Field(alias="ProductArn")


class MalwareModel(BaseModel):
    name: str = Field(alias="Name")
    type: Optional[
        Literal[
            "ADWARE",
            "BLENDED_THREAT",
            "BOTNET_AGENT",
            "COIN_MINER",
            "EXPLOIT_KIT",
            "KEYLOGGER",
            "MACRO",
            "POTENTIALLY_UNWANTED",
            "RANSOMWARE",
            "REMOTE_ACCESS",
            "ROOTKIT",
            "SPYWARE",
            "TROJAN",
            "VIRUS",
            "WORM",
        ]
    ] = Field(default=None, alias="Type")
    path: Optional[str] = Field(default=None, alias="Path")
    state: Optional[Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"]] = Field(
        default=None, alias="State"
    )


class NoteModel(BaseModel):
    text: str = Field(alias="Text")
    updated_by: str = Field(alias="UpdatedBy")
    updated_at: str = Field(alias="UpdatedAt")


class PatchSummaryModel(BaseModel):
    id: str = Field(alias="Id")
    installed_count: Optional[int] = Field(default=None, alias="InstalledCount")
    missing_count: Optional[int] = Field(default=None, alias="MissingCount")
    failed_count: Optional[int] = Field(default=None, alias="FailedCount")
    installed_other_count: Optional[int] = Field(
        default=None, alias="InstalledOtherCount"
    )
    installed_rejected_count: Optional[int] = Field(
        default=None, alias="InstalledRejectedCount"
    )
    installed_pending_reboot: Optional[int] = Field(
        default=None, alias="InstalledPendingReboot"
    )
    operation_start_time: Optional[str] = Field(
        default=None, alias="OperationStartTime"
    )
    operation_end_time: Optional[str] = Field(default=None, alias="OperationEndTime")
    reboot_option: Optional[str] = Field(default=None, alias="RebootOption")
    operation: Optional[str] = Field(default=None, alias="Operation")


class ProcessDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    path: Optional[str] = Field(default=None, alias="Path")
    pid: Optional[int] = Field(default=None, alias="Pid")
    parent_pid: Optional[int] = Field(default=None, alias="ParentPid")
    launched_at: Optional[str] = Field(default=None, alias="LaunchedAt")
    terminated_at: Optional[str] = Field(default=None, alias="TerminatedAt")


class RelatedFindingModel(BaseModel):
    product_arn: str = Field(alias="ProductArn")
    id: str = Field(alias="Id")


class SeverityModel(BaseModel):
    product: Optional[float] = Field(default=None, alias="Product")
    label: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
    ] = Field(default=None, alias="Label")
    normalized: Optional[int] = Field(default=None, alias="Normalized")
    original: Optional[str] = Field(default=None, alias="Original")


class ThreatIntelIndicatorModel(BaseModel):
    type: Optional[
        Literal[
            "DOMAIN",
            "EMAIL_ADDRESS",
            "HASH_MD5",
            "HASH_SHA1",
            "HASH_SHA256",
            "HASH_SHA512",
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MUTEX",
            "PROCESS",
            "URL",
        ]
    ] = Field(default=None, alias="Type")
    value: Optional[str] = Field(default=None, alias="Value")
    category: Optional[
        Literal[
            "BACKDOOR",
            "CARD_STEALER",
            "COMMAND_AND_CONTROL",
            "DROP_SITE",
            "EXPLOIT_SITE",
            "KEYLOGGER",
        ]
    ] = Field(default=None, alias="Category")
    last_observed_at: Optional[str] = Field(default=None, alias="LastObservedAt")
    source: Optional[str] = Field(default=None, alias="Source")
    source_url: Optional[str] = Field(default=None, alias="SourceUrl")


class WorkflowModel(BaseModel):
    status: Optional[Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]] = Field(
        default=None, alias="Status"
    )


class AwsSnsTopicSubscriptionModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    protocol: Optional[str] = Field(default=None, alias="Protocol")


class AwsSqsQueueDetailsModel(BaseModel):
    kms_data_key_reuse_period_seconds: Optional[int] = Field(
        default=None, alias="KmsDataKeyReusePeriodSeconds"
    )
    kms_master_key_id: Optional[str] = Field(default=None, alias="KmsMasterKeyId")
    queue_name: Optional[str] = Field(default=None, alias="QueueName")
    dead_letter_target_arn: Optional[str] = Field(
        default=None, alias="DeadLetterTargetArn"
    )


class AwsSsmComplianceSummaryModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    compliant_critical_count: Optional[int] = Field(
        default=None, alias="CompliantCriticalCount"
    )
    compliant_high_count: Optional[int] = Field(
        default=None, alias="CompliantHighCount"
    )
    compliant_medium_count: Optional[int] = Field(
        default=None, alias="CompliantMediumCount"
    )
    execution_type: Optional[str] = Field(default=None, alias="ExecutionType")
    non_compliant_critical_count: Optional[int] = Field(
        default=None, alias="NonCompliantCriticalCount"
    )
    compliant_informational_count: Optional[int] = Field(
        default=None, alias="CompliantInformationalCount"
    )
    non_compliant_informational_count: Optional[int] = Field(
        default=None, alias="NonCompliantInformationalCount"
    )
    compliant_unspecified_count: Optional[int] = Field(
        default=None, alias="CompliantUnspecifiedCount"
    )
    non_compliant_low_count: Optional[int] = Field(
        default=None, alias="NonCompliantLowCount"
    )
    non_compliant_high_count: Optional[int] = Field(
        default=None, alias="NonCompliantHighCount"
    )
    compliant_low_count: Optional[int] = Field(default=None, alias="CompliantLowCount")
    compliance_type: Optional[str] = Field(default=None, alias="ComplianceType")
    patch_baseline_id: Optional[str] = Field(default=None, alias="PatchBaselineId")
    overall_severity: Optional[str] = Field(default=None, alias="OverallSeverity")
    non_compliant_medium_count: Optional[int] = Field(
        default=None, alias="NonCompliantMediumCount"
    )
    non_compliant_unspecified_count: Optional[int] = Field(
        default=None, alias="NonCompliantUnspecifiedCount"
    )
    patch_group: Optional[str] = Field(default=None, alias="PatchGroup")


class AwsWafRateBasedRuleMatchPredicateModel(BaseModel):
    data_id: Optional[str] = Field(default=None, alias="DataId")
    negated: Optional[bool] = Field(default=None, alias="Negated")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRegionalRateBasedRuleMatchPredicateModel(BaseModel):
    data_id: Optional[str] = Field(default=None, alias="DataId")
    negated: Optional[bool] = Field(default=None, alias="Negated")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRegionalRulePredicateListDetailsModel(BaseModel):
    data_id: Optional[str] = Field(default=None, alias="DataId")
    negated: Optional[bool] = Field(default=None, alias="Negated")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRegionalRuleGroupRulesActionDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRegionalWebAclRulesListActionDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRegionalWebAclRulesListOverrideActionDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRulePredicateListDetailsModel(BaseModel):
    data_id: Optional[str] = Field(default=None, alias="DataId")
    negated: Optional[bool] = Field(default=None, alias="Negated")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRuleGroupRulesActionDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class WafActionModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class WafExcludedRuleModel(BaseModel):
    rule_id: Optional[str] = Field(default=None, alias="RuleId")


class WafOverrideActionModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafv2CustomHttpHeaderModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class AwsWafv2VisibilityConfigDetailsModel(BaseModel):
    cloud_watch_metrics_enabled: Optional[bool] = Field(
        default=None, alias="CloudWatchMetricsEnabled"
    )
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    sampled_requests_enabled: Optional[bool] = Field(
        default=None, alias="SampledRequestsEnabled"
    )


class AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsModel(BaseModel):
    immunity_time: Optional[int] = Field(default=None, alias="ImmunityTime")


class AwsXrayEncryptionConfigDetailsModel(BaseModel):
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    status: Optional[str] = Field(default=None, alias="Status")
    type: Optional[str] = Field(default=None, alias="Type")


class BatchDisableStandardsRequestModel(BaseModel):
    standards_subscription_arns: Sequence[str] = Field(
        alias="StandardsSubscriptionArns"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class StandardsSubscriptionRequestModel(BaseModel):
    standards_arn: str = Field(alias="StandardsArn")
    standards_input: Optional[Mapping[str, str]] = Field(
        default=None, alias="StandardsInput"
    )


class BatchGetSecurityControlsRequestModel(BaseModel):
    security_control_ids: Sequence[str] = Field(alias="SecurityControlIds")


class SecurityControlModel(BaseModel):
    security_control_id: str = Field(alias="SecurityControlId")
    security_control_arn: str = Field(alias="SecurityControlArn")
    title: str = Field(alias="Title")
    description: str = Field(alias="Description")
    remediation_url: str = Field(alias="RemediationUrl")
    severity_rating: Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"] = Field(
        alias="SeverityRating"
    )
    security_control_status: Literal["DISABLED", "ENABLED"] = Field(
        alias="SecurityControlStatus"
    )


class UnprocessedSecurityControlModel(BaseModel):
    security_control_id: str = Field(alias="SecurityControlId")
    error_code: Literal[
        "ACCESS_DENIED", "INVALID_INPUT", "LIMIT_EXCEEDED", "NOT_FOUND"
    ] = Field(alias="ErrorCode")
    error_reason: Optional[str] = Field(default=None, alias="ErrorReason")


class StandardsControlAssociationIdModel(BaseModel):
    security_control_id: str = Field(alias="SecurityControlId")
    standards_arn: str = Field(alias="StandardsArn")


class StandardsControlAssociationDetailModel(BaseModel):
    standards_arn: str = Field(alias="StandardsArn")
    security_control_id: str = Field(alias="SecurityControlId")
    security_control_arn: str = Field(alias="SecurityControlArn")
    association_status: Literal["DISABLED", "ENABLED"] = Field(
        alias="AssociationStatus"
    )
    related_requirements: Optional[List[str]] = Field(
        default=None, alias="RelatedRequirements"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    updated_reason: Optional[str] = Field(default=None, alias="UpdatedReason")
    standards_control_title: Optional[str] = Field(
        default=None, alias="StandardsControlTitle"
    )
    standards_control_description: Optional[str] = Field(
        default=None, alias="StandardsControlDescription"
    )
    standards_control_arns: Optional[List[str]] = Field(
        default=None, alias="StandardsControlArns"
    )


class ImportFindingsErrorModel(BaseModel):
    id: str = Field(alias="Id")
    error_code: str = Field(alias="ErrorCode")
    error_message: str = Field(alias="ErrorMessage")


class NoteUpdateModel(BaseModel):
    text: str = Field(alias="Text")
    updated_by: str = Field(alias="UpdatedBy")


class SeverityUpdateModel(BaseModel):
    normalized: Optional[int] = Field(default=None, alias="Normalized")
    product: Optional[float] = Field(default=None, alias="Product")
    label: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
    ] = Field(default=None, alias="Label")


class WorkflowUpdateModel(BaseModel):
    status: Optional[Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]] = Field(
        default=None, alias="Status"
    )


class StandardsControlAssociationUpdateModel(BaseModel):
    standards_arn: str = Field(alias="StandardsArn")
    security_control_id: str = Field(alias="SecurityControlId")
    association_status: Literal["DISABLED", "ENABLED"] = Field(
        alias="AssociationStatus"
    )
    updated_reason: Optional[str] = Field(default=None, alias="UpdatedReason")


class CellModel(BaseModel):
    column: Optional[int] = Field(default=None, alias="Column")
    row: Optional[int] = Field(default=None, alias="Row")
    column_name: Optional[str] = Field(default=None, alias="ColumnName")
    cell_reference: Optional[str] = Field(default=None, alias="CellReference")


class ClassificationStatusModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    reason: Optional[str] = Field(default=None, alias="Reason")


class StatusReasonModel(BaseModel):
    reason_code: str = Field(alias="ReasonCode")
    description: Optional[str] = Field(default=None, alias="Description")


class VolumeMountModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    mount_path: Optional[str] = Field(default=None, alias="MountPath")


class CreateActionTargetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    id: str = Field(alias="Id")


class CreateFindingAggregatorRequestModel(BaseModel):
    region_linking_mode: str = Field(alias="RegionLinkingMode")
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")


class ResultModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    processing_result: Optional[str] = Field(default=None, alias="ProcessingResult")


class DateRangeModel(BaseModel):
    value: Optional[int] = Field(default=None, alias="Value")
    unit: Optional[Literal["DAYS"]] = Field(default=None, alias="Unit")


class DeclineInvitationsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class DeleteActionTargetRequestModel(BaseModel):
    action_target_arn: str = Field(alias="ActionTargetArn")


class DeleteFindingAggregatorRequestModel(BaseModel):
    finding_aggregator_arn: str = Field(alias="FindingAggregatorArn")


class DeleteInsightRequestModel(BaseModel):
    insight_arn: str = Field(alias="InsightArn")


class DeleteInvitationsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class DeleteMembersRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeActionTargetsRequestModel(BaseModel):
    action_target_arns: Optional[Sequence[str]] = Field(
        default=None, alias="ActionTargetArns"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeHubRequestModel(BaseModel):
    hub_arn: Optional[str] = Field(default=None, alias="HubArn")


class DescribeProductsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    product_arn: Optional[str] = Field(default=None, alias="ProductArn")


class ProductModel(BaseModel):
    product_arn: str = Field(alias="ProductArn")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    company_name: Optional[str] = Field(default=None, alias="CompanyName")
    description: Optional[str] = Field(default=None, alias="Description")
    categories: Optional[List[str]] = Field(default=None, alias="Categories")
    integration_types: Optional[
        List[
            Literal[
                "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
                "SEND_FINDINGS_TO_SECURITY_HUB",
                "UPDATE_FINDINGS_IN_SECURITY_HUB",
            ]
        ]
    ] = Field(default=None, alias="IntegrationTypes")
    marketplace_url: Optional[str] = Field(default=None, alias="MarketplaceUrl")
    activation_url: Optional[str] = Field(default=None, alias="ActivationUrl")
    product_subscription_resource_policy: Optional[str] = Field(
        default=None, alias="ProductSubscriptionResourcePolicy"
    )


class DescribeStandardsControlsRequestModel(BaseModel):
    standards_subscription_arn: str = Field(alias="StandardsSubscriptionArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class StandardsControlModel(BaseModel):
    standards_control_arn: Optional[str] = Field(
        default=None, alias="StandardsControlArn"
    )
    control_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ControlStatus"
    )
    disabled_reason: Optional[str] = Field(default=None, alias="DisabledReason")
    control_status_updated_at: Optional[datetime] = Field(
        default=None, alias="ControlStatusUpdatedAt"
    )
    control_id: Optional[str] = Field(default=None, alias="ControlId")
    title: Optional[str] = Field(default=None, alias="Title")
    description: Optional[str] = Field(default=None, alias="Description")
    remediation_url: Optional[str] = Field(default=None, alias="RemediationUrl")
    severity_rating: Optional[Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="SeverityRating"
    )
    related_requirements: Optional[List[str]] = Field(
        default=None, alias="RelatedRequirements"
    )


class DescribeStandardsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DisableImportFindingsForProductRequestModel(BaseModel):
    product_subscription_arn: str = Field(alias="ProductSubscriptionArn")


class DisableOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: str = Field(alias="AdminAccountId")


class DisassociateMembersRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class EnableImportFindingsForProductRequestModel(BaseModel):
    product_arn: str = Field(alias="ProductArn")


class EnableOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: str = Field(alias="AdminAccountId")


class EnableSecurityHubRequestModel(BaseModel):
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    enable_default_standards: Optional[bool] = Field(
        default=None, alias="EnableDefaultStandards"
    )
    control_finding_generator: Optional[
        Literal["SECURITY_CONTROL", "STANDARD_CONTROL"]
    ] = Field(default=None, alias="ControlFindingGenerator")


class FilePathsModel(BaseModel):
    file_path: Optional[str] = Field(default=None, alias="FilePath")
    file_name: Optional[str] = Field(default=None, alias="FileName")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    hash: Optional[str] = Field(default=None, alias="Hash")


class FindingAggregatorModel(BaseModel):
    finding_aggregator_arn: Optional[str] = Field(
        default=None, alias="FindingAggregatorArn"
    )


class FindingProviderSeverityModel(BaseModel):
    label: Optional[
        Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
    ] = Field(default=None, alias="Label")
    original: Optional[str] = Field(default=None, alias="Original")


class FirewallPolicyStatefulRuleGroupReferencesDetailsModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class FirewallPolicyStatelessRuleGroupReferencesDetailsModel(BaseModel):
    priority: Optional[int] = Field(default=None, alias="Priority")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class InvitationModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    invitation_id: Optional[str] = Field(default=None, alias="InvitationId")
    invited_at: Optional[datetime] = Field(default=None, alias="InvitedAt")
    member_status: Optional[str] = Field(default=None, alias="MemberStatus")


class GetEnabledStandardsRequestModel(BaseModel):
    standards_subscription_arns: Optional[Sequence[str]] = Field(
        default=None, alias="StandardsSubscriptionArns"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetFindingAggregatorRequestModel(BaseModel):
    finding_aggregator_arn: str = Field(alias="FindingAggregatorArn")


class SortCriterionModel(BaseModel):
    field: Optional[str] = Field(default=None, alias="Field")
    sort_order: Optional[Literal["asc", "desc"]] = Field(
        default=None, alias="SortOrder"
    )


class GetInsightResultsRequestModel(BaseModel):
    insight_arn: str = Field(alias="InsightArn")


class GetInsightsRequestModel(BaseModel):
    insight_arns: Optional[Sequence[str]] = Field(default=None, alias="InsightArns")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class GetMembersRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class MemberModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    email: Optional[str] = Field(default=None, alias="Email")
    master_id: Optional[str] = Field(default=None, alias="MasterId")
    administrator_id: Optional[str] = Field(default=None, alias="AdministratorId")
    member_status: Optional[str] = Field(default=None, alias="MemberStatus")
    invited_at: Optional[datetime] = Field(default=None, alias="InvitedAt")
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")


class InsightResultValueModel(BaseModel):
    group_by_attribute_value: str = Field(alias="GroupByAttributeValue")
    count: int = Field(alias="Count")


class InviteMembersRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class ListEnabledProductsForImportRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFindingAggregatorsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListInvitationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMembersRequestModel(BaseModel):
    only_associated: Optional[bool] = Field(default=None, alias="OnlyAssociated")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListOrganizationAdminAccountsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSecurityControlDefinitionsRequestModel(BaseModel):
    standards_arn: Optional[str] = Field(default=None, alias="StandardsArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SecurityControlDefinitionModel(BaseModel):
    security_control_id: str = Field(alias="SecurityControlId")
    title: str = Field(alias="Title")
    description: str = Field(alias="Description")
    remediation_url: str = Field(alias="RemediationUrl")
    severity_rating: Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"] = Field(
        alias="SeverityRating"
    )
    current_region_availability: Literal["AVAILABLE", "UNAVAILABLE"] = Field(
        alias="CurrentRegionAvailability"
    )


class ListStandardsControlAssociationsRequestModel(BaseModel):
    security_control_id: str = Field(alias="SecurityControlId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class StandardsControlAssociationSummaryModel(BaseModel):
    standards_arn: str = Field(alias="StandardsArn")
    security_control_id: str = Field(alias="SecurityControlId")
    security_control_arn: str = Field(alias="SecurityControlArn")
    association_status: Literal["DISABLED", "ENABLED"] = Field(
        alias="AssociationStatus"
    )
    related_requirements: Optional[List[str]] = Field(
        default=None, alias="RelatedRequirements"
    )
    updated_at: Optional[datetime] = Field(default=None, alias="UpdatedAt")
    updated_reason: Optional[str] = Field(default=None, alias="UpdatedReason")
    standards_control_title: Optional[str] = Field(
        default=None, alias="StandardsControlTitle"
    )
    standards_control_description: Optional[str] = Field(
        default=None, alias="StandardsControlDescription"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class PortRangeModel(BaseModel):
    begin: Optional[int] = Field(default=None, alias="Begin")
    end: Optional[int] = Field(default=None, alias="End")


class RangeModel(BaseModel):
    start: Optional[int] = Field(default=None, alias="Start")
    end: Optional[int] = Field(default=None, alias="End")
    start_column: Optional[int] = Field(default=None, alias="StartColumn")


class RecordModel(BaseModel):
    json_path: Optional[str] = Field(default=None, alias="JsonPath")
    record_index: Optional[int] = Field(default=None, alias="RecordIndex")


class RecommendationModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")
    url: Optional[str] = Field(default=None, alias="Url")


class RuleGroupSourceListDetailsModel(BaseModel):
    generated_rules_type: Optional[str] = Field(
        default=None, alias="GeneratedRulesType"
    )
    target_types: Optional[Sequence[str]] = Field(default=None, alias="TargetTypes")
    targets: Optional[Sequence[str]] = Field(default=None, alias="Targets")


class RuleGroupSourceStatefulRulesHeaderDetailsModel(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")
    destination_port: Optional[str] = Field(default=None, alias="DestinationPort")
    direction: Optional[str] = Field(default=None, alias="Direction")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    source: Optional[str] = Field(default=None, alias="Source")
    source_port: Optional[str] = Field(default=None, alias="SourcePort")


class RuleGroupSourceStatefulRulesOptionsDetailsModel(BaseModel):
    keyword: Optional[str] = Field(default=None, alias="Keyword")
    settings: Optional[Sequence[str]] = Field(default=None, alias="Settings")


class RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsModel(BaseModel):
    from_port: Optional[int] = Field(default=None, alias="FromPort")
    to_port: Optional[int] = Field(default=None, alias="ToPort")


class RuleGroupSourceStatelessRuleMatchAttributesDestinationsModel(BaseModel):
    address_definition: Optional[str] = Field(default=None, alias="AddressDefinition")


class RuleGroupSourceStatelessRuleMatchAttributesSourcePortsModel(BaseModel):
    from_port: Optional[int] = Field(default=None, alias="FromPort")
    to_port: Optional[int] = Field(default=None, alias="ToPort")


class RuleGroupSourceStatelessRuleMatchAttributesSourcesModel(BaseModel):
    address_definition: Optional[str] = Field(default=None, alias="AddressDefinition")


class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsModel(BaseModel):
    flags: Optional[Sequence[str]] = Field(default=None, alias="Flags")
    masks: Optional[Sequence[str]] = Field(default=None, alias="Masks")


class RuleGroupVariablesIpSetsDetailsModel(BaseModel):
    definition: Optional[Sequence[str]] = Field(default=None, alias="Definition")


class RuleGroupVariablesPortSetsDetailsModel(BaseModel):
    definition: Optional[Sequence[str]] = Field(default=None, alias="Definition")


class SoftwarePackageModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")
    epoch: Optional[str] = Field(default=None, alias="Epoch")
    release: Optional[str] = Field(default=None, alias="Release")
    architecture: Optional[str] = Field(default=None, alias="Architecture")
    package_manager: Optional[str] = Field(default=None, alias="PackageManager")
    file_path: Optional[str] = Field(default=None, alias="FilePath")
    fixed_in_version: Optional[str] = Field(default=None, alias="FixedInVersion")
    remediation: Optional[str] = Field(default=None, alias="Remediation")
    source_layer_hash: Optional[str] = Field(default=None, alias="SourceLayerHash")
    source_layer_arn: Optional[str] = Field(default=None, alias="SourceLayerArn")


class StandardsManagedByModel(BaseModel):
    company: Optional[str] = Field(default=None, alias="Company")
    product: Optional[str] = Field(default=None, alias="Product")


class StandardsStatusReasonModel(BaseModel):
    status_reason_code: Literal[
        "INTERNAL_ERROR", "NO_AVAILABLE_CONFIGURATION_RECORDER"
    ] = Field(alias="StatusReasonCode")


class StatelessCustomPublishMetricActionDimensionModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateActionTargetRequestModel(BaseModel):
    action_target_arn: str = Field(alias="ActionTargetArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateFindingAggregatorRequestModel(BaseModel):
    finding_aggregator_arn: str = Field(alias="FindingAggregatorArn")
    region_linking_mode: str = Field(alias="RegionLinkingMode")
    regions: Optional[Sequence[str]] = Field(default=None, alias="Regions")


class UpdateOrganizationConfigurationRequestModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")
    auto_enable_standards: Optional[Literal["DEFAULT", "NONE"]] = Field(
        default=None, alias="AutoEnableStandards"
    )


class UpdateSecurityHubConfigurationRequestModel(BaseModel):
    auto_enable_controls: Optional[bool] = Field(
        default=None, alias="AutoEnableControls"
    )
    control_finding_generator: Optional[
        Literal["SECURITY_CONTROL", "STANDARD_CONTROL"]
    ] = Field(default=None, alias="ControlFindingGenerator")


class UpdateStandardsControlRequestModel(BaseModel):
    standards_control_arn: str = Field(alias="StandardsControlArn")
    control_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ControlStatus"
    )
    disabled_reason: Optional[str] = Field(default=None, alias="DisabledReason")


class VulnerabilityVendorModel(BaseModel):
    name: str = Field(alias="Name")
    url: Optional[str] = Field(default=None, alias="Url")
    vendor_severity: Optional[str] = Field(default=None, alias="VendorSeverity")
    vendor_created_at: Optional[str] = Field(default=None, alias="VendorCreatedAt")
    vendor_updated_at: Optional[str] = Field(default=None, alias="VendorUpdatedAt")


class CreateMembersRequestModel(BaseModel):
    account_details: Sequence[AccountDetailsModel] = Field(alias="AccountDetails")


class ActionRemoteIpDetailsModel(BaseModel):
    ip_address_v4: Optional[str] = Field(default=None, alias="IpAddressV4")
    organization: Optional[IpOrganizationDetailsModel] = Field(
        default=None, alias="Organization"
    )
    country: Optional[CountryModel] = Field(default=None, alias="Country")
    city: Optional[CityModel] = Field(default=None, alias="City")
    geo_location: Optional[GeoLocationModel] = Field(default=None, alias="GeoLocation")


class CvssModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="Version")
    base_score: Optional[float] = Field(default=None, alias="BaseScore")
    base_vector: Optional[str] = Field(default=None, alias="BaseVector")
    source: Optional[str] = Field(default=None, alias="Source")
    adjustments: Optional[Sequence[AdjustmentModel]] = Field(
        default=None, alias="Adjustments"
    )


class AwsApiGatewayRestApiDetailsModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    created_date: Optional[str] = Field(default=None, alias="CreatedDate")
    version: Optional[str] = Field(default=None, alias="Version")
    binary_media_types: Optional[Sequence[str]] = Field(
        default=None, alias="BinaryMediaTypes"
    )
    minimum_compression_size: Optional[int] = Field(
        default=None, alias="MinimumCompressionSize"
    )
    api_key_source: Optional[str] = Field(default=None, alias="ApiKeySource")
    endpoint_configuration: Optional[AwsApiGatewayEndpointConfigurationModel] = Field(
        default=None, alias="EndpointConfiguration"
    )


class AwsApiGatewayStageDetailsModel(BaseModel):
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    client_certificate_id: Optional[str] = Field(
        default=None, alias="ClientCertificateId"
    )
    stage_name: Optional[str] = Field(default=None, alias="StageName")
    description: Optional[str] = Field(default=None, alias="Description")
    cache_cluster_enabled: Optional[bool] = Field(
        default=None, alias="CacheClusterEnabled"
    )
    cache_cluster_size: Optional[str] = Field(default=None, alias="CacheClusterSize")
    cache_cluster_status: Optional[str] = Field(
        default=None, alias="CacheClusterStatus"
    )
    method_settings: Optional[Sequence[AwsApiGatewayMethodSettingsModel]] = Field(
        default=None, alias="MethodSettings"
    )
    variables: Optional[Mapping[str, str]] = Field(default=None, alias="Variables")
    documentation_version: Optional[str] = Field(
        default=None, alias="DocumentationVersion"
    )
    access_log_settings: Optional[AwsApiGatewayAccessLogSettingsModel] = Field(
        default=None, alias="AccessLogSettings"
    )
    canary_settings: Optional[AwsApiGatewayCanarySettingsModel] = Field(
        default=None, alias="CanarySettings"
    )
    tracing_enabled: Optional[bool] = Field(default=None, alias="TracingEnabled")
    created_date: Optional[str] = Field(default=None, alias="CreatedDate")
    last_updated_date: Optional[str] = Field(default=None, alias="LastUpdatedDate")
    web_acl_arn: Optional[str] = Field(default=None, alias="WebAclArn")


class AwsApiGatewayV2ApiDetailsModel(BaseModel):
    api_endpoint: Optional[str] = Field(default=None, alias="ApiEndpoint")
    api_id: Optional[str] = Field(default=None, alias="ApiId")
    api_key_selection_expression: Optional[str] = Field(
        default=None, alias="ApiKeySelectionExpression"
    )
    created_date: Optional[str] = Field(default=None, alias="CreatedDate")
    description: Optional[str] = Field(default=None, alias="Description")
    version: Optional[str] = Field(default=None, alias="Version")
    name: Optional[str] = Field(default=None, alias="Name")
    protocol_type: Optional[str] = Field(default=None, alias="ProtocolType")
    route_selection_expression: Optional[str] = Field(
        default=None, alias="RouteSelectionExpression"
    )
    cors_configuration: Optional[AwsCorsConfigurationModel] = Field(
        default=None, alias="CorsConfiguration"
    )


class AwsApiGatewayV2StageDetailsModel(BaseModel):
    client_certificate_id: Optional[str] = Field(
        default=None, alias="ClientCertificateId"
    )
    created_date: Optional[str] = Field(default=None, alias="CreatedDate")
    description: Optional[str] = Field(default=None, alias="Description")
    default_route_settings: Optional[AwsApiGatewayV2RouteSettingsModel] = Field(
        default=None, alias="DefaultRouteSettings"
    )
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    last_updated_date: Optional[str] = Field(default=None, alias="LastUpdatedDate")
    route_settings: Optional[AwsApiGatewayV2RouteSettingsModel] = Field(
        default=None, alias="RouteSettings"
    )
    stage_name: Optional[str] = Field(default=None, alias="StageName")
    stage_variables: Optional[Mapping[str, str]] = Field(
        default=None, alias="StageVariables"
    )
    access_log_settings: Optional[AwsApiGatewayAccessLogSettingsModel] = Field(
        default=None, alias="AccessLogSettings"
    )
    auto_deploy: Optional[bool] = Field(default=None, alias="AutoDeploy")
    last_deployment_status_message: Optional[str] = Field(
        default=None, alias="LastDeploymentStatusMessage"
    )
    api_gateway_managed: Optional[bool] = Field(default=None, alias="ApiGatewayManaged")


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsModel(
    BaseModel
):
    launch_template_specification: Optional[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationModel
    ] = Field(default=None, alias="LaunchTemplateSpecification")
    overrides: Optional[
        Sequence[
            AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsModel
        ]
    ] = Field(default=None, alias="Overrides")


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    ebs: Optional[
        AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsModel
    ] = Field(default=None, alias="Ebs")
    no_device: Optional[bool] = Field(default=None, alias="NoDevice")
    virtual_name: Optional[str] = Field(default=None, alias="VirtualName")


class AwsBackupBackupPlanRuleCopyActionsDetailsModel(BaseModel):
    destination_backup_vault_arn: Optional[str] = Field(
        default=None, alias="DestinationBackupVaultArn"
    )
    lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsModel] = Field(
        default=None, alias="Lifecycle"
    )


class AwsBackupBackupVaultDetailsModel(BaseModel):
    backup_vault_arn: Optional[str] = Field(default=None, alias="BackupVaultArn")
    backup_vault_name: Optional[str] = Field(default=None, alias="BackupVaultName")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    notifications: Optional[AwsBackupBackupVaultNotificationsDetailsModel] = Field(
        default=None, alias="Notifications"
    )
    access_policy: Optional[str] = Field(default=None, alias="AccessPolicy")


class AwsBackupRecoveryPointDetailsModel(BaseModel):
    backup_size_in_bytes: Optional[int] = Field(default=None, alias="BackupSizeInBytes")
    backup_vault_arn: Optional[str] = Field(default=None, alias="BackupVaultArn")
    backup_vault_name: Optional[str] = Field(default=None, alias="BackupVaultName")
    calculated_lifecycle: Optional[
        AwsBackupRecoveryPointCalculatedLifecycleDetailsModel
    ] = Field(default=None, alias="CalculatedLifecycle")
    completion_date: Optional[str] = Field(default=None, alias="CompletionDate")
    created_by: Optional[AwsBackupRecoveryPointCreatedByDetailsModel] = Field(
        default=None, alias="CreatedBy"
    )
    creation_date: Optional[str] = Field(default=None, alias="CreationDate")
    encryption_key_arn: Optional[str] = Field(default=None, alias="EncryptionKeyArn")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    is_encrypted: Optional[bool] = Field(default=None, alias="IsEncrypted")
    last_restore_time: Optional[str] = Field(default=None, alias="LastRestoreTime")
    lifecycle: Optional[AwsBackupRecoveryPointLifecycleDetailsModel] = Field(
        default=None, alias="Lifecycle"
    )
    recovery_point_arn: Optional[str] = Field(default=None, alias="RecoveryPointArn")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    source_backup_vault_arn: Optional[str] = Field(
        default=None, alias="SourceBackupVaultArn"
    )
    status: Optional[str] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    storage_class: Optional[str] = Field(default=None, alias="StorageClass")


class AwsCertificateManagerCertificateDomainValidationOptionModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    resource_record: Optional[
        AwsCertificateManagerCertificateResourceRecordModel
    ] = Field(default=None, alias="ResourceRecord")
    validation_domain: Optional[str] = Field(default=None, alias="ValidationDomain")
    validation_emails: Optional[Sequence[str]] = Field(
        default=None, alias="ValidationEmails"
    )
    validation_method: Optional[str] = Field(default=None, alias="ValidationMethod")
    validation_status: Optional[str] = Field(default=None, alias="ValidationStatus")


class AwsCloudFormationStackDetailsModel(BaseModel):
    capabilities: Optional[Sequence[str]] = Field(default=None, alias="Capabilities")
    creation_time: Optional[str] = Field(default=None, alias="CreationTime")
    description: Optional[str] = Field(default=None, alias="Description")
    disable_rollback: Optional[bool] = Field(default=None, alias="DisableRollback")
    drift_information: Optional[
        AwsCloudFormationStackDriftInformationDetailsModel
    ] = Field(default=None, alias="DriftInformation")
    enable_termination_protection: Optional[bool] = Field(
        default=None, alias="EnableTerminationProtection"
    )
    last_updated_time: Optional[str] = Field(default=None, alias="LastUpdatedTime")
    notification_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NotificationArns"
    )
    outputs: Optional[Sequence[AwsCloudFormationStackOutputsDetailsModel]] = Field(
        default=None, alias="Outputs"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    stack_id: Optional[str] = Field(default=None, alias="StackId")
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    stack_status: Optional[str] = Field(default=None, alias="StackStatus")
    stack_status_reason: Optional[str] = Field(default=None, alias="StackStatusReason")
    timeout_in_minutes: Optional[int] = Field(default=None, alias="TimeoutInMinutes")


class AwsCloudFrontDistributionCacheBehaviorsModel(BaseModel):
    items: Optional[Sequence[AwsCloudFrontDistributionCacheBehaviorModel]] = Field(
        default=None, alias="Items"
    )


class AwsCloudFrontDistributionOriginCustomOriginConfigModel(BaseModel):
    http_port: Optional[int] = Field(default=None, alias="HttpPort")
    https_port: Optional[int] = Field(default=None, alias="HttpsPort")
    origin_keepalive_timeout: Optional[int] = Field(
        default=None, alias="OriginKeepaliveTimeout"
    )
    origin_protocol_policy: Optional[str] = Field(
        default=None, alias="OriginProtocolPolicy"
    )
    origin_read_timeout: Optional[int] = Field(default=None, alias="OriginReadTimeout")
    origin_ssl_protocols: Optional[
        AwsCloudFrontDistributionOriginSslProtocolsModel
    ] = Field(default=None, alias="OriginSslProtocols")


class AwsCloudFrontDistributionOriginGroupFailoverModel(BaseModel):
    status_codes: Optional[
        AwsCloudFrontDistributionOriginGroupFailoverStatusCodesModel
    ] = Field(default=None, alias="StatusCodes")


class AwsCloudWatchAlarmDetailsModel(BaseModel):
    actions_enabled: Optional[bool] = Field(default=None, alias="ActionsEnabled")
    alarm_actions: Optional[Sequence[str]] = Field(default=None, alias="AlarmActions")
    alarm_arn: Optional[str] = Field(default=None, alias="AlarmArn")
    alarm_configuration_updated_timestamp: Optional[str] = Field(
        default=None, alias="AlarmConfigurationUpdatedTimestamp"
    )
    alarm_description: Optional[str] = Field(default=None, alias="AlarmDescription")
    alarm_name: Optional[str] = Field(default=None, alias="AlarmName")
    comparison_operator: Optional[str] = Field(default=None, alias="ComparisonOperator")
    datapoints_to_alarm: Optional[int] = Field(default=None, alias="DatapointsToAlarm")
    dimensions: Optional[Sequence[AwsCloudWatchAlarmDimensionsDetailsModel]] = Field(
        default=None, alias="Dimensions"
    )
    evaluate_low_sample_count_percentile: Optional[str] = Field(
        default=None, alias="EvaluateLowSampleCountPercentile"
    )
    evaluation_periods: Optional[int] = Field(default=None, alias="EvaluationPeriods")
    extended_statistic: Optional[str] = Field(default=None, alias="ExtendedStatistic")
    insufficient_data_actions: Optional[Sequence[str]] = Field(
        default=None, alias="InsufficientDataActions"
    )
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    ok_actions: Optional[Sequence[str]] = Field(default=None, alias="OkActions")
    period: Optional[int] = Field(default=None, alias="Period")
    statistic: Optional[str] = Field(default=None, alias="Statistic")
    threshold: Optional[float] = Field(default=None, alias="Threshold")
    threshold_metric_id: Optional[str] = Field(default=None, alias="ThresholdMetricId")
    treat_missing_data: Optional[str] = Field(default=None, alias="TreatMissingData")
    unit: Optional[str] = Field(default=None, alias="Unit")


class AwsCodeBuildProjectEnvironmentModel(BaseModel):
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    environment_variables: Optional[
        Sequence[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsModel]
    ] = Field(default=None, alias="EnvironmentVariables")
    privileged_mode: Optional[bool] = Field(default=None, alias="PrivilegedMode")
    image_pull_credentials_type: Optional[str] = Field(
        default=None, alias="ImagePullCredentialsType"
    )
    registry_credential: Optional[
        AwsCodeBuildProjectEnvironmentRegistryCredentialModel
    ] = Field(default=None, alias="RegistryCredential")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsCodeBuildProjectLogsConfigDetailsModel(BaseModel):
    cloud_watch_logs: Optional[
        AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsModel
    ] = Field(default=None, alias="CloudWatchLogs")
    s3_logs: Optional[AwsCodeBuildProjectLogsConfigS3LogsDetailsModel] = Field(
        default=None, alias="S3Logs"
    )


class AwsDynamoDbTableGlobalSecondaryIndexModel(BaseModel):
    backfilling: Optional[bool] = Field(default=None, alias="Backfilling")
    index_arn: Optional[str] = Field(default=None, alias="IndexArn")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    index_size_bytes: Optional[int] = Field(default=None, alias="IndexSizeBytes")
    index_status: Optional[str] = Field(default=None, alias="IndexStatus")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    key_schema: Optional[Sequence[AwsDynamoDbTableKeySchemaModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[AwsDynamoDbTableProjectionModel] = Field(
        default=None, alias="Projection"
    )
    provisioned_throughput: Optional[
        AwsDynamoDbTableProvisionedThroughputModel
    ] = Field(default=None, alias="ProvisionedThroughput")


class AwsDynamoDbTableLocalSecondaryIndexModel(BaseModel):
    index_arn: Optional[str] = Field(default=None, alias="IndexArn")
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    key_schema: Optional[Sequence[AwsDynamoDbTableKeySchemaModel]] = Field(
        default=None, alias="KeySchema"
    )
    projection: Optional[AwsDynamoDbTableProjectionModel] = Field(
        default=None, alias="Projection"
    )


class AwsDynamoDbTableReplicaGlobalSecondaryIndexModel(BaseModel):
    index_name: Optional[str] = Field(default=None, alias="IndexName")
    provisioned_throughput_override: Optional[
        AwsDynamoDbTableProvisionedThroughputOverrideModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")


class AwsEc2InstanceDetailsModel(BaseModel):
    type: Optional[str] = Field(default=None, alias="Type")
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    ip_v4_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="IpV4Addresses"
    )
    ip_v6_addresses: Optional[Sequence[str]] = Field(
        default=None, alias="IpV6Addresses"
    )
    key_name: Optional[str] = Field(default=None, alias="KeyName")
    iam_instance_profile_arn: Optional[str] = Field(
        default=None, alias="IamInstanceProfileArn"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    launched_at: Optional[str] = Field(default=None, alias="LaunchedAt")
    network_interfaces: Optional[
        Sequence[AwsEc2InstanceNetworkInterfacesDetailsModel]
    ] = Field(default=None, alias="NetworkInterfaces")
    virtualization_type: Optional[str] = Field(default=None, alias="VirtualizationType")
    metadata_options: Optional[AwsEc2InstanceMetadataOptionsModel] = Field(
        default=None, alias="MetadataOptions"
    )


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsModel(BaseModel):
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    ebs: Optional[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsModel] = Field(
        default=None, alias="Ebs"
    )
    no_device: Optional[str] = Field(default=None, alias="NoDevice")
    virtual_name: Optional[str] = Field(default=None, alias="VirtualName")


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsModel(BaseModel):
    capacity_reservation_preference: Optional[str] = Field(
        default=None, alias="CapacityReservationPreference"
    )
    capacity_reservation_target: Optional[
        AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsModel
    ] = Field(default=None, alias="CapacityReservationTarget")


class AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsModel(BaseModel):
    market_type: Optional[str] = Field(default=None, alias="MarketType")
    spot_options: Optional[
        AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsModel
    ] = Field(default=None, alias="SpotOptions")


class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsModel(BaseModel):
    accelerator_count: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsModel
    ] = Field(default=None, alias="AcceleratorCount")
    accelerator_manufacturers: Optional[Sequence[str]] = Field(
        default=None, alias="AcceleratorManufacturers"
    )
    accelerator_names: Optional[Sequence[str]] = Field(
        default=None, alias="AcceleratorNames"
    )
    accelerator_total_memory_mi_b: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsModel
    ] = Field(default=None, alias="AcceleratorTotalMemoryMiB")
    accelerator_types: Optional[Sequence[str]] = Field(
        default=None, alias="AcceleratorTypes"
    )
    bare_metal: Optional[str] = Field(default=None, alias="BareMetal")
    baseline_ebs_bandwidth_mbps: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsModel
    ] = Field(default=None, alias="BaselineEbsBandwidthMbps")
    burstable_performance: Optional[str] = Field(
        default=None, alias="BurstablePerformance"
    )
    cpu_manufacturers: Optional[Sequence[str]] = Field(
        default=None, alias="CpuManufacturers"
    )
    excluded_instance_types: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedInstanceTypes"
    )
    instance_generations: Optional[Sequence[str]] = Field(
        default=None, alias="InstanceGenerations"
    )
    local_storage: Optional[str] = Field(default=None, alias="LocalStorage")
    local_storage_types: Optional[Sequence[str]] = Field(
        default=None, alias="LocalStorageTypes"
    )
    memory_gi_bper_vcpu: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsModel
    ] = Field(default=None, alias="MemoryGiBPerVCpu")
    memory_mi_b: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsModel
    ] = Field(default=None, alias="MemoryMiB")
    network_interface_count: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsModel
    ] = Field(default=None, alias="NetworkInterfaceCount")
    on_demand_max_price_percentage_over_lowest_price: Optional[int] = Field(
        default=None, alias="OnDemandMaxPricePercentageOverLowestPrice"
    )
    require_hibernate_support: Optional[bool] = Field(
        default=None, alias="RequireHibernateSupport"
    )
    spot_max_price_percentage_over_lowest_price: Optional[int] = Field(
        default=None, alias="SpotMaxPricePercentageOverLowestPrice"
    )
    total_local_storage_gb: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsModel
    ] = Field(default=None, alias="TotalLocalStorageGB")
    vcpu_count: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsModel
    ] = Field(default=None, alias="VCpuCount")


class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsModel(BaseModel):
    associate_carrier_ip_address: Optional[bool] = Field(
        default=None, alias="AssociateCarrierIpAddress"
    )
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="AssociatePublicIpAddress"
    )
    delete_on_termination: Optional[bool] = Field(
        default=None, alias="DeleteOnTermination"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    device_index: Optional[int] = Field(default=None, alias="DeviceIndex")
    groups: Optional[Sequence[str]] = Field(default=None, alias="Groups")
    interface_type: Optional[str] = Field(default=None, alias="InterfaceType")
    ipv4_prefix_count: Optional[int] = Field(default=None, alias="Ipv4PrefixCount")
    ipv4_prefixes: Optional[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsModel]
    ] = Field(default=None, alias="Ipv4Prefixes")
    ipv6_address_count: Optional[int] = Field(default=None, alias="Ipv6AddressCount")
    ipv6_addresses: Optional[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsModel]
    ] = Field(default=None, alias="Ipv6Addresses")
    ipv6_prefix_count: Optional[int] = Field(default=None, alias="Ipv6PrefixCount")
    ipv6_prefixes: Optional[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsModel]
    ] = Field(default=None, alias="Ipv6Prefixes")
    network_card_index: Optional[int] = Field(default=None, alias="NetworkCardIndex")
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")
    private_ip_addresses: Optional[
        Sequence[
            AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsModel
        ]
    ] = Field(default=None, alias="PrivateIpAddresses")
    secondary_private_ip_address_count: Optional[int] = Field(
        default=None, alias="SecondaryPrivateIpAddressCount"
    )
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")


class AwsEc2NetworkAclEntryModel(BaseModel):
    cidr_block: Optional[str] = Field(default=None, alias="CidrBlock")
    egress: Optional[bool] = Field(default=None, alias="Egress")
    icmp_type_code: Optional[IcmpTypeCodeModel] = Field(
        default=None, alias="IcmpTypeCode"
    )
    ipv6_cidr_block: Optional[str] = Field(default=None, alias="Ipv6CidrBlock")
    port_range: Optional[PortRangeFromToModel] = Field(default=None, alias="PortRange")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    rule_action: Optional[str] = Field(default=None, alias="RuleAction")
    rule_number: Optional[int] = Field(default=None, alias="RuleNumber")


class AwsEc2NetworkInterfaceDetailsModel(BaseModel):
    attachment: Optional[AwsEc2NetworkInterfaceAttachmentModel] = Field(
        default=None, alias="Attachment"
    )
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    security_groups: Optional[
        Sequence[AwsEc2NetworkInterfaceSecurityGroupModel]
    ] = Field(default=None, alias="SecurityGroups")
    source_dest_check: Optional[bool] = Field(default=None, alias="SourceDestCheck")
    ip_v6_addresses: Optional[
        Sequence[AwsEc2NetworkInterfaceIpV6AddressDetailModel]
    ] = Field(default=None, alias="IpV6Addresses")
    private_ip_addresses: Optional[
        Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetailModel]
    ] = Field(default=None, alias="PrivateIpAddresses")
    public_dns_name: Optional[str] = Field(default=None, alias="PublicDnsName")
    public_ip: Optional[str] = Field(default=None, alias="PublicIp")


class AwsEc2SecurityGroupIpPermissionModel(BaseModel):
    ip_protocol: Optional[str] = Field(default=None, alias="IpProtocol")
    from_port: Optional[int] = Field(default=None, alias="FromPort")
    to_port: Optional[int] = Field(default=None, alias="ToPort")
    user_id_group_pairs: Optional[
        Sequence[AwsEc2SecurityGroupUserIdGroupPairModel]
    ] = Field(default=None, alias="UserIdGroupPairs")
    ip_ranges: Optional[Sequence[AwsEc2SecurityGroupIpRangeModel]] = Field(
        default=None, alias="IpRanges"
    )
    ipv6_ranges: Optional[Sequence[AwsEc2SecurityGroupIpv6RangeModel]] = Field(
        default=None, alias="Ipv6Ranges"
    )
    prefix_list_ids: Optional[Sequence[AwsEc2SecurityGroupPrefixListIdModel]] = Field(
        default=None, alias="PrefixListIds"
    )


class AwsEc2SubnetDetailsModel(BaseModel):
    assign_ipv6_address_on_creation: Optional[bool] = Field(
        default=None, alias="AssignIpv6AddressOnCreation"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    availability_zone_id: Optional[str] = Field(
        default=None, alias="AvailabilityZoneId"
    )
    available_ip_address_count: Optional[int] = Field(
        default=None, alias="AvailableIpAddressCount"
    )
    cidr_block: Optional[str] = Field(default=None, alias="CidrBlock")
    default_for_az: Optional[bool] = Field(default=None, alias="DefaultForAz")
    map_public_ip_on_launch: Optional[bool] = Field(
        default=None, alias="MapPublicIpOnLaunch"
    )
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    state: Optional[str] = Field(default=None, alias="State")
    subnet_arn: Optional[str] = Field(default=None, alias="SubnetArn")
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    ipv6_cidr_block_association_set: Optional[
        Sequence[Ipv6CidrBlockAssociationModel]
    ] = Field(default=None, alias="Ipv6CidrBlockAssociationSet")


class AwsEc2VolumeDetailsModel(BaseModel):
    create_time: Optional[str] = Field(default=None, alias="CreateTime")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    size: Optional[int] = Field(default=None, alias="Size")
    snapshot_id: Optional[str] = Field(default=None, alias="SnapshotId")
    status: Optional[str] = Field(default=None, alias="Status")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    attachments: Optional[Sequence[AwsEc2VolumeAttachmentModel]] = Field(
        default=None, alias="Attachments"
    )
    volume_id: Optional[str] = Field(default=None, alias="VolumeId")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    volume_scan_status: Optional[str] = Field(default=None, alias="VolumeScanStatus")


class AwsEc2VpcDetailsModel(BaseModel):
    cidr_block_association_set: Optional[Sequence[CidrBlockAssociationModel]] = Field(
        default=None, alias="CidrBlockAssociationSet"
    )
    ipv6_cidr_block_association_set: Optional[
        Sequence[Ipv6CidrBlockAssociationModel]
    ] = Field(default=None, alias="Ipv6CidrBlockAssociationSet")
    dhcp_options_id: Optional[str] = Field(default=None, alias="DhcpOptionsId")
    state: Optional[str] = Field(default=None, alias="State")


class AwsEc2VpcEndpointServiceDetailsModel(BaseModel):
    acceptance_required: Optional[bool] = Field(
        default=None, alias="AcceptanceRequired"
    )
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    base_endpoint_dns_names: Optional[Sequence[str]] = Field(
        default=None, alias="BaseEndpointDnsNames"
    )
    manages_vpc_endpoints: Optional[bool] = Field(
        default=None, alias="ManagesVpcEndpoints"
    )
    gateway_load_balancer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="GatewayLoadBalancerArns"
    )
    network_load_balancer_arns: Optional[Sequence[str]] = Field(
        default=None, alias="NetworkLoadBalancerArns"
    )
    private_dns_name: Optional[str] = Field(default=None, alias="PrivateDnsName")
    service_id: Optional[str] = Field(default=None, alias="ServiceId")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    service_state: Optional[str] = Field(default=None, alias="ServiceState")
    service_type: Optional[
        Sequence[AwsEc2VpcEndpointServiceServiceTypeDetailsModel]
    ] = Field(default=None, alias="ServiceType")


class AwsEc2VpcPeeringConnectionVpcInfoDetailsModel(BaseModel):
    cidr_block: Optional[str] = Field(default=None, alias="CidrBlock")
    cidr_block_set: Optional[Sequence[VpcInfoCidrBlockSetDetailsModel]] = Field(
        default=None, alias="CidrBlockSet"
    )
    ipv6_cidr_block_set: Optional[
        Sequence[VpcInfoIpv6CidrBlockSetDetailsModel]
    ] = Field(default=None, alias="Ipv6CidrBlockSet")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    peering_options: Optional[VpcInfoPeeringOptionsDetailsModel] = Field(
        default=None, alias="PeeringOptions"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class AwsEc2VpnConnectionOptionsDetailsModel(BaseModel):
    static_routes_only: Optional[bool] = Field(default=None, alias="StaticRoutesOnly")
    tunnel_options: Optional[
        Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsModel]
    ] = Field(default=None, alias="TunnelOptions")


class AwsEcrRepositoryDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    image_scanning_configuration: Optional[
        AwsEcrRepositoryImageScanningConfigurationDetailsModel
    ] = Field(default=None, alias="ImageScanningConfiguration")
    image_tag_mutability: Optional[str] = Field(
        default=None, alias="ImageTagMutability"
    )
    lifecycle_policy: Optional[AwsEcrRepositoryLifecyclePolicyDetailsModel] = Field(
        default=None, alias="LifecyclePolicy"
    )
    repository_name: Optional[str] = Field(default=None, alias="RepositoryName")
    repository_policy_text: Optional[str] = Field(
        default=None, alias="RepositoryPolicyText"
    )


class AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsModel(BaseModel):
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    log_configuration: Optional[
        AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsModel
    ] = Field(default=None, alias="LogConfiguration")
    logging: Optional[str] = Field(default=None, alias="Logging")


class AwsEcsContainerDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    image: Optional[str] = Field(default=None, alias="Image")
    mount_points: Optional[Sequence[AwsMountPointModel]] = Field(
        default=None, alias="MountPoints"
    )
    privileged: Optional[bool] = Field(default=None, alias="Privileged")


class AwsEcsServiceDeploymentConfigurationDetailsModel(BaseModel):
    deployment_circuit_breaker: Optional[
        AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsModel
    ] = Field(default=None, alias="DeploymentCircuitBreaker")
    maximum_percent: Optional[int] = Field(default=None, alias="MaximumPercent")
    minimum_healthy_percent: Optional[int] = Field(
        default=None, alias="MinimumHealthyPercent"
    )


class AwsEcsServiceNetworkConfigurationDetailsModel(BaseModel):
    aws_vpc_configuration: Optional[
        AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsModel
    ] = Field(default=None, alias="AwsVpcConfiguration")


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsModel(BaseModel):
    capabilities: Optional[
        AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsModel
    ] = Field(default=None, alias="Capabilities")
    devices: Optional[
        Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsModel
        ]
    ] = Field(default=None, alias="Devices")
    init_process_enabled: Optional[bool] = Field(
        default=None, alias="InitProcessEnabled"
    )
    max_swap: Optional[int] = Field(default=None, alias="MaxSwap")
    shared_memory_size: Optional[int] = Field(default=None, alias="SharedMemorySize")
    swappiness: Optional[int] = Field(default=None, alias="Swappiness")
    tmpfs: Optional[
        Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsModel
        ]
    ] = Field(default=None, alias="Tmpfs")


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsModel(BaseModel):
    log_driver: Optional[str] = Field(default=None, alias="LogDriver")
    options: Optional[Mapping[str, str]] = Field(default=None, alias="Options")
    secret_options: Optional[
        Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsModel
        ]
    ] = Field(default=None, alias="SecretOptions")


class AwsEcsTaskDefinitionProxyConfigurationDetailsModel(BaseModel):
    container_name: Optional[str] = Field(default=None, alias="ContainerName")
    proxy_configuration_properties: Optional[
        Sequence[
            AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsModel
        ]
    ] = Field(default=None, alias="ProxyConfigurationProperties")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsModel(BaseModel):
    authorization_config: Optional[
        AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsModel
    ] = Field(default=None, alias="AuthorizationConfig")
    filesystem_id: Optional[str] = Field(default=None, alias="FilesystemId")
    root_directory: Optional[str] = Field(default=None, alias="RootDirectory")
    transit_encryption: Optional[str] = Field(default=None, alias="TransitEncryption")
    transit_encryption_port: Optional[int] = Field(
        default=None, alias="TransitEncryptionPort"
    )


class AwsEcsTaskVolumeDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    host: Optional[AwsEcsTaskVolumeHostDetailsModel] = Field(default=None, alias="Host")


class AwsEfsAccessPointRootDirectoryDetailsModel(BaseModel):
    creation_info: Optional[
        AwsEfsAccessPointRootDirectoryCreationInfoDetailsModel
    ] = Field(default=None, alias="CreationInfo")
    path: Optional[str] = Field(default=None, alias="Path")


class AwsEksClusterLoggingDetailsModel(BaseModel):
    cluster_logging: Optional[
        Sequence[AwsEksClusterLoggingClusterLoggingDetailsModel]
    ] = Field(default=None, alias="ClusterLogging")


class AwsElasticBeanstalkEnvironmentDetailsModel(BaseModel):
    application_name: Optional[str] = Field(default=None, alias="ApplicationName")
    cname: Optional[str] = Field(default=None, alias="Cname")
    date_created: Optional[str] = Field(default=None, alias="DateCreated")
    date_updated: Optional[str] = Field(default=None, alias="DateUpdated")
    description: Optional[str] = Field(default=None, alias="Description")
    endpoint_url: Optional[str] = Field(default=None, alias="EndpointUrl")
    environment_arn: Optional[str] = Field(default=None, alias="EnvironmentArn")
    environment_id: Optional[str] = Field(default=None, alias="EnvironmentId")
    environment_links: Optional[
        Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLinkModel]
    ] = Field(default=None, alias="EnvironmentLinks")
    environment_name: Optional[str] = Field(default=None, alias="EnvironmentName")
    option_settings: Optional[
        Sequence[AwsElasticBeanstalkEnvironmentOptionSettingModel]
    ] = Field(default=None, alias="OptionSettings")
    platform_arn: Optional[str] = Field(default=None, alias="PlatformArn")
    solution_stack_name: Optional[str] = Field(default=None, alias="SolutionStackName")
    status: Optional[str] = Field(default=None, alias="Status")
    tier: Optional[AwsElasticBeanstalkEnvironmentTierModel] = Field(
        default=None, alias="Tier"
    )
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")


class AwsElasticsearchDomainElasticsearchClusterConfigDetailsModel(BaseModel):
    dedicated_master_count: Optional[int] = Field(
        default=None, alias="DedicatedMasterCount"
    )
    dedicated_master_enabled: Optional[bool] = Field(
        default=None, alias="DedicatedMasterEnabled"
    )
    dedicated_master_type: Optional[str] = Field(
        default=None, alias="DedicatedMasterType"
    )
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    zone_awareness_config: Optional[
        AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsModel
    ] = Field(default=None, alias="ZoneAwarenessConfig")
    zone_awareness_enabled: Optional[bool] = Field(
        default=None, alias="ZoneAwarenessEnabled"
    )


class AwsElasticsearchDomainLogPublishingOptionsModel(BaseModel):
    index_slow_logs: Optional[
        AwsElasticsearchDomainLogPublishingOptionsLogConfigModel
    ] = Field(default=None, alias="IndexSlowLogs")
    search_slow_logs: Optional[
        AwsElasticsearchDomainLogPublishingOptionsLogConfigModel
    ] = Field(default=None, alias="SearchSlowLogs")
    audit_logs: Optional[
        AwsElasticsearchDomainLogPublishingOptionsLogConfigModel
    ] = Field(default=None, alias="AuditLogs")


class AwsElbLoadBalancerPoliciesModel(BaseModel):
    app_cookie_stickiness_policies: Optional[
        Sequence[AwsElbAppCookieStickinessPolicyModel]
    ] = Field(default=None, alias="AppCookieStickinessPolicies")
    lb_cookie_stickiness_policies: Optional[
        Sequence[AwsElbLbCookieStickinessPolicyModel]
    ] = Field(default=None, alias="LbCookieStickinessPolicies")
    other_policies: Optional[Sequence[str]] = Field(default=None, alias="OtherPolicies")


class AwsElbLoadBalancerAttributesModel(BaseModel):
    access_log: Optional[AwsElbLoadBalancerAccessLogModel] = Field(
        default=None, alias="AccessLog"
    )
    connection_draining: Optional[AwsElbLoadBalancerConnectionDrainingModel] = Field(
        default=None, alias="ConnectionDraining"
    )
    connection_settings: Optional[AwsElbLoadBalancerConnectionSettingsModel] = Field(
        default=None, alias="ConnectionSettings"
    )
    cross_zone_load_balancing: Optional[
        AwsElbLoadBalancerCrossZoneLoadBalancingModel
    ] = Field(default=None, alias="CrossZoneLoadBalancing")
    additional_attributes: Optional[
        Sequence[AwsElbLoadBalancerAdditionalAttributeModel]
    ] = Field(default=None, alias="AdditionalAttributes")


class AwsElbLoadBalancerListenerDescriptionModel(BaseModel):
    listener: Optional[AwsElbLoadBalancerListenerModel] = Field(
        default=None, alias="Listener"
    )
    policy_names: Optional[Sequence[str]] = Field(default=None, alias="PolicyNames")


class AwsElbv2LoadBalancerDetailsModel(BaseModel):
    availability_zones: Optional[Sequence[AvailabilityZoneModel]] = Field(
        default=None, alias="AvailabilityZones"
    )
    canonical_hosted_zone_id: Optional[str] = Field(
        default=None, alias="CanonicalHostedZoneId"
    )
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    ip_address_type: Optional[str] = Field(default=None, alias="IpAddressType")
    scheme: Optional[str] = Field(default=None, alias="Scheme")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    state: Optional[LoadBalancerStateModel] = Field(default=None, alias="State")
    type: Optional[str] = Field(default=None, alias="Type")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    load_balancer_attributes: Optional[
        Sequence[AwsElbv2LoadBalancerAttributeModel]
    ] = Field(default=None, alias="LoadBalancerAttributes")


class AwsIamAccessKeySessionContextModel(BaseModel):
    attributes: Optional[AwsIamAccessKeySessionContextAttributesModel] = Field(
        default=None, alias="Attributes"
    )
    session_issuer: Optional[AwsIamAccessKeySessionContextSessionIssuerModel] = Field(
        default=None, alias="SessionIssuer"
    )


class AwsIamGroupDetailsModel(BaseModel):
    attached_managed_policies: Optional[
        Sequence[AwsIamAttachedManagedPolicyModel]
    ] = Field(default=None, alias="AttachedManagedPolicies")
    create_date: Optional[str] = Field(default=None, alias="CreateDate")
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_policy_list: Optional[Sequence[AwsIamGroupPolicyModel]] = Field(
        default=None, alias="GroupPolicyList"
    )
    path: Optional[str] = Field(default=None, alias="Path")


class AwsIamInstanceProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    create_date: Optional[str] = Field(default=None, alias="CreateDate")
    instance_profile_id: Optional[str] = Field(default=None, alias="InstanceProfileId")
    instance_profile_name: Optional[str] = Field(
        default=None, alias="InstanceProfileName"
    )
    path: Optional[str] = Field(default=None, alias="Path")
    roles: Optional[Sequence[AwsIamInstanceProfileRoleModel]] = Field(
        default=None, alias="Roles"
    )


class AwsIamPolicyDetailsModel(BaseModel):
    attachment_count: Optional[int] = Field(default=None, alias="AttachmentCount")
    create_date: Optional[str] = Field(default=None, alias="CreateDate")
    default_version_id: Optional[str] = Field(default=None, alias="DefaultVersionId")
    description: Optional[str] = Field(default=None, alias="Description")
    is_attachable: Optional[bool] = Field(default=None, alias="IsAttachable")
    path: Optional[str] = Field(default=None, alias="Path")
    permissions_boundary_usage_count: Optional[int] = Field(
        default=None, alias="PermissionsBoundaryUsageCount"
    )
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_version_list: Optional[Sequence[AwsIamPolicyVersionModel]] = Field(
        default=None, alias="PolicyVersionList"
    )
    update_date: Optional[str] = Field(default=None, alias="UpdateDate")


class AwsIamUserDetailsModel(BaseModel):
    attached_managed_policies: Optional[
        Sequence[AwsIamAttachedManagedPolicyModel]
    ] = Field(default=None, alias="AttachedManagedPolicies")
    create_date: Optional[str] = Field(default=None, alias="CreateDate")
    group_list: Optional[Sequence[str]] = Field(default=None, alias="GroupList")
    path: Optional[str] = Field(default=None, alias="Path")
    permissions_boundary: Optional[AwsIamPermissionsBoundaryModel] = Field(
        default=None, alias="PermissionsBoundary"
    )
    user_id: Optional[str] = Field(default=None, alias="UserId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    user_policy_list: Optional[Sequence[AwsIamUserPolicyModel]] = Field(
        default=None, alias="UserPolicyList"
    )


class AwsKinesisStreamDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    stream_encryption: Optional[AwsKinesisStreamStreamEncryptionDetailsModel] = Field(
        default=None, alias="StreamEncryption"
    )
    shard_count: Optional[int] = Field(default=None, alias="ShardCount")
    retention_period_hours: Optional[int] = Field(
        default=None, alias="RetentionPeriodHours"
    )


class AwsLambdaFunctionEnvironmentModel(BaseModel):
    variables: Optional[Mapping[str, str]] = Field(default=None, alias="Variables")
    error: Optional[AwsLambdaFunctionEnvironmentErrorModel] = Field(
        default=None, alias="Error"
    )


class AwsNetworkFirewallFirewallDetailsModel(BaseModel):
    delete_protection: Optional[bool] = Field(default=None, alias="DeleteProtection")
    description: Optional[str] = Field(default=None, alias="Description")
    firewall_arn: Optional[str] = Field(default=None, alias="FirewallArn")
    firewall_id: Optional[str] = Field(default=None, alias="FirewallId")
    firewall_name: Optional[str] = Field(default=None, alias="FirewallName")
    firewall_policy_arn: Optional[str] = Field(default=None, alias="FirewallPolicyArn")
    firewall_policy_change_protection: Optional[bool] = Field(
        default=None, alias="FirewallPolicyChangeProtection"
    )
    subnet_change_protection: Optional[bool] = Field(
        default=None, alias="SubnetChangeProtection"
    )
    subnet_mappings: Optional[
        Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetailsModel]
    ] = Field(default=None, alias="SubnetMappings")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    internal_user_database_enabled: Optional[bool] = Field(
        default=None, alias="InternalUserDatabaseEnabled"
    )
    master_user_options: Optional[
        AwsOpenSearchServiceDomainMasterUserOptionsDetailsModel
    ] = Field(default=None, alias="MasterUserOptions")


class AwsOpenSearchServiceDomainClusterConfigDetailsModel(BaseModel):
    instance_count: Optional[int] = Field(default=None, alias="InstanceCount")
    warm_enabled: Optional[bool] = Field(default=None, alias="WarmEnabled")
    warm_count: Optional[int] = Field(default=None, alias="WarmCount")
    dedicated_master_enabled: Optional[bool] = Field(
        default=None, alias="DedicatedMasterEnabled"
    )
    zone_awareness_config: Optional[
        AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsModel
    ] = Field(default=None, alias="ZoneAwarenessConfig")
    dedicated_master_count: Optional[int] = Field(
        default=None, alias="DedicatedMasterCount"
    )
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    warm_type: Optional[str] = Field(default=None, alias="WarmType")
    zone_awareness_enabled: Optional[bool] = Field(
        default=None, alias="ZoneAwarenessEnabled"
    )
    dedicated_master_type: Optional[str] = Field(
        default=None, alias="DedicatedMasterType"
    )


class AwsOpenSearchServiceDomainLogPublishingOptionsDetailsModel(BaseModel):
    index_slow_logs: Optional[
        AwsOpenSearchServiceDomainLogPublishingOptionModel
    ] = Field(default=None, alias="IndexSlowLogs")
    search_slow_logs: Optional[
        AwsOpenSearchServiceDomainLogPublishingOptionModel
    ] = Field(default=None, alias="SearchSlowLogs")
    audit_logs: Optional[AwsOpenSearchServiceDomainLogPublishingOptionModel] = Field(
        default=None, alias="AuditLogs"
    )


class AwsRdsDbClusterDetailsModel(BaseModel):
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    database_name: Optional[str] = Field(default=None, alias="DatabaseName")
    status: Optional[str] = Field(default=None, alias="Status")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    reader_endpoint: Optional[str] = Field(default=None, alias="ReaderEndpoint")
    custom_endpoints: Optional[Sequence[str]] = Field(
        default=None, alias="CustomEndpoints"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAz")
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    port: Optional[int] = Field(default=None, alias="Port")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    read_replica_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="ReadReplicaIdentifiers"
    )
    vpc_security_groups: Optional[
        Sequence[AwsRdsDbInstanceVpcSecurityGroupModel]
    ] = Field(default=None, alias="VpcSecurityGroups")
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    db_cluster_resource_id: Optional[str] = Field(
        default=None, alias="DbClusterResourceId"
    )
    associated_roles: Optional[Sequence[AwsRdsDbClusterAssociatedRoleModel]] = Field(
        default=None, alias="AssociatedRoles"
    )
    cluster_create_time: Optional[str] = Field(default=None, alias="ClusterCreateTime")
    enabled_cloud_watch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnabledCloudWatchLogsExports"
    )
    engine_mode: Optional[str] = Field(default=None, alias="EngineMode")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    http_endpoint_enabled: Optional[bool] = Field(
        default=None, alias="HttpEndpointEnabled"
    )
    activity_stream_status: Optional[str] = Field(
        default=None, alias="ActivityStreamStatus"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    cross_account_clone: Optional[bool] = Field(default=None, alias="CrossAccountClone")
    domain_memberships: Optional[Sequence[AwsRdsDbDomainMembershipModel]] = Field(
        default=None, alias="DomainMemberships"
    )
    db_cluster_parameter_group: Optional[str] = Field(
        default=None, alias="DbClusterParameterGroup"
    )
    db_subnet_group: Optional[str] = Field(default=None, alias="DbSubnetGroup")
    db_cluster_option_group_memberships: Optional[
        Sequence[AwsRdsDbClusterOptionGroupMembershipModel]
    ] = Field(default=None, alias="DbClusterOptionGroupMemberships")
    db_cluster_identifier: Optional[str] = Field(
        default=None, alias="DbClusterIdentifier"
    )
    db_cluster_members: Optional[Sequence[AwsRdsDbClusterMemberModel]] = Field(
        default=None, alias="DbClusterMembers"
    )
    iam_database_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IamDatabaseAuthenticationEnabled"
    )


class AwsRdsDbSnapshotDetailsModel(BaseModel):
    db_snapshot_identifier: Optional[str] = Field(
        default=None, alias="DbSnapshotIdentifier"
    )
    db_instance_identifier: Optional[str] = Field(
        default=None, alias="DbInstanceIdentifier"
    )
    snapshot_create_time: Optional[str] = Field(
        default=None, alias="SnapshotCreateTime"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    status: Optional[str] = Field(default=None, alias="Status")
    port: Optional[int] = Field(default=None, alias="Port")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    instance_create_time: Optional[str] = Field(
        default=None, alias="InstanceCreateTime"
    )
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    snapshot_type: Optional[str] = Field(default=None, alias="SnapshotType")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_name: Optional[str] = Field(default=None, alias="OptionGroupName")
    percent_progress: Optional[int] = Field(default=None, alias="PercentProgress")
    source_region: Optional[str] = Field(default=None, alias="SourceRegion")
    source_db_snapshot_identifier: Optional[str] = Field(
        default=None, alias="SourceDbSnapshotIdentifier"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    iam_database_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IamDatabaseAuthenticationEnabled"
    )
    processor_features: Optional[Sequence[AwsRdsDbProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")


class AwsRdsDbPendingModifiedValuesModel(BaseModel):
    db_instance_class: Optional[str] = Field(default=None, alias="DbInstanceClass")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    master_user_password: Optional[str] = Field(
        default=None, alias="MasterUserPassword"
    )
    port: Optional[int] = Field(default=None, alias="Port")
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    multi_az: Optional[bool] = Field(default=None, alias="MultiAZ")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    db_instance_identifier: Optional[str] = Field(
        default=None, alias="DbInstanceIdentifier"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    ca_certificate_identifier: Optional[str] = Field(
        default=None, alias="CaCertificateIdentifier"
    )
    db_subnet_group_name: Optional[str] = Field(default=None, alias="DbSubnetGroupName")
    pending_cloud_watch_logs_exports: Optional[
        AwsRdsPendingCloudWatchLogsExportsModel
    ] = Field(default=None, alias="PendingCloudWatchLogsExports")
    processor_features: Optional[Sequence[AwsRdsDbProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )


class AwsRdsDbSecurityGroupDetailsModel(BaseModel):
    db_security_group_arn: Optional[str] = Field(
        default=None, alias="DbSecurityGroupArn"
    )
    db_security_group_description: Optional[str] = Field(
        default=None, alias="DbSecurityGroupDescription"
    )
    db_security_group_name: Optional[str] = Field(
        default=None, alias="DbSecurityGroupName"
    )
    ec2_security_groups: Optional[
        Sequence[AwsRdsDbSecurityGroupEc2SecurityGroupModel]
    ] = Field(default=None, alias="Ec2SecurityGroups")
    ip_ranges: Optional[Sequence[AwsRdsDbSecurityGroupIpRangeModel]] = Field(
        default=None, alias="IpRanges"
    )
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class AwsRdsDbSubnetGroupSubnetModel(BaseModel):
    subnet_identifier: Optional[str] = Field(default=None, alias="SubnetIdentifier")
    subnet_availability_zone: Optional[
        AwsRdsDbSubnetGroupSubnetAvailabilityZoneModel
    ] = Field(default=None, alias="SubnetAvailabilityZone")
    subnet_status: Optional[str] = Field(default=None, alias="SubnetStatus")


class AwsRedshiftClusterClusterParameterGroupModel(BaseModel):
    cluster_parameter_status_list: Optional[
        Sequence[AwsRedshiftClusterClusterParameterStatusModel]
    ] = Field(default=None, alias="ClusterParameterStatusList")
    parameter_apply_status: Optional[str] = Field(
        default=None, alias="ParameterApplyStatus"
    )
    parameter_group_name: Optional[str] = Field(
        default=None, alias="ParameterGroupName"
    )


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsModel(
    BaseModel
):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[
        AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsModel
    ] = Field(default=None, alias="Tag")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsS3BucketNotificationConfigurationS3KeyFilterModel(BaseModel):
    filter_rules: Optional[
        Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRuleModel]
    ] = Field(default=None, alias="FilterRules")


class AwsS3BucketServerSideEncryptionRuleModel(BaseModel):
    apply_server_side_encryption_by_default: Optional[
        AwsS3BucketServerSideEncryptionByDefaultModel
    ] = Field(default=None, alias="ApplyServerSideEncryptionByDefault")


class AwsS3BucketWebsiteConfigurationRoutingRuleModel(BaseModel):
    condition: Optional[
        AwsS3BucketWebsiteConfigurationRoutingRuleConditionModel
    ] = Field(default=None, alias="Condition")
    redirect: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleRedirectModel] = Field(
        default=None, alias="Redirect"
    )


class AwsSageMakerNotebookInstanceDetailsModel(BaseModel):
    accelerator_types: Optional[Sequence[str]] = Field(
        default=None, alias="AcceleratorTypes"
    )
    additional_code_repositories: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalCodeRepositories"
    )
    default_code_repository: Optional[str] = Field(
        default=None, alias="DefaultCodeRepository"
    )
    direct_internet_access: Optional[str] = Field(
        default=None, alias="DirectInternetAccess"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    instance_metadata_service_configuration: Optional[
        AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsModel
    ] = Field(default=None, alias="InstanceMetadataServiceConfiguration")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    notebook_instance_arn: Optional[str] = Field(
        default=None, alias="NotebookInstanceArn"
    )
    notebook_instance_lifecycle_config_name: Optional[str] = Field(
        default=None, alias="NotebookInstanceLifecycleConfigName"
    )
    notebook_instance_name: Optional[str] = Field(
        default=None, alias="NotebookInstanceName"
    )
    notebook_instance_status: Optional[str] = Field(
        default=None, alias="NotebookInstanceStatus"
    )
    platform_identifier: Optional[str] = Field(default=None, alias="PlatformIdentifier")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    root_access: Optional[str] = Field(default=None, alias="RootAccess")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    url: Optional[str] = Field(default=None, alias="Url")
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")


class AwsSecretsManagerSecretDetailsModel(BaseModel):
    rotation_rules: Optional[AwsSecretsManagerSecretRotationRulesModel] = Field(
        default=None, alias="RotationRules"
    )
    rotation_occurred_within_frequency: Optional[bool] = Field(
        default=None, alias="RotationOccurredWithinFrequency"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    rotation_enabled: Optional[bool] = Field(default=None, alias="RotationEnabled")
    rotation_lambda_arn: Optional[str] = Field(default=None, alias="RotationLambdaArn")
    deleted: Optional[bool] = Field(default=None, alias="Deleted")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class BatchUpdateFindingsUnprocessedFindingModel(BaseModel):
    finding_identifier: AwsSecurityFindingIdentifierModel = Field(
        alias="FindingIdentifier"
    )
    error_code: str = Field(alias="ErrorCode")
    error_message: str = Field(alias="ErrorMessage")


class AwsSnsTopicDetailsModel(BaseModel):
    kms_master_key_id: Optional[str] = Field(default=None, alias="KmsMasterKeyId")
    subscription: Optional[Sequence[AwsSnsTopicSubscriptionModel]] = Field(
        default=None, alias="Subscription"
    )
    topic_name: Optional[str] = Field(default=None, alias="TopicName")
    owner: Optional[str] = Field(default=None, alias="Owner")
    sqs_success_feedback_role_arn: Optional[str] = Field(
        default=None, alias="SqsSuccessFeedbackRoleArn"
    )
    sqs_failure_feedback_role_arn: Optional[str] = Field(
        default=None, alias="SqsFailureFeedbackRoleArn"
    )
    application_success_feedback_role_arn: Optional[str] = Field(
        default=None, alias="ApplicationSuccessFeedbackRoleArn"
    )
    firehose_success_feedback_role_arn: Optional[str] = Field(
        default=None, alias="FirehoseSuccessFeedbackRoleArn"
    )
    firehose_failure_feedback_role_arn: Optional[str] = Field(
        default=None, alias="FirehoseFailureFeedbackRoleArn"
    )
    http_success_feedback_role_arn: Optional[str] = Field(
        default=None, alias="HttpSuccessFeedbackRoleArn"
    )
    http_failure_feedback_role_arn: Optional[str] = Field(
        default=None, alias="HttpFailureFeedbackRoleArn"
    )


class AwsSsmPatchModel(BaseModel):
    compliance_summary: Optional[AwsSsmComplianceSummaryModel] = Field(
        default=None, alias="ComplianceSummary"
    )


class AwsWafRateBasedRuleDetailsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    name: Optional[str] = Field(default=None, alias="Name")
    rate_key: Optional[str] = Field(default=None, alias="RateKey")
    rate_limit: Optional[int] = Field(default=None, alias="RateLimit")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    match_predicates: Optional[
        Sequence[AwsWafRateBasedRuleMatchPredicateModel]
    ] = Field(default=None, alias="MatchPredicates")


class AwsWafRegionalRateBasedRuleDetailsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    name: Optional[str] = Field(default=None, alias="Name")
    rate_key: Optional[str] = Field(default=None, alias="RateKey")
    rate_limit: Optional[int] = Field(default=None, alias="RateLimit")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    match_predicates: Optional[
        Sequence[AwsWafRegionalRateBasedRuleMatchPredicateModel]
    ] = Field(default=None, alias="MatchPredicates")


class AwsWafRegionalRuleDetailsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    name: Optional[str] = Field(default=None, alias="Name")
    predicate_list: Optional[
        Sequence[AwsWafRegionalRulePredicateListDetailsModel]
    ] = Field(default=None, alias="PredicateList")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")


class AwsWafRegionalRuleGroupRulesDetailsModel(BaseModel):
    action: Optional[AwsWafRegionalRuleGroupRulesActionDetailsModel] = Field(
        default=None, alias="Action"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRegionalWebAclRulesListDetailsModel(BaseModel):
    action: Optional[AwsWafRegionalWebAclRulesListActionDetailsModel] = Field(
        default=None, alias="Action"
    )
    override_action: Optional[
        AwsWafRegionalWebAclRulesListOverrideActionDetailsModel
    ] = Field(default=None, alias="OverrideAction")
    priority: Optional[int] = Field(default=None, alias="Priority")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafRuleDetailsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    name: Optional[str] = Field(default=None, alias="Name")
    predicate_list: Optional[Sequence[AwsWafRulePredicateListDetailsModel]] = Field(
        default=None, alias="PredicateList"
    )
    rule_id: Optional[str] = Field(default=None, alias="RuleId")


class AwsWafRuleGroupRulesDetailsModel(BaseModel):
    action: Optional[AwsWafRuleGroupRulesActionDetailsModel] = Field(
        default=None, alias="Action"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafWebAclRuleModel(BaseModel):
    action: Optional[WafActionModel] = Field(default=None, alias="Action")
    excluded_rules: Optional[Sequence[WafExcludedRuleModel]] = Field(
        default=None, alias="ExcludedRules"
    )
    override_action: Optional[WafOverrideActionModel] = Field(
        default=None, alias="OverrideAction"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafv2CustomRequestHandlingDetailsModel(BaseModel):
    insert_headers: Optional[Sequence[AwsWafv2CustomHttpHeaderModel]] = Field(
        default=None, alias="InsertHeaders"
    )


class AwsWafv2CustomResponseDetailsModel(BaseModel):
    custom_response_body_key: Optional[str] = Field(
        default=None, alias="CustomResponseBodyKey"
    )
    response_code: Optional[int] = Field(default=None, alias="ResponseCode")
    response_headers: Optional[Sequence[AwsWafv2CustomHttpHeaderModel]] = Field(
        default=None, alias="ResponseHeaders"
    )


class AwsWafv2WebAclCaptchaConfigDetailsModel(BaseModel):
    immunity_time_property: Optional[
        AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsModel
    ] = Field(default=None, alias="ImmunityTimeProperty")


class CreateActionTargetResponseModel(BaseModel):
    action_target_arn: str = Field(alias="ActionTargetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFindingAggregatorResponseModel(BaseModel):
    finding_aggregator_arn: str = Field(alias="FindingAggregatorArn")
    finding_aggregation_region: str = Field(alias="FindingAggregationRegion")
    region_linking_mode: str = Field(alias="RegionLinkingMode")
    regions: List[str] = Field(alias="Regions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInsightResponseModel(BaseModel):
    insight_arn: str = Field(alias="InsightArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteActionTargetResponseModel(BaseModel):
    action_target_arn: str = Field(alias="ActionTargetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInsightResponseModel(BaseModel):
    insight_arn: str = Field(alias="InsightArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeActionTargetsResponseModel(BaseModel):
    action_targets: List[ActionTargetModel] = Field(alias="ActionTargets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHubResponseModel(BaseModel):
    hub_arn: str = Field(alias="HubArn")
    subscribed_at: str = Field(alias="SubscribedAt")
    auto_enable_controls: bool = Field(alias="AutoEnableControls")
    control_finding_generator: Literal["SECURITY_CONTROL", "STANDARD_CONTROL"] = Field(
        alias="ControlFindingGenerator"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationConfigurationResponseModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")
    member_account_limit_reached: bool = Field(alias="MemberAccountLimitReached")
    auto_enable_standards: Literal["DEFAULT", "NONE"] = Field(
        alias="AutoEnableStandards"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableImportFindingsForProductResponseModel(BaseModel):
    product_subscription_arn: str = Field(alias="ProductSubscriptionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFindingAggregatorResponseModel(BaseModel):
    finding_aggregator_arn: str = Field(alias="FindingAggregatorArn")
    finding_aggregation_region: str = Field(alias="FindingAggregationRegion")
    region_linking_mode: str = Field(alias="RegionLinkingMode")
    regions: List[str] = Field(alias="Regions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInvitationsCountResponseModel(BaseModel):
    invitations_count: int = Field(alias="InvitationsCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEnabledProductsForImportResponseModel(BaseModel):
    product_subscriptions: List[str] = Field(alias="ProductSubscriptions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrganizationAdminAccountsResponseModel(BaseModel):
    admin_accounts: List[AdminAccountModel] = Field(alias="AdminAccounts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFindingAggregatorResponseModel(BaseModel):
    finding_aggregator_arn: str = Field(alias="FindingAggregatorArn")
    finding_aggregation_region: str = Field(alias="FindingAggregationRegion")
    region_linking_mode: str = Field(alias="RegionLinkingMode")
    regions: List[str] = Field(alias="Regions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchEnableStandardsRequestModel(BaseModel):
    standards_subscription_requests: Sequence[
        StandardsSubscriptionRequestModel
    ] = Field(alias="StandardsSubscriptionRequests")


class BatchGetSecurityControlsResponseModel(BaseModel):
    security_controls: List[SecurityControlModel] = Field(alias="SecurityControls")
    unprocessed_ids: List[UnprocessedSecurityControlModel] = Field(
        alias="UnprocessedIds"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetStandardsControlAssociationsRequestModel(BaseModel):
    standards_control_association_ids: Sequence[
        StandardsControlAssociationIdModel
    ] = Field(alias="StandardsControlAssociationIds")


class UnprocessedStandardsControlAssociationModel(BaseModel):
    standards_control_association_id: StandardsControlAssociationIdModel = Field(
        alias="StandardsControlAssociationId"
    )
    error_code: Literal[
        "ACCESS_DENIED", "INVALID_INPUT", "LIMIT_EXCEEDED", "NOT_FOUND"
    ] = Field(alias="ErrorCode")
    error_reason: Optional[str] = Field(default=None, alias="ErrorReason")


class BatchImportFindingsResponseModel(BaseModel):
    failed_count: int = Field(alias="FailedCount")
    success_count: int = Field(alias="SuccessCount")
    failed_findings: List[ImportFindingsErrorModel] = Field(alias="FailedFindings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateFindingsRequestModel(BaseModel):
    finding_identifiers: Sequence[AwsSecurityFindingIdentifierModel] = Field(
        alias="FindingIdentifiers"
    )
    note: Optional[NoteUpdateModel] = Field(default=None, alias="Note")
    severity: Optional[SeverityUpdateModel] = Field(default=None, alias="Severity")
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="VerificationState")
    confidence: Optional[int] = Field(default=None, alias="Confidence")
    criticality: Optional[int] = Field(default=None, alias="Criticality")
    types: Optional[Sequence[str]] = Field(default=None, alias="Types")
    user_defined_fields: Optional[Mapping[str, str]] = Field(
        default=None, alias="UserDefinedFields"
    )
    workflow: Optional[WorkflowUpdateModel] = Field(default=None, alias="Workflow")
    related_findings: Optional[Sequence[RelatedFindingModel]] = Field(
        default=None, alias="RelatedFindings"
    )


class BatchUpdateStandardsControlAssociationsRequestModel(BaseModel):
    standards_control_association_updates: Sequence[
        StandardsControlAssociationUpdateModel
    ] = Field(alias="StandardsControlAssociationUpdates")


class UnprocessedStandardsControlAssociationUpdateModel(BaseModel):
    standards_control_association_update: StandardsControlAssociationUpdateModel = (
        Field(alias="StandardsControlAssociationUpdate")
    )
    error_code: Literal[
        "ACCESS_DENIED", "INVALID_INPUT", "LIMIT_EXCEEDED", "NOT_FOUND"
    ] = Field(alias="ErrorCode")
    error_reason: Optional[str] = Field(default=None, alias="ErrorReason")


class ComplianceModel(BaseModel):
    status: Optional[Literal["FAILED", "NOT_AVAILABLE", "PASSED", "WARNING"]] = Field(
        default=None, alias="Status"
    )
    related_requirements: Optional[Sequence[str]] = Field(
        default=None, alias="RelatedRequirements"
    )
    status_reasons: Optional[Sequence[StatusReasonModel]] = Field(
        default=None, alias="StatusReasons"
    )
    security_control_id: Optional[str] = Field(default=None, alias="SecurityControlId")
    associated_standards: Optional[Sequence[AssociatedStandardModel]] = Field(
        default=None, alias="AssociatedStandards"
    )


class ContainerDetailsModel(BaseModel):
    container_runtime: Optional[str] = Field(default=None, alias="ContainerRuntime")
    name: Optional[str] = Field(default=None, alias="Name")
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    image_name: Optional[str] = Field(default=None, alias="ImageName")
    launched_at: Optional[str] = Field(default=None, alias="LaunchedAt")
    volume_mounts: Optional[Sequence[VolumeMountModel]] = Field(
        default=None, alias="VolumeMounts"
    )
    privileged: Optional[bool] = Field(default=None, alias="Privileged")


class CreateMembersResponseModel(BaseModel):
    unprocessed_accounts: List[ResultModel] = Field(alias="UnprocessedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeclineInvitationsResponseModel(BaseModel):
    unprocessed_accounts: List[ResultModel] = Field(alias="UnprocessedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInvitationsResponseModel(BaseModel):
    unprocessed_accounts: List[ResultModel] = Field(alias="UnprocessedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMembersResponseModel(BaseModel):
    unprocessed_accounts: List[ResultModel] = Field(alias="UnprocessedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InviteMembersResponseModel(BaseModel):
    unprocessed_accounts: List[ResultModel] = Field(alias="UnprocessedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DateFilterModel(BaseModel):
    start: Optional[str] = Field(default=None, alias="Start")
    end: Optional[str] = Field(default=None, alias="End")
    date_range: Optional[DateRangeModel] = Field(default=None, alias="DateRange")


class DescribeActionTargetsRequestDescribeActionTargetsPaginateModel(BaseModel):
    action_target_arns: Optional[Sequence[str]] = Field(
        default=None, alias="ActionTargetArns"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeProductsRequestDescribeProductsPaginateModel(BaseModel):
    product_arn: Optional[str] = Field(default=None, alias="ProductArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStandardsControlsRequestDescribeStandardsControlsPaginateModel(BaseModel):
    standards_subscription_arn: str = Field(alias="StandardsSubscriptionArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStandardsRequestDescribeStandardsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetEnabledStandardsRequestGetEnabledStandardsPaginateModel(BaseModel):
    standards_subscription_arns: Optional[Sequence[str]] = Field(
        default=None, alias="StandardsSubscriptionArns"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetInsightsRequestGetInsightsPaginateModel(BaseModel):
    insight_arns: Optional[Sequence[str]] = Field(default=None, alias="InsightArns")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingAggregatorsRequestListFindingAggregatorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInvitationsRequestListInvitationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembersRequestListMembersPaginateModel(BaseModel):
    only_associated: Optional[bool] = Field(default=None, alias="OnlyAssociated")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateModel(
    BaseModel
):
    standards_arn: Optional[str] = Field(default=None, alias="StandardsArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateModel(
    BaseModel
):
    security_control_id: str = Field(alias="SecurityControlId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeProductsResponseModel(BaseModel):
    products: List[ProductModel] = Field(alias="Products")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStandardsControlsResponseModel(BaseModel):
    controls: List[StandardsControlModel] = Field(alias="Controls")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ThreatModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[str] = Field(default=None, alias="Severity")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    file_paths: Optional[Sequence[FilePathsModel]] = Field(
        default=None, alias="FilePaths"
    )


class ListFindingAggregatorsResponseModel(BaseModel):
    finding_aggregators: List[FindingAggregatorModel] = Field(
        alias="FindingAggregators"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FindingProviderFieldsModel(BaseModel):
    confidence: Optional[int] = Field(default=None, alias="Confidence")
    criticality: Optional[int] = Field(default=None, alias="Criticality")
    related_findings: Optional[Sequence[RelatedFindingModel]] = Field(
        default=None, alias="RelatedFindings"
    )
    severity: Optional[FindingProviderSeverityModel] = Field(
        default=None, alias="Severity"
    )
    types: Optional[Sequence[str]] = Field(default=None, alias="Types")


class GetAdministratorAccountResponseModel(BaseModel):
    administrator: InvitationModel = Field(alias="Administrator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMasterAccountResponseModel(BaseModel):
    master: InvitationModel = Field(alias="Master")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInvitationsResponseModel(BaseModel):
    invitations: List[InvitationModel] = Field(alias="Invitations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMembersResponseModel(BaseModel):
    members: List[MemberModel] = Field(alias="Members")
    unprocessed_accounts: List[ResultModel] = Field(alias="UnprocessedAccounts")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMembersResponseModel(BaseModel):
    members: List[MemberModel] = Field(alias="Members")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InsightResultsModel(BaseModel):
    insight_arn: str = Field(alias="InsightArn")
    group_by_attribute: str = Field(alias="GroupByAttribute")
    result_values: List[InsightResultValueModel] = Field(alias="ResultValues")


class ListSecurityControlDefinitionsResponseModel(BaseModel):
    security_control_definitions: List[SecurityControlDefinitionModel] = Field(
        alias="SecurityControlDefinitions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStandardsControlAssociationsResponseModel(BaseModel):
    standards_control_association_summaries: List[
        StandardsControlAssociationSummaryModel
    ] = Field(alias="StandardsControlAssociationSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkPathComponentDetailsModel(BaseModel):
    address: Optional[Sequence[str]] = Field(default=None, alias="Address")
    port_ranges: Optional[Sequence[PortRangeModel]] = Field(
        default=None, alias="PortRanges"
    )


class NetworkModel(BaseModel):
    direction: Optional[Literal["IN", "OUT"]] = Field(default=None, alias="Direction")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    open_port_range: Optional[PortRangeModel] = Field(
        default=None, alias="OpenPortRange"
    )
    source_ip_v4: Optional[str] = Field(default=None, alias="SourceIpV4")
    source_ip_v6: Optional[str] = Field(default=None, alias="SourceIpV6")
    source_port: Optional[int] = Field(default=None, alias="SourcePort")
    source_domain: Optional[str] = Field(default=None, alias="SourceDomain")
    source_mac: Optional[str] = Field(default=None, alias="SourceMac")
    destination_ip_v4: Optional[str] = Field(default=None, alias="DestinationIpV4")
    destination_ip_v6: Optional[str] = Field(default=None, alias="DestinationIpV6")
    destination_port: Optional[int] = Field(default=None, alias="DestinationPort")
    destination_domain: Optional[str] = Field(default=None, alias="DestinationDomain")


class PageModel(BaseModel):
    page_number: Optional[int] = Field(default=None, alias="PageNumber")
    line_range: Optional[RangeModel] = Field(default=None, alias="LineRange")
    offset_range: Optional[RangeModel] = Field(default=None, alias="OffsetRange")


class RemediationModel(BaseModel):
    recommendation: Optional[RecommendationModel] = Field(
        default=None, alias="Recommendation"
    )


class RuleGroupSourceStatefulRulesDetailsModel(BaseModel):
    action: Optional[str] = Field(default=None, alias="Action")
    header: Optional[RuleGroupSourceStatefulRulesHeaderDetailsModel] = Field(
        default=None, alias="Header"
    )
    rule_options: Optional[
        Sequence[RuleGroupSourceStatefulRulesOptionsDetailsModel]
    ] = Field(default=None, alias="RuleOptions")


class RuleGroupSourceStatelessRuleMatchAttributesModel(BaseModel):
    destination_ports: Optional[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsModel]
    ] = Field(default=None, alias="DestinationPorts")
    destinations: Optional[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationsModel]
    ] = Field(default=None, alias="Destinations")
    protocols: Optional[Sequence[int]] = Field(default=None, alias="Protocols")
    source_ports: Optional[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsModel]
    ] = Field(default=None, alias="SourcePorts")
    sources: Optional[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcesModel]
    ] = Field(default=None, alias="Sources")
    tcp_flags: Optional[
        Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsModel]
    ] = Field(default=None, alias="TcpFlags")


class RuleGroupVariablesModel(BaseModel):
    ip_sets: Optional[RuleGroupVariablesIpSetsDetailsModel] = Field(
        default=None, alias="IpSets"
    )
    port_sets: Optional[RuleGroupVariablesPortSetsDetailsModel] = Field(
        default=None, alias="PortSets"
    )


class StandardModel(BaseModel):
    standards_arn: Optional[str] = Field(default=None, alias="StandardsArn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    enabled_by_default: Optional[bool] = Field(default=None, alias="EnabledByDefault")
    standards_managed_by: Optional[StandardsManagedByModel] = Field(
        default=None, alias="StandardsManagedBy"
    )


class StandardsSubscriptionModel(BaseModel):
    standards_subscription_arn: str = Field(alias="StandardsSubscriptionArn")
    standards_arn: str = Field(alias="StandardsArn")
    standards_input: Dict[str, str] = Field(alias="StandardsInput")
    standards_status: Literal[
        "DELETING", "FAILED", "INCOMPLETE", "PENDING", "READY"
    ] = Field(alias="StandardsStatus")
    standards_status_reason: Optional[StandardsStatusReasonModel] = Field(
        default=None, alias="StandardsStatusReason"
    )


class StatelessCustomPublishMetricActionModel(BaseModel):
    dimensions: Optional[
        Sequence[StatelessCustomPublishMetricActionDimensionModel]
    ] = Field(default=None, alias="Dimensions")


class AwsApiCallActionModel(BaseModel):
    api: Optional[str] = Field(default=None, alias="Api")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    caller_type: Optional[str] = Field(default=None, alias="CallerType")
    remote_ip_details: Optional[ActionRemoteIpDetailsModel] = Field(
        default=None, alias="RemoteIpDetails"
    )
    domain_details: Optional[AwsApiCallActionDomainDetailsModel] = Field(
        default=None, alias="DomainDetails"
    )
    affected_resources: Optional[Mapping[str, str]] = Field(
        default=None, alias="AffectedResources"
    )
    first_seen: Optional[str] = Field(default=None, alias="FirstSeen")
    last_seen: Optional[str] = Field(default=None, alias="LastSeen")


class NetworkConnectionActionModel(BaseModel):
    connection_direction: Optional[str] = Field(
        default=None, alias="ConnectionDirection"
    )
    remote_ip_details: Optional[ActionRemoteIpDetailsModel] = Field(
        default=None, alias="RemoteIpDetails"
    )
    remote_port_details: Optional[ActionRemotePortDetailsModel] = Field(
        default=None, alias="RemotePortDetails"
    )
    local_port_details: Optional[ActionLocalPortDetailsModel] = Field(
        default=None, alias="LocalPortDetails"
    )
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    blocked: Optional[bool] = Field(default=None, alias="Blocked")


class PortProbeDetailModel(BaseModel):
    local_port_details: Optional[ActionLocalPortDetailsModel] = Field(
        default=None, alias="LocalPortDetails"
    )
    local_ip_details: Optional[ActionLocalIpDetailsModel] = Field(
        default=None, alias="LocalIpDetails"
    )
    remote_ip_details: Optional[ActionRemoteIpDetailsModel] = Field(
        default=None, alias="RemoteIpDetails"
    )


class VulnerabilityModel(BaseModel):
    id: str = Field(alias="Id")
    vulnerable_packages: Optional[Sequence[SoftwarePackageModel]] = Field(
        default=None, alias="VulnerablePackages"
    )
    cvss: Optional[Sequence[CvssModel]] = Field(default=None, alias="Cvss")
    related_vulnerabilities: Optional[Sequence[str]] = Field(
        default=None, alias="RelatedVulnerabilities"
    )
    vendor: Optional[VulnerabilityVendorModel] = Field(default=None, alias="Vendor")
    reference_urls: Optional[Sequence[str]] = Field(default=None, alias="ReferenceUrls")
    fix_available: Optional[Literal["NO", "PARTIAL", "YES"]] = Field(
        default=None, alias="FixAvailable"
    )


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsModel(BaseModel):
    instances_distribution: Optional[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsModel
    ] = Field(default=None, alias="InstancesDistribution")
    launch_template: Optional[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsModel
    ] = Field(default=None, alias="LaunchTemplate")


class AwsAutoScalingLaunchConfigurationDetailsModel(BaseModel):
    associate_public_ip_address: Optional[bool] = Field(
        default=None, alias="AssociatePublicIpAddress"
    )
    block_device_mappings: Optional[
        Sequence[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsModel]
    ] = Field(default=None, alias="BlockDeviceMappings")
    classic_link_vpc_id: Optional[str] = Field(default=None, alias="ClassicLinkVpcId")
    classic_link_vpc_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="ClassicLinkVpcSecurityGroups"
    )
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    iam_instance_profile: Optional[str] = Field(
        default=None, alias="IamInstanceProfile"
    )
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    instance_monitoring: Optional[
        AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsModel
    ] = Field(default=None, alias="InstanceMonitoring")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    kernel_id: Optional[str] = Field(default=None, alias="KernelId")
    key_name: Optional[str] = Field(default=None, alias="KeyName")
    launch_configuration_name: Optional[str] = Field(
        default=None, alias="LaunchConfigurationName"
    )
    placement_tenancy: Optional[str] = Field(default=None, alias="PlacementTenancy")
    ramdisk_id: Optional[str] = Field(default=None, alias="RamdiskId")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    spot_price: Optional[str] = Field(default=None, alias="SpotPrice")
    user_data: Optional[str] = Field(default=None, alias="UserData")
    metadata_options: Optional[
        AwsAutoScalingLaunchConfigurationMetadataOptionsModel
    ] = Field(default=None, alias="MetadataOptions")


class AwsBackupBackupPlanRuleDetailsModel(BaseModel):
    target_backup_vault: Optional[str] = Field(default=None, alias="TargetBackupVault")
    start_window_minutes: Optional[int] = Field(
        default=None, alias="StartWindowMinutes"
    )
    schedule_expression: Optional[str] = Field(default=None, alias="ScheduleExpression")
    rule_name: Optional[str] = Field(default=None, alias="RuleName")
    rule_id: Optional[str] = Field(default=None, alias="RuleId")
    enable_continuous_backup: Optional[bool] = Field(
        default=None, alias="EnableContinuousBackup"
    )
    completion_window_minutes: Optional[int] = Field(
        default=None, alias="CompletionWindowMinutes"
    )
    copy_actions: Optional[
        Sequence[AwsBackupBackupPlanRuleCopyActionsDetailsModel]
    ] = Field(default=None, alias="CopyActions")
    lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsModel] = Field(
        default=None, alias="Lifecycle"
    )


class AwsCertificateManagerCertificateRenewalSummaryModel(BaseModel):
    domain_validation_options: Optional[
        Sequence[AwsCertificateManagerCertificateDomainValidationOptionModel]
    ] = Field(default=None, alias="DomainValidationOptions")
    renewal_status: Optional[str] = Field(default=None, alias="RenewalStatus")
    renewal_status_reason: Optional[str] = Field(
        default=None, alias="RenewalStatusReason"
    )
    updated_at: Optional[str] = Field(default=None, alias="UpdatedAt")


class AwsCloudFrontDistributionOriginItemModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    id: Optional[str] = Field(default=None, alias="Id")
    origin_path: Optional[str] = Field(default=None, alias="OriginPath")
    s3_origin_config: Optional[
        AwsCloudFrontDistributionOriginS3OriginConfigModel
    ] = Field(default=None, alias="S3OriginConfig")
    custom_origin_config: Optional[
        AwsCloudFrontDistributionOriginCustomOriginConfigModel
    ] = Field(default=None, alias="CustomOriginConfig")


class AwsCloudFrontDistributionOriginGroupModel(BaseModel):
    failover_criteria: Optional[
        AwsCloudFrontDistributionOriginGroupFailoverModel
    ] = Field(default=None, alias="FailoverCriteria")


class AwsCodeBuildProjectDetailsModel(BaseModel):
    encryption_key: Optional[str] = Field(default=None, alias="EncryptionKey")
    artifacts: Optional[Sequence[AwsCodeBuildProjectArtifactsDetailsModel]] = Field(
        default=None, alias="Artifacts"
    )
    environment: Optional[AwsCodeBuildProjectEnvironmentModel] = Field(
        default=None, alias="Environment"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    source: Optional[AwsCodeBuildProjectSourceModel] = Field(
        default=None, alias="Source"
    )
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")
    logs_config: Optional[AwsCodeBuildProjectLogsConfigDetailsModel] = Field(
        default=None, alias="LogsConfig"
    )
    vpc_config: Optional[AwsCodeBuildProjectVpcConfigModel] = Field(
        default=None, alias="VpcConfig"
    )
    secondary_artifacts: Optional[
        Sequence[AwsCodeBuildProjectArtifactsDetailsModel]
    ] = Field(default=None, alias="SecondaryArtifacts")


class AwsDynamoDbTableReplicaModel(BaseModel):
    global_secondary_indexes: Optional[
        Sequence[AwsDynamoDbTableReplicaGlobalSecondaryIndexModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    kms_master_key_id: Optional[str] = Field(default=None, alias="KmsMasterKeyId")
    provisioned_throughput_override: Optional[
        AwsDynamoDbTableProvisionedThroughputOverrideModel
    ] = Field(default=None, alias="ProvisionedThroughputOverride")
    region_name: Optional[str] = Field(default=None, alias="RegionName")
    replica_status: Optional[str] = Field(default=None, alias="ReplicaStatus")
    replica_status_description: Optional[str] = Field(
        default=None, alias="ReplicaStatusDescription"
    )


class AwsEc2LaunchTemplateDataDetailsModel(BaseModel):
    block_device_mapping_set: Optional[
        Sequence[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsModel]
    ] = Field(default=None, alias="BlockDeviceMappingSet")
    capacity_reservation_specification: Optional[
        AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsModel
    ] = Field(default=None, alias="CapacityReservationSpecification")
    cpu_options: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetailsModel] = Field(
        default=None, alias="CpuOptions"
    )
    credit_specification: Optional[
        AwsEc2LaunchTemplateDataCreditSpecificationDetailsModel
    ] = Field(default=None, alias="CreditSpecification")
    disable_api_stop: Optional[bool] = Field(default=None, alias="DisableApiStop")
    disable_api_termination: Optional[bool] = Field(
        default=None, alias="DisableApiTermination"
    )
    ebs_optimized: Optional[bool] = Field(default=None, alias="EbsOptimized")
    elastic_gpu_specification_set: Optional[
        Sequence[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsModel]
    ] = Field(default=None, alias="ElasticGpuSpecificationSet")
    elastic_inference_accelerator_set: Optional[
        Sequence[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsModel]
    ] = Field(default=None, alias="ElasticInferenceAcceleratorSet")
    enclave_options: Optional[
        AwsEc2LaunchTemplateDataEnclaveOptionsDetailsModel
    ] = Field(default=None, alias="EnclaveOptions")
    hibernation_options: Optional[
        AwsEc2LaunchTemplateDataHibernationOptionsDetailsModel
    ] = Field(default=None, alias="HibernationOptions")
    iam_instance_profile: Optional[
        AwsEc2LaunchTemplateDataIamInstanceProfileDetailsModel
    ] = Field(default=None, alias="IamInstanceProfile")
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    instance_initiated_shutdown_behavior: Optional[str] = Field(
        default=None, alias="InstanceInitiatedShutdownBehavior"
    )
    instance_market_options: Optional[
        AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsModel
    ] = Field(default=None, alias="InstanceMarketOptions")
    instance_requirements: Optional[
        AwsEc2LaunchTemplateDataInstanceRequirementsDetailsModel
    ] = Field(default=None, alias="InstanceRequirements")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    kernel_id: Optional[str] = Field(default=None, alias="KernelId")
    key_name: Optional[str] = Field(default=None, alias="KeyName")
    license_set: Optional[
        Sequence[AwsEc2LaunchTemplateDataLicenseSetDetailsModel]
    ] = Field(default=None, alias="LicenseSet")
    maintenance_options: Optional[
        AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsModel
    ] = Field(default=None, alias="MaintenanceOptions")
    metadata_options: Optional[
        AwsEc2LaunchTemplateDataMetadataOptionsDetailsModel
    ] = Field(default=None, alias="MetadataOptions")
    monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetailsModel] = Field(
        default=None, alias="Monitoring"
    )
    network_interface_set: Optional[
        Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsModel]
    ] = Field(default=None, alias="NetworkInterfaceSet")
    placement: Optional[AwsEc2LaunchTemplateDataPlacementDetailsModel] = Field(
        default=None, alias="Placement"
    )
    private_dns_name_options: Optional[
        AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsModel
    ] = Field(default=None, alias="PrivateDnsNameOptions")
    ram_disk_id: Optional[str] = Field(default=None, alias="RamDiskId")
    security_group_id_set: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIdSet"
    )
    security_group_set: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupSet"
    )
    user_data: Optional[str] = Field(default=None, alias="UserData")


class AwsEc2NetworkAclDetailsModel(BaseModel):
    is_default: Optional[bool] = Field(default=None, alias="IsDefault")
    network_acl_id: Optional[str] = Field(default=None, alias="NetworkAclId")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    associations: Optional[Sequence[AwsEc2NetworkAclAssociationModel]] = Field(
        default=None, alias="Associations"
    )
    entries: Optional[Sequence[AwsEc2NetworkAclEntryModel]] = Field(
        default=None, alias="Entries"
    )


class AwsEc2SecurityGroupDetailsModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    ip_permissions: Optional[Sequence[AwsEc2SecurityGroupIpPermissionModel]] = Field(
        default=None, alias="IpPermissions"
    )
    ip_permissions_egress: Optional[
        Sequence[AwsEc2SecurityGroupIpPermissionModel]
    ] = Field(default=None, alias="IpPermissionsEgress")


class AwsEc2VpcPeeringConnectionDetailsModel(BaseModel):
    accepter_vpc_info: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsModel] = Field(
        default=None, alias="AccepterVpcInfo"
    )
    expiration_time: Optional[str] = Field(default=None, alias="ExpirationTime")
    requester_vpc_info: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsModel] = Field(
        default=None, alias="RequesterVpcInfo"
    )
    status: Optional[AwsEc2VpcPeeringConnectionStatusDetailsModel] = Field(
        default=None, alias="Status"
    )
    vpc_peering_connection_id: Optional[str] = Field(
        default=None, alias="VpcPeeringConnectionId"
    )


class AwsEc2VpnConnectionDetailsModel(BaseModel):
    vpn_connection_id: Optional[str] = Field(default=None, alias="VpnConnectionId")
    state: Optional[str] = Field(default=None, alias="State")
    customer_gateway_id: Optional[str] = Field(default=None, alias="CustomerGatewayId")
    customer_gateway_configuration: Optional[str] = Field(
        default=None, alias="CustomerGatewayConfiguration"
    )
    type: Optional[str] = Field(default=None, alias="Type")
    vpn_gateway_id: Optional[str] = Field(default=None, alias="VpnGatewayId")
    category: Optional[str] = Field(default=None, alias="Category")
    vgw_telemetry: Optional[
        Sequence[AwsEc2VpnConnectionVgwTelemetryDetailsModel]
    ] = Field(default=None, alias="VgwTelemetry")
    options: Optional[AwsEc2VpnConnectionOptionsDetailsModel] = Field(
        default=None, alias="Options"
    )
    routes: Optional[Sequence[AwsEc2VpnConnectionRoutesDetailsModel]] = Field(
        default=None, alias="Routes"
    )
    transit_gateway_id: Optional[str] = Field(default=None, alias="TransitGatewayId")


class AwsEcsClusterConfigurationDetailsModel(BaseModel):
    execute_command_configuration: Optional[
        AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsModel
    ] = Field(default=None, alias="ExecuteCommandConfiguration")


class AwsEcsServiceDetailsModel(BaseModel):
    capacity_provider_strategy: Optional[
        Sequence[AwsEcsServiceCapacityProviderStrategyDetailsModel]
    ] = Field(default=None, alias="CapacityProviderStrategy")
    cluster: Optional[str] = Field(default=None, alias="Cluster")
    deployment_configuration: Optional[
        AwsEcsServiceDeploymentConfigurationDetailsModel
    ] = Field(default=None, alias="DeploymentConfiguration")
    deployment_controller: Optional[
        AwsEcsServiceDeploymentControllerDetailsModel
    ] = Field(default=None, alias="DeploymentController")
    desired_count: Optional[int] = Field(default=None, alias="DesiredCount")
    enable_ecs_managed_tags: Optional[bool] = Field(
        default=None, alias="EnableEcsManagedTags"
    )
    enable_execute_command: Optional[bool] = Field(
        default=None, alias="EnableExecuteCommand"
    )
    health_check_grace_period_seconds: Optional[int] = Field(
        default=None, alias="HealthCheckGracePeriodSeconds"
    )
    launch_type: Optional[str] = Field(default=None, alias="LaunchType")
    load_balancers: Optional[Sequence[AwsEcsServiceLoadBalancersDetailsModel]] = Field(
        default=None, alias="LoadBalancers"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    network_configuration: Optional[
        AwsEcsServiceNetworkConfigurationDetailsModel
    ] = Field(default=None, alias="NetworkConfiguration")
    placement_constraints: Optional[
        Sequence[AwsEcsServicePlacementConstraintsDetailsModel]
    ] = Field(default=None, alias="PlacementConstraints")
    placement_strategies: Optional[
        Sequence[AwsEcsServicePlacementStrategiesDetailsModel]
    ] = Field(default=None, alias="PlacementStrategies")
    platform_version: Optional[str] = Field(default=None, alias="PlatformVersion")
    propagate_tags: Optional[str] = Field(default=None, alias="PropagateTags")
    role: Optional[str] = Field(default=None, alias="Role")
    scheduling_strategy: Optional[str] = Field(default=None, alias="SchedulingStrategy")
    service_arn: Optional[str] = Field(default=None, alias="ServiceArn")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    service_registries: Optional[
        Sequence[AwsEcsServiceServiceRegistriesDetailsModel]
    ] = Field(default=None, alias="ServiceRegistries")
    task_definition: Optional[str] = Field(default=None, alias="TaskDefinition")


class AwsEcsTaskDefinitionContainerDefinitionsDetailsModel(BaseModel):
    command: Optional[Sequence[str]] = Field(default=None, alias="Command")
    cpu: Optional[int] = Field(default=None, alias="Cpu")
    depends_on: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsModel]
    ] = Field(default=None, alias="DependsOn")
    disable_networking: Optional[bool] = Field(default=None, alias="DisableNetworking")
    dns_search_domains: Optional[Sequence[str]] = Field(
        default=None, alias="DnsSearchDomains"
    )
    dns_servers: Optional[Sequence[str]] = Field(default=None, alias="DnsServers")
    docker_labels: Optional[Mapping[str, str]] = Field(
        default=None, alias="DockerLabels"
    )
    docker_security_options: Optional[Sequence[str]] = Field(
        default=None, alias="DockerSecurityOptions"
    )
    entry_point: Optional[Sequence[str]] = Field(default=None, alias="EntryPoint")
    environment: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsModel]
    ] = Field(default=None, alias="Environment")
    environment_files: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsModel]
    ] = Field(default=None, alias="EnvironmentFiles")
    essential: Optional[bool] = Field(default=None, alias="Essential")
    extra_hosts: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsModel]
    ] = Field(default=None, alias="ExtraHosts")
    firelens_configuration: Optional[
        AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsModel
    ] = Field(default=None, alias="FirelensConfiguration")
    health_check: Optional[
        AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsModel
    ] = Field(default=None, alias="HealthCheck")
    hostname: Optional[str] = Field(default=None, alias="Hostname")
    image: Optional[str] = Field(default=None, alias="Image")
    interactive: Optional[bool] = Field(default=None, alias="Interactive")
    links: Optional[Sequence[str]] = Field(default=None, alias="Links")
    linux_parameters: Optional[
        AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsModel
    ] = Field(default=None, alias="LinuxParameters")
    log_configuration: Optional[
        AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsModel
    ] = Field(default=None, alias="LogConfiguration")
    memory: Optional[int] = Field(default=None, alias="Memory")
    memory_reservation: Optional[int] = Field(default=None, alias="MemoryReservation")
    mount_points: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsModel]
    ] = Field(default=None, alias="MountPoints")
    name: Optional[str] = Field(default=None, alias="Name")
    port_mappings: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsModel]
    ] = Field(default=None, alias="PortMappings")
    privileged: Optional[bool] = Field(default=None, alias="Privileged")
    pseudo_terminal: Optional[bool] = Field(default=None, alias="PseudoTerminal")
    readonly_root_filesystem: Optional[bool] = Field(
        default=None, alias="ReadonlyRootFilesystem"
    )
    repository_credentials: Optional[
        AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsModel
    ] = Field(default=None, alias="RepositoryCredentials")
    resource_requirements: Optional[
        Sequence[
            AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsModel
        ]
    ] = Field(default=None, alias="ResourceRequirements")
    secrets: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsModel]
    ] = Field(default=None, alias="Secrets")
    start_timeout: Optional[int] = Field(default=None, alias="StartTimeout")
    stop_timeout: Optional[int] = Field(default=None, alias="StopTimeout")
    system_controls: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsModel]
    ] = Field(default=None, alias="SystemControls")
    ulimits: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsModel]
    ] = Field(default=None, alias="Ulimits")
    user: Optional[str] = Field(default=None, alias="User")
    volumes_from: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsModel]
    ] = Field(default=None, alias="VolumesFrom")
    working_directory: Optional[str] = Field(default=None, alias="WorkingDirectory")


class AwsEcsTaskDefinitionVolumesDetailsModel(BaseModel):
    docker_volume_configuration: Optional[
        AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsModel
    ] = Field(default=None, alias="DockerVolumeConfiguration")
    efs_volume_configuration: Optional[
        AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsModel
    ] = Field(default=None, alias="EfsVolumeConfiguration")
    host: Optional[AwsEcsTaskDefinitionVolumesHostDetailsModel] = Field(
        default=None, alias="Host"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class AwsEcsTaskDetailsModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    task_definition_arn: Optional[str] = Field(default=None, alias="TaskDefinitionArn")
    version: Optional[str] = Field(default=None, alias="Version")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    started_at: Optional[str] = Field(default=None, alias="StartedAt")
    started_by: Optional[str] = Field(default=None, alias="StartedBy")
    group: Optional[str] = Field(default=None, alias="Group")
    volumes: Optional[Sequence[AwsEcsTaskVolumeDetailsModel]] = Field(
        default=None, alias="Volumes"
    )
    containers: Optional[Sequence[AwsEcsContainerDetailsModel]] = Field(
        default=None, alias="Containers"
    )


class AwsEfsAccessPointDetailsModel(BaseModel):
    access_point_id: Optional[str] = Field(default=None, alias="AccessPointId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    posix_user: Optional[AwsEfsAccessPointPosixUserDetailsModel] = Field(
        default=None, alias="PosixUser"
    )
    root_directory: Optional[AwsEfsAccessPointRootDirectoryDetailsModel] = Field(
        default=None, alias="RootDirectory"
    )


class AwsEksClusterDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    certificate_authority_data: Optional[str] = Field(
        default=None, alias="CertificateAuthorityData"
    )
    cluster_status: Optional[str] = Field(default=None, alias="ClusterStatus")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    name: Optional[str] = Field(default=None, alias="Name")
    resources_vpc_config: Optional[AwsEksClusterResourcesVpcConfigDetailsModel] = Field(
        default=None, alias="ResourcesVpcConfig"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    version: Optional[str] = Field(default=None, alias="Version")
    logging: Optional[AwsEksClusterLoggingDetailsModel] = Field(
        default=None, alias="Logging"
    )


class AwsElasticsearchDomainDetailsModel(BaseModel):
    access_policies: Optional[str] = Field(default=None, alias="AccessPolicies")
    domain_endpoint_options: Optional[
        AwsElasticsearchDomainDomainEndpointOptionsModel
    ] = Field(default=None, alias="DomainEndpointOptions")
    domain_id: Optional[str] = Field(default=None, alias="DomainId")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    endpoints: Optional[Mapping[str, str]] = Field(default=None, alias="Endpoints")
    elasticsearch_version: Optional[str] = Field(
        default=None, alias="ElasticsearchVersion"
    )
    elasticsearch_cluster_config: Optional[
        AwsElasticsearchDomainElasticsearchClusterConfigDetailsModel
    ] = Field(default=None, alias="ElasticsearchClusterConfig")
    encryption_at_rest_options: Optional[
        AwsElasticsearchDomainEncryptionAtRestOptionsModel
    ] = Field(default=None, alias="EncryptionAtRestOptions")
    log_publishing_options: Optional[
        AwsElasticsearchDomainLogPublishingOptionsModel
    ] = Field(default=None, alias="LogPublishingOptions")
    node_to_node_encryption_options: Optional[
        AwsElasticsearchDomainNodeToNodeEncryptionOptionsModel
    ] = Field(default=None, alias="NodeToNodeEncryptionOptions")
    service_software_options: Optional[
        AwsElasticsearchDomainServiceSoftwareOptionsModel
    ] = Field(default=None, alias="ServiceSoftwareOptions")
    vp_coptions: Optional[AwsElasticsearchDomainVPCOptionsModel] = Field(
        default=None, alias="VPCOptions"
    )


class AwsElbLoadBalancerDetailsModel(BaseModel):
    availability_zones: Optional[Sequence[str]] = Field(
        default=None, alias="AvailabilityZones"
    )
    backend_server_descriptions: Optional[
        Sequence[AwsElbLoadBalancerBackendServerDescriptionModel]
    ] = Field(default=None, alias="BackendServerDescriptions")
    canonical_hosted_zone_name: Optional[str] = Field(
        default=None, alias="CanonicalHostedZoneName"
    )
    canonical_hosted_zone_name_id: Optional[str] = Field(
        default=None, alias="CanonicalHostedZoneNameID"
    )
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")
    dns_name: Optional[str] = Field(default=None, alias="DnsName")
    health_check: Optional[AwsElbLoadBalancerHealthCheckModel] = Field(
        default=None, alias="HealthCheck"
    )
    instances: Optional[Sequence[AwsElbLoadBalancerInstanceModel]] = Field(
        default=None, alias="Instances"
    )
    listener_descriptions: Optional[
        Sequence[AwsElbLoadBalancerListenerDescriptionModel]
    ] = Field(default=None, alias="ListenerDescriptions")
    load_balancer_attributes: Optional[AwsElbLoadBalancerAttributesModel] = Field(
        default=None, alias="LoadBalancerAttributes"
    )
    load_balancer_name: Optional[str] = Field(default=None, alias="LoadBalancerName")
    policies: Optional[AwsElbLoadBalancerPoliciesModel] = Field(
        default=None, alias="Policies"
    )
    scheme: Optional[str] = Field(default=None, alias="Scheme")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    source_security_group: Optional[AwsElbLoadBalancerSourceSecurityGroupModel] = Field(
        default=None, alias="SourceSecurityGroup"
    )
    subnets: Optional[Sequence[str]] = Field(default=None, alias="Subnets")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class AwsIamAccessKeyDetailsModel(BaseModel):
    user_name: Optional[str] = Field(default=None, alias="UserName")
    status: Optional[Literal["Active", "Inactive"]] = Field(
        default=None, alias="Status"
    )
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    principal_type: Optional[str] = Field(default=None, alias="PrincipalType")
    principal_name: Optional[str] = Field(default=None, alias="PrincipalName")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    access_key_id: Optional[str] = Field(default=None, alias="AccessKeyId")
    session_context: Optional[AwsIamAccessKeySessionContextModel] = Field(
        default=None, alias="SessionContext"
    )


class AwsIamRoleDetailsModel(BaseModel):
    assume_role_policy_document: Optional[str] = Field(
        default=None, alias="AssumeRolePolicyDocument"
    )
    attached_managed_policies: Optional[
        Sequence[AwsIamAttachedManagedPolicyModel]
    ] = Field(default=None, alias="AttachedManagedPolicies")
    create_date: Optional[str] = Field(default=None, alias="CreateDate")
    instance_profile_list: Optional[Sequence[AwsIamInstanceProfileModel]] = Field(
        default=None, alias="InstanceProfileList"
    )
    permissions_boundary: Optional[AwsIamPermissionsBoundaryModel] = Field(
        default=None, alias="PermissionsBoundary"
    )
    role_id: Optional[str] = Field(default=None, alias="RoleId")
    role_name: Optional[str] = Field(default=None, alias="RoleName")
    role_policy_list: Optional[Sequence[AwsIamRolePolicyModel]] = Field(
        default=None, alias="RolePolicyList"
    )
    max_session_duration: Optional[int] = Field(
        default=None, alias="MaxSessionDuration"
    )
    path: Optional[str] = Field(default=None, alias="Path")


class AwsLambdaFunctionDetailsModel(BaseModel):
    code: Optional[AwsLambdaFunctionCodeModel] = Field(default=None, alias="Code")
    code_sha256: Optional[str] = Field(default=None, alias="CodeSha256")
    dead_letter_config: Optional[AwsLambdaFunctionDeadLetterConfigModel] = Field(
        default=None, alias="DeadLetterConfig"
    )
    environment: Optional[AwsLambdaFunctionEnvironmentModel] = Field(
        default=None, alias="Environment"
    )
    function_name: Optional[str] = Field(default=None, alias="FunctionName")
    handler: Optional[str] = Field(default=None, alias="Handler")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")
    last_modified: Optional[str] = Field(default=None, alias="LastModified")
    layers: Optional[Sequence[AwsLambdaFunctionLayerModel]] = Field(
        default=None, alias="Layers"
    )
    master_arn: Optional[str] = Field(default=None, alias="MasterArn")
    memory_size: Optional[int] = Field(default=None, alias="MemorySize")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    role: Optional[str] = Field(default=None, alias="Role")
    runtime: Optional[str] = Field(default=None, alias="Runtime")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    tracing_config: Optional[AwsLambdaFunctionTracingConfigModel] = Field(
        default=None, alias="TracingConfig"
    )
    vpc_config: Optional[AwsLambdaFunctionVpcConfigModel] = Field(
        default=None, alias="VpcConfig"
    )
    version: Optional[str] = Field(default=None, alias="Version")
    architectures: Optional[Sequence[str]] = Field(default=None, alias="Architectures")
    package_type: Optional[str] = Field(default=None, alias="PackageType")


class AwsOpenSearchServiceDomainDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    access_policies: Optional[str] = Field(default=None, alias="AccessPolicies")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    id: Optional[str] = Field(default=None, alias="Id")
    domain_endpoint: Optional[str] = Field(default=None, alias="DomainEndpoint")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    encryption_at_rest_options: Optional[
        AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsModel
    ] = Field(default=None, alias="EncryptionAtRestOptions")
    node_to_node_encryption_options: Optional[
        AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsModel
    ] = Field(default=None, alias="NodeToNodeEncryptionOptions")
    service_software_options: Optional[
        AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsModel
    ] = Field(default=None, alias="ServiceSoftwareOptions")
    cluster_config: Optional[
        AwsOpenSearchServiceDomainClusterConfigDetailsModel
    ] = Field(default=None, alias="ClusterConfig")
    domain_endpoint_options: Optional[
        AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsModel
    ] = Field(default=None, alias="DomainEndpointOptions")
    vpc_options: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsModel] = Field(
        default=None, alias="VpcOptions"
    )
    log_publishing_options: Optional[
        AwsOpenSearchServiceDomainLogPublishingOptionsDetailsModel
    ] = Field(default=None, alias="LogPublishingOptions")
    domain_endpoints: Optional[Mapping[str, str]] = Field(
        default=None, alias="DomainEndpoints"
    )
    advanced_security_options: Optional[
        AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsModel
    ] = Field(default=None, alias="AdvancedSecurityOptions")


class AwsRdsDbSubnetGroupModel(BaseModel):
    db_subnet_group_name: Optional[str] = Field(default=None, alias="DbSubnetGroupName")
    db_subnet_group_description: Optional[str] = Field(
        default=None, alias="DbSubnetGroupDescription"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    subnet_group_status: Optional[str] = Field(default=None, alias="SubnetGroupStatus")
    subnets: Optional[Sequence[AwsRdsDbSubnetGroupSubnetModel]] = Field(
        default=None, alias="Subnets"
    )
    db_subnet_group_arn: Optional[str] = Field(default=None, alias="DbSubnetGroupArn")


class AwsRedshiftClusterDetailsModel(BaseModel):
    allow_version_upgrade: Optional[bool] = Field(
        default=None, alias="AllowVersionUpgrade"
    )
    automated_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="AutomatedSnapshotRetentionPeriod"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    cluster_availability_status: Optional[str] = Field(
        default=None, alias="ClusterAvailabilityStatus"
    )
    cluster_create_time: Optional[str] = Field(default=None, alias="ClusterCreateTime")
    cluster_identifier: Optional[str] = Field(default=None, alias="ClusterIdentifier")
    cluster_nodes: Optional[Sequence[AwsRedshiftClusterClusterNodeModel]] = Field(
        default=None, alias="ClusterNodes"
    )
    cluster_parameter_groups: Optional[
        Sequence[AwsRedshiftClusterClusterParameterGroupModel]
    ] = Field(default=None, alias="ClusterParameterGroups")
    cluster_public_key: Optional[str] = Field(default=None, alias="ClusterPublicKey")
    cluster_revision_number: Optional[str] = Field(
        default=None, alias="ClusterRevisionNumber"
    )
    cluster_security_groups: Optional[
        Sequence[AwsRedshiftClusterClusterSecurityGroupModel]
    ] = Field(default=None, alias="ClusterSecurityGroups")
    cluster_snapshot_copy_status: Optional[
        AwsRedshiftClusterClusterSnapshotCopyStatusModel
    ] = Field(default=None, alias="ClusterSnapshotCopyStatus")
    cluster_status: Optional[str] = Field(default=None, alias="ClusterStatus")
    cluster_subnet_group_name: Optional[str] = Field(
        default=None, alias="ClusterSubnetGroupName"
    )
    cluster_version: Optional[str] = Field(default=None, alias="ClusterVersion")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    deferred_maintenance_windows: Optional[
        Sequence[AwsRedshiftClusterDeferredMaintenanceWindowModel]
    ] = Field(default=None, alias="DeferredMaintenanceWindows")
    elastic_ip_status: Optional[AwsRedshiftClusterElasticIpStatusModel] = Field(
        default=None, alias="ElasticIpStatus"
    )
    elastic_resize_number_of_node_options: Optional[str] = Field(
        default=None, alias="ElasticResizeNumberOfNodeOptions"
    )
    encrypted: Optional[bool] = Field(default=None, alias="Encrypted")
    endpoint: Optional[AwsRedshiftClusterEndpointModel] = Field(
        default=None, alias="Endpoint"
    )
    enhanced_vpc_routing: Optional[bool] = Field(
        default=None, alias="EnhancedVpcRouting"
    )
    expected_next_snapshot_schedule_time: Optional[str] = Field(
        default=None, alias="ExpectedNextSnapshotScheduleTime"
    )
    expected_next_snapshot_schedule_time_status: Optional[str] = Field(
        default=None, alias="ExpectedNextSnapshotScheduleTimeStatus"
    )
    hsm_status: Optional[AwsRedshiftClusterHsmStatusModel] = Field(
        default=None, alias="HsmStatus"
    )
    iam_roles: Optional[Sequence[AwsRedshiftClusterIamRoleModel]] = Field(
        default=None, alias="IamRoles"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    maintenance_track_name: Optional[str] = Field(
        default=None, alias="MaintenanceTrackName"
    )
    manual_snapshot_retention_period: Optional[int] = Field(
        default=None, alias="ManualSnapshotRetentionPeriod"
    )
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    next_maintenance_window_start_time: Optional[str] = Field(
        default=None, alias="NextMaintenanceWindowStartTime"
    )
    node_type: Optional[str] = Field(default=None, alias="NodeType")
    number_of_nodes: Optional[int] = Field(default=None, alias="NumberOfNodes")
    pending_actions: Optional[Sequence[str]] = Field(
        default=None, alias="PendingActions"
    )
    pending_modified_values: Optional[
        AwsRedshiftClusterPendingModifiedValuesModel
    ] = Field(default=None, alias="PendingModifiedValues")
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    resize_info: Optional[AwsRedshiftClusterResizeInfoModel] = Field(
        default=None, alias="ResizeInfo"
    )
    restore_status: Optional[AwsRedshiftClusterRestoreStatusModel] = Field(
        default=None, alias="RestoreStatus"
    )
    snapshot_schedule_identifier: Optional[str] = Field(
        default=None, alias="SnapshotScheduleIdentifier"
    )
    snapshot_schedule_state: Optional[str] = Field(
        default=None, alias="SnapshotScheduleState"
    )
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    vpc_security_groups: Optional[
        Sequence[AwsRedshiftClusterVpcSecurityGroupModel]
    ] = Field(default=None, alias="VpcSecurityGroups")
    logging_status: Optional[AwsRedshiftClusterLoggingStatusModel] = Field(
        default=None, alias="LoggingStatus"
    )


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsModel(
    BaseModel
):
    operands: Optional[
        Sequence[
            AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsModel
        ]
    ] = Field(default=None, alias="Operands")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    tag: Optional[
        AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsModel
    ] = Field(default=None, alias="Tag")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsS3BucketNotificationConfigurationFilterModel(BaseModel):
    s3_key_filter: Optional[
        AwsS3BucketNotificationConfigurationS3KeyFilterModel
    ] = Field(default=None, alias="S3KeyFilter")


class AwsS3BucketServerSideEncryptionConfigurationModel(BaseModel):
    rules: Optional[Sequence[AwsS3BucketServerSideEncryptionRuleModel]] = Field(
        default=None, alias="Rules"
    )


class AwsS3BucketWebsiteConfigurationModel(BaseModel):
    error_document: Optional[str] = Field(default=None, alias="ErrorDocument")
    index_document_suffix: Optional[str] = Field(
        default=None, alias="IndexDocumentSuffix"
    )
    redirect_all_requests_to: Optional[
        AwsS3BucketWebsiteConfigurationRedirectToModel
    ] = Field(default=None, alias="RedirectAllRequestsTo")
    routing_rules: Optional[
        Sequence[AwsS3BucketWebsiteConfigurationRoutingRuleModel]
    ] = Field(default=None, alias="RoutingRules")


class BatchUpdateFindingsResponseModel(BaseModel):
    processed_findings: List[AwsSecurityFindingIdentifierModel] = Field(
        alias="ProcessedFindings"
    )
    unprocessed_findings: List[BatchUpdateFindingsUnprocessedFindingModel] = Field(
        alias="UnprocessedFindings"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AwsSsmPatchComplianceDetailsModel(BaseModel):
    patch: Optional[AwsSsmPatchModel] = Field(default=None, alias="Patch")


class AwsWafRegionalRuleGroupDetailsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    name: Optional[str] = Field(default=None, alias="Name")
    rule_group_id: Optional[str] = Field(default=None, alias="RuleGroupId")
    rules: Optional[Sequence[AwsWafRegionalRuleGroupRulesDetailsModel]] = Field(
        default=None, alias="Rules"
    )


class AwsWafRegionalWebAclDetailsModel(BaseModel):
    default_action: Optional[str] = Field(default=None, alias="DefaultAction")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    name: Optional[str] = Field(default=None, alias="Name")
    rules_list: Optional[Sequence[AwsWafRegionalWebAclRulesListDetailsModel]] = Field(
        default=None, alias="RulesList"
    )
    web_acl_id: Optional[str] = Field(default=None, alias="WebAclId")


class AwsWafRuleGroupDetailsModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    name: Optional[str] = Field(default=None, alias="Name")
    rule_group_id: Optional[str] = Field(default=None, alias="RuleGroupId")
    rules: Optional[Sequence[AwsWafRuleGroupRulesDetailsModel]] = Field(
        default=None, alias="Rules"
    )


class AwsWafWebAclDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    default_action: Optional[str] = Field(default=None, alias="DefaultAction")
    rules: Optional[Sequence[AwsWafWebAclRuleModel]] = Field(
        default=None, alias="Rules"
    )
    web_acl_id: Optional[str] = Field(default=None, alias="WebAclId")


class AwsWafv2ActionAllowDetailsModel(BaseModel):
    custom_request_handling: Optional[
        AwsWafv2CustomRequestHandlingDetailsModel
    ] = Field(default=None, alias="CustomRequestHandling")


class AwsWafv2RulesActionCaptchaDetailsModel(BaseModel):
    custom_request_handling: Optional[
        AwsWafv2CustomRequestHandlingDetailsModel
    ] = Field(default=None, alias="CustomRequestHandling")


class AwsWafv2RulesActionCountDetailsModel(BaseModel):
    custom_request_handling: Optional[
        AwsWafv2CustomRequestHandlingDetailsModel
    ] = Field(default=None, alias="CustomRequestHandling")


class AwsWafv2ActionBlockDetailsModel(BaseModel):
    custom_response: Optional[AwsWafv2CustomResponseDetailsModel] = Field(
        default=None, alias="CustomResponse"
    )


class BatchGetStandardsControlAssociationsResponseModel(BaseModel):
    standards_control_association_details: List[
        StandardsControlAssociationDetailModel
    ] = Field(alias="StandardsControlAssociationDetails")
    unprocessed_associations: List[UnprocessedStandardsControlAssociationModel] = Field(
        alias="UnprocessedAssociations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateStandardsControlAssociationsResponseModel(BaseModel):
    unprocessed_association_updates: List[
        UnprocessedStandardsControlAssociationUpdateModel
    ] = Field(alias="UnprocessedAssociationUpdates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AwsSecurityFindingFiltersModel(BaseModel):
    product_arn: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ProductArn"
    )
    aws_account_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="AwsAccountId"
    )
    id: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="Id")
    generator_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="GeneratorId"
    )
    region: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="Region")
    type: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="Type")
    first_observed_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="FirstObservedAt"
    )
    last_observed_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="LastObservedAt"
    )
    created_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="CreatedAt"
    )
    updated_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="UpdatedAt"
    )
    severity_product: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="SeverityProduct"
    )
    severity_normalized: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="SeverityNormalized"
    )
    severity_label: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="SeverityLabel"
    )
    confidence: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="Confidence"
    )
    criticality: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="Criticality"
    )
    title: Optional[Sequence[StringFilterModel]] = Field(default=None, alias="Title")
    description: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="Description"
    )
    recommendation_text: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="RecommendationText"
    )
    source_url: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="SourceUrl"
    )
    product_fields: Optional[Sequence[MapFilterModel]] = Field(
        default=None, alias="ProductFields"
    )
    product_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ProductName"
    )
    company_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="CompanyName"
    )
    user_defined_fields: Optional[Sequence[MapFilterModel]] = Field(
        default=None, alias="UserDefinedFields"
    )
    malware_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="MalwareName"
    )
    malware_type: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="MalwareType"
    )
    malware_path: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="MalwarePath"
    )
    malware_state: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="MalwareState"
    )
    network_direction: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="NetworkDirection"
    )
    network_protocol: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="NetworkProtocol"
    )
    network_source_ip_v4: Optional[Sequence[IpFilterModel]] = Field(
        default=None, alias="NetworkSourceIpV4"
    )
    network_source_ip_v6: Optional[Sequence[IpFilterModel]] = Field(
        default=None, alias="NetworkSourceIpV6"
    )
    network_source_port: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="NetworkSourcePort"
    )
    network_source_domain: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="NetworkSourceDomain"
    )
    network_source_mac: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="NetworkSourceMac"
    )
    network_destination_ip_v4: Optional[Sequence[IpFilterModel]] = Field(
        default=None, alias="NetworkDestinationIpV4"
    )
    network_destination_ip_v6: Optional[Sequence[IpFilterModel]] = Field(
        default=None, alias="NetworkDestinationIpV6"
    )
    network_destination_port: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="NetworkDestinationPort"
    )
    network_destination_domain: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="NetworkDestinationDomain"
    )
    process_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ProcessName"
    )
    process_path: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ProcessPath"
    )
    process_pid: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="ProcessPid"
    )
    process_parent_pid: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="ProcessParentPid"
    )
    process_launched_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="ProcessLaunchedAt"
    )
    process_terminated_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="ProcessTerminatedAt"
    )
    threat_intel_indicator_type: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ThreatIntelIndicatorType"
    )
    threat_intel_indicator_value: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ThreatIntelIndicatorValue"
    )
    threat_intel_indicator_category: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ThreatIntelIndicatorCategory"
    )
    threat_intel_indicator_last_observed_at: Optional[
        Sequence[DateFilterModel]
    ] = Field(default=None, alias="ThreatIntelIndicatorLastObservedAt")
    threat_intel_indicator_source: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ThreatIntelIndicatorSource"
    )
    threat_intel_indicator_source_url: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ThreatIntelIndicatorSourceUrl"
    )
    resource_type: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceType"
    )
    resource_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceId"
    )
    resource_partition: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourcePartition"
    )
    resource_region: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceRegion"
    )
    resource_tags: Optional[Sequence[MapFilterModel]] = Field(
        default=None, alias="ResourceTags"
    )
    resource_aws_ec2_instance_type: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsEc2InstanceType"
    )
    resource_aws_ec2_instance_image_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsEc2InstanceImageId"
    )
    resource_aws_ec2_instance_ip_v4_addresses: Optional[
        Sequence[IpFilterModel]
    ] = Field(default=None, alias="ResourceAwsEc2InstanceIpV4Addresses")
    resource_aws_ec2_instance_ip_v6_addresses: Optional[
        Sequence[IpFilterModel]
    ] = Field(default=None, alias="ResourceAwsEc2InstanceIpV6Addresses")
    resource_aws_ec2_instance_key_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsEc2InstanceKeyName"
    )
    resource_aws_ec2_instance_iam_instance_profile_arn: Optional[
        Sequence[StringFilterModel]
    ] = Field(default=None, alias="ResourceAwsEc2InstanceIamInstanceProfileArn")
    resource_aws_ec2_instance_vpc_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsEc2InstanceVpcId"
    )
    resource_aws_ec2_instance_subnet_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsEc2InstanceSubnetId"
    )
    resource_aws_ec2_instance_launched_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="ResourceAwsEc2InstanceLaunchedAt"
    )
    resource_aws_s3_bucket_owner_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsS3BucketOwnerId"
    )
    resource_aws_s3_bucket_owner_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsS3BucketOwnerName"
    )
    resource_aws_iam_access_key_user_name: Optional[
        Sequence[StringFilterModel]
    ] = Field(default=None, alias="ResourceAwsIamAccessKeyUserName")
    resource_aws_iam_access_key_principal_name: Optional[
        Sequence[StringFilterModel]
    ] = Field(default=None, alias="ResourceAwsIamAccessKeyPrincipalName")
    resource_aws_iam_access_key_status: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsIamAccessKeyStatus"
    )
    resource_aws_iam_access_key_created_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="ResourceAwsIamAccessKeyCreatedAt"
    )
    resource_aws_iam_user_user_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceAwsIamUserUserName"
    )
    resource_container_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceContainerName"
    )
    resource_container_image_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceContainerImageId"
    )
    resource_container_image_name: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ResourceContainerImageName"
    )
    resource_container_launched_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="ResourceContainerLaunchedAt"
    )
    resource_details_other: Optional[Sequence[MapFilterModel]] = Field(
        default=None, alias="ResourceDetailsOther"
    )
    compliance_status: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ComplianceStatus"
    )
    verification_state: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="VerificationState"
    )
    workflow_state: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="WorkflowState"
    )
    workflow_status: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="WorkflowStatus"
    )
    record_state: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="RecordState"
    )
    related_findings_product_arn: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="RelatedFindingsProductArn"
    )
    related_findings_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="RelatedFindingsId"
    )
    note_text: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="NoteText"
    )
    note_updated_at: Optional[Sequence[DateFilterModel]] = Field(
        default=None, alias="NoteUpdatedAt"
    )
    note_updated_by: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="NoteUpdatedBy"
    )
    keyword: Optional[Sequence[KeywordFilterModel]] = Field(
        default=None, alias="Keyword"
    )
    finding_provider_fields_confidence: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="FindingProviderFieldsConfidence"
    )
    finding_provider_fields_criticality: Optional[Sequence[NumberFilterModel]] = Field(
        default=None, alias="FindingProviderFieldsCriticality"
    )
    finding_provider_fields_related_findings_id: Optional[
        Sequence[StringFilterModel]
    ] = Field(default=None, alias="FindingProviderFieldsRelatedFindingsId")
    finding_provider_fields_related_findings_product_arn: Optional[
        Sequence[StringFilterModel]
    ] = Field(default=None, alias="FindingProviderFieldsRelatedFindingsProductArn")
    finding_provider_fields_severity_label: Optional[
        Sequence[StringFilterModel]
    ] = Field(default=None, alias="FindingProviderFieldsSeverityLabel")
    finding_provider_fields_severity_original: Optional[
        Sequence[StringFilterModel]
    ] = Field(default=None, alias="FindingProviderFieldsSeverityOriginal")
    finding_provider_fields_types: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="FindingProviderFieldsTypes"
    )
    sample: Optional[Sequence[BooleanFilterModel]] = Field(default=None, alias="Sample")
    compliance_security_control_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ComplianceSecurityControlId"
    )
    compliance_associated_standards_id: Optional[Sequence[StringFilterModel]] = Field(
        default=None, alias="ComplianceAssociatedStandardsId"
    )


class GetInsightResultsResponseModel(BaseModel):
    insight_results: InsightResultsModel = Field(alias="InsightResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkHeaderModel(BaseModel):
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    destination: Optional[NetworkPathComponentDetailsModel] = Field(
        default=None, alias="Destination"
    )
    source: Optional[NetworkPathComponentDetailsModel] = Field(
        default=None, alias="Source"
    )


class OccurrencesModel(BaseModel):
    line_ranges: Optional[Sequence[RangeModel]] = Field(
        default=None, alias="LineRanges"
    )
    offset_ranges: Optional[Sequence[RangeModel]] = Field(
        default=None, alias="OffsetRanges"
    )
    pages: Optional[Sequence[PageModel]] = Field(default=None, alias="Pages")
    records: Optional[Sequence[RecordModel]] = Field(default=None, alias="Records")
    cells: Optional[Sequence[CellModel]] = Field(default=None, alias="Cells")


class RuleGroupSourceStatelessRuleDefinitionModel(BaseModel):
    actions: Optional[Sequence[str]] = Field(default=None, alias="Actions")
    match_attributes: Optional[
        RuleGroupSourceStatelessRuleMatchAttributesModel
    ] = Field(default=None, alias="MatchAttributes")


class DescribeStandardsResponseModel(BaseModel):
    standards: List[StandardModel] = Field(alias="Standards")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisableStandardsResponseModel(BaseModel):
    standards_subscriptions: List[StandardsSubscriptionModel] = Field(
        alias="StandardsSubscriptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchEnableStandardsResponseModel(BaseModel):
    standards_subscriptions: List[StandardsSubscriptionModel] = Field(
        alias="StandardsSubscriptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEnabledStandardsResponseModel(BaseModel):
    standards_subscriptions: List[StandardsSubscriptionModel] = Field(
        alias="StandardsSubscriptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StatelessCustomActionDefinitionModel(BaseModel):
    publish_metric_action: Optional[StatelessCustomPublishMetricActionModel] = Field(
        default=None, alias="PublishMetricAction"
    )


class PortProbeActionModel(BaseModel):
    port_probe_details: Optional[Sequence[PortProbeDetailModel]] = Field(
        default=None, alias="PortProbeDetails"
    )
    blocked: Optional[bool] = Field(default=None, alias="Blocked")


class AwsAutoScalingAutoScalingGroupDetailsModel(BaseModel):
    launch_configuration_name: Optional[str] = Field(
        default=None, alias="LaunchConfigurationName"
    )
    load_balancer_names: Optional[Sequence[str]] = Field(
        default=None, alias="LoadBalancerNames"
    )
    health_check_type: Optional[str] = Field(default=None, alias="HealthCheckType")
    health_check_grace_period: Optional[int] = Field(
        default=None, alias="HealthCheckGracePeriod"
    )
    created_time: Optional[str] = Field(default=None, alias="CreatedTime")
    mixed_instances_policy: Optional[
        AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsModel
    ] = Field(default=None, alias="MixedInstancesPolicy")
    availability_zones: Optional[
        Sequence[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsModel]
    ] = Field(default=None, alias="AvailabilityZones")
    launch_template: Optional[
        AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationModel
    ] = Field(default=None, alias="LaunchTemplate")
    capacity_rebalance: Optional[bool] = Field(default=None, alias="CapacityRebalance")


class AwsBackupBackupPlanBackupPlanDetailsModel(BaseModel):
    backup_plan_name: Optional[str] = Field(default=None, alias="BackupPlanName")
    advanced_backup_settings: Optional[
        Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsModel]
    ] = Field(default=None, alias="AdvancedBackupSettings")
    backup_plan_rule: Optional[Sequence[AwsBackupBackupPlanRuleDetailsModel]] = Field(
        default=None, alias="BackupPlanRule"
    )


class AwsCertificateManagerCertificateDetailsModel(BaseModel):
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    domain_validation_options: Optional[
        Sequence[AwsCertificateManagerCertificateDomainValidationOptionModel]
    ] = Field(default=None, alias="DomainValidationOptions")
    extended_key_usages: Optional[
        Sequence[AwsCertificateManagerCertificateExtendedKeyUsageModel]
    ] = Field(default=None, alias="ExtendedKeyUsages")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    imported_at: Optional[str] = Field(default=None, alias="ImportedAt")
    in_use_by: Optional[Sequence[str]] = Field(default=None, alias="InUseBy")
    issued_at: Optional[str] = Field(default=None, alias="IssuedAt")
    issuer: Optional[str] = Field(default=None, alias="Issuer")
    key_algorithm: Optional[str] = Field(default=None, alias="KeyAlgorithm")
    key_usages: Optional[
        Sequence[AwsCertificateManagerCertificateKeyUsageModel]
    ] = Field(default=None, alias="KeyUsages")
    not_after: Optional[str] = Field(default=None, alias="NotAfter")
    not_before: Optional[str] = Field(default=None, alias="NotBefore")
    options: Optional[AwsCertificateManagerCertificateOptionsModel] = Field(
        default=None, alias="Options"
    )
    renewal_eligibility: Optional[str] = Field(default=None, alias="RenewalEligibility")
    renewal_summary: Optional[
        AwsCertificateManagerCertificateRenewalSummaryModel
    ] = Field(default=None, alias="RenewalSummary")
    serial: Optional[str] = Field(default=None, alias="Serial")
    signature_algorithm: Optional[str] = Field(default=None, alias="SignatureAlgorithm")
    status: Optional[str] = Field(default=None, alias="Status")
    subject: Optional[str] = Field(default=None, alias="Subject")
    subject_alternative_names: Optional[Sequence[str]] = Field(
        default=None, alias="SubjectAlternativeNames"
    )
    type: Optional[str] = Field(default=None, alias="Type")


class AwsCloudFrontDistributionOriginsModel(BaseModel):
    items: Optional[Sequence[AwsCloudFrontDistributionOriginItemModel]] = Field(
        default=None, alias="Items"
    )


class AwsCloudFrontDistributionOriginGroupsModel(BaseModel):
    items: Optional[Sequence[AwsCloudFrontDistributionOriginGroupModel]] = Field(
        default=None, alias="Items"
    )


class AwsDynamoDbTableDetailsModel(BaseModel):
    attribute_definitions: Optional[
        Sequence[AwsDynamoDbTableAttributeDefinitionModel]
    ] = Field(default=None, alias="AttributeDefinitions")
    billing_mode_summary: Optional[AwsDynamoDbTableBillingModeSummaryModel] = Field(
        default=None, alias="BillingModeSummary"
    )
    creation_date_time: Optional[str] = Field(default=None, alias="CreationDateTime")
    global_secondary_indexes: Optional[
        Sequence[AwsDynamoDbTableGlobalSecondaryIndexModel]
    ] = Field(default=None, alias="GlobalSecondaryIndexes")
    global_table_version: Optional[str] = Field(
        default=None, alias="GlobalTableVersion"
    )
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    key_schema: Optional[Sequence[AwsDynamoDbTableKeySchemaModel]] = Field(
        default=None, alias="KeySchema"
    )
    latest_stream_arn: Optional[str] = Field(default=None, alias="LatestStreamArn")
    latest_stream_label: Optional[str] = Field(default=None, alias="LatestStreamLabel")
    local_secondary_indexes: Optional[
        Sequence[AwsDynamoDbTableLocalSecondaryIndexModel]
    ] = Field(default=None, alias="LocalSecondaryIndexes")
    provisioned_throughput: Optional[
        AwsDynamoDbTableProvisionedThroughputModel
    ] = Field(default=None, alias="ProvisionedThroughput")
    replicas: Optional[Sequence[AwsDynamoDbTableReplicaModel]] = Field(
        default=None, alias="Replicas"
    )
    restore_summary: Optional[AwsDynamoDbTableRestoreSummaryModel] = Field(
        default=None, alias="RestoreSummary"
    )
    sse_description: Optional[AwsDynamoDbTableSseDescriptionModel] = Field(
        default=None, alias="SseDescription"
    )
    stream_specification: Optional[AwsDynamoDbTableStreamSpecificationModel] = Field(
        default=None, alias="StreamSpecification"
    )
    table_id: Optional[str] = Field(default=None, alias="TableId")
    table_name: Optional[str] = Field(default=None, alias="TableName")
    table_size_bytes: Optional[int] = Field(default=None, alias="TableSizeBytes")
    table_status: Optional[str] = Field(default=None, alias="TableStatus")


class AwsEc2LaunchTemplateDetailsModel(BaseModel):
    launch_template_name: Optional[str] = Field(
        default=None, alias="LaunchTemplateName"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    launch_template_data: Optional[AwsEc2LaunchTemplateDataDetailsModel] = Field(
        default=None, alias="LaunchTemplateData"
    )
    default_version_number: Optional[int] = Field(
        default=None, alias="DefaultVersionNumber"
    )
    latest_version_number: Optional[int] = Field(
        default=None, alias="LatestVersionNumber"
    )


class AwsEcsClusterDetailsModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    active_services_count: Optional[int] = Field(
        default=None, alias="ActiveServicesCount"
    )
    capacity_providers: Optional[Sequence[str]] = Field(
        default=None, alias="CapacityProviders"
    )
    cluster_settings: Optional[
        Sequence[AwsEcsClusterClusterSettingsDetailsModel]
    ] = Field(default=None, alias="ClusterSettings")
    configuration: Optional[AwsEcsClusterConfigurationDetailsModel] = Field(
        default=None, alias="Configuration"
    )
    default_capacity_provider_strategy: Optional[
        Sequence[AwsEcsClusterDefaultCapacityProviderStrategyDetailsModel]
    ] = Field(default=None, alias="DefaultCapacityProviderStrategy")
    cluster_name: Optional[str] = Field(default=None, alias="ClusterName")
    registered_container_instances_count: Optional[int] = Field(
        default=None, alias="RegisteredContainerInstancesCount"
    )
    running_tasks_count: Optional[int] = Field(default=None, alias="RunningTasksCount")
    status: Optional[str] = Field(default=None, alias="Status")


class AwsEcsTaskDefinitionDetailsModel(BaseModel):
    container_definitions: Optional[
        Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsModel]
    ] = Field(default=None, alias="ContainerDefinitions")
    cpu: Optional[str] = Field(default=None, alias="Cpu")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    family: Optional[str] = Field(default=None, alias="Family")
    inference_accelerators: Optional[
        Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsModel]
    ] = Field(default=None, alias="InferenceAccelerators")
    ipc_mode: Optional[str] = Field(default=None, alias="IpcMode")
    memory: Optional[str] = Field(default=None, alias="Memory")
    network_mode: Optional[str] = Field(default=None, alias="NetworkMode")
    pid_mode: Optional[str] = Field(default=None, alias="PidMode")
    placement_constraints: Optional[
        Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetailsModel]
    ] = Field(default=None, alias="PlacementConstraints")
    proxy_configuration: Optional[
        AwsEcsTaskDefinitionProxyConfigurationDetailsModel
    ] = Field(default=None, alias="ProxyConfiguration")
    requires_compatibilities: Optional[Sequence[str]] = Field(
        default=None, alias="RequiresCompatibilities"
    )
    task_role_arn: Optional[str] = Field(default=None, alias="TaskRoleArn")
    volumes: Optional[Sequence[AwsEcsTaskDefinitionVolumesDetailsModel]] = Field(
        default=None, alias="Volumes"
    )


class AwsRdsDbInstanceDetailsModel(BaseModel):
    associated_roles: Optional[Sequence[AwsRdsDbInstanceAssociatedRoleModel]] = Field(
        default=None, alias="AssociatedRoles"
    )
    cacertificate_identifier: Optional[str] = Field(
        default=None, alias="CACertificateIdentifier"
    )
    dbcluster_identifier: Optional[str] = Field(
        default=None, alias="DBClusterIdentifier"
    )
    dbinstance_identifier: Optional[str] = Field(
        default=None, alias="DBInstanceIdentifier"
    )
    dbinstance_class: Optional[str] = Field(default=None, alias="DBInstanceClass")
    db_instance_port: Optional[int] = Field(default=None, alias="DbInstancePort")
    dbi_resource_id: Optional[str] = Field(default=None, alias="DbiResourceId")
    dbname: Optional[str] = Field(default=None, alias="DBName")
    deletion_protection: Optional[bool] = Field(
        default=None, alias="DeletionProtection"
    )
    endpoint: Optional[AwsRdsDbInstanceEndpointModel] = Field(
        default=None, alias="Endpoint"
    )
    engine: Optional[str] = Field(default=None, alias="Engine")
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    iamdatabase_authentication_enabled: Optional[bool] = Field(
        default=None, alias="IAMDatabaseAuthenticationEnabled"
    )
    instance_create_time: Optional[str] = Field(
        default=None, alias="InstanceCreateTime"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    publicly_accessible: Optional[bool] = Field(
        default=None, alias="PubliclyAccessible"
    )
    storage_encrypted: Optional[bool] = Field(default=None, alias="StorageEncrypted")
    tde_credential_arn: Optional[str] = Field(default=None, alias="TdeCredentialArn")
    vpc_security_groups: Optional[
        Sequence[AwsRdsDbInstanceVpcSecurityGroupModel]
    ] = Field(default=None, alias="VpcSecurityGroups")
    multi_az: Optional[bool] = Field(default=None, alias="MultiAz")
    enhanced_monitoring_resource_arn: Optional[str] = Field(
        default=None, alias="EnhancedMonitoringResourceArn"
    )
    db_instance_status: Optional[str] = Field(default=None, alias="DbInstanceStatus")
    master_username: Optional[str] = Field(default=None, alias="MasterUsername")
    allocated_storage: Optional[int] = Field(default=None, alias="AllocatedStorage")
    preferred_backup_window: Optional[str] = Field(
        default=None, alias="PreferredBackupWindow"
    )
    backup_retention_period: Optional[int] = Field(
        default=None, alias="BackupRetentionPeriod"
    )
    db_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="DbSecurityGroups"
    )
    db_parameter_groups: Optional[Sequence[AwsRdsDbParameterGroupModel]] = Field(
        default=None, alias="DbParameterGroups"
    )
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    db_subnet_group: Optional[AwsRdsDbSubnetGroupModel] = Field(
        default=None, alias="DbSubnetGroup"
    )
    preferred_maintenance_window: Optional[str] = Field(
        default=None, alias="PreferredMaintenanceWindow"
    )
    pending_modified_values: Optional[AwsRdsDbPendingModifiedValuesModel] = Field(
        default=None, alias="PendingModifiedValues"
    )
    latest_restorable_time: Optional[str] = Field(
        default=None, alias="LatestRestorableTime"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    read_replica_source_dbinstance_identifier: Optional[str] = Field(
        default=None, alias="ReadReplicaSourceDBInstanceIdentifier"
    )
    read_replica_dbinstance_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="ReadReplicaDBInstanceIdentifiers"
    )
    read_replica_dbcluster_identifiers: Optional[Sequence[str]] = Field(
        default=None, alias="ReadReplicaDBClusterIdentifiers"
    )
    license_model: Optional[str] = Field(default=None, alias="LicenseModel")
    iops: Optional[int] = Field(default=None, alias="Iops")
    option_group_memberships: Optional[
        Sequence[AwsRdsDbOptionGroupMembershipModel]
    ] = Field(default=None, alias="OptionGroupMemberships")
    character_set_name: Optional[str] = Field(default=None, alias="CharacterSetName")
    secondary_availability_zone: Optional[str] = Field(
        default=None, alias="SecondaryAvailabilityZone"
    )
    status_infos: Optional[Sequence[AwsRdsDbStatusInfoModel]] = Field(
        default=None, alias="StatusInfos"
    )
    storage_type: Optional[str] = Field(default=None, alias="StorageType")
    domain_memberships: Optional[Sequence[AwsRdsDbDomainMembershipModel]] = Field(
        default=None, alias="DomainMemberships"
    )
    copy_tags_to_snapshot: Optional[bool] = Field(
        default=None, alias="CopyTagsToSnapshot"
    )
    monitoring_interval: Optional[int] = Field(default=None, alias="MonitoringInterval")
    monitoring_role_arn: Optional[str] = Field(default=None, alias="MonitoringRoleArn")
    promotion_tier: Optional[int] = Field(default=None, alias="PromotionTier")
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    performance_insights_enabled: Optional[bool] = Field(
        default=None, alias="PerformanceInsightsEnabled"
    )
    performance_insights_kms_key_id: Optional[str] = Field(
        default=None, alias="PerformanceInsightsKmsKeyId"
    )
    performance_insights_retention_period: Optional[int] = Field(
        default=None, alias="PerformanceInsightsRetentionPeriod"
    )
    enabled_cloud_watch_logs_exports: Optional[Sequence[str]] = Field(
        default=None, alias="EnabledCloudWatchLogsExports"
    )
    processor_features: Optional[Sequence[AwsRdsDbProcessorFeatureModel]] = Field(
        default=None, alias="ProcessorFeatures"
    )
    listener_endpoint: Optional[AwsRdsDbInstanceEndpointModel] = Field(
        default=None, alias="ListenerEndpoint"
    )
    max_allocated_storage: Optional[int] = Field(
        default=None, alias="MaxAllocatedStorage"
    )


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsModel(BaseModel):
    predicate: Optional[
        AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsModel
    ] = Field(default=None, alias="Predicate")


class AwsS3BucketNotificationConfigurationDetailModel(BaseModel):
    events: Optional[Sequence[str]] = Field(default=None, alias="Events")
    filter: Optional[AwsS3BucketNotificationConfigurationFilterModel] = Field(
        default=None, alias="Filter"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")
    type: Optional[str] = Field(default=None, alias="Type")


class AwsWafv2RulesActionDetailsModel(BaseModel):
    allow: Optional[AwsWafv2ActionAllowDetailsModel] = Field(
        default=None, alias="Allow"
    )
    block: Optional[AwsWafv2ActionBlockDetailsModel] = Field(
        default=None, alias="Block"
    )
    captcha: Optional[AwsWafv2RulesActionCaptchaDetailsModel] = Field(
        default=None, alias="Captcha"
    )
    count: Optional[AwsWafv2RulesActionCountDetailsModel] = Field(
        default=None, alias="Count"
    )


class AwsWafv2WebAclActionDetailsModel(BaseModel):
    allow: Optional[AwsWafv2ActionAllowDetailsModel] = Field(
        default=None, alias="Allow"
    )
    block: Optional[AwsWafv2ActionBlockDetailsModel] = Field(
        default=None, alias="Block"
    )


class CreateInsightRequestModel(BaseModel):
    name: str = Field(alias="Name")
    filters: AwsSecurityFindingFiltersModel = Field(alias="Filters")
    group_by_attribute: str = Field(alias="GroupByAttribute")


class GetFindingsRequestGetFindingsPaginateModel(BaseModel):
    filters: Optional[AwsSecurityFindingFiltersModel] = Field(
        default=None, alias="Filters"
    )
    sort_criteria: Optional[Sequence[SortCriterionModel]] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetFindingsRequestModel(BaseModel):
    filters: Optional[AwsSecurityFindingFiltersModel] = Field(
        default=None, alias="Filters"
    )
    sort_criteria: Optional[Sequence[SortCriterionModel]] = Field(
        default=None, alias="SortCriteria"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class InsightModel(BaseModel):
    insight_arn: str = Field(alias="InsightArn")
    name: str = Field(alias="Name")
    filters: AwsSecurityFindingFiltersModel = Field(alias="Filters")
    group_by_attribute: str = Field(alias="GroupByAttribute")


class UpdateFindingsRequestModel(BaseModel):
    filters: AwsSecurityFindingFiltersModel = Field(alias="Filters")
    note: Optional[NoteUpdateModel] = Field(default=None, alias="Note")
    record_state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(
        default=None, alias="RecordState"
    )


class UpdateInsightRequestModel(BaseModel):
    insight_arn: str = Field(alias="InsightArn")
    name: Optional[str] = Field(default=None, alias="Name")
    filters: Optional[AwsSecurityFindingFiltersModel] = Field(
        default=None, alias="Filters"
    )
    group_by_attribute: Optional[str] = Field(default=None, alias="GroupByAttribute")


class NetworkPathComponentModel(BaseModel):
    component_id: Optional[str] = Field(default=None, alias="ComponentId")
    component_type: Optional[str] = Field(default=None, alias="ComponentType")
    egress: Optional[NetworkHeaderModel] = Field(default=None, alias="Egress")
    ingress: Optional[NetworkHeaderModel] = Field(default=None, alias="Ingress")


class CustomDataIdentifiersDetectionsModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    occurrences: Optional[OccurrencesModel] = Field(default=None, alias="Occurrences")


class SensitiveDataDetectionsModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="Count")
    type: Optional[str] = Field(default=None, alias="Type")
    occurrences: Optional[OccurrencesModel] = Field(default=None, alias="Occurrences")


class RuleGroupSourceStatelessRulesDetailsModel(BaseModel):
    priority: Optional[int] = Field(default=None, alias="Priority")
    rule_definition: Optional[RuleGroupSourceStatelessRuleDefinitionModel] = Field(
        default=None, alias="RuleDefinition"
    )


class FirewallPolicyStatelessCustomActionsDetailsModel(BaseModel):
    action_definition: Optional[StatelessCustomActionDefinitionModel] = Field(
        default=None, alias="ActionDefinition"
    )
    action_name: Optional[str] = Field(default=None, alias="ActionName")


class RuleGroupSourceCustomActionsDetailsModel(BaseModel):
    action_definition: Optional[StatelessCustomActionDefinitionModel] = Field(
        default=None, alias="ActionDefinition"
    )
    action_name: Optional[str] = Field(default=None, alias="ActionName")


class ActionModel(BaseModel):
    action_type: Optional[str] = Field(default=None, alias="ActionType")
    network_connection_action: Optional[NetworkConnectionActionModel] = Field(
        default=None, alias="NetworkConnectionAction"
    )
    aws_api_call_action: Optional[AwsApiCallActionModel] = Field(
        default=None, alias="AwsApiCallAction"
    )
    dns_request_action: Optional[DnsRequestActionModel] = Field(
        default=None, alias="DnsRequestAction"
    )
    port_probe_action: Optional[PortProbeActionModel] = Field(
        default=None, alias="PortProbeAction"
    )


class AwsBackupBackupPlanDetailsModel(BaseModel):
    backup_plan: Optional[AwsBackupBackupPlanBackupPlanDetailsModel] = Field(
        default=None, alias="BackupPlan"
    )
    backup_plan_arn: Optional[str] = Field(default=None, alias="BackupPlanArn")
    backup_plan_id: Optional[str] = Field(default=None, alias="BackupPlanId")
    version_id: Optional[str] = Field(default=None, alias="VersionId")


class AwsCloudFrontDistributionDetailsModel(BaseModel):
    cache_behaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsModel] = Field(
        default=None, alias="CacheBehaviors"
    )
    default_cache_behavior: Optional[
        AwsCloudFrontDistributionDefaultCacheBehaviorModel
    ] = Field(default=None, alias="DefaultCacheBehavior")
    default_root_object: Optional[str] = Field(default=None, alias="DefaultRootObject")
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    etag: Optional[str] = Field(default=None, alias="ETag")
    last_modified_time: Optional[str] = Field(default=None, alias="LastModifiedTime")
    logging: Optional[AwsCloudFrontDistributionLoggingModel] = Field(
        default=None, alias="Logging"
    )
    origins: Optional[AwsCloudFrontDistributionOriginsModel] = Field(
        default=None, alias="Origins"
    )
    origin_groups: Optional[AwsCloudFrontDistributionOriginGroupsModel] = Field(
        default=None, alias="OriginGroups"
    )
    viewer_certificate: Optional[
        AwsCloudFrontDistributionViewerCertificateModel
    ] = Field(default=None, alias="ViewerCertificate")
    status: Optional[str] = Field(default=None, alias="Status")
    web_acl_id: Optional[str] = Field(default=None, alias="WebAclId")


class AwsS3BucketBucketLifecycleConfigurationRulesDetailsModel(BaseModel):
    abort_incomplete_multipart_upload: Optional[
        AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsModel
    ] = Field(default=None, alias="AbortIncompleteMultipartUpload")
    expiration_date: Optional[str] = Field(default=None, alias="ExpirationDate")
    expiration_in_days: Optional[int] = Field(default=None, alias="ExpirationInDays")
    expired_object_delete_marker: Optional[bool] = Field(
        default=None, alias="ExpiredObjectDeleteMarker"
    )
    filter: Optional[
        AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsModel
    ] = Field(default=None, alias="Filter")
    id: Optional[str] = Field(default=None, alias="ID")
    noncurrent_version_expiration_in_days: Optional[int] = Field(
        default=None, alias="NoncurrentVersionExpirationInDays"
    )
    noncurrent_version_transitions: Optional[
        Sequence[
            AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsModel
        ]
    ] = Field(default=None, alias="NoncurrentVersionTransitions")
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    status: Optional[str] = Field(default=None, alias="Status")
    transitions: Optional[
        Sequence[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsModel]
    ] = Field(default=None, alias="Transitions")


class AwsS3BucketNotificationConfigurationModel(BaseModel):
    configurations: Optional[
        Sequence[AwsS3BucketNotificationConfigurationDetailModel]
    ] = Field(default=None, alias="Configurations")


class AwsWafv2RulesDetailsModel(BaseModel):
    action: Optional[AwsWafv2RulesActionDetailsModel] = Field(
        default=None, alias="Action"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    override_action: Optional[str] = Field(default=None, alias="OverrideAction")
    priority: Optional[int] = Field(default=None, alias="Priority")
    visibility_config: Optional[AwsWafv2VisibilityConfigDetailsModel] = Field(
        default=None, alias="VisibilityConfig"
    )


class GetInsightsResponseModel(BaseModel):
    insights: List[InsightModel] = Field(alias="Insights")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomDataIdentifiersResultModel(BaseModel):
    detections: Optional[Sequence[CustomDataIdentifiersDetectionsModel]] = Field(
        default=None, alias="Detections"
    )
    total_count: Optional[int] = Field(default=None, alias="TotalCount")


class SensitiveDataResultModel(BaseModel):
    category: Optional[str] = Field(default=None, alias="Category")
    detections: Optional[Sequence[SensitiveDataDetectionsModel]] = Field(
        default=None, alias="Detections"
    )
    total_count: Optional[int] = Field(default=None, alias="TotalCount")


class FirewallPolicyDetailsModel(BaseModel):
    stateful_rule_group_references: Optional[
        Sequence[FirewallPolicyStatefulRuleGroupReferencesDetailsModel]
    ] = Field(default=None, alias="StatefulRuleGroupReferences")
    stateless_custom_actions: Optional[
        Sequence[FirewallPolicyStatelessCustomActionsDetailsModel]
    ] = Field(default=None, alias="StatelessCustomActions")
    stateless_default_actions: Optional[Sequence[str]] = Field(
        default=None, alias="StatelessDefaultActions"
    )
    stateless_fragment_default_actions: Optional[Sequence[str]] = Field(
        default=None, alias="StatelessFragmentDefaultActions"
    )
    stateless_rule_group_references: Optional[
        Sequence[FirewallPolicyStatelessRuleGroupReferencesDetailsModel]
    ] = Field(default=None, alias="StatelessRuleGroupReferences")


class RuleGroupSourceStatelessRulesAndCustomActionsDetailsModel(BaseModel):
    custom_actions: Optional[
        Sequence[RuleGroupSourceCustomActionsDetailsModel]
    ] = Field(default=None, alias="CustomActions")
    stateless_rules: Optional[
        Sequence[RuleGroupSourceStatelessRulesDetailsModel]
    ] = Field(default=None, alias="StatelessRules")


class AwsS3BucketBucketLifecycleConfigurationDetailsModel(BaseModel):
    rules: Optional[
        Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsModel]
    ] = Field(default=None, alias="Rules")


class AwsWafv2RuleGroupDetailsModel(BaseModel):
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    description: Optional[str] = Field(default=None, alias="Description")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    rules: Optional[Sequence[AwsWafv2RulesDetailsModel]] = Field(
        default=None, alias="Rules"
    )
    scope: Optional[str] = Field(default=None, alias="Scope")
    visibility_config: Optional[AwsWafv2VisibilityConfigDetailsModel] = Field(
        default=None, alias="VisibilityConfig"
    )


class AwsWafv2WebAclDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    managedby_firewall_manager: Optional[bool] = Field(
        default=None, alias="ManagedbyFirewallManager"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    captcha_config: Optional[AwsWafv2WebAclCaptchaConfigDetailsModel] = Field(
        default=None, alias="CaptchaConfig"
    )
    default_action: Optional[AwsWafv2WebAclActionDetailsModel] = Field(
        default=None, alias="DefaultAction"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    rules: Optional[Sequence[AwsWafv2RulesDetailsModel]] = Field(
        default=None, alias="Rules"
    )
    visibility_config: Optional[AwsWafv2VisibilityConfigDetailsModel] = Field(
        default=None, alias="VisibilityConfig"
    )


class ClassificationResultModel(BaseModel):
    mime_type: Optional[str] = Field(default=None, alias="MimeType")
    size_classified: Optional[int] = Field(default=None, alias="SizeClassified")
    additional_occurrences: Optional[bool] = Field(
        default=None, alias="AdditionalOccurrences"
    )
    status: Optional[ClassificationStatusModel] = Field(default=None, alias="Status")
    sensitive_data: Optional[Sequence[SensitiveDataResultModel]] = Field(
        default=None, alias="SensitiveData"
    )
    custom_data_identifiers: Optional[CustomDataIdentifiersResultModel] = Field(
        default=None, alias="CustomDataIdentifiers"
    )


class AwsNetworkFirewallFirewallPolicyDetailsModel(BaseModel):
    firewall_policy: Optional[FirewallPolicyDetailsModel] = Field(
        default=None, alias="FirewallPolicy"
    )
    firewall_policy_arn: Optional[str] = Field(default=None, alias="FirewallPolicyArn")
    firewall_policy_id: Optional[str] = Field(default=None, alias="FirewallPolicyId")
    firewall_policy_name: Optional[str] = Field(
        default=None, alias="FirewallPolicyName"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class RuleGroupSourceModel(BaseModel):
    rules_source_list: Optional[RuleGroupSourceListDetailsModel] = Field(
        default=None, alias="RulesSourceList"
    )
    rules_string: Optional[str] = Field(default=None, alias="RulesString")
    stateful_rules: Optional[
        Sequence[RuleGroupSourceStatefulRulesDetailsModel]
    ] = Field(default=None, alias="StatefulRules")
    stateless_rules_and_custom_actions: Optional[
        RuleGroupSourceStatelessRulesAndCustomActionsDetailsModel
    ] = Field(default=None, alias="StatelessRulesAndCustomActions")


class AwsS3BucketDetailsModel(BaseModel):
    owner_id: Optional[str] = Field(default=None, alias="OwnerId")
    owner_name: Optional[str] = Field(default=None, alias="OwnerName")
    owner_account_id: Optional[str] = Field(default=None, alias="OwnerAccountId")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    server_side_encryption_configuration: Optional[
        AwsS3BucketServerSideEncryptionConfigurationModel
    ] = Field(default=None, alias="ServerSideEncryptionConfiguration")
    bucket_lifecycle_configuration: Optional[
        AwsS3BucketBucketLifecycleConfigurationDetailsModel
    ] = Field(default=None, alias="BucketLifecycleConfiguration")
    public_access_block_configuration: Optional[
        AwsS3AccountPublicAccessBlockDetailsModel
    ] = Field(default=None, alias="PublicAccessBlockConfiguration")
    access_control_list: Optional[str] = Field(default=None, alias="AccessControlList")
    bucket_logging_configuration: Optional[
        AwsS3BucketLoggingConfigurationModel
    ] = Field(default=None, alias="BucketLoggingConfiguration")
    bucket_website_configuration: Optional[
        AwsS3BucketWebsiteConfigurationModel
    ] = Field(default=None, alias="BucketWebsiteConfiguration")
    bucket_notification_configuration: Optional[
        AwsS3BucketNotificationConfigurationModel
    ] = Field(default=None, alias="BucketNotificationConfiguration")
    bucket_versioning_configuration: Optional[
        AwsS3BucketBucketVersioningConfigurationModel
    ] = Field(default=None, alias="BucketVersioningConfiguration")


class DataClassificationDetailsModel(BaseModel):
    detailed_results_location: Optional[str] = Field(
        default=None, alias="DetailedResultsLocation"
    )
    result: Optional[ClassificationResultModel] = Field(default=None, alias="Result")


class RuleGroupDetailsModel(BaseModel):
    rule_variables: Optional[RuleGroupVariablesModel] = Field(
        default=None, alias="RuleVariables"
    )
    rules_source: Optional[RuleGroupSourceModel] = Field(
        default=None, alias="RulesSource"
    )


class AwsNetworkFirewallRuleGroupDetailsModel(BaseModel):
    capacity: Optional[int] = Field(default=None, alias="Capacity")
    description: Optional[str] = Field(default=None, alias="Description")
    rule_group: Optional[RuleGroupDetailsModel] = Field(default=None, alias="RuleGroup")
    rule_group_arn: Optional[str] = Field(default=None, alias="RuleGroupArn")
    rule_group_id: Optional[str] = Field(default=None, alias="RuleGroupId")
    rule_group_name: Optional[str] = Field(default=None, alias="RuleGroupName")
    type: Optional[str] = Field(default=None, alias="Type")


class ResourceDetailsModel(BaseModel):
    aws_auto_scaling_auto_scaling_group: Optional[
        AwsAutoScalingAutoScalingGroupDetailsModel
    ] = Field(default=None, alias="AwsAutoScalingAutoScalingGroup")
    aws_code_build_project: Optional[AwsCodeBuildProjectDetailsModel] = Field(
        default=None, alias="AwsCodeBuildProject"
    )
    aws_cloud_front_distribution: Optional[
        AwsCloudFrontDistributionDetailsModel
    ] = Field(default=None, alias="AwsCloudFrontDistribution")
    aws_ec2_instance: Optional[AwsEc2InstanceDetailsModel] = Field(
        default=None, alias="AwsEc2Instance"
    )
    aws_ec2_network_interface: Optional[AwsEc2NetworkInterfaceDetailsModel] = Field(
        default=None, alias="AwsEc2NetworkInterface"
    )
    aws_ec2_security_group: Optional[AwsEc2SecurityGroupDetailsModel] = Field(
        default=None, alias="AwsEc2SecurityGroup"
    )
    aws_ec2_volume: Optional[AwsEc2VolumeDetailsModel] = Field(
        default=None, alias="AwsEc2Volume"
    )
    aws_ec2_vpc: Optional[AwsEc2VpcDetailsModel] = Field(
        default=None, alias="AwsEc2Vpc"
    )
    aws_ec2_eip: Optional[AwsEc2EipDetailsModel] = Field(
        default=None, alias="AwsEc2Eip"
    )
    aws_ec2_subnet: Optional[AwsEc2SubnetDetailsModel] = Field(
        default=None, alias="AwsEc2Subnet"
    )
    aws_ec2_network_acl: Optional[AwsEc2NetworkAclDetailsModel] = Field(
        default=None, alias="AwsEc2NetworkAcl"
    )
    aws_elbv2_load_balancer: Optional[AwsElbv2LoadBalancerDetailsModel] = Field(
        default=None, alias="AwsElbv2LoadBalancer"
    )
    aws_elastic_beanstalk_environment: Optional[
        AwsElasticBeanstalkEnvironmentDetailsModel
    ] = Field(default=None, alias="AwsElasticBeanstalkEnvironment")
    aws_elasticsearch_domain: Optional[AwsElasticsearchDomainDetailsModel] = Field(
        default=None, alias="AwsElasticsearchDomain"
    )
    aws_s3_bucket: Optional[AwsS3BucketDetailsModel] = Field(
        default=None, alias="AwsS3Bucket"
    )
    aws_s3_account_public_access_block: Optional[
        AwsS3AccountPublicAccessBlockDetailsModel
    ] = Field(default=None, alias="AwsS3AccountPublicAccessBlock")
    aws_s3_object: Optional[AwsS3ObjectDetailsModel] = Field(
        default=None, alias="AwsS3Object"
    )
    aws_secrets_manager_secret: Optional[AwsSecretsManagerSecretDetailsModel] = Field(
        default=None, alias="AwsSecretsManagerSecret"
    )
    aws_iam_access_key: Optional[AwsIamAccessKeyDetailsModel] = Field(
        default=None, alias="AwsIamAccessKey"
    )
    aws_iam_user: Optional[AwsIamUserDetailsModel] = Field(
        default=None, alias="AwsIamUser"
    )
    aws_iam_policy: Optional[AwsIamPolicyDetailsModel] = Field(
        default=None, alias="AwsIamPolicy"
    )
    aws_api_gateway_v2_stage: Optional[AwsApiGatewayV2StageDetailsModel] = Field(
        default=None, alias="AwsApiGatewayV2Stage"
    )
    aws_api_gateway_v2_api: Optional[AwsApiGatewayV2ApiDetailsModel] = Field(
        default=None, alias="AwsApiGatewayV2Api"
    )
    aws_dynamo_db_table: Optional[AwsDynamoDbTableDetailsModel] = Field(
        default=None, alias="AwsDynamoDbTable"
    )
    aws_api_gateway_stage: Optional[AwsApiGatewayStageDetailsModel] = Field(
        default=None, alias="AwsApiGatewayStage"
    )
    aws_api_gateway_rest_api: Optional[AwsApiGatewayRestApiDetailsModel] = Field(
        default=None, alias="AwsApiGatewayRestApi"
    )
    aws_cloud_trail_trail: Optional[AwsCloudTrailTrailDetailsModel] = Field(
        default=None, alias="AwsCloudTrailTrail"
    )
    aws_ssm_patch_compliance: Optional[AwsSsmPatchComplianceDetailsModel] = Field(
        default=None, alias="AwsSsmPatchCompliance"
    )
    aws_certificate_manager_certificate: Optional[
        AwsCertificateManagerCertificateDetailsModel
    ] = Field(default=None, alias="AwsCertificateManagerCertificate")
    aws_redshift_cluster: Optional[AwsRedshiftClusterDetailsModel] = Field(
        default=None, alias="AwsRedshiftCluster"
    )
    aws_elb_load_balancer: Optional[AwsElbLoadBalancerDetailsModel] = Field(
        default=None, alias="AwsElbLoadBalancer"
    )
    aws_iam_group: Optional[AwsIamGroupDetailsModel] = Field(
        default=None, alias="AwsIamGroup"
    )
    aws_iam_role: Optional[AwsIamRoleDetailsModel] = Field(
        default=None, alias="AwsIamRole"
    )
    aws_kms_key: Optional[AwsKmsKeyDetailsModel] = Field(
        default=None, alias="AwsKmsKey"
    )
    aws_lambda_function: Optional[AwsLambdaFunctionDetailsModel] = Field(
        default=None, alias="AwsLambdaFunction"
    )
    aws_lambda_layer_version: Optional[AwsLambdaLayerVersionDetailsModel] = Field(
        default=None, alias="AwsLambdaLayerVersion"
    )
    aws_rds_db_instance: Optional[AwsRdsDbInstanceDetailsModel] = Field(
        default=None, alias="AwsRdsDbInstance"
    )
    aws_sns_topic: Optional[AwsSnsTopicDetailsModel] = Field(
        default=None, alias="AwsSnsTopic"
    )
    aws_sqs_queue: Optional[AwsSqsQueueDetailsModel] = Field(
        default=None, alias="AwsSqsQueue"
    )
    aws_waf_web_acl: Optional[AwsWafWebAclDetailsModel] = Field(
        default=None, alias="AwsWafWebAcl"
    )
    aws_rds_db_snapshot: Optional[AwsRdsDbSnapshotDetailsModel] = Field(
        default=None, alias="AwsRdsDbSnapshot"
    )
    aws_rds_db_cluster_snapshot: Optional[AwsRdsDbClusterSnapshotDetailsModel] = Field(
        default=None, alias="AwsRdsDbClusterSnapshot"
    )
    aws_rds_db_cluster: Optional[AwsRdsDbClusterDetailsModel] = Field(
        default=None, alias="AwsRdsDbCluster"
    )
    aws_ecs_cluster: Optional[AwsEcsClusterDetailsModel] = Field(
        default=None, alias="AwsEcsCluster"
    )
    aws_ecs_container: Optional[AwsEcsContainerDetailsModel] = Field(
        default=None, alias="AwsEcsContainer"
    )
    aws_ecs_task_definition: Optional[AwsEcsTaskDefinitionDetailsModel] = Field(
        default=None, alias="AwsEcsTaskDefinition"
    )
    container: Optional[ContainerDetailsModel] = Field(default=None, alias="Container")
    other: Optional[Mapping[str, str]] = Field(default=None, alias="Other")
    aws_rds_event_subscription: Optional[AwsRdsEventSubscriptionDetailsModel] = Field(
        default=None, alias="AwsRdsEventSubscription"
    )
    aws_ecs_service: Optional[AwsEcsServiceDetailsModel] = Field(
        default=None, alias="AwsEcsService"
    )
    aws_auto_scaling_launch_configuration: Optional[
        AwsAutoScalingLaunchConfigurationDetailsModel
    ] = Field(default=None, alias="AwsAutoScalingLaunchConfiguration")
    aws_ec2_vpn_connection: Optional[AwsEc2VpnConnectionDetailsModel] = Field(
        default=None, alias="AwsEc2VpnConnection"
    )
    aws_ecr_container_image: Optional[AwsEcrContainerImageDetailsModel] = Field(
        default=None, alias="AwsEcrContainerImage"
    )
    aws_open_search_service_domain: Optional[
        AwsOpenSearchServiceDomainDetailsModel
    ] = Field(default=None, alias="AwsOpenSearchServiceDomain")
    aws_ec2_vpc_endpoint_service: Optional[
        AwsEc2VpcEndpointServiceDetailsModel
    ] = Field(default=None, alias="AwsEc2VpcEndpointService")
    aws_xray_encryption_config: Optional[AwsXrayEncryptionConfigDetailsModel] = Field(
        default=None, alias="AwsXrayEncryptionConfig"
    )
    aws_waf_rate_based_rule: Optional[AwsWafRateBasedRuleDetailsModel] = Field(
        default=None, alias="AwsWafRateBasedRule"
    )
    aws_waf_regional_rate_based_rule: Optional[
        AwsWafRegionalRateBasedRuleDetailsModel
    ] = Field(default=None, alias="AwsWafRegionalRateBasedRule")
    aws_ecr_repository: Optional[AwsEcrRepositoryDetailsModel] = Field(
        default=None, alias="AwsEcrRepository"
    )
    aws_eks_cluster: Optional[AwsEksClusterDetailsModel] = Field(
        default=None, alias="AwsEksCluster"
    )
    aws_network_firewall_firewall_policy: Optional[
        AwsNetworkFirewallFirewallPolicyDetailsModel
    ] = Field(default=None, alias="AwsNetworkFirewallFirewallPolicy")
    aws_network_firewall_firewall: Optional[
        AwsNetworkFirewallFirewallDetailsModel
    ] = Field(default=None, alias="AwsNetworkFirewallFirewall")
    aws_network_firewall_rule_group: Optional[
        AwsNetworkFirewallRuleGroupDetailsModel
    ] = Field(default=None, alias="AwsNetworkFirewallRuleGroup")
    aws_rds_db_security_group: Optional[AwsRdsDbSecurityGroupDetailsModel] = Field(
        default=None, alias="AwsRdsDbSecurityGroup"
    )
    aws_kinesis_stream: Optional[AwsKinesisStreamDetailsModel] = Field(
        default=None, alias="AwsKinesisStream"
    )
    aws_ec2_transit_gateway: Optional[AwsEc2TransitGatewayDetailsModel] = Field(
        default=None, alias="AwsEc2TransitGateway"
    )
    aws_efs_access_point: Optional[AwsEfsAccessPointDetailsModel] = Field(
        default=None, alias="AwsEfsAccessPoint"
    )
    aws_cloud_formation_stack: Optional[AwsCloudFormationStackDetailsModel] = Field(
        default=None, alias="AwsCloudFormationStack"
    )
    aws_cloud_watch_alarm: Optional[AwsCloudWatchAlarmDetailsModel] = Field(
        default=None, alias="AwsCloudWatchAlarm"
    )
    aws_ec2_vpc_peering_connection: Optional[
        AwsEc2VpcPeeringConnectionDetailsModel
    ] = Field(default=None, alias="AwsEc2VpcPeeringConnection")
    aws_waf_regional_rule_group: Optional[AwsWafRegionalRuleGroupDetailsModel] = Field(
        default=None, alias="AwsWafRegionalRuleGroup"
    )
    aws_waf_regional_rule: Optional[AwsWafRegionalRuleDetailsModel] = Field(
        default=None, alias="AwsWafRegionalRule"
    )
    aws_waf_regional_web_acl: Optional[AwsWafRegionalWebAclDetailsModel] = Field(
        default=None, alias="AwsWafRegionalWebAcl"
    )
    aws_waf_rule: Optional[AwsWafRuleDetailsModel] = Field(
        default=None, alias="AwsWafRule"
    )
    aws_waf_rule_group: Optional[AwsWafRuleGroupDetailsModel] = Field(
        default=None, alias="AwsWafRuleGroup"
    )
    aws_ecs_task: Optional[AwsEcsTaskDetailsModel] = Field(
        default=None, alias="AwsEcsTask"
    )
    aws_backup_backup_vault: Optional[AwsBackupBackupVaultDetailsModel] = Field(
        default=None, alias="AwsBackupBackupVault"
    )
    aws_backup_backup_plan: Optional[AwsBackupBackupPlanDetailsModel] = Field(
        default=None, alias="AwsBackupBackupPlan"
    )
    aws_backup_recovery_point: Optional[AwsBackupRecoveryPointDetailsModel] = Field(
        default=None, alias="AwsBackupRecoveryPoint"
    )
    aws_ec2_launch_template: Optional[AwsEc2LaunchTemplateDetailsModel] = Field(
        default=None, alias="AwsEc2LaunchTemplate"
    )
    aws_sage_maker_notebook_instance: Optional[
        AwsSageMakerNotebookInstanceDetailsModel
    ] = Field(default=None, alias="AwsSageMakerNotebookInstance")
    aws_wafv2_web_acl: Optional[AwsWafv2WebAclDetailsModel] = Field(
        default=None, alias="AwsWafv2WebAcl"
    )
    aws_wafv2_rule_group: Optional[AwsWafv2RuleGroupDetailsModel] = Field(
        default=None, alias="AwsWafv2RuleGroup"
    )


class ResourceModel(BaseModel):
    type: str = Field(alias="Type")
    id: str = Field(alias="Id")
    partition: Optional[Literal["aws", "aws-cn", "aws-us-gov"]] = Field(
        default=None, alias="Partition"
    )
    region: Optional[str] = Field(default=None, alias="Region")
    resource_role: Optional[str] = Field(default=None, alias="ResourceRole")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    data_classification: Optional[DataClassificationDetailsModel] = Field(
        default=None, alias="DataClassification"
    )
    details: Optional[ResourceDetailsModel] = Field(default=None, alias="Details")


class AwsSecurityFindingModel(BaseModel):
    schema_version: str = Field(alias="SchemaVersion")
    id: str = Field(alias="Id")
    product_arn: str = Field(alias="ProductArn")
    generator_id: str = Field(alias="GeneratorId")
    aws_account_id: str = Field(alias="AwsAccountId")
    created_at: str = Field(alias="CreatedAt")
    updated_at: str = Field(alias="UpdatedAt")
    title: str = Field(alias="Title")
    description: str = Field(alias="Description")
    resources: Sequence[ResourceModel] = Field(alias="Resources")
    product_name: Optional[str] = Field(default=None, alias="ProductName")
    company_name: Optional[str] = Field(default=None, alias="CompanyName")
    region: Optional[str] = Field(default=None, alias="Region")
    types: Optional[Sequence[str]] = Field(default=None, alias="Types")
    first_observed_at: Optional[str] = Field(default=None, alias="FirstObservedAt")
    last_observed_at: Optional[str] = Field(default=None, alias="LastObservedAt")
    severity: Optional[SeverityModel] = Field(default=None, alias="Severity")
    confidence: Optional[int] = Field(default=None, alias="Confidence")
    criticality: Optional[int] = Field(default=None, alias="Criticality")
    remediation: Optional[RemediationModel] = Field(default=None, alias="Remediation")
    source_url: Optional[str] = Field(default=None, alias="SourceUrl")
    product_fields: Optional[Mapping[str, str]] = Field(
        default=None, alias="ProductFields"
    )
    user_defined_fields: Optional[Mapping[str, str]] = Field(
        default=None, alias="UserDefinedFields"
    )
    malware: Optional[Sequence[MalwareModel]] = Field(default=None, alias="Malware")
    network: Optional[NetworkModel] = Field(default=None, alias="Network")
    network_path: Optional[Sequence[NetworkPathComponentModel]] = Field(
        default=None, alias="NetworkPath"
    )
    process: Optional[ProcessDetailsModel] = Field(default=None, alias="Process")
    threats: Optional[Sequence[ThreatModel]] = Field(default=None, alias="Threats")
    threat_intel_indicators: Optional[Sequence[ThreatIntelIndicatorModel]] = Field(
        default=None, alias="ThreatIntelIndicators"
    )
    compliance: Optional[ComplianceModel] = Field(default=None, alias="Compliance")
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="VerificationState")
    workflow_state: Optional[
        Literal["ASSIGNED", "DEFERRED", "IN_PROGRESS", "NEW", "RESOLVED"]
    ] = Field(default=None, alias="WorkflowState")
    workflow: Optional[WorkflowModel] = Field(default=None, alias="Workflow")
    record_state: Optional[Literal["ACTIVE", "ARCHIVED"]] = Field(
        default=None, alias="RecordState"
    )
    related_findings: Optional[Sequence[RelatedFindingModel]] = Field(
        default=None, alias="RelatedFindings"
    )
    note: Optional[NoteModel] = Field(default=None, alias="Note")
    vulnerabilities: Optional[Sequence[VulnerabilityModel]] = Field(
        default=None, alias="Vulnerabilities"
    )
    patch_summary: Optional[PatchSummaryModel] = Field(
        default=None, alias="PatchSummary"
    )
    action: Optional[ActionModel] = Field(default=None, alias="Action")
    finding_provider_fields: Optional[FindingProviderFieldsModel] = Field(
        default=None, alias="FindingProviderFields"
    )
    sample: Optional[bool] = Field(default=None, alias="Sample")


class BatchImportFindingsRequestModel(BaseModel):
    findings: Sequence[AwsSecurityFindingModel] = Field(alias="Findings")


class GetFindingsResponseModel(BaseModel):
    findings: List[AwsSecurityFindingModel] = Field(alias="Findings")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
