# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessPolicyDetailModel(BaseModel):
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    policy: Optional[Dict[str, Any]] = Field(default=None, alias="policy")
    policy_version: Optional[str] = Field(default=None, alias="policyVersion")
    type: Optional[Literal["data"]] = Field(default=None, alias="type")


class AccessPolicyStatsModel(BaseModel):
    data_policy_count: Optional[int] = Field(default=None, alias="DataPolicyCount")


class AccessPolicySummaryModel(BaseModel):
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    policy_version: Optional[str] = Field(default=None, alias="policyVersion")
    type: Optional[Literal["data"]] = Field(default=None, alias="type")


class CapacityLimitsModel(BaseModel):
    max_indexing_capacity_in_ocu: Optional[int] = Field(
        default=None, alias="maxIndexingCapacityInOCU"
    )
    max_search_capacity_in_ocu: Optional[int] = Field(
        default=None, alias="maxSearchCapacityInOCU"
    )


class BatchGetCollectionRequestModel(BaseModel):
    ids: Optional[Sequence[str]] = Field(default=None, alias="ids")
    names: Optional[Sequence[str]] = Field(default=None, alias="names")


class CollectionDetailModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    collection_endpoint: Optional[str] = Field(default=None, alias="collectionEndpoint")
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    dashboard_endpoint: Optional[str] = Field(default=None, alias="dashboardEndpoint")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="status"
    )
    type: Optional[Literal["SEARCH", "TIMESERIES"]] = Field(default=None, alias="type")


class CollectionErrorDetailModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class BatchGetVpcEndpointRequestModel(BaseModel):
    ids: Sequence[str] = Field(alias="ids")


class VpcEndpointDetailModel(BaseModel):
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    status: Optional[Literal["ACTIVE", "DELETING", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")


class VpcEndpointErrorDetailModel(BaseModel):
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    id: Optional[str] = Field(default=None, alias="id")


class CollectionFiltersModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="status"
    )


class CollectionSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="status"
    )


class CreateAccessPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    policy: str = Field(alias="policy")
    type: Literal["data"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")


class CreateCollectionDetailModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="status"
    )
    type: Optional[Literal["SEARCH", "TIMESERIES"]] = Field(default=None, alias="type")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class SamlConfigOptionsModel(BaseModel):
    metadata: str = Field(alias="metadata")
    group_attribute: Optional[str] = Field(default=None, alias="groupAttribute")
    session_timeout: Optional[int] = Field(default=None, alias="sessionTimeout")
    user_attribute: Optional[str] = Field(default=None, alias="userAttribute")


class CreateSecurityPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    policy: str = Field(alias="policy")
    type: Literal["encryption", "network"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")


class SecurityPolicyDetailModel(BaseModel):
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    policy: Optional[Dict[str, Any]] = Field(default=None, alias="policy")
    policy_version: Optional[str] = Field(default=None, alias="policyVersion")
    type: Optional[Literal["encryption", "network"]] = Field(default=None, alias="type")


class CreateVpcEndpointDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "DELETING", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )


