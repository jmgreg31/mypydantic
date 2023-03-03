# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AggregationConfigModel(BaseModel):
    aggregation_type: Optional[Literal["None", "SingleFile"]] = Field(
        default=None, alias="aggregationType"
    )
    target_file_size: Optional[int] = Field(default=None, alias="targetFileSize")


class AmplitudeConnectorProfileCredentialsModel(BaseModel):
    api_key: str = Field(alias="apiKey")
    secret_key: str = Field(alias="secretKey")


class AmplitudeSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class ApiKeyCredentialsModel(BaseModel):
    api_key: str = Field(alias="apiKey")
    api_secret_key: Optional[str] = Field(default=None, alias="apiSecretKey")


class AuthParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    is_required: Optional[bool] = Field(default=None, alias="isRequired")
    label: Optional[str] = Field(default=None, alias="label")
    description: Optional[str] = Field(default=None, alias="description")
    is_sensitive_field: Optional[bool] = Field(default=None, alias="isSensitiveField")
    connector_supplied_values: Optional[List[str]] = Field(
        default=None, alias="connectorSuppliedValues"
    )


class BasicAuthCredentialsModel(BaseModel):
    username: str = Field(alias="username")
    password: str = Field(alias="password")


class ConnectorRuntimeSettingModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    data_type: Optional[str] = Field(default=None, alias="dataType")
    is_required: Optional[bool] = Field(default=None, alias="isRequired")
    label: Optional[str] = Field(default=None, alias="label")
    description: Optional[str] = Field(default=None, alias="description")
    scope: Optional[str] = Field(default=None, alias="scope")
    connector_supplied_value_options: Optional[List[str]] = Field(
        default=None, alias="connectorSuppliedValueOptions"
    )


class ConnectorDetailModel(BaseModel):
    connector_description: Optional[str] = Field(
        default=None, alias="connectorDescription"
    )
    connector_name: Optional[str] = Field(default=None, alias="connectorName")
    connector_owner: Optional[str] = Field(default=None, alias="connectorOwner")
    connector_version: Optional[str] = Field(default=None, alias="connectorVersion")
    application_type: Optional[str] = Field(default=None, alias="applicationType")
    connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="connectorType")
    connector_label: Optional[str] = Field(default=None, alias="connectorLabel")
    registered_at: Optional[datetime] = Field(default=None, alias="registeredAt")
    registered_by: Optional[str] = Field(default=None, alias="registeredBy")
    connector_provisioning_type: Optional[Literal["LAMBDA"]] = Field(
        default=None, alias="connectorProvisioningType"
    )
    connector_modes: Optional[List[str]] = Field(default=None, alias="connectorModes")


class DestinationFieldPropertiesModel(BaseModel):
    is_creatable: Optional[bool] = Field(default=None, alias="isCreatable")
    is_nullable: Optional[bool] = Field(default=None, alias="isNullable")
    is_upsertable: Optional[bool] = Field(default=None, alias="isUpsertable")
    is_updatable: Optional[bool] = Field(default=None, alias="isUpdatable")
    is_defaulted_on_create: Optional[bool] = Field(
        default=None, alias="isDefaultedOnCreate"
    )
    supported_write_operations: Optional[
        List[Literal["DELETE", "INSERT", "UPDATE", "UPSERT"]]
    ] = Field(default=None, alias="supportedWriteOperations")


class SourceFieldPropertiesModel(BaseModel):
    is_retrievable: Optional[bool] = Field(default=None, alias="isRetrievable")
    is_queryable: Optional[bool] = Field(default=None, alias="isQueryable")
    is_timestamp_field_for_incremental_queries: Optional[bool] = Field(
        default=None, alias="isTimestampFieldForIncrementalQueries"
    )


class ConnectorEntityModel(BaseModel):
    name: str = Field(alias="name")
    label: Optional[str] = Field(default=None, alias="label")
    has_nested_entities: Optional[bool] = Field(default=None, alias="hasNestedEntities")


class GoogleAnalyticsMetadataModel(BaseModel):
    oauth_scopes: Optional[List[str]] = Field(default=None, alias="oAuthScopes")


class HoneycodeMetadataModel(BaseModel):
    oauth_scopes: Optional[List[str]] = Field(default=None, alias="oAuthScopes")


class SalesforceMetadataModel(BaseModel):
    oauth_scopes: Optional[List[str]] = Field(default=None, alias="oAuthScopes")
    data_transfer_apis: Optional[
        List[Literal["AUTOMATIC", "BULKV2", "REST_SYNC"]]
    ] = Field(default=None, alias="dataTransferApis")


class SlackMetadataModel(BaseModel):
    oauth_scopes: Optional[List[str]] = Field(default=None, alias="oAuthScopes")


class SnowflakeMetadataModel(BaseModel):
    supported_regions: Optional[List[str]] = Field(
        default=None, alias="supportedRegions"
    )


class ZendeskMetadataModel(BaseModel):
    oauth_scopes: Optional[List[str]] = Field(default=None, alias="oAuthScopes")


class ConnectorOAuthRequestModel(BaseModel):
    auth_code: Optional[str] = Field(default=None, alias="authCode")
    redirect_uri: Optional[str] = Field(default=None, alias="redirectUri")


