# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptResourceShareInvitationRequestModel(BaseModel):
    resource_share_invitation_arn: str = Field(alias="resourceShareInvitationArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateResourceSharePermissionRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    permission_arn: str = Field(alias="permissionArn")
    replace: Optional[bool] = Field(default=None, alias="replace")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    permission_version: Optional[int] = Field(default=None, alias="permissionVersion")


class AssociateResourceShareRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="resourceArns")
    principals: Optional[Sequence[str]] = Field(default=None, alias="principals")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ResourceShareAssociationModel(BaseModel):
    resource_share_arn: Optional[str] = Field(default=None, alias="resourceShareArn")
    resource_share_name: Optional[str] = Field(default=None, alias="resourceShareName")
    associated_entity: Optional[str] = Field(default=None, alias="associatedEntity")
    association_type: Optional[Literal["PRINCIPAL", "RESOURCE"]] = Field(
        default=None, alias="associationType"
    )
    status: Optional[
        Literal[
            "ASSOCIATED", "ASSOCIATING", "DISASSOCIATED", "DISASSOCIATING", "FAILED"
        ]
    ] = Field(default=None, alias="status")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    external: Optional[bool] = Field(default=None, alias="external")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class DeleteResourceShareRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DisassociateResourceSharePermissionRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    permission_arn: str = Field(alias="permissionArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DisassociateResourceShareRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="resourceArns")
    principals: Optional[Sequence[str]] = Field(default=None, alias="principals")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class GetPermissionRequestModel(BaseModel):
    permission_arn: str = Field(alias="permissionArn")
    permission_version: Optional[int] = Field(default=None, alias="permissionVersion")


class ResourceSharePermissionDetailModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    version: Optional[str] = Field(default=None, alias="version")
    default_version: Optional[bool] = Field(default=None, alias="defaultVersion")
    name: Optional[str] = Field(default=None, alias="name")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    permission: Optional[str] = Field(default=None, alias="permission")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    is_resource_type_default: Optional[bool] = Field(
        default=None, alias="isResourceModelault"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetResourcePoliciesRequestModel(BaseModel):
    resource_arns: Sequence[str] = Field(alias="resourceArns")
    principal: Optional[str] = Field(default=None, alias="principal")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetResourceShareAssociationsRequestModel(BaseModel):
    association_type: Literal["PRINCIPAL", "RESOURCE"] = Field(alias="associationType")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    principal: Optional[str] = Field(default=None, alias="principal")
    association_status: Optional[
        Literal[
            "ASSOCIATED", "ASSOCIATING", "DISASSOCIATED", "DISASSOCIATING", "FAILED"
        ]
    ] = Field(default=None, alias="associationStatus")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class GetResourceShareInvitationsRequestModel(BaseModel):
    resource_share_invitation_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareInvitationArns"
    )
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class TagFilterModel(BaseModel):
    tag_key: Optional[str] = Field(default=None, alias="tagKey")
    tag_values: Optional[Sequence[str]] = Field(default=None, alias="tagValues")


class ListPendingInvitationResourcesRequestModel(BaseModel):
    resource_share_invitation_arn: str = Field(alias="resourceShareInvitationArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    resource_region_scope: Optional[Literal["ALL", "GLOBAL", "REGIONAL"]] = Field(
        default=None, alias="resourceRegionScope"
    )


class ResourceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    type: Optional[str] = Field(default=None, alias="type")
    resource_share_arn: Optional[str] = Field(default=None, alias="resourceShareArn")
    resource_group_arn: Optional[str] = Field(default=None, alias="resourceGroupArn")
    status: Optional[
        Literal[
            "AVAILABLE",
            "LIMIT_EXCEEDED",
            "PENDING",
            "UNAVAILABLE",
            "ZONAL_RESOURCE_INACCESSIBLE",
        ]
    ] = Field(default=None, alias="status")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    resource_region_scope: Optional[Literal["GLOBAL", "REGIONAL"]] = Field(
        default=None, alias="resourceRegionScope"
    )


class ListPermissionVersionsRequestModel(BaseModel):
    permission_arn: str = Field(alias="permissionArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ResourceSharePermissionSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    version: Optional[str] = Field(default=None, alias="version")
    default_version: Optional[bool] = Field(default=None, alias="defaultVersion")
    name: Optional[str] = Field(default=None, alias="name")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    status: Optional[str] = Field(default=None, alias="status")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    is_resource_type_default: Optional[bool] = Field(
        default=None, alias="isResourceModelault"
    )


class ListPermissionsRequestModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListPrincipalsRequestModel(BaseModel):
    resource_owner: Literal["OTHER-ACCOUNTS", "SELF"] = Field(alias="resourceOwner")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    principals: Optional[Sequence[str]] = Field(default=None, alias="principals")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class PrincipalModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    resource_share_arn: Optional[str] = Field(default=None, alias="resourceShareArn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    external: Optional[bool] = Field(default=None, alias="external")


class ListResourceSharePermissionsRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListResourceTypesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    resource_region_scope: Optional[Literal["ALL", "GLOBAL", "REGIONAL"]] = Field(
        default=None, alias="resourceRegionScope"
    )


class ServiceNameAndResourceTypeModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    service_name: Optional[str] = Field(default=None, alias="serviceName")
    resource_region_scope: Optional[Literal["GLOBAL", "REGIONAL"]] = Field(
        default=None, alias="resourceRegionScope"
    )


class ListResourcesRequestModel(BaseModel):
    resource_owner: Literal["OTHER-ACCOUNTS", "SELF"] = Field(alias="resourceOwner")
    principal: Optional[str] = Field(default=None, alias="principal")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="resourceArns")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    resource_region_scope: Optional[Literal["ALL", "GLOBAL", "REGIONAL"]] = Field(
        default=None, alias="resourceRegionScope"
    )


class PromoteResourceShareCreatedFromPolicyRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")


class RejectResourceShareInvitationRequestModel(BaseModel):
    resource_share_invitation_arn: str = Field(alias="resourceShareInvitationArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UntagResourceRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateResourceShareRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    name: Optional[str] = Field(default=None, alias="name")
    allow_external_principals: Optional[bool] = Field(
        default=None, alias="allowExternalPrincipals"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class AssociateResourceSharePermissionResponseModel(BaseModel):
    return_value: bool = Field(alias="returnValue")
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResourceShareResponseModel(BaseModel):
    return_value: bool = Field(alias="returnValue")
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateResourceSharePermissionResponseModel(BaseModel):
    return_value: bool = Field(alias="returnValue")
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableSharingWithAwsOrganizationResponseModel(BaseModel):
    return_value: bool = Field(alias="returnValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePoliciesResponseModel(BaseModel):
    policies: List[str] = Field(alias="policies")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PromoteResourceShareCreatedFromPolicyResponseModel(BaseModel):
    return_value: bool = Field(alias="returnValue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateResourceShareResponseModel(BaseModel):
    resource_share_associations: List[ResourceShareAssociationModel] = Field(
        alias="resourceShareAssociations"
    )
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateResourceShareResponseModel(BaseModel):
    resource_share_associations: List[ResourceShareAssociationModel] = Field(
        alias="resourceShareAssociations"
    )
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceShareAssociationsResponseModel(BaseModel):
    resource_share_associations: List[ResourceShareAssociationModel] = Field(
        alias="resourceShareAssociations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceShareInvitationModel(BaseModel):
    resource_share_invitation_arn: Optional[str] = Field(
        default=None, alias="resourceShareInvitationArn"
    )
    resource_share_name: Optional[str] = Field(default=None, alias="resourceShareName")
    resource_share_arn: Optional[str] = Field(default=None, alias="resourceShareArn")
    sender_account_id: Optional[str] = Field(default=None, alias="senderAccountId")
    receiver_account_id: Optional[str] = Field(default=None, alias="receiverAccountId")
    invitation_timestamp: Optional[datetime] = Field(
        default=None, alias="invitationTimestamp"
    )
    status: Optional[Literal["ACCEPTED", "EXPIRED", "PENDING", "REJECTED"]] = Field(
        default=None, alias="status"
    )
    resource_share_associations: Optional[List[ResourceShareAssociationModel]] = Field(
        default=None, alias="resourceShareAssociations"
    )
    receiver_arn: Optional[str] = Field(default=None, alias="receiverArn")


class CreateResourceShareRequestModel(BaseModel):
    name: str = Field(alias="name")
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="resourceArns")
    principals: Optional[Sequence[str]] = Field(default=None, alias="principals")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    allow_external_principals: Optional[bool] = Field(
        default=None, alias="allowExternalPrincipals"
    )
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    permission_arns: Optional[Sequence[str]] = Field(
        default=None, alias="permissionArns"
    )


class ResourceShareModel(BaseModel):
    resource_share_arn: Optional[str] = Field(default=None, alias="resourceShareArn")
    name: Optional[str] = Field(default=None, alias="name")
    owning_account_id: Optional[str] = Field(default=None, alias="owningAccountId")
    allow_external_principals: Optional[bool] = Field(
        default=None, alias="allowExternalPrincipals"
    )
    status: Optional[
        Literal["ACTIVE", "DELETED", "DELETING", "FAILED", "PENDING"]
    ] = Field(default=None, alias="status")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    tags: Optional[List[TagModel]] = Field(default=None, alias="tags")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="lastUpdatedTime")
    feature_set: Optional[
        Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"]
    ] = Field(default=None, alias="featureSet")


class TagResourceRequestModel(BaseModel):
    resource_share_arn: str = Field(alias="resourceShareArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class GetPermissionResponseModel(BaseModel):
    permission: ResourceSharePermissionDetailModel = Field(alias="permission")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourcePoliciesRequestGetResourcePoliciesPaginateModel(BaseModel):
    resource_arns: Sequence[str] = Field(alias="resourceArns")
    principal: Optional[str] = Field(default=None, alias="principal")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourceShareAssociationsRequestGetResourceShareAssociationsPaginateModel(
    BaseModel
):
    association_type: Literal["PRINCIPAL", "RESOURCE"] = Field(alias="associationType")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    principal: Optional[str] = Field(default=None, alias="principal")
    association_status: Optional[
        Literal[
            "ASSOCIATED", "ASSOCIATING", "DISASSOCIATED", "DISASSOCIATING", "FAILED"
        ]
    ] = Field(default=None, alias="associationStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourceShareInvitationsRequestGetResourceShareInvitationsPaginateModel(
    BaseModel
):
    resource_share_invitation_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareInvitationArns"
    )
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPrincipalsRequestListPrincipalsPaginateModel(BaseModel):
    resource_owner: Literal["OTHER-ACCOUNTS", "SELF"] = Field(alias="resourceOwner")
    resource_arn: Optional[str] = Field(default=None, alias="resourceArn")
    principals: Optional[Sequence[str]] = Field(default=None, alias="principals")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourcesRequestListResourcesPaginateModel(BaseModel):
    resource_owner: Literal["OTHER-ACCOUNTS", "SELF"] = Field(alias="resourceOwner")
    principal: Optional[str] = Field(default=None, alias="principal")
    resource_type: Optional[str] = Field(default=None, alias="resourceType")
    resource_arns: Optional[Sequence[str]] = Field(default=None, alias="resourceArns")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    resource_region_scope: Optional[Literal["ALL", "GLOBAL", "REGIONAL"]] = Field(
        default=None, alias="resourceRegionScope"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourceSharesRequestGetResourceSharesPaginateModel(BaseModel):
    resource_owner: Literal["OTHER-ACCOUNTS", "SELF"] = Field(alias="resourceOwner")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    resource_share_status: Optional[
        Literal["ACTIVE", "DELETED", "DELETING", "FAILED", "PENDING"]
    ] = Field(default=None, alias="resourceShareStatus")
    name: Optional[str] = Field(default=None, alias="name")
    tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="tagFilters"
    )
    permission_arn: Optional[str] = Field(default=None, alias="permissionArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourceSharesRequestModel(BaseModel):
    resource_owner: Literal["OTHER-ACCOUNTS", "SELF"] = Field(alias="resourceOwner")
    resource_share_arns: Optional[Sequence[str]] = Field(
        default=None, alias="resourceShareArns"
    )
    resource_share_status: Optional[
        Literal["ACTIVE", "DELETED", "DELETING", "FAILED", "PENDING"]
    ] = Field(default=None, alias="resourceShareStatus")
    name: Optional[str] = Field(default=None, alias="name")
    tag_filters: Optional[Sequence[TagFilterModel]] = Field(
        default=None, alias="tagFilters"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    permission_arn: Optional[str] = Field(default=None, alias="permissionArn")


class ListPendingInvitationResourcesResponseModel(BaseModel):
    resources: List[ResourceModel] = Field(alias="resources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesResponseModel(BaseModel):
    resources: List[ResourceModel] = Field(alias="resources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPermissionVersionsResponseModel(BaseModel):
    permissions: List[ResourceSharePermissionSummaryModel] = Field(alias="permissions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPermissionsResponseModel(BaseModel):
    permissions: List[ResourceSharePermissionSummaryModel] = Field(alias="permissions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceSharePermissionsResponseModel(BaseModel):
    permissions: List[ResourceSharePermissionSummaryModel] = Field(alias="permissions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPrincipalsResponseModel(BaseModel):
    principals: List[PrincipalModel] = Field(alias="principals")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceTypesResponseModel(BaseModel):
    resource_types: List[ServiceNameAndResourceTypeModel] = Field(alias="resourceTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AcceptResourceShareInvitationResponseModel(BaseModel):
    resource_share_invitation: ResourceShareInvitationModel = Field(
        alias="resourceShareInvitation"
    )
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceShareInvitationsResponseModel(BaseModel):
    resource_share_invitations: List[ResourceShareInvitationModel] = Field(
        alias="resourceShareInvitations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RejectResourceShareInvitationResponseModel(BaseModel):
    resource_share_invitation: ResourceShareInvitationModel = Field(
        alias="resourceShareInvitation"
    )
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourceShareResponseModel(BaseModel):
    resource_share: ResourceShareModel = Field(alias="resourceShare")
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceSharesResponseModel(BaseModel):
    resource_shares: List[ResourceShareModel] = Field(alias="resourceShares")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResourceShareResponseModel(BaseModel):
    resource_share: ResourceShareModel = Field(alias="resourceShare")
    client_token: str = Field(alias="clientToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
