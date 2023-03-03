# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionRequiredModel(BaseModel):
    action_required_code: Optional[str] = Field(
        default=None, alias="ActionRequiredCode"
    )
    action_required_info: Optional[str] = Field(
        default=None, alias="ActionRequiredInfo"
    )


class AvailabilityZoneModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class EngineVersionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class BrokerInstanceModel(BaseModel):
    console_url: Optional[str] = Field(default=None, alias="ConsoleURL")
    endpoints: Optional[List[str]] = Field(default=None, alias="Endpoints")
    ip_address: Optional[str] = Field(default=None, alias="IpAddress")


class BrokerSummaryModel(BaseModel):
    deployment_mode: Literal[
        "ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ", "SINGLE_INSTANCE"
    ] = Field(alias="DeploymentMode")
    engine_type: Literal["ACTIVEMQ", "RABBITMQ"] = Field(alias="EngineType")
    broker_arn: Optional[str] = Field(default=None, alias="BrokerArn")
    broker_id: Optional[str] = Field(default=None, alias="BrokerId")
    broker_name: Optional[str] = Field(default=None, alias="BrokerName")
    broker_state: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CRITICAL_ACTION_REQUIRED",
            "DELETION_IN_PROGRESS",
            "REBOOT_IN_PROGRESS",
            "RUNNING",
        ]
    ] = Field(default=None, alias="BrokerState")
    created: Optional[datetime] = Field(default=None, alias="Created")
    host_instance_type: Optional[str] = Field(default=None, alias="HostInstanceType")


class ConfigurationIdModel(BaseModel):
    id: str = Field(alias="Id")
    revision: Optional[int] = Field(default=None, alias="Revision")


class ConfigurationRevisionModel(BaseModel):
    created: datetime = Field(alias="Created")
    revision: int = Field(alias="Revision")
    description: Optional[str] = Field(default=None, alias="Description")


class EncryptionOptionsModel(BaseModel):
    use_aws_owned_key: bool = Field(alias="UseAwsOwnedKey")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class LdapServerMetadataInputModel(BaseModel):
    hosts: Sequence[str] = Field(alias="Hosts")
    role_base: str = Field(alias="RoleBase")
    role_search_matching: str = Field(alias="RoleSearchMatching")
    service_account_password: str = Field(alias="ServiceAccountPassword")
    service_account_username: str = Field(alias="ServiceAccountUsername")
    user_base: str = Field(alias="UserBase")
    user_search_matching: str = Field(alias="UserSearchMatching")
    role_name: Optional[str] = Field(default=None, alias="RoleName")
    role_search_subtree: Optional[bool] = Field(default=None, alias="RoleSearchSubtree")
    user_role_name: Optional[str] = Field(default=None, alias="UserRoleName")
    user_search_subtree: Optional[bool] = Field(default=None, alias="UserSearchSubtree")


class LogsModel(BaseModel):
    audit: Optional[bool] = Field(default=None, alias="Audit")
    general: Optional[bool] = Field(default=None, alias="General")


class UserModel(BaseModel):
    password: str = Field(alias="Password")
    username: str = Field(alias="Username")
    console_access: Optional[bool] = Field(default=None, alias="ConsoleAccess")
    groups: Optional[Sequence[str]] = Field(default=None, alias="Groups")


