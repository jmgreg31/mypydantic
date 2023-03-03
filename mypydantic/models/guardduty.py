# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptAdministratorInvitationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    administrator_id: str = Field(alias="AdministratorId")
    invitation_id: str = Field(alias="InvitationId")


class AcceptInvitationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    master_id: str = Field(alias="MasterId")
    invitation_id: str = Field(alias="InvitationId")


class AccessControlListModel(BaseModel):
    allows_public_read_access: Optional[bool] = Field(
        default=None, alias="AllowsPublicReadAccess"
    )
    allows_public_write_access: Optional[bool] = Field(
        default=None, alias="AllowsPublicWriteAccess"
    )


class AccessKeyDetailsModel(BaseModel):
    access_key_id: Optional[str] = Field(default=None, alias="AccessKeyId")
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    user_type: Optional[str] = Field(default=None, alias="UserType")


class AccountDetailModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    email: str = Field(alias="Email")


class BlockPublicAccessModel(BaseModel):
    ignore_public_acls: Optional[bool] = Field(default=None, alias="IgnorePublicAcls")
    restrict_public_buckets: Optional[bool] = Field(
        default=None, alias="RestrictPublicBuckets"
    )
    block_public_acls: Optional[bool] = Field(default=None, alias="BlockPublicAcls")
    block_public_policy: Optional[bool] = Field(default=None, alias="BlockPublicPolicy")


class DnsRequestActionModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    blocked: Optional[bool] = Field(default=None, alias="Blocked")


class AdminAccountModel(BaseModel):
    admin_account_id: Optional[str] = Field(default=None, alias="AdminAccountId")
    admin_status: Optional[Literal["DISABLE_IN_PROGRESS", "ENABLED"]] = Field(
        default=None, alias="AdminStatus"
    )


class AdministratorModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    invitation_id: Optional[str] = Field(default=None, alias="InvitationId")
    relationship_status: Optional[str] = Field(default=None, alias="RelationshipStatus")
    invited_at: Optional[str] = Field(default=None, alias="InvitedAt")


class ArchiveFindingsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_ids: Sequence[str] = Field(alias="FindingIds")


class DomainDetailsModel(BaseModel):
    domain: Optional[str] = Field(default=None, alias="Domain")


class RemoteAccountDetailsModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    affiliated: Optional[bool] = Field(default=None, alias="Affiliated")


class BucketPolicyModel(BaseModel):
    allows_public_read_access: Optional[bool] = Field(
        default=None, alias="AllowsPublicReadAccess"
    )
    allows_public_write_access: Optional[bool] = Field(
        default=None, alias="AllowsPublicWriteAccess"
    )


class CityModel(BaseModel):
    city_name: Optional[str] = Field(default=None, alias="CityName")


class CloudTrailConfigurationResultModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")


class ConditionModel(BaseModel):
    eq: Optional[Sequence[str]] = Field(default=None, alias="Eq")
    neq: Optional[Sequence[str]] = Field(default=None, alias="Neq")
    gt: Optional[int] = Field(default=None, alias="Gt")
    gte: Optional[int] = Field(default=None, alias="Gte")
    lt: Optional[int] = Field(default=None, alias="Lt")
    lte: Optional[int] = Field(default=None, alias="Lte")
    equals: Optional[Sequence[str]] = Field(default=None, alias="Equals")
    not_equals: Optional[Sequence[str]] = Field(default=None, alias="NotEquals")
    greater_than: Optional[int] = Field(default=None, alias="GreaterThan")
    greater_than_or_equal: Optional[int] = Field(
        default=None, alias="GreaterThanOrEqual"
    )
    less_than: Optional[int] = Field(default=None, alias="LessThan")
    less_than_or_equal: Optional[int] = Field(default=None, alias="LessThanOrEqual")


class SecurityContextModel(BaseModel):
    privileged: Optional[bool] = Field(default=None, alias="Privileged")


class VolumeMountModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    mount_path: Optional[str] = Field(default=None, alias="MountPath")


