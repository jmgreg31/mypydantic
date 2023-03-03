# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddressModel(BaseModel):
    street_address: Optional[str] = Field(default=None, alias="StreetAddress")
    locality: Optional[str] = Field(default=None, alias="Locality")
    region: Optional[str] = Field(default=None, alias="Region")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")
    country: Optional[str] = Field(default=None, alias="Country")
    formatted: Optional[str] = Field(default=None, alias="Formatted")
    type: Optional[str] = Field(default=None, alias="Type")
    primary: Optional[bool] = Field(default=None, alias="Primary")


class ExternalIdModel(BaseModel):
    issuer: str = Field(alias="Issuer")
    id: str = Field(alias="Id")


class UniqueAttributeModel(BaseModel):
    attribute_path: str = Field(alias="AttributePath")
    attribute_value: Mapping[str, Any] = Field(alias="AttributeValue")


class AttributeOperationModel(BaseModel):
    attribute_path: str = Field(alias="AttributePath")
    attribute_value: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AttributeValue"
    )


class MemberIdModel(BaseModel):
    user_id: Optional[str] = Field(default=None, alias="UserId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateGroupRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")


class EmailModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    type: Optional[str] = Field(default=None, alias="Type")
    primary: Optional[bool] = Field(default=None, alias="Primary")


class NameModel(BaseModel):
    formatted: Optional[str] = Field(default=None, alias="Formatted")
    family_name: Optional[str] = Field(default=None, alias="FamilyName")
    given_name: Optional[str] = Field(default=None, alias="GivenName")
    middle_name: Optional[str] = Field(default=None, alias="MiddleName")
    honorific_prefix: Optional[str] = Field(default=None, alias="HonorificPrefix")
    honorific_suffix: Optional[str] = Field(default=None, alias="HonorificSuffix")


class PhoneNumberModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="Value")
    type: Optional[str] = Field(default=None, alias="Type")
    primary: Optional[bool] = Field(default=None, alias="Primary")


class DeleteGroupMembershipRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    membership_id: str = Field(alias="MembershipId")


class DeleteGroupRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    group_id: str = Field(alias="GroupId")


class DeleteUserRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    user_id: str = Field(alias="UserId")


class DescribeGroupMembershipRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    membership_id: str = Field(alias="MembershipId")


class DescribeGroupRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    group_id: str = Field(alias="GroupId")


class DescribeUserRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    user_id: str = Field(alias="UserId")


