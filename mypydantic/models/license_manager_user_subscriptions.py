# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActiveDirectoryIdentityProviderModel(BaseModel):
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FilterModel(BaseModel):
    attribute: Optional[str] = Field(default=None, alias="Attribute")
    operation: Optional[str] = Field(default=None, alias="Operation")
    value: Optional[str] = Field(default=None, alias="Value")


class SettingsModel(BaseModel):
    security_group_id: str = Field(alias="SecurityGroupId")
    subnets: List[str] = Field(alias="Subnets")


class InstanceSummaryModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    products: List[str] = Field(alias="Products")
    status: str = Field(alias="Status")
    last_status_check_date: Optional[str] = Field(
        default=None, alias="LastStatusCheckDate"
    )
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListIdentityProvidersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UpdateSettingsModel(BaseModel):
    add_subnets: Sequence[str] = Field(alias="AddSubnets")
    remove_subnets: Sequence[str] = Field(alias="RemoveSubnets")
    security_group_id: Optional[str] = Field(default=None, alias="SecurityGroupId")


class IdentityProviderModel(BaseModel):
    active_directory_identity_provider: Optional[
        ActiveDirectoryIdentityProviderModel
    ] = Field(default=None, alias="ActiveDirectoryIdentityProvider")


class ListInstancesRequestModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInstancesResponseModel(BaseModel):
    instance_summaries: List[InstanceSummaryModel] = Field(alias="InstanceSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityProvidersRequestListIdentityProvidersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstancesRequestListInstancesPaginateModel(BaseModel):
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class AssociateUserRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    instance_id: str = Field(alias="InstanceId")
    username: str = Field(alias="Username")
    domain: Optional[str] = Field(default=None, alias="Domain")


class DeregisterIdentityProviderRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")


class DisassociateUserRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    instance_id: str = Field(alias="InstanceId")
    username: str = Field(alias="Username")
    domain: Optional[str] = Field(default=None, alias="Domain")


class IdentityProviderSummaryModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    settings: SettingsModel = Field(alias="Settings")
    status: str = Field(alias="Status")
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")


class InstanceUserSummaryModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    instance_id: str = Field(alias="InstanceId")
    status: str = Field(alias="Status")
    username: str = Field(alias="Username")
    association_date: Optional[str] = Field(default=None, alias="AssociationDate")
    disassociation_date: Optional[str] = Field(default=None, alias="DisassociationDate")
    domain: Optional[str] = Field(default=None, alias="Domain")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")


class ListProductSubscriptionsRequestListProductSubscriptionsPaginateModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProductSubscriptionsRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListUserAssociationsRequestListUserAssociationsPaginateModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    instance_id: str = Field(alias="InstanceId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUserAssociationsRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    instance_id: str = Field(alias="InstanceId")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="Filters")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ProductUserSummaryModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    status: str = Field(alias="Status")
    username: str = Field(alias="Username")
    domain: Optional[str] = Field(default=None, alias="Domain")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    subscription_end_date: Optional[str] = Field(
        default=None, alias="SubscriptionEndDate"
    )
    subscription_start_date: Optional[str] = Field(
        default=None, alias="SubscriptionStartDate"
    )


class RegisterIdentityProviderRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    settings: Optional[SettingsModel] = Field(default=None, alias="Settings")


class StartProductSubscriptionRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    username: str = Field(alias="Username")
    domain: Optional[str] = Field(default=None, alias="Domain")


class StopProductSubscriptionRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    username: str = Field(alias="Username")
    domain: Optional[str] = Field(default=None, alias="Domain")


class UpdateIdentityProviderSettingsRequestModel(BaseModel):
    identity_provider: IdentityProviderModel = Field(alias="IdentityProvider")
    product: str = Field(alias="Product")
    update_settings: UpdateSettingsModel = Field(alias="UpdateSettings")


class DeregisterIdentityProviderResponseModel(BaseModel):
    identity_provider_summary: IdentityProviderSummaryModel = Field(
        alias="IdentityProviderSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityProvidersResponseModel(BaseModel):
    identity_provider_summaries: List[IdentityProviderSummaryModel] = Field(
        alias="IdentityProviderSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterIdentityProviderResponseModel(BaseModel):
    identity_provider_summary: IdentityProviderSummaryModel = Field(
        alias="IdentityProviderSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIdentityProviderSettingsResponseModel(BaseModel):
    identity_provider_summary: IdentityProviderSummaryModel = Field(
        alias="IdentityProviderSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateUserResponseModel(BaseModel):
    instance_user_summary: InstanceUserSummaryModel = Field(alias="InstanceUserSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateUserResponseModel(BaseModel):
    instance_user_summary: InstanceUserSummaryModel = Field(alias="InstanceUserSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserAssociationsResponseModel(BaseModel):
    instance_user_summaries: List[InstanceUserSummaryModel] = Field(
        alias="InstanceUserSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProductSubscriptionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    product_user_summaries: List[ProductUserSummaryModel] = Field(
        alias="ProductUserSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartProductSubscriptionResponseModel(BaseModel):
    product_user_summary: ProductUserSummaryModel = Field(alias="ProductUserSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopProductSubscriptionResponseModel(BaseModel):
    product_user_summary: ProductUserSummaryModel = Field(alias="ProductUserSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
