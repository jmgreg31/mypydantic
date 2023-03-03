# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class LogsStatusModel(BaseModel):
    health_status: Literal["ACTIVE", "DEACTIVATED", "PENDING"] = Field(
        alias="healthStatus"
    )
    path_to_logs: str = Field(alias="pathToLogs")


class AutoEnableNewRegionConfigurationModel(BaseModel):
    region: Literal[
        "ap-northeast-1",
        "ap-southeast-2",
        "eu-central-1",
        "eu-west-1",
        "us-east-1",
        "us-east-2",
        "us-west-2",
    ] = Field(alias="region")
    sources: Sequence[
        Literal["CLOUD_TRAIL", "ROUTE53", "SH_FINDINGS", "VPC_FLOW"]
    ] = Field(alias="sources")


class CreateAwsLogSourceRequestModel(BaseModel):
    input_order: Sequence[Literal["MEMBER", "REGION", "SOURCE_TYPE"]] = Field(
        alias="inputOrder"
    )
    enable_all_dimensions: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="enableAllDimensions"
    )
    enable_single_dimension: Optional[Sequence[str]] = Field(
        default=None, alias="enableSingleDimension"
    )
    enable_two_dimensions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="enableTwoDimensions"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateCustomLogSourceRequestModel(BaseModel):
    custom_source_name: str = Field(alias="customSourceName")
    event_class: Literal[
        "ACCESS_ACTIVITY",
        "ACCOUNT_CHANGE",
        "AUTHENTICATION",
        "AUTHORIZATION",
        "CLOUD_API",
        "CLOUD_STORAGE",
        "CONFIG_STATE",
        "CONTAINER_LIFECYCLE",
        "DATABASE_LIFECYCLE",
        "DHCP_ACTIVITY",
        "DNS_ACTIVITY",
        "ENTITY_MANAGEMENT_AUDIT",
        "FILE_ACTIVITY",
        "FTP_ACTIVITY",
        "HTTP_ACTIVITY",
        "INVENTORY_INFO",
        "KERNEL_ACTIVITY",
        "KERNEL_EXTENSION",
        "MEMORY_ACTIVITY",
        "MODULE_ACTIVITY",
        "NETWORK_ACTIVITY",
        "PROCESS_ACTIVITY",
        "RDP_ACTIVITY",
        "REGISTRY_KEY_ACTIVITY",
        "REGISTRY_VALUE_ACTIVITY",
        "RESOURCE_ACTIVITY",
        "RFB_ACTIVITY",
        "SCHEDULED_JOB_ACTIVITY",
        "SECURITY_FINDING",
        "SMB_ACTIVITY",
        "SMTP_ACTIVITY",
        "SSH_ACTIVITY",
        "VIRTUAL_MACHINE_ACTIVITY",
    ] = Field(alias="eventClass")
    glue_invocation_role_arn: str = Field(alias="glueInvocationRoleArn")
    log_provider_account_id: str = Field(alias="logProviderAccountId")


class CreateDatalakeDelegatedAdminRequestModel(BaseModel):
    account: str = Field(alias="account")


class CreateDatalakeExceptionsSubscriptionRequestModel(BaseModel):
    notification_endpoint: str = Field(alias="notificationEndpoint")
    subscription_protocol: Literal[
        "APP",
        "EMAIL",
        "EMAIL_JSON",
        "FIREHOSE",
        "HTTP",
        "HTTPS",
        "LAMBDA",
        "SMS",
        "SQS",
    ] = Field(alias="subscriptionProtocol")


class SourceTypeModel(BaseModel):
    aws_source_type: Optional[
        Literal["CLOUD_TRAIL", "ROUTE53", "SH_FINDINGS", "VPC_FLOW"]
    ] = Field(default=None, alias="awsSourceType")
    custom_source_type: Optional[str] = Field(default=None, alias="customSourceType")


