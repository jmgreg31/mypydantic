# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptHandshakeRequestModel(BaseModel):
    handshake_id: str = Field(alias="HandshakeId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AccountModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    email: Optional[str] = Field(default=None, alias="Email")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["ACTIVE", "PENDING_CLOSURE", "SUSPENDED"]] = Field(
        default=None, alias="Status"
    )
    joined_method: Optional[Literal["CREATED", "INVITED"]] = Field(
        default=None, alias="JoinedMethod"
    )
    joined_timestamp: Optional[datetime] = Field(default=None, alias="JoinedTimestamp")


class AttachPolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    target_id: str = Field(alias="TargetId")


class CancelHandshakeRequestModel(BaseModel):
    handshake_id: str = Field(alias="HandshakeId")


class ChildModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]] = Field(
        default=None, alias="Type"
    )


class CloseAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateAccountStatusModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    state: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="State"
    )
    requested_timestamp: Optional[datetime] = Field(
        default=None, alias="RequestedTimestamp"
    )
    completed_timestamp: Optional[datetime] = Field(
        default=None, alias="CompletedTimestamp"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    gov_cloud_account_id: Optional[str] = Field(default=None, alias="GovCloudAccountId")
    failure_reason: Optional[
        Literal[
            "ACCOUNT_LIMIT_EXCEEDED",
            "CONCURRENT_ACCOUNT_MODIFICATION",
            "EMAIL_ALREADY_EXISTS",
            "FAILED_BUSINESS_VALIDATION",
            "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
            "INTERNAL_FAILURE",
            "INVALID_ADDRESS",
            "INVALID_EMAIL",
            "INVALID_IDENTITY_FOR_BUSINESS_VALIDATION",
            "INVALID_PAYMENT_INSTRUMENT",
            "MISSING_BUSINESS_VALIDATION",
            "MISSING_PAYMENT_INSTRUMENT",
            "PENDING_BUSINESS_VALIDATION",
            "UNKNOWN_BUSINESS_VALIDATION",
            "UPDATE_EXISTING_RESOURCE_POLICY_WITH_TAGS_NOT_SUPPORTED",
        ]
    ] = Field(default=None, alias="FailureReason")


class CreateOrganizationRequestModel(BaseModel):
    feature_set: Optional[Literal["ALL", "CONSOLIDATED_BILLING"]] = Field(
        default=None, alias="FeatureSet"
    )


class OrganizationalUnitModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")


class DeclineHandshakeRequestModel(BaseModel):
    handshake_id: str = Field(alias="HandshakeId")


class DelegatedAdministratorModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    email: Optional[str] = Field(default=None, alias="Email")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["ACTIVE", "PENDING_CLOSURE", "SUSPENDED"]] = Field(
        default=None, alias="Status"
    )
    joined_method: Optional[Literal["CREATED", "INVITED"]] = Field(
        default=None, alias="JoinedMethod"
    )
    joined_timestamp: Optional[datetime] = Field(default=None, alias="JoinedTimestamp")
    delegation_enabled_date: Optional[datetime] = Field(
        default=None, alias="DelegationEnabledDate"
    )


class DelegatedServiceModel(BaseModel):
    service_principal: Optional[str] = Field(default=None, alias="ServicePrincipal")
    delegation_enabled_date: Optional[datetime] = Field(
        default=None, alias="DelegationEnabledDate"
    )


class DeleteOrganizationalUnitRequestModel(BaseModel):
    organizational_unit_id: str = Field(alias="OrganizationalUnitId")


class DeletePolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")


class DeregisterDelegatedAdministratorRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    service_principal: str = Field(alias="ServicePrincipal")


class DescribeAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class DescribeCreateAccountStatusRequestModel(BaseModel):
    create_account_request_id: str = Field(alias="CreateAccountRequestId")


class DescribeEffectivePolicyRequestModel(BaseModel):
    policy_type: Literal[
        "AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "TAG_POLICY"
    ] = Field(alias="PolicyType")
    target_id: Optional[str] = Field(default=None, alias="TargetId")


