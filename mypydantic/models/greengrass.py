# Model Generated: Thu Mar  2 21:56:19 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AssociateRoleToGroupRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    role_arn: str = Field(alias="RoleArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AssociateServiceRoleToAccountRequestModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")


class BulkDeploymentMetricsModel(BaseModel):
    invalid_input_records: Optional[int] = Field(
        default=None, alias="InvalidInputRecords"
    )
    records_processed: Optional[int] = Field(default=None, alias="RecordsProcessed")
    retry_attempts: Optional[int] = Field(default=None, alias="RetryAttempts")


class ErrorDetailModel(BaseModel):
    detailed_error_code: Optional[str] = Field(default=None, alias="DetailedErrorCode")
    detailed_error_message: Optional[str] = Field(
        default=None, alias="DetailedErrorMessage"
    )


class BulkDeploymentModel(BaseModel):
    bulk_deployment_arn: Optional[str] = Field(default=None, alias="BulkDeploymentArn")
    bulk_deployment_id: Optional[str] = Field(default=None, alias="BulkDeploymentId")
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")


class ConnectivityInfoModel(BaseModel):
    host_address: Optional[str] = Field(default=None, alias="HostAddress")
    id: Optional[str] = Field(default=None, alias="Id")
    metadata: Optional[str] = Field(default=None, alias="Metadata")
    port_number: Optional[int] = Field(default=None, alias="PortNumber")


class ConnectorModel(BaseModel):
    connector_arn: str = Field(alias="ConnectorArn")
    id: str = Field(alias="Id")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")


class CoreModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    id: str = Field(alias="Id")
    thing_arn: str = Field(alias="ThingArn")
    sync_shadow: Optional[bool] = Field(default=None, alias="SyncShadow")