class CreateSubscriptionNotificationConfigurationRequestModel(BaseModel):
    subscription_id: str = Field(alias="subscriptionId")
    create_sqs: Optional[bool] = Field(default=None, alias="createSqs")
    https_api_key_name: Optional[str] = Field(default=None, alias="httpsApiKeyName")
    https_api_key_value: Optional[str] = Field(default=None, alias="httpsApiKeyValue")
    https_method: Optional[Literal["POST", "PUT"]] = Field(
        default=None, alias="httpsMethod"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    subscription_endpoint: Optional[str] = Field(
        default=None, alias="subscriptionEndpoint"
    )


class DeleteAwsLogSourceRequestModel(BaseModel):
    input_order: Sequence[Literal["MEMBER", "REGION", "SOURCE_TYPE"]] = Field(
        alias="inputOrder"
    )
    disable_all_dimensions: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="disableAllDimensions"
    )
    disable_single_dimension: Optional[Sequence[str]] = Field(
        default=None, alias="disableSingleDimension"
    )
    disable_two_dimensions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="disableTwoDimensions"
    )


class DeleteCustomLogSourceRequestModel(BaseModel):
    custom_source_name: str = Field(alias="customSourceName")


class DeleteDatalakeDelegatedAdminRequestModel(BaseModel):
    account: str = Field(alias="account")


class DeleteSubscriberRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteSubscriptionNotificationConfigurationRequestModel(BaseModel):
    subscription_id: str = Field(alias="subscriptionId")


class FailuresModel(BaseModel):
    exception_message: str = Field(alias="exceptionMessage")
    remediation: str = Field(alias="remediation")
    timestamp: datetime = Field(alias="timestamp")


class ProtocolAndNotificationEndpointModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="endpoint")
    protocol: Optional[str] = Field(default=None, alias="protocol")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetDatalakeStatusRequestModel(BaseModel):
    account_set: Optional[Sequence[str]] = Field(default=None, alias="accountSet")
    max_account_results: Optional[int] = Field(default=None, alias="maxAccountResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetSubscriberRequestModel(BaseModel):
    id: str = Field(alias="id")


class RetentionSettingModel(BaseModel):
    retention_period: Optional[int] = Field(default=None, alias="retentionPeriod")
    storage_class: Optional[
        Literal[
            "DEEP_ARCHIVE",
            "EXPIRE",
            "GLACIER",
            "GLACIER_IR",
            "INTELLIGENT_TIERING",
            "ONEZONE_IA",
            "STANDARD_IA",
        ]
    ] = Field(default=None, alias="storageClass")


class ListDatalakeExceptionsRequestModel(BaseModel):
    max_failures: Optional[int] = Field(default=None, alias="maxFailures")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    region_set: Optional[
        Sequence[
            Literal[
                "ap-northeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "eu-west-1",
                "us-east-1",
                "us-east-2",
                "us-west-2",
            ]
        ]
    ] = Field(default=None, alias="regionSet")


class ListLogSourcesRequestModel(BaseModel):
    input_order: Optional[Sequence[Literal["MEMBER", "REGION", "SOURCE_TYPE"]]] = Field(
        default=None, alias="inputOrder"
    )
    list_all_dimensions: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="listAllDimensions"
    )
    list_single_dimension: Optional[Sequence[str]] = Field(
        default=None, alias="listSingleDimension"
    )
    list_two_dimensions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="listTwoDimensions"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSubscribersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class UpdateDatalakeExceptionsExpiryRequestModel(BaseModel):
    exception_message_expiry: int = Field(alias="exceptionMessageExpiry")


class UpdateDatalakeExceptionsSubscriptionRequestModel(BaseModel):
    notification_endpoint: str = Field(alias="notificationEndpoint")
    subscription_protocol: Literal[
        "APP",
        "EMAIL",
        "EMAIL_JSON",
        "FIREHOSE",
        "HTTP",
        "HTTPS",
        "LAMBDA",
        "SMS",
        "SQS",
    ] = Field(alias="subscriptionProtocol")


