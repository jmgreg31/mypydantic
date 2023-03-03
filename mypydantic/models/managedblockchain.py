# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessorSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["BILLING_TOKEN"]] = Field(default=None, alias="Type")
    status: Optional[Literal["AVAILABLE", "DELETED", "PENDING_DELETION"]] = Field(
        default=None, alias="Status"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    arn: Optional[str] = Field(default=None, alias="Arn")


class AccessorModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    type: Optional[Literal["BILLING_TOKEN"]] = Field(default=None, alias="Type")
    billing_token: Optional[str] = Field(default=None, alias="BillingToken")
    status: Optional[Literal["AVAILABLE", "DELETED", "PENDING_DELETION"]] = Field(
        default=None, alias="Status"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    arn: Optional[str] = Field(default=None, alias="Arn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ApprovalThresholdPolicyModel(BaseModel):
    threshold_percentage: Optional[int] = Field(
        default=None, alias="ThresholdPercentage"
    )
    proposal_duration_in_hours: Optional[int] = Field(
        default=None, alias="ProposalDurationInHours"
    )
    threshold_comparator: Optional[
        Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"]
    ] = Field(default=None, alias="ThresholdComparator")


class CreateAccessorInputRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    accessor_type: Literal["BILLING_TOKEN"] = Field(alias="AccessorType")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteAccessorInputRequestModel(BaseModel):
    accessor_id: str = Field(alias="AccessorId")


class DeleteMemberInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    member_id: str = Field(alias="MemberId")


class DeleteNodeInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    node_id: str = Field(alias="NodeId")
    member_id: Optional[str] = Field(default=None, alias="MemberId")


class GetAccessorInputRequestModel(BaseModel):
    accessor_id: str = Field(alias="AccessorId")


class GetMemberInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    member_id: str = Field(alias="MemberId")


class GetNetworkInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")


class GetNodeInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    node_id: str = Field(alias="NodeId")
    member_id: Optional[str] = Field(default=None, alias="MemberId")


class GetProposalInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    proposal_id: str = Field(alias="ProposalId")


class NetworkSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    framework: Optional[Literal["ETHEREUM", "HYPERLEDGER_FABRIC"]] = Field(
        default=None, alias="Framework"
    )
    framework_version: Optional[str] = Field(default=None, alias="FrameworkVersion")
    status: Optional[
        Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING"]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    arn: Optional[str] = Field(default=None, alias="Arn")


class InviteActionModel(BaseModel):
    principal: str = Field(alias="Principal")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccessorsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInvitationsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListMembersInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_KEY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    is_owned: Optional[bool] = Field(default=None, alias="IsOwned")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class MemberSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_KEY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    is_owned: Optional[bool] = Field(default=None, alias="IsOwned")
    arn: Optional[str] = Field(default=None, alias="Arn")


class ListNetworksInputRequestModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    framework: Optional[Literal["ETHEREUM", "HYPERLEDGER_FABRIC"]] = Field(
        default=None, alias="Framework"
    )
    status: Optional[
        Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING"]
    ] = Field(default=None, alias="Status")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListNodesInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "FAILED",
            "INACCESSIBLE_ENCRYPTION_KEY",
            "UNHEALTHY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NodeSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "FAILED",
            "INACCESSIBLE_ENCRYPTION_KEY",
            "UNHEALTHY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    arn: Optional[str] = Field(default=None, alias="Arn")


class ListProposalVotesInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    proposal_id: str = Field(alias="ProposalId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class VoteSummaryModel(BaseModel):
    vote: Optional[Literal["NO", "YES"]] = Field(default=None, alias="Vote")
    member_name: Optional[str] = Field(default=None, alias="MemberName")
    member_id: Optional[str] = Field(default=None, alias="MemberId")


class ListProposalsInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ProposalSummaryModel(BaseModel):
    proposal_id: Optional[str] = Field(default=None, alias="ProposalId")
    description: Optional[str] = Field(default=None, alias="Description")
    proposed_by_member_id: Optional[str] = Field(
        default=None, alias="ProposedByMemberId"
    )
    proposed_by_member_name: Optional[str] = Field(
        default=None, alias="ProposedByMemberName"
    )
    status: Optional[
        Literal["ACTION_FAILED", "APPROVED", "EXPIRED", "IN_PROGRESS", "REJECTED"]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    expiration_date: Optional[datetime] = Field(default=None, alias="ExpirationDate")
    arn: Optional[str] = Field(default=None, alias="Arn")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class LogConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class MemberFabricAttributesModel(BaseModel):
    admin_username: Optional[str] = Field(default=None, alias="AdminUsername")
    ca_endpoint: Optional[str] = Field(default=None, alias="CaEndpoint")


class MemberFabricConfigurationModel(BaseModel):
    admin_username: str = Field(alias="AdminUsername")
    admin_password: str = Field(alias="AdminPassword")


class NetworkEthereumAttributesModel(BaseModel):
    chain_id: Optional[str] = Field(default=None, alias="ChainId")


class NetworkFabricAttributesModel(BaseModel):
    ordering_service_endpoint: Optional[str] = Field(
        default=None, alias="OrderingServiceEndpoint"
    )
    edition: Optional[Literal["STANDARD", "STARTER"]] = Field(
        default=None, alias="Edition"
    )


class NetworkFabricConfigurationModel(BaseModel):
    edition: Literal["STANDARD", "STARTER"] = Field(alias="Edition")


class NodeEthereumAttributesModel(BaseModel):
    http_endpoint: Optional[str] = Field(default=None, alias="HttpEndpoint")
    web_socket_endpoint: Optional[str] = Field(default=None, alias="WebSocketEndpoint")


class NodeFabricAttributesModel(BaseModel):
    peer_endpoint: Optional[str] = Field(default=None, alias="PeerEndpoint")
    peer_event_endpoint: Optional[str] = Field(default=None, alias="PeerEventEndpoint")


class RemoveActionModel(BaseModel):
    member_id: str = Field(alias="MemberId")


class RejectInvitationInputRequestModel(BaseModel):
    invitation_id: str = Field(alias="InvitationId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class VoteOnProposalInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    proposal_id: str = Field(alias="ProposalId")
    voter_member_id: str = Field(alias="VoterMemberId")
    vote: Literal["NO", "YES"] = Field(alias="Vote")


class VotingPolicyModel(BaseModel):
    approval_threshold_policy: Optional[ApprovalThresholdPolicyModel] = Field(
        default=None, alias="ApprovalThresholdPolicy"
    )


class CreateAccessorOutputModel(BaseModel):
    accessor_id: str = Field(alias="AccessorId")
    billing_token: str = Field(alias="BillingToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMemberOutputModel(BaseModel):
    member_id: str = Field(alias="MemberId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNetworkOutputModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    member_id: str = Field(alias="MemberId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNodeOutputModel(BaseModel):
    node_id: str = Field(alias="NodeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProposalOutputModel(BaseModel):
    proposal_id: str = Field(alias="ProposalId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAccessorOutputModel(BaseModel):
    accessor: AccessorModel = Field(alias="Accessor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessorsOutputModel(BaseModel):
    accessors: List[AccessorSummaryModel] = Field(alias="Accessors")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InvitationModel(BaseModel):
    invitation_id: Optional[str] = Field(default=None, alias="InvitationId")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    expiration_date: Optional[datetime] = Field(default=None, alias="ExpirationDate")
    status: Optional[
        Literal["ACCEPTED", "ACCEPTING", "EXPIRED", "PENDING", "REJECTED"]
    ] = Field(default=None, alias="Status")
    network_summary: Optional[NetworkSummaryModel] = Field(
        default=None, alias="NetworkSummary"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")


class ListNetworksOutputModel(BaseModel):
    networks: List[NetworkSummaryModel] = Field(alias="Networks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccessorsInputListAccessorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMembersOutputModel(BaseModel):
    members: List[MemberSummaryModel] = Field(alias="Members")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNodesOutputModel(BaseModel):
    nodes: List[NodeSummaryModel] = Field(alias="Nodes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProposalVotesOutputModel(BaseModel):
    proposal_votes: List[VoteSummaryModel] = Field(alias="ProposalVotes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProposalsOutputModel(BaseModel):
    proposals: List[ProposalSummaryModel] = Field(alias="Proposals")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LogConfigurationsModel(BaseModel):
    cloudwatch: Optional[LogConfigurationModel] = Field(
        default=None, alias="Cloudwatch"
    )


class MemberFrameworkAttributesModel(BaseModel):
    fabric: Optional[MemberFabricAttributesModel] = Field(default=None, alias="Fabric")


class MemberFrameworkConfigurationModel(BaseModel):
    fabric: Optional[MemberFabricConfigurationModel] = Field(
        default=None, alias="Fabric"
    )


class NetworkFrameworkAttributesModel(BaseModel):
    fabric: Optional[NetworkFabricAttributesModel] = Field(default=None, alias="Fabric")
    ethereum: Optional[NetworkEthereumAttributesModel] = Field(
        default=None, alias="Ethereum"
    )


class NetworkFrameworkConfigurationModel(BaseModel):
    fabric: Optional[NetworkFabricConfigurationModel] = Field(
        default=None, alias="Fabric"
    )


class NodeFrameworkAttributesModel(BaseModel):
    fabric: Optional[NodeFabricAttributesModel] = Field(default=None, alias="Fabric")
    ethereum: Optional[NodeEthereumAttributesModel] = Field(
        default=None, alias="Ethereum"
    )


class ProposalActionsModel(BaseModel):
    invitations: Optional[Sequence[InviteActionModel]] = Field(
        default=None, alias="Invitations"
    )
    removals: Optional[Sequence[RemoveActionModel]] = Field(
        default=None, alias="Removals"
    )


class ListInvitationsOutputModel(BaseModel):
    invitations: List[InvitationModel] = Field(alias="Invitations")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MemberFabricLogPublishingConfigurationModel(BaseModel):
    ca_logs: Optional[LogConfigurationsModel] = Field(default=None, alias="CaLogs")


class NodeFabricLogPublishingConfigurationModel(BaseModel):
    chaincode_logs: Optional[LogConfigurationsModel] = Field(
        default=None, alias="ChaincodeLogs"
    )
    peer_logs: Optional[LogConfigurationsModel] = Field(default=None, alias="PeerLogs")


class NetworkModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    framework: Optional[Literal["ETHEREUM", "HYPERLEDGER_FABRIC"]] = Field(
        default=None, alias="Framework"
    )
    framework_version: Optional[str] = Field(default=None, alias="FrameworkVersion")
    framework_attributes: Optional[NetworkFrameworkAttributesModel] = Field(
        default=None, alias="FrameworkAttributes"
    )
    vpc_endpoint_service_name: Optional[str] = Field(
        default=None, alias="VpcEndpointServiceName"
    )
    voting_policy: Optional[VotingPolicyModel] = Field(
        default=None, alias="VotingPolicy"
    )
    status: Optional[
        Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING"]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    arn: Optional[str] = Field(default=None, alias="Arn")


class CreateProposalInputRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    network_id: str = Field(alias="NetworkId")
    member_id: str = Field(alias="MemberId")
    actions: ProposalActionsModel = Field(alias="Actions")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ProposalModel(BaseModel):
    proposal_id: Optional[str] = Field(default=None, alias="ProposalId")
    network_id: Optional[str] = Field(default=None, alias="NetworkId")
    description: Optional[str] = Field(default=None, alias="Description")
    actions: Optional[ProposalActionsModel] = Field(default=None, alias="Actions")
    proposed_by_member_id: Optional[str] = Field(
        default=None, alias="ProposedByMemberId"
    )
    proposed_by_member_name: Optional[str] = Field(
        default=None, alias="ProposedByMemberName"
    )
    status: Optional[
        Literal["ACTION_FAILED", "APPROVED", "EXPIRED", "IN_PROGRESS", "REJECTED"]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    expiration_date: Optional[datetime] = Field(default=None, alias="ExpirationDate")
    yes_vote_count: Optional[int] = Field(default=None, alias="YesVoteCount")
    no_vote_count: Optional[int] = Field(default=None, alias="NoVoteCount")
    outstanding_vote_count: Optional[int] = Field(
        default=None, alias="OutstandingVoteCount"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    arn: Optional[str] = Field(default=None, alias="Arn")


class MemberLogPublishingConfigurationModel(BaseModel):
    fabric: Optional[MemberFabricLogPublishingConfigurationModel] = Field(
        default=None, alias="Fabric"
    )


class NodeLogPublishingConfigurationModel(BaseModel):
    fabric: Optional[NodeFabricLogPublishingConfigurationModel] = Field(
        default=None, alias="Fabric"
    )


class GetNetworkOutputModel(BaseModel):
    network: NetworkModel = Field(alias="Network")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProposalOutputModel(BaseModel):
    proposal: ProposalModel = Field(alias="Proposal")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MemberConfigurationModel(BaseModel):
    name: str = Field(alias="Name")
    framework_configuration: MemberFrameworkConfigurationModel = Field(
        alias="FrameworkConfiguration"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    log_publishing_configuration: Optional[
        MemberLogPublishingConfigurationModel
    ] = Field(default=None, alias="LogPublishingConfiguration")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class MemberModel(BaseModel):
    network_id: Optional[str] = Field(default=None, alias="NetworkId")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    framework_attributes: Optional[MemberFrameworkAttributesModel] = Field(
        default=None, alias="FrameworkAttributes"
    )
    log_publishing_configuration: Optional[
        MemberLogPublishingConfigurationModel
    ] = Field(default=None, alias="LogPublishingConfiguration")
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "INACCESSIBLE_ENCRYPTION_KEY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    arn: Optional[str] = Field(default=None, alias="Arn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class UpdateMemberInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    member_id: str = Field(alias="MemberId")
    log_publishing_configuration: Optional[
        MemberLogPublishingConfigurationModel
    ] = Field(default=None, alias="LogPublishingConfiguration")


class NodeConfigurationModel(BaseModel):
    instance_type: str = Field(alias="InstanceType")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    log_publishing_configuration: Optional[NodeLogPublishingConfigurationModel] = Field(
        default=None, alias="LogPublishingConfiguration"
    )
    state_db: Optional[Literal["CouchDB", "LevelDB"]] = Field(
        default=None, alias="StateDB"
    )


class NodeModel(BaseModel):
    network_id: Optional[str] = Field(default=None, alias="NetworkId")
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    id: Optional[str] = Field(default=None, alias="Id")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    availability_zone: Optional[str] = Field(default=None, alias="AvailabilityZone")
    framework_attributes: Optional[NodeFrameworkAttributesModel] = Field(
        default=None, alias="FrameworkAttributes"
    )
    log_publishing_configuration: Optional[NodeLogPublishingConfigurationModel] = Field(
        default=None, alias="LogPublishingConfiguration"
    )
    state_db: Optional[Literal["CouchDB", "LevelDB"]] = Field(
        default=None, alias="StateDB"
    )
    status: Optional[
        Literal[
            "AVAILABLE",
            "CREATE_FAILED",
            "CREATING",
            "DELETED",
            "DELETING",
            "FAILED",
            "INACCESSIBLE_ENCRYPTION_KEY",
            "UNHEALTHY",
            "UPDATING",
        ]
    ] = Field(default=None, alias="Status")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    arn: Optional[str] = Field(default=None, alias="Arn")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class UpdateNodeInputRequestModel(BaseModel):
    network_id: str = Field(alias="NetworkId")
    node_id: str = Field(alias="NodeId")
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    log_publishing_configuration: Optional[NodeLogPublishingConfigurationModel] = Field(
        default=None, alias="LogPublishingConfiguration"
    )


class CreateMemberInputRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    invitation_id: str = Field(alias="InvitationId")
    network_id: str = Field(alias="NetworkId")
    member_configuration: MemberConfigurationModel = Field(alias="MemberConfiguration")


class CreateNetworkInputRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    name: str = Field(alias="Name")
    framework: Literal["ETHEREUM", "HYPERLEDGER_FABRIC"] = Field(alias="Framework")
    framework_version: str = Field(alias="FrameworkVersion")
    voting_policy: VotingPolicyModel = Field(alias="VotingPolicy")
    member_configuration: MemberConfigurationModel = Field(alias="MemberConfiguration")
    description: Optional[str] = Field(default=None, alias="Description")
    framework_configuration: Optional[NetworkFrameworkConfigurationModel] = Field(
        default=None, alias="FrameworkConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class GetMemberOutputModel(BaseModel):
    member: MemberModel = Field(alias="Member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNodeInputRequestModel(BaseModel):
    client_request_token: str = Field(alias="ClientRequestToken")
    network_id: str = Field(alias="NetworkId")
    node_configuration: NodeConfigurationModel = Field(alias="NodeConfiguration")
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class GetNodeOutputModel(BaseModel):
    node: NodeModel = Field(alias="Node")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
