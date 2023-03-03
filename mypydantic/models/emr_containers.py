# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelJobRunRequestModel(BaseModel):
    id: str = Field(alias="id")
    virtual_cluster_id: str = Field(alias="virtualClusterId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CertificateModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_data: Optional[str] = Field(default=None, alias="certificateData")


class CloudWatchMonitoringConfigurationModel(BaseModel):
    log_group_name: str = Field(alias="logGroupName")
    log_stream_name_prefix: Optional[str] = Field(
        default=None, alias="logStreamNamePrefix"
    )


class ConfigurationModel(BaseModel):
    classification: str = Field(alias="classification")
    properties: Optional[Mapping[str, str]] = Field(default=None, alias="properties")
    configurations: Optional[Sequence[Dict[str, Any]]] = Field(
        default=None, alias="configurations"
    )


class EksInfoModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="namespace")


class DeleteJobTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class DeleteManagedEndpointRequestModel(BaseModel):
    id: str = Field(alias="id")
    virtual_cluster_id: str = Field(alias="virtualClusterId")


class DeleteVirtualClusterRequestModel(BaseModel):
    id: str = Field(alias="id")


class DescribeJobRunRequestModel(BaseModel):
    id: str = Field(alias="id")
    virtual_cluster_id: str = Field(alias="virtualClusterId")


class DescribeJobTemplateRequestModel(BaseModel):
    id: str = Field(alias="id")


class DescribeManagedEndpointRequestModel(BaseModel):
    id: str = Field(alias="id")
    virtual_cluster_id: str = Field(alias="virtualClusterId")


class DescribeVirtualClusterRequestModel(BaseModel):
    id: str = Field(alias="id")


class SparkSqlJobDriverModel(BaseModel):
    entry_point: Optional[str] = Field(default=None, alias="entryPoint")
    spark_sql_parameters: Optional[str] = Field(
        default=None, alias="sparkSqlParameters"
    )


class SparkSubmitJobDriverModel(BaseModel):
    entry_point: str = Field(alias="entryPoint")
    entry_point_arguments: Optional[Sequence[str]] = Field(
        default=None, alias="entryPointArguments"
    )
    spark_submit_parameters: Optional[str] = Field(
        default=None, alias="sparkSubmitParameters"
    )


class RetryPolicyConfigurationModel(BaseModel):
    max_attempts: int = Field(alias="maxAttempts")


class RetryPolicyExecutionModel(BaseModel):
    current_attempt_count: int = Field(alias="currentAttemptCount")


class TemplateParameterConfigurationModel(BaseModel):
    type: Optional[Literal["NUMBER", "STRING"]] = Field(default=None, alias="type")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListJobRunsRequestModel(BaseModel):
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    name: Optional[str] = Field(default=None, alias="name")
    states: Optional[
        Sequence[
            Literal[
                "CANCELLED",
                "CANCEL_PENDING",
                "COMPLETED",
                "FAILED",
                "PENDING",
                "RUNNING",
                "SUBMITTED",
            ]
        ]
    ] = Field(default=None, alias="states")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListJobTemplatesRequestModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListManagedEndpointsRequestModel(BaseModel):
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    types: Optional[Sequence[str]] = Field(default=None, alias="types")
    states: Optional[
        Sequence[
            Literal[
                "ACTIVE",
                "CREATING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
                "TERMINATING",
            ]
        ]
    ] = Field(default=None, alias="states")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListVirtualClustersRequestModel(BaseModel):
    container_provider_id: Optional[str] = Field(
        default=None, alias="containerProviderId"
    )
    container_provider_type: Optional[Literal["EKS"]] = Field(
        default=None, alias="containerProviderType"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    states: Optional[
        Sequence[Literal["ARRESTED", "RUNNING", "TERMINATED", "TERMINATING"]]
    ] = Field(default=None, alias="states")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class S3MonitoringConfigurationModel(BaseModel):
    log_uri: str = Field(alias="logUri")


class ParametricCloudWatchMonitoringConfigurationModel(BaseModel):
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")
    log_stream_name_prefix: Optional[str] = Field(
        default=None, alias="logStreamNamePrefix"
    )


class ParametricS3MonitoringConfigurationModel(BaseModel):
    log_uri: Optional[str] = Field(default=None, alias="logUri")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CancelJobRunResponseModel(BaseModel):
    id: str = Field(alias="id")
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobTemplateResponseModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    created_at: datetime = Field(alias="createdAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateManagedEndpointResponseModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVirtualClusterResponseModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteJobTemplateResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteManagedEndpointResponseModel(BaseModel):
    id: str = Field(alias="id")
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVirtualClusterResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartJobRunResponseModel(BaseModel):
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ContainerInfoModel(BaseModel):
    eks_info: Optional[EksInfoModel] = Field(default=None, alias="eksInfo")


class JobDriverModel(BaseModel):
    spark_submit_job_driver: Optional[SparkSubmitJobDriverModel] = Field(
        default=None, alias="sparkSubmitJobDriver"
    )
    spark_sql_job_driver: Optional[SparkSqlJobDriverModel] = Field(
        default=None, alias="sparkSqlJobDriver"
    )


class ListJobRunsRequestListJobRunsPaginateModel(BaseModel):
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    name: Optional[str] = Field(default=None, alias="name")
    states: Optional[
        Sequence[
            Literal[
                "CANCELLED",
                "CANCEL_PENDING",
                "COMPLETED",
                "FAILED",
                "PENDING",
                "RUNNING",
                "SUBMITTED",
            ]
        ]
    ] = Field(default=None, alias="states")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobTemplatesRequestListJobTemplatesPaginateModel(BaseModel):
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListManagedEndpointsRequestListManagedEndpointsPaginateModel(BaseModel):
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    types: Optional[Sequence[str]] = Field(default=None, alias="types")
    states: Optional[
        Sequence[
            Literal[
                "ACTIVE",
                "CREATING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
                "TERMINATING",
            ]
        ]
    ] = Field(default=None, alias="states")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVirtualClustersRequestListVirtualClustersPaginateModel(BaseModel):
    container_provider_id: Optional[str] = Field(
        default=None, alias="containerProviderId"
    )
    container_provider_type: Optional[Literal["EKS"]] = Field(
        default=None, alias="containerProviderType"
    )
    created_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdAfter"
    )
    created_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="createdBefore"
    )
    states: Optional[
        Sequence[Literal["ARRESTED", "RUNNING", "TERMINATED", "TERMINATING"]]
    ] = Field(default=None, alias="states")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class MonitoringConfigurationModel(BaseModel):
    persistent_app_ui: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="persistentAppUI"
    )
    cloud_watch_monitoring_configuration: Optional[
        CloudWatchMonitoringConfigurationModel
    ] = Field(default=None, alias="cloudWatchMonitoringConfiguration")
    s3_monitoring_configuration: Optional[S3MonitoringConfigurationModel] = Field(
        default=None, alias="s3MonitoringConfiguration"
    )