class UpdateSubscriptionNotificationConfigurationRequestModel(BaseModel):
    subscription_id: str = Field(alias="subscriptionId")
    create_sqs: Optional[bool] = Field(default=None, alias="createSqs")
    https_api_key_name: Optional[str] = Field(default=None, alias="httpsApiKeyName")
    https_api_key_value: Optional[str] = Field(default=None, alias="httpsApiKeyValue")
    https_method: Optional[Literal["POST", "PUT"]] = Field(
        default=None, alias="httpsMethod"
    )
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    subscription_endpoint: Optional[str] = Field(
        default=None, alias="subscriptionEndpoint"
    )


class AccountSourcesModel(BaseModel):
    account: str = Field(alias="account")
    source_type: str = Field(alias="sourceType")
    event_class: Optional[
        Literal[
            "ACCESS_ACTIVITY",
            "ACCOUNT_CHANGE",
            "AUTHENTICATION",
            "AUTHORIZATION",
            "CLOUD_API",
            "CLOUD_STORAGE",
            "CONFIG_STATE",
            "CONTAINER_LIFECYCLE",
            "DATABASE_LIFECYCLE",
            "DHCP_ACTIVITY",
            "DNS_ACTIVITY",
            "ENTITY_MANAGEMENT_AUDIT",
            "FILE_ACTIVITY",
            "FTP_ACTIVITY",
            "HTTP_ACTIVITY",
            "INVENTORY_INFO",
            "KERNEL_ACTIVITY",
            "KERNEL_EXTENSION",
            "MEMORY_ACTIVITY",
            "MODULE_ACTIVITY",
            "NETWORK_ACTIVITY",
            "PROCESS_ACTIVITY",
            "RDP_ACTIVITY",
            "REGISTRY_KEY_ACTIVITY",
            "REGISTRY_VALUE_ACTIVITY",
            "RESOURCE_ACTIVITY",
            "RFB_ACTIVITY",
            "SCHEDULED_JOB_ACTIVITY",
            "SECURITY_FINDING",
            "SMB_ACTIVITY",
            "SMTP_ACTIVITY",
            "SSH_ACTIVITY",
            "VIRTUAL_MACHINE_ACTIVITY",
        ]
    ] = Field(default=None, alias="eventClass")
    logs_status: Optional[List[LogsStatusModel]] = Field(
        default=None, alias="logsStatus"
    )


class CreateDatalakeAutoEnableRequestModel(BaseModel):
    configuration_for_new_accounts: Sequence[
        AutoEnableNewRegionConfigurationModel
    ] = Field(alias="configurationForNewAccounts")


class DeleteDatalakeAutoEnableRequestModel(BaseModel):
    remove_from_configuration_for_new_accounts: Sequence[
        AutoEnableNewRegionConfigurationModel
    ] = Field(alias="removeFromConfigurationForNewAccounts")