class ConnectorOperatorModel(BaseModel):
    amplitude: Optional[Literal["BETWEEN"]] = Field(default=None, alias="Amplitude")
    datadog: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Datadog")
    dynatrace: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Dynatrace")
    google_analytics: Optional[Literal["BETWEEN", "PROJECTION"]] = Field(
        default=None, alias="GoogleAnalytics"
    )
    infor_nexus: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="InforNexus")
    marketo: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "GREATER_THAN",
            "LESS_THAN",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Marketo")
    s3: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="S3")
    salesforce: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Salesforce")
    service_now: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="ServiceNow")
    singular: Optional[
        Literal[
            "ADDITION",
            "DIVISION",
            "EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Singular")
    slack: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Slack")
    trendmicro: Optional[
        Literal[
            "ADDITION",
            "DIVISION",
            "EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Trendmicro")
    veeva: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Veeva")
    zendesk: Optional[
        Literal[
            "ADDITION",
            "DIVISION",
            "GREATER_THAN",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Zendesk")
    s_ap_odata: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="SAPOData")
    custom_connector: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="CustomConnector")
    pardot: Optional[
        Literal[
            "ADDITION",
            "DIVISION",
            "EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Pardot")


class DatadogConnectorProfileCredentialsModel(BaseModel):
    api_key: str = Field(alias="apiKey")
    application_key: str = Field(alias="applicationKey")


class DynatraceConnectorProfileCredentialsModel(BaseModel):
    api_token: str = Field(alias="apiToken")


class InforNexusConnectorProfileCredentialsModel(BaseModel):
    access_key_id: str = Field(alias="accessKeyId")
    user_id: str = Field(alias="userId")
    secret_access_key: str = Field(alias="secretAccessKey")
    datakey: str = Field(alias="datakey")


class RedshiftConnectorProfileCredentialsModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="username")
    password: Optional[str] = Field(default=None, alias="password")


class ServiceNowConnectorProfileCredentialsModel(BaseModel):
    username: str = Field(alias="username")
    password: str = Field(alias="password")


class SingularConnectorProfileCredentialsModel(BaseModel):
    api_key: str = Field(alias="apiKey")


class SnowflakeConnectorProfileCredentialsModel(BaseModel):
    username: str = Field(alias="username")
    password: str = Field(alias="password")


class TrendmicroConnectorProfileCredentialsModel(BaseModel):
    api_secret_key: str = Field(alias="apiSecretKey")


class VeevaConnectorProfileCredentialsModel(BaseModel):
    username: str = Field(alias="username")
    password: str = Field(alias="password")


class DatadogConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class DynatraceConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class InforNexusConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class MarketoConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class PardotConnectorProfilePropertiesModel(BaseModel):
    instance_url: Optional[str] = Field(default=None, alias="instanceUrl")
    is_sandbox_environment: Optional[bool] = Field(
        default=None, alias="isSandboxEnvironment"
    )
    business_unit_id: Optional[str] = Field(default=None, alias="businessUnitId")


class RedshiftConnectorProfilePropertiesModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    role_arn: str = Field(alias="roleArn")
    database_url: Optional[str] = Field(default=None, alias="databaseUrl")
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    data_api_role_arn: Optional[str] = Field(default=None, alias="dataApiRoleArn")
    is_redshift_serverless: Optional[bool] = Field(
        default=None, alias="isRedshiftServerless"
    )
    cluster_identifier: Optional[str] = Field(default=None, alias="clusterIdentifier")
    workgroup_name: Optional[str] = Field(default=None, alias="workgroupName")
    database_name: Optional[str] = Field(default=None, alias="databaseName")


class SalesforceConnectorProfilePropertiesModel(BaseModel):
    instance_url: Optional[str] = Field(default=None, alias="instanceUrl")
    is_sandbox_environment: Optional[bool] = Field(
        default=None, alias="isSandboxEnvironment"
    )
    use_private_link_for_metadata_and_authorization: Optional[bool] = Field(
        default=None, alias="usePrivateLinkForMetadataAndAuthorization"
    )


class ServiceNowConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class SlackConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class SnowflakeConnectorProfilePropertiesModel(BaseModel):
    warehouse: str = Field(alias="warehouse")
    stage: str = Field(alias="stage")
    bucket_name: str = Field(alias="bucketName")
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    private_link_service_name: Optional[str] = Field(
        default=None, alias="privateLinkServiceName"
    )
    account_name: Optional[str] = Field(default=None, alias="accountName")
    region: Optional[str] = Field(default=None, alias="region")


class VeevaConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class ZendeskConnectorProfilePropertiesModel(BaseModel):
    instance_url: str = Field(alias="instanceUrl")


class PrivateConnectionProvisioningStateModel(BaseModel):
    status: Optional[Literal["CREATED", "FAILED", "PENDING"]] = Field(
        default=None, alias="status"
    )
    failure_message: Optional[str] = Field(default=None, alias="failureMessage")
    failure_cause: Optional[
        Literal[
            "ACCESS_DENIED",
            "CONNECTOR_AUTHENTICATION",
            "CONNECTOR_SERVER",
            "INTERNAL_SERVER",
            "VALIDATION",
        ]
    ] = Field(default=None, alias="failureCause")


class LambdaConnectorProvisioningConfigModel(BaseModel):
    lambda_arn: str = Field(alias="lambdaArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CustomAuthCredentialsModel(BaseModel):
    custom_authentication_type: str = Field(alias="customAuthenticationType")
    credentials_map: Optional[Mapping[str, str]] = Field(
        default=None, alias="credentialsMap"
    )


class ErrorHandlingConfigModel(BaseModel):
    fail_on_first_destination_error: Optional[bool] = Field(
        default=None, alias="failOnFirstDestinationError"
    )
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")


class OAuth2PropertiesModel(BaseModel):
    token_url: str = Field(alias="tokenUrl")
    oauth2_grant_type: Literal["AUTHORIZATION_CODE", "CLIENT_CREDENTIALS"] = Field(
        alias="oAuth2GrantType"
    )
    token_url_custom_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="tokenUrlCustomProperties"
    )


class CustomConnectorSourcePropertiesModel(BaseModel):
    entity_name: str = Field(alias="entityName")
    custom_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="customProperties"
    )


class CustomerProfilesDestinationPropertiesModel(BaseModel):
    domain_name: str = Field(alias="domainName")
    object_type_name: Optional[str] = Field(default=None, alias="objectTypeName")


class DatadogSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class DeleteConnectorProfileRequestModel(BaseModel):
    connector_profile_name: str = Field(alias="connectorProfileName")
    force_delete: Optional[bool] = Field(default=None, alias="forceDelete")


class DeleteFlowRequestModel(BaseModel):
    flow_name: str = Field(alias="flowName")
    force_delete: Optional[bool] = Field(default=None, alias="forceDelete")


class DescribeConnectorEntityRequestModel(BaseModel):
    connector_entity_name: str = Field(alias="connectorEntityName")
    connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="connectorType")
    connector_profile_name: Optional[str] = Field(
        default=None, alias="connectorProfileName"
    )
    api_version: Optional[str] = Field(default=None, alias="apiVersion")


class DescribeConnectorProfilesRequestModel(BaseModel):
    connector_profile_names: Optional[Sequence[str]] = Field(
        default=None, alias="connectorProfileNames"
    )
    connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="connectorType")
    connector_label: Optional[str] = Field(default=None, alias="connectorLabel")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeConnectorRequestModel(BaseModel):
    connector_type: Literal[
        "Amplitude",
        "CustomConnector",
        "CustomerProfiles",
        "Datadog",
        "Dynatrace",
        "EventBridge",
        "Googleanalytics",
        "Honeycode",
        "Infornexus",
        "LookoutMetrics",
        "Marketo",
        "Pardot",
        "Redshift",
        "S3",
        "SAPOData",
        "Salesforce",
        "Servicenow",
        "Singular",
        "Slack",
        "Snowflake",
        "Trendmicro",
        "Upsolver",
        "Veeva",
        "Zendesk",
    ] = Field(alias="connectorType")
    connector_label: Optional[str] = Field(default=None, alias="connectorLabel")


class DescribeConnectorsRequestModel(BaseModel):
    connector_types: Optional[
        Sequence[
            Literal[
                "Amplitude",
                "CustomConnector",
                "CustomerProfiles",
                "Datadog",
                "Dynatrace",
                "EventBridge",
                "Googleanalytics",
                "Honeycode",
                "Infornexus",
                "LookoutMetrics",
                "Marketo",
                "Pardot",
                "Redshift",
                "S3",
                "SAPOData",
                "Salesforce",
                "Servicenow",
                "Singular",
                "Slack",
                "Snowflake",
                "Trendmicro",
                "Upsolver",
                "Veeva",
                "Zendesk",
            ]
        ]
    ] = Field(default=None, alias="connectorTypes")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeFlowExecutionRecordsRequestModel(BaseModel):
    flow_name: str = Field(alias="flowName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeFlowRequestModel(BaseModel):
    flow_name: str = Field(alias="flowName")


class ExecutionDetailsModel(BaseModel):
    most_recent_execution_message: Optional[str] = Field(
        default=None, alias="mostRecentExecutionMessage"
    )
    most_recent_execution_time: Optional[datetime] = Field(
        default=None, alias="mostRecentExecutionTime"
    )
    most_recent_execution_status: Optional[
        Literal["Error", "InProgress", "Successful"]
    ] = Field(default=None, alias="mostRecentExecutionStatus")


class DynatraceSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class ErrorInfoModel(BaseModel):
    put_failures_count: Optional[int] = Field(default=None, alias="putFailuresCount")
    execution_message: Optional[str] = Field(default=None, alias="executionMessage")


class RangeModel(BaseModel):
    maximum: Optional[float] = Field(default=None, alias="maximum")
    minimum: Optional[float] = Field(default=None, alias="minimum")


class GlueDataCatalogConfigModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    database_name: str = Field(alias="databaseName")
    table_prefix: str = Field(alias="tablePrefix")


class GoogleAnalyticsSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class IncrementalPullConfigModel(BaseModel):
    datetime_type_field_name: Optional[str] = Field(
        default=None, alias="datetimeTypeFieldName"
    )


class InforNexusSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class ListConnectorEntitiesRequestModel(BaseModel):
    connector_profile_name: Optional[str] = Field(
        default=None, alias="connectorProfileName"
    )
    connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="connectorType")
    entities_path: Optional[str] = Field(default=None, alias="entitiesPath")
    api_version: Optional[str] = Field(default=None, alias="apiVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListConnectorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListFlowsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class MarketoSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class RegistrationOutputModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")
    result: Optional[str] = Field(default=None, alias="result")
    status: Optional[Literal["Error", "InProgress", "Successful"]] = Field(
        default=None, alias="status"
    )