class FilterModel(BaseModel):
    attribute_path: str = Field(alias="AttributePath")
    attribute_value: str = Field(alias="AttributeValue")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListGroupMembershipsRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    group_id: str = Field(alias="GroupId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GroupModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    external_ids: Optional[List[ExternalIdModel]] = Field(
        default=None, alias="ExternalIds"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class AlternateIdentifierModel(BaseModel):
    external_id: Optional[ExternalIdModel] = Field(default=None, alias="ExternalId")
    unique_attribute: Optional[UniqueAttributeModel] = Field(
        default=None, alias="UniqueAttribute"
    )


class UpdateGroupRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    group_id: str = Field(alias="GroupId")
    operations: Sequence[AttributeOperationModel] = Field(alias="Operations")


class UpdateUserRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    user_id: str = Field(alias="UserId")
    operations: Sequence[AttributeOperationModel] = Field(alias="Operations")


class CreateGroupMembershipRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    group_id: str = Field(alias="GroupId")
    member_id: MemberIdModel = Field(alias="MemberId")


class GetGroupMembershipIdRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    group_id: str = Field(alias="GroupId")
    member_id: MemberIdModel = Field(alias="MemberId")


class GroupMembershipExistenceResultModel(BaseModel):
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    member_id: Optional[MemberIdModel] = Field(default=None, alias="MemberId")
    membership_exists: Optional[bool] = Field(default=None, alias="MembershipExists")


class GroupMembershipModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    membership_id: Optional[str] = Field(default=None, alias="MembershipId")
    group_id: Optional[str] = Field(default=None, alias="GroupId")
    member_id: Optional[MemberIdModel] = Field(default=None, alias="MemberId")


class IsMemberInGroupsRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    member_id: MemberIdModel = Field(alias="MemberId")
    group_ids: Sequence[str] = Field(alias="GroupIds")


class ListGroupMembershipsForMemberRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    member_id: MemberIdModel = Field(alias="MemberId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CreateGroupMembershipResponseModel(BaseModel):
    membership_id: str = Field(alias="MembershipId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupResponseModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    user_id: str = Field(alias="UserId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGroupMembershipResponseModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    membership_id: str = Field(alias="MembershipId")
    group_id: str = Field(alias="GroupId")
    member_id: MemberIdModel = Field(alias="MemberId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGroupResponseModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    display_name: str = Field(alias="DisplayName")
    external_ids: List[ExternalIdModel] = Field(alias="ExternalIds")
    description: str = Field(alias="Description")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupIdResponseModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupMembershipIdResponseModel(BaseModel):
    membership_id: str = Field(alias="MembershipId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUserIdResponseModel(BaseModel):
    user_id: str = Field(alias="UserId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    name: Optional[NameModel] = Field(default=None, alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    nick_name: Optional[str] = Field(default=None, alias="NickName")
    profile_url: Optional[str] = Field(default=None, alias="ProfileUrl")
    emails: Optional[Sequence[EmailModel]] = Field(default=None, alias="Emails")
    addresses: Optional[Sequence[AddressModel]] = Field(default=None, alias="Addresses")
    phone_numbers: Optional[Sequence[PhoneNumberModel]] = Field(
        default=None, alias="PhoneNumbers"
    )
    user_type: Optional[str] = Field(default=None, alias="UserType")
    title: Optional[str] = Field(default=None, alias="Title")
    preferred_language: Optional[str] = Field(default=None, alias="PreferredLanguage")
    locale: Optional[str] = Field(default=None, alias="Locale")
    timezone: Optional[str] = Field(default=None, alias="Timezone")


class DescribeUserResponseModel(BaseModel):
    user_name: str = Field(alias="UserName")
    user_id: str = Field(alias="UserId")
    external_ids: List[ExternalIdModel] = Field(alias="ExternalIds")
    name: NameModel = Field(alias="Name")
    display_name: str = Field(alias="DisplayName")
    nick_name: str = Field(alias="NickName")
    profile_url: str = Field(alias="ProfileUrl")
    emails: List[EmailModel] = Field(alias="Emails")
    addresses: List[AddressModel] = Field(alias="Addresses")
    phone_numbers: List[PhoneNumberModel] = Field(alias="PhoneNumbers")
    user_type: str = Field(alias="UserType")
    title: str = Field(alias="Title")
    preferred_language: str = Field(alias="PreferredLanguage")
    locale: str = Field(alias="Locale")
    timezone: str = Field(alias="Timezone")
    identity_store_id: str = Field(alias="IdentityStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserModel(BaseModel):
    user_id: str = Field(alias="UserId")
    identity_store_id: str = Field(alias="IdentityStoreId")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    external_ids: Optional[List[ExternalIdModel]] = Field(
        default=None, alias="ExternalIds"
    )
    name: Optional[NameModel] = Field(default=None, alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    nick_name: Optional[str] = Field(default=None, alias="NickName")
    profile_url: Optional[str] = Field(default=None, alias="ProfileUrl")
    emails: Optional[List[EmailModel]] = Field(default=None, alias="Emails")
    addresses: Optional[List[AddressModel]] = Field(default=None, alias="Addresses")
    phone_numbers: Optional[List[PhoneNumberModel]] = Field(
        default=None, alias="PhoneNumbers"
    )
    user_type: Optional[str] = Field(default=None, alias="UserType")
    title: Optional[str] = Field(default=None, alias="Title")
    preferred_language: Optional[str] = Field(default=None, alias="PreferredLanguage")
    locale: Optional[str] = Field(default=None, alias="Locale")
    timezone: Optional[str] = Field(default=None, alias="Timezone")


class ListGroupsRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListUsersRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")


class ListGroupMembershipsForMemberRequestListGroupMembershipsForMemberPaginateModel(
    BaseModel
):
    identity_store_id: str = Field(alias="IdentityStoreId")
    member_id: MemberIdModel = Field(alias="MemberId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupMembershipsRequestListGroupMembershipsPaginateModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    group_id: str = Field(alias="GroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupsRequestListGroupsPaginateModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupsResponseModel(BaseModel):
    groups: List[GroupModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupIdRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    alternate_identifier: AlternateIdentifierModel = Field(alias="AlternateIdentifier")


class GetUserIdRequestModel(BaseModel):
    identity_store_id: str = Field(alias="IdentityStoreId")
    alternate_identifier: AlternateIdentifierModel = Field(alias="AlternateIdentifier")


class IsMemberInGroupsResponseModel(BaseModel):
    results: List[GroupMembershipExistenceResultModel] = Field(alias="Results")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupMembershipsForMemberResponseModel(BaseModel):
    group_memberships: List[GroupMembershipModel] = Field(alias="GroupMemberships")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupMembershipsResponseModel(BaseModel):
    group_memberships: List[GroupMembershipModel] = Field(alias="GroupMemberships")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