class CreateDeploymentRequestModel(BaseModel):
    deployment_type: Literal[
        "ForceResetDeployment", "NewDeployment", "Redeployment", "ResetDeployment"
    ] = Field(alias="DeploymentType")
    group_id: str = Field(alias="GroupId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    group_version_id: Optional[str] = Field(default=None, alias="GroupVersionId")


class DeviceModel(BaseModel):
    certificate_arn: str = Field(alias="CertificateArn")
    id: str = Field(alias="Id")
    thing_arn: str = Field(alias="ThingArn")
    sync_shadow: Optional[bool] = Field(default=None, alias="SyncShadow")


class CreateGroupCertificateAuthorityRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")


class GroupVersionModel(BaseModel):
    connector_definition_version_arn: Optional[str] = Field(
        default=None, alias="ConnectorDefinitionVersionArn"
    )
    core_definition_version_arn: Optional[str] = Field(
        default=None, alias="CoreDefinitionVersionArn"
    )
    device_definition_version_arn: Optional[str] = Field(
        default=None, alias="DeviceDefinitionVersionArn"
    )
    function_definition_version_arn: Optional[str] = Field(
        default=None, alias="FunctionDefinitionVersionArn"
    )
    logger_definition_version_arn: Optional[str] = Field(
        default=None, alias="LoggerDefinitionVersionArn"
    )
    resource_definition_version_arn: Optional[str] = Field(
        default=None, alias="ResourceDefinitionVersionArn"
    )
    subscription_definition_version_arn: Optional[str] = Field(
        default=None, alias="SubscriptionDefinitionVersionArn"
    )


class CreateGroupVersionRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    connector_definition_version_arn: Optional[str] = Field(
        default=None, alias="ConnectorDefinitionVersionArn"
    )
    core_definition_version_arn: Optional[str] = Field(
        default=None, alias="CoreDefinitionVersionArn"
    )
    device_definition_version_arn: Optional[str] = Field(
        default=None, alias="DeviceDefinitionVersionArn"
    )
    function_definition_version_arn: Optional[str] = Field(
        default=None, alias="FunctionDefinitionVersionArn"
    )
    logger_definition_version_arn: Optional[str] = Field(
        default=None, alias="LoggerDefinitionVersionArn"
    )
    resource_definition_version_arn: Optional[str] = Field(
        default=None, alias="ResourceDefinitionVersionArn"
    )
    subscription_definition_version_arn: Optional[str] = Field(
        default=None, alias="SubscriptionDefinitionVersionArn"
    )


class LoggerModel(BaseModel):
    component: Literal["GreengrassSystem", "Lambda"] = Field(alias="Component")
    id: str = Field(alias="Id")
    level: Literal["DEBUG", "ERROR", "FATAL", "INFO", "WARN"] = Field(alias="Level")
    type: Literal["AWSCloudWatch", "FileSystem"] = Field(alias="Type")
    space: Optional[int] = Field(default=None, alias="Space")


class CreateSoftwareUpdateJobRequestModel(BaseModel):
    s3_url_signer_role: str = Field(alias="S3UrlSignerRole")
    software_to_update: Literal["core", "ota_agent"] = Field(alias="SoftwareToUpdate")
    update_targets: Sequence[str] = Field(alias="UpdateTargets")
    update_targets_architecture: Literal[
        "aarch64", "armv6l", "armv7l", "x86_64"
    ] = Field(alias="UpdateTargetsArchitecture")
    update_targets_operating_system: Literal[
        "amazon_linux", "openwrt", "raspbian", "ubuntu"
    ] = Field(alias="UpdateTargetsOperatingSystem")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    update_agent_log_level: Optional[
        Literal["DEBUG", "ERROR", "FATAL", "INFO", "NONE", "TRACE", "VERBOSE", "WARN"]
    ] = Field(default=None, alias="UpdateAgentLogLevel")


class SubscriptionModel(BaseModel):
    id: str = Field(alias="Id")
    source: str = Field(alias="Source")
    subject: str = Field(alias="Subject")
    target: str = Field(alias="Target")


class DefinitionInformationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_timestamp: Optional[str] = Field(default=None, alias="CreationTimestamp")
    id: Optional[str] = Field(default=None, alias="Id")
    last_updated_timestamp: Optional[str] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    latest_version: Optional[str] = Field(default=None, alias="LatestVersion")
    latest_version_arn: Optional[str] = Field(default=None, alias="LatestVersionArn")
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class DeleteConnectorDefinitionRequestModel(BaseModel):
    connector_definition_id: str = Field(alias="ConnectorDefinitionId")


class DeleteCoreDefinitionRequestModel(BaseModel):
    core_definition_id: str = Field(alias="CoreDefinitionId")


class DeleteDeviceDefinitionRequestModel(BaseModel):
    device_definition_id: str = Field(alias="DeviceDefinitionId")


class DeleteFunctionDefinitionRequestModel(BaseModel):
    function_definition_id: str = Field(alias="FunctionDefinitionId")


class DeleteGroupRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")


class DeleteLoggerDefinitionRequestModel(BaseModel):
    logger_definition_id: str = Field(alias="LoggerDefinitionId")


class DeleteResourceDefinitionRequestModel(BaseModel):
    resource_definition_id: str = Field(alias="ResourceDefinitionId")


class DeleteSubscriptionDefinitionRequestModel(BaseModel):
    subscription_definition_id: str = Field(alias="SubscriptionDefinitionId")


class DeploymentModel(BaseModel):
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    deployment_arn: Optional[str] = Field(default=None, alias="DeploymentArn")
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    deployment_type: Optional[
        Literal[
            "ForceResetDeployment", "NewDeployment", "Redeployment", "ResetDeployment"
        ]
    ] = Field(default=None, alias="DeploymentType")
    group_arn: Optional[str] = Field(default=None, alias="GroupArn")


class DisassociateRoleFromGroupRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")


class ResourceAccessPolicyModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    permission: Optional[Literal["ro", "rw"]] = Field(default=None, alias="Permission")


class FunctionRunAsConfigModel(BaseModel):
    gid: Optional[int] = Field(default=None, alias="Gid")
    uid: Optional[int] = Field(default=None, alias="Uid")


class GetAssociatedRoleRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")


class GetBulkDeploymentStatusRequestModel(BaseModel):
    bulk_deployment_id: str = Field(alias="BulkDeploymentId")


class GetConnectivityInfoRequestModel(BaseModel):
    thing_name: str = Field(alias="ThingName")


class GetConnectorDefinitionRequestModel(BaseModel):
    connector_definition_id: str = Field(alias="ConnectorDefinitionId")


class GetConnectorDefinitionVersionRequestModel(BaseModel):
    connector_definition_id: str = Field(alias="ConnectorDefinitionId")
    connector_definition_version_id: str = Field(alias="ConnectorDefinitionVersionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCoreDefinitionRequestModel(BaseModel):
    core_definition_id: str = Field(alias="CoreDefinitionId")


class GetCoreDefinitionVersionRequestModel(BaseModel):
    core_definition_id: str = Field(alias="CoreDefinitionId")
    core_definition_version_id: str = Field(alias="CoreDefinitionVersionId")


class GetDeploymentStatusRequestModel(BaseModel):
    deployment_id: str = Field(alias="DeploymentId")
    group_id: str = Field(alias="GroupId")


class GetDeviceDefinitionRequestModel(BaseModel):
    device_definition_id: str = Field(alias="DeviceDefinitionId")


class GetDeviceDefinitionVersionRequestModel(BaseModel):
    device_definition_id: str = Field(alias="DeviceDefinitionId")
    device_definition_version_id: str = Field(alias="DeviceDefinitionVersionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetFunctionDefinitionRequestModel(BaseModel):
    function_definition_id: str = Field(alias="FunctionDefinitionId")


class GetFunctionDefinitionVersionRequestModel(BaseModel):
    function_definition_id: str = Field(alias="FunctionDefinitionId")
    function_definition_version_id: str = Field(alias="FunctionDefinitionVersionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetGroupCertificateAuthorityRequestModel(BaseModel):
    certificate_authority_id: str = Field(alias="CertificateAuthorityId")
    group_id: str = Field(alias="GroupId")


class GetGroupCertificateConfigurationRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")


class GetGroupRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")


class GetGroupVersionRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    group_version_id: str = Field(alias="GroupVersionId")


class GetLoggerDefinitionRequestModel(BaseModel):
    logger_definition_id: str = Field(alias="LoggerDefinitionId")


class GetLoggerDefinitionVersionRequestModel(BaseModel):
    logger_definition_id: str = Field(alias="LoggerDefinitionId")
    logger_definition_version_id: str = Field(alias="LoggerDefinitionVersionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetResourceDefinitionRequestModel(BaseModel):
    resource_definition_id: str = Field(alias="ResourceDefinitionId")


class GetResourceDefinitionVersionRequestModel(BaseModel):
    resource_definition_id: str = Field(alias="ResourceDefinitionId")
    resource_definition_version_id: str = Field(alias="ResourceDefinitionVersionId")


class GetSubscriptionDefinitionRequestModel(BaseModel):
    subscription_definition_id: str = Field(alias="SubscriptionDefinitionId")


class GetSubscriptionDefinitionVersionRequestModel(BaseModel):
    subscription_definition_id: str = Field(alias="SubscriptionDefinitionId")
    subscription_definition_version_id: str = Field(
        alias="SubscriptionDefinitionVersionId"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetThingRuntimeConfigurationRequestModel(BaseModel):
    thing_name: str = Field(alias="ThingName")


class GroupCertificateAuthorityPropertiesModel(BaseModel):
    group_certificate_authority_arn: Optional[str] = Field(
        default=None, alias="GroupCertificateAuthorityArn"
    )
    group_certificate_authority_id: Optional[str] = Field(
        default=None, alias="GroupCertificateAuthorityId"
    )


class GroupInformationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_timestamp: Optional[str] = Field(default=None, alias="CreationTimestamp")
    id: Optional[str] = Field(default=None, alias="Id")
    last_updated_timestamp: Optional[str] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    latest_version: Optional[str] = Field(default=None, alias="LatestVersion")
    latest_version_arn: Optional[str] = Field(default=None, alias="LatestVersionArn")
    name: Optional[str] = Field(default=None, alias="Name")


class GroupOwnerSettingModel(BaseModel):
    auto_add_group_owner: Optional[bool] = Field(
        default=None, alias="AutoAddGroupOwner"
    )
    group_owner: Optional[str] = Field(default=None, alias="GroupOwner")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBulkDeploymentDetailedReportsRequestModel(BaseModel):
    bulk_deployment_id: str = Field(alias="BulkDeploymentId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListBulkDeploymentsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConnectorDefinitionVersionsRequestModel(BaseModel):
    connector_definition_id: str = Field(alias="ConnectorDefinitionId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class VersionInformationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_timestamp: Optional[str] = Field(default=None, alias="CreationTimestamp")
    id: Optional[str] = Field(default=None, alias="Id")
    version: Optional[str] = Field(default=None, alias="Version")


class ListConnectorDefinitionsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCoreDefinitionVersionsRequestModel(BaseModel):
    core_definition_id: str = Field(alias="CoreDefinitionId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListCoreDefinitionsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDeploymentsRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDeviceDefinitionVersionsRequestModel(BaseModel):
    device_definition_id: str = Field(alias="DeviceDefinitionId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDeviceDefinitionsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFunctionDefinitionVersionsRequestModel(BaseModel):
    function_definition_id: str = Field(alias="FunctionDefinitionId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListFunctionDefinitionsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGroupCertificateAuthoritiesRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")


class ListGroupVersionsRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListGroupsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLoggerDefinitionVersionsRequestModel(BaseModel):
    logger_definition_id: str = Field(alias="LoggerDefinitionId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListLoggerDefinitionsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListResourceDefinitionVersionsRequestModel(BaseModel):
    resource_definition_id: str = Field(alias="ResourceDefinitionId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListResourceDefinitionsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSubscriptionDefinitionVersionsRequestModel(BaseModel):
    subscription_definition_id: str = Field(alias="SubscriptionDefinitionId")
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSubscriptionDefinitionsRequestModel(BaseModel):
    max_results: Optional[str] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ResetDeploymentsRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    force: Optional[bool] = Field(default=None, alias="Force")


class SecretsManagerSecretResourceDataModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="ARN")
    additional_staging_labels_to_download: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalStagingLabelsToDownload"
    )


class ResourceDownloadOwnerSettingModel(BaseModel):
    group_owner: str = Field(alias="GroupOwner")
    group_permission: Literal["ro", "rw"] = Field(alias="GroupPermission")


class TelemetryConfigurationModel(BaseModel):
    telemetry: Literal["Off", "On"] = Field(alias="Telemetry")
    configuration_sync_status: Optional[Literal["InSync", "OutOfSync"]] = Field(
        default=None, alias="ConfigurationSyncStatus"
    )


class StartBulkDeploymentRequestModel(BaseModel):
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    input_file_uri: str = Field(alias="InputFileUri")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class StopBulkDeploymentRequestModel(BaseModel):
    bulk_deployment_id: str = Field(alias="BulkDeploymentId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class TelemetryConfigurationUpdateModel(BaseModel):
    telemetry: Literal["Off", "On"] = Field(alias="Telemetry")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateConnectorDefinitionRequestModel(BaseModel):
    connector_definition_id: str = Field(alias="ConnectorDefinitionId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateCoreDefinitionRequestModel(BaseModel):
    core_definition_id: str = Field(alias="CoreDefinitionId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateDeviceDefinitionRequestModel(BaseModel):
    device_definition_id: str = Field(alias="DeviceDefinitionId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateFunctionDefinitionRequestModel(BaseModel):
    function_definition_id: str = Field(alias="FunctionDefinitionId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateGroupCertificateConfigurationRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    certificate_expiry_in_milliseconds: Optional[str] = Field(
        default=None, alias="CertificateExpiryInMilliseconds"
    )


class UpdateGroupRequestModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateLoggerDefinitionRequestModel(BaseModel):
    logger_definition_id: str = Field(alias="LoggerDefinitionId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateResourceDefinitionRequestModel(BaseModel):
    resource_definition_id: str = Field(alias="ResourceDefinitionId")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateSubscriptionDefinitionRequestModel(BaseModel):
    subscription_definition_id: str = Field(alias="SubscriptionDefinitionId")
    name: Optional[str] = Field(default=None, alias="Name")


class AssociateRoleToGroupResponseModel(BaseModel):
    associated_at: str = Field(alias="AssociatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateServiceRoleToAccountResponseModel(BaseModel):
    associated_at: str = Field(alias="AssociatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectorDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectorDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCoreDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCoreDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeploymentResponseModel(BaseModel):
    deployment_arn: str = Field(alias="DeploymentArn")
    deployment_id: str = Field(alias="DeploymentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeviceDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeviceDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFunctionDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFunctionDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupCertificateAuthorityResponseModel(BaseModel):
    group_certificate_authority_arn: str = Field(alias="GroupCertificateAuthorityArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoggerDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoggerDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourceDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourceDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSoftwareUpdateJobResponseModel(BaseModel):
    iot_job_arn: str = Field(alias="IotJobArn")
    iot_job_id: str = Field(alias="IotJobId")
    platform_software_version: str = Field(alias="PlatformSoftwareVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSubscriptionDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSubscriptionDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateRoleFromGroupResponseModel(BaseModel):
    disassociated_at: str = Field(alias="DisassociatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateServiceRoleFromAccountResponseModel(BaseModel):
    disassociated_at: str = Field(alias="DisassociatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAssociatedRoleResponseModel(BaseModel):
    associated_at: str = Field(alias="AssociatedAt")
    role_arn: str = Field(alias="RoleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectorDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCoreDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeviceDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFunctionDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupCertificateAuthorityResponseModel(BaseModel):
    group_certificate_authority_arn: str = Field(alias="GroupCertificateAuthorityArn")
    group_certificate_authority_id: str = Field(alias="GroupCertificateAuthorityId")
    pem_encoded_certificate: str = Field(alias="PemEncodedCertificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupCertificateConfigurationResponseModel(BaseModel):
    certificate_authority_expiry_in_milliseconds: str = Field(
        alias="CertificateAuthorityExpiryInMilliseconds"
    )
    certificate_expiry_in_milliseconds: str = Field(
        alias="CertificateExpiryInMilliseconds"
    )
    group_id: str = Field(alias="GroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGroupResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLoggerDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServiceRoleForAccountResponseModel(BaseModel):
    associated_at: str = Field(alias="AssociatedAt")
    role_arn: str = Field(alias="RoleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSubscriptionDefinitionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    id: str = Field(alias="Id")
    last_updated_timestamp: str = Field(alias="LastUpdatedTimestamp")
    latest_version: str = Field(alias="LatestVersion")
    latest_version_arn: str = Field(alias="LatestVersionArn")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResetDeploymentsResponseModel(BaseModel):
    deployment_arn: str = Field(alias="DeploymentArn")
    deployment_id: str = Field(alias="DeploymentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartBulkDeploymentResponseModel(BaseModel):
    bulk_deployment_arn: str = Field(alias="BulkDeploymentArn")
    bulk_deployment_id: str = Field(alias="BulkDeploymentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectivityInfoResponseModel(BaseModel):
    message: str = Field(alias="Message")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGroupCertificateConfigurationResponseModel(BaseModel):
    certificate_authority_expiry_in_milliseconds: str = Field(
        alias="CertificateAuthorityExpiryInMilliseconds"
    )
    certificate_expiry_in_milliseconds: str = Field(
        alias="CertificateExpiryInMilliseconds"
    )
    group_id: str = Field(alias="GroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BulkDeploymentResultModel(BaseModel):
    created_at: Optional[str] = Field(default=None, alias="CreatedAt")
    deployment_arn: Optional[str] = Field(default=None, alias="DeploymentArn")
    deployment_id: Optional[str] = Field(default=None, alias="DeploymentId")
    deployment_status: Optional[str] = Field(default=None, alias="DeploymentStatus")
    deployment_type: Optional[
        Literal[
            "ForceResetDeployment", "NewDeployment", "Redeployment", "ResetDeployment"
        ]
    ] = Field(default=None, alias="DeploymentType")
    error_details: Optional[List[ErrorDetailModel]] = Field(
        default=None, alias="ErrorDetails"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    group_arn: Optional[str] = Field(default=None, alias="GroupArn")


class GetBulkDeploymentStatusResponseModel(BaseModel):
    bulk_deployment_metrics: BulkDeploymentMetricsModel = Field(
        alias="BulkDeploymentMetrics"
    )
    bulk_deployment_status: Literal[
        "Completed", "Failed", "Initializing", "Running", "Stopped", "Stopping"
    ] = Field(alias="BulkDeploymentStatus")
    created_at: str = Field(alias="CreatedAt")
    error_details: List[ErrorDetailModel] = Field(alias="ErrorDetails")
    error_message: str = Field(alias="ErrorMessage")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeploymentStatusResponseModel(BaseModel):
    deployment_status: str = Field(alias="DeploymentStatus")
    deployment_type: Literal[
        "ForceResetDeployment", "NewDeployment", "Redeployment", "ResetDeployment"
    ] = Field(alias="DeploymentType")
    error_details: List[ErrorDetailModel] = Field(alias="ErrorDetails")
    error_message: str = Field(alias="ErrorMessage")
    updated_at: str = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBulkDeploymentsResponseModel(BaseModel):
    bulk_deployments: List[BulkDeploymentModel] = Field(alias="BulkDeployments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConnectivityInfoResponseModel(BaseModel):
    connectivity_info: List[ConnectivityInfoModel] = Field(alias="ConnectivityInfo")
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectivityInfoRequestModel(BaseModel):
    thing_name: str = Field(alias="ThingName")
    connectivity_info: Optional[Sequence[ConnectivityInfoModel]] = Field(
        default=None, alias="ConnectivityInfo"
    )


class ConnectorDefinitionVersionModel(BaseModel):
    connectors: Optional[Sequence[ConnectorModel]] = Field(
        default=None, alias="Connectors"
    )


class CreateConnectorDefinitionVersionRequestModel(BaseModel):
    connector_definition_id: str = Field(alias="ConnectorDefinitionId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    connectors: Optional[Sequence[ConnectorModel]] = Field(
        default=None, alias="Connectors"
    )


class CoreDefinitionVersionModel(BaseModel):
    cores: Optional[Sequence[CoreModel]] = Field(default=None, alias="Cores")


class CreateCoreDefinitionVersionRequestModel(BaseModel):
    core_definition_id: str = Field(alias="CoreDefinitionId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    cores: Optional[Sequence[CoreModel]] = Field(default=None, alias="Cores")


class CreateDeviceDefinitionVersionRequestModel(BaseModel):
    device_definition_id: str = Field(alias="DeviceDefinitionId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    devices: Optional[Sequence[DeviceModel]] = Field(default=None, alias="Devices")


class DeviceDefinitionVersionModel(BaseModel):
    devices: Optional[Sequence[DeviceModel]] = Field(default=None, alias="Devices")


class CreateGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[GroupVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetGroupVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: GroupVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoggerDefinitionVersionRequestModel(BaseModel):
    logger_definition_id: str = Field(alias="LoggerDefinitionId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    loggers: Optional[Sequence[LoggerModel]] = Field(default=None, alias="Loggers")


class LoggerDefinitionVersionModel(BaseModel):
    loggers: Optional[Sequence[LoggerModel]] = Field(default=None, alias="Loggers")


class CreateSubscriptionDefinitionVersionRequestModel(BaseModel):
    subscription_definition_id: str = Field(alias="SubscriptionDefinitionId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    subscriptions: Optional[Sequence[SubscriptionModel]] = Field(
        default=None, alias="Subscriptions"
    )


class SubscriptionDefinitionVersionModel(BaseModel):
    subscriptions: Optional[Sequence[SubscriptionModel]] = Field(
        default=None, alias="Subscriptions"
    )


class ListConnectorDefinitionsResponseModel(BaseModel):
    definitions: List[DefinitionInformationModel] = Field(alias="Definitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCoreDefinitionsResponseModel(BaseModel):
    definitions: List[DefinitionInformationModel] = Field(alias="Definitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceDefinitionsResponseModel(BaseModel):
    definitions: List[DefinitionInformationModel] = Field(alias="Definitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFunctionDefinitionsResponseModel(BaseModel):
    definitions: List[DefinitionInformationModel] = Field(alias="Definitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLoggerDefinitionsResponseModel(BaseModel):
    definitions: List[DefinitionInformationModel] = Field(alias="Definitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceDefinitionsResponseModel(BaseModel):
    definitions: List[DefinitionInformationModel] = Field(alias="Definitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSubscriptionDefinitionsResponseModel(BaseModel):
    definitions: List[DefinitionInformationModel] = Field(alias="Definitions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeploymentsResponseModel(BaseModel):
    deployments: List[DeploymentModel] = Field(alias="Deployments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionDefaultExecutionConfigModel(BaseModel):
    isolation_mode: Optional[Literal["GreengrassContainer", "NoContainer"]] = Field(
        default=None, alias="IsolationMode"
    )
    run_as: Optional[FunctionRunAsConfigModel] = Field(default=None, alias="RunAs")


class FunctionExecutionConfigModel(BaseModel):
    isolation_mode: Optional[Literal["GreengrassContainer", "NoContainer"]] = Field(
        default=None, alias="IsolationMode"
    )
    run_as: Optional[FunctionRunAsConfigModel] = Field(default=None, alias="RunAs")


class ListGroupCertificateAuthoritiesResponseModel(BaseModel):
    group_certificate_authorities: List[
        GroupCertificateAuthorityPropertiesModel
    ] = Field(alias="GroupCertificateAuthorities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsResponseModel(BaseModel):
    groups: List[GroupInformationModel] = Field(alias="Groups")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LocalDeviceResourceDataModel(BaseModel):
    group_owner_setting: Optional[GroupOwnerSettingModel] = Field(
        default=None, alias="GroupOwnerSetting"
    )
    source_path: Optional[str] = Field(default=None, alias="SourcePath")


class LocalVolumeResourceDataModel(BaseModel):
    destination_path: Optional[str] = Field(default=None, alias="DestinationPath")
    group_owner_setting: Optional[GroupOwnerSettingModel] = Field(
        default=None, alias="GroupOwnerSetting"
    )
    source_path: Optional[str] = Field(default=None, alias="SourcePath")


class ListBulkDeploymentDetailedReportsRequestListBulkDeploymentDetailedReportsPaginateModel(
    BaseModel
):
    bulk_deployment_id: str = Field(alias="BulkDeploymentId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBulkDeploymentsRequestListBulkDeploymentsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConnectorDefinitionVersionsRequestListConnectorDefinitionVersionsPaginateModel(
    BaseModel
):
    connector_definition_id: str = Field(alias="ConnectorDefinitionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConnectorDefinitionsRequestListConnectorDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCoreDefinitionVersionsRequestListCoreDefinitionVersionsPaginateModel(
    BaseModel
):
    core_definition_id: str = Field(alias="CoreDefinitionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCoreDefinitionsRequestListCoreDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeploymentsRequestListDeploymentsPaginateModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeviceDefinitionVersionsRequestListDeviceDefinitionVersionsPaginateModel(
    BaseModel
):
    device_definition_id: str = Field(alias="DeviceDefinitionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeviceDefinitionsRequestListDeviceDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionDefinitionVersionsRequestListFunctionDefinitionVersionsPaginateModel(
    BaseModel
):
    function_definition_id: str = Field(alias="FunctionDefinitionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFunctionDefinitionsRequestListFunctionDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupVersionsRequestListGroupVersionsPaginateModel(BaseModel):
    group_id: str = Field(alias="GroupId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGroupsRequestListGroupsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLoggerDefinitionVersionsRequestListLoggerDefinitionVersionsPaginateModel(
    BaseModel
):
    logger_definition_id: str = Field(alias="LoggerDefinitionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLoggerDefinitionsRequestListLoggerDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceDefinitionVersionsRequestListResourceDefinitionVersionsPaginateModel(
    BaseModel
):
    resource_definition_id: str = Field(alias="ResourceDefinitionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceDefinitionsRequestListResourceDefinitionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSubscriptionDefinitionVersionsRequestListSubscriptionDefinitionVersionsPaginateModel(
    BaseModel
):
    subscription_definition_id: str = Field(alias="SubscriptionDefinitionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSubscriptionDefinitionsRequestListSubscriptionDefinitionsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConnectorDefinitionVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCoreDefinitionVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceDefinitionVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFunctionDefinitionVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLoggerDefinitionVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceDefinitionVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSubscriptionDefinitionVersionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    versions: List[VersionInformationModel] = Field(alias="Versions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class S3MachineLearningModelResourceDataModel(BaseModel):
    destination_path: Optional[str] = Field(default=None, alias="DestinationPath")
    owner_setting: Optional[ResourceDownloadOwnerSettingModel] = Field(
        default=None, alias="OwnerSetting"
    )
    s3_uri: Optional[str] = Field(default=None, alias="S3Uri")


class SageMakerMachineLearningModelResourceDataModel(BaseModel):
    destination_path: Optional[str] = Field(default=None, alias="DestinationPath")
    owner_setting: Optional[ResourceDownloadOwnerSettingModel] = Field(
        default=None, alias="OwnerSetting"
    )
    sage_maker_job_arn: Optional[str] = Field(default=None, alias="SageMakerJobArn")


class RuntimeConfigurationModel(BaseModel):
    telemetry_configuration: Optional[TelemetryConfigurationModel] = Field(
        default=None, alias="TelemetryConfiguration"
    )


class UpdateThingRuntimeConfigurationRequestModel(BaseModel):
    thing_name: str = Field(alias="ThingName")
    telemetry_configuration: Optional[TelemetryConfigurationUpdateModel] = Field(
        default=None, alias="TelemetryConfiguration"
    )


class ListBulkDeploymentDetailedReportsResponseModel(BaseModel):
    deployments: List[BulkDeploymentResultModel] = Field(alias="Deployments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectorDefinitionRequestModel(BaseModel):
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[ConnectorDefinitionVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetConnectorDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: ConnectorDefinitionVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    next_token: str = Field(alias="NextToken")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCoreDefinitionRequestModel(BaseModel):
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[CoreDefinitionVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetCoreDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: CoreDefinitionVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    next_token: str = Field(alias="NextToken")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDeviceDefinitionRequestModel(BaseModel):
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[DeviceDefinitionVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetDeviceDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: DeviceDefinitionVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    next_token: str = Field(alias="NextToken")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateLoggerDefinitionRequestModel(BaseModel):
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[LoggerDefinitionVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetLoggerDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: LoggerDefinitionVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSubscriptionDefinitionRequestModel(BaseModel):
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[SubscriptionDefinitionVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetSubscriptionDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: SubscriptionDefinitionVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    next_token: str = Field(alias="NextToken")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionDefaultConfigModel(BaseModel):
    execution: Optional[FunctionDefaultExecutionConfigModel] = Field(
        default=None, alias="Execution"
    )


class FunctionConfigurationEnvironmentModel(BaseModel):
    access_sysfs: Optional[bool] = Field(default=None, alias="AccessSysfs")
    execution: Optional[FunctionExecutionConfigModel] = Field(
        default=None, alias="Execution"
    )
    resource_access_policies: Optional[Sequence[ResourceAccessPolicyModel]] = Field(
        default=None, alias="ResourceAccessPolicies"
    )
    variables: Optional[Mapping[str, str]] = Field(default=None, alias="Variables")


class ResourceDataContainerModel(BaseModel):
    local_device_resource_data: Optional[LocalDeviceResourceDataModel] = Field(
        default=None, alias="LocalDeviceResourceData"
    )
    local_volume_resource_data: Optional[LocalVolumeResourceDataModel] = Field(
        default=None, alias="LocalVolumeResourceData"
    )
    s3_machine_learning_model_resource_data: Optional[
        S3MachineLearningModelResourceDataModel
    ] = Field(default=None, alias="S3MachineLearningModelResourceData")
    sage_maker_machine_learning_model_resource_data: Optional[
        SageMakerMachineLearningModelResourceDataModel
    ] = Field(default=None, alias="SageMakerMachineLearningModelResourceData")
    secrets_manager_secret_resource_data: Optional[
        SecretsManagerSecretResourceDataModel
    ] = Field(default=None, alias="SecretsManagerSecretResourceData")


class GetThingRuntimeConfigurationResponseModel(BaseModel):
    runtime_configuration: RuntimeConfigurationModel = Field(
        alias="RuntimeConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FunctionConfigurationModel(BaseModel):
    encoding_type: Optional[Literal["binary", "json"]] = Field(
        default=None, alias="EncodingType"
    )
    environment: Optional[FunctionConfigurationEnvironmentModel] = Field(
        default=None, alias="Environment"
    )
    exec_args: Optional[str] = Field(default=None, alias="ExecArgs")
    executable: Optional[str] = Field(default=None, alias="Executable")
    memory_size: Optional[int] = Field(default=None, alias="MemorySize")
    pinned: Optional[bool] = Field(default=None, alias="Pinned")
    timeout: Optional[int] = Field(default=None, alias="Timeout")
    function_runtime_override: Optional[str] = Field(
        default=None, alias="FunctionRuntimeOverride"
    )


class ResourceModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    resource_data_container: ResourceDataContainerModel = Field(
        alias="ResourceDataContainer"
    )


class FunctionModel(BaseModel):
    id: str = Field(alias="Id")
    function_arn: Optional[str] = Field(default=None, alias="FunctionArn")
    function_configuration: Optional[FunctionConfigurationModel] = Field(
        default=None, alias="FunctionConfiguration"
    )


class CreateResourceDefinitionVersionRequestModel(BaseModel):
    resource_definition_id: str = Field(alias="ResourceDefinitionId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    resources: Optional[Sequence[ResourceModel]] = Field(
        default=None, alias="Resources"
    )


class ResourceDefinitionVersionModel(BaseModel):
    resources: Optional[Sequence[ResourceModel]] = Field(
        default=None, alias="Resources"
    )


class CreateFunctionDefinitionVersionRequestModel(BaseModel):
    function_definition_id: str = Field(alias="FunctionDefinitionId")
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    default_config: Optional[FunctionDefaultConfigModel] = Field(
        default=None, alias="DefaultConfig"
    )
    functions: Optional[Sequence[FunctionModel]] = Field(
        default=None, alias="Functions"
    )


class FunctionDefinitionVersionModel(BaseModel):
    default_config: Optional[FunctionDefaultConfigModel] = Field(
        default=None, alias="DefaultConfig"
    )
    functions: Optional[Sequence[FunctionModel]] = Field(
        default=None, alias="Functions"
    )


class CreateResourceDefinitionRequestModel(BaseModel):
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[ResourceDefinitionVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetResourceDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: ResourceDefinitionVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFunctionDefinitionRequestModel(BaseModel):
    amzn_client_token: Optional[str] = Field(default=None, alias="AmznClientToken")
    initial_version: Optional[FunctionDefinitionVersionModel] = Field(
        default=None, alias="InitialVersion"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetFunctionDefinitionVersionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    creation_timestamp: str = Field(alias="CreationTimestamp")
    definition: FunctionDefinitionVersionModel = Field(alias="Definition")
    id: str = Field(alias="Id")
    next_token: str = Field(alias="NextToken")
    version: str = Field(alias="Version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