class ParametricMonitoringConfigurationModel(BaseModel):
    persistent_app_ui: Optional[str] = Field(default=None, alias="persistentAppUI")
    cloud_watch_monitoring_configuration: Optional[
        ParametricCloudWatchMonitoringConfigurationModel
    ] = Field(default=None, alias="cloudWatchMonitoringConfiguration")
    s3_monitoring_configuration: Optional[
        ParametricS3MonitoringConfigurationModel
    ] = Field(default=None, alias="s3MonitoringConfiguration")


class ContainerProviderModel(BaseModel):
    type: Literal["EKS"] = Field(alias="type")
    id: str = Field(alias="id")
    info: Optional[ContainerInfoModel] = Field(default=None, alias="info")


class ConfigurationOverridesModel(BaseModel):
    application_configuration: Optional[Sequence[ConfigurationModel]] = Field(
        default=None, alias="applicationConfiguration"
    )
    monitoring_configuration: Optional[MonitoringConfigurationModel] = Field(
        default=None, alias="monitoringConfiguration"
    )


class ParametricConfigurationOverridesModel(BaseModel):
    application_configuration: Optional[Sequence[ConfigurationModel]] = Field(
        default=None, alias="applicationConfiguration"
    )
    monitoring_configuration: Optional[ParametricMonitoringConfigurationModel] = Field(
        default=None, alias="monitoringConfiguration"
    )