class CreateAwsLogSourceResponseModel(BaseModel):
    failed: List[str] = Field(alias="failed")
    processing: List[str] = Field(alias="processing")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomLogSourceResponseModel(BaseModel):
    custom_data_location: str = Field(alias="customDataLocation")
    glue_crawler_name: str = Field(alias="glueCrawlerName")
    glue_database_name: str = Field(alias="glueDatabaseName")
    glue_table_name: str = Field(alias="glueTableName")
    log_provider_access_role_arn: str = Field(alias="logProviderAccessRoleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSubscriberResponseModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    s3_bucket_arn: str = Field(alias="s3BucketArn")
    sns_arn: str = Field(alias="snsArn")
    subscription_id: str = Field(alias="subscriptionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSubscriptionNotificationConfigurationResponseModel(BaseModel):
    queue_arn: str = Field(alias="queueArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAwsLogSourceResponseModel(BaseModel):
    failed: List[str] = Field(alias="failed")
    processing: List[str] = Field(alias="processing")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCustomLogSourceResponseModel(BaseModel):
    custom_data_location: str = Field(alias="customDataLocation")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDatalakeExceptionsSubscriptionResponseModel(BaseModel):
    status: str = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDatalakeAutoEnableResponseModel(BaseModel):
    auto_enable_new_accounts: List[AutoEnableNewRegionConfigurationModel] = Field(
        alias="autoEnableNewAccounts"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDatalakeExceptionsExpiryResponseModel(BaseModel):
    exception_message_expiry: int = Field(alias="exceptionMessageExpiry")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLogSourcesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    region_source_types_accounts_list: List[Dict[str, Dict[str, List[str]]]] = Field(
        alias="regionSourceTypesAccountsList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSubscriptionNotificationConfigurationResponseModel(BaseModel):
    queue_arn: str = Field(alias="queueArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSubscriberRequestModel(BaseModel):
    account_id: str = Field(alias="accountId")
    external_id: str = Field(alias="externalId")
    source_types: Sequence[SourceTypeModel] = Field(alias="sourceTypes")
    subscriber_name: str = Field(alias="subscriberName")
    access_types: Optional[Sequence[Literal["LAKEFORMATION", "S3"]]] = Field(
        default=None, alias="accessTypes"
    )
    subscriber_description: Optional[str] = Field(
        default=None, alias="subscriberDescription"
    )


class SubscriberResourceModel(BaseModel):
    account_id: str = Field(alias="accountId")
    source_types: List[SourceTypeModel] = Field(alias="sourceTypes")
    subscription_id: str = Field(alias="subscriptionId")
    access_types: Optional[List[Literal["LAKEFORMATION", "S3"]]] = Field(
        default=None, alias="accessTypes"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    external_id: Optional[str] = Field(default=None, alias="externalId")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    s3_bucket_arn: Optional[str] = Field(default=None, alias="s3BucketArn")
    sns_arn: Optional[str] = Field(default=None, alias="snsArn")
    subscriber_description: Optional[str] = Field(
        default=None, alias="subscriberDescription"
    )
    subscriber_name: Optional[str] = Field(default=None, alias="subscriberName")
    subscription_endpoint: Optional[str] = Field(
        default=None, alias="subscriptionEndpoint"
    )
    subscription_protocol: Optional[Literal["HTTPS", "SQS"]] = Field(
        default=None, alias="subscriptionProtocol"
    )
    subscription_status: Optional[
        Literal["ACTIVE", "DEACTIVATED", "PENDING", "READY"]
    ] = Field(default=None, alias="subscriptionStatus")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class UpdateSubscriberRequestModel(BaseModel):
    id: str = Field(alias="id")
    source_types: Sequence[SourceTypeModel] = Field(alias="sourceTypes")
    external_id: Optional[str] = Field(default=None, alias="externalId")
    subscriber_description: Optional[str] = Field(
        default=None, alias="subscriberDescription"
    )
    subscriber_name: Optional[str] = Field(default=None, alias="subscriberName")


class FailuresResponseModel(BaseModel):
    failures: Optional[List[FailuresModel]] = Field(default=None, alias="failures")
    region: Optional[str] = Field(default=None, alias="region")


class GetDatalakeExceptionsSubscriptionResponseModel(BaseModel):
    protocol_and_notification_endpoint: ProtocolAndNotificationEndpointModel = Field(
        alias="protocolAndNotificationEndpoint"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDatalakeStatusRequestGetDatalakeStatusPaginateModel(BaseModel):
    account_set: Optional[Sequence[str]] = Field(default=None, alias="accountSet")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatalakeExceptionsRequestListDatalakeExceptionsPaginateModel(BaseModel):
    region_set: Optional[
        Sequence[
            Literal[
                "ap-northeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "eu-west-1",
                "us-east-1",
                "us-east-2",
                "us-west-2",
            ]
        ]
    ] = Field(default=None, alias="regionSet")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListLogSourcesRequestListLogSourcesPaginateModel(BaseModel):
    input_order: Optional[Sequence[Literal["MEMBER", "REGION", "SOURCE_TYPE"]]] = Field(
        default=None, alias="inputOrder"
    )
    list_all_dimensions: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = Field(
        default=None, alias="listAllDimensions"
    )
    list_single_dimension: Optional[Sequence[str]] = Field(
        default=None, alias="listSingleDimension"
    )
    list_two_dimensions: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="listTwoDimensions"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSubscribersRequestListSubscribersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LakeConfigurationRequestModel(BaseModel):
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    replication_destination_regions: Optional[
        Sequence[
            Literal[
                "ap-northeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "eu-west-1",
                "us-east-1",
                "us-east-2",
                "us-west-2",
            ]
        ]
    ] = Field(default=None, alias="replicationDestinationRegions")
    replication_role_arn: Optional[str] = Field(
        default=None, alias="replicationRoleArn"
    )
    retention_settings: Optional[Sequence[RetentionSettingModel]] = Field(
        default=None, alias="retentionSettings"
    )
    tags_map: Optional[Mapping[str, str]] = Field(default=None, alias="tagsMap")


class LakeConfigurationResponseModel(BaseModel):
    encryption_key: Optional[str] = Field(default=None, alias="encryptionKey")
    replication_destination_regions: Optional[
        List[
            Literal[
                "ap-northeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "eu-west-1",
                "us-east-1",
                "us-east-2",
                "us-west-2",
            ]
        ]
    ] = Field(default=None, alias="replicationDestinationRegions")
    replication_role_arn: Optional[str] = Field(
        default=None, alias="replicationRoleArn"
    )
    retention_settings: Optional[List[RetentionSettingModel]] = Field(
        default=None, alias="retentionSettings"
    )
    s3_bucket_arn: Optional[str] = Field(default=None, alias="s3BucketArn")
    status: Optional[Literal["COMPLETED", "FAILED", "INITIALIZED", "PENDING"]] = Field(
        default=None, alias="status"
    )
    tags_map: Optional[Dict[str, str]] = Field(default=None, alias="tagsMap")


class GetDatalakeStatusResponseModel(BaseModel):
    account_sources_list: List[AccountSourcesModel] = Field(alias="accountSourcesList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSubscriberResponseModel(BaseModel):
    subscriber: SubscriberResourceModel = Field(alias="subscriber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSubscribersResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    subscribers: List[SubscriberResourceModel] = Field(alias="subscribers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSubscriberResponseModel(BaseModel):
    subscriber: SubscriberResourceModel = Field(alias="subscriber")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatalakeExceptionsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    non_retryable_failures: List[FailuresResponseModel] = Field(
        alias="nonRetryableFailures"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatalakeRequestModel(BaseModel):
    configurations: Optional[
        Mapping[
            Literal[
                "ap-northeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "eu-west-1",
                "us-east-1",
                "us-east-2",
                "us-west-2",
            ],
            LakeConfigurationRequestModel,
        ]
    ] = Field(default=None, alias="configurations")
    enable_all: Optional[bool] = Field(default=None, alias="enableAll")
    meta_store_manager_role_arn: Optional[str] = Field(
        default=None, alias="metaStoreManagerRoleArn"
    )
    regions: Optional[
        Sequence[
            Literal[
                "ap-northeast-1",
                "ap-southeast-2",
                "eu-central-1",
                "eu-west-1",
                "us-east-1",
                "us-east-2",
                "us-west-2",
            ]
        ]
    ] = Field(default=None, alias="regions")


class UpdateDatalakeRequestModel(BaseModel):
    configurations: Mapping[
        Literal[
            "ap-northeast-1",
            "ap-southeast-2",
            "eu-central-1",
            "eu-west-1",
            "us-east-1",
            "us-east-2",
            "us-west-2",
        ],
        LakeConfigurationRequestModel,
    ] = Field(alias="configurations")


class GetDatalakeResponseModel(BaseModel):
    configurations: Dict[
        Literal[
            "ap-northeast-1",
            "ap-southeast-2",
            "eu-central-1",
            "eu-west-1",
            "us-east-1",
            "us-east-2",
            "us-west-2",
        ],
        LakeConfigurationResponseModel,
    ] = Field(alias="configurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