class OAuth2CustomParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    is_required: Optional[bool] = Field(default=None, alias="isRequired")
    label: Optional[str] = Field(default=None, alias="label")
    description: Optional[str] = Field(default=None, alias="description")
    is_sensitive_field: Optional[bool] = Field(default=None, alias="isSensitiveField")
    connector_supplied_values: Optional[List[str]] = Field(
        default=None, alias="connectorSuppliedValues"
    )
    type: Optional[Literal["AUTH_URL", "TOKEN_URL"]] = Field(default=None, alias="type")


class OAuthPropertiesModel(BaseModel):
    token_url: str = Field(alias="tokenUrl")
    auth_code_url: str = Field(alias="authCodeUrl")
    oauth_scopes: Sequence[str] = Field(alias="oAuthScopes")


class PardotSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class PrefixConfigModel(BaseModel):
    prefix_type: Optional[Literal["FILENAME", "PATH", "PATH_AND_FILENAME"]] = Field(
        default=None, alias="prefixType"
    )
    prefix_format: Optional[Literal["DAY", "HOUR", "MINUTE", "MONTH", "YEAR"]] = Field(
        default=None, alias="prefixFormat"
    )
    path_prefix_hierarchy: Optional[
        Sequence[Literal["EXECUTION_ID", "SCHEMA_VERSION"]]
    ] = Field(default=None, alias="pathPrefixHierarchy")


class S3InputFormatConfigModel(BaseModel):
    s3_input_file_type: Optional[Literal["CSV", "JSON"]] = Field(
        default=None, alias="s3InputFileType"
    )


class SuccessResponseHandlingConfigModel(BaseModel):
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    bucket_name: Optional[str] = Field(default=None, alias="bucketName")


class SAPODataSourcePropertiesModel(BaseModel):
    object_path: Optional[str] = Field(default=None, alias="objectPath")


class SalesforceSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")
    enable_dynamic_field_update: Optional[bool] = Field(
        default=None, alias="enableDynamicFieldUpdate"
    )
    include_deleted_records: Optional[bool] = Field(
        default=None, alias="includeDeletedRecords"
    )
    data_transfer_api: Optional[Literal["AUTOMATIC", "BULKV2", "REST_SYNC"]] = Field(
        default=None, alias="dataTransferApi"
    )


class ScheduledTriggerPropertiesModel(BaseModel):
    schedule_expression: str = Field(alias="scheduleExpression")
    data_pull_mode: Optional[Literal["Complete", "Incremental"]] = Field(
        default=None, alias="dataPullMode"
    )
    schedule_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="scheduleStartTime"
    )
    schedule_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="scheduleEndTime"
    )
    timezone: Optional[str] = Field(default=None, alias="timezone")
    schedule_offset: Optional[int] = Field(default=None, alias="scheduleOffset")
    first_execution_from: Optional[Union[datetime, str]] = Field(
        default=None, alias="firstExecutionFrom"
    )
    flow_error_deactivation_threshold: Optional[int] = Field(
        default=None, alias="flowErrorDeactivationThreshold"
    )


class ServiceNowSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class SingularSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class SlackSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class TrendmicroSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class VeevaSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")
    document_type: Optional[str] = Field(default=None, alias="documentType")
    include_source_files: Optional[bool] = Field(
        default=None, alias="includeSourceFiles"
    )
    include_renditions: Optional[bool] = Field(default=None, alias="includeRenditions")
    include_all_versions: Optional[bool] = Field(
        default=None, alias="includeAllVersions"
    )


class ZendeskSourcePropertiesModel(BaseModel):
    object: str = Field(alias="object")


class StartFlowRequestModel(BaseModel):
    flow_name: str = Field(alias="flowName")


class StopFlowRequestModel(BaseModel):
    flow_name: str = Field(alias="flowName")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UnregisterConnectorRequestModel(BaseModel):
    connector_label: str = Field(alias="connectorLabel")
    force_delete: Optional[bool] = Field(default=None, alias="forceDelete")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CustomAuthConfigModel(BaseModel):
    custom_authentication_type: Optional[str] = Field(
        default=None, alias="customAuthenticationType"
    )
    auth_parameters: Optional[List[AuthParameterModel]] = Field(
        default=None, alias="authParameters"
    )


class ConnectorMetadataModel(BaseModel):
    amplitude: Optional[Dict[str, Any]] = Field(default=None, alias="Amplitude")
    datadog: Optional[Dict[str, Any]] = Field(default=None, alias="Datadog")
    dynatrace: Optional[Dict[str, Any]] = Field(default=None, alias="Dynatrace")
    google_analytics: Optional[GoogleAnalyticsMetadataModel] = Field(
        default=None, alias="GoogleAnalytics"
    )
    infor_nexus: Optional[Dict[str, Any]] = Field(default=None, alias="InforNexus")
    marketo: Optional[Dict[str, Any]] = Field(default=None, alias="Marketo")
    redshift: Optional[Dict[str, Any]] = Field(default=None, alias="Redshift")
    s3: Optional[Dict[str, Any]] = Field(default=None, alias="S3")
    salesforce: Optional[SalesforceMetadataModel] = Field(
        default=None, alias="Salesforce"
    )
    service_now: Optional[Dict[str, Any]] = Field(default=None, alias="ServiceNow")
    singular: Optional[Dict[str, Any]] = Field(default=None, alias="Singular")
    slack: Optional[SlackMetadataModel] = Field(default=None, alias="Slack")
    snowflake: Optional[SnowflakeMetadataModel] = Field(default=None, alias="Snowflake")
    trendmicro: Optional[Dict[str, Any]] = Field(default=None, alias="Trendmicro")
    veeva: Optional[Dict[str, Any]] = Field(default=None, alias="Veeva")
    zendesk: Optional[ZendeskMetadataModel] = Field(default=None, alias="Zendesk")
    event_bridge: Optional[Dict[str, Any]] = Field(default=None, alias="EventBridge")
    upsolver: Optional[Dict[str, Any]] = Field(default=None, alias="Upsolver")
    customer_profiles: Optional[Dict[str, Any]] = Field(
        default=None, alias="CustomerProfiles"
    )
    honeycode: Optional[HoneycodeMetadataModel] = Field(default=None, alias="Honeycode")
    s_ap_odata: Optional[Dict[str, Any]] = Field(default=None, alias="SAPOData")
    pardot: Optional[Dict[str, Any]] = Field(default=None, alias="Pardot")


