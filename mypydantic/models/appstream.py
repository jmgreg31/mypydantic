# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccessEndpointModel(BaseModel):
    endpoint_type: Literal["STREAMING"] = Field(alias="EndpointType")
    vpce_id: Optional[str] = Field(default=None, alias="VpceId")


class S3LocationModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")
    s3_key: str = Field(alias="S3Key")


class ApplicationFleetAssociationModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    application_arn: str = Field(alias="ApplicationArn")


class ApplicationSettingsResponseModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    settings_group: Optional[str] = Field(default=None, alias="SettingsGroup")
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")


class ApplicationSettingsModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    settings_group: Optional[str] = Field(default=None, alias="SettingsGroup")


class AssociateApplicationFleetRequestModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    application_arn: str = Field(alias="ApplicationArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateApplicationToEntitlementRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    entitlement_name: str = Field(alias="EntitlementName")
    application_identifier: str = Field(alias="ApplicationIdentifier")


class AssociateFleetRequestModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    stack_name: str = Field(alias="StackName")


class UserStackAssociationModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    user_name: str = Field(alias="UserName")
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )
    send_email_notification: Optional[bool] = Field(
        default=None, alias="SendEmailNotification"
    )


class CertificateBasedAuthPropertiesModel(BaseModel):
    status: Optional[
        Literal["DISABLED", "ENABLED", "ENABLED_NO_DIRECTORY_LOGIN_FALLBACK"]
    ] = Field(default=None, alias="Status")
    certificate_authority_arn: Optional[str] = Field(
        default=None, alias="CertificateAuthorityArn"
    )


class ComputeCapacityStatusModel(BaseModel):
    desired: int = Field(alias="Desired")
    running: Optional[int] = Field(default=None, alias="Running")
    in_use: Optional[int] = Field(default=None, alias="InUse")
    available: Optional[int] = Field(default=None, alias="Available")


class ComputeCapacityModel(BaseModel):
    desired_instances: int = Field(alias="DesiredInstances")


class CopyImageRequestModel(BaseModel):
    source_image_name: str = Field(alias="SourceImageName")
    destination_image_name: str = Field(alias="DestinationImageName")
    destination_region: str = Field(alias="DestinationRegion")
    destination_image_description: Optional[str] = Field(
        default=None, alias="DestinationImageDescription"
    )


class ServiceAccountCredentialsModel(BaseModel):
    account_name: str = Field(alias="AccountName")
    account_password: str = Field(alias="AccountPassword")


class EntitlementAttributeModel(BaseModel):
    name: str = Field(alias="Name")
    value: str = Field(alias="Value")


class DomainJoinInfoModel(BaseModel):
    directory_name: Optional[str] = Field(default=None, alias="DirectoryName")
    organizational_unit_distinguished_name: Optional[str] = Field(
        default=None, alias="OrganizationalUnitDistinguishedName"
    )


class VpcConfigModel(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class CreateImageBuilderStreamingURLRequestModel(BaseModel):
    name: str = Field(alias="Name")
    validity: Optional[int] = Field(default=None, alias="Validity")


class StorageConnectorModel(BaseModel):
    connector_type: Literal["GOOGLE_DRIVE", "HOMEFOLDERS", "ONE_DRIVE"] = Field(
        alias="ConnectorType"
    )
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    domains: Optional[Sequence[str]] = Field(default=None, alias="Domains")


class StreamingExperienceSettingsModel(BaseModel):
    preferred_protocol: Optional[Literal["TCP", "UDP"]] = Field(
        default=None, alias="PreferredProtocol"
    )


class UserSettingModel(BaseModel):
    action: Literal[
        "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
        "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
        "DOMAIN_PASSWORD_SIGNIN",
        "DOMAIN_SMART_CARD_SIGNIN",
        "FILE_DOWNLOAD",
        "FILE_UPLOAD",
        "PRINTING_TO_LOCAL_DEVICE",
    ] = Field(alias="Action")
    permission: Literal["DISABLED", "ENABLED"] = Field(alias="Permission")


class CreateStreamingURLRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    fleet_name: str = Field(alias="FleetName")
    user_id: str = Field(alias="UserId")
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    validity: Optional[int] = Field(default=None, alias="Validity")
    session_context: Optional[str] = Field(default=None, alias="SessionContext")


class CreateUpdatedImageRequestModel(BaseModel):
    existing_image_name: str = Field(alias="existingImageName")
    new_image_name: str = Field(alias="newImageName")
    new_image_description: Optional[str] = Field(
        default=None, alias="newImageDescription"
    )
    new_image_display_name: Optional[str] = Field(
        default=None, alias="newImageDisplayName"
    )
    new_image_tags: Optional[Mapping[str, str]] = Field(
        default=None, alias="newImageTags"
    )
    dry_run: Optional[bool] = Field(default=None, alias="dryRun")


class CreateUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )
    message_action: Optional[Literal["RESEND", "SUPPRESS"]] = Field(
        default=None, alias="MessageAction"
    )
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")


class DeleteAppBlockRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteApplicationRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteDirectoryConfigRequestModel(BaseModel):
    directory_name: str = Field(alias="DirectoryName")


class DeleteEntitlementRequestModel(BaseModel):
    name: str = Field(alias="Name")
    stack_name: str = Field(alias="StackName")


class DeleteFleetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteImageBuilderRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteImagePermissionsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    shared_account_id: str = Field(alias="SharedAccountId")


class DeleteImageRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteStackRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )


class DescribeAppBlocksRequestModel(BaseModel):
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeApplicationFleetAssociationsRequestModel(BaseModel):
    fleet_name: Optional[str] = Field(default=None, alias="FleetName")
    application_arn: Optional[str] = Field(default=None, alias="ApplicationArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeApplicationsRequestModel(BaseModel):
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeDirectoryConfigsRequestModel(BaseModel):
    directory_names: Optional[Sequence[str]] = Field(
        default=None, alias="DirectoryNames"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeEntitlementsRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    name: Optional[str] = Field(default=None, alias="Name")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeFleetsRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeImageBuildersRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeImagePermissionsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    shared_aws_account_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SharedAwsAccountIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeImagesRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")
    type: Optional[Literal["PRIVATE", "PUBLIC", "SHARED"]] = Field(
        default=None, alias="Type"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeSessionsRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    fleet_name: str = Field(alias="FleetName")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")
    authentication_type: Optional[Literal["API", "AWS_AD", "SAML", "USERPOOL"]] = Field(
        default=None, alias="AuthenticationType"
    )


class DescribeStacksRequestModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeUsageReportSubscriptionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeUserStackAssociationsRequestModel(BaseModel):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    authentication_type: Optional[Literal["API", "AWS_AD", "SAML", "USERPOOL"]] = Field(
        default=None, alias="AuthenticationType"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeUsersRequestModel(BaseModel):
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class UserModel(BaseModel):
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    status: Optional[str] = Field(default=None, alias="Status")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class DisableUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )


class DisassociateApplicationFleetRequestModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    application_arn: str = Field(alias="ApplicationArn")


class DisassociateApplicationFromEntitlementRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    entitlement_name: str = Field(alias="EntitlementName")
    application_identifier: str = Field(alias="ApplicationIdentifier")


class DisassociateFleetRequestModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    stack_name: str = Field(alias="StackName")


class EnableUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )


class EntitledApplicationModel(BaseModel):
    application_identifier: str = Field(alias="ApplicationIdentifier")


class ExpireSessionRequestModel(BaseModel):
    session_id: str = Field(alias="SessionId")


class FleetErrorModel(BaseModel):
    error_code: Optional[
        Literal[
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "FLEET_INSTANCE_PROVISIONING_FAILURE",
            "FLEET_STOPPED",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IGW_NOT_ATTACHED",
            "IMAGE_NOT_FOUND",
            "INTERNAL_SERVICE_ERROR",
            "INVALID_SUBNET_CONFIGURATION",
            "MACHINE_ROLE_IS_MISSING",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "SECURITY_GROUPS_NOT_FOUND",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "SUBNET_NOT_FOUND",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ImageBuilderStateChangeReasonModel(BaseModel):
    code: Optional[Literal["IMAGE_UNAVAILABLE", "INTERNAL_ERROR"]] = Field(
        default=None, alias="Code"
    )
    message: Optional[str] = Field(default=None, alias="Message")


class NetworkAccessConfigurationModel(BaseModel):
    eni_private_ip_address: Optional[str] = Field(
        default=None, alias="EniPrivateIpAddress"
    )
    eni_id: Optional[str] = Field(default=None, alias="EniId")


class ResourceErrorModel(BaseModel):
    error_code: Optional[
        Literal[
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "FLEET_INSTANCE_PROVISIONING_FAILURE",
            "FLEET_STOPPED",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IGW_NOT_ATTACHED",
            "IMAGE_NOT_FOUND",
            "INTERNAL_SERVICE_ERROR",
            "INVALID_SUBNET_CONFIGURATION",
            "MACHINE_ROLE_IS_MISSING",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "SECURITY_GROUPS_NOT_FOUND",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "SUBNET_NOT_FOUND",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    error_timestamp: Optional[datetime] = Field(default=None, alias="ErrorTimestamp")


class ImagePermissionsModel(BaseModel):
    allow_fleet: Optional[bool] = Field(default=None, alias="allowFleet")
    allow_image_builder: Optional[bool] = Field(default=None, alias="allowImageBuilder")


class ImageStateChangeReasonModel(BaseModel):
    code: Optional[
        Literal["IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE", "INTERNAL_ERROR"]
    ] = Field(default=None, alias="Code")
    message: Optional[str] = Field(default=None, alias="Message")


class LastReportGenerationExecutionErrorModel(BaseModel):
    error_code: Optional[
        Literal["ACCESS_DENIED", "INTERNAL_SERVICE_ERROR", "RESOURCE_NOT_FOUND"]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class ListAssociatedFleetsRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAssociatedStacksRequestModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListEntitledApplicationsRequestModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    entitlement_name: str = Field(alias="EntitlementName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class StackErrorModel(BaseModel):
    error_code: Optional[
        Literal["INTERNAL_SERVICE_ERROR", "STORAGE_CONNECTOR_ERROR"]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class StartFleetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StartImageBuilderRequestModel(BaseModel):
    name: str = Field(alias="Name")
    appstream_agent_version: Optional[str] = Field(
        default=None, alias="AppstreamAgentVersion"
    )


class StopFleetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class StopImageBuilderRequestModel(BaseModel):
    name: str = Field(alias="Name")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ApplicationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    icon_url: Optional[str] = Field(default=None, alias="IconURL")
    launch_path: Optional[str] = Field(default=None, alias="LaunchPath")
    launch_parameters: Optional[str] = Field(default=None, alias="LaunchParameters")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    metadata: Optional[Dict[str, str]] = Field(default=None, alias="Metadata")
    working_directory: Optional[str] = Field(default=None, alias="WorkingDirectory")
    description: Optional[str] = Field(default=None, alias="Description")
    arn: Optional[str] = Field(default=None, alias="Arn")
    app_block_arn: Optional[str] = Field(default=None, alias="AppBlockArn")
    icon_s3_location: Optional[S3LocationModel] = Field(
        default=None, alias="IconS3Location"
    )
    platforms: Optional[
        List[
            Literal[
                "AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"
            ]
        ]
    ] = Field(default=None, alias="Platforms")
    instance_families: Optional[List[str]] = Field(
        default=None, alias="InstanceFamilies"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class CreateApplicationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    icon_s3_location: S3LocationModel = Field(alias="IconS3Location")
    launch_path: str = Field(alias="LaunchPath")
    platforms: Sequence[
        Literal[
            "AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"
        ]
    ] = Field(alias="Platforms")
    instance_families: Sequence[str] = Field(alias="InstanceFamilies")
    app_block_arn: str = Field(alias="AppBlockArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")
    working_directory: Optional[str] = Field(default=None, alias="WorkingDirectory")
    launch_parameters: Optional[str] = Field(default=None, alias="LaunchParameters")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ScriptDetailsModel(BaseModel):
    script_s3_location: S3LocationModel = Field(alias="ScriptS3Location")
    executable_path: str = Field(alias="ExecutablePath")
    timeout_in_seconds: int = Field(alias="TimeoutInSeconds")
    executable_parameters: Optional[str] = Field(
        default=None, alias="ExecutableParameters"
    )


class UpdateApplicationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")
    icon_s3_location: Optional[S3LocationModel] = Field(
        default=None, alias="IconS3Location"
    )
    launch_path: Optional[str] = Field(default=None, alias="LaunchPath")
    working_directory: Optional[str] = Field(default=None, alias="WorkingDirectory")
    launch_parameters: Optional[str] = Field(default=None, alias="LaunchParameters")
    app_block_arn: Optional[str] = Field(default=None, alias="AppBlockArn")
    attributes_to_delete: Optional[
        Sequence[Literal["LAUNCH_PARAMETERS", "WORKING_DIRECTORY"]]
    ] = Field(default=None, alias="AttributesToDelete")


class AssociateApplicationFleetResultModel(BaseModel):
    application_fleet_association: ApplicationFleetAssociationModel = Field(
        alias="ApplicationFleetAssociation"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CopyImageResponseModel(BaseModel):
    destination_image_name: str = Field(alias="DestinationImageName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageBuilderStreamingURLResultModel(BaseModel):
    streaming_url: str = Field(alias="StreamingURL")
    expires: datetime = Field(alias="Expires")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamingURLResultModel(BaseModel):
    streaming_url: str = Field(alias="StreamingURL")
    expires: datetime = Field(alias="Expires")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUsageReportSubscriptionResultModel(BaseModel):
    s3_bucket_name: str = Field(alias="S3BucketName")
    schedule: Literal["DAILY"] = Field(alias="Schedule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationFleetAssociationsResultModel(BaseModel):
    application_fleet_associations: List[ApplicationFleetAssociationModel] = Field(
        alias="ApplicationFleetAssociations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociatedFleetsResultModel(BaseModel):
    names: List[str] = Field(alias="Names")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociatedStacksResultModel(BaseModel):
    names: List[str] = Field(alias="Names")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchAssociateUserStackRequestModel(BaseModel):
    user_stack_associations: Sequence[UserStackAssociationModel] = Field(
        alias="UserStackAssociations"
    )


class BatchDisassociateUserStackRequestModel(BaseModel):
    user_stack_associations: Sequence[UserStackAssociationModel] = Field(
        alias="UserStackAssociations"
    )


class DescribeUserStackAssociationsResultModel(BaseModel):
    user_stack_associations: List[UserStackAssociationModel] = Field(
        alias="UserStackAssociations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UserStackAssociationErrorModel(BaseModel):
    user_stack_association: Optional[UserStackAssociationModel] = Field(
        default=None, alias="UserStackAssociation"
    )
    error_code: Optional[
        Literal[
            "DIRECTORY_NOT_FOUND",
            "INTERNAL_ERROR",
            "STACK_NOT_FOUND",
            "USER_NAME_NOT_FOUND",
        ]
    ] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")


class CreateDirectoryConfigRequestModel(BaseModel):
    directory_name: str = Field(alias="DirectoryName")
    organizational_unit_distinguished_names: Sequence[str] = Field(
        alias="OrganizationalUnitDistinguishedNames"
    )
    service_account_credentials: Optional[ServiceAccountCredentialsModel] = Field(
        default=None, alias="ServiceAccountCredentials"
    )
    certificate_based_auth_properties: Optional[
        CertificateBasedAuthPropertiesModel
    ] = Field(default=None, alias="CertificateBasedAuthProperties")


class DirectoryConfigModel(BaseModel):
    directory_name: str = Field(alias="DirectoryName")
    organizational_unit_distinguished_names: Optional[List[str]] = Field(
        default=None, alias="OrganizationalUnitDistinguishedNames"
    )
    service_account_credentials: Optional[ServiceAccountCredentialsModel] = Field(
        default=None, alias="ServiceAccountCredentials"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    certificate_based_auth_properties: Optional[
        CertificateBasedAuthPropertiesModel
    ] = Field(default=None, alias="CertificateBasedAuthProperties")


class UpdateDirectoryConfigRequestModel(BaseModel):
    directory_name: str = Field(alias="DirectoryName")
    organizational_unit_distinguished_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationalUnitDistinguishedNames"
    )
    service_account_credentials: Optional[ServiceAccountCredentialsModel] = Field(
        default=None, alias="ServiceAccountCredentials"
    )
    certificate_based_auth_properties: Optional[
        CertificateBasedAuthPropertiesModel
    ] = Field(default=None, alias="CertificateBasedAuthProperties")


class CreateEntitlementRequestModel(BaseModel):
    name: str = Field(alias="Name")
    stack_name: str = Field(alias="StackName")
    app_visibility: Literal["ALL", "ASSOCIATED"] = Field(alias="AppVisibility")
    attributes: Sequence[EntitlementAttributeModel] = Field(alias="Attributes")
    description: Optional[str] = Field(default=None, alias="Description")


class EntitlementModel(BaseModel):
    name: str = Field(alias="Name")
    stack_name: str = Field(alias="StackName")
    app_visibility: Literal["ALL", "ASSOCIATED"] = Field(alias="AppVisibility")
    attributes: List[EntitlementAttributeModel] = Field(alias="Attributes")
    description: Optional[str] = Field(default=None, alias="Description")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_modified_time: Optional[datetime] = Field(
        default=None, alias="LastModifiedTime"
    )


class UpdateEntitlementRequestModel(BaseModel):
    name: str = Field(alias="Name")
    stack_name: str = Field(alias="StackName")
    description: Optional[str] = Field(default=None, alias="Description")
    app_visibility: Optional[Literal["ALL", "ASSOCIATED"]] = Field(
        default=None, alias="AppVisibility"
    )
    attributes: Optional[Sequence[EntitlementAttributeModel]] = Field(
        default=None, alias="Attributes"
    )


class CreateFleetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    instance_type: str = Field(alias="InstanceType")
    image_name: Optional[str] = Field(default=None, alias="ImageName")
    image_arn: Optional[str] = Field(default=None, alias="ImageArn")
    fleet_type: Optional[Literal["ALWAYS_ON", "ELASTIC", "ON_DEMAND"]] = Field(
        default=None, alias="FleetType"
    )
    compute_capacity: Optional[ComputeCapacityModel] = Field(
        default=None, alias="ComputeCapacity"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    max_user_duration_in_seconds: Optional[int] = Field(
        default=None, alias="MaxUserDurationInSeconds"
    )
    disconnect_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="DisconnectTimeoutInSeconds"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    enable_default_internet_access: Optional[bool] = Field(
        default=None, alias="EnableDefaultInternetAccess"
    )
    domain_join_info: Optional[DomainJoinInfoModel] = Field(
        default=None, alias="DomainJoinInfo"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    idle_disconnect_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="IdleDisconnectTimeoutInSeconds"
    )
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    stream_view: Optional[Literal["APP", "DESKTOP"]] = Field(
        default=None, alias="StreamView"
    )
    platform: Optional[
        Literal[
            "AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"
        ]
    ] = Field(default=None, alias="Platform")
    max_concurrent_sessions: Optional[int] = Field(
        default=None, alias="MaxConcurrentSessions"
    )
    usb_device_filter_strings: Optional[Sequence[str]] = Field(
        default=None, alias="UsbDeviceFilterStrings"
    )
    session_script_s3_location: Optional[S3LocationModel] = Field(
        default=None, alias="SessionScriptS3Location"
    )


class CreateImageBuilderRequestModel(BaseModel):
    name: str = Field(alias="Name")
    instance_type: str = Field(alias="InstanceType")
    image_name: Optional[str] = Field(default=None, alias="ImageName")
    image_arn: Optional[str] = Field(default=None, alias="ImageArn")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    enable_default_internet_access: Optional[bool] = Field(
        default=None, alias="EnableDefaultInternetAccess"
    )
    domain_join_info: Optional[DomainJoinInfoModel] = Field(
        default=None, alias="DomainJoinInfo"
    )
    appstream_agent_version: Optional[str] = Field(
        default=None, alias="AppstreamAgentVersion"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    access_endpoints: Optional[Sequence[AccessEndpointModel]] = Field(
        default=None, alias="AccessEndpoints"
    )


class UpdateFleetRequestModel(BaseModel):
    image_name: Optional[str] = Field(default=None, alias="ImageName")
    image_arn: Optional[str] = Field(default=None, alias="ImageArn")
    name: Optional[str] = Field(default=None, alias="Name")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    compute_capacity: Optional[ComputeCapacityModel] = Field(
        default=None, alias="ComputeCapacity"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    max_user_duration_in_seconds: Optional[int] = Field(
        default=None, alias="MaxUserDurationInSeconds"
    )
    disconnect_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="DisconnectTimeoutInSeconds"
    )
    delete_vpc_config: Optional[bool] = Field(default=None, alias="DeleteVpcConfig")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    enable_default_internet_access: Optional[bool] = Field(
        default=None, alias="EnableDefaultInternetAccess"
    )
    domain_join_info: Optional[DomainJoinInfoModel] = Field(
        default=None, alias="DomainJoinInfo"
    )
    idle_disconnect_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="IdleDisconnectTimeoutInSeconds"
    )
    attributes_to_delete: Optional[
        Sequence[
            Literal[
                "DOMAIN_JOIN_INFO",
                "IAM_ROLE_ARN",
                "SESSION_SCRIPT_S3_LOCATION",
                "USB_DEVICE_FILTER_STRINGS",
                "VPC_CONFIGURATION",
                "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
            ]
        ]
    ] = Field(default=None, alias="AttributesToDelete")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    stream_view: Optional[Literal["APP", "DESKTOP"]] = Field(
        default=None, alias="StreamView"
    )
    platform: Optional[
        Literal[
            "AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"
        ]
    ] = Field(default=None, alias="Platform")
    max_concurrent_sessions: Optional[int] = Field(
        default=None, alias="MaxConcurrentSessions"
    )
    usb_device_filter_strings: Optional[Sequence[str]] = Field(
        default=None, alias="UsbDeviceFilterStrings"
    )
    session_script_s3_location: Optional[S3LocationModel] = Field(
        default=None, alias="SessionScriptS3Location"
    )


class CreateStackRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    storage_connectors: Optional[Sequence[StorageConnectorModel]] = Field(
        default=None, alias="StorageConnectors"
    )
    redirect_url: Optional[str] = Field(default=None, alias="RedirectURL")
    feedback_url: Optional[str] = Field(default=None, alias="FeedbackURL")
    user_settings: Optional[Sequence[UserSettingModel]] = Field(
        default=None, alias="UserSettings"
    )
    application_settings: Optional[ApplicationSettingsModel] = Field(
        default=None, alias="ApplicationSettings"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    access_endpoints: Optional[Sequence[AccessEndpointModel]] = Field(
        default=None, alias="AccessEndpoints"
    )
    embed_host_domains: Optional[Sequence[str]] = Field(
        default=None, alias="EmbedHostDomains"
    )
    streaming_experience_settings: Optional[StreamingExperienceSettingsModel] = Field(
        default=None, alias="StreamingExperienceSettings"
    )


class UpdateStackRequestModel(BaseModel):
    name: str = Field(alias="Name")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")
    storage_connectors: Optional[Sequence[StorageConnectorModel]] = Field(
        default=None, alias="StorageConnectors"
    )
    delete_storage_connectors: Optional[bool] = Field(
        default=None, alias="DeleteStorageConnectors"
    )
    redirect_url: Optional[str] = Field(default=None, alias="RedirectURL")
    feedback_url: Optional[str] = Field(default=None, alias="FeedbackURL")
    attributes_to_delete: Optional[
        Sequence[
            Literal[
                "ACCESS_ENDPOINTS",
                "EMBED_HOST_DOMAINS",
                "FEEDBACK_URL",
                "IAM_ROLE_ARN",
                "REDIRECT_URL",
                "STORAGE_CONNECTORS",
                "STORAGE_CONNECTOR_GOOGLE_DRIVE",
                "STORAGE_CONNECTOR_HOMEFOLDERS",
                "STORAGE_CONNECTOR_ONE_DRIVE",
                "STREAMING_EXPERIENCE_SETTINGS",
                "THEME_NAME",
                "USER_SETTINGS",
            ]
        ]
    ] = Field(default=None, alias="AttributesToDelete")
    user_settings: Optional[Sequence[UserSettingModel]] = Field(
        default=None, alias="UserSettings"
    )
    application_settings: Optional[ApplicationSettingsModel] = Field(
        default=None, alias="ApplicationSettings"
    )
    access_endpoints: Optional[Sequence[AccessEndpointModel]] = Field(
        default=None, alias="AccessEndpoints"
    )
    embed_host_domains: Optional[Sequence[str]] = Field(
        default=None, alias="EmbedHostDomains"
    )
    streaming_experience_settings: Optional[StreamingExperienceSettingsModel] = Field(
        default=None, alias="StreamingExperienceSettings"
    )


class DescribeDirectoryConfigsRequestDescribeDirectoryConfigsPaginateModel(BaseModel):
    directory_names: Optional[Sequence[str]] = Field(
        default=None, alias="DirectoryNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFleetsRequestDescribeFleetsPaginateModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeImageBuildersRequestDescribeImageBuildersPaginateModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeImagesRequestDescribeImagesPaginateModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    arns: Optional[Sequence[str]] = Field(default=None, alias="Arns")
    type: Optional[Literal["PRIVATE", "PUBLIC", "SHARED"]] = Field(
        default=None, alias="Type"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSessionsRequestDescribeSessionsPaginateModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    fleet_name: str = Field(alias="FleetName")
    user_id: Optional[str] = Field(default=None, alias="UserId")
    authentication_type: Optional[Literal["API", "AWS_AD", "SAML", "USERPOOL"]] = Field(
        default=None, alias="AuthenticationType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeStacksRequestDescribeStacksPaginateModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUserStackAssociationsRequestDescribeUserStackAssociationsPaginateModel(
    BaseModel
):
    stack_name: Optional[str] = Field(default=None, alias="StackName")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    authentication_type: Optional[Literal["API", "AWS_AD", "SAML", "USERPOOL"]] = Field(
        default=None, alias="AuthenticationType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeUsersRequestDescribeUsersPaginateModel(BaseModel):
    authentication_type: Literal["API", "AWS_AD", "SAML", "USERPOOL"] = Field(
        alias="AuthenticationType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociatedFleetsRequestListAssociatedFleetsPaginateModel(BaseModel):
    stack_name: str = Field(alias="StackName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAssociatedStacksRequestListAssociatedStacksPaginateModel(BaseModel):
    fleet_name: str = Field(alias="FleetName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeFleetsRequestFleetStartedWaitModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeFleetsRequestFleetStoppedWaitModel(BaseModel):
    names: Optional[Sequence[str]] = Field(default=None, alias="Names")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeUsersResultModel(BaseModel):
    users: List[UserModel] = Field(alias="Users")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEntitledApplicationsResultModel(BaseModel):
    entitled_applications: List[EntitledApplicationModel] = Field(
        alias="EntitledApplications"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FleetModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    instance_type: str = Field(alias="InstanceType")
    compute_capacity_status: ComputeCapacityStatusModel = Field(
        alias="ComputeCapacityStatus"
    )
    state: Literal["RUNNING", "STARTING", "STOPPED", "STOPPING"] = Field(alias="State")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    description: Optional[str] = Field(default=None, alias="Description")
    image_name: Optional[str] = Field(default=None, alias="ImageName")
    image_arn: Optional[str] = Field(default=None, alias="ImageArn")
    fleet_type: Optional[Literal["ALWAYS_ON", "ELASTIC", "ON_DEMAND"]] = Field(
        default=None, alias="FleetType"
    )
    max_user_duration_in_seconds: Optional[int] = Field(
        default=None, alias="MaxUserDurationInSeconds"
    )
    disconnect_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="DisconnectTimeoutInSeconds"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    fleet_errors: Optional[List[FleetErrorModel]] = Field(
        default=None, alias="FleetErrors"
    )
    enable_default_internet_access: Optional[bool] = Field(
        default=None, alias="EnableDefaultInternetAccess"
    )
    domain_join_info: Optional[DomainJoinInfoModel] = Field(
        default=None, alias="DomainJoinInfo"
    )
    idle_disconnect_timeout_in_seconds: Optional[int] = Field(
        default=None, alias="IdleDisconnectTimeoutInSeconds"
    )
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    stream_view: Optional[Literal["APP", "DESKTOP"]] = Field(
        default=None, alias="StreamView"
    )
    platform: Optional[
        Literal[
            "AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"
        ]
    ] = Field(default=None, alias="Platform")
    max_concurrent_sessions: Optional[int] = Field(
        default=None, alias="MaxConcurrentSessions"
    )
    usb_device_filter_strings: Optional[List[str]] = Field(
        default=None, alias="UsbDeviceFilterStrings"
    )
    session_script_s3_location: Optional[S3LocationModel] = Field(
        default=None, alias="SessionScriptS3Location"
    )


class SessionModel(BaseModel):
    id: str = Field(alias="Id")
    user_id: str = Field(alias="UserId")
    stack_name: str = Field(alias="StackName")
    fleet_name: str = Field(alias="FleetName")
    state: Literal["ACTIVE", "EXPIRED", "PENDING"] = Field(alias="State")
    connection_state: Optional[Literal["CONNECTED", "NOT_CONNECTED"]] = Field(
        default=None, alias="ConnectionState"
    )
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    max_expiration_time: Optional[datetime] = Field(
        default=None, alias="MaxExpirationTime"
    )
    authentication_type: Optional[Literal["API", "AWS_AD", "SAML", "USERPOOL"]] = Field(
        default=None, alias="AuthenticationType"
    )
    network_access_configuration: Optional[NetworkAccessConfigurationModel] = Field(
        default=None, alias="NetworkAccessConfiguration"
    )


class ImageBuilderModel(BaseModel):
    name: str = Field(alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    image_arn: Optional[str] = Field(default=None, alias="ImageArn")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="VpcConfig")
    instance_type: Optional[str] = Field(default=None, alias="InstanceType")
    platform: Optional[
        Literal[
            "AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"
        ]
    ] = Field(default=None, alias="Platform")
    iam_role_arn: Optional[str] = Field(default=None, alias="IamRoleArn")
    state: Optional[
        Literal[
            "DELETING",
            "FAILED",
            "PENDING",
            "PENDING_QUALIFICATION",
            "REBOOTING",
            "RUNNING",
            "SNAPSHOTTING",
            "STOPPED",
            "STOPPING",
            "UPDATING",
            "UPDATING_AGENT",
        ]
    ] = Field(default=None, alias="State")
    state_change_reason: Optional[ImageBuilderStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    enable_default_internet_access: Optional[bool] = Field(
        default=None, alias="EnableDefaultInternetAccess"
    )
    domain_join_info: Optional[DomainJoinInfoModel] = Field(
        default=None, alias="DomainJoinInfo"
    )
    network_access_configuration: Optional[NetworkAccessConfigurationModel] = Field(
        default=None, alias="NetworkAccessConfiguration"
    )
    image_builder_errors: Optional[List[ResourceErrorModel]] = Field(
        default=None, alias="ImageBuilderErrors"
    )
    appstream_agent_version: Optional[str] = Field(
        default=None, alias="AppstreamAgentVersion"
    )
    access_endpoints: Optional[List[AccessEndpointModel]] = Field(
        default=None, alias="AccessEndpoints"
    )


class SharedImagePermissionsModel(BaseModel):
    shared_account_id: str = Field(alias="sharedAccountId")
    image_permissions: ImagePermissionsModel = Field(alias="imagePermissions")


class UpdateImagePermissionsRequestModel(BaseModel):
    name: str = Field(alias="Name")
    shared_account_id: str = Field(alias="SharedAccountId")
    image_permissions: ImagePermissionsModel = Field(alias="ImagePermissions")


class UsageReportSubscriptionModel(BaseModel):
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    schedule: Optional[Literal["DAILY"]] = Field(default=None, alias="Schedule")
    last_generated_report_date: Optional[datetime] = Field(
        default=None, alias="LastGeneratedReportDate"
    )
    subscription_errors: Optional[
        List[LastReportGenerationExecutionErrorModel]
    ] = Field(default=None, alias="SubscriptionErrors")


class StackModel(BaseModel):
    name: str = Field(alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    storage_connectors: Optional[List[StorageConnectorModel]] = Field(
        default=None, alias="StorageConnectors"
    )
    redirect_url: Optional[str] = Field(default=None, alias="RedirectURL")
    feedback_url: Optional[str] = Field(default=None, alias="FeedbackURL")
    stack_errors: Optional[List[StackErrorModel]] = Field(
        default=None, alias="StackErrors"
    )
    user_settings: Optional[List[UserSettingModel]] = Field(
        default=None, alias="UserSettings"
    )
    application_settings: Optional[ApplicationSettingsResponseModel] = Field(
        default=None, alias="ApplicationSettings"
    )
    access_endpoints: Optional[List[AccessEndpointModel]] = Field(
        default=None, alias="AccessEndpoints"
    )
    embed_host_domains: Optional[List[str]] = Field(
        default=None, alias="EmbedHostDomains"
    )
    streaming_experience_settings: Optional[StreamingExperienceSettingsModel] = Field(
        default=None, alias="StreamingExperienceSettings"
    )


class CreateApplicationResultModel(BaseModel):
    application: ApplicationModel = Field(alias="Application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeApplicationsResultModel(BaseModel):
    applications: List[ApplicationModel] = Field(alias="Applications")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImageModel(BaseModel):
    name: str = Field(alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    base_image_arn: Optional[str] = Field(default=None, alias="BaseImageArn")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    state: Optional[
        Literal[
            "AVAILABLE",
            "COPYING",
            "CREATING",
            "DELETING",
            "FAILED",
            "IMPORTING",
            "PENDING",
        ]
    ] = Field(default=None, alias="State")
    visibility: Optional[Literal["PRIVATE", "PUBLIC", "SHARED"]] = Field(
        default=None, alias="Visibility"
    )
    image_builder_supported: Optional[bool] = Field(
        default=None, alias="ImageBuilderSupported"
    )
    image_builder_name: Optional[str] = Field(default=None, alias="ImageBuilderName")
    platform: Optional[
        Literal[
            "AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"
        ]
    ] = Field(default=None, alias="Platform")
    description: Optional[str] = Field(default=None, alias="Description")
    state_change_reason: Optional[ImageStateChangeReasonModel] = Field(
        default=None, alias="StateChangeReason"
    )
    applications: Optional[List[ApplicationModel]] = Field(
        default=None, alias="Applications"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    public_base_image_released_date: Optional[datetime] = Field(
        default=None, alias="PublicBaseImageReleasedDate"
    )
    appstream_agent_version: Optional[str] = Field(
        default=None, alias="AppstreamAgentVersion"
    )
    image_permissions: Optional[ImagePermissionsModel] = Field(
        default=None, alias="ImagePermissions"
    )
    image_errors: Optional[List[ResourceErrorModel]] = Field(
        default=None, alias="ImageErrors"
    )


class UpdateApplicationResultModel(BaseModel):
    application: ApplicationModel = Field(alias="Application")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AppBlockModel(BaseModel):
    name: str = Field(alias="Name")
    arn: str = Field(alias="Arn")
    setup_script_details: ScriptDetailsModel = Field(alias="SetupScriptDetails")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    source_s3_location: Optional[S3LocationModel] = Field(
        default=None, alias="SourceS3Location"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class CreateAppBlockRequestModel(BaseModel):
    name: str = Field(alias="Name")
    source_s3_location: S3LocationModel = Field(alias="SourceS3Location")
    setup_script_details: ScriptDetailsModel = Field(alias="SetupScriptDetails")
    description: Optional[str] = Field(default=None, alias="Description")
    display_name: Optional[str] = Field(default=None, alias="DisplayName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class BatchAssociateUserStackResultModel(BaseModel):
    errors: List[UserStackAssociationErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchDisassociateUserStackResultModel(BaseModel):
    errors: List[UserStackAssociationErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDirectoryConfigResultModel(BaseModel):
    directory_config: DirectoryConfigModel = Field(alias="DirectoryConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDirectoryConfigsResultModel(BaseModel):
    directory_configs: List[DirectoryConfigModel] = Field(alias="DirectoryConfigs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDirectoryConfigResultModel(BaseModel):
    directory_config: DirectoryConfigModel = Field(alias="DirectoryConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateEntitlementResultModel(BaseModel):
    entitlement: EntitlementModel = Field(alias="Entitlement")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEntitlementsResultModel(BaseModel):
    entitlements: List[EntitlementModel] = Field(alias="Entitlements")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEntitlementResultModel(BaseModel):
    entitlement: EntitlementModel = Field(alias="Entitlement")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFleetResultModel(BaseModel):
    fleet: FleetModel = Field(alias="Fleet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetsResultModel(BaseModel):
    fleets: List[FleetModel] = Field(alias="Fleets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFleetResultModel(BaseModel):
    fleet: FleetModel = Field(alias="Fleet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSessionsResultModel(BaseModel):
    sessions: List[SessionModel] = Field(alias="Sessions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateImageBuilderResultModel(BaseModel):
    image_builder: ImageBuilderModel = Field(alias="ImageBuilder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteImageBuilderResultModel(BaseModel):
    image_builder: ImageBuilderModel = Field(alias="ImageBuilder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImageBuildersResultModel(BaseModel):
    image_builders: List[ImageBuilderModel] = Field(alias="ImageBuilders")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImageBuilderResultModel(BaseModel):
    image_builder: ImageBuilderModel = Field(alias="ImageBuilder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopImageBuilderResultModel(BaseModel):
    image_builder: ImageBuilderModel = Field(alias="ImageBuilder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImagePermissionsResultModel(BaseModel):
    name: str = Field(alias="Name")
    shared_image_permissions_list: List[SharedImagePermissionsModel] = Field(
        alias="SharedImagePermissionsList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUsageReportSubscriptionsResultModel(BaseModel):
    usage_report_subscriptions: List[UsageReportSubscriptionModel] = Field(
        alias="UsageReportSubscriptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStackResultModel(BaseModel):
    stack: StackModel = Field(alias="Stack")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeStacksResultModel(BaseModel):
    stacks: List[StackModel] = Field(alias="Stacks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStackResultModel(BaseModel):
    stack: StackModel = Field(alias="Stack")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUpdatedImageResultModel(BaseModel):
    image: ImageModel = Field(alias="image")
    can_update_image: bool = Field(alias="canUpdateImage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteImageResultModel(BaseModel):
    image: ImageModel = Field(alias="Image")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeImagesResultModel(BaseModel):
    images: List[ImageModel] = Field(alias="Images")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAppBlockResultModel(BaseModel):
    app_block: AppBlockModel = Field(alias="AppBlock")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAppBlocksResultModel(BaseModel):
    app_blocks: List[AppBlockModel] = Field(alias="AppBlocks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