class WeeklyStartTimeModel(BaseModel):
    day_of_week: Literal[
        "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
    ] = Field(alias="DayOfWeek")
    time_of_day: str = Field(alias="TimeOfDay")
    time_zone: Optional[str] = Field(default=None, alias="TimeZone")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateConfigurationRequestModel(BaseModel):
    engine_type: Literal["ACTIVEMQ", "RABBITMQ"] = Field(alias="EngineType")
    engine_version: str = Field(alias="EngineVersion")
    name: str = Field(alias="Name")
    authentication_strategy: Optional[Literal["LDAP", "SIMPLE"]] = Field(
        default=None, alias="AuthenticationStrategy"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateUserRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    password: str = Field(alias="Password")
    username: str = Field(alias="Username")
    console_access: Optional[bool] = Field(default=None, alias="ConsoleAccess")
    groups: Optional[Sequence[str]] = Field(default=None, alias="Groups")


class DeleteBrokerRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")


class DeleteTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class DeleteUserRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    username: str = Field(alias="Username")


class DescribeBrokerEngineTypesRequestModel(BaseModel):
    engine_type: Optional[str] = Field(default=None, alias="EngineType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeBrokerInstanceOptionsRequestModel(BaseModel):
    engine_type: Optional[str] = Field(default=None, alias="EngineType")
    host_instance_type: Optional[str] = Field(default=None, alias="HostInstanceType")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    storage_type: Optional[str] = Field(default=None, alias="StorageType")


class DescribeBrokerRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")


class LdapServerMetadataOutputModel(BaseModel):
    hosts: List[str] = Field(alias="Hosts")
    role_base: str = Field(alias="RoleBase")
    role_search_matching: str = Field(alias="RoleSearchMatching")
    service_account_username: str = Field(alias="ServiceAccountUsername")
    user_base: str = Field(alias="UserBase")
    user_search_matching: str = Field(alias="UserSearchMatching")
    role_name: Optional[str] = Field(default=None, alias="RoleName")
    role_search_subtree: Optional[bool] = Field(default=None, alias="RoleSearchSubtree")
    user_role_name: Optional[str] = Field(default=None, alias="UserRoleName")
    user_search_subtree: Optional[bool] = Field(default=None, alias="UserSearchSubtree")


class UserSummaryModel(BaseModel):
    username: str = Field(alias="Username")
    pending_change: Optional[Literal["CREATE", "DELETE", "UPDATE"]] = Field(
        default=None, alias="PendingChange"
    )


class DescribeConfigurationRequestModel(BaseModel):
    configuration_id: str = Field(alias="ConfigurationId")


class DescribeConfigurationRevisionRequestModel(BaseModel):
    configuration_id: str = Field(alias="ConfigurationId")
    configuration_revision: str = Field(alias="ConfigurationRevision")


class DescribeUserRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    username: str = Field(alias="Username")


class UserPendingChangesModel(BaseModel):
    pending_change: Literal["CREATE", "DELETE", "UPDATE"] = Field(alias="PendingChange")
    console_access: Optional[bool] = Field(default=None, alias="ConsoleAccess")
    groups: Optional[List[str]] = Field(default=None, alias="Groups")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListBrokersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConfigurationRevisionsRequestModel(BaseModel):
    configuration_id: str = Field(alias="ConfigurationId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListUsersRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PendingLogsModel(BaseModel):
    audit: Optional[bool] = Field(default=None, alias="Audit")
    general: Optional[bool] = Field(default=None, alias="General")


class RebootBrokerRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")


class SanitizationWarningModel(BaseModel):
    reason: Literal[
        "DISALLOWED_ATTRIBUTE_REMOVED",
        "DISALLOWED_ELEMENT_REMOVED",
        "INVALID_ATTRIBUTE_VALUE_REMOVED",
    ] = Field(alias="Reason")
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")
    element_name: Optional[str] = Field(default=None, alias="ElementName")


class UpdateConfigurationRequestModel(BaseModel):
    configuration_id: str = Field(alias="ConfigurationId")
    data: str = Field(alias="Data")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateUserRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    username: str = Field(alias="Username")
    console_access: Optional[bool] = Field(default=None, alias="ConsoleAccess")
    groups: Optional[Sequence[str]] = Field(default=None, alias="Groups")
    password: Optional[str] = Field(default=None, alias="Password")


class BrokerInstanceOptionModel(BaseModel):
    availability_zones: Optional[List[AvailabilityZoneModel]] = Field(
        default=None, alias="AvailabilityZones"
    )
    engine_type: Optional[Literal["ACTIVEMQ", "RABBITMQ"]] = Field(
        default=None, alias="EngineType"
    )
    host_instance_type: Optional[str] = Field(default=None, alias="HostInstanceType")
    storage_type: Optional[Literal["EBS", "EFS"]] = Field(
        default=None, alias="StorageType"
    )
    supported_deployment_modes: Optional[
        List[Literal["ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ", "SINGLE_INSTANCE"]]
    ] = Field(default=None, alias="SupportedDeploymentModes")
    supported_engine_versions: Optional[List[str]] = Field(
        default=None, alias="SupportedEngineVersions"
    )


class BrokerEngineTypeModel(BaseModel):
    engine_type: Optional[Literal["ACTIVEMQ", "RABBITMQ"]] = Field(
        default=None, alias="EngineType"
    )
    engine_versions: Optional[List[EngineVersionModel]] = Field(
        default=None, alias="EngineVersions"
    )


class ConfigurationsModel(BaseModel):
    current: Optional[ConfigurationIdModel] = Field(default=None, alias="Current")
    history: Optional[List[ConfigurationIdModel]] = Field(default=None, alias="History")
    pending: Optional[ConfigurationIdModel] = Field(default=None, alias="Pending")


class ConfigurationModel(BaseModel):
    arn: str = Field(alias="Arn")
    authentication_strategy: Literal["LDAP", "SIMPLE"] = Field(
        alias="AuthenticationStrategy"
    )
    created: datetime = Field(alias="Created")
    description: str = Field(alias="Description")
    engine_type: Literal["ACTIVEMQ", "RABBITMQ"] = Field(alias="EngineType")
    engine_version: str = Field(alias="EngineVersion")
    id: str = Field(alias="Id")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    name: str = Field(alias="Name")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class CreateBrokerRequestModel(BaseModel):
    auto_minor_version_upgrade: bool = Field(alias="AutoMinorVersionUpgrade")
    broker_name: str = Field(alias="BrokerName")
    deployment_mode: Literal[
        "ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ", "SINGLE_INSTANCE"
    ] = Field(alias="DeploymentMode")
    engine_type: Literal["ACTIVEMQ", "RABBITMQ"] = Field(alias="EngineType")
    engine_version: str = Field(alias="EngineVersion")
    host_instance_type: str = Field(alias="HostInstanceType")
    publicly_accessible: bool = Field(alias="PubliclyAccessible")
    users: Sequence[UserModel] = Field(alias="Users")
    authentication_strategy: Optional[Literal["LDAP", "SIMPLE"]] = Field(
        default=None, alias="AuthenticationStrategy"
    )
    configuration: Optional[ConfigurationIdModel] = Field(
        default=None, alias="Configuration"
    )
    creator_request_id: Optional[str] = Field(default=None, alias="CreatorRequestId")
    encryption_options: Optional[EncryptionOptionsModel] = Field(
        default=None, alias="EncryptionOptions"
    )
    ldap_server_metadata: Optional[LdapServerMetadataInputModel] = Field(
        default=None, alias="LdapServerMetadata"
    )
    logs: Optional[LogsModel] = Field(default=None, alias="Logs")
    maintenance_window_start_time: Optional[WeeklyStartTimeModel] = Field(
        default=None, alias="MaintenanceWindowStartTime"
    )
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )
    storage_type: Optional[Literal["EBS", "EFS"]] = Field(
        default=None, alias="StorageType"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateBrokerRequestModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    authentication_strategy: Optional[Literal["LDAP", "SIMPLE"]] = Field(
        default=None, alias="AuthenticationStrategy"
    )
    auto_minor_version_upgrade: Optional[bool] = Field(
        default=None, alias="AutoMinorVersionUpgrade"
    )
    configuration: Optional[ConfigurationIdModel] = Field(
        default=None, alias="Configuration"
    )
    engine_version: Optional[str] = Field(default=None, alias="EngineVersion")
    host_instance_type: Optional[str] = Field(default=None, alias="HostInstanceType")
    ldap_server_metadata: Optional[LdapServerMetadataInputModel] = Field(
        default=None, alias="LdapServerMetadata"
    )
    logs: Optional[LogsModel] = Field(default=None, alias="Logs")
    maintenance_window_start_time: Optional[WeeklyStartTimeModel] = Field(
        default=None, alias="MaintenanceWindowStartTime"
    )
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroups"
    )


class CreateBrokerResponseModel(BaseModel):
    broker_arn: str = Field(alias="BrokerArn")
    broker_id: str = Field(alias="BrokerId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    authentication_strategy: Literal["LDAP", "SIMPLE"] = Field(
        alias="AuthenticationStrategy"
    )
    created: datetime = Field(alias="Created")
    id: str = Field(alias="Id")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    name: str = Field(alias="Name")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteBrokerResponseModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    authentication_strategy: Literal["LDAP", "SIMPLE"] = Field(
        alias="AuthenticationStrategy"
    )
    created: datetime = Field(alias="Created")
    description: str = Field(alias="Description")
    engine_type: Literal["ACTIVEMQ", "RABBITMQ"] = Field(alias="EngineType")
    engine_version: str = Field(alias="EngineVersion")
    id: str = Field(alias="Id")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    name: str = Field(alias="Name")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationRevisionResponseModel(BaseModel):
    configuration_id: str = Field(alias="ConfigurationId")
    created: datetime = Field(alias="Created")
    data: str = Field(alias="Data")
    description: str = Field(alias="Description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBrokersResponseModel(BaseModel):
    broker_summaries: List[BrokerSummaryModel] = Field(alias="BrokerSummaries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationRevisionsResponseModel(BaseModel):
    configuration_id: str = Field(alias="ConfigurationId")
    max_results: int = Field(alias="MaxResults")
    next_token: str = Field(alias="NextToken")
    revisions: List[ConfigurationRevisionModel] = Field(alias="Revisions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBrokerResponseModel(BaseModel):
    authentication_strategy: Literal["LDAP", "SIMPLE"] = Field(
        alias="AuthenticationStrategy"
    )
    auto_minor_version_upgrade: bool = Field(alias="AutoMinorVersionUpgrade")
    broker_id: str = Field(alias="BrokerId")
    configuration: ConfigurationIdModel = Field(alias="Configuration")
    engine_version: str = Field(alias="EngineVersion")
    host_instance_type: str = Field(alias="HostInstanceType")
    ldap_server_metadata: LdapServerMetadataOutputModel = Field(
        alias="LdapServerMetadata"
    )
    logs: LogsModel = Field(alias="Logs")
    maintenance_window_start_time: WeeklyStartTimeModel = Field(
        alias="MaintenanceWindowStartTime"
    )
    security_groups: List[str] = Field(alias="SecurityGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    max_results: int = Field(alias="MaxResults")
    next_token: str = Field(alias="NextToken")
    users: List[UserSummaryModel] = Field(alias="Users")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserResponseModel(BaseModel):
    broker_id: str = Field(alias="BrokerId")
    console_access: bool = Field(alias="ConsoleAccess")
    groups: List[str] = Field(alias="Groups")
    pending: UserPendingChangesModel = Field(alias="Pending")
    username: str = Field(alias="Username")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBrokersRequestListBrokersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LogsSummaryModel(BaseModel):
    general: bool = Field(alias="General")
    general_log_group: str = Field(alias="GeneralLogGroup")
    audit: Optional[bool] = Field(default=None, alias="Audit")
    audit_log_group: Optional[str] = Field(default=None, alias="AuditLogGroup")
    pending: Optional[PendingLogsModel] = Field(default=None, alias="Pending")


class UpdateConfigurationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created: datetime = Field(alias="Created")
    id: str = Field(alias="Id")
    latest_revision: ConfigurationRevisionModel = Field(alias="LatestRevision")
    name: str = Field(alias="Name")
    warnings: List[SanitizationWarningModel] = Field(alias="Warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBrokerInstanceOptionsResponseModel(BaseModel):
    broker_instance_options: List[BrokerInstanceOptionModel] = Field(
        alias="BrokerInstanceOptions"
    )
    max_results: int = Field(alias="MaxResults")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBrokerEngineTypesResponseModel(BaseModel):
    broker_engine_types: List[BrokerEngineTypeModel] = Field(alias="BrokerEngineTypes")
    max_results: int = Field(alias="MaxResults")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationsResponseModel(BaseModel):
    configurations: List[ConfigurationModel] = Field(alias="Configurations")
    max_results: int = Field(alias="MaxResults")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBrokerResponseModel(BaseModel):
    actions_required: List[ActionRequiredModel] = Field(alias="ActionsRequired")
    authentication_strategy: Literal["LDAP", "SIMPLE"] = Field(
        alias="AuthenticationStrategy"
    )
    auto_minor_version_upgrade: bool = Field(alias="AutoMinorVersionUpgrade")
    broker_arn: str = Field(alias="BrokerArn")
    broker_id: str = Field(alias="BrokerId")
    broker_instances: List[BrokerInstanceModel] = Field(alias="BrokerInstances")
    broker_name: str = Field(alias="BrokerName")
    broker_state: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CRITICAL_ACTION_REQUIRED",
        "DELETION_IN_PROGRESS",
        "REBOOT_IN_PROGRESS",
        "RUNNING",
    ] = Field(alias="BrokerState")
    configurations: ConfigurationsModel = Field(alias="Configurations")
    created: datetime = Field(alias="Created")
    deployment_mode: Literal[
        "ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ", "SINGLE_INSTANCE"
    ] = Field(alias="DeploymentMode")
    encryption_options: EncryptionOptionsModel = Field(alias="EncryptionOptions")
    engine_type: Literal["ACTIVEMQ", "RABBITMQ"] = Field(alias="EngineType")
    engine_version: str = Field(alias="EngineVersion")
    host_instance_type: str = Field(alias="HostInstanceType")
    ldap_server_metadata: LdapServerMetadataOutputModel = Field(
        alias="LdapServerMetadata"
    )
    logs: LogsSummaryModel = Field(alias="Logs")
    maintenance_window_start_time: WeeklyStartTimeModel = Field(
        alias="MaintenanceWindowStartTime"
    )
    pending_authentication_strategy: Literal["LDAP", "SIMPLE"] = Field(
        alias="PendingAuthenticationStrategy"
    )
    pending_engine_version: str = Field(alias="PendingEngineVersion")
    pending_host_instance_type: str = Field(alias="PendingHostInstanceType")
    pending_ldap_server_metadata: LdapServerMetadataOutputModel = Field(
        alias="PendingLdapServerMetadata"
    )
    pending_security_groups: List[str] = Field(alias="PendingSecurityGroups")
    publicly_accessible: bool = Field(alias="PubliclyAccessible")
    security_groups: List[str] = Field(alias="SecurityGroups")
    storage_type: Literal["EBS", "EFS"] = Field(alias="StorageType")
    subnet_ids: List[str] = Field(alias="SubnetIds")
    tags: Dict[str, str] = Field(alias="Tags")
    users: List[UserSummaryModel] = Field(alias="Users")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