class CreateVirtualClusterRequestModel(BaseModel):
    name: str = Field(alias="name")
    container_provider: ContainerProviderModel = Field(alias="containerProvider")
    client_token: str = Field(alias="clientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class VirtualClusterModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    state: Optional[
        Literal["ARRESTED", "RUNNING", "TERMINATED", "TERMINATING"]
    ] = Field(default=None, alias="state")
    container_provider: Optional[ContainerProviderModel] = Field(
        default=None, alias="containerProvider"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateManagedEndpointRequestModel(BaseModel):
    name: str = Field(alias="name")
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    type: str = Field(alias="type")
    release_label: str = Field(alias="releaseLabel")
    execution_role_arn: str = Field(alias="executionRoleArn")
    client_token: str = Field(alias="clientToken")
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    configuration_overrides: Optional[ConfigurationOverridesModel] = Field(
        default=None, alias="configurationOverrides"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class EndpointModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    virtual_cluster_id: Optional[str] = Field(default=None, alias="virtualClusterId")
    type: Optional[str] = Field(default=None, alias="type")
    state: Optional[
        Literal[
            "ACTIVE", "CREATING", "TERMINATED", "TERMINATED_WITH_ERRORS", "TERMINATING"
        ]
    ] = Field(default=None, alias="state")
    release_label: Optional[str] = Field(default=None, alias="releaseLabel")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_authority: Optional[CertificateModel] = Field(
        default=None, alias="certificateAuthority"
    )
    configuration_overrides: Optional[ConfigurationOverridesModel] = Field(
        default=None, alias="configurationOverrides"
    )
    server_url: Optional[str] = Field(default=None, alias="serverUrl")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    security_group: Optional[str] = Field(default=None, alias="securityGroup")
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    state_details: Optional[str] = Field(default=None, alias="stateDetails")
    failure_reason: Optional[
        Literal[
            "CLUSTER_UNAVAILABLE", "INTERNAL_ERROR", "USER_ERROR", "VALIDATION_ERROR"
        ]
    ] = Field(default=None, alias="failureReason")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class JobRunModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    virtual_cluster_id: Optional[str] = Field(default=None, alias="virtualClusterId")
    arn: Optional[str] = Field(default=None, alias="arn")
    state: Optional[
        Literal[
            "CANCELLED",
            "CANCEL_PENDING",
            "COMPLETED",
            "FAILED",
            "PENDING",
            "RUNNING",
            "SUBMITTED",
        ]
    ] = Field(default=None, alias="state")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    release_label: Optional[str] = Field(default=None, alias="releaseLabel")
    configuration_overrides: Optional[ConfigurationOverridesModel] = Field(
        default=None, alias="configurationOverrides"
    )
    job_driver: Optional[JobDriverModel] = Field(default=None, alias="jobDriver")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    finished_at: Optional[datetime] = Field(default=None, alias="finishedAt")
    state_details: Optional[str] = Field(default=None, alias="stateDetails")
    failure_reason: Optional[
        Literal[
            "CLUSTER_UNAVAILABLE", "INTERNAL_ERROR", "USER_ERROR", "VALIDATION_ERROR"
        ]
    ] = Field(default=None, alias="failureReason")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    retry_policy_configuration: Optional[RetryPolicyConfigurationModel] = Field(
        default=None, alias="retryPolicyConfiguration"
    )
    retry_policy_execution: Optional[RetryPolicyExecutionModel] = Field(
        default=None, alias="retryPolicyExecution"
    )


class StartJobRunRequestModel(BaseModel):
    virtual_cluster_id: str = Field(alias="virtualClusterId")
    client_token: str = Field(alias="clientToken")
    name: Optional[str] = Field(default=None, alias="name")
    execution_role_arn: Optional[str] = Field(default=None, alias="executionRoleArn")
    release_label: Optional[str] = Field(default=None, alias="releaseLabel")
    job_driver: Optional[JobDriverModel] = Field(default=None, alias="jobDriver")
    configuration_overrides: Optional[ConfigurationOverridesModel] = Field(
        default=None, alias="configurationOverrides"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    job_template_id: Optional[str] = Field(default=None, alias="jobTemplateId")
    job_template_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="jobTemplateParameters"
    )
    retry_policy_configuration: Optional[RetryPolicyConfigurationModel] = Field(
        default=None, alias="retryPolicyConfiguration"
    )


class JobTemplateDataModel(BaseModel):
    execution_role_arn: str = Field(alias="executionRoleArn")
    release_label: str = Field(alias="releaseLabel")
    job_driver: JobDriverModel = Field(alias="jobDriver")
    configuration_overrides: Optional[ParametricConfigurationOverridesModel] = Field(
        default=None, alias="configurationOverrides"
    )
    parameter_configuration: Optional[
        Mapping[str, TemplateParameterConfigurationModel]
    ] = Field(default=None, alias="parameterConfiguration")
    job_tags: Optional[Mapping[str, str]] = Field(default=None, alias="jobTags")


class DescribeVirtualClusterResponseModel(BaseModel):
    virtual_cluster: VirtualClusterModel = Field(alias="virtualCluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVirtualClustersResponseModel(BaseModel):
    virtual_clusters: List[VirtualClusterModel] = Field(alias="virtualClusters")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeManagedEndpointResponseModel(BaseModel):
    endpoint: EndpointModel = Field(alias="endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListManagedEndpointsResponseModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="endpoints")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeJobRunResponseModel(BaseModel):
    job_run: JobRunModel = Field(alias="jobRun")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobRunsResponseModel(BaseModel):
    job_runs: List[JobRunModel] = Field(alias="jobRuns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobTemplateRequestModel(BaseModel):
    name: str = Field(alias="name")
    client_token: str = Field(alias="clientToken")
    job_template_data: JobTemplateDataModel = Field(alias="jobTemplateData")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")


class JobTemplateModel(BaseModel):
    job_template_data: JobTemplateDataModel = Field(alias="jobTemplateData")
    name: Optional[str] = Field(default=None, alias="name")
    id: Optional[str] = Field(default=None, alias="id")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    kms_key_arn: Optional[str] = Field(default=None, alias="kmsKeyArn")
    decryption_error: Optional[str] = Field(default=None, alias="decryptionError")


class DescribeJobTemplateResponseModel(BaseModel):
    job_template: JobTemplateModel = Field(alias="jobTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobTemplatesResponseModel(BaseModel):
    templates: List[JobTemplateModel] = Field(alias="templates")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