class CreateVpcEndpointRequestModel(BaseModel):
    name: str = Field(alias="name")
    subnet_ids: Sequence[str] = Field(alias="subnetIds")
    vpc_id: str = Field(alias="vpcId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )


class DeleteAccessPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["data"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteCollectionDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="status"
    )


class DeleteCollectionRequestModel(BaseModel):
    id: str = Field(alias="id")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteSecurityConfigRequestModel(BaseModel):
    id: str = Field(alias="id")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteSecurityPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["encryption", "network"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteVpcEndpointDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "DELETING", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )


class DeleteVpcEndpointRequestModel(BaseModel):
    id: str = Field(alias="id")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GetAccessPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["data"] = Field(alias="type")


class SecurityConfigStatsModel(BaseModel):
    saml_config_count: Optional[int] = Field(default=None, alias="SamlConfigCount")


class SecurityPolicyStatsModel(BaseModel):
    encryption_policy_count: Optional[int] = Field(
        default=None, alias="EncryptionPolicyCount"
    )
    network_policy_count: Optional[int] = Field(
        default=None, alias="NetworkPolicyCount"
    )


class GetSecurityConfigRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetSecurityPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["encryption", "network"] = Field(alias="type")


class ListAccessPoliciesRequestModel(BaseModel):
    type: Literal["data"] = Field(alias="type")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    resource: Optional[Sequence[str]] = Field(default=None, alias="resource")


class ListSecurityConfigsRequestModel(BaseModel):
    type: Literal["saml"] = Field(alias="type")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SecurityConfigSummaryModel(BaseModel):
    config_version: Optional[str] = Field(default=None, alias="configVersion")
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    type: Optional[Literal["saml"]] = Field(default=None, alias="type")


class ListSecurityPoliciesRequestModel(BaseModel):
    type: Literal["encryption", "network"] = Field(alias="type")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    resource: Optional[Sequence[str]] = Field(default=None, alias="resource")


class SecurityPolicySummaryModel(BaseModel):
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    policy_version: Optional[str] = Field(default=None, alias="policyVersion")
    type: Optional[Literal["encryption", "network"]] = Field(default=None, alias="type")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class VpcEndpointFiltersModel(BaseModel):
    status: Optional[Literal["ACTIVE", "DELETING", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )


class VpcEndpointSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "DELETING", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAccessPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    policy_version: str = Field(alias="policyVersion")
    type: Literal["data"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    policy: Optional[str] = Field(default=None, alias="policy")


class UpdateCollectionDetailModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]] = Field(
        default=None, alias="status"
    )
    type: Optional[Literal["SEARCH", "TIMESERIES"]] = Field(default=None, alias="type")


class UpdateCollectionRequestModel(BaseModel):
    id: str = Field(alias="id")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateSecurityPolicyRequestModel(BaseModel):
    name: str = Field(alias="name")
    policy_version: str = Field(alias="policyVersion")
    type: Literal["encryption", "network"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    policy: Optional[str] = Field(default=None, alias="policy")


class UpdateVpcEndpointDetailModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    name: Optional[str] = Field(default=None, alias="name")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    status: Optional[Literal["ACTIVE", "DELETING", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")


class UpdateVpcEndpointRequestModel(BaseModel):
    id: str = Field(alias="id")
    add_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="addSecurityGroupIds"
    )
    add_subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="addSubnetIds")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    remove_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="removeSecurityGroupIds"
    )
    remove_subnet_ids: Optional[Sequence[str]] = Field(
        default=None, alias="removeSubnetIds"
    )


class AccountSettingsDetailModel(BaseModel):
    capacity_limits: Optional[CapacityLimitsModel] = Field(
        default=None, alias="capacityLimits"
    )


class UpdateAccountSettingsRequestModel(BaseModel):
    capacity_limits: Optional[CapacityLimitsModel] = Field(
        default=None, alias="capacityLimits"
    )


class BatchGetCollectionResponseModel(BaseModel):
    collection_details: List[CollectionDetailModel] = Field(alias="collectionDetails")
    collection_error_details: List[CollectionErrorDetailModel] = Field(
        alias="collectionErrorDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccessPolicyResponseModel(BaseModel):
    access_policy_detail: AccessPolicyDetailModel = Field(alias="accessPolicyDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessPolicyResponseModel(BaseModel):
    access_policy_detail: AccessPolicyDetailModel = Field(alias="accessPolicyDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessPoliciesResponseModel(BaseModel):
    access_policy_summaries: List[AccessPolicySummaryModel] = Field(
        alias="accessPolicySummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccessPolicyResponseModel(BaseModel):
    access_policy_detail: AccessPolicyDetailModel = Field(alias="accessPolicyDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetVpcEndpointResponseModel(BaseModel):
    vpc_endpoint_details: List[VpcEndpointDetailModel] = Field(
        alias="vpcEndpointDetails"
    )
    vpc_endpoint_error_details: List[VpcEndpointErrorDetailModel] = Field(
        alias="vpcEndpointErrorDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCollectionsRequestModel(BaseModel):
    collection_filters: Optional[CollectionFiltersModel] = Field(
        default=None, alias="collectionFilters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListCollectionsResponseModel(BaseModel):
    collection_summaries: List[CollectionSummaryModel] = Field(
        alias="collectionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCollectionResponseModel(BaseModel):
    create_collection_detail: CreateCollectionDetailModel = Field(
        alias="createCollectionDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCollectionRequestModel(BaseModel):
    name: str = Field(alias="name")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    type: Optional[Literal["SEARCH", "TIMESERIES"]] = Field(default=None, alias="type")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateSecurityConfigRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["saml"] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    saml_options: Optional[SamlConfigOptionsModel] = Field(
        default=None, alias="samlOptions"
    )


class SecurityConfigDetailModel(BaseModel):
    config_version: Optional[str] = Field(default=None, alias="configVersion")
    created_date: Optional[int] = Field(default=None, alias="createdDate")
    description: Optional[str] = Field(default=None, alias="description")
    id: Optional[str] = Field(default=None, alias="id")
    last_modified_date: Optional[int] = Field(default=None, alias="lastModifiedDate")
    saml_options: Optional[SamlConfigOptionsModel] = Field(
        default=None, alias="samlOptions"
    )
    type: Optional[Literal["saml"]] = Field(default=None, alias="type")


class UpdateSecurityConfigRequestModel(BaseModel):
    config_version: str = Field(alias="configVersion")
    id: str = Field(alias="id")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    saml_options: Optional[SamlConfigOptionsModel] = Field(
        default=None, alias="samlOptions"
    )


class CreateSecurityPolicyResponseModel(BaseModel):
    security_policy_detail: SecurityPolicyDetailModel = Field(
        alias="securityPolicyDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSecurityPolicyResponseModel(BaseModel):
    security_policy_detail: SecurityPolicyDetailModel = Field(
        alias="securityPolicyDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSecurityPolicyResponseModel(BaseModel):
    security_policy_detail: SecurityPolicyDetailModel = Field(
        alias="securityPolicyDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVpcEndpointResponseModel(BaseModel):
    create_vpc_endpoint_detail: CreateVpcEndpointDetailModel = Field(
        alias="createVpcEndpointDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCollectionResponseModel(BaseModel):
    delete_collection_detail: DeleteCollectionDetailModel = Field(
        alias="deleteCollectionDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVpcEndpointResponseModel(BaseModel):
    delete_vpc_endpoint_detail: DeleteVpcEndpointDetailModel = Field(
        alias="deleteVpcEndpointDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPoliciesStatsResponseModel(BaseModel):
    access_policy_stats: AccessPolicyStatsModel = Field(alias="AccessPolicyStats")
    security_config_stats: SecurityConfigStatsModel = Field(alias="SecurityConfigStats")
    security_policy_stats: SecurityPolicyStatsModel = Field(alias="SecurityPolicyStats")
    total_policy_count: int = Field(alias="TotalPolicyCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityConfigsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    security_config_summaries: List[SecurityConfigSummaryModel] = Field(
        alias="securityConfigSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityPoliciesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    security_policy_summaries: List[SecurityPolicySummaryModel] = Field(
        alias="securityPolicySummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVpcEndpointsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    vpc_endpoint_filters: Optional[VpcEndpointFiltersModel] = Field(
        default=None, alias="vpcEndpointFilters"
    )


class ListVpcEndpointsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    vpc_endpoint_summaries: List[VpcEndpointSummaryModel] = Field(
        alias="vpcEndpointSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCollectionResponseModel(BaseModel):
    update_collection_detail: UpdateCollectionDetailModel = Field(
        alias="updateCollectionDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVpcEndpointResponseModel(BaseModel):
    update_vpc_endpoint_detail: UpdateVpcEndpointDetailModel = Field(
        alias="UpdateVpcEndpointDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccountSettingsResponseModel(BaseModel):
    account_settings_detail: AccountSettingsDetailModel = Field(
        alias="accountSettingsDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountSettingsResponseModel(BaseModel):
    account_settings_detail: AccountSettingsDetailModel = Field(
        alias="accountSettingsDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSecurityConfigResponseModel(BaseModel):
    security_config_detail: SecurityConfigDetailModel = Field(
        alias="securityConfigDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSecurityConfigResponseModel(BaseModel):
    security_config_detail: SecurityConfigDetailModel = Field(
        alias="securityConfigDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSecurityConfigResponseModel(BaseModel):
    security_config_detail: SecurityConfigDetailModel = Field(
        alias="securityConfigDetail"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
