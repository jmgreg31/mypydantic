# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessControlAttributeValueModel(BaseModel):
    source: Sequence[str] = Field(alias="Source")


class AccountAssignmentOperationStatusMetadataModel(BaseModel):
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")


class AccountAssignmentOperationStatusModel(BaseModel):
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    target_id: Optional[str] = Field(default=None, alias="TargetId")
    target_type: Optional[Literal["AWS_ACCOUNT"]] = Field(
        default=None, alias="TargetType"
    )
    permission_set_arn: Optional[str] = Field(default=None, alias="PermissionSetArn")
    principal_type: Optional[Literal["GROUP", "USER"]] = Field(
        default=None, alias="PrincipalType"
    )
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")


class AccountAssignmentModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    permission_set_arn: Optional[str] = Field(default=None, alias="PermissionSetArn")
    principal_type: Optional[Literal["GROUP", "USER"]] = Field(
        default=None, alias="PrincipalType"
    )
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")


class CustomerManagedPolicyReferenceModel(BaseModel):
    name: str = Field(alias="Name")
    path: Optional[str] = Field(default=None, alias="Path")


class AttachManagedPolicyToPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    managed_policy_arn: str = Field(alias="ManagedPolicyArn")


class AttachedManagedPolicyModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")


class CreateAccountAssignmentRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    target_id: str = Field(alias="TargetId")
    target_type: Literal["AWS_ACCOUNT"] = Field(alias="TargetType")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    principal_type: Literal["GROUP", "USER"] = Field(alias="PrincipalType")
    principal_id: str = Field(alias="PrincipalId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class PermissionSetModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    permission_set_arn: Optional[str] = Field(default=None, alias="PermissionSetArn")
    description: Optional[str] = Field(default=None, alias="Description")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    session_duration: Optional[str] = Field(default=None, alias="SessionDuration")
    relay_state: Optional[str] = Field(default=None, alias="RelayState")


class DeleteAccountAssignmentRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    target_id: str = Field(alias="TargetId")
    target_type: Literal["AWS_ACCOUNT"] = Field(alias="TargetType")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    principal_type: Literal["GROUP", "USER"] = Field(alias="PrincipalType")
    principal_id: str = Field(alias="PrincipalId")


class DeleteInlinePolicyFromPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")


class DeleteInstanceAccessControlAttributeConfigurationRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")


class DeletePermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")


class DeletePermissionsBoundaryFromPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")


class DescribeAccountAssignmentCreationStatusRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    account_assignment_creation_request_id: str = Field(
        alias="AccountAssignmentCreationRequestId"
    )


class DescribeAccountAssignmentDeletionStatusRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    account_assignment_deletion_request_id: str = Field(
        alias="AccountAssignmentDeletionRequestId"
    )


class DescribeInstanceAccessControlAttributeConfigurationRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")


class DescribePermissionSetProvisioningStatusRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    provision_permission_set_request_id: str = Field(
        alias="ProvisionPermissionSetRequestId"
    )


class PermissionSetProvisioningStatusModel(BaseModel):
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    permission_set_arn: Optional[str] = Field(default=None, alias="PermissionSetArn")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")


class DescribePermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")


class DetachManagedPolicyFromPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    managed_policy_arn: str = Field(alias="ManagedPolicyArn")


class GetInlinePolicyForPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")


class GetPermissionsBoundaryForPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")


class InstanceMetadataModel(BaseModel):
    instance_arn: Optional[str] = Field(default=None, alias="InstanceArn")
    identity_store_id: Optional[str] = Field(default=None, alias="IdentityStoreId")


class OperationStatusFilterModel(BaseModel):
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccountAssignmentsRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    account_id: str = Field(alias="AccountId")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAccountsForProvisionedPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    provisioning_status: Optional[
        Literal[
            "LATEST_PERMISSION_SET_NOT_PROVISIONED", "LATEST_PERMISSION_SET_PROVISIONED"
        ]
    ] = Field(default=None, alias="ProvisioningStatus")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCustomerManagedPolicyReferencesInPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListInstancesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListManagedPoliciesInPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PermissionSetProvisioningStatusMetadataModel(BaseModel):
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]] = Field(
        default=None, alias="Status"
    )
    request_id: Optional[str] = Field(default=None, alias="RequestId")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")


class ListPermissionSetsProvisionedToAccountRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    account_id: str = Field(alias="AccountId")
    provisioning_status: Optional[
        Literal[
            "LATEST_PERMISSION_SET_NOT_PROVISIONED", "LATEST_PERMISSION_SET_PROVISIONED"
        ]
    ] = Field(default=None, alias="ProvisioningStatus")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListPermissionSetsRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ProvisionPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    target_type: Literal["ALL_PROVISIONED_ACCOUNTS", "AWS_ACCOUNT"] = Field(
        alias="TargetType"
    )
    target_id: Optional[str] = Field(default=None, alias="TargetId")


class PutInlinePolicyToPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    inline_policy: str = Field(alias="InlinePolicy")


class UntagResourceRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdatePermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    description: Optional[str] = Field(default=None, alias="Description")
    session_duration: Optional[str] = Field(default=None, alias="SessionDuration")
    relay_state: Optional[str] = Field(default=None, alias="RelayState")


class AccessControlAttributeModel(BaseModel):
    key: str = Field(alias="Key")
    value: AccessControlAttributeValueModel = Field(alias="Value")


class AttachCustomerManagedPolicyReferenceToPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    customer_managed_policy_reference: CustomerManagedPolicyReferenceModel = Field(
        alias="CustomerManagedPolicyReference"
    )


class DetachCustomerManagedPolicyReferenceFromPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    customer_managed_policy_reference: CustomerManagedPolicyReferenceModel = Field(
        alias="CustomerManagedPolicyReference"
    )


class PermissionsBoundaryModel(BaseModel):
    customer_managed_policy_reference: Optional[
        CustomerManagedPolicyReferenceModel
    ] = Field(default=None, alias="CustomerManagedPolicyReference")
    managed_policy_arn: Optional[str] = Field(default=None, alias="ManagedPolicyArn")


