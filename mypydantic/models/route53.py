# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountLimitModel(BaseModel):
    type: Literal[
        "MAX_HEALTH_CHECKS_BY_OWNER",
        "MAX_HOSTED_ZONES_BY_OWNER",
        "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
        "MAX_TRAFFIC_POLICIES_BY_OWNER",
        "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
    ] = Field(alias="Type")
    value: int = Field(alias="Value")


class ActivateKeySigningKeyRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    name: str = Field(alias="Name")


class ChangeInfoModel(BaseModel):
    id: str = Field(alias="Id")
    status: Literal["INSYNC", "PENDING"] = Field(alias="Status")
    submitted_at: datetime = Field(alias="SubmittedAt")
    comment: Optional[str] = Field(default=None, alias="Comment")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AlarmIdentifierModel(BaseModel):
    region: Literal[
        "af-south-1",
        "ap-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-northeast-3",
        "ap-south-1",
        "ap-south-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ap-southeast-4",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "eu-central-1",
        "eu-central-2",
        "eu-north-1",
        "eu-south-1",
        "eu-south-2",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "me-central-1",
        "me-south-1",
        "sa-east-1",
        "us-east-1",
        "us-east-2",
        "us-gov-east-1",
        "us-gov-west-1",
        "us-iso-east-1",
        "us-iso-west-1",
        "us-isob-east-1",
        "us-west-1",
        "us-west-2",
    ] = Field(alias="Region")
    name: str = Field(alias="Name")


class AliasTargetModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    dns_name: str = Field(alias="DNSName")
    evaluate_target_health: bool = Field(alias="EvaluateTargetHealth")


class VPCModel(BaseModel):
    vp_cregion: Optional[
        Literal[
            "af-south-1",
            "ap-east-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "ap-south-1",
            "ap-south-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-southeast-3",
            "ap-southeast-4",
            "ca-central-1",
            "cn-north-1",
            "eu-central-1",
            "eu-central-2",
            "eu-north-1",
            "eu-south-1",
            "eu-south-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "me-central-1",
            "me-south-1",
            "sa-east-1",
            "us-east-1",
            "us-east-2",
            "us-gov-east-1",
            "us-gov-west-1",
            "us-iso-east-1",
            "us-iso-west-1",
            "us-isob-east-1",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="VPCRegion")
    vp_cid: Optional[str] = Field(default=None, alias="VPCId")


class CidrCollectionChangeModel(BaseModel):
    location_name: str = Field(alias="LocationName")
    action: Literal["DELETE_IF_EXISTS", "PUT"] = Field(alias="Action")
    cidr_list: Sequence[str] = Field(alias="CidrList")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CidrBlockSummaryModel(BaseModel):
    cidr_block: Optional[str] = Field(default=None, alias="CidrBlock")
    location_name: Optional[str] = Field(default=None, alias="LocationName")


class CidrCollectionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[int] = Field(default=None, alias="Version")


class CidrRoutingConfigModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    location_name: str = Field(alias="LocationName")


class DimensionModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class CollectionSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[int] = Field(default=None, alias="Version")


class CreateCidrCollectionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    caller_reference: str = Field(alias="CallerReference")


class HostedZoneConfigModel(BaseModel):
    comment: Optional[str] = Field(default=None, alias="Comment")
    private_zone: Optional[bool] = Field(default=None, alias="PrivateZone")


class DelegationSetModel(BaseModel):
    name_servers: List[str] = Field(alias="NameServers")
    id: Optional[str] = Field(default=None, alias="Id")
    caller_reference: Optional[str] = Field(default=None, alias="CallerReference")


class CreateKeySigningKeyRequestModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    hosted_zone_id: str = Field(alias="HostedZoneId")
    key_management_service_arn: str = Field(alias="KeyManagementServiceArn")
    name: str = Field(alias="Name")
    status: str = Field(alias="Status")


class KeySigningKeyModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    kms_arn: Optional[str] = Field(default=None, alias="KmsArn")
    flag: Optional[int] = Field(default=None, alias="Flag")
    signing_algorithm_mnemonic: Optional[str] = Field(
        default=None, alias="SigningAlgorithmMnemonic"
    )
    signing_algorithm_type: Optional[int] = Field(
        default=None, alias="SigningAlgorithmType"
    )
    digest_algorithm_mnemonic: Optional[str] = Field(
        default=None, alias="DigestAlgorithmMnemonic"
    )
    digest_algorithm_type: Optional[int] = Field(
        default=None, alias="DigestAlgorithmType"
    )
    key_tag: Optional[int] = Field(default=None, alias="KeyTag")
    digest_value: Optional[str] = Field(default=None, alias="DigestValue")
    public_key: Optional[str] = Field(default=None, alias="PublicKey")
    ds_record: Optional[str] = Field(default=None, alias="DSRecord")
    dns_keyrecord: Optional[str] = Field(default=None, alias="DNSKEYRecord")
    status: Optional[str] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="LastModifiedDate"
    )


class CreateQueryLoggingConfigRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    cloud_watch_logs_log_group_arn: str = Field(alias="CloudWatchLogsLogGroupArn")


class QueryLoggingConfigModel(BaseModel):
    id: str = Field(alias="Id")
    hosted_zone_id: str = Field(alias="HostedZoneId")
    cloud_watch_logs_log_group_arn: str = Field(alias="CloudWatchLogsLogGroupArn")


class CreateReusableDelegationSetRequestModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")


class CreateTrafficPolicyInstanceRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    name: str = Field(alias="Name")
    ttl: int = Field(alias="TTL")
    traffic_policy_id: str = Field(alias="TrafficPolicyId")
    traffic_policy_version: int = Field(alias="TrafficPolicyVersion")


class TrafficPolicyInstanceModel(BaseModel):
    id: str = Field(alias="Id")
    hosted_zone_id: str = Field(alias="HostedZoneId")
    name: str = Field(alias="Name")
    ttl: int = Field(alias="TTL")
    state: str = Field(alias="State")
    message: str = Field(alias="Message")
    traffic_policy_id: str = Field(alias="TrafficPolicyId")
    traffic_policy_version: int = Field(alias="TrafficPolicyVersion")
    traffic_policy_type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="TrafficPolicyType")


class CreateTrafficPolicyRequestModel(BaseModel):
    name: str = Field(alias="Name")
    document: str = Field(alias="Document")
    comment: Optional[str] = Field(default=None, alias="Comment")


class TrafficPolicyModel(BaseModel):
    id: str = Field(alias="Id")
    version: int = Field(alias="Version")
    name: str = Field(alias="Name")
    type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="Type")
    document: str = Field(alias="Document")
    comment: Optional[str] = Field(default=None, alias="Comment")


class CreateTrafficPolicyVersionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    document: str = Field(alias="Document")
    comment: Optional[str] = Field(default=None, alias="Comment")


class DNSSECStatusModel(BaseModel):
    serve_signature: Optional[str] = Field(default=None, alias="ServeSignature")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class DeactivateKeySigningKeyRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    name: str = Field(alias="Name")


class DeleteCidrCollectionRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteHealthCheckRequestModel(BaseModel):
    health_check_id: str = Field(alias="HealthCheckId")


class DeleteHostedZoneRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteKeySigningKeyRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    name: str = Field(alias="Name")


class DeleteQueryLoggingConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteReusableDelegationSetRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteTrafficPolicyInstanceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DeleteTrafficPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    version: int = Field(alias="Version")


class DisableHostedZoneDNSSECRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")


class EnableHostedZoneDNSSECRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")


class GeoLocationDetailsModel(BaseModel):
    continent_code: Optional[str] = Field(default=None, alias="ContinentCode")
    continent_name: Optional[str] = Field(default=None, alias="ContinentName")
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    country_name: Optional[str] = Field(default=None, alias="CountryName")
    subdivision_code: Optional[str] = Field(default=None, alias="SubdivisionCode")
    subdivision_name: Optional[str] = Field(default=None, alias="SubdivisionName")


class GeoLocationModel(BaseModel):
    continent_code: Optional[str] = Field(default=None, alias="ContinentCode")
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    subdivision_code: Optional[str] = Field(default=None, alias="SubdivisionCode")


class GetAccountLimitRequestModel(BaseModel):
    type: Literal[
        "MAX_HEALTH_CHECKS_BY_OWNER",
        "MAX_HOSTED_ZONES_BY_OWNER",
        "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
        "MAX_TRAFFIC_POLICIES_BY_OWNER",
        "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
    ] = Field(alias="Type")


class GetChangeRequestModel(BaseModel):
    id: str = Field(alias="Id")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetDNSSECRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")


class GetGeoLocationRequestModel(BaseModel):
    continent_code: Optional[str] = Field(default=None, alias="ContinentCode")
    country_code: Optional[str] = Field(default=None, alias="CountryCode")
    subdivision_code: Optional[str] = Field(default=None, alias="SubdivisionCode")


class GetHealthCheckLastFailureReasonRequestModel(BaseModel):
    health_check_id: str = Field(alias="HealthCheckId")


class GetHealthCheckRequestModel(BaseModel):
    health_check_id: str = Field(alias="HealthCheckId")


class GetHealthCheckStatusRequestModel(BaseModel):
    health_check_id: str = Field(alias="HealthCheckId")


class GetHostedZoneLimitRequestModel(BaseModel):
    type: Literal["MAX_RRSETS_BY_ZONE", "MAX_VPCS_ASSOCIATED_BY_ZONE"] = Field(
        alias="Type"
    )
    hosted_zone_id: str = Field(alias="HostedZoneId")


class HostedZoneLimitModel(BaseModel):
    type: Literal["MAX_RRSETS_BY_ZONE", "MAX_VPCS_ASSOCIATED_BY_ZONE"] = Field(
        alias="Type"
    )
    value: int = Field(alias="Value")


class GetHostedZoneRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetQueryLoggingConfigRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetReusableDelegationSetLimitRequestModel(BaseModel):
    type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"] = Field(alias="Type")
    delegation_set_id: str = Field(alias="DelegationSetId")