class CountryModel(BaseModel):
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    country_name: Optional[str] = Field(default=None, alias="CountryName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateIPSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    name: str = Field(alias="Name")
    format: Literal[
        "ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"
    ] = Field(alias="Format")
    location: str = Field(alias="Location")
    activate: bool = Field(alias="Activate")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UnprocessedAccountModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    result: str = Field(alias="Result")


class DestinationPropertiesModel(BaseModel):
    destination_arn: Optional[str] = Field(default=None, alias="DestinationArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class CreateSampleFindingsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_types: Optional[Sequence[str]] = Field(default=None, alias="FindingTypes")


class CreateThreatIntelSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    name: str = Field(alias="Name")
    format: Literal[
        "ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"
    ] = Field(alias="Format")
    location: str = Field(alias="Location")
    activate: bool = Field(alias="Activate")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class DNSLogsConfigurationResultModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")


class FlowLogsConfigurationResultModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")


class S3LogsConfigurationResultModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")


class S3LogsConfigurationModel(BaseModel):
    enable: bool = Field(alias="Enable")


class DataSourceFreeTrialModel(BaseModel):
    free_trial_days_remaining: Optional[int] = Field(
        default=None, alias="FreeTrialDaysRemaining"
    )


class DeclineInvitationsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class DefaultServerSideEncryptionModel(BaseModel):
    encryption_type: Optional[str] = Field(default=None, alias="EncryptionType")
    kms_master_key_arn: Optional[str] = Field(default=None, alias="KmsMasterKeyArn")


class DeleteDetectorRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class DeleteFilterRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    filter_name: str = Field(alias="FilterName")


class DeleteIPSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    ip_set_id: str = Field(alias="IpSetId")


class DeleteInvitationsRequestModel(BaseModel):
    account_ids: Sequence[str] = Field(alias="AccountIds")


class DeleteMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class DeletePublishingDestinationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    destination_id: str = Field(alias="DestinationId")


class DeleteThreatIntelSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    threat_intel_set_id: str = Field(alias="ThreatIntelSetId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class SortCriteriaModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    order_by: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="OrderBy")


class DescribeOrganizationConfigurationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class DescribePublishingDestinationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    destination_id: str = Field(alias="DestinationId")


class DestinationModel(BaseModel):
    destination_id: str = Field(alias="DestinationId")
    destination_type: Literal["S3"] = Field(alias="DestinationType")
    status: Literal[
        "PENDING_VERIFICATION",
        "PUBLISHING",
        "STOPPED",
        "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
    ] = Field(alias="Status")


class DisableOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: str = Field(alias="AdminAccountId")


class DisassociateFromAdministratorAccountRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class DisassociateFromMasterAccountRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class DisassociateMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class VolumeDetailModel(BaseModel):
    volume_arn: Optional[str] = Field(default=None, alias="VolumeArn")
    volume_type: Optional[str] = Field(default=None, alias="VolumeType")
    device_name: Optional[str] = Field(default=None, alias="DeviceName")
    volume_size_in_gb: Optional[int] = Field(default=None, alias="VolumeSizeInGB")
    encryption_type: Optional[str] = Field(default=None, alias="EncryptionType")
    snapshot_arn: Optional[str] = Field(default=None, alias="SnapshotArn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class EbsVolumesResultModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )
    reason: Optional[str] = Field(default=None, alias="Reason")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class EnableOrganizationAdminAccountRequestModel(BaseModel):
    admin_account_id: str = Field(alias="AdminAccountId")


class ThreatIntelligenceDetailModel(BaseModel):
    threat_list_name: Optional[str] = Field(default=None, alias="ThreatListName")
    threat_names: Optional[List[str]] = Field(default=None, alias="ThreatNames")


class FilterConditionModel(BaseModel):
    equals_value: Optional[str] = Field(default=None, alias="EqualsValue")
    greater_than: Optional[int] = Field(default=None, alias="GreaterThan")
    less_than: Optional[int] = Field(default=None, alias="LessThan")


class FindingStatisticsModel(BaseModel):
    count_by_severity: Optional[Dict[str, int]] = Field(
        default=None, alias="CountBySeverity"
    )


class GeoLocationModel(BaseModel):
    lat: Optional[float] = Field(default=None, alias="Lat")
    lon: Optional[float] = Field(default=None, alias="Lon")


class GetAdministratorAccountRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class GetDetectorRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class GetFilterRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    filter_name: str = Field(alias="FilterName")


class GetIPSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    ip_set_id: str = Field(alias="IpSetId")


class GetMalwareScanSettingsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class GetMasterAccountRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")


class MasterModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    invitation_id: Optional[str] = Field(default=None, alias="InvitationId")
    relationship_status: Optional[str] = Field(default=None, alias="RelationshipStatus")
    invited_at: Optional[str] = Field(default=None, alias="InvitedAt")


class GetMemberDetectorsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class GetMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class MemberModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    master_id: str = Field(alias="MasterId")
    email: str = Field(alias="Email")
    relationship_status: str = Field(alias="RelationshipStatus")
    updated_at: str = Field(alias="UpdatedAt")
    detector_id: Optional[str] = Field(default=None, alias="DetectorId")
    invited_at: Optional[str] = Field(default=None, alias="InvitedAt")
    administrator_id: Optional[str] = Field(default=None, alias="AdministratorId")


class GetRemainingFreeTrialDaysRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")


class GetThreatIntelSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    threat_intel_set_id: str = Field(alias="ThreatIntelSetId")


class UsageCriteriaModel(BaseModel):
    data_sources: Sequence[
        Literal[
            "CLOUD_TRAIL",
            "DNS_LOGS",
            "EC2_MALWARE_SCAN",
            "FLOW_LOGS",
            "KUBERNETES_AUDIT_LOGS",
            "S3_LOGS",
        ]
    ] = Field(alias="DataSources")
    account_ids: Optional[Sequence[str]] = Field(default=None, alias="AccountIds")
    resources: Optional[Sequence[str]] = Field(default=None, alias="Resources")


class HighestSeverityThreatDetailsModel(BaseModel):
    severity: Optional[str] = Field(default=None, alias="Severity")
    threat_name: Optional[str] = Field(default=None, alias="ThreatName")
    count: Optional[int] = Field(default=None, alias="Count")


class HostPathModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")


class IamInstanceProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")


class ProductCodeModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="Code")
    product_type: Optional[str] = Field(default=None, alias="ProductType")


class InvitationModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    invitation_id: Optional[str] = Field(default=None, alias="InvitationId")
    relationship_status: Optional[str] = Field(default=None, alias="RelationshipStatus")
    invited_at: Optional[str] = Field(default=None, alias="InvitedAt")


class InviteMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")
    disable_email_notification: Optional[bool] = Field(
        default=None, alias="DisableEmailNotification"
    )
    message: Optional[str] = Field(default=None, alias="Message")


class KubernetesAuditLogsConfigurationResultModel(BaseModel):
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")


class KubernetesAuditLogsConfigurationModel(BaseModel):
    enable: bool = Field(alias="Enable")


class KubernetesUserDetailsModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="Username")
    uid: Optional[str] = Field(default=None, alias="Uid")
    groups: Optional[List[str]] = Field(default=None, alias="Groups")


class ListDetectorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFiltersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListIPSetsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInvitationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    only_associated: Optional[str] = Field(default=None, alias="OnlyAssociated")


class ListOrganizationAdminAccountsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPublishingDestinationsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListThreatIntelSetsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class LocalIpDetailsModel(BaseModel):
    ip_address_v4: Optional[str] = Field(default=None, alias="IpAddressV4")


class LocalPortDetailsModel(BaseModel):
    port: Optional[int] = Field(default=None, alias="Port")
    port_name: Optional[str] = Field(default=None, alias="PortName")


class ScanEc2InstanceWithFindingsModel(BaseModel):
    ebs_volumes: Optional[bool] = Field(default=None, alias="EbsVolumes")


class RemotePortDetailsModel(BaseModel):
    port: Optional[int] = Field(default=None, alias="Port")
    port_name: Optional[str] = Field(default=None, alias="PortName")


class PrivateIpAddressDetailsModel(BaseModel):
    private_dns_name: Optional[str] = Field(default=None, alias="PrivateDnsName")
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")


class SecurityGroupModel(BaseModel):
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    group_name: Optional[str] = Field(default=None, alias="GroupName")


class OrganizationS3LogsConfigurationResultModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")


class OrganizationS3LogsConfigurationModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")


class OrganizationEbsVolumesResultModel(BaseModel):
    auto_enable: Optional[bool] = Field(default=None, alias="AutoEnable")


class OrganizationEbsVolumesModel(BaseModel):
    auto_enable: Optional[bool] = Field(default=None, alias="AutoEnable")


class OrganizationKubernetesAuditLogsConfigurationResultModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")


class OrganizationKubernetesAuditLogsConfigurationModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")


class OrganizationModel(BaseModel):
    asn: Optional[str] = Field(default=None, alias="Asn")
    asn_org: Optional[str] = Field(default=None, alias="AsnOrg")
    isp: Optional[str] = Field(default=None, alias="Isp")
    org: Optional[str] = Field(default=None, alias="Org")


class OwnerModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class ResourceDetailsModel(BaseModel):
    instance_arn: Optional[str] = Field(default=None, alias="InstanceArn")


class ScanConditionPairModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ScannedItemCountModel(BaseModel):
    total_gb: Optional[int] = Field(default=None, alias="TotalGb")
    files: Optional[int] = Field(default=None, alias="Files")
    volumes: Optional[int] = Field(default=None, alias="Volumes")


class ThreatsDetectedItemCountModel(BaseModel):
    files: Optional[int] = Field(default=None, alias="Files")


class ScanFilePathModel(BaseModel):
    file_path: Optional[str] = Field(default=None, alias="FilePath")
    volume_arn: Optional[str] = Field(default=None, alias="VolumeArn")
    hash: Optional[str] = Field(default=None, alias="Hash")
    file_name: Optional[str] = Field(default=None, alias="FileName")


class ScanResultDetailsModel(BaseModel):
    scan_result: Optional[Literal["CLEAN", "INFECTED"]] = Field(
        default=None, alias="ScanResult"
    )


class TriggerDetailsModel(BaseModel):
    guard_duty_finding_id: Optional[str] = Field(
        default=None, alias="GuardDutyFindingId"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ServiceAdditionalInfoModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    type: Optional[str] = Field(default=None, alias="Type")


class StartMonitoringMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class StopMonitoringMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class TotalModel(BaseModel):
    amount: Optional[str] = Field(default=None, alias="Amount")
    unit: Optional[str] = Field(default=None, alias="Unit")


class UnarchiveFindingsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_ids: Sequence[str] = Field(alias="FindingIds")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateFindingsFeedbackRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_ids: Sequence[str] = Field(alias="FindingIds")
    feedback: Literal["NOT_USEFUL", "USEFUL"] = Field(alias="Feedback")
    comments: Optional[str] = Field(default=None, alias="Comments")


class UpdateIPSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    ip_set_id: str = Field(alias="IpSetId")
    name: Optional[str] = Field(default=None, alias="Name")
    location: Optional[str] = Field(default=None, alias="Location")
    activate: Optional[bool] = Field(default=None, alias="Activate")


class UpdateThreatIntelSetRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    threat_intel_set_id: str = Field(alias="ThreatIntelSetId")
    name: Optional[str] = Field(default=None, alias="Name")
    location: Optional[str] = Field(default=None, alias="Location")
    activate: Optional[bool] = Field(default=None, alias="Activate")


class CreateMembersRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_details: Sequence[AccountDetailModel] = Field(alias="AccountDetails")


class AccountLevelPermissionsModel(BaseModel):
    block_public_access: Optional[BlockPublicAccessModel] = Field(
        default=None, alias="BlockPublicAccess"
    )


class BucketLevelPermissionsModel(BaseModel):
    access_control_list: Optional[AccessControlListModel] = Field(
        default=None, alias="AccessControlList"
    )
    bucket_policy: Optional[BucketPolicyModel] = Field(
        default=None, alias="BucketPolicy"
    )
    block_public_access: Optional[BlockPublicAccessModel] = Field(
        default=None, alias="BlockPublicAccess"
    )


class FindingCriteriaModel(BaseModel):
    criterion: Optional[Mapping[str, ConditionModel]] = Field(
        default=None, alias="Criterion"
    )


class ContainerModel(BaseModel):
    container_runtime: Optional[str] = Field(default=None, alias="ContainerRuntime")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    image: Optional[str] = Field(default=None, alias="Image")
    image_prefix: Optional[str] = Field(default=None, alias="ImagePrefix")
    volume_mounts: Optional[List[VolumeMountModel]] = Field(
        default=None, alias="VolumeMounts"
    )
    security_context: Optional[SecurityContextModel] = Field(
        default=None, alias="SecurityContext"
    )


class CreateFilterResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIPSetResponseModel(BaseModel):
    ip_set_id: str = Field(alias="IpSetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePublishingDestinationResponseModel(BaseModel):
    destination_id: str = Field(alias="DestinationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThreatIntelSetResponseModel(BaseModel):
    threat_intel_set_id: str = Field(alias="ThreatIntelSetId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAdministratorAccountResponseModel(BaseModel):
    administrator: AdministratorModel = Field(alias="Administrator")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIPSetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    format: Literal[
        "ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"
    ] = Field(alias="Format")
    location: str = Field(alias="Location")
    status: Literal[
        "ACTIVATING",
        "ACTIVE",
        "DEACTIVATING",
        "DELETED",
        "DELETE_PENDING",
        "ERROR",
        "INACTIVE",
    ] = Field(alias="Status")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInvitationsCountResponseModel(BaseModel):
    invitations_count: int = Field(alias="InvitationsCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetThreatIntelSetResponseModel(BaseModel):
    name: str = Field(alias="Name")
    format: Literal[
        "ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"
    ] = Field(alias="Format")
    location: str = Field(alias="Location")
    status: Literal[
        "ACTIVATING",
        "ACTIVE",
        "DEACTIVATING",
        "DELETED",
        "DELETE_PENDING",
        "ERROR",
        "INACTIVE",
    ] = Field(alias="Status")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDetectorsResponseModel(BaseModel):
    detector_ids: List[str] = Field(alias="DetectorIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFiltersResponseModel(BaseModel):
    filter_names: List[str] = Field(alias="FilterNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFindingsResponseModel(BaseModel):
    finding_ids: List[str] = Field(alias="FindingIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIPSetsResponseModel(BaseModel):
    ip_set_ids: List[str] = Field(alias="IpSetIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrganizationAdminAccountsResponseModel(BaseModel):
    admin_accounts: List[AdminAccountModel] = Field(alias="AdminAccounts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThreatIntelSetsResponseModel(BaseModel):
    threat_intel_set_ids: List[str] = Field(alias="ThreatIntelSetIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFilterResponseModel(BaseModel):
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMembersResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeclineInvitationsResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteInvitationsResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMembersResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateMembersResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InviteMembersResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartMonitoringMembersResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopMonitoringMembersResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMemberDetectorsResponseModel(BaseModel):
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePublishingDestinationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    destination_type: Literal["S3"] = Field(alias="DestinationType")
    destination_properties: DestinationPropertiesModel = Field(
        alias="DestinationProperties"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DescribePublishingDestinationResponseModel(BaseModel):
    destination_id: str = Field(alias="DestinationId")
    destination_type: Literal["S3"] = Field(alias="DestinationType")
    status: Literal[
        "PENDING_VERIFICATION",
        "PUBLISHING",
        "STOPPED",
        "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY",
    ] = Field(alias="Status")
    publishing_failure_start_timestamp: int = Field(
        alias="PublishingFailureStartTimestamp"
    )
    destination_properties: DestinationPropertiesModel = Field(
        alias="DestinationProperties"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePublishingDestinationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    destination_id: str = Field(alias="DestinationId")
    destination_properties: Optional[DestinationPropertiesModel] = Field(
        default=None, alias="DestinationProperties"
    )


class KubernetesDataSourceFreeTrialModel(BaseModel):
    audit_logs: Optional[DataSourceFreeTrialModel] = Field(
        default=None, alias="AuditLogs"
    )


class MalwareProtectionDataSourceFreeTrialModel(BaseModel):
    scan_ec2_instance_with_findings: Optional[DataSourceFreeTrialModel] = Field(
        default=None, alias="ScanEc2InstanceWithFindings"
    )


class ListDetectorsRequestListDetectorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFiltersRequestListFiltersPaginateModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIPSetsRequestListIPSetsPaginateModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInvitationsRequestListInvitationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembersRequestListMembersPaginateModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    only_associated: Optional[str] = Field(default=None, alias="OnlyAssociated")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThreatIntelSetsRequestListThreatIntelSetsPaginateModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetFindingsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_ids: Sequence[str] = Field(alias="FindingIds")
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="SortCriteria"
    )


class ListPublishingDestinationsResponseModel(BaseModel):
    destinations: List[DestinationModel] = Field(alias="Destinations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EbsVolumeDetailsModel(BaseModel):
    scanned_volume_details: Optional[List[VolumeDetailModel]] = Field(
        default=None, alias="ScannedVolumeDetails"
    )
    skipped_volume_details: Optional[List[VolumeDetailModel]] = Field(
        default=None, alias="SkippedVolumeDetails"
    )


class ScanEc2InstanceWithFindingsResultModel(BaseModel):
    ebs_volumes: Optional[EbsVolumesResultModel] = Field(
        default=None, alias="EbsVolumes"
    )


class EksClusterDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    status: Optional[str] = Field(default=None, alias="Status")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")


class EvidenceModel(BaseModel):
    threat_intelligence_details: Optional[List[ThreatIntelligenceDetailModel]] = Field(
        default=None, alias="ThreatIntelligenceDetails"
    )


class FilterCriterionModel(BaseModel):
    criterion_key: Optional[
        Literal[
            "ACCOUNT_ID",
            "EC2_INSTANCE_ARN",
            "GUARDDUTY_FINDING_ID",
            "SCAN_ID",
            "SCAN_START_TIME",
            "SCAN_STATUS",
        ]
    ] = Field(default=None, alias="CriterionKey")
    filter_condition: Optional[FilterConditionModel] = Field(
        default=None, alias="FilterCondition"
    )


class GetFindingsStatisticsResponseModel(BaseModel):
    finding_statistics: FindingStatisticsModel = Field(alias="FindingStatistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMasterAccountResponseModel(BaseModel):
    master: MasterModel = Field(alias="Master")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMembersResponseModel(BaseModel):
    members: List[MemberModel] = Field(alias="Members")
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMembersResponseModel(BaseModel):
    members: List[MemberModel] = Field(alias="Members")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUsageStatisticsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    usage_statistic_type: Literal[
        "SUM_BY_ACCOUNT", "SUM_BY_DATA_SOURCE", "SUM_BY_RESOURCE", "TOP_RESOURCES"
    ] = Field(alias="UsageStatisticType")
    usage_criteria: UsageCriteriaModel = Field(alias="UsageCriteria")
    unit: Optional[str] = Field(default=None, alias="Unit")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class VolumeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    host_path: Optional[HostPathModel] = Field(default=None, alias="HostPath")


class ListInvitationsResponseModel(BaseModel):
    invitations: List[InvitationModel] = Field(alias="Invitations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class KubernetesConfigurationResultModel(BaseModel):
    audit_logs: KubernetesAuditLogsConfigurationResultModel = Field(alias="AuditLogs")


class KubernetesConfigurationModel(BaseModel):
    audit_logs: KubernetesAuditLogsConfigurationModel = Field(alias="AuditLogs")


class MalwareProtectionConfigurationModel(BaseModel):
    scan_ec2_instance_with_findings: Optional[ScanEc2InstanceWithFindingsModel] = Field(
        default=None, alias="ScanEc2InstanceWithFindings"
    )


class NetworkInterfaceModel(BaseModel):
    ipv6_addresses: Optional[List[str]] = Field(default=None, alias="Ipv6Addresses")
    network_interface_id: Optional[str] = Field(
        default=None, alias="NetworkInterfaceId"
    )
    private_dns_name: Optional[str] = Field(default=None, alias="PrivateDnsName")
    private_ip_address: Optional[str] = Field(default=None, alias="PrivateIpAddress")
    private_ip_addresses: Optional[List[PrivateIpAddressDetailsModel]] = Field(
        default=None, alias="PrivateIpAddresses"
    )
    public_dns_name: Optional[str] = Field(default=None, alias="PublicDnsName")
    public_ip: Optional[str] = Field(default=None, alias="PublicIp")
    security_groups: Optional[List[SecurityGroupModel]] = Field(
        default=None, alias="SecurityGroups"
    )
    subnet_id: Optional[str] = Field(default=None, alias="SubnetId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")


class OrganizationScanEc2InstanceWithFindingsResultModel(BaseModel):
    ebs_volumes: Optional[OrganizationEbsVolumesResultModel] = Field(
        default=None, alias="EbsVolumes"
    )


class OrganizationScanEc2InstanceWithFindingsModel(BaseModel):
    ebs_volumes: Optional[OrganizationEbsVolumesModel] = Field(
        default=None, alias="EbsVolumes"
    )


class OrganizationKubernetesConfigurationResultModel(BaseModel):
    audit_logs: OrganizationKubernetesAuditLogsConfigurationResultModel = Field(
        alias="AuditLogs"
    )


class OrganizationKubernetesConfigurationModel(BaseModel):
    audit_logs: OrganizationKubernetesAuditLogsConfigurationModel = Field(
        alias="AuditLogs"
    )


class RemoteIpDetailsModel(BaseModel):
    city: Optional[CityModel] = Field(default=None, alias="City")
    country: Optional[CountryModel] = Field(default=None, alias="Country")
    geo_location: Optional[GeoLocationModel] = Field(default=None, alias="GeoLocation")
    ip_address_v4: Optional[str] = Field(default=None, alias="IpAddressV4")
    organization: Optional[OrganizationModel] = Field(
        default=None, alias="Organization"
    )


class ScanConditionModel(BaseModel):
    map_equals: List[ScanConditionPairModel] = Field(alias="MapEquals")


class ScanThreatNameModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    severity: Optional[str] = Field(default=None, alias="Severity")
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    file_paths: Optional[List[ScanFilePathModel]] = Field(
        default=None, alias="FilePaths"
    )


class ScanModel(BaseModel):
    detector_id: Optional[str] = Field(default=None, alias="DetectorId")
    admin_detector_id: Optional[str] = Field(default=None, alias="AdminDetectorId")
    scan_id: Optional[str] = Field(default=None, alias="ScanId")
    scan_status: Optional[Literal["COMPLETED", "FAILED", "RUNNING"]] = Field(
        default=None, alias="ScanStatus"
    )
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    scan_start_time: Optional[datetime] = Field(default=None, alias="ScanStartTime")
    scan_end_time: Optional[datetime] = Field(default=None, alias="ScanEndTime")
    trigger_details: Optional[TriggerDetailsModel] = Field(
        default=None, alias="TriggerDetails"
    )
    resource_details: Optional[ResourceDetailsModel] = Field(
        default=None, alias="ResourceDetails"
    )
    scan_result_details: Optional[ScanResultDetailsModel] = Field(
        default=None, alias="ScanResultDetails"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    total_bytes: Optional[int] = Field(default=None, alias="TotalBytes")
    file_count: Optional[int] = Field(default=None, alias="FileCount")
    attached_volumes: Optional[List[VolumeDetailModel]] = Field(
        default=None, alias="AttachedVolumes"
    )


class UsageAccountResultModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    total: Optional[TotalModel] = Field(default=None, alias="Total")


class UsageDataSourceResultModel(BaseModel):
    data_source: Optional[
        Literal[
            "CLOUD_TRAIL",
            "DNS_LOGS",
            "EC2_MALWARE_SCAN",
            "FLOW_LOGS",
            "KUBERNETES_AUDIT_LOGS",
            "S3_LOGS",
        ]
    ] = Field(default=None, alias="DataSource")
    total: Optional[TotalModel] = Field(default=None, alias="Total")


class UsageResourceResultModel(BaseModel):
    resource: Optional[str] = Field(default=None, alias="Resource")
    total: Optional[TotalModel] = Field(default=None, alias="Total")


class PermissionConfigurationModel(BaseModel):
    bucket_level_permissions: Optional[BucketLevelPermissionsModel] = Field(
        default=None, alias="BucketLevelPermissions"
    )
    account_level_permissions: Optional[AccountLevelPermissionsModel] = Field(
        default=None, alias="AccountLevelPermissions"
    )


class CreateFilterRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    name: str = Field(alias="Name")
    finding_criteria: FindingCriteriaModel = Field(alias="FindingCriteria")
    description: Optional[str] = Field(default=None, alias="Description")
    action: Optional[Literal["ARCHIVE", "NOOP"]] = Field(default=None, alias="Action")
    rank: Optional[int] = Field(default=None, alias="Rank")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class GetFilterResponseModel(BaseModel):
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    action: Literal["ARCHIVE", "NOOP"] = Field(alias="Action")
    rank: int = Field(alias="Rank")
    finding_criteria: FindingCriteriaModel = Field(alias="FindingCriteria")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFindingsStatisticsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_statistic_types: Sequence[Literal["COUNT_BY_SEVERITY"]] = Field(
        alias="FindingStatisticTypes"
    )
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="FindingCriteria"
    )


class ListFindingsRequestListFindingsPaginateModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="FindingCriteria"
    )
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFindingsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="FindingCriteria"
    )
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="SortCriteria"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateFilterRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    filter_name: str = Field(alias="FilterName")
    description: Optional[str] = Field(default=None, alias="Description")
    action: Optional[Literal["ARCHIVE", "NOOP"]] = Field(default=None, alias="Action")
    rank: Optional[int] = Field(default=None, alias="Rank")
    finding_criteria: Optional[FindingCriteriaModel] = Field(
        default=None, alias="FindingCriteria"
    )


class DataSourcesFreeTrialModel(BaseModel):
    cloud_trail: Optional[DataSourceFreeTrialModel] = Field(
        default=None, alias="CloudTrail"
    )
    dns_logs: Optional[DataSourceFreeTrialModel] = Field(default=None, alias="DnsLogs")
    flow_logs: Optional[DataSourceFreeTrialModel] = Field(
        default=None, alias="FlowLogs"
    )
    s3_logs: Optional[DataSourceFreeTrialModel] = Field(default=None, alias="S3Logs")
    kubernetes: Optional[KubernetesDataSourceFreeTrialModel] = Field(
        default=None, alias="Kubernetes"
    )
    malware_protection: Optional[MalwareProtectionDataSourceFreeTrialModel] = Field(
        default=None, alias="MalwareProtection"
    )


class MalwareProtectionConfigurationResultModel(BaseModel):
    scan_ec2_instance_with_findings: Optional[
        ScanEc2InstanceWithFindingsResultModel
    ] = Field(default=None, alias="ScanEc2InstanceWithFindings")
    service_role: Optional[str] = Field(default=None, alias="ServiceRole")


class FilterCriteriaModel(BaseModel):
    filter_criterion: Optional[Sequence[FilterCriterionModel]] = Field(
        default=None, alias="FilterCriterion"
    )


class EcsTaskDetailsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    definition_arn: Optional[str] = Field(default=None, alias="DefinitionArn")
    version: Optional[str] = Field(default=None, alias="Version")
    task_created_at: Optional[datetime] = Field(default=None, alias="TaskCreatedAt")
    started_at: Optional[datetime] = Field(default=None, alias="StartedAt")
    started_by: Optional[str] = Field(default=None, alias="StartedBy")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    volumes: Optional[List[VolumeModel]] = Field(default=None, alias="Volumes")
    containers: Optional[List[ContainerModel]] = Field(default=None, alias="Containers")
    group: Optional[str] = Field(default=None, alias="Group")


class KubernetesWorkloadDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    uid: Optional[str] = Field(default=None, alias="Uid")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    host_network: Optional[bool] = Field(default=None, alias="HostNetwork")
    containers: Optional[List[ContainerModel]] = Field(default=None, alias="Containers")
    volumes: Optional[List[VolumeModel]] = Field(default=None, alias="Volumes")


class DataSourceConfigurationsModel(BaseModel):
    s3_logs: Optional[S3LogsConfigurationModel] = Field(default=None, alias="S3Logs")
    kubernetes: Optional[KubernetesConfigurationModel] = Field(
        default=None, alias="Kubernetes"
    )
    malware_protection: Optional[MalwareProtectionConfigurationModel] = Field(
        default=None, alias="MalwareProtection"
    )


class InstanceDetailsModel(BaseModel):
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    iam_instance_profile: Optional[IamInstanceProfileModel] = Field(
        default=None, alias="IamInstanceProfile"
    )
    image_description: Optional[str] = Field(default=None, alias="ImageDescription")
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    instance_id: Optional[str] = Field(default=None, alias="InstanceId")
    instance_state: Optional[str] = Field(default=None, alias="InstanceState")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    outpost_arn: Optional[str] = Field(default=None, alias="OutpostArn")
    launch_time: Optional[str] = Field(default=None, alias="LaunchTime")
    network_interfaces: Optional[List[NetworkInterfaceModel]] = Field(
        default=None, alias="NetworkInterfaces"
    )
    platform: Optional[str] = Field(default=None, alias="Platform")
    product_codes: Optional[List[ProductCodeModel]] = Field(
        default=None, alias="ProductCodes"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class OrganizationMalwareProtectionConfigurationResultModel(BaseModel):
    scan_ec2_instance_with_findings: Optional[
        OrganizationScanEc2InstanceWithFindingsResultModel
    ] = Field(default=None, alias="ScanEc2InstanceWithFindings")


class OrganizationMalwareProtectionConfigurationModel(BaseModel):
    scan_ec2_instance_with_findings: Optional[
        OrganizationScanEc2InstanceWithFindingsModel
    ] = Field(default=None, alias="ScanEc2InstanceWithFindings")


class AwsApiCallActionModel(BaseModel):
    api: Optional[str] = Field(default=None, alias="Api")
    caller_type: Optional[str] = Field(default=None, alias="CallerType")
    domain_details: Optional[DomainDetailsModel] = Field(
        default=None, alias="DomainDetails"
    )
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    user_agent: Optional[str] = Field(default=None, alias="UserAgent")
    remote_ip_details: Optional[RemoteIpDetailsModel] = Field(
        default=None, alias="RemoteIpDetails"
    )
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    remote_account_details: Optional[RemoteAccountDetailsModel] = Field(
        default=None, alias="RemoteAccountDetails"
    )
    affected_resources: Optional[Dict[str, str]] = Field(
        default=None, alias="AffectedResources"
    )


class KubernetesApiCallActionModel(BaseModel):
    request_uri: Optional[str] = Field(default=None, alias="RequestUri")
    verb: Optional[str] = Field(default=None, alias="Verb")
    source_ips: Optional[List[str]] = Field(default=None, alias="SourceIps")
    user_agent: Optional[str] = Field(default=None, alias="UserAgent")
    remote_ip_details: Optional[RemoteIpDetailsModel] = Field(
        default=None, alias="RemoteIpDetails"
    )
    status_code: Optional[int] = Field(default=None, alias="StatusCode")
    parameters: Optional[str] = Field(default=None, alias="Parameters")


class NetworkConnectionActionModel(BaseModel):
    blocked: Optional[bool] = Field(default=None, alias="Blocked")
    connection_direction: Optional[str] = Field(
        default=None, alias="ConnectionDirection"
    )
    local_port_details: Optional[LocalPortDetailsModel] = Field(
        default=None, alias="LocalPortDetails"
    )
    protocol: Optional[str] = Field(default=None, alias="Protocol")
    local_ip_details: Optional[LocalIpDetailsModel] = Field(
        default=None, alias="LocalIpDetails"
    )
    remote_ip_details: Optional[RemoteIpDetailsModel] = Field(
        default=None, alias="RemoteIpDetails"
    )
    remote_port_details: Optional[RemotePortDetailsModel] = Field(
        default=None, alias="RemotePortDetails"
    )


class PortProbeDetailModel(BaseModel):
    local_port_details: Optional[LocalPortDetailsModel] = Field(
        default=None, alias="LocalPortDetails"
    )
    local_ip_details: Optional[LocalIpDetailsModel] = Field(
        default=None, alias="LocalIpDetails"
    )
    remote_ip_details: Optional[RemoteIpDetailsModel] = Field(
        default=None, alias="RemoteIpDetails"
    )


class ScanResourceCriteriaModel(BaseModel):
    include: Optional[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionModel]] = Field(
        default=None, alias="Include"
    )
    exclude: Optional[Dict[Literal["EC2_INSTANCE_TAG"], ScanConditionModel]] = Field(
        default=None, alias="Exclude"
    )


class ThreatDetectedByNameModel(BaseModel):
    item_count: Optional[int] = Field(default=None, alias="ItemCount")
    unique_threat_name_count: Optional[int] = Field(
        default=None, alias="UniqueThreatNameCount"
    )
    shortened: Optional[bool] = Field(default=None, alias="Shortened")
    threat_names: Optional[List[ScanThreatNameModel]] = Field(
        default=None, alias="ThreatNames"
    )


class DescribeMalwareScansResponseModel(BaseModel):
    scans: List[ScanModel] = Field(alias="Scans")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UsageStatisticsModel(BaseModel):
    sum_by_account: Optional[List[UsageAccountResultModel]] = Field(
        default=None, alias="SumByAccount"
    )
    sum_by_data_source: Optional[List[UsageDataSourceResultModel]] = Field(
        default=None, alias="SumByDataSource"
    )
    sum_by_resource: Optional[List[UsageResourceResultModel]] = Field(
        default=None, alias="SumByResource"
    )
    top_resources: Optional[List[UsageResourceResultModel]] = Field(
        default=None, alias="TopResources"
    )


class PublicAccessModel(BaseModel):
    permission_configuration: Optional[PermissionConfigurationModel] = Field(
        default=None, alias="PermissionConfiguration"
    )
    effective_permission: Optional[str] = Field(
        default=None, alias="EffectivePermission"
    )


class AccountFreeTrialInfoModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    data_sources: Optional[DataSourcesFreeTrialModel] = Field(
        default=None, alias="DataSources"
    )


class DataSourceConfigurationsResultModel(BaseModel):
    cloud_trail: CloudTrailConfigurationResultModel = Field(alias="CloudTrail")
    dns_logs: DNSLogsConfigurationResultModel = Field(alias="DNSLogs")
    flow_logs: FlowLogsConfigurationResultModel = Field(alias="FlowLogs")
    s3_logs: S3LogsConfigurationResultModel = Field(alias="S3Logs")
    kubernetes: Optional[KubernetesConfigurationResultModel] = Field(
        default=None, alias="Kubernetes"
    )
    malware_protection: Optional[MalwareProtectionConfigurationResultModel] = Field(
        default=None, alias="MalwareProtection"
    )


class UnprocessedDataSourcesResultModel(BaseModel):
    malware_protection: Optional[MalwareProtectionConfigurationResultModel] = Field(
        default=None, alias="MalwareProtection"
    )


class DescribeMalwareScansRequestDescribeMalwareScansPaginateModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="FilterCriteria"
    )
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="SortCriteria"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeMalwareScansRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    filter_criteria: Optional[FilterCriteriaModel] = Field(
        default=None, alias="FilterCriteria"
    )
    sort_criteria: Optional[SortCriteriaModel] = Field(
        default=None, alias="SortCriteria"
    )


class EcsClusterDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    status: Optional[str] = Field(default=None, alias="Status")
    active_services_count: Optional[int] = Field(
        default=None, alias="ActiveServicesCount"
    )
    registered_container_instances_count: Optional[int] = Field(
        default=None, alias="RegisteredContainerInstancesCount"
    )
    running_tasks_count: Optional[int] = Field(default=None, alias="RunningTasksCount")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    task_details: Optional[EcsTaskDetailsModel] = Field(
        default=None, alias="TaskDetails"
    )


class KubernetesDetailsModel(BaseModel):
    kubernetes_user_details: Optional[KubernetesUserDetailsModel] = Field(
        default=None, alias="KubernetesUserDetails"
    )
    kubernetes_workload_details: Optional[KubernetesWorkloadDetailsModel] = Field(
        default=None, alias="KubernetesWorkloadDetails"
    )


class CreateDetectorRequestModel(BaseModel):
    enable: bool = Field(alias="Enable")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    finding_publishing_frequency: Optional[
        Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
    ] = Field(default=None, alias="FindingPublishingFrequency")
    data_sources: Optional[DataSourceConfigurationsModel] = Field(
        default=None, alias="DataSources"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateDetectorRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    enable: Optional[bool] = Field(default=None, alias="Enable")
    finding_publishing_frequency: Optional[
        Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
    ] = Field(default=None, alias="FindingPublishingFrequency")
    data_sources: Optional[DataSourceConfigurationsModel] = Field(
        default=None, alias="DataSources"
    )


class UpdateMemberDetectorsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    account_ids: Sequence[str] = Field(alias="AccountIds")
    data_sources: Optional[DataSourceConfigurationsModel] = Field(
        default=None, alias="DataSources"
    )


class OrganizationDataSourceConfigurationsResultModel(BaseModel):
    s3_logs: OrganizationS3LogsConfigurationResultModel = Field(alias="S3Logs")
    kubernetes: Optional[OrganizationKubernetesConfigurationResultModel] = Field(
        default=None, alias="Kubernetes"
    )
    malware_protection: Optional[
        OrganizationMalwareProtectionConfigurationResultModel
    ] = Field(default=None, alias="MalwareProtection")


class OrganizationDataSourceConfigurationsModel(BaseModel):
    s3_logs: Optional[OrganizationS3LogsConfigurationModel] = Field(
        default=None, alias="S3Logs"
    )
    kubernetes: Optional[OrganizationKubernetesConfigurationModel] = Field(
        default=None, alias="Kubernetes"
    )
    malware_protection: Optional[
        OrganizationMalwareProtectionConfigurationModel
    ] = Field(default=None, alias="MalwareProtection")


class PortProbeActionModel(BaseModel):
    blocked: Optional[bool] = Field(default=None, alias="Blocked")
    port_probe_details: Optional[List[PortProbeDetailModel]] = Field(
        default=None, alias="PortProbeDetails"
    )


class GetMalwareScanSettingsResponseModel(BaseModel):
    scan_resource_criteria: ScanResourceCriteriaModel = Field(
        alias="ScanResourceCriteria"
    )
    ebs_snapshot_preservation: Literal[
        "NO_RETENTION", "RETENTION_WITH_FINDING"
    ] = Field(alias="EbsSnapshotPreservation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMalwareScanSettingsRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    scan_resource_criteria: Optional[ScanResourceCriteriaModel] = Field(
        default=None, alias="ScanResourceCriteria"
    )
    ebs_snapshot_preservation: Optional[
        Literal["NO_RETENTION", "RETENTION_WITH_FINDING"]
    ] = Field(default=None, alias="EbsSnapshotPreservation")


class ScanDetectionsModel(BaseModel):
    scanned_item_count: Optional[ScannedItemCountModel] = Field(
        default=None, alias="ScannedItemCount"
    )
    threats_detected_item_count: Optional[ThreatsDetectedItemCountModel] = Field(
        default=None, alias="ThreatsDetectedItemCount"
    )
    highest_severity_threat_details: Optional[
        HighestSeverityThreatDetailsModel
    ] = Field(default=None, alias="HighestSeverityThreatDetails")
    threat_detected_by_name: Optional[ThreatDetectedByNameModel] = Field(
        default=None, alias="ThreatDetectedByName"
    )


class GetUsageStatisticsResponseModel(BaseModel):
    usage_statistics: UsageStatisticsModel = Field(alias="UsageStatistics")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3BucketDetailModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[str] = Field(default=None, alias="Type")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    owner: Optional[OwnerModel] = Field(default=None, alias="Owner")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    default_server_side_encryption: Optional[DefaultServerSideEncryptionModel] = Field(
        default=None, alias="DefaultServerSideEncryption"
    )
    public_access: Optional[PublicAccessModel] = Field(
        default=None, alias="PublicAccess"
    )


class GetRemainingFreeTrialDaysResponseModel(BaseModel):
    accounts: List[AccountFreeTrialInfoModel] = Field(alias="Accounts")
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDetectorResponseModel(BaseModel):
    created_at: str = Field(alias="CreatedAt")
    finding_publishing_frequency: Literal[
        "FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"
    ] = Field(alias="FindingPublishingFrequency")
    service_role: str = Field(alias="ServiceRole")
    status: Literal["DISABLED", "ENABLED"] = Field(alias="Status")
    updated_at: str = Field(alias="UpdatedAt")
    data_sources: DataSourceConfigurationsResultModel = Field(alias="DataSources")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MemberDataSourceConfigurationModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    data_sources: DataSourceConfigurationsResultModel = Field(alias="DataSources")


class CreateDetectorResponseModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    unprocessed_data_sources: UnprocessedDataSourcesResultModel = Field(
        alias="UnprocessedDataSources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationConfigurationResponseModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")
    member_account_limit_reached: bool = Field(alias="MemberAccountLimitReached")
    data_sources: OrganizationDataSourceConfigurationsResultModel = Field(
        alias="DataSources"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateOrganizationConfigurationRequestModel(BaseModel):
    detector_id: str = Field(alias="DetectorId")
    auto_enable: bool = Field(alias="AutoEnable")
    data_sources: Optional[OrganizationDataSourceConfigurationsModel] = Field(
        default=None, alias="DataSources"
    )


class ActionModel(BaseModel):
    action_type: Optional[str] = Field(default=None, alias="ActionType")
    aws_api_call_action: Optional[AwsApiCallActionModel] = Field(
        default=None, alias="AwsApiCallAction"
    )
    dns_request_action: Optional[DnsRequestActionModel] = Field(
        default=None, alias="DnsRequestAction"
    )
    network_connection_action: Optional[NetworkConnectionActionModel] = Field(
        default=None, alias="NetworkConnectionAction"
    )
    port_probe_action: Optional[PortProbeActionModel] = Field(
        default=None, alias="PortProbeAction"
    )
    kubernetes_api_call_action: Optional[KubernetesApiCallActionModel] = Field(
        default=None, alias="KubernetesApiCallAction"
    )


class EbsVolumeScanDetailsModel(BaseModel):
    scan_id: Optional[str] = Field(default=None, alias="ScanId")
    scan_started_at: Optional[datetime] = Field(default=None, alias="ScanStartedAt")
    scan_completed_at: Optional[datetime] = Field(default=None, alias="ScanCompletedAt")
    trigger_finding_id: Optional[str] = Field(default=None, alias="TriggerFindingId")
    sources: Optional[List[str]] = Field(default=None, alias="Sources")
    scan_detections: Optional[ScanDetectionsModel] = Field(
        default=None, alias="ScanDetections"
    )


class ResourceModel(BaseModel):
    access_key_details: Optional[AccessKeyDetailsModel] = Field(
        default=None, alias="AccessKeyDetails"
    )
    s3_bucket_details: Optional[List[S3BucketDetailModel]] = Field(
        default=None, alias="S3BucketDetails"
    )
    instance_details: Optional[InstanceDetailsModel] = Field(
        default=None, alias="InstanceDetails"
    )
    eks_cluster_details: Optional[EksClusterDetailsModel] = Field(
        default=None, alias="EksClusterDetails"
    )
    kubernetes_details: Optional[KubernetesDetailsModel] = Field(
        default=None, alias="KubernetesDetails"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    ebs_volume_details: Optional[EbsVolumeDetailsModel] = Field(
        default=None, alias="EbsVolumeDetails"
    )
    ecs_cluster_details: Optional[EcsClusterDetailsModel] = Field(
        default=None, alias="EcsClusterDetails"
    )
    container_details: Optional[ContainerModel] = Field(
        default=None, alias="ContainerDetails"
    )


class GetMemberDetectorsResponseModel(BaseModel):
    member_data_source_configurations: List[MemberDataSourceConfigurationModel] = Field(
        alias="MemberDataSourceConfigurations"
    )
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ServiceModel(BaseModel):
    action: Optional[ActionModel] = Field(default=None, alias="Action")
    evidence: Optional[EvidenceModel] = Field(default=None, alias="Evidence")
    archived: Optional[bool] = Field(default=None, alias="Archived")
    count: Optional[int] = Field(default=None, alias="Count")
    detector_id: Optional[str] = Field(default=None, alias="DetectorId")
    event_first_seen: Optional[str] = Field(default=None, alias="EventFirstSeen")
    event_last_seen: Optional[str] = Field(default=None, alias="EventLastSeen")
    resource_role: Optional[str] = Field(default=None, alias="ResourceRole")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    user_feedback: Optional[str] = Field(default=None, alias="UserFeedback")
    additional_info: Optional[ServiceAdditionalInfoModel] = Field(
        default=None, alias="AdditionalInfo"
    )
    feature_name: Optional[str] = Field(default=None, alias="FeatureName")
    ebs_volume_scan_details: Optional[EbsVolumeScanDetailsModel] = Field(
        default=None, alias="EbsVolumeScanDetails"
    )


class FindingModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    arn: str = Field(alias="Arn")
    created_at: str = Field(alias="CreatedAt")
    id: str = Field(alias="Id")
    region: str = Field(alias="Region")
    resource: ResourceModel = Field(alias="Resource")
    schema_version: str = Field(alias="SchemaVersion")
    severity: float = Field(alias="Severity")
    type: str = Field(alias="Type")
    updated_at: str = Field(alias="UpdatedAt")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    description: Optional[str] = Field(default=None, alias="Description")
    partition: Optional[str] = Field(default=None, alias="Partition")
    service: Optional[ServiceModel] = Field(default=None, alias="Service")
    title: Optional[str] = Field(default=None, alias="Title")


class GetFindingsResponseModel(BaseModel):
    findings: List[FindingModel] = Field(alias="Findings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