class GoogleAnalyticsConnectorProfileCredentialsModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    refresh_token: Optional[str] = Field(default=None, alias="refreshToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )


class HoneycodeConnectorProfileCredentialsModel(BaseModel):
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    refresh_token: Optional[str] = Field(default=None, alias="refreshToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )


class MarketoConnectorProfileCredentialsModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )


class OAuth2CredentialsModel(BaseModel):
    client_id: Optional[str] = Field(default=None, alias="clientId")
    client_secret: Optional[str] = Field(default=None, alias="clientSecret")
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    refresh_token: Optional[str] = Field(default=None, alias="refreshToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )


class OAuthCredentialsModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    refresh_token: Optional[str] = Field(default=None, alias="refreshToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )


class PardotConnectorProfileCredentialsModel(BaseModel):
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    refresh_token: Optional[str] = Field(default=None, alias="refreshToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )
    client_credentials_arn: Optional[str] = Field(
        default=None, alias="clientCredentialsArn"
    )


class SalesforceConnectorProfileCredentialsModel(BaseModel):
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    refresh_token: Optional[str] = Field(default=None, alias="refreshToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )
    client_credentials_arn: Optional[str] = Field(
        default=None, alias="clientCredentialsArn"
    )


class SlackConnectorProfileCredentialsModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )


class ZendeskConnectorProfileCredentialsModel(BaseModel):
    client_id: str = Field(alias="clientId")
    client_secret: str = Field(alias="clientSecret")
    access_token: Optional[str] = Field(default=None, alias="accessToken")
    oauth_request: Optional[ConnectorOAuthRequestModel] = Field(
        default=None, alias="oAuthRequest"
    )


class TaskModel(BaseModel):
    source_fields: Sequence[str] = Field(alias="sourceFields")
    task_type: Literal[
        "Arithmetic",
        "Filter",
        "Map",
        "Map_all",
        "Mask",
        "Merge",
        "Partition",
        "Passthrough",
        "Truncate",
        "Validate",
    ] = Field(alias="taskType")
    connector_operator: Optional[ConnectorOperatorModel] = Field(
        default=None, alias="connectorOperator"
    )
    destination_field: Optional[str] = Field(default=None, alias="destinationField")
    task_properties: Optional[
        Mapping[
            Literal[
                "CONCAT_FORMAT",
                "DATA_TYPE",
                "DESTINATION_DATA_TYPE",
                "EXCLUDE_SOURCE_FIELDS_LIST",
                "INCLUDE_NEW_FIELDS",
                "LOWER_BOUND",
                "MASK_LENGTH",
                "MASK_VALUE",
                "MATH_OPERATION_FIELDS_ORDER",
                "ORDERED_PARTITION_KEYS_LIST",
                "SOURCE_DATA_TYPE",
                "SUBFIELD_CATEGORY_MAP",
                "TRUNCATE_LENGTH",
                "UPPER_BOUND",
                "VALIDATION_ACTION",
                "VALUE",
                "VALUES",
            ],
            str,
        ]
    ] = Field(default=None, alias="taskProperties")


class ConnectorProvisioningConfigModel(BaseModel):
    lambda_: Optional[LambdaConnectorProvisioningConfigModel] = Field(
        default=None, alias="lambda"
    )


class CreateConnectorProfileResponseModel(BaseModel):
    connector_profile_arn: str = Field(alias="connectorProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFlowResponseModel(BaseModel):
    flow_arn: str = Field(alias="flowArn")
    flow_status: Literal[
        "Active", "Deleted", "Deprecated", "Draft", "Errored", "Suspended"
    ] = Field(alias="flowStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConnectorEntitiesResponseModel(BaseModel):
    connector_entity_map: Dict[str, List[ConnectorEntityModel]] = Field(
        alias="connectorEntityMap"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConnectorsResponseModel(BaseModel):
    connectors: List[ConnectorDetailModel] = Field(alias="connectors")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterConnectorResponseModel(BaseModel):
    connector_arn: str = Field(alias="connectorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFlowResponseModel(BaseModel):
    flow_arn: str = Field(alias="flowArn")
    flow_status: Literal[
        "Active", "Deleted", "Deprecated", "Draft", "Errored", "Suspended"
    ] = Field(alias="flowStatus")
    execution_id: str = Field(alias="executionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopFlowResponseModel(BaseModel):
    flow_arn: str = Field(alias="flowArn")
    flow_status: Literal[
        "Active", "Deleted", "Deprecated", "Draft", "Errored", "Suspended"
    ] = Field(alias="flowStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectorProfileResponseModel(BaseModel):
    connector_profile_arn: str = Field(alias="connectorProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectorRegistrationResponseModel(BaseModel):
    connector_arn: str = Field(alias="connectorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlowResponseModel(BaseModel):
    flow_status: Literal[
        "Active", "Deleted", "Deprecated", "Draft", "Errored", "Suspended"
    ] = Field(alias="flowStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomConnectorDestinationPropertiesModel(BaseModel):
    entity_name: str = Field(alias="entityName")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )
    write_operation_type: Optional[
        Literal["DELETE", "INSERT", "UPDATE", "UPSERT"]
    ] = Field(default=None, alias="writeOperationType")
    id_field_names: Optional[Sequence[str]] = Field(default=None, alias="idFieldNames")
    custom_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="customProperties"
    )


class EventBridgeDestinationPropertiesModel(BaseModel):
    object: str = Field(alias="object")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )


class HoneycodeDestinationPropertiesModel(BaseModel):
    object: str = Field(alias="object")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )


class MarketoDestinationPropertiesModel(BaseModel):
    object: str = Field(alias="object")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )


class RedshiftDestinationPropertiesModel(BaseModel):
    object: str = Field(alias="object")
    intermediate_bucket_name: str = Field(alias="intermediateBucketName")
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )


class SalesforceDestinationPropertiesModel(BaseModel):
    object: str = Field(alias="object")
    id_field_names: Optional[Sequence[str]] = Field(default=None, alias="idFieldNames")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )
    write_operation_type: Optional[
        Literal["DELETE", "INSERT", "UPDATE", "UPSERT"]
    ] = Field(default=None, alias="writeOperationType")
    data_transfer_api: Optional[Literal["AUTOMATIC", "BULKV2", "REST_SYNC"]] = Field(
        default=None, alias="dataTransferApi"
    )


class SnowflakeDestinationPropertiesModel(BaseModel):
    object: str = Field(alias="object")
    intermediate_bucket_name: str = Field(alias="intermediateBucketName")
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )


class ZendeskDestinationPropertiesModel(BaseModel):
    object: str = Field(alias="object")
    id_field_names: Optional[Sequence[str]] = Field(default=None, alias="idFieldNames")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )
    write_operation_type: Optional[
        Literal["DELETE", "INSERT", "UPDATE", "UPSERT"]
    ] = Field(default=None, alias="writeOperationType")


class CustomConnectorProfilePropertiesModel(BaseModel):
    profile_properties: Optional[Mapping[str, str]] = Field(
        default=None, alias="profileProperties"
    )
    oauth2_properties: Optional[OAuth2PropertiesModel] = Field(
        default=None, alias="oAuth2Properties"
    )


class FlowDefinitionModel(BaseModel):
    flow_arn: Optional[str] = Field(default=None, alias="flowArn")
    description: Optional[str] = Field(default=None, alias="description")
    flow_name: Optional[str] = Field(default=None, alias="flowName")
    flow_status: Optional[
        Literal["Active", "Deleted", "Deprecated", "Draft", "Errored", "Suspended"]
    ] = Field(default=None, alias="flowStatus")
    source_connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="sourceConnectorType")
    source_connector_label: Optional[str] = Field(
        default=None, alias="sourceConnectorLabel"
    )
    destination_connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="destinationConnectorType")
    destination_connector_label: Optional[str] = Field(
        default=None, alias="destinationConnectorLabel"
    )
    trigger_type: Optional[Literal["Event", "OnDemand", "Scheduled"]] = Field(
        default=None, alias="triggerType"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    last_updated_by: Optional[str] = Field(default=None, alias="lastUpdatedBy")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    last_run_execution_details: Optional[ExecutionDetailsModel] = Field(
        default=None, alias="lastRunExecutionDetails"
    )


class ExecutionResultModel(BaseModel):
    error_info: Optional[ErrorInfoModel] = Field(default=None, alias="errorInfo")
    bytes_processed: Optional[int] = Field(default=None, alias="bytesProcessed")
    bytes_written: Optional[int] = Field(default=None, alias="bytesWritten")
    records_processed: Optional[int] = Field(default=None, alias="recordsProcessed")


class FieldTypeDetailsModel(BaseModel):
    field_type: str = Field(alias="fieldType")
    filter_operators: List[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(alias="filterOperators")
    supported_values: Optional[List[str]] = Field(default=None, alias="supportedValues")
    value_regex_pattern: Optional[str] = Field(default=None, alias="valueRegexPattern")
    supported_date_format: Optional[str] = Field(
        default=None, alias="supportedDateFormat"
    )
    field_value_range: Optional[RangeModel] = Field(
        default=None, alias="fieldValueRange"
    )
    field_length_range: Optional[RangeModel] = Field(
        default=None, alias="fieldLengthRange"
    )


class MetadataCatalogConfigModel(BaseModel):
    glue_data_catalog: Optional[GlueDataCatalogConfigModel] = Field(
        default=None, alias="glueDataCatalog"
    )


class MetadataCatalogDetailModel(BaseModel):
    catalog_type: Optional[Literal["GLUE"]] = Field(default=None, alias="catalogType")
    table_name: Optional[str] = Field(default=None, alias="tableName")
    table_registration_output: Optional[RegistrationOutputModel] = Field(
        default=None, alias="tableRegistrationOutput"
    )
    partition_registration_output: Optional[RegistrationOutputModel] = Field(
        default=None, alias="partitionRegistrationOutput"
    )


class OAuth2DefaultsModel(BaseModel):
    oauth_scopes: Optional[List[str]] = Field(default=None, alias="oauthScopes")
    token_urls: Optional[List[str]] = Field(default=None, alias="tokenUrls")
    auth_code_urls: Optional[List[str]] = Field(default=None, alias="authCodeUrls")
    oauth2_grant_types_supported: Optional[
        List[Literal["AUTHORIZATION_CODE", "CLIENT_CREDENTIALS"]]
    ] = Field(default=None, alias="oauth2GrantTypesSupported")
    oauth2_custom_properties: Optional[List[OAuth2CustomParameterModel]] = Field(
        default=None, alias="oauth2CustomProperties"
    )


class SAPODataConnectorProfilePropertiesModel(BaseModel):
    application_host_url: str = Field(alias="applicationHostUrl")
    application_service_path: str = Field(alias="applicationServicePath")
    port_number: int = Field(alias="portNumber")
    client_number: str = Field(alias="clientNumber")
    logon_language: Optional[str] = Field(default=None, alias="logonLanguage")
    private_link_service_name: Optional[str] = Field(
        default=None, alias="privateLinkServiceName"
    )
    oauth_properties: Optional[OAuthPropertiesModel] = Field(
        default=None, alias="oAuthProperties"
    )


class S3OutputFormatConfigModel(BaseModel):
    file_type: Optional[Literal["CSV", "JSON", "PARQUET"]] = Field(
        default=None, alias="fileType"
    )
    prefix_config: Optional[PrefixConfigModel] = Field(
        default=None, alias="prefixConfig"
    )
    aggregation_config: Optional[AggregationConfigModel] = Field(
        default=None, alias="aggregationConfig"
    )
    preserve_source_data_typing: Optional[bool] = Field(
        default=None, alias="preserveSourceDataTyping"
    )


class UpsolverS3OutputFormatConfigModel(BaseModel):
    prefix_config: PrefixConfigModel = Field(alias="prefixConfig")
    file_type: Optional[Literal["CSV", "JSON", "PARQUET"]] = Field(
        default=None, alias="fileType"
    )
    aggregation_config: Optional[AggregationConfigModel] = Field(
        default=None, alias="aggregationConfig"
    )


class S3SourcePropertiesModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    s3_input_format_config: Optional[S3InputFormatConfigModel] = Field(
        default=None, alias="s3InputFormatConfig"
    )


class SAPODataDestinationPropertiesModel(BaseModel):
    object_path: str = Field(alias="objectPath")
    success_response_handling_config: Optional[
        SuccessResponseHandlingConfigModel
    ] = Field(default=None, alias="successResponseHandlingConfig")
    id_field_names: Optional[Sequence[str]] = Field(default=None, alias="idFieldNames")
    error_handling_config: Optional[ErrorHandlingConfigModel] = Field(
        default=None, alias="errorHandlingConfig"
    )
    write_operation_type: Optional[
        Literal["DELETE", "INSERT", "UPDATE", "UPSERT"]
    ] = Field(default=None, alias="writeOperationType")


class TriggerPropertiesModel(BaseModel):
    scheduled: Optional[ScheduledTriggerPropertiesModel] = Field(
        default=None, alias="Scheduled"
    )


class CustomConnectorProfileCredentialsModel(BaseModel):
    authentication_type: Literal["APIKEY", "BASIC", "CUSTOM", "OAUTH2"] = Field(
        alias="authenticationType"
    )
    basic: Optional[BasicAuthCredentialsModel] = Field(default=None, alias="basic")
    oauth2: Optional[OAuth2CredentialsModel] = Field(default=None, alias="oauth2")
    api_key: Optional[ApiKeyCredentialsModel] = Field(default=None, alias="apiKey")
    custom: Optional[CustomAuthCredentialsModel] = Field(default=None, alias="custom")


class SAPODataConnectorProfileCredentialsModel(BaseModel):
    basic_auth_credentials: Optional[BasicAuthCredentialsModel] = Field(
        default=None, alias="basicAuthCredentials"
    )
    oauth_credentials: Optional[OAuthCredentialsModel] = Field(
        default=None, alias="oAuthCredentials"
    )


class RegisterConnectorRequestModel(BaseModel):
    connector_label: Optional[str] = Field(default=None, alias="connectorLabel")
    description: Optional[str] = Field(default=None, alias="description")
    connector_provisioning_type: Optional[Literal["LAMBDA"]] = Field(
        default=None, alias="connectorProvisioningType"
    )
    connector_provisioning_config: Optional[ConnectorProvisioningConfigModel] = Field(
        default=None, alias="connectorProvisioningConfig"
    )


class UpdateConnectorRegistrationRequestModel(BaseModel):
    connector_label: str = Field(alias="connectorLabel")
    description: Optional[str] = Field(default=None, alias="description")
    connector_provisioning_config: Optional[ConnectorProvisioningConfigModel] = Field(
        default=None, alias="connectorProvisioningConfig"
    )


class ListFlowsResponseModel(BaseModel):
    flows: List[FlowDefinitionModel] = Field(alias="flows")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SupportedFieldTypeDetailsModel(BaseModel):
    v1: FieldTypeDetailsModel = Field(alias="v1")


class ExecutionRecordModel(BaseModel):
    execution_id: Optional[str] = Field(default=None, alias="executionId")
    execution_status: Optional[Literal["Error", "InProgress", "Successful"]] = Field(
        default=None, alias="executionStatus"
    )
    execution_result: Optional[ExecutionResultModel] = Field(
        default=None, alias="executionResult"
    )
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    data_pull_start_time: Optional[datetime] = Field(
        default=None, alias="dataPullStartTime"
    )
    data_pull_end_time: Optional[datetime] = Field(
        default=None, alias="dataPullEndTime"
    )
    metadata_catalog_details: Optional[List[MetadataCatalogDetailModel]] = Field(
        default=None, alias="metadataCatalogDetails"
    )


class AuthenticationConfigModel(BaseModel):
    is_basic_auth_supported: Optional[bool] = Field(
        default=None, alias="isBasicAuthSupported"
    )
    is_api_key_auth_supported: Optional[bool] = Field(
        default=None, alias="isApiKeyAuthSupported"
    )
    is_oauth2_supported: Optional[bool] = Field(default=None, alias="isOAuth2Supported")
    is_custom_auth_supported: Optional[bool] = Field(
        default=None, alias="isCustomAuthSupported"
    )
    oauth2_defaults: Optional[OAuth2DefaultsModel] = Field(
        default=None, alias="oAuth2Defaults"
    )
    custom_auth_configs: Optional[List[CustomAuthConfigModel]] = Field(
        default=None, alias="customAuthConfigs"
    )


class ConnectorProfilePropertiesModel(BaseModel):
    amplitude: Optional[Mapping[str, Any]] = Field(default=None, alias="Amplitude")
    datadog: Optional[DatadogConnectorProfilePropertiesModel] = Field(
        default=None, alias="Datadog"
    )
    dynatrace: Optional[DynatraceConnectorProfilePropertiesModel] = Field(
        default=None, alias="Dynatrace"
    )
    google_analytics: Optional[Mapping[str, Any]] = Field(
        default=None, alias="GoogleAnalytics"
    )
    honeycode: Optional[Mapping[str, Any]] = Field(default=None, alias="Honeycode")
    infor_nexus: Optional[InforNexusConnectorProfilePropertiesModel] = Field(
        default=None, alias="InforNexus"
    )
    marketo: Optional[MarketoConnectorProfilePropertiesModel] = Field(
        default=None, alias="Marketo"
    )
    redshift: Optional[RedshiftConnectorProfilePropertiesModel] = Field(
        default=None, alias="Redshift"
    )
    salesforce: Optional[SalesforceConnectorProfilePropertiesModel] = Field(
        default=None, alias="Salesforce"
    )
    service_now: Optional[ServiceNowConnectorProfilePropertiesModel] = Field(
        default=None, alias="ServiceNow"
    )
    singular: Optional[Mapping[str, Any]] = Field(default=None, alias="Singular")
    slack: Optional[SlackConnectorProfilePropertiesModel] = Field(
        default=None, alias="Slack"
    )
    snowflake: Optional[SnowflakeConnectorProfilePropertiesModel] = Field(
        default=None, alias="Snowflake"
    )
    trendmicro: Optional[Mapping[str, Any]] = Field(default=None, alias="Trendmicro")
    veeva: Optional[VeevaConnectorProfilePropertiesModel] = Field(
        default=None, alias="Veeva"
    )
    zendesk: Optional[ZendeskConnectorProfilePropertiesModel] = Field(
        default=None, alias="Zendesk"
    )
    s_ap_odata: Optional[SAPODataConnectorProfilePropertiesModel] = Field(
        default=None, alias="SAPOData"
    )
    custom_connector: Optional[CustomConnectorProfilePropertiesModel] = Field(
        default=None, alias="CustomConnector"
    )
    pardot: Optional[PardotConnectorProfilePropertiesModel] = Field(
        default=None, alias="Pardot"
    )


class S3DestinationPropertiesModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")
    s3_output_format_config: Optional[S3OutputFormatConfigModel] = Field(
        default=None, alias="s3OutputFormatConfig"
    )


class UpsolverDestinationPropertiesModel(BaseModel):
    bucket_name: str = Field(alias="bucketName")
    s3_output_format_config: UpsolverS3OutputFormatConfigModel = Field(
        alias="s3OutputFormatConfig"
    )
    bucket_prefix: Optional[str] = Field(default=None, alias="bucketPrefix")


class SourceConnectorPropertiesModel(BaseModel):
    amplitude: Optional[AmplitudeSourcePropertiesModel] = Field(
        default=None, alias="Amplitude"
    )
    datadog: Optional[DatadogSourcePropertiesModel] = Field(
        default=None, alias="Datadog"
    )
    dynatrace: Optional[DynatraceSourcePropertiesModel] = Field(
        default=None, alias="Dynatrace"
    )
    google_analytics: Optional[GoogleAnalyticsSourcePropertiesModel] = Field(
        default=None, alias="GoogleAnalytics"
    )
    infor_nexus: Optional[InforNexusSourcePropertiesModel] = Field(
        default=None, alias="InforNexus"
    )
    marketo: Optional[MarketoSourcePropertiesModel] = Field(
        default=None, alias="Marketo"
    )
    s3: Optional[S3SourcePropertiesModel] = Field(default=None, alias="S3")
    salesforce: Optional[SalesforceSourcePropertiesModel] = Field(
        default=None, alias="Salesforce"
    )
    service_now: Optional[ServiceNowSourcePropertiesModel] = Field(
        default=None, alias="ServiceNow"
    )
    singular: Optional[SingularSourcePropertiesModel] = Field(
        default=None, alias="Singular"
    )
    slack: Optional[SlackSourcePropertiesModel] = Field(default=None, alias="Slack")
    trendmicro: Optional[TrendmicroSourcePropertiesModel] = Field(
        default=None, alias="Trendmicro"
    )
    veeva: Optional[VeevaSourcePropertiesModel] = Field(default=None, alias="Veeva")
    zendesk: Optional[ZendeskSourcePropertiesModel] = Field(
        default=None, alias="Zendesk"
    )
    s_ap_odata: Optional[SAPODataSourcePropertiesModel] = Field(
        default=None, alias="SAPOData"
    )
    custom_connector: Optional[CustomConnectorSourcePropertiesModel] = Field(
        default=None, alias="CustomConnector"
    )
    pardot: Optional[PardotSourcePropertiesModel] = Field(default=None, alias="Pardot")


class TriggerConfigModel(BaseModel):
    trigger_type: Literal["Event", "OnDemand", "Scheduled"] = Field(alias="triggerType")
    trigger_properties: Optional[TriggerPropertiesModel] = Field(
        default=None, alias="triggerProperties"
    )


class ConnectorProfileCredentialsModel(BaseModel):
    amplitude: Optional[AmplitudeConnectorProfileCredentialsModel] = Field(
        default=None, alias="Amplitude"
    )
    datadog: Optional[DatadogConnectorProfileCredentialsModel] = Field(
        default=None, alias="Datadog"
    )
    dynatrace: Optional[DynatraceConnectorProfileCredentialsModel] = Field(
        default=None, alias="Dynatrace"
    )
    google_analytics: Optional[GoogleAnalyticsConnectorProfileCredentialsModel] = Field(
        default=None, alias="GoogleAnalytics"
    )
    honeycode: Optional[HoneycodeConnectorProfileCredentialsModel] = Field(
        default=None, alias="Honeycode"
    )
    infor_nexus: Optional[InforNexusConnectorProfileCredentialsModel] = Field(
        default=None, alias="InforNexus"
    )
    marketo: Optional[MarketoConnectorProfileCredentialsModel] = Field(
        default=None, alias="Marketo"
    )
    redshift: Optional[RedshiftConnectorProfileCredentialsModel] = Field(
        default=None, alias="Redshift"
    )
    salesforce: Optional[SalesforceConnectorProfileCredentialsModel] = Field(
        default=None, alias="Salesforce"
    )
    service_now: Optional[ServiceNowConnectorProfileCredentialsModel] = Field(
        default=None, alias="ServiceNow"
    )
    singular: Optional[SingularConnectorProfileCredentialsModel] = Field(
        default=None, alias="Singular"
    )
    slack: Optional[SlackConnectorProfileCredentialsModel] = Field(
        default=None, alias="Slack"
    )
    snowflake: Optional[SnowflakeConnectorProfileCredentialsModel] = Field(
        default=None, alias="Snowflake"
    )
    trendmicro: Optional[TrendmicroConnectorProfileCredentialsModel] = Field(
        default=None, alias="Trendmicro"
    )
    veeva: Optional[VeevaConnectorProfileCredentialsModel] = Field(
        default=None, alias="Veeva"
    )
    zendesk: Optional[ZendeskConnectorProfileCredentialsModel] = Field(
        default=None, alias="Zendesk"
    )
    s_ap_odata: Optional[SAPODataConnectorProfileCredentialsModel] = Field(
        default=None, alias="SAPOData"
    )
    custom_connector: Optional[CustomConnectorProfileCredentialsModel] = Field(
        default=None, alias="CustomConnector"
    )
    pardot: Optional[PardotConnectorProfileCredentialsModel] = Field(
        default=None, alias="Pardot"
    )


class ConnectorEntityFieldModel(BaseModel):
    identifier: str = Field(alias="identifier")
    parent_identifier: Optional[str] = Field(default=None, alias="parentIdentifier")
    label: Optional[str] = Field(default=None, alias="label")
    is_primary_key: Optional[bool] = Field(default=None, alias="isPrimaryKey")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    is_deprecated: Optional[bool] = Field(default=None, alias="isDeprecated")
    supported_field_type_details: Optional[SupportedFieldTypeDetailsModel] = Field(
        default=None, alias="supportedFieldTypeDetails"
    )
    description: Optional[str] = Field(default=None, alias="description")
    source_properties: Optional[SourceFieldPropertiesModel] = Field(
        default=None, alias="sourceProperties"
    )
    destination_properties: Optional[DestinationFieldPropertiesModel] = Field(
        default=None, alias="destinationProperties"
    )
    custom_properties: Optional[Dict[str, str]] = Field(
        default=None, alias="customProperties"
    )


class DescribeFlowExecutionRecordsResponseModel(BaseModel):
    flow_executions: List[ExecutionRecordModel] = Field(alias="flowExecutions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConnectorConfigurationModel(BaseModel):
    can_use_as_source: Optional[bool] = Field(default=None, alias="canUseAsSource")
    can_use_as_destination: Optional[bool] = Field(
        default=None, alias="canUseAsDestination"
    )
    supported_destination_connectors: Optional[
        List[
            Literal[
                "Amplitude",
                "CustomConnector",
                "CustomerProfiles",
                "Datadog",
                "Dynatrace",
                "EventBridge",
                "Googleanalytics",
                "Honeycode",
                "Infornexus",
                "LookoutMetrics",
                "Marketo",
                "Pardot",
                "Redshift",
                "S3",
                "SAPOData",
                "Salesforce",
                "Servicenow",
                "Singular",
                "Slack",
                "Snowflake",
                "Trendmicro",
                "Upsolver",
                "Veeva",
                "Zendesk",
            ]
        ]
    ] = Field(default=None, alias="supportedDestinationConnectors")
    supported_scheduling_frequencies: Optional[
        List[Literal["BYMINUTE", "DAILY", "HOURLY", "MONTHLY", "ONCE", "WEEKLY"]]
    ] = Field(default=None, alias="supportedSchedulingFrequencies")
    is_private_link_enabled: Optional[bool] = Field(
        default=None, alias="isPrivateLinkEnabled"
    )
    is_private_link_endpoint_url_required: Optional[bool] = Field(
        default=None, alias="isPrivateLinkEndpointUrlRequired"
    )
    supported_trigger_types: Optional[
        List[Literal["Event", "OnDemand", "Scheduled"]]
    ] = Field(default=None, alias="supportedTriggerTypes")
    connector_metadata: Optional[ConnectorMetadataModel] = Field(
        default=None, alias="connectorMetadata"
    )
    connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="connectorType")
    connector_label: Optional[str] = Field(default=None, alias="connectorLabel")
    connector_description: Optional[str] = Field(
        default=None, alias="connectorDescription"
    )
    connector_owner: Optional[str] = Field(default=None, alias="connectorOwner")
    connector_name: Optional[str] = Field(default=None, alias="connectorName")
    connector_version: Optional[str] = Field(default=None, alias="connectorVersion")
    connector_arn: Optional[str] = Field(default=None, alias="connectorArn")
    connector_modes: Optional[List[str]] = Field(default=None, alias="connectorModes")
    authentication_config: Optional[AuthenticationConfigModel] = Field(
        default=None, alias="authenticationConfig"
    )
    connector_runtime_settings: Optional[List[ConnectorRuntimeSettingModel]] = Field(
        default=None, alias="connectorRuntimeSettings"
    )
    supported_api_versions: Optional[List[str]] = Field(
        default=None, alias="supportedApiVersions"
    )
    supported_operators: Optional[
        List[
            Literal[
                "ADDITION",
                "BETWEEN",
                "CONTAINS",
                "DIVISION",
                "EQUAL_TO",
                "GREATER_THAN",
                "GREATER_THAN_OR_EQUAL_TO",
                "LESS_THAN",
                "LESS_THAN_OR_EQUAL_TO",
                "MASK_ALL",
                "MASK_FIRST_N",
                "MASK_LAST_N",
                "MULTIPLICATION",
                "NOT_EQUAL_TO",
                "NO_OP",
                "PROJECTION",
                "SUBTRACTION",
                "VALIDATE_NON_NEGATIVE",
                "VALIDATE_NON_NULL",
                "VALIDATE_NON_ZERO",
                "VALIDATE_NUMERIC",
            ]
        ]
    ] = Field(default=None, alias="supportedOperators")
    supported_write_operations: Optional[
        List[Literal["DELETE", "INSERT", "UPDATE", "UPSERT"]]
    ] = Field(default=None, alias="supportedWriteOperations")
    connector_provisioning_type: Optional[Literal["LAMBDA"]] = Field(
        default=None, alias="connectorProvisioningType"
    )
    connector_provisioning_config: Optional[ConnectorProvisioningConfigModel] = Field(
        default=None, alias="connectorProvisioningConfig"
    )
    logo_url: Optional[str] = Field(default=None, alias="logoURL")
    registered_at: Optional[datetime] = Field(default=None, alias="registeredAt")
    registered_by: Optional[str] = Field(default=None, alias="registeredBy")


class ConnectorProfileModel(BaseModel):
    connector_profile_arn: Optional[str] = Field(
        default=None, alias="connectorProfileArn"
    )
    connector_profile_name: Optional[str] = Field(
        default=None, alias="connectorProfileName"
    )
    connector_type: Optional[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ]
    ] = Field(default=None, alias="connectorType")
    connector_label: Optional[str] = Field(default=None, alias="connectorLabel")
    connection_mode: Optional[Literal["Private", "Public"]] = Field(
        default=None, alias="connectionMode"
    )
    credentials_arn: Optional[str] = Field(default=None, alias="credentialsArn")
    connector_profile_properties: Optional[ConnectorProfilePropertiesModel] = Field(
        default=None, alias="connectorProfileProperties"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    private_connection_provisioning_state: Optional[
        PrivateConnectionProvisioningStateModel
    ] = Field(default=None, alias="privateConnectionProvisioningState")


class DestinationConnectorPropertiesModel(BaseModel):
    redshift: Optional[RedshiftDestinationPropertiesModel] = Field(
        default=None, alias="Redshift"
    )
    s3: Optional[S3DestinationPropertiesModel] = Field(default=None, alias="S3")
    salesforce: Optional[SalesforceDestinationPropertiesModel] = Field(
        default=None, alias="Salesforce"
    )
    snowflake: Optional[SnowflakeDestinationPropertiesModel] = Field(
        default=None, alias="Snowflake"
    )
    event_bridge: Optional[EventBridgeDestinationPropertiesModel] = Field(
        default=None, alias="EventBridge"
    )
    lookout_metrics: Optional[Mapping[str, Any]] = Field(
        default=None, alias="LookoutMetrics"
    )
    upsolver: Optional[UpsolverDestinationPropertiesModel] = Field(
        default=None, alias="Upsolver"
    )
    honeycode: Optional[HoneycodeDestinationPropertiesModel] = Field(
        default=None, alias="Honeycode"
    )
    customer_profiles: Optional[CustomerProfilesDestinationPropertiesModel] = Field(
        default=None, alias="CustomerProfiles"
    )
    zendesk: Optional[ZendeskDestinationPropertiesModel] = Field(
        default=None, alias="Zendesk"
    )
    marketo: Optional[MarketoDestinationPropertiesModel] = Field(
        default=None, alias="Marketo"
    )
    custom_connector: Optional[CustomConnectorDestinationPropertiesModel] = Field(
        default=None, alias="CustomConnector"
    )
    s_ap_odata: Optional[SAPODataDestinationPropertiesModel] = Field(
        default=None, alias="SAPOData"
    )


class SourceFlowConfigModel(BaseModel):
    connector_type: Literal[
        "Amplitude",
        "CustomConnector",
        "CustomerProfiles",
        "Datadog",
        "Dynatrace",
        "EventBridge",
        "Googleanalytics",
        "Honeycode",
        "Infornexus",
        "LookoutMetrics",
        "Marketo",
        "Pardot",
        "Redshift",
        "S3",
        "SAPOData",
        "Salesforce",
        "Servicenow",
        "Singular",
        "Slack",
        "Snowflake",
        "Trendmicro",
        "Upsolver",
        "Veeva",
        "Zendesk",
    ] = Field(alias="connectorType")
    source_connector_properties: SourceConnectorPropertiesModel = Field(
        alias="sourceConnectorProperties"
    )
    api_version: Optional[str] = Field(default=None, alias="apiVersion")
    connector_profile_name: Optional[str] = Field(
        default=None, alias="connectorProfileName"
    )
    incremental_pull_config: Optional[IncrementalPullConfigModel] = Field(
        default=None, alias="incrementalPullConfig"
    )


class ConnectorProfileConfigModel(BaseModel):
    connector_profile_properties: ConnectorProfilePropertiesModel = Field(
        alias="connectorProfileProperties"
    )
    connector_profile_credentials: Optional[ConnectorProfileCredentialsModel] = Field(
        default=None, alias="connectorProfileCredentials"
    )


class DescribeConnectorEntityResponseModel(BaseModel):
    connector_entity_fields: List[ConnectorEntityFieldModel] = Field(
        alias="connectorEntityFields"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConnectorResponseModel(BaseModel):
    connector_configuration: ConnectorConfigurationModel = Field(
        alias="connectorConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConnectorsResponseModel(BaseModel):
    connector_configurations: Dict[
        Literal[
            "Amplitude",
            "CustomConnector",
            "CustomerProfiles",
            "Datadog",
            "Dynatrace",
            "EventBridge",
            "Googleanalytics",
            "Honeycode",
            "Infornexus",
            "LookoutMetrics",
            "Marketo",
            "Pardot",
            "Redshift",
            "S3",
            "SAPOData",
            "Salesforce",
            "Servicenow",
            "Singular",
            "Slack",
            "Snowflake",
            "Trendmicro",
            "Upsolver",
            "Veeva",
            "Zendesk",
        ],
        ConnectorConfigurationModel,
    ] = Field(alias="connectorConfigurations")
    connectors: List[ConnectorDetailModel] = Field(alias="connectors")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConnectorProfilesResponseModel(BaseModel):
    connector_profile_details: List[ConnectorProfileModel] = Field(
        alias="connectorProfileDetails"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DestinationFlowConfigModel(BaseModel):
    connector_type: Literal[
        "Amplitude",
        "CustomConnector",
        "CustomerProfiles",
        "Datadog",
        "Dynatrace",
        "EventBridge",
        "Googleanalytics",
        "Honeycode",
        "Infornexus",
        "LookoutMetrics",
        "Marketo",
        "Pardot",
        "Redshift",
        "S3",
        "SAPOData",
        "Salesforce",
        "Servicenow",
        "Singular",
        "Slack",
        "Snowflake",
        "Trendmicro",
        "Upsolver",
        "Veeva",
        "Zendesk",
    ] = Field(alias="connectorType")
    destination_connector_properties: DestinationConnectorPropertiesModel = Field(
        alias="destinationConnectorProperties"
    )
    api_version: Optional[str] = Field(default=None, alias="apiVersion")
    connector_profile_name: Optional[str] = Field(
        default=None, alias="connectorProfileName"
    )


class CreateConnectorProfileRequestModel(BaseModel):
    connector_profile_name: str = Field(alias="connectorProfileName")
    connector_type: Literal[
        "Amplitude",
        "CustomConnector",
        "CustomerProfiles",
        "Datadog",
        "Dynatrace",
        "EventBridge",
        "Googleanalytics",
        "Honeycode",
        "Infornexus",
        "LookoutMetrics",
        "Marketo",
        "Pardot",
        "Redshift",
        "S3",
        "SAPOData",
        "Salesforce",
        "Servicenow",
        "Singular",
        "Slack",
        "Snowflake",
        "Trendmicro",
        "Upsolver",
        "Veeva",
        "Zendesk",
    ] = Field(alias="connectorType")
    connection_mode: Literal["Private", "Public"] = Field(alias="connectionMode")
    connector_profile_config: ConnectorProfileConfigModel = Field(
        alias="connectorProfileConfig"
    )
    kms_arn: Optional[str] = Field(default=None, alias="kmsArn")
    connector_label: Optional[str] = Field(default=None, alias="connectorLabel")


class UpdateConnectorProfileRequestModel(BaseModel):
    connector_profile_name: str = Field(alias="connectorProfileName")
    connection_mode: Literal["Private", "Public"] = Field(alias="connectionMode")
    connector_profile_config: ConnectorProfileConfigModel = Field(
        alias="connectorProfileConfig"
    )


class CreateFlowRequestModel(BaseModel):
    flow_name: str = Field(alias="flowName")
    trigger_config: TriggerConfigModel = Field(alias="triggerConfig")
    source_flow_config: SourceFlowConfigModel = Field(alias="sourceFlowConfig")
    destination_flow_config_list: Sequence[DestinationFlowConfigModel] = Field(
        alias="destinationFlowConfigList"
    )
    tasks: Sequence[TaskModel] = Field(alias="tasks")
    description: Optional[str] = Field(default=None, alias="description")
    kms_arn: Optional[str] = Field(default=None, alias="kmsArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    metadata_catalog_config: Optional[MetadataCatalogConfigModel] = Field(
        default=None, alias="metadataCatalogConfig"
    )


class DescribeFlowResponseModel(BaseModel):
    flow_arn: str = Field(alias="flowArn")
    description: str = Field(alias="description")
    flow_name: str = Field(alias="flowName")
    kms_arn: str = Field(alias="kmsArn")
    flow_status: Literal[
        "Active", "Deleted", "Deprecated", "Draft", "Errored", "Suspended"
    ] = Field(alias="flowStatus")
    flow_status_message: str = Field(alias="flowStatusMessage")
    source_flow_config: SourceFlowConfigModel = Field(alias="sourceFlowConfig")
    destination_flow_config_list: List[DestinationFlowConfigModel] = Field(
        alias="destinationFlowConfigList"
    )
    last_run_execution_details: ExecutionDetailsModel = Field(
        alias="lastRunExecutionDetails"
    )
    trigger_config: TriggerConfigModel = Field(alias="triggerConfig")
    tasks: List[TaskModel] = Field(alias="tasks")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    created_by: str = Field(alias="createdBy")
    last_updated_by: str = Field(alias="lastUpdatedBy")
    tags: Dict[str, str] = Field(alias="tags")
    metadata_catalog_config: MetadataCatalogConfigModel = Field(
        alias="metadataCatalogConfig"
    )
    last_run_metadata_catalog_details: List[MetadataCatalogDetailModel] = Field(
        alias="lastRunMetadataCatalogDetails"
    )
    schema_version: int = Field(alias="schemaVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFlowRequestModel(BaseModel):
    flow_name: str = Field(alias="flowName")
    trigger_config: TriggerConfigModel = Field(alias="triggerConfig")
    source_flow_config: SourceFlowConfigModel = Field(alias="sourceFlowConfig")
    destination_flow_config_list: Sequence[DestinationFlowConfigModel] = Field(
        alias="destinationFlowConfigList"
    )
    tasks: Sequence[TaskModel] = Field(alias="tasks")
    description: Optional[str] = Field(default=None, alias="description")
    metadata_catalog_config: Optional[MetadataCatalogConfigModel] = Field(
        default=None, alias="metadataCatalogConfig"
    )