class ReusableDelegationSetLimitModel(BaseModel):
    type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"] = Field(alias="Type")
    value: int = Field(alias="Value")


class GetReusableDelegationSetRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetTrafficPolicyInstanceRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetTrafficPolicyRequestModel(BaseModel):
    id: str = Field(alias="Id")
    version: int = Field(alias="Version")


class StatusReportModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="Status")
    checked_time: Optional[datetime] = Field(default=None, alias="CheckedTime")


class LinkedServiceModel(BaseModel):
    service_principal: Optional[str] = Field(default=None, alias="ServicePrincipal")
    description: Optional[str] = Field(default=None, alias="Description")


class HostedZoneOwnerModel(BaseModel):
    owning_account: Optional[str] = Field(default=None, alias="OwningAccount")
    owning_service: Optional[str] = Field(default=None, alias="OwningService")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListCidrBlocksRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    location_name: Optional[str] = Field(default=None, alias="LocationName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")


class ListCidrCollectionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")


class ListCidrLocationsRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")


class LocationSummaryModel(BaseModel):
    location_name: Optional[str] = Field(default=None, alias="LocationName")


class ListGeoLocationsRequestModel(BaseModel):
    start_continent_code: Optional[str] = Field(
        default=None, alias="StartContinentCode"
    )
    start_country_code: Optional[str] = Field(default=None, alias="StartCountryCode")
    start_subdivision_code: Optional[str] = Field(
        default=None, alias="StartSubdivisionCode"
    )
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListHealthChecksRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListHostedZonesByNameRequestModel(BaseModel):
    dns_name: Optional[str] = Field(default=None, alias="DNSName")
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListHostedZonesByVPCRequestModel(BaseModel):
    vp_cid: str = Field(alias="VPCId")
    vp_cregion: Literal[
        "af-south-1",
        "ap-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-northeast-3",
        "ap-south-1",
        "ap-south-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ap-southeast-4",
        "ca-central-1",
        "cn-north-1",
        "eu-central-1",
        "eu-central-2",
        "eu-north-1",
        "eu-south-1",
        "eu-south-2",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "me-central-1",
        "me-south-1",
        "sa-east-1",
        "us-east-1",
        "us-east-2",
        "us-gov-east-1",
        "us-gov-west-1",
        "us-iso-east-1",
        "us-iso-west-1",
        "us-isob-east-1",
        "us-west-1",
        "us-west-2",
    ] = Field(alias="VPCRegion")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHostedZonesRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")
    delegation_set_id: Optional[str] = Field(default=None, alias="DelegationSetId")


class ListQueryLoggingConfigsRequestModel(BaseModel):
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")


class ListResourceRecordSetsRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    start_record_name: Optional[str] = Field(default=None, alias="StartRecordName")
    start_record_type: Optional[
        Literal[
            "A",
            "AAAA",
            "CAA",
            "CNAME",
            "DS",
            "MX",
            "NAPTR",
            "NS",
            "PTR",
            "SOA",
            "SPF",
            "SRV",
            "TXT",
        ]
    ] = Field(default=None, alias="StartRecordType")
    start_record_identifier: Optional[str] = Field(
        default=None, alias="StartRecordIdentifier"
    )
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListReusableDelegationSetsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="Marker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListTagsForResourceRequestModel(BaseModel):
    resource_type: Literal["healthcheck", "hostedzone"] = Field(alias="ResourceType")
    resource_id: str = Field(alias="ResourceId")


class ListTagsForResourcesRequestModel(BaseModel):
    resource_type: Literal["healthcheck", "hostedzone"] = Field(alias="ResourceType")
    resource_ids: Sequence[str] = Field(alias="ResourceIds")


class ListTrafficPoliciesRequestModel(BaseModel):
    traffic_policy_id_marker: Optional[str] = Field(
        default=None, alias="TrafficPolicyIdMarker"
    )
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class TrafficPolicySummaryModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="Type")
    latest_version: int = Field(alias="LatestVersion")
    traffic_policy_count: int = Field(alias="TrafficPolicyCount")


