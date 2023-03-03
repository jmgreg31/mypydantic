# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptInvitationRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")


class AccountModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    email_address: str = Field(alias="EmailAddress")


class AdministratorModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    graph_arn: Optional[str] = Field(default=None, alias="GraphArn")
    delegation_time: Optional[datetime] = Field(default=None, alias="DelegationTime")


class BatchGetGraphMemberDatasourcesRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class UnprocessedAccountModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    reason: Optional[str] = Field(default=None, alias="Reason")


class BatchGetMembershipDatasourcesRequestModel(BaseModel):
    graph_arns: Sequence[str] = Field(alias="GraphArns")


class UnprocessedGraphModel(BaseModel):
    graph_arn: Optional[str] = Field(default=None, alias="GraphArn")
    reason: Optional[str] = Field(default=None, alias="Reason")


class CreateGraphRequestModel(BaseModel):
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class TimestampForCollectionModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class DatasourcePackageUsageInfoModel(BaseModel):
    volume_usage_in_bytes: Optional[int] = Field(
        default=None, alias="VolumeUsageInBytes"
    )
    volume_usage_update_time: Optional[datetime] = Field(
        default=None, alias="VolumeUsageUpdateTime"
    )


class DeleteGraphRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")


class DeleteMembersRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class DescribeOrganizationConfigurationRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")


class DisassociateMembershipRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")


class EnableOrganizationAdminAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")


class GetMembersRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    account_ids: Sequence[str] = Field(alias="AccountIds")


class GraphModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class ListDatasourcePackagesRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGraphsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListInvitationsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMembersRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListOrganizationAdminAccountsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class RejectInvitationRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")


class StartMonitoringMemberRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    account_id: str = Field(alias="AccountId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDatasourcePackagesRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    datasource_packages: Sequence[Literal["DETECTIVE_CORE", "EKS_AUDIT"]] = Field(
        alias="DatasourcePackages"
    )


class UpdateOrganizationConfigurationRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    auto_enable: Optional[bool] = Field(default=None, alias="AutoEnable")


class CreateMembersRequestModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    accounts: Sequence[AccountModel] = Field(alias="Accounts")
    message: Optional[str] = Field(default=None, alias="Message")
    disable_email_notification: Optional[bool] = Field(
        default=None, alias="DisableEmailNotification"
    )


class CreateGraphResponseModel(BaseModel):
    graph_arn: str = Field(alias="GraphArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationConfigurationResponseModel(BaseModel):
    auto_enable: bool = Field(alias="AutoEnable")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOrganizationAdminAccountsResponseModel(BaseModel):
    administrators: List[AdministratorModel] = Field(alias="Administrators")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteMembersResponseModel(BaseModel):
    account_ids: List[str] = Field(alias="AccountIds")
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DatasourcePackageIngestDetailModel(BaseModel):
    datasource_package_ingest_state: Optional[
        Literal["DISABLED", "STARTED", "STOPPED"]
    ] = Field(default=None, alias="DatasourcePackageIngestState")
    last_ingest_state_change: Optional[
        Dict[Literal["DISABLED", "STARTED", "STOPPED"], TimestampForCollectionModel]
    ] = Field(default=None, alias="LastIngestStateChange")


class MembershipDatasourcesModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    graph_arn: Optional[str] = Field(default=None, alias="GraphArn")
    datasource_package_ingest_history: Optional[
        Dict[
            Literal["DETECTIVE_CORE", "EKS_AUDIT"],
            Dict[
                Literal["DISABLED", "STARTED", "STOPPED"], TimestampForCollectionModel
            ],
        ]
    ] = Field(default=None, alias="DatasourcePackageIngestHistory")


class MemberDetailModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    graph_arn: Optional[str] = Field(default=None, alias="GraphArn")
    master_id: Optional[str] = Field(default=None, alias="MasterId")
    administrator_id: Optional[str] = Field(default=None, alias="AdministratorId")
    status: Optional[
        Literal[
            "ACCEPTED_BUT_DISABLED",
            "ENABLED",
            "INVITED",
            "VERIFICATION_FAILED",
            "VERIFICATION_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")
    disabled_reason: Optional[Literal["VOLUME_TOO_HIGH", "VOLUME_UNKNOWN"]] = Field(
        default=None, alias="DisabledReason"
    )
    invited_time: Optional[datetime] = Field(default=None, alias="InvitedTime")
    updated_time: Optional[datetime] = Field(default=None, alias="UpdatedTime")
    volume_usage_in_bytes: Optional[int] = Field(
        default=None, alias="VolumeUsageInBytes"
    )
    volume_usage_updated_time: Optional[datetime] = Field(
        default=None, alias="VolumeUsageUpdatedTime"
    )
    percent_of_graph_utilization: Optional[float] = Field(
        default=None, alias="PercentOfGraphUtilization"
    )
    percent_of_graph_utilization_updated_time: Optional[datetime] = Field(
        default=None, alias="PercentOfGraphUtilizationUpdatedTime"
    )
    invitation_type: Optional[Literal["INVITATION", "ORGANIZATION"]] = Field(
        default=None, alias="InvitationType"
    )
    volume_usage_by_datasource_package: Optional[
        Dict[Literal["DETECTIVE_CORE", "EKS_AUDIT"], DatasourcePackageUsageInfoModel]
    ] = Field(default=None, alias="VolumeUsageByDatasourcePackage")
    datasource_package_ingest_states: Optional[
        Dict[
            Literal["DETECTIVE_CORE", "EKS_AUDIT"],
            Literal["DISABLED", "STARTED", "STOPPED"],
        ]
    ] = Field(default=None, alias="DatasourcePackageIngestStates")


class ListGraphsResponseModel(BaseModel):
    graph_list: List[GraphModel] = Field(alias="GraphList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasourcePackagesResponseModel(BaseModel):
    datasource_packages: Dict[
        Literal["DETECTIVE_CORE", "EKS_AUDIT"], DatasourcePackageIngestDetailModel
    ] = Field(alias="DatasourcePackages")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetGraphMemberDatasourcesResponseModel(BaseModel):
    member_datasources: List[MembershipDatasourcesModel] = Field(
        alias="MemberDatasources"
    )
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetMembershipDatasourcesResponseModel(BaseModel):
    membership_datasources: List[MembershipDatasourcesModel] = Field(
        alias="MembershipDatasources"
    )
    unprocessed_graphs: List[UnprocessedGraphModel] = Field(alias="UnprocessedGraphs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMembersResponseModel(BaseModel):
    members: List[MemberDetailModel] = Field(alias="Members")
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMembersResponseModel(BaseModel):
    member_details: List[MemberDetailModel] = Field(alias="MemberDetails")
    unprocessed_accounts: List[UnprocessedAccountModel] = Field(
        alias="UnprocessedAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInvitationsResponseModel(BaseModel):
    invitations: List[MemberDetailModel] = Field(alias="Invitations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMembersResponseModel(BaseModel):
    member_details: List[MemberDetailModel] = Field(alias="MemberDetails")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
