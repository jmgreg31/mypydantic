# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionInvocationModel(BaseModel):
    extension_identifier: Optional[str] = Field(
        default=None, alias="ExtensionIdentifier"
    )
    action_name: Optional[str] = Field(default=None, alias="ActionName")
    uri: Optional[str] = Field(default=None, alias="Uri")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    invocation_id: Optional[str] = Field(default=None, alias="InvocationId")


class ActionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    uri: Optional[str] = Field(default=None, alias="Uri")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ApplicationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class AppliedExtensionModel(BaseModel):
    extension_id: Optional[str] = Field(default=None, alias="ExtensionId")
    extension_association_id: Optional[str] = Field(
        default=None, alias="ExtensionAssociationId"
    )
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    parameters: Optional[Dict[str, str]] = Field(default=None, alias="Parameters")


class ConfigurationProfileSummaryModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    location_uri: Optional[str] = Field(default=None, alias="LocationUri")
    validator_types: Optional[List[Literal["JSON_SCHEMA", "LAMBDA"]]] = Field(
        default=None, alias="ValidatorTypes"
    )
    type: Optional[str] = Field(default=None, alias="Type")


class ValidatorModel(BaseModel):
    type: Literal["JSON_SCHEMA", "LAMBDA"] = Field(alias="Type")
    content: str = Field(alias="Content")


class CreateApplicationRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateDeploymentStrategyRequestModel(BaseModel):
    name: str = Field(alias="Name")
    deployment_duration_in_minutes: int = Field(alias="DeploymentDurationInMinutes")
    growth_factor: float = Field(alias="GrowthFactor")
    description: Optional[str] = Field(default=None, alias="Description")
    final_bake_time_in_minutes: Optional[int] = Field(
        default=None, alias="FinalBakeTimeInMinutes"
    )
    growth_type: Optional[Literal["EXPONENTIAL", "LINEAR"]] = Field(
        default=None, alias="GrowthType"
    )
    replicate_to: Optional[Literal["NONE", "SSM_DOCUMENT"]] = Field(
        default=None, alias="ReplicateTo"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class MonitorModel(BaseModel):
    alarm_arn: str = Field(alias="AlarmArn")
    alarm_role_arn: Optional[str] = Field(default=None, alias="AlarmRoleArn")


class CreateExtensionAssociationRequestModel(BaseModel):
    extension_identifier: str = Field(alias="ExtensionIdentifier")
    resource_identifier: str = Field(alias="ResourceIdentifier")
    extension_version_number: Optional[int] = Field(
        default=None, alias="ExtensionVersionNumber"
    )
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ParameterModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    required: Optional[bool] = Field(default=None, alias="Required")


class CreateHostedConfigurationVersionRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    content: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Content"
    )
    content_type: str = Field(alias="ContentType")
    description: Optional[str] = Field(default=None, alias="Description")
    latest_version_number: Optional[int] = Field(
        default=None, alias="LatestVersionNumber"
    )
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")


class DeleteApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class DeleteConfigurationProfileRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")


class DeleteDeploymentStrategyRequestModel(BaseModel):
    deployment_strategy_id: str = Field(alias="DeploymentStrategyId")


class DeleteEnvironmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")


class DeleteExtensionAssociationRequestModel(BaseModel):
    extension_association_id: str = Field(alias="ExtensionAssociationId")


class DeleteExtensionRequestModel(BaseModel):
    extension_identifier: str = Field(alias="ExtensionIdentifier")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")


class DeleteHostedConfigurationVersionRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    version_number: int = Field(alias="VersionNumber")


class DeploymentStrategyModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    deployment_duration_in_minutes: Optional[int] = Field(
        default=None, alias="DeploymentDurationInMinutes"
    )
    growth_type: Optional[Literal["EXPONENTIAL", "LINEAR"]] = Field(
        default=None, alias="GrowthType"
    )
    growth_factor: Optional[float] = Field(default=None, alias="GrowthFactor")
    final_bake_time_in_minutes: Optional[int] = Field(
        default=None, alias="FinalBakeTimeInMinutes"
    )
    replicate_to: Optional[Literal["NONE", "SSM_DOCUMENT"]] = Field(
        default=None, alias="ReplicateTo"
    )