class EffectivePolicyModel(BaseModel):
    policy_content: Optional[str] = Field(default=None, alias="PolicyContent")
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    target_id: Optional[str] = Field(default=None, alias="TargetId")
    policy_type: Optional[
        Literal["AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "TAG_POLICY"]
    ] = Field(default=None, alias="PolicyType")


class DescribeHandshakeRequestModel(BaseModel):
    handshake_id: str = Field(alias="HandshakeId")


class DescribeOrganizationalUnitRequestModel(BaseModel):
    organizational_unit_id: str = Field(alias="OrganizationalUnitId")


class DescribePolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")


class DetachPolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    target_id: str = Field(alias="TargetId")


class DisableAWSServiceAccessRequestModel(BaseModel):
    service_principal: str = Field(alias="ServicePrincipal")


class DisablePolicyTypeRequestModel(BaseModel):
    root_id: str = Field(alias="RootId")
    policy_type: Literal[
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ] = Field(alias="PolicyType")


class EnableAWSServiceAccessRequestModel(BaseModel):
    service_principal: str = Field(alias="ServicePrincipal")


class EnablePolicyTypeRequestModel(BaseModel):
    root_id: str = Field(alias="RootId")
    policy_type: Literal[
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ] = Field(alias="PolicyType")


class EnabledServicePrincipalModel(BaseModel):
    service_principal: Optional[str] = Field(default=None, alias="ServicePrincipal")
    date_enabled: Optional[datetime] = Field(default=None, alias="DateEnabled")


class HandshakeFilterModel(BaseModel):
    action_type: Optional[
        Literal[
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
            "APPROVE_ALL_FEATURES",
            "ENABLE_ALL_FEATURES",
            "INVITE",
        ]
    ] = Field(default=None, alias="ActionType")
    parent_handshake_id: Optional[str] = Field(default=None, alias="ParentHandshakeId")


class HandshakePartyModel(BaseModel):
    id: str = Field(alias="Id")
    type: Literal["ACCOUNT", "EMAIL", "ORGANIZATION"] = Field(alias="Type")


class HandshakeResourceModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    type: Optional[
        Literal[
            "ACCOUNT",
            "EMAIL",
            "MASTER_EMAIL",
            "MASTER_NAME",
            "NOTES",
            "ORGANIZATION",
            "ORGANIZATION_FEATURE_SET",
            "PARENT_HANDSHAKE",
        ]
    ] = Field(default=None, alias="Type")
    resources: Optional[List[Dict[str, Any]]] = Field(default=None, alias="Resources")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAWSServiceAccessForOrganizationRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAccountsForParentRequestModel(BaseModel):
    parent_id: str = Field(alias="ParentId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListAccountsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListChildrenRequestModel(BaseModel):
    parent_id: str = Field(alias="ParentId")
    child_type: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"] = Field(alias="ChildType")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListCreateAccountStatusRequestModel(BaseModel):
    states: Optional[Sequence[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]]] = Field(
        default=None, alias="States"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDelegatedAdministratorsRequestModel(BaseModel):
    service_principal: Optional[str] = Field(default=None, alias="ServicePrincipal")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDelegatedServicesForAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListOrganizationalUnitsForParentRequestModel(BaseModel):
    parent_id: str = Field(alias="ParentId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListParentsRequestModel(BaseModel):
    child_id: str = Field(alias="ChildId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ParentModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["ORGANIZATIONAL_UNIT", "ROOT"]] = Field(
        default=None, alias="Type"
    )


class ListPoliciesForTargetRequestModel(BaseModel):
    target_id: str = Field(alias="TargetId")
    filter: Literal[
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ] = Field(alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PolicySummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[
        Literal[
            "AISERVICES_OPT_OUT_POLICY",
            "BACKUP_POLICY",
            "SERVICE_CONTROL_POLICY",
            "TAG_POLICY",
        ]
    ] = Field(default=None, alias="Type")
    aws_managed: Optional[bool] = Field(default=None, alias="AwsManaged")


class ListPoliciesRequestModel(BaseModel):
    filter: Literal[
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ] = Field(alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListRootsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTargetsForPolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PolicyTargetSummaryModel(BaseModel):
    target_id: Optional[str] = Field(default=None, alias="TargetId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"]] = Field(
        default=None, alias="Type"
    )


class MoveAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    source_parent_id: str = Field(alias="SourceParentId")
    destination_parent_id: str = Field(alias="DestinationParentId")


class PolicyTypeSummaryModel(BaseModel):
    type: Optional[
        Literal[
            "AISERVICES_OPT_OUT_POLICY",
            "BACKUP_POLICY",
            "SERVICE_CONTROL_POLICY",
            "TAG_POLICY",
        ]
    ] = Field(default=None, alias="Type")
    status: Optional[Literal["ENABLED", "PENDING_DISABLE", "PENDING_ENABLE"]] = Field(
        default=None, alias="Status"
    )


class RegisterDelegatedAdministratorRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    service_principal: str = Field(alias="ServicePrincipal")


class RemoveAccountFromOrganizationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class ResourcePolicySummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")


class UntagResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateOrganizationalUnitRequestModel(BaseModel):
    organizational_unit_id: str = Field(alias="OrganizationalUnitId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdatePolicyRequestModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    content: Optional[str] = Field(default=None, alias="Content")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountResponseModel(BaseModel):
    account: AccountModel = Field(alias="Account")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountsForParentResponseModel(BaseModel):
    accounts: List[AccountModel] = Field(alias="Accounts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountsResponseModel(BaseModel):
    accounts: List[AccountModel] = Field(alias="Accounts")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListChildrenResponseModel(BaseModel):
    children: List[ChildModel] = Field(alias="Children")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccountRequestModel(BaseModel):
    email: str = Field(alias="Email")
    account_name: str = Field(alias="AccountName")
    role_name: Optional[str] = Field(default=None, alias="RoleName")
    iam_user_access_to_billing: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="IamUserAccessToBilling"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateGovCloudAccountRequestModel(BaseModel):
    email: str = Field(alias="Email")
    account_name: str = Field(alias="AccountName")
    role_name: Optional[str] = Field(default=None, alias="RoleName")
    iam_user_access_to_billing: Optional[Literal["ALLOW", "DENY"]] = Field(
        default=None, alias="IamUserAccessToBilling"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateOrganizationalUnitRequestModel(BaseModel):
    parent_id: str = Field(alias="ParentId")
    name: str = Field(alias="Name")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreatePolicyRequestModel(BaseModel):
    content: str = Field(alias="Content")
    description: str = Field(alias="Description")
    name: str = Field(alias="Name")
    type: Literal[
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ] = Field(alias="Type")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyRequestModel(BaseModel):
    content: str = Field(alias="Content")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateAccountResponseModel(BaseModel):
    create_account_status: CreateAccountStatusModel = Field(alias="CreateAccountStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGovCloudAccountResponseModel(BaseModel):
    create_account_status: CreateAccountStatusModel = Field(alias="CreateAccountStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCreateAccountStatusResponseModel(BaseModel):
    create_account_status: CreateAccountStatusModel = Field(alias="CreateAccountStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCreateAccountStatusResponseModel(BaseModel):
    create_account_statuses: List[CreateAccountStatusModel] = Field(
        alias="CreateAccountStatuses"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOrganizationalUnitResponseModel(BaseModel):
    organizational_unit: OrganizationalUnitModel = Field(alias="OrganizationalUnit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationalUnitResponseModel(BaseModel):
    organizational_unit: OrganizationalUnitModel = Field(alias="OrganizationalUnit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrganizationalUnitsForParentResponseModel(BaseModel):
    organizational_units: List[OrganizationalUnitModel] = Field(
        alias="OrganizationalUnits"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateOrganizationalUnitResponseModel(BaseModel):
    organizational_unit: OrganizationalUnitModel = Field(alias="OrganizationalUnit")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDelegatedAdministratorsResponseModel(BaseModel):
    delegated_administrators: List[DelegatedAdministratorModel] = Field(
        alias="DelegatedAdministrators"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDelegatedServicesForAccountResponseModel(BaseModel):
    delegated_services: List[DelegatedServiceModel] = Field(alias="DelegatedServices")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEffectivePolicyResponseModel(BaseModel):
    effective_policy: EffectivePolicyModel = Field(alias="EffectivePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAWSServiceAccessForOrganizationResponseModel(BaseModel):
    enabled_service_principals: List[EnabledServicePrincipalModel] = Field(
        alias="EnabledServicePrincipals"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHandshakesForAccountRequestModel(BaseModel):
    filter: Optional[HandshakeFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListHandshakesForOrganizationRequestModel(BaseModel):
    filter: Optional[HandshakeFilterModel] = Field(default=None, alias="Filter")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class HandshakeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    parties: Optional[List[HandshakePartyModel]] = Field(default=None, alias="Parties")
    state: Optional[
        Literal["ACCEPTED", "CANCELED", "DECLINED", "EXPIRED", "OPEN", "REQUESTED"]
    ] = Field(default=None, alias="State")
    requested_timestamp: Optional[datetime] = Field(
        default=None, alias="RequestedTimestamp"
    )
    expiration_timestamp: Optional[datetime] = Field(
        default=None, alias="ExpirationTimestamp"
    )
    action: Optional[
        Literal[
            "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE",
            "APPROVE_ALL_FEATURES",
            "ENABLE_ALL_FEATURES",
            "INVITE",
        ]
    ] = Field(default=None, alias="Action")
    resources: Optional[List[HandshakeResourceModel]] = Field(
        default=None, alias="Resources"
    )


class InviteAccountToOrganizationRequestModel(BaseModel):
    target: HandshakePartyModel = Field(alias="Target")
    notes: Optional[str] = Field(default=None, alias="Notes")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListAWSServiceAccessForOrganizationRequestListAWSServiceAccessForOrganizationPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountsForParentRequestListAccountsForParentPaginateModel(BaseModel):
    parent_id: str = Field(alias="ParentId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountsRequestListAccountsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListChildrenRequestListChildrenPaginateModel(BaseModel):
    parent_id: str = Field(alias="ParentId")
    child_type: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"] = Field(alias="ChildType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCreateAccountStatusRequestListCreateAccountStatusPaginateModel(BaseModel):
    states: Optional[Sequence[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]]] = Field(
        default=None, alias="States"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDelegatedAdministratorsRequestListDelegatedAdministratorsPaginateModel(
    BaseModel
):
    service_principal: Optional[str] = Field(default=None, alias="ServicePrincipal")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDelegatedServicesForAccountRequestListDelegatedServicesForAccountPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHandshakesForAccountRequestListHandshakesForAccountPaginateModel(BaseModel):
    filter: Optional[HandshakeFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListHandshakesForOrganizationRequestListHandshakesForOrganizationPaginateModel(
    BaseModel
):
    filter: Optional[HandshakeFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOrganizationalUnitsForParentRequestListOrganizationalUnitsForParentPaginateModel(
    BaseModel
):
    parent_id: str = Field(alias="ParentId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListParentsRequestListParentsPaginateModel(BaseModel):
    child_id: str = Field(alias="ChildId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPoliciesForTargetRequestListPoliciesForTargetPaginateModel(BaseModel):
    target_id: str = Field(alias="TargetId")
    filter: Literal[
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ] = Field(alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPoliciesRequestListPoliciesPaginateModel(BaseModel):
    filter: Literal[
        "AISERVICES_OPT_OUT_POLICY",
        "BACKUP_POLICY",
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
    ] = Field(alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRootsRequestListRootsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTargetsForPolicyRequestListTargetsForPolicyPaginateModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListParentsResponseModel(BaseModel):
    parents: List[ParentModel] = Field(alias="Parents")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPoliciesForTargetResponseModel(BaseModel):
    policies: List[PolicySummaryModel] = Field(alias="Policies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPoliciesResponseModel(BaseModel):
    policies: List[PolicySummaryModel] = Field(alias="Policies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PolicyModel(BaseModel):
    policy_summary: Optional[PolicySummaryModel] = Field(
        default=None, alias="PolicySummary"
    )
    content: Optional[str] = Field(default=None, alias="Content")


class ListTargetsForPolicyResponseModel(BaseModel):
    targets: List[PolicyTargetSummaryModel] = Field(alias="Targets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OrganizationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    feature_set: Optional[Literal["ALL", "CONSOLIDATED_BILLING"]] = Field(
        default=None, alias="FeatureSet"
    )
    master_account_arn: Optional[str] = Field(default=None, alias="MasterAccountArn")
    master_account_id: Optional[str] = Field(default=None, alias="MasterAccountId")
    master_account_email: Optional[str] = Field(
        default=None, alias="MasterAccountEmail"
    )
    available_policy_types: Optional[List[PolicyTypeSummaryModel]] = Field(
        default=None, alias="AvailablePolicyTypes"
    )


class RootModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    policy_types: Optional[List[PolicyTypeSummaryModel]] = Field(
        default=None, alias="PolicyTypes"
    )


class ResourcePolicyModel(BaseModel):
    resource_policy_summary: Optional[ResourcePolicySummaryModel] = Field(
        default=None, alias="ResourcePolicySummary"
    )
    content: Optional[str] = Field(default=None, alias="Content")


class AcceptHandshakeResponseModel(BaseModel):
    handshake: HandshakeModel = Field(alias="Handshake")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelHandshakeResponseModel(BaseModel):
    handshake: HandshakeModel = Field(alias="Handshake")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeclineHandshakeResponseModel(BaseModel):
    handshake: HandshakeModel = Field(alias="Handshake")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHandshakeResponseModel(BaseModel):
    handshake: HandshakeModel = Field(alias="Handshake")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableAllFeaturesResponseModel(BaseModel):
    handshake: HandshakeModel = Field(alias="Handshake")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InviteAccountToOrganizationResponseModel(BaseModel):
    handshake: HandshakeModel = Field(alias="Handshake")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHandshakesForAccountResponseModel(BaseModel):
    handshakes: List[HandshakeModel] = Field(alias="Handshakes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHandshakesForOrganizationResponseModel(BaseModel):
    handshakes: List[HandshakeModel] = Field(alias="Handshakes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOrganizationResponseModel(BaseModel):
    organization: OrganizationModel = Field(alias="Organization")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationResponseModel(BaseModel):
    organization: OrganizationModel = Field(alias="Organization")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisablePolicyTypeResponseModel(BaseModel):
    root: RootModel = Field(alias="Root")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnablePolicyTypeResponseModel(BaseModel):
    root: RootModel = Field(alias="Root")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRootsResponseModel(BaseModel):
    roots: List[RootModel] = Field(alias="Roots")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeResourcePolicyResponseModel(BaseModel):
    resource_policy: ResourcePolicyModel = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourcePolicyResponseModel(BaseModel):
    resource_policy: ResourcePolicyModel = Field(alias="ResourcePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