class ListTrafficPolicyInstancesByHostedZoneRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    traffic_policy_instance_name_marker: Optional[str] = Field(
        default=None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: Optional[
        Literal[
            "A",
            "AAAA",
            "CAA",
            "CNAME",
            "DS",
            "MX",
            "NAPTR",
            "NS",
            "PTR",
            "SOA",
            "SPF",
            "SRV",
            "TXT",
        ]
    ] = Field(default=None, alias="TrafficPolicyInstanceTypeMarker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListTrafficPolicyInstancesByPolicyRequestModel(BaseModel):
    traffic_policy_id: str = Field(alias="TrafficPolicyId")
    traffic_policy_version: int = Field(alias="TrafficPolicyVersion")
    hosted_zone_id_marker: Optional[str] = Field(
        default=None, alias="HostedZoneIdMarker"
    )
    traffic_policy_instance_name_marker: Optional[str] = Field(
        default=None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: Optional[
        Literal[
            "A",
            "AAAA",
            "CAA",
            "CNAME",
            "DS",
            "MX",
            "NAPTR",
            "NS",
            "PTR",
            "SOA",
            "SPF",
            "SRV",
            "TXT",
        ]
    ] = Field(default=None, alias="TrafficPolicyInstanceTypeMarker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListTrafficPolicyInstancesRequestModel(BaseModel):
    hosted_zone_id_marker: Optional[str] = Field(
        default=None, alias="HostedZoneIdMarker"
    )
    traffic_policy_instance_name_marker: Optional[str] = Field(
        default=None, alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: Optional[
        Literal[
            "A",
            "AAAA",
            "CAA",
            "CNAME",
            "DS",
            "MX",
            "NAPTR",
            "NS",
            "PTR",
            "SOA",
            "SPF",
            "SRV",
            "TXT",
        ]
    ] = Field(default=None, alias="TrafficPolicyInstanceTypeMarker")
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListTrafficPolicyVersionsRequestModel(BaseModel):
    id: str = Field(alias="Id")
    traffic_policy_version_marker: Optional[str] = Field(
        default=None, alias="TrafficPolicyVersionMarker"
    )
    max_items: Optional[str] = Field(default=None, alias="MaxItems")


class ListVPCAssociationAuthorizationsRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")


class ResourceRecordModel(BaseModel):
    value: str = Field(alias="Value")


class TestDNSAnswerRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    record_name: str = Field(alias="RecordName")
    record_type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="RecordType")
    resolver_ip: Optional[str] = Field(default=None, alias="ResolverIP")
    edns0_client_subnet_ip: Optional[str] = Field(
        default=None, alias="EDNS0ClientSubnetIP"
    )
    edns0_client_subnet_mask: Optional[str] = Field(
        default=None, alias="EDNS0ClientSubnetMask"
    )


class UpdateHostedZoneCommentRequestModel(BaseModel):
    id: str = Field(alias="Id")
    comment: Optional[str] = Field(default=None, alias="Comment")


class UpdateTrafficPolicyCommentRequestModel(BaseModel):
    id: str = Field(alias="Id")
    version: int = Field(alias="Version")
    comment: str = Field(alias="Comment")


class UpdateTrafficPolicyInstanceRequestModel(BaseModel):
    id: str = Field(alias="Id")
    ttl: int = Field(alias="TTL")
    traffic_policy_id: str = Field(alias="TrafficPolicyId")
    traffic_policy_version: int = Field(alias="TrafficPolicyVersion")


class ActivateKeySigningKeyResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateVPCWithHostedZoneResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeCidrCollectionResponseModel(BaseModel):
    id: str = Field(alias="Id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeResourceRecordSetsResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeactivateKeySigningKeyResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteHostedZoneResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteKeySigningKeyResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableHostedZoneDNSSECResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateVPCFromHostedZoneResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableHostedZoneDNSSECResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountLimitResponseModel(BaseModel):
    limit: AccountLimitModel = Field(alias="Limit")
    count: int = Field(alias="Count")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChangeResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCheckerIpRangesResponseModel(BaseModel):
    checker_ip_ranges: List[str] = Field(alias="CheckerIpRanges")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHealthCheckCountResponseModel(BaseModel):
    health_check_count: int = Field(alias="HealthCheckCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHostedZoneCountResponseModel(BaseModel):
    hosted_zone_count: int = Field(alias="HostedZoneCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTrafficPolicyInstanceCountResponseModel(BaseModel):
    traffic_policy_instance_count: int = Field(alias="TrafficPolicyInstanceCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestDNSAnswerResponseModel(BaseModel):
    nameserver: str = Field(alias="Nameserver")
    record_name: str = Field(alias="RecordName")
    record_type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="RecordType")
    record_data: List[str] = Field(alias="RecordData")
    response_code: str = Field(alias="ResponseCode")
    protocol: str = Field(alias="Protocol")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HealthCheckConfigModel(BaseModel):
    type: Literal[
        "CALCULATED",
        "CLOUDWATCH_METRIC",
        "HTTP",
        "HTTPS",
        "HTTPS_STR_MATCH",
        "HTTP_STR_MATCH",
        "RECOVERY_CONTROL",
        "TCP",
    ] = Field(alias="Type")
    ip_address: Optional[str] = Field(default=None, alias="IPAddress")
    port: Optional[int] = Field(default=None, alias="Port")
    resource_path: Optional[str] = Field(default=None, alias="ResourcePath")
    fully_qualified_domain_name: Optional[str] = Field(
        default=None, alias="FullyQualifiedDomainName"
    )
    search_string: Optional[str] = Field(default=None, alias="SearchString")
    request_interval: Optional[int] = Field(default=None, alias="RequestInterval")
    failure_threshold: Optional[int] = Field(default=None, alias="FailureThreshold")
    measure_latency: Optional[bool] = Field(default=None, alias="MeasureLatency")
    inverted: Optional[bool] = Field(default=None, alias="Inverted")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    health_threshold: Optional[int] = Field(default=None, alias="HealthThreshold")
    child_health_checks: Optional[Sequence[str]] = Field(
        default=None, alias="ChildHealthChecks"
    )
    enable_s_ni: Optional[bool] = Field(default=None, alias="EnableSNI")
    regions: Optional[
        Sequence[
            Literal[
                "ap-northeast-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "eu-west-1",
                "sa-east-1",
                "us-east-1",
                "us-west-1",
                "us-west-2",
            ]
        ]
    ] = Field(default=None, alias="Regions")
    alarm_identifier: Optional[AlarmIdentifierModel] = Field(
        default=None, alias="AlarmIdentifier"
    )
    insufficient_data_health_status: Optional[
        Literal["Healthy", "LastKnownStatus", "Unhealthy"]
    ] = Field(default=None, alias="InsufficientDataHealthStatus")
    routing_control_arn: Optional[str] = Field(default=None, alias="RoutingControlArn")


class UpdateHealthCheckRequestModel(BaseModel):
    health_check_id: str = Field(alias="HealthCheckId")
    health_check_version: Optional[int] = Field(
        default=None, alias="HealthCheckVersion"
    )
    ip_address: Optional[str] = Field(default=None, alias="IPAddress")
    port: Optional[int] = Field(default=None, alias="Port")
    resource_path: Optional[str] = Field(default=None, alias="ResourcePath")
    fully_qualified_domain_name: Optional[str] = Field(
        default=None, alias="FullyQualifiedDomainName"
    )
    search_string: Optional[str] = Field(default=None, alias="SearchString")
    failure_threshold: Optional[int] = Field(default=None, alias="FailureThreshold")
    inverted: Optional[bool] = Field(default=None, alias="Inverted")
    disabled: Optional[bool] = Field(default=None, alias="Disabled")
    health_threshold: Optional[int] = Field(default=None, alias="HealthThreshold")
    child_health_checks: Optional[Sequence[str]] = Field(
        default=None, alias="ChildHealthChecks"
    )
    enable_s_ni: Optional[bool] = Field(default=None, alias="EnableSNI")
    regions: Optional[
        Sequence[
            Literal[
                "ap-northeast-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "eu-west-1",
                "sa-east-1",
                "us-east-1",
                "us-west-1",
                "us-west-2",
            ]
        ]
    ] = Field(default=None, alias="Regions")
    alarm_identifier: Optional[AlarmIdentifierModel] = Field(
        default=None, alias="AlarmIdentifier"
    )
    insufficient_data_health_status: Optional[
        Literal["Healthy", "LastKnownStatus", "Unhealthy"]
    ] = Field(default=None, alias="InsufficientDataHealthStatus")
    reset_elements: Optional[
        Sequence[
            Literal[
                "ChildHealthChecks",
                "FullyQualifiedDomainName",
                "Regions",
                "ResourcePath",
            ]
        ]
    ] = Field(default=None, alias="ResetElements")


class AssociateVPCWithHostedZoneRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    vp_c: VPCModel = Field(alias="VPC")
    comment: Optional[str] = Field(default=None, alias="Comment")


class CreateVPCAssociationAuthorizationRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    vp_c: VPCModel = Field(alias="VPC")


class CreateVPCAssociationAuthorizationResponseModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    vp_c: VPCModel = Field(alias="VPC")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVPCAssociationAuthorizationRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    vp_c: VPCModel = Field(alias="VPC")


class DisassociateVPCFromHostedZoneRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    vp_c: VPCModel = Field(alias="VPC")
    comment: Optional[str] = Field(default=None, alias="Comment")


class ListVPCAssociationAuthorizationsResponseModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    next_token: str = Field(alias="NextToken")
    vp_cs: List[VPCModel] = Field(alias="VPCs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeCidrCollectionRequestModel(BaseModel):
    id: str = Field(alias="Id")
    changes: Sequence[CidrCollectionChangeModel] = Field(alias="Changes")
    collection_version: Optional[int] = Field(default=None, alias="CollectionVersion")


class ChangeTagsForResourceRequestModel(BaseModel):
    resource_type: Literal["healthcheck", "hostedzone"] = Field(alias="ResourceType")
    resource_id: str = Field(alias="ResourceId")
    add_tags: Optional[Sequence[TagModel]] = Field(default=None, alias="AddTags")
    remove_tag_keys: Optional[Sequence[str]] = Field(
        default=None, alias="RemoveTagKeys"
    )


class ResourceTagSetModel(BaseModel):
    resource_type: Optional[Literal["healthcheck", "hostedzone"]] = Field(
        default=None, alias="ResourceType"
    )
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ListCidrBlocksResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    cidr_blocks: List[CidrBlockSummaryModel] = Field(alias="CidrBlocks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCidrCollectionResponseModel(BaseModel):
    collection: CidrCollectionModel = Field(alias="Collection")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CloudWatchAlarmConfigurationModel(BaseModel):
    evaluation_periods: int = Field(alias="EvaluationPeriods")
    threshold: float = Field(alias="Threshold")
    comparison_operator: Literal[
        "GreaterThanOrEqualToThreshold",
        "GreaterThanThreshold",
        "LessThanOrEqualToThreshold",
        "LessThanThreshold",
    ] = Field(alias="ComparisonOperator")
    period: int = Field(alias="Period")
    metric_name: str = Field(alias="MetricName")
    namespace: str = Field(alias="Namespace")
    statistic: Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"] = Field(
        alias="Statistic"
    )
    dimensions: Optional[List[DimensionModel]] = Field(default=None, alias="Dimensions")


class ListCidrCollectionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    cidr_collections: List[CollectionSummaryModel] = Field(alias="CidrCollections")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHostedZoneRequestModel(BaseModel):
    name: str = Field(alias="Name")
    caller_reference: str = Field(alias="CallerReference")
    vp_c: Optional[VPCModel] = Field(default=None, alias="VPC")
    hosted_zone_config: Optional[HostedZoneConfigModel] = Field(
        default=None, alias="HostedZoneConfig"
    )
    delegation_set_id: Optional[str] = Field(default=None, alias="DelegationSetId")


class CreateReusableDelegationSetResponseModel(BaseModel):
    delegation_set: DelegationSetModel = Field(alias="DelegationSet")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReusableDelegationSetResponseModel(BaseModel):
    delegation_set: DelegationSetModel = Field(alias="DelegationSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListReusableDelegationSetsResponseModel(BaseModel):
    delegation_sets: List[DelegationSetModel] = Field(alias="DelegationSets")
    marker: str = Field(alias="Marker")
    is_truncated: bool = Field(alias="IsTruncated")
    next_marker: str = Field(alias="NextMarker")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateKeySigningKeyResponseModel(BaseModel):
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    key_signing_key: KeySigningKeyModel = Field(alias="KeySigningKey")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateQueryLoggingConfigResponseModel(BaseModel):
    query_logging_config: QueryLoggingConfigModel = Field(alias="QueryLoggingConfig")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueryLoggingConfigResponseModel(BaseModel):
    query_logging_config: QueryLoggingConfigModel = Field(alias="QueryLoggingConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueryLoggingConfigsResponseModel(BaseModel):
    query_logging_configs: List[QueryLoggingConfigModel] = Field(
        alias="QueryLoggingConfigs"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrafficPolicyInstanceResponseModel(BaseModel):
    traffic_policy_instance: TrafficPolicyInstanceModel = Field(
        alias="TrafficPolicyInstance"
    )
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTrafficPolicyInstanceResponseModel(BaseModel):
    traffic_policy_instance: TrafficPolicyInstanceModel = Field(
        alias="TrafficPolicyInstance"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrafficPolicyInstancesByHostedZoneResponseModel(BaseModel):
    traffic_policy_instances: List[TrafficPolicyInstanceModel] = Field(
        alias="TrafficPolicyInstances"
    )
    traffic_policy_instance_name_marker: str = Field(
        alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="TrafficPolicyInstanceTypeMarker")
    is_truncated: bool = Field(alias="IsTruncated")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrafficPolicyInstancesByPolicyResponseModel(BaseModel):
    traffic_policy_instances: List[TrafficPolicyInstanceModel] = Field(
        alias="TrafficPolicyInstances"
    )
    hosted_zone_id_marker: str = Field(alias="HostedZoneIdMarker")
    traffic_policy_instance_name_marker: str = Field(
        alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="TrafficPolicyInstanceTypeMarker")
    is_truncated: bool = Field(alias="IsTruncated")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrafficPolicyInstancesResponseModel(BaseModel):
    traffic_policy_instances: List[TrafficPolicyInstanceModel] = Field(
        alias="TrafficPolicyInstances"
    )
    hosted_zone_id_marker: str = Field(alias="HostedZoneIdMarker")
    traffic_policy_instance_name_marker: str = Field(
        alias="TrafficPolicyInstanceNameMarker"
    )
    traffic_policy_instance_type_marker: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="TrafficPolicyInstanceTypeMarker")
    is_truncated: bool = Field(alias="IsTruncated")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrafficPolicyInstanceResponseModel(BaseModel):
    traffic_policy_instance: TrafficPolicyInstanceModel = Field(
        alias="TrafficPolicyInstance"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrafficPolicyResponseModel(BaseModel):
    traffic_policy: TrafficPolicyModel = Field(alias="TrafficPolicy")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrafficPolicyVersionResponseModel(BaseModel):
    traffic_policy: TrafficPolicyModel = Field(alias="TrafficPolicy")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTrafficPolicyResponseModel(BaseModel):
    traffic_policy: TrafficPolicyModel = Field(alias="TrafficPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrafficPolicyVersionsResponseModel(BaseModel):
    traffic_policies: List[TrafficPolicyModel] = Field(alias="TrafficPolicies")
    is_truncated: bool = Field(alias="IsTruncated")
    traffic_policy_version_marker: str = Field(alias="TrafficPolicyVersionMarker")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTrafficPolicyCommentResponseModel(BaseModel):
    traffic_policy: TrafficPolicyModel = Field(alias="TrafficPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDNSSECResponseModel(BaseModel):
    status: DNSSECStatusModel = Field(alias="Status")
    key_signing_keys: List[KeySigningKeyModel] = Field(alias="KeySigningKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGeoLocationResponseModel(BaseModel):
    geo_location_details: GeoLocationDetailsModel = Field(alias="GeoLocationDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGeoLocationsResponseModel(BaseModel):
    geo_location_details_list: List[GeoLocationDetailsModel] = Field(
        alias="GeoLocationDetailsList"
    )
    is_truncated: bool = Field(alias="IsTruncated")
    next_continent_code: str = Field(alias="NextContinentCode")
    next_country_code: str = Field(alias="NextCountryCode")
    next_subdivision_code: str = Field(alias="NextSubdivisionCode")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChangeRequestResourceRecordSetsChangedWaitModel(BaseModel):
    id: str = Field(alias="Id")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetHostedZoneLimitResponseModel(BaseModel):
    limit: HostedZoneLimitModel = Field(alias="Limit")
    count: int = Field(alias="Count")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetReusableDelegationSetLimitResponseModel(BaseModel):
    limit: ReusableDelegationSetLimitModel = Field(alias="Limit")
    count: int = Field(alias="Count")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HealthCheckObservationModel(BaseModel):
    region: Optional[
        Literal[
            "ap-northeast-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "eu-west-1",
            "sa-east-1",
            "us-east-1",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="Region")
    ip_address: Optional[str] = Field(default=None, alias="IPAddress")
    status_report: Optional[StatusReportModel] = Field(
        default=None, alias="StatusReport"
    )


class HostedZoneModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    caller_reference: str = Field(alias="CallerReference")
    config: Optional[HostedZoneConfigModel] = Field(default=None, alias="Config")
    resource_record_set_count: Optional[int] = Field(
        default=None, alias="ResourceRecordSetCount"
    )
    linked_service: Optional[LinkedServiceModel] = Field(
        default=None, alias="LinkedService"
    )


class HostedZoneSummaryModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    name: str = Field(alias="Name")
    owner: HostedZoneOwnerModel = Field(alias="Owner")


class ListCidrBlocksRequestListCidrBlocksPaginateModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    location_name: Optional[str] = Field(default=None, alias="LocationName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCidrCollectionsRequestListCidrCollectionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCidrLocationsRequestListCidrLocationsPaginateModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHealthChecksRequestListHealthChecksPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHostedZonesRequestListHostedZonesPaginateModel(BaseModel):
    delegation_set_id: Optional[str] = Field(default=None, alias="DelegationSetId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQueryLoggingConfigsRequestListQueryLoggingConfigsPaginateModel(BaseModel):
    hosted_zone_id: Optional[str] = Field(default=None, alias="HostedZoneId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceRecordSetsRequestListResourceRecordSetsPaginateModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVPCAssociationAuthorizationsRequestListVPCAssociationAuthorizationsPaginateModel(
    BaseModel
):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCidrLocationsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    cidr_locations: List[LocationSummaryModel] = Field(alias="CidrLocations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTrafficPoliciesResponseModel(BaseModel):
    traffic_policy_summaries: List[TrafficPolicySummaryModel] = Field(
        alias="TrafficPolicySummaries"
    )
    is_truncated: bool = Field(alias="IsTruncated")
    traffic_policy_id_marker: str = Field(alias="TrafficPolicyIdMarker")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceRecordSetModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="Type")
    set_identifier: Optional[str] = Field(default=None, alias="SetIdentifier")
    weight: Optional[int] = Field(default=None, alias="Weight")
    region: Optional[
        Literal[
            "af-south-1",
            "ap-east-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "ap-south-1",
            "ap-south-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-southeast-3",
            "ap-southeast-4",
            "ca-central-1",
            "cn-north-1",
            "cn-northwest-1",
            "eu-central-1",
            "eu-central-2",
            "eu-north-1",
            "eu-south-1",
            "eu-south-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "me-central-1",
            "me-south-1",
            "sa-east-1",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
        ]
    ] = Field(default=None, alias="Region")
    geo_location: Optional[GeoLocationModel] = Field(default=None, alias="GeoLocation")
    failover: Optional[Literal["PRIMARY", "SECONDARY"]] = Field(
        default=None, alias="Failover"
    )
    multi_value_answer: Optional[bool] = Field(default=None, alias="MultiValueAnswer")
    ttl: Optional[int] = Field(default=None, alias="TTL")
    resource_records: Optional[Sequence[ResourceRecordModel]] = Field(
        default=None, alias="ResourceRecords"
    )
    alias_target: Optional[AliasTargetModel] = Field(default=None, alias="AliasTarget")
    health_check_id: Optional[str] = Field(default=None, alias="HealthCheckId")
    traffic_policy_instance_id: Optional[str] = Field(
        default=None, alias="TrafficPolicyInstanceId"
    )
    cidr_routing_config: Optional[CidrRoutingConfigModel] = Field(
        default=None, alias="CidrRoutingConfig"
    )


class CreateHealthCheckRequestModel(BaseModel):
    caller_reference: str = Field(alias="CallerReference")
    health_check_config: HealthCheckConfigModel = Field(alias="HealthCheckConfig")


class ListTagsForResourceResponseModel(BaseModel):
    resource_tag_set: ResourceTagSetModel = Field(alias="ResourceTagSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourcesResponseModel(BaseModel):
    resource_tag_sets: List[ResourceTagSetModel] = Field(alias="ResourceTagSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HealthCheckModel(BaseModel):
    id: str = Field(alias="Id")
    caller_reference: str = Field(alias="CallerReference")
    health_check_config: HealthCheckConfigModel = Field(alias="HealthCheckConfig")
    health_check_version: int = Field(alias="HealthCheckVersion")
    linked_service: Optional[LinkedServiceModel] = Field(
        default=None, alias="LinkedService"
    )
    cloud_watch_alarm_configuration: Optional[
        CloudWatchAlarmConfigurationModel
    ] = Field(default=None, alias="CloudWatchAlarmConfiguration")


class GetHealthCheckLastFailureReasonResponseModel(BaseModel):
    health_check_observations: List[HealthCheckObservationModel] = Field(
        alias="HealthCheckObservations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHealthCheckStatusResponseModel(BaseModel):
    health_check_observations: List[HealthCheckObservationModel] = Field(
        alias="HealthCheckObservations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHostedZoneResponseModel(BaseModel):
    hosted_zone: HostedZoneModel = Field(alias="HostedZone")
    change_info: ChangeInfoModel = Field(alias="ChangeInfo")
    delegation_set: DelegationSetModel = Field(alias="DelegationSet")
    vp_c: VPCModel = Field(alias="VPC")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHostedZoneResponseModel(BaseModel):
    hosted_zone: HostedZoneModel = Field(alias="HostedZone")
    delegation_set: DelegationSetModel = Field(alias="DelegationSet")
    vp_cs: List[VPCModel] = Field(alias="VPCs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHostedZonesByNameResponseModel(BaseModel):
    hosted_zones: List[HostedZoneModel] = Field(alias="HostedZones")
    dns_name: str = Field(alias="DNSName")
    hosted_zone_id: str = Field(alias="HostedZoneId")
    is_truncated: bool = Field(alias="IsTruncated")
    next_dns_name: str = Field(alias="NextDNSName")
    next_hosted_zone_id: str = Field(alias="NextHostedZoneId")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHostedZonesResponseModel(BaseModel):
    hosted_zones: List[HostedZoneModel] = Field(alias="HostedZones")
    marker: str = Field(alias="Marker")
    is_truncated: bool = Field(alias="IsTruncated")
    next_marker: str = Field(alias="NextMarker")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateHostedZoneCommentResponseModel(BaseModel):
    hosted_zone: HostedZoneModel = Field(alias="HostedZone")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHostedZonesByVPCResponseModel(BaseModel):
    hosted_zone_summaries: List[HostedZoneSummaryModel] = Field(
        alias="HostedZoneSummaries"
    )
    max_items: str = Field(alias="MaxItems")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeModel(BaseModel):
    action: Literal["CREATE", "DELETE", "UPSERT"] = Field(alias="Action")
    resource_record_set: ResourceRecordSetModel = Field(alias="ResourceRecordSet")


class ListResourceRecordSetsResponseModel(BaseModel):
    resource_record_sets: List[ResourceRecordSetModel] = Field(
        alias="ResourceRecordSets"
    )
    is_truncated: bool = Field(alias="IsTruncated")
    next_record_name: str = Field(alias="NextRecordName")
    next_record_type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DS",
        "MX",
        "NAPTR",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "SRV",
        "TXT",
    ] = Field(alias="NextRecordType")
    next_record_identifier: str = Field(alias="NextRecordIdentifier")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateHealthCheckResponseModel(BaseModel):
    health_check: HealthCheckModel = Field(alias="HealthCheck")
    location: str = Field(alias="Location")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetHealthCheckResponseModel(BaseModel):
    health_check: HealthCheckModel = Field(alias="HealthCheck")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHealthChecksResponseModel(BaseModel):
    health_checks: List[HealthCheckModel] = Field(alias="HealthChecks")
    marker: str = Field(alias="Marker")
    is_truncated: bool = Field(alias="IsTruncated")
    next_marker: str = Field(alias="NextMarker")
    max_items: str = Field(alias="MaxItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateHealthCheckResponseModel(BaseModel):
    health_check: HealthCheckModel = Field(alias="HealthCheck")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ChangeBatchModel(BaseModel):
    changes: Sequence[ChangeModel] = Field(alias="Changes")
    comment: Optional[str] = Field(default=None, alias="Comment")


class ChangeResourceRecordSetsRequestModel(BaseModel):
    hosted_zone_id: str = Field(alias="HostedZoneId")
    change_batch: ChangeBatchModel = Field(alias="ChangeBatch")