class DeploymentSummaryModel(BaseModel):
    deployment_number: Optional[int] = Field(default=None, alias="DeploymentNumber")
    configuration_name: Optional[str] = Field(default=None, alias="ConfigurationName")
    configuration_version: Optional[str] = Field(
        default=None, alias="ConfigurationVersion"
    )
    deployment_duration_in_minutes: Optional[int] = Field(
        default=None, alias="DeploymentDurationInMinutes"
    )
    growth_type: Optional[Literal["EXPONENTIAL", "LINEAR"]] = Field(
        default=None, alias="GrowthType"
    )
    growth_factor: Optional[float] = Field(default=None, alias="GrowthFactor")
    final_bake_time_in_minutes: Optional[int] = Field(
        default=None, alias="FinalBakeTimeInMinutes"
    )
    state: Optional[
        Literal[
            "BAKING",
            "COMPLETE",
            "DEPLOYING",
            "ROLLED_BACK",
            "ROLLING_BACK",
            "VALIDATING",
        ]
    ] = Field(default=None, alias="State")
    percentage_complete: Optional[float] = Field(
        default=None, alias="PercentageComplete"
    )
    started_at: Optional[datetime] = Field(default=None, alias="StartedAt")
    completed_at: Optional[datetime] = Field(default=None, alias="CompletedAt")


class ExtensionAssociationSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    extension_arn: Optional[str] = Field(default=None, alias="ExtensionArn")
    resource_arn: Optional[str] = Field(default=None, alias="ResourceArn")


class ExtensionSummaryModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")


class GetApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class GetConfigurationProfileRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")


class GetConfigurationRequestModel(BaseModel):
    application: str = Field(alias="Application")
    environment: str = Field(alias="Environment")
    configuration: str = Field(alias="Configuration")
    client_id: str = Field(alias="ClientId")
    client_configuration_version: Optional[str] = Field(
        default=None, alias="ClientConfigurationVersion"
    )


class GetDeploymentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")
    deployment_number: int = Field(alias="DeploymentNumber")


class GetDeploymentStrategyRequestModel(BaseModel):
    deployment_strategy_id: str = Field(alias="DeploymentStrategyId")


class GetEnvironmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")


class GetExtensionAssociationRequestModel(BaseModel):
    extension_association_id: str = Field(alias="ExtensionAssociationId")


class GetExtensionRequestModel(BaseModel):
    extension_identifier: str = Field(alias="ExtensionIdentifier")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")


class GetHostedConfigurationVersionRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    version_number: int = Field(alias="VersionNumber")


class HostedConfigurationVersionSummaryModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    configuration_profile_id: Optional[str] = Field(
        default=None, alias="ConfigurationProfileId"
    )
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    description: Optional[str] = Field(default=None, alias="Description")
    content_type: Optional[str] = Field(default=None, alias="ContentType")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")


class ListApplicationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConfigurationProfilesRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    type: Optional[str] = Field(default=None, alias="Type")


class ListDeploymentStrategiesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDeploymentsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListEnvironmentsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListExtensionAssociationsRequestModel(BaseModel):
    resource_identifier: Optional[str] = Field(default=None, alias="ResourceIdentifier")
    extension_identifier: Optional[str] = Field(
        default=None, alias="ExtensionIdentifier"
    )
    extension_version_number: Optional[int] = Field(
        default=None, alias="ExtensionVersionNumber"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListExtensionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    name: Optional[str] = Field(default=None, alias="Name")


class ListHostedConfigurationVersionsRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    version_label: Optional[str] = Field(default=None, alias="VersionLabel")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class StartDeploymentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")
    deployment_strategy_id: str = Field(alias="DeploymentStrategyId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    configuration_version: str = Field(alias="ConfigurationVersion")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    kms_key_identifier: Optional[str] = Field(default=None, alias="KmsKeyIdentifier")


class StopDeploymentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")
    deployment_number: int = Field(alias="DeploymentNumber")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateApplicationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateDeploymentStrategyRequestModel(BaseModel):
    deployment_strategy_id: str = Field(alias="DeploymentStrategyId")
    description: Optional[str] = Field(default=None, alias="Description")
    deployment_duration_in_minutes: Optional[int] = Field(
        default=None, alias="DeploymentDurationInMinutes"
    )
    final_bake_time_in_minutes: Optional[int] = Field(
        default=None, alias="FinalBakeTimeInMinutes"
    )
    growth_factor: Optional[float] = Field(default=None, alias="GrowthFactor")
    growth_type: Optional[Literal["EXPONENTIAL", "LINEAR"]] = Field(
        default=None, alias="GrowthType"
    )


class UpdateExtensionAssociationRequestModel(BaseModel):
    extension_association_id: str = Field(alias="ExtensionAssociationId")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")


class ValidateConfigurationRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    configuration_version: str = Field(alias="ConfigurationVersion")


class DeploymentEventModel(BaseModel):
    event_type: Optional[
        Literal[
            "BAKE_TIME_STARTED",
            "DEPLOYMENT_COMPLETED",
            "DEPLOYMENT_STARTED",
            "PERCENTAGE_UPDATED",
            "ROLLBACK_COMPLETED",
            "ROLLBACK_STARTED",
        ]
    ] = Field(default=None, alias="EventType")
    triggered_by: Optional[
        Literal["APPCONFIG", "CLOUDWATCH_ALARM", "INTERNAL_ERROR", "USER"]
    ] = Field(default=None, alias="TriggeredBy")
    description: Optional[str] = Field(default=None, alias="Description")
    action_invocations: Optional[List[ActionInvocationModel]] = Field(
        default=None, alias="ActionInvocations"
    )
    occurred_at: Optional[datetime] = Field(default=None, alias="OccurredAt")


class ApplicationResponseMetadataModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationModel(BaseModel):
    content: Type[StreamingBody] = Field(alias="Content")
    configuration_version: str = Field(alias="ConfigurationVersion")
    content_type: str = Field(alias="ContentType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentStrategyResponseMetadataModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    deployment_duration_in_minutes: int = Field(alias="DeploymentDurationInMinutes")
    growth_type: Literal["EXPONENTIAL", "LINEAR"] = Field(alias="GrowthType")
    growth_factor: float = Field(alias="GrowthFactor")
    final_bake_time_in_minutes: int = Field(alias="FinalBakeTimeInMinutes")
    replicate_to: Literal["NONE", "SSM_DOCUMENT"] = Field(alias="ReplicateTo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExtensionAssociationModel(BaseModel):
    id: str = Field(alias="Id")
    extension_arn: str = Field(alias="ExtensionArn")
    resource_arn: str = Field(alias="ResourceArn")
    arn: str = Field(alias="Arn")
    parameters: Dict[str, str] = Field(alias="Parameters")
    extension_version_number: int = Field(alias="ExtensionVersionNumber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HostedConfigurationVersionModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    version_number: int = Field(alias="VersionNumber")
    description: str = Field(alias="Description")
    content: Type[StreamingBody] = Field(alias="Content")
    content_type: str = Field(alias="ContentType")
    version_label: str = Field(alias="VersionLabel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ResourceTagsModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ApplicationsModel(BaseModel):
    items: List[ApplicationModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationProfilesModel(BaseModel):
    items: List[ConfigurationProfileSummaryModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationProfileModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    location_uri: str = Field(alias="LocationUri")
    retrieval_role_arn: str = Field(alias="RetrievalRoleArn")
    validators: List[ValidatorModel] = Field(alias="Validators")
    type: str = Field(alias="Type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConfigurationProfileRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    name: str = Field(alias="Name")
    location_uri: str = Field(alias="LocationUri")
    description: Optional[str] = Field(default=None, alias="Description")
    retrieval_role_arn: Optional[str] = Field(default=None, alias="RetrievalRoleArn")
    validators: Optional[Sequence[ValidatorModel]] = Field(
        default=None, alias="Validators"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    type: Optional[str] = Field(default=None, alias="Type")


class UpdateConfigurationProfileRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    retrieval_role_arn: Optional[str] = Field(default=None, alias="RetrievalRoleArn")
    validators: Optional[Sequence[ValidatorModel]] = Field(
        default=None, alias="Validators"
    )


class CreateEnvironmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    monitors: Optional[Sequence[MonitorModel]] = Field(default=None, alias="Monitors")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class EnvironmentResponseMetadataModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    description: str = Field(alias="Description")
    state: Literal[
        "DEPLOYING", "READY_FOR_DEPLOYMENT", "ROLLED_BACK", "ROLLING_BACK"
    ] = Field(alias="State")
    monitors: List[MonitorModel] = Field(alias="Monitors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    id: Optional[str] = Field(default=None, alias="Id")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    state: Optional[
        Literal["DEPLOYING", "READY_FOR_DEPLOYMENT", "ROLLED_BACK", "ROLLING_BACK"]
    ] = Field(default=None, alias="State")
    monitors: Optional[List[MonitorModel]] = Field(default=None, alias="Monitors")


class UpdateEnvironmentRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    monitors: Optional[Sequence[MonitorModel]] = Field(default=None, alias="Monitors")


class CreateExtensionRequestModel(BaseModel):
    name: str = Field(alias="Name")
    actions: Mapping[
        Literal[
            "ON_DEPLOYMENT_BAKING",
            "ON_DEPLOYMENT_COMPLETE",
            "ON_DEPLOYMENT_ROLLED_BACK",
            "ON_DEPLOYMENT_START",
            "ON_DEPLOYMENT_STEP",
            "PRE_CREATE_HOSTED_CONFIGURATION_VERSION",
            "PRE_START_DEPLOYMENT",
        ],
        Sequence[ActionModel],
    ] = Field(alias="Actions")
    description: Optional[str] = Field(default=None, alias="Description")
    parameters: Optional[Mapping[str, ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    latest_version_number: Optional[int] = Field(
        default=None, alias="LatestVersionNumber"
    )


class ExtensionModel(BaseModel):
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    version_number: int = Field(alias="VersionNumber")
    arn: str = Field(alias="Arn")
    description: str = Field(alias="Description")
    actions: Dict[
        Literal[
            "ON_DEPLOYMENT_BAKING",
            "ON_DEPLOYMENT_COMPLETE",
            "ON_DEPLOYMENT_ROLLED_BACK",
            "ON_DEPLOYMENT_START",
            "ON_DEPLOYMENT_STEP",
            "PRE_CREATE_HOSTED_CONFIGURATION_VERSION",
            "PRE_START_DEPLOYMENT",
        ],
        List[ActionModel],
    ] = Field(alias="Actions")
    parameters: Dict[str, ParameterModel] = Field(alias="Parameters")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateExtensionRequestModel(BaseModel):
    extension_identifier: str = Field(alias="ExtensionIdentifier")
    description: Optional[str] = Field(default=None, alias="Description")
    actions: Optional[
        Mapping[
            Literal[
                "ON_DEPLOYMENT_BAKING",
                "ON_DEPLOYMENT_COMPLETE",
                "ON_DEPLOYMENT_ROLLED_BACK",
                "ON_DEPLOYMENT_START",
                "ON_DEPLOYMENT_STEP",
                "PRE_CREATE_HOSTED_CONFIGURATION_VERSION",
                "PRE_START_DEPLOYMENT",
            ],
            Sequence[ActionModel],
        ]
    ] = Field(default=None, alias="Actions")
    parameters: Optional[Mapping[str, ParameterModel]] = Field(
        default=None, alias="Parameters"
    )
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")


class DeploymentStrategiesModel(BaseModel):
    items: List[DeploymentStrategyModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentsModel(BaseModel):
    items: List[DeploymentSummaryModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExtensionAssociationsModel(BaseModel):
    items: List[ExtensionAssociationSummaryModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExtensionsModel(BaseModel):
    items: List[ExtensionSummaryModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HostedConfigurationVersionsModel(BaseModel):
    items: List[HostedConfigurationVersionSummaryModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeploymentModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    environment_id: str = Field(alias="EnvironmentId")
    deployment_strategy_id: str = Field(alias="DeploymentStrategyId")
    configuration_profile_id: str = Field(alias="ConfigurationProfileId")
    deployment_number: int = Field(alias="DeploymentNumber")
    configuration_name: str = Field(alias="ConfigurationName")
    configuration_location_uri: str = Field(alias="ConfigurationLocationUri")
    configuration_version: str = Field(alias="ConfigurationVersion")
    description: str = Field(alias="Description")
    deployment_duration_in_minutes: int = Field(alias="DeploymentDurationInMinutes")
    growth_type: Literal["EXPONENTIAL", "LINEAR"] = Field(alias="GrowthType")
    growth_factor: float = Field(alias="GrowthFactor")
    final_bake_time_in_minutes: int = Field(alias="FinalBakeTimeInMinutes")
    state: Literal[
        "BAKING", "COMPLETE", "DEPLOYING", "ROLLED_BACK", "ROLLING_BACK", "VALIDATING"
    ] = Field(alias="State")
    event_log: List[DeploymentEventModel] = Field(alias="EventLog")
    percentage_complete: float = Field(alias="PercentageComplete")
    started_at: datetime = Field(alias="StartedAt")
    completed_at: datetime = Field(alias="CompletedAt")
    applied_extensions: List[AppliedExtensionModel] = Field(alias="AppliedExtensions")
    kms_key_arn: str = Field(alias="KmsKeyArn")
    kms_key_identifier: str = Field(alias="KmsKeyIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnvironmentsModel(BaseModel):
    items: List[EnvironmentModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