class CreateAccountAssignmentResponseModel(BaseModel):
    account_assignment_creation_status: AccountAssignmentOperationStatusModel = Field(
        alias="AccountAssignmentCreationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAccountAssignmentResponseModel(BaseModel):
    account_assignment_deletion_status: AccountAssignmentOperationStatusModel = Field(
        alias="AccountAssignmentDeletionStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountAssignmentCreationStatusResponseModel(BaseModel):
    account_assignment_creation_status: AccountAssignmentOperationStatusModel = Field(
        alias="AccountAssignmentCreationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountAssignmentDeletionStatusResponseModel(BaseModel):
    account_assignment_deletion_status: AccountAssignmentOperationStatusModel = Field(
        alias="AccountAssignmentDeletionStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetInlinePolicyForPermissionSetResponseModel(BaseModel):
    inline_policy: str = Field(alias="InlinePolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountAssignmentCreationStatusResponseModel(BaseModel):
    account_assignments_creation_status: List[
        AccountAssignmentOperationStatusMetadataModel
    ] = Field(alias="AccountAssignmentsCreationStatus")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountAssignmentDeletionStatusResponseModel(BaseModel):
    account_assignments_deletion_status: List[
        AccountAssignmentOperationStatusMetadataModel
    ] = Field(alias="AccountAssignmentsDeletionStatus")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountAssignmentsResponseModel(BaseModel):
    account_assignments: List[AccountAssignmentModel] = Field(
        alias="AccountAssignments"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountsForProvisionedPermissionSetResponseModel(BaseModel):
    account_ids: List[str] = Field(alias="AccountIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomerManagedPolicyReferencesInPermissionSetResponseModel(BaseModel):
    customer_managed_policy_references: List[
        CustomerManagedPolicyReferenceModel
    ] = Field(alias="CustomerManagedPolicyReferences")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListManagedPoliciesInPermissionSetResponseModel(BaseModel):
    attached_managed_policies: List[AttachedManagedPolicyModel] = Field(
        alias="AttachedManagedPolicies"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPermissionSetsProvisionedToAccountResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    permission_sets: List[str] = Field(alias="PermissionSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPermissionSetsResponseModel(BaseModel):
    permission_sets: List[str] = Field(alias="PermissionSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePermissionSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    instance_arn: str = Field(alias="InstanceArn")
    description: Optional[str] = Field(default=None, alias="Description")
    session_duration: Optional[str] = Field(default=None, alias="SessionDuration")
    relay_state: Optional[str] = Field(default=None, alias="RelayState")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreatePermissionSetResponseModel(BaseModel):
    permission_set: PermissionSetModel = Field(alias="PermissionSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePermissionSetResponseModel(BaseModel):
    permission_set: PermissionSetModel = Field(alias="PermissionSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePermissionSetProvisioningStatusResponseModel(BaseModel):
    permission_set_provisioning_status: PermissionSetProvisioningStatusModel = Field(
        alias="PermissionSetProvisioningStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProvisionPermissionSetResponseModel(BaseModel):
    permission_set_provisioning_status: PermissionSetProvisioningStatusModel = Field(
        alias="PermissionSetProvisioningStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstancesResponseModel(BaseModel):
    instances: List[InstanceMetadataModel] = Field(alias="Instances")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountAssignmentCreationStatusRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filter: Optional[OperationStatusFilterModel] = Field(default=None, alias="Filter")


class ListAccountAssignmentDeletionStatusRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filter: Optional[OperationStatusFilterModel] = Field(default=None, alias="Filter")


class ListPermissionSetProvisioningStatusRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filter: Optional[OperationStatusFilterModel] = Field(default=None, alias="Filter")


class ListAccountAssignmentCreationStatusRequestListAccountAssignmentCreationStatusPaginateModel(
    BaseModel
):
    instance_arn: str = Field(alias="InstanceArn")
    filter: Optional[OperationStatusFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountAssignmentDeletionStatusRequestListAccountAssignmentDeletionStatusPaginateModel(
    BaseModel
):
    instance_arn: str = Field(alias="InstanceArn")
    filter: Optional[OperationStatusFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountAssignmentsRequestListAccountAssignmentsPaginateModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    account_id: str = Field(alias="AccountId")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccountsForProvisionedPermissionSetRequestListAccountsForProvisionedPermissionSetPaginateModel(
    BaseModel
):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    provisioning_status: Optional[
        Literal[
            "LATEST_PERMISSION_SET_NOT_PROVISIONED", "LATEST_PERMISSION_SET_PROVISIONED"
        ]
    ] = Field(default=None, alias="ProvisioningStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomerManagedPolicyReferencesInPermissionSetRequestListCustomerManagedPolicyReferencesInPermissionSetPaginateModel(
    BaseModel
):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstancesRequestListInstancesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListManagedPoliciesInPermissionSetRequestListManagedPoliciesInPermissionSetPaginateModel(
    BaseModel
):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionSetProvisioningStatusRequestListPermissionSetProvisioningStatusPaginateModel(
    BaseModel
):
    instance_arn: str = Field(alias="InstanceArn")
    filter: Optional[OperationStatusFilterModel] = Field(default=None, alias="Filter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionSetsProvisionedToAccountRequestListPermissionSetsProvisionedToAccountPaginateModel(
    BaseModel
):
    instance_arn: str = Field(alias="InstanceArn")
    account_id: str = Field(alias="AccountId")
    provisioning_status: Optional[
        Literal[
            "LATEST_PERMISSION_SET_NOT_PROVISIONED", "LATEST_PERMISSION_SET_PROVISIONED"
        ]
    ] = Field(default=None, alias="ProvisioningStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionSetsRequestListPermissionSetsPaginateModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPermissionSetProvisioningStatusResponseModel(BaseModel):
    permission_sets_provisioning_status: List[
        PermissionSetProvisioningStatusMetadataModel
    ] = Field(alias="PermissionSetsProvisioningStatus")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstanceAccessControlAttributeConfigurationModel(BaseModel):
    access_control_attributes: Sequence[AccessControlAttributeModel] = Field(
        alias="AccessControlAttributes"
    )


class GetPermissionsBoundaryForPermissionSetResponseModel(BaseModel):
    permissions_boundary: PermissionsBoundaryModel = Field(alias="PermissionsBoundary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPermissionsBoundaryToPermissionSetRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    permission_set_arn: str = Field(alias="PermissionSetArn")
    permissions_boundary: PermissionsBoundaryModel = Field(alias="PermissionsBoundary")


class CreateInstanceAccessControlAttributeConfigurationRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    instance_access_control_attribute_configuration: InstanceAccessControlAttributeConfigurationModel = Field(
        alias="InstanceAccessControlAttributeConfiguration"
    )


class DescribeInstanceAccessControlAttributeConfigurationResponseModel(BaseModel):
    status: Literal["CREATION_FAILED", "CREATION_IN_PROGRESS", "ENABLED"] = Field(
        alias="Status"
    )
    status_reason: str = Field(alias="StatusReason")
    instance_access_control_attribute_configuration: InstanceAccessControlAttributeConfigurationModel = Field(
        alias="InstanceAccessControlAttributeConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInstanceAccessControlAttributeConfigurationRequestModel(BaseModel):
    instance_arn: str = Field(alias="InstanceArn")
    instance_access_control_attribute_configuration: InstanceAccessControlAttributeConfigurationModel = Field(
        alias="InstanceAccessControlAttributeConfiguration"
    )
