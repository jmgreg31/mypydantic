# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AcceptEulasRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    eula_ids: Optional[Sequence[str]] = Field(default=None, alias="eulaIds")


class EulaAcceptanceModel(BaseModel):
    accepted_at: Optional[datetime] = Field(default=None, alias="acceptedAt")
    accepted_by: Optional[str] = Field(default=None, alias="acceptedBy")
    acceptee_id: Optional[str] = Field(default=None, alias="accepteeId")
    eula_acceptance_id: Optional[str] = Field(default=None, alias="eulaAcceptanceId")
    eula_id: Optional[str] = Field(default=None, alias="eulaId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ActiveDirectoryComputerAttributeModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class ComputeFarmConfigurationModel(BaseModel):
    active_directory_user: Optional[str] = Field(
        default=None, alias="activeDirectoryUser"
    )
    endpoint: Optional[str] = Field(default=None, alias="endpoint")


class CreateStreamingImageRequestModel(BaseModel):
    ec2_image_id: str = Field(alias="ec2ImageId")
    name: str = Field(alias="name")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateStreamingSessionRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    ec2_instance_type: Optional[
        Literal[
            "g3.4xlarge",
            "g3s.xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.xlarge",
            "g5.16xlarge",
            "g5.2xlarge",
            "g5.4xlarge",
            "g5.8xlarge",
            "g5.xlarge",
        ]
    ] = Field(default=None, alias="ec2InstanceType")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    streaming_image_id: Optional[str] = Field(default=None, alias="streamingImageId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateStreamingSessionStreamRequestModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    expiration_in_seconds: Optional[int] = Field(
        default=None, alias="expirationInSeconds"
    )


class StreamingSessionStreamModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETED",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "READY",
        ]
    ] = Field(default=None, alias="state")
    status_code: Optional[
        Literal[
            "INTERNAL_ERROR",
            "NETWORK_CONNECTION_ERROR",
            "STREAM_CREATE_IN_PROGRESS",
            "STREAM_DELETED",
            "STREAM_DELETE_IN_PROGRESS",
            "STREAM_READY",
        ]
    ] = Field(default=None, alias="statusCode")
    stream_id: Optional[str] = Field(default=None, alias="streamId")
    url: Optional[str] = Field(default=None, alias="url")


class ScriptParameterKeyValueModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")


class StudioComponentInitializationScriptModel(BaseModel):
    launch_profile_protocol_version: Optional[str] = Field(
        default=None, alias="launchProfileProtocolVersion"
    )
    platform: Optional[Literal["LINUX", "WINDOWS"]] = Field(
        default=None, alias="platform"
    )
    run_context: Optional[
        Literal["SYSTEM_INITIALIZATION", "USER_INITIALIZATION"]
    ] = Field(default=None, alias="runContext")
    script: Optional[str] = Field(default=None, alias="script")


class StudioEncryptionConfigurationModel(BaseModel):
    key_type: Literal["AWS_OWNED_KEY", "CUSTOMER_MANAGED_KEY"] = Field(alias="keyType")
    key_arn: Optional[str] = Field(default=None, alias="keyArn")


class DeleteLaunchProfileMemberRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    principal_id: str = Field(alias="principalId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteLaunchProfileRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteStreamingImageRequestModel(BaseModel):
    streaming_image_id: str = Field(alias="streamingImageId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteStreamingSessionRequestModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteStudioComponentRequestModel(BaseModel):
    studio_component_id: str = Field(alias="studioComponentId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteStudioMemberRequestModel(BaseModel):
    principal_id: str = Field(alias="principalId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class DeleteStudioRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class EulaModel(BaseModel):
    content: Optional[str] = Field(default=None, alias="content")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    eula_id: Optional[str] = Field(default=None, alias="eulaId")
    name: Optional[str] = Field(default=None, alias="name")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class GetEulaRequestModel(BaseModel):
    eula_id: str = Field(alias="eulaId")


class GetLaunchProfileDetailsRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")


class StudioComponentSummaryModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")
    studio_component_id: Optional[str] = Field(default=None, alias="studioComponentId")
    subtype: Optional[
        Literal[
            "AMAZON_FSX_FOR_LUSTRE",
            "AMAZON_FSX_FOR_WINDOWS",
            "AWS_MANAGED_MICROSOFT_AD",
            "CUSTOM",
        ]
    ] = Field(default=None, alias="subtype")
    type: Optional[
        Literal[
            "ACTIVE_DIRECTORY",
            "COMPUTE_FARM",
            "CUSTOM",
            "LICENSE_SERVICE",
            "SHARED_FILE_SYSTEM",
        ]
    ] = Field(default=None, alias="type")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    updated_by: Optional[str] = Field(default=None, alias="updatedBy")


class GetLaunchProfileInitializationRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    launch_profile_protocol_versions: Sequence[str] = Field(
        alias="launchProfileProtocolVersions"
    )
    launch_purpose: str = Field(alias="launchPurpose")
    platform: str = Field(alias="platform")
    studio_id: str = Field(alias="studioId")


class GetLaunchProfileMemberRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    principal_id: str = Field(alias="principalId")
    studio_id: str = Field(alias="studioId")


class LaunchProfileMembershipModel(BaseModel):
    identity_store_id: Optional[str] = Field(default=None, alias="identityStoreId")
    persona: Optional[Literal["USER"]] = Field(default=None, alias="persona")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    sid: Optional[str] = Field(default=None, alias="sid")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class GetLaunchProfileRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")


class GetStreamingImageRequestModel(BaseModel):
    streaming_image_id: str = Field(alias="streamingImageId")
    studio_id: str = Field(alias="studioId")


class GetStreamingSessionBackupRequestModel(BaseModel):
    backup_id: str = Field(alias="backupId")
    studio_id: str = Field(alias="studioId")


class StreamingSessionBackupModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    backup_id: Optional[str] = Field(default=None, alias="backupId")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    launch_profile_id: Optional[str] = Field(default=None, alias="launchProfileId")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    session_id: Optional[str] = Field(default=None, alias="sessionId")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETED",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "READY",
            "START_FAILED",
            "START_IN_PROGRESS",
            "STOPPED",
            "STOP_FAILED",
            "STOP_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="state")
    status_code: Optional[
        Literal[
            "ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR",
            "AMI_VALIDATION_ERROR",
            "DECRYPT_STREAMING_IMAGE_ERROR",
            "INITIALIZATION_SCRIPT_ERROR",
            "INSUFFICIENT_CAPACITY",
            "INTERNAL_ERROR",
            "NETWORK_CONNECTION_ERROR",
            "NETWORK_INTERFACE_ERROR",
            "STREAMING_SESSION_CREATE_IN_PROGRESS",
            "STREAMING_SESSION_DELETED",
            "STREAMING_SESSION_DELETE_IN_PROGRESS",
            "STREAMING_SESSION_READY",
            "STREAMING_SESSION_STARTED",
            "STREAMING_SESSION_START_IN_PROGRESS",
            "STREAMING_SESSION_STOPPED",
            "STREAMING_SESSION_STOP_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="statusCode")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class GetStreamingSessionRequestModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")


class GetStreamingSessionStreamRequestModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    stream_id: str = Field(alias="streamId")
    studio_id: str = Field(alias="studioId")


class GetStudioComponentRequestModel(BaseModel):
    studio_component_id: str = Field(alias="studioComponentId")
    studio_id: str = Field(alias="studioId")


class GetStudioMemberRequestModel(BaseModel):
    principal_id: str = Field(alias="principalId")
    studio_id: str = Field(alias="studioId")


class StudioMembershipModel(BaseModel):
    identity_store_id: Optional[str] = Field(default=None, alias="identityStoreId")
    persona: Optional[Literal["ADMINISTRATOR"]] = Field(default=None, alias="persona")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    sid: Optional[str] = Field(default=None, alias="sid")


class GetStudioRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")


class LaunchProfileInitializationScriptModel(BaseModel):
    runtime_role_arn: Optional[str] = Field(default=None, alias="runtimeRoleArn")
    script: Optional[str] = Field(default=None, alias="script")
    secure_initialization_role_arn: Optional[str] = Field(
        default=None, alias="secureInitializationRoleArn"
    )
    studio_component_id: Optional[str] = Field(default=None, alias="studioComponentId")
    studio_component_name: Optional[str] = Field(
        default=None, alias="studioComponentName"
    )


class ValidationResultModel(BaseModel):
    state: Literal[
        "VALIDATION_FAILED",
        "VALIDATION_FAILED_INTERNAL_SERVER_ERROR",
        "VALIDATION_IN_PROGRESS",
        "VALIDATION_NOT_STARTED",
        "VALIDATION_SUCCESS",
    ] = Field(alias="state")
    status_code: Literal[
        "VALIDATION_FAILED_INTERNAL_SERVER_ERROR",
        "VALIDATION_FAILED_INVALID_ACTIVE_DIRECTORY",
        "VALIDATION_FAILED_INVALID_SECURITY_GROUP_ASSOCIATION",
        "VALIDATION_FAILED_INVALID_SUBNET_ROUTE_TABLE_ASSOCIATION",
        "VALIDATION_FAILED_SUBNET_NOT_FOUND",
        "VALIDATION_FAILED_UNAUTHORIZED",
        "VALIDATION_IN_PROGRESS",
        "VALIDATION_NOT_STARTED",
        "VALIDATION_SUCCESS",
    ] = Field(alias="statusCode")
    status_message: str = Field(alias="statusMessage")
    type: Literal[
        "VALIDATE_ACTIVE_DIRECTORY_STUDIO_COMPONENT",
        "VALIDATE_NETWORK_ACL_ASSOCIATION",
        "VALIDATE_SECURITY_GROUP_ASSOCIATION",
        "VALIDATE_SUBNET_ASSOCIATION",
    ] = Field(alias="type")


class LicenseServiceConfigurationModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="endpoint")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListEulaAcceptancesRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    eula_ids: Optional[Sequence[str]] = Field(default=None, alias="eulaIds")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListEulasRequestModel(BaseModel):
    eula_ids: Optional[Sequence[str]] = Field(default=None, alias="eulaIds")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListLaunchProfileMembersRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListLaunchProfilesRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    states: Optional[
        Sequence[
            Literal[
                "CREATE_FAILED",
                "CREATE_IN_PROGRESS",
                "DELETED",
                "DELETE_FAILED",
                "DELETE_IN_PROGRESS",
                "READY",
                "UPDATE_FAILED",
                "UPDATE_IN_PROGRESS",
            ]
        ]
    ] = Field(default=None, alias="states")


class ListStreamingImagesRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    owner: Optional[str] = Field(default=None, alias="owner")


class ListStreamingSessionBackupsRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")


class ListStreamingSessionsRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    session_ids: Optional[str] = Field(default=None, alias="sessionIds")


class ListStudioComponentsRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    states: Optional[
        Sequence[
            Literal[
                "CREATE_FAILED",
                "CREATE_IN_PROGRESS",
                "DELETED",
                "DELETE_FAILED",
                "DELETE_IN_PROGRESS",
                "READY",
                "UPDATE_FAILED",
                "UPDATE_IN_PROGRESS",
            ]
        ]
    ] = Field(default=None, alias="states")
    types: Optional[
        Sequence[
            Literal[
                "ACTIVE_DIRECTORY",
                "COMPUTE_FARM",
                "CUSTOM",
                "LICENSE_SERVICE",
                "SHARED_FILE_SYSTEM",
            ]
        ]
    ] = Field(default=None, alias="types")


class ListStudioMembersRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListStudiosRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class NewLaunchProfileMemberModel(BaseModel):
    persona: Literal["USER"] = Field(alias="persona")
    principal_id: str = Field(alias="principalId")


class NewStudioMemberModel(BaseModel):
    persona: Literal["ADMINISTRATOR"] = Field(alias="persona")
    principal_id: str = Field(alias="principalId")


class SharedFileSystemConfigurationModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="endpoint")
    file_system_id: Optional[str] = Field(default=None, alias="fileSystemId")
    linux_mount_point: Optional[str] = Field(default=None, alias="linuxMountPoint")
    share_name: Optional[str] = Field(default=None, alias="shareName")
    windows_mount_drive: Optional[str] = Field(default=None, alias="windowsMountDrive")


class StartStreamingSessionRequestModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")
    backup_id: Optional[str] = Field(default=None, alias="backupId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class StartStudioSSOConfigurationRepairRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class StopStreamingSessionRequestModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    volume_retention_mode: Optional[Literal["DELETE", "RETAIN"]] = Field(
        default=None, alias="volumeRetentionMode"
    )


class StreamConfigurationSessionBackupModel(BaseModel):
    max_backups_to_retain: Optional[int] = Field(
        default=None, alias="maxBackupsToRetain"
    )
    mode: Optional[Literal["AUTOMATIC", "DEACTIVATED"]] = Field(
        default=None, alias="mode"
    )


class VolumeConfigurationModel(BaseModel):
    iops: Optional[int] = Field(default=None, alias="iops")
    size: Optional[int] = Field(default=None, alias="size")
    throughput: Optional[int] = Field(default=None, alias="throughput")


class StreamingSessionStorageRootModel(BaseModel):
    linux: Optional[str] = Field(default=None, alias="linux")
    windows: Optional[str] = Field(default=None, alias="windows")


class StreamingImageEncryptionConfigurationModel(BaseModel):
    key_type: Literal["CUSTOMER_MANAGED_KEY"] = Field(alias="keyType")
    key_arn: Optional[str] = Field(default=None, alias="keyArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateLaunchProfileMemberRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    persona: Literal["USER"] = Field(alias="persona")
    principal_id: str = Field(alias="principalId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateStreamingImageRequestModel(BaseModel):
    streaming_image_id: str = Field(alias="streamingImageId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[str] = Field(default=None, alias="name")


class UpdateStudioRequestModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    admin_role_arn: Optional[str] = Field(default=None, alias="adminRoleArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    user_role_arn: Optional[str] = Field(default=None, alias="userRoleArn")


class AcceptEulasResponseModel(BaseModel):
    eula_acceptances: List[EulaAcceptanceModel] = Field(alias="eulaAcceptances")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEulaAcceptancesResponseModel(BaseModel):
    eula_acceptances: List[EulaAcceptanceModel] = Field(alias="eulaAcceptances")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActiveDirectoryConfigurationModel(BaseModel):
    computer_attributes: Optional[
        Sequence[ActiveDirectoryComputerAttributeModel]
    ] = Field(default=None, alias="computerAttributes")
    directory_id: Optional[str] = Field(default=None, alias="directoryId")
    organizational_unit_distinguished_name: Optional[str] = Field(
        default=None, alias="organizationalUnitDistinguishedName"
    )


class LaunchProfileInitializationActiveDirectoryModel(BaseModel):
    computer_attributes: Optional[List[ActiveDirectoryComputerAttributeModel]] = Field(
        default=None, alias="computerAttributes"
    )
    directory_id: Optional[str] = Field(default=None, alias="directoryId")
    directory_name: Optional[str] = Field(default=None, alias="directoryName")
    dns_ip_addresses: Optional[List[str]] = Field(default=None, alias="dnsIpAddresses")
    organizational_unit_distinguished_name: Optional[str] = Field(
        default=None, alias="organizationalUnitDistinguishedName"
    )
    studio_component_id: Optional[str] = Field(default=None, alias="studioComponentId")
    studio_component_name: Optional[str] = Field(
        default=None, alias="studioComponentName"
    )


class CreateStreamingSessionStreamResponseModel(BaseModel):
    stream: StreamingSessionStreamModel = Field(alias="stream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStreamingSessionStreamResponseModel(BaseModel):
    stream: StreamingSessionStreamModel = Field(alias="stream")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStudioRequestModel(BaseModel):
    admin_role_arn: str = Field(alias="adminRoleArn")
    display_name: str = Field(alias="displayName")
    studio_name: str = Field(alias="studioName")
    user_role_arn: str = Field(alias="userRoleArn")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    studio_encryption_configuration: Optional[
        StudioEncryptionConfigurationModel
    ] = Field(default=None, alias="studioEncryptionConfiguration")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class StudioModel(BaseModel):
    admin_role_arn: Optional[str] = Field(default=None, alias="adminRoleArn")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    home_region: Optional[str] = Field(default=None, alias="homeRegion")
    sso_client_id: Optional[str] = Field(default=None, alias="ssoClientId")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETED",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "READY",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="state")
    status_code: Optional[
        Literal[
            "AWS_SSO_ACCESS_DENIED",
            "AWS_SSO_CONFIGURATION_REPAIRED",
            "AWS_SSO_CONFIGURATION_REPAIR_IN_PROGRESS",
            "AWS_SSO_NOT_ENABLED",
            "AWS_STS_REGION_DISABLED",
            "ENCRYPTION_KEY_ACCESS_DENIED",
            "ENCRYPTION_KEY_NOT_FOUND",
            "INTERNAL_ERROR",
            "ROLE_COULD_NOT_BE_ASSUMED",
            "ROLE_NOT_OWNED_BY_STUDIO_OWNER",
            "STUDIO_CREATED",
            "STUDIO_CREATE_IN_PROGRESS",
            "STUDIO_DELETED",
            "STUDIO_DELETE_IN_PROGRESS",
            "STUDIO_UPDATED",
            "STUDIO_UPDATE_IN_PROGRESS",
            "STUDIO_WITH_LAUNCH_PROFILES_NOT_DELETED",
            "STUDIO_WITH_STREAMING_IMAGES_NOT_DELETED",
            "STUDIO_WITH_STUDIO_COMPONENTS_NOT_DELETED",
        ]
    ] = Field(default=None, alias="statusCode")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    studio_encryption_configuration: Optional[
        StudioEncryptionConfigurationModel
    ] = Field(default=None, alias="studioEncryptionConfiguration")
    studio_id: Optional[str] = Field(default=None, alias="studioId")
    studio_name: Optional[str] = Field(default=None, alias="studioName")
    studio_url: Optional[str] = Field(default=None, alias="studioUrl")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    user_role_arn: Optional[str] = Field(default=None, alias="userRoleArn")


class GetEulaResponseModel(BaseModel):
    eula: EulaModel = Field(alias="eula")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEulasResponseModel(BaseModel):
    eulas: List[EulaModel] = Field(alias="eulas")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLaunchProfileMemberResponseModel(BaseModel):
    member: LaunchProfileMembershipModel = Field(alias="member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLaunchProfileMembersResponseModel(BaseModel):
    members: List[LaunchProfileMembershipModel] = Field(alias="members")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLaunchProfileMemberResponseModel(BaseModel):
    member: LaunchProfileMembershipModel = Field(alias="member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLaunchProfileRequestLaunchProfileDeletedWaitModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetLaunchProfileRequestLaunchProfileReadyWaitModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingImageRequestStreamingImageDeletedWaitModel(BaseModel):
    streaming_image_id: str = Field(alias="streamingImageId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingImageRequestStreamingImageReadyWaitModel(BaseModel):
    streaming_image_id: str = Field(alias="streamingImageId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingSessionRequestStreamingSessionDeletedWaitModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingSessionRequestStreamingSessionReadyWaitModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingSessionRequestStreamingSessionStoppedWaitModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingSessionStreamRequestStreamingSessionStreamReadyWaitModel(BaseModel):
    session_id: str = Field(alias="sessionId")
    stream_id: str = Field(alias="streamId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStudioComponentRequestStudioComponentDeletedWaitModel(BaseModel):
    studio_component_id: str = Field(alias="studioComponentId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStudioComponentRequestStudioComponentReadyWaitModel(BaseModel):
    studio_component_id: str = Field(alias="studioComponentId")
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStudioRequestStudioDeletedWaitModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStudioRequestStudioReadyWaitModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class GetStreamingSessionBackupResponseModel(BaseModel):
    streaming_session_backup: StreamingSessionBackupModel = Field(
        alias="streamingSessionBackup"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamingSessionBackupsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    streaming_session_backups: List[StreamingSessionBackupModel] = Field(
        alias="streamingSessionBackups"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStudioMemberResponseModel(BaseModel):
    member: StudioMembershipModel = Field(alias="member")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStudioMembersResponseModel(BaseModel):
    members: List[StudioMembershipModel] = Field(alias="members")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListEulaAcceptancesRequestListEulaAcceptancesPaginateModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    eula_ids: Optional[Sequence[str]] = Field(default=None, alias="eulaIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEulasRequestListEulasPaginateModel(BaseModel):
    eula_ids: Optional[Sequence[str]] = Field(default=None, alias="eulaIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLaunchProfileMembersRequestListLaunchProfileMembersPaginateModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLaunchProfilesRequestListLaunchProfilesPaginateModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    principal_id: Optional[str] = Field(default=None, alias="principalId")
    states: Optional[
        Sequence[
            Literal[
                "CREATE_FAILED",
                "CREATE_IN_PROGRESS",
                "DELETED",
                "DELETE_FAILED",
                "DELETE_IN_PROGRESS",
                "READY",
                "UPDATE_FAILED",
                "UPDATE_IN_PROGRESS",
            ]
        ]
    ] = Field(default=None, alias="states")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamingImagesRequestListStreamingImagesPaginateModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    owner: Optional[str] = Field(default=None, alias="owner")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamingSessionBackupsRequestListStreamingSessionBackupsPaginateModel(
    BaseModel
):
    studio_id: str = Field(alias="studioId")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamingSessionsRequestListStreamingSessionsPaginateModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    session_ids: Optional[str] = Field(default=None, alias="sessionIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStudioComponentsRequestListStudioComponentsPaginateModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    states: Optional[
        Sequence[
            Literal[
                "CREATE_FAILED",
                "CREATE_IN_PROGRESS",
                "DELETED",
                "DELETE_FAILED",
                "DELETE_IN_PROGRESS",
                "READY",
                "UPDATE_FAILED",
                "UPDATE_IN_PROGRESS",
            ]
        ]
    ] = Field(default=None, alias="states")
    types: Optional[
        Sequence[
            Literal[
                "ACTIVE_DIRECTORY",
                "COMPUTE_FARM",
                "CUSTOM",
                "LICENSE_SERVICE",
                "SHARED_FILE_SYSTEM",
            ]
        ]
    ] = Field(default=None, alias="types")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStudioMembersRequestListStudioMembersPaginateModel(BaseModel):
    studio_id: str = Field(alias="studioId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStudiosRequestListStudiosPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class PutLaunchProfileMembersRequestModel(BaseModel):
    identity_store_id: str = Field(alias="identityStoreId")
    launch_profile_id: str = Field(alias="launchProfileId")
    members: Sequence[NewLaunchProfileMemberModel] = Field(alias="members")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class PutStudioMembersRequestModel(BaseModel):
    identity_store_id: str = Field(alias="identityStoreId")
    members: Sequence[NewStudioMemberModel] = Field(alias="members")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class StreamingSessionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    automatic_termination_mode: Optional[Literal["ACTIVATED", "DEACTIVATED"]] = Field(
        default=None, alias="automaticTerminationMode"
    )
    backup_mode: Optional[Literal["AUTOMATIC", "DEACTIVATED"]] = Field(
        default=None, alias="backupMode"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    ec2_instance_type: Optional[str] = Field(default=None, alias="ec2InstanceType")
    launch_profile_id: Optional[str] = Field(default=None, alias="launchProfileId")
    max_backups_to_retain: Optional[int] = Field(
        default=None, alias="maxBackupsToRetain"
    )
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    session_id: Optional[str] = Field(default=None, alias="sessionId")
    session_persistence_mode: Optional[Literal["ACTIVATED", "DEACTIVATED"]] = Field(
        default=None, alias="sessionPersistenceMode"
    )
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    started_by: Optional[str] = Field(default=None, alias="startedBy")
    started_from_backup_id: Optional[str] = Field(
        default=None, alias="startedFromBackupId"
    )
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETED",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "READY",
            "START_FAILED",
            "START_IN_PROGRESS",
            "STOPPED",
            "STOP_FAILED",
            "STOP_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="state")
    status_code: Optional[
        Literal[
            "ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR",
            "AMI_VALIDATION_ERROR",
            "DECRYPT_STREAMING_IMAGE_ERROR",
            "INITIALIZATION_SCRIPT_ERROR",
            "INSUFFICIENT_CAPACITY",
            "INTERNAL_ERROR",
            "NETWORK_CONNECTION_ERROR",
            "NETWORK_INTERFACE_ERROR",
            "STREAMING_SESSION_CREATE_IN_PROGRESS",
            "STREAMING_SESSION_DELETED",
            "STREAMING_SESSION_DELETE_IN_PROGRESS",
            "STREAMING_SESSION_READY",
            "STREAMING_SESSION_STARTED",
            "STREAMING_SESSION_START_IN_PROGRESS",
            "STREAMING_SESSION_STOPPED",
            "STREAMING_SESSION_STOP_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="statusCode")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    stop_at: Optional[datetime] = Field(default=None, alias="stopAt")
    stopped_at: Optional[datetime] = Field(default=None, alias="stoppedAt")
    stopped_by: Optional[str] = Field(default=None, alias="stoppedBy")
    streaming_image_id: Optional[str] = Field(default=None, alias="streamingImageId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    terminate_at: Optional[datetime] = Field(default=None, alias="terminateAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    updated_by: Optional[str] = Field(default=None, alias="updatedBy")
    volume_configuration: Optional[VolumeConfigurationModel] = Field(
        default=None, alias="volumeConfiguration"
    )
    volume_retention_mode: Optional[Literal["DELETE", "RETAIN"]] = Field(
        default=None, alias="volumeRetentionMode"
    )


class StreamConfigurationSessionStorageModel(BaseModel):
    mode: Sequence[Literal["UPLOAD"]] = Field(alias="mode")
    root: Optional[StreamingSessionStorageRootModel] = Field(default=None, alias="root")


class StreamingImageModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    description: Optional[str] = Field(default=None, alias="description")
    ec2_image_id: Optional[str] = Field(default=None, alias="ec2ImageId")
    encryption_configuration: Optional[
        StreamingImageEncryptionConfigurationModel
    ] = Field(default=None, alias="encryptionConfiguration")
    eula_ids: Optional[List[str]] = Field(default=None, alias="eulaIds")
    name: Optional[str] = Field(default=None, alias="name")
    owner: Optional[str] = Field(default=None, alias="owner")
    platform: Optional[str] = Field(default=None, alias="platform")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETED",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "READY",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="state")
    status_code: Optional[
        Literal[
            "ACCESS_DENIED",
            "INTERNAL_ERROR",
            "STREAMING_IMAGE_CREATE_IN_PROGRESS",
            "STREAMING_IMAGE_DELETED",
            "STREAMING_IMAGE_DELETE_IN_PROGRESS",
            "STREAMING_IMAGE_READY",
            "STREAMING_IMAGE_UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="statusCode")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    streaming_image_id: Optional[str] = Field(default=None, alias="streamingImageId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class StudioComponentConfigurationModel(BaseModel):
    active_directory_configuration: Optional[ActiveDirectoryConfigurationModel] = Field(
        default=None, alias="activeDirectoryConfiguration"
    )
    compute_farm_configuration: Optional[ComputeFarmConfigurationModel] = Field(
        default=None, alias="computeFarmConfiguration"
    )
    license_service_configuration: Optional[LicenseServiceConfigurationModel] = Field(
        default=None, alias="licenseServiceConfiguration"
    )
    shared_file_system_configuration: Optional[
        SharedFileSystemConfigurationModel
    ] = Field(default=None, alias="sharedFileSystemConfiguration")


class LaunchProfileInitializationModel(BaseModel):
    active_directory: Optional[LaunchProfileInitializationActiveDirectoryModel] = Field(
        default=None, alias="activeDirectory"
    )
    ec2_security_group_ids: Optional[List[str]] = Field(
        default=None, alias="ec2SecurityGroupIds"
    )
    launch_profile_id: Optional[str] = Field(default=None, alias="launchProfileId")
    launch_profile_protocol_version: Optional[str] = Field(
        default=None, alias="launchProfileProtocolVersion"
    )
    launch_purpose: Optional[str] = Field(default=None, alias="launchPurpose")
    name: Optional[str] = Field(default=None, alias="name")
    platform: Optional[Literal["LINUX", "WINDOWS"]] = Field(
        default=None, alias="platform"
    )
    system_initialization_scripts: Optional[
        List[LaunchProfileInitializationScriptModel]
    ] = Field(default=None, alias="systemInitializationScripts")
    user_initialization_scripts: Optional[
        List[LaunchProfileInitializationScriptModel]
    ] = Field(default=None, alias="userInitializationScripts")


class CreateStudioResponseModel(BaseModel):
    studio: StudioModel = Field(alias="studio")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteStudioResponseModel(BaseModel):
    studio: StudioModel = Field(alias="studio")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStudioResponseModel(BaseModel):
    studio: StudioModel = Field(alias="studio")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStudiosResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    studios: List[StudioModel] = Field(alias="studios")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartStudioSSOConfigurationRepairResponseModel(BaseModel):
    studio: StudioModel = Field(alias="studio")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStudioResponseModel(BaseModel):
    studio: StudioModel = Field(alias="studio")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamingSessionResponseModel(BaseModel):
    session: StreamingSessionModel = Field(alias="session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteStreamingSessionResponseModel(BaseModel):
    session: StreamingSessionModel = Field(alias="session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStreamingSessionResponseModel(BaseModel):
    session: StreamingSessionModel = Field(alias="session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamingSessionsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    sessions: List[StreamingSessionModel] = Field(alias="sessions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartStreamingSessionResponseModel(BaseModel):
    session: StreamingSessionModel = Field(alias="session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopStreamingSessionResponseModel(BaseModel):
    session: StreamingSessionModel = Field(alias="session")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamConfigurationCreateModel(BaseModel):
    clipboard_mode: Literal["DISABLED", "ENABLED"] = Field(alias="clipboardMode")
    ec2_instance_types: Sequence[
        Literal[
            "g3.4xlarge",
            "g3s.xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.xlarge",
            "g5.16xlarge",
            "g5.2xlarge",
            "g5.4xlarge",
            "g5.8xlarge",
            "g5.xlarge",
        ]
    ] = Field(alias="ec2InstanceTypes")
    streaming_image_ids: Sequence[str] = Field(alias="streamingImageIds")
    automatic_termination_mode: Optional[Literal["ACTIVATED", "DEACTIVATED"]] = Field(
        default=None, alias="automaticTerminationMode"
    )
    max_session_length_in_minutes: Optional[int] = Field(
        default=None, alias="maxSessionLengthInMinutes"
    )
    max_stopped_session_length_in_minutes: Optional[int] = Field(
        default=None, alias="maxStoppedSessionLengthInMinutes"
    )
    session_backup: Optional[StreamConfigurationSessionBackupModel] = Field(
        default=None, alias="sessionBackup"
    )
    session_persistence_mode: Optional[Literal["ACTIVATED", "DEACTIVATED"]] = Field(
        default=None, alias="sessionPersistenceMode"
    )
    session_storage: Optional[StreamConfigurationSessionStorageModel] = Field(
        default=None, alias="sessionStorage"
    )
    volume_configuration: Optional[VolumeConfigurationModel] = Field(
        default=None, alias="volumeConfiguration"
    )


class StreamConfigurationModel(BaseModel):
    clipboard_mode: Literal["DISABLED", "ENABLED"] = Field(alias="clipboardMode")
    ec2_instance_types: List[
        Literal[
            "g3.4xlarge",
            "g3s.xlarge",
            "g4dn.12xlarge",
            "g4dn.16xlarge",
            "g4dn.2xlarge",
            "g4dn.4xlarge",
            "g4dn.8xlarge",
            "g4dn.xlarge",
            "g5.16xlarge",
            "g5.2xlarge",
            "g5.4xlarge",
            "g5.8xlarge",
            "g5.xlarge",
        ]
    ] = Field(alias="ec2InstanceTypes")
    streaming_image_ids: List[str] = Field(alias="streamingImageIds")
    automatic_termination_mode: Optional[Literal["ACTIVATED", "DEACTIVATED"]] = Field(
        default=None, alias="automaticTerminationMode"
    )
    max_session_length_in_minutes: Optional[int] = Field(
        default=None, alias="maxSessionLengthInMinutes"
    )
    max_stopped_session_length_in_minutes: Optional[int] = Field(
        default=None, alias="maxStoppedSessionLengthInMinutes"
    )
    session_backup: Optional[StreamConfigurationSessionBackupModel] = Field(
        default=None, alias="sessionBackup"
    )
    session_persistence_mode: Optional[Literal["ACTIVATED", "DEACTIVATED"]] = Field(
        default=None, alias="sessionPersistenceMode"
    )
    session_storage: Optional[StreamConfigurationSessionStorageModel] = Field(
        default=None, alias="sessionStorage"
    )
    volume_configuration: Optional[VolumeConfigurationModel] = Field(
        default=None, alias="volumeConfiguration"
    )


class CreateStreamingImageResponseModel(BaseModel):
    streaming_image: StreamingImageModel = Field(alias="streamingImage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteStreamingImageResponseModel(BaseModel):
    streaming_image: StreamingImageModel = Field(alias="streamingImage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStreamingImageResponseModel(BaseModel):
    streaming_image: StreamingImageModel = Field(alias="streamingImage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamingImagesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    streaming_images: List[StreamingImageModel] = Field(alias="streamingImages")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStreamingImageResponseModel(BaseModel):
    streaming_image: StreamingImageModel = Field(alias="streamingImage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStudioComponentRequestModel(BaseModel):
    name: str = Field(alias="name")
    studio_id: str = Field(alias="studioId")
    type: Literal[
        "ACTIVE_DIRECTORY",
        "COMPUTE_FARM",
        "CUSTOM",
        "LICENSE_SERVICE",
        "SHARED_FILE_SYSTEM",
    ] = Field(alias="type")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    configuration: Optional[StudioComponentConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    description: Optional[str] = Field(default=None, alias="description")
    ec2_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ec2SecurityGroupIds"
    )
    initialization_scripts: Optional[
        Sequence[StudioComponentInitializationScriptModel]
    ] = Field(default=None, alias="initializationScripts")
    runtime_role_arn: Optional[str] = Field(default=None, alias="runtimeRoleArn")
    script_parameters: Optional[Sequence[ScriptParameterKeyValueModel]] = Field(
        default=None, alias="scriptParameters"
    )
    secure_initialization_role_arn: Optional[str] = Field(
        default=None, alias="secureInitializationRoleArn"
    )
    subtype: Optional[
        Literal[
            "AMAZON_FSX_FOR_LUSTRE",
            "AMAZON_FSX_FOR_WINDOWS",
            "AWS_MANAGED_MICROSOFT_AD",
            "CUSTOM",
        ]
    ] = Field(default=None, alias="subtype")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class StudioComponentModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    configuration: Optional[StudioComponentConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    description: Optional[str] = Field(default=None, alias="description")
    ec2_security_group_ids: Optional[List[str]] = Field(
        default=None, alias="ec2SecurityGroupIds"
    )
    initialization_scripts: Optional[
        List[StudioComponentInitializationScriptModel]
    ] = Field(default=None, alias="initializationScripts")
    name: Optional[str] = Field(default=None, alias="name")
    runtime_role_arn: Optional[str] = Field(default=None, alias="runtimeRoleArn")
    script_parameters: Optional[List[ScriptParameterKeyValueModel]] = Field(
        default=None, alias="scriptParameters"
    )
    secure_initialization_role_arn: Optional[str] = Field(
        default=None, alias="secureInitializationRoleArn"
    )
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETED",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "READY",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="state")
    status_code: Optional[
        Literal[
            "ACTIVE_DIRECTORY_ALREADY_EXISTS",
            "ENCRYPTION_KEY_ACCESS_DENIED",
            "ENCRYPTION_KEY_NOT_FOUND",
            "INTERNAL_ERROR",
            "STUDIO_COMPONENT_CREATED",
            "STUDIO_COMPONENT_CREATE_IN_PROGRESS",
            "STUDIO_COMPONENT_DELETED",
            "STUDIO_COMPONENT_DELETE_IN_PROGRESS",
            "STUDIO_COMPONENT_UPDATED",
            "STUDIO_COMPONENT_UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="statusCode")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    studio_component_id: Optional[str] = Field(default=None, alias="studioComponentId")
    subtype: Optional[
        Literal[
            "AMAZON_FSX_FOR_LUSTRE",
            "AMAZON_FSX_FOR_WINDOWS",
            "AWS_MANAGED_MICROSOFT_AD",
            "CUSTOM",
        ]
    ] = Field(default=None, alias="subtype")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    type: Optional[
        Literal[
            "ACTIVE_DIRECTORY",
            "COMPUTE_FARM",
            "CUSTOM",
            "LICENSE_SERVICE",
            "SHARED_FILE_SYSTEM",
        ]
    ] = Field(default=None, alias="type")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    updated_by: Optional[str] = Field(default=None, alias="updatedBy")


class UpdateStudioComponentRequestModel(BaseModel):
    studio_component_id: str = Field(alias="studioComponentId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    configuration: Optional[StudioComponentConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    description: Optional[str] = Field(default=None, alias="description")
    ec2_security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ec2SecurityGroupIds"
    )
    initialization_scripts: Optional[
        Sequence[StudioComponentInitializationScriptModel]
    ] = Field(default=None, alias="initializationScripts")
    name: Optional[str] = Field(default=None, alias="name")
    runtime_role_arn: Optional[str] = Field(default=None, alias="runtimeRoleArn")
    script_parameters: Optional[Sequence[ScriptParameterKeyValueModel]] = Field(
        default=None, alias="scriptParameters"
    )
    secure_initialization_role_arn: Optional[str] = Field(
        default=None, alias="secureInitializationRoleArn"
    )
    subtype: Optional[
        Literal[
            "AMAZON_FSX_FOR_LUSTRE",
            "AMAZON_FSX_FOR_WINDOWS",
            "AWS_MANAGED_MICROSOFT_AD",
            "CUSTOM",
        ]
    ] = Field(default=None, alias="subtype")
    type: Optional[
        Literal[
            "ACTIVE_DIRECTORY",
            "COMPUTE_FARM",
            "CUSTOM",
            "LICENSE_SERVICE",
            "SHARED_FILE_SYSTEM",
        ]
    ] = Field(default=None, alias="type")


class GetLaunchProfileInitializationResponseModel(BaseModel):
    launch_profile_initialization: LaunchProfileInitializationModel = Field(
        alias="launchProfileInitialization"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLaunchProfileRequestModel(BaseModel):
    ec2_subnet_ids: Sequence[str] = Field(alias="ec2SubnetIds")
    launch_profile_protocol_versions: Sequence[str] = Field(
        alias="launchProfileProtocolVersions"
    )
    name: str = Field(alias="name")
    stream_configuration: StreamConfigurationCreateModel = Field(
        alias="streamConfiguration"
    )
    studio_component_ids: Sequence[str] = Field(alias="studioComponentIds")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateLaunchProfileRequestModel(BaseModel):
    launch_profile_id: str = Field(alias="launchProfileId")
    studio_id: str = Field(alias="studioId")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    description: Optional[str] = Field(default=None, alias="description")
    launch_profile_protocol_versions: Optional[Sequence[str]] = Field(
        default=None, alias="launchProfileProtocolVersions"
    )
    name: Optional[str] = Field(default=None, alias="name")
    stream_configuration: Optional[StreamConfigurationCreateModel] = Field(
        default=None, alias="streamConfiguration"
    )
    studio_component_ids: Optional[Sequence[str]] = Field(
        default=None, alias="studioComponentIds"
    )


class LaunchProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    description: Optional[str] = Field(default=None, alias="description")
    ec2_subnet_ids: Optional[List[str]] = Field(default=None, alias="ec2SubnetIds")
    launch_profile_id: Optional[str] = Field(default=None, alias="launchProfileId")
    launch_profile_protocol_versions: Optional[List[str]] = Field(
        default=None, alias="launchProfileProtocolVersions"
    )
    name: Optional[str] = Field(default=None, alias="name")
    state: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETED",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "READY",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="state")
    status_code: Optional[
        Literal[
            "ENCRYPTION_KEY_ACCESS_DENIED",
            "ENCRYPTION_KEY_NOT_FOUND",
            "INTERNAL_ERROR",
            "INVALID_INSTANCE_TYPES_PROVIDED",
            "INVALID_SUBNETS_COMBINATION",
            "INVALID_SUBNETS_PROVIDED",
            "LAUNCH_PROFILE_CREATED",
            "LAUNCH_PROFILE_CREATE_IN_PROGRESS",
            "LAUNCH_PROFILE_DELETED",
            "LAUNCH_PROFILE_DELETE_IN_PROGRESS",
            "LAUNCH_PROFILE_UPDATED",
            "LAUNCH_PROFILE_UPDATE_IN_PROGRESS",
            "LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED",
            "STREAMING_IMAGE_NOT_FOUND",
            "STREAMING_IMAGE_NOT_READY",
        ]
    ] = Field(default=None, alias="statusCode")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    stream_configuration: Optional[StreamConfigurationModel] = Field(
        default=None, alias="streamConfiguration"
    )
    studio_component_ids: Optional[List[str]] = Field(
        default=None, alias="studioComponentIds"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    updated_by: Optional[str] = Field(default=None, alias="updatedBy")
    validation_results: Optional[List[ValidationResultModel]] = Field(
        default=None, alias="validationResults"
    )


class CreateStudioComponentResponseModel(BaseModel):
    studio_component: StudioComponentModel = Field(alias="studioComponent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteStudioComponentResponseModel(BaseModel):
    studio_component: StudioComponentModel = Field(alias="studioComponent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStudioComponentResponseModel(BaseModel):
    studio_component: StudioComponentModel = Field(alias="studioComponent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStudioComponentsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    studio_components: List[StudioComponentModel] = Field(alias="studioComponents")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStudioComponentResponseModel(BaseModel):
    studio_component: StudioComponentModel = Field(alias="studioComponent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLaunchProfileResponseModel(BaseModel):
    launch_profile: LaunchProfileModel = Field(alias="launchProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteLaunchProfileResponseModel(BaseModel):
    launch_profile: LaunchProfileModel = Field(alias="launchProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLaunchProfileDetailsResponseModel(BaseModel):
    launch_profile: LaunchProfileModel = Field(alias="launchProfile")
    streaming_images: List[StreamingImageModel] = Field(alias="streamingImages")
    studio_component_summaries: List[StudioComponentSummaryModel] = Field(
        alias="studioComponentSummaries"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLaunchProfileResponseModel(BaseModel):
    launch_profile: LaunchProfileModel = Field(alias="launchProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLaunchProfilesResponseModel(BaseModel):
    launch_profiles: List[LaunchProfileModel] = Field(alias="launchProfiles")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateLaunchProfileResponseModel(BaseModel):
    launch_profile: LaunchProfileModel = Field(alias="launchProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
