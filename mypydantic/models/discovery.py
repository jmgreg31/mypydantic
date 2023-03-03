# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AgentConfigurationStatusModel(BaseModel):
    agent_id: Optional[str] = Field(default=None, alias="agentId")
    operation_succeeded: Optional[bool] = Field(
        default=None, alias="operationSucceeded"
    )
    description: Optional[str] = Field(default=None, alias="description")


class AgentNetworkInfoModel(BaseModel):
    ip_address: Optional[str] = Field(default=None, alias="ipAddress")
    mac_address: Optional[str] = Field(default=None, alias="macAddress")


class AssociateConfigurationItemsToApplicationRequestModel(BaseModel):
    application_configuration_id: str = Field(alias="applicationConfigurationId")
    configuration_ids: Sequence[str] = Field(alias="configurationIds")


class BatchDeleteImportDataErrorModel(BaseModel):
    import_task_id: Optional[str] = Field(default=None, alias="importTaskId")
    error_code: Optional[
        Literal["INTERNAL_SERVER_ERROR", "NOT_FOUND", "OVER_LIMIT"]
    ] = Field(default=None, alias="errorCode")
    error_description: Optional[str] = Field(default=None, alias="errorDescription")


class BatchDeleteImportDataRequestModel(BaseModel):
    import_task_ids: Sequence[str] = Field(alias="importTaskIds")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ConfigurationTagModel(BaseModel):
    configuration_type: Optional[
        Literal["APPLICATION", "CONNECTION", "PROCESS", "SERVER"]
    ] = Field(default=None, alias="configurationType")
    configuration_id: Optional[str] = Field(default=None, alias="configurationId")
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")
    time_of_creation: Optional[datetime] = Field(default=None, alias="timeOfCreation")


class ContinuousExportDescriptionModel(BaseModel):
    export_id: Optional[str] = Field(default=None, alias="exportId")
    status: Optional[
        Literal[
            "ACTIVE",
            "ERROR",
            "INACTIVE",
            "START_FAILED",
            "START_IN_PROGRESS",
            "STOP_FAILED",
            "STOP_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="status")
    status_detail: Optional[str] = Field(default=None, alias="statusDetail")
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    stop_time: Optional[datetime] = Field(default=None, alias="stopTime")
    data_source: Optional[Literal["AGENT"]] = Field(default=None, alias="dataSource")
    schema_storage_config: Optional[Dict[str, str]] = Field(
        default=None, alias="schemaStorageConfig"
    )


class CreateApplicationRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class CustomerAgentInfoModel(BaseModel):
    active_agents: int = Field(alias="activeAgents")
    healthy_agents: int = Field(alias="healthyAgents")
    black_listed_agents: int = Field(alias="blackListedAgents")
    shutdown_agents: int = Field(alias="shutdownAgents")
    unhealthy_agents: int = Field(alias="unhealthyAgents")
    total_agents: int = Field(alias="totalAgents")
    unknown_agents: int = Field(alias="unknownAgents")


class CustomerAgentlessCollectorInfoModel(BaseModel):
    active_agentless_collectors: int = Field(alias="activeAgentlessCollectors")
    healthy_agentless_collectors: int = Field(alias="healthyAgentlessCollectors")
    deny_listed_agentless_collectors: int = Field(alias="denyListedAgentlessCollectors")
    shutdown_agentless_collectors: int = Field(alias="shutdownAgentlessCollectors")
    unhealthy_agentless_collectors: int = Field(alias="unhealthyAgentlessCollectors")
    total_agentless_collectors: int = Field(alias="totalAgentlessCollectors")
    unknown_agentless_collectors: int = Field(alias="unknownAgentlessCollectors")


class CustomerConnectorInfoModel(BaseModel):
    active_connectors: int = Field(alias="activeConnectors")
    healthy_connectors: int = Field(alias="healthyConnectors")
    black_listed_connectors: int = Field(alias="blackListedConnectors")
    shutdown_connectors: int = Field(alias="shutdownConnectors")
    unhealthy_connectors: int = Field(alias="unhealthyConnectors")
    total_connectors: int = Field(alias="totalConnectors")
    unknown_connectors: int = Field(alias="unknownConnectors")


class CustomerMeCollectorInfoModel(BaseModel):
    active_me_collectors: int = Field(alias="activeMeCollectors")
    healthy_me_collectors: int = Field(alias="healthyMeCollectors")
    deny_listed_me_collectors: int = Field(alias="denyListedMeCollectors")
    shutdown_me_collectors: int = Field(alias="shutdownMeCollectors")
    unhealthy_me_collectors: int = Field(alias="unhealthyMeCollectors")
    total_me_collectors: int = Field(alias="totalMeCollectors")
    unknown_me_collectors: int = Field(alias="unknownMeCollectors")


class DeleteApplicationsRequestModel(BaseModel):
    configuration_ids: Sequence[str] = Field(alias="configurationIds")


class FilterModel(BaseModel):
    name: str = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    condition: str = Field(alias="condition")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeConfigurationsRequestModel(BaseModel):
    configuration_ids: Sequence[str] = Field(alias="configurationIds")


class DescribeContinuousExportsRequestModel(BaseModel):
    export_ids: Optional[Sequence[str]] = Field(default=None, alias="exportIds")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeExportConfigurationsRequestModel(BaseModel):
    export_ids: Optional[Sequence[str]] = Field(default=None, alias="exportIds")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ExportInfoModel(BaseModel):
    export_id: str = Field(alias="exportId")
    export_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(
        alias="exportStatus"
    )
    status_message: str = Field(alias="statusMessage")
    export_request_time: datetime = Field(alias="exportRequestTime")
    configurations_download_url: Optional[str] = Field(
        default=None, alias="configurationsDownloadUrl"
    )
    is_truncated: Optional[bool] = Field(default=None, alias="isTruncated")
    requested_start_time: Optional[datetime] = Field(
        default=None, alias="requestedStartTime"
    )
    requested_end_time: Optional[datetime] = Field(
        default=None, alias="requestedEndTime"
    )


class ExportFilterModel(BaseModel):
    name: str = Field(alias="name")
    values: Sequence[str] = Field(alias="values")
    condition: str = Field(alias="condition")


class ImportTaskFilterModel(BaseModel):
    name: Optional[Literal["IMPORT_TASK_ID", "NAME", "STATUS"]] = Field(
        default=None, alias="name"
    )
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class ImportTaskModel(BaseModel):
    import_task_id: Optional[str] = Field(default=None, alias="importTaskId")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    name: Optional[str] = Field(default=None, alias="name")
    import_url: Optional[str] = Field(default=None, alias="importUrl")
    status: Optional[
        Literal[
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_FAILED_LIMIT_EXCEEDED",
            "DELETE_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_COMPLETE_WITH_ERRORS",
            "IMPORT_FAILED",
            "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
            "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
            "IMPORT_IN_PROGRESS",
            "INTERNAL_ERROR",
        ]
    ] = Field(default=None, alias="status")
    import_request_time: Optional[datetime] = Field(
        default=None, alias="importRequestTime"
    )
    import_completion_time: Optional[datetime] = Field(
        default=None, alias="importCompletionTime"
    )
    import_deleted_time: Optional[datetime] = Field(
        default=None, alias="importDeletedTime"
    )
    server_import_success: Optional[int] = Field(
        default=None, alias="serverImportSuccess"
    )
    server_import_failure: Optional[int] = Field(
        default=None, alias="serverImportFailure"
    )
    application_import_success: Optional[int] = Field(
        default=None, alias="applicationImportSuccess"
    )
    application_import_failure: Optional[int] = Field(
        default=None, alias="applicationImportFailure"
    )
    errors_and_failed_entries_zip: Optional[str] = Field(
        default=None, alias="errorsAndFailedEntriesZip"
    )


class TagFilterModel(BaseModel):
    name: str = Field(alias="name")
    values: Sequence[str] = Field(alias="values")


class DisassociateConfigurationItemsFromApplicationRequestModel(BaseModel):
    application_configuration_id: str = Field(alias="applicationConfigurationId")
    configuration_ids: Sequence[str] = Field(alias="configurationIds")


class OrderByElementModel(BaseModel):
    field_name: str = Field(alias="fieldName")
    sort_order: Optional[Literal["ASC", "DESC"]] = Field(
        default=None, alias="sortOrder"
    )


class ListServerNeighborsRequestModel(BaseModel):
    configuration_id: str = Field(alias="configurationId")
    port_information_needed: Optional[bool] = Field(
        default=None, alias="portInformationNeeded"
    )
    neighbor_configuration_ids: Optional[Sequence[str]] = Field(
        default=None, alias="neighborConfigurationIds"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class NeighborConnectionDetailModel(BaseModel):
    source_server_id: str = Field(alias="sourceServerId")
    destination_server_id: str = Field(alias="destinationServerId")
    connections_count: int = Field(alias="connectionsCount")
    destination_port: Optional[int] = Field(default=None, alias="destinationPort")
    transport_protocol: Optional[str] = Field(default=None, alias="transportProtocol")


class StartDataCollectionByAgentIdsRequestModel(BaseModel):
    agent_ids: Sequence[str] = Field(alias="agentIds")


class StartImportTaskRequestModel(BaseModel):
    name: str = Field(alias="name")
    import_url: str = Field(alias="importUrl")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class StopContinuousExportRequestModel(BaseModel):
    export_id: str = Field(alias="exportId")


class StopDataCollectionByAgentIdsRequestModel(BaseModel):
    agent_ids: Sequence[str] = Field(alias="agentIds")


class UpdateApplicationRequestModel(BaseModel):
    configuration_id: str = Field(alias="configurationId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class AgentInfoModel(BaseModel):
    agent_id: Optional[str] = Field(default=None, alias="agentId")
    host_name: Optional[str] = Field(default=None, alias="hostName")
    agent_network_info_list: Optional[List[AgentNetworkInfoModel]] = Field(
        default=None, alias="agentNetworkInfoList"
    )
    connector_id: Optional[str] = Field(default=None, alias="connectorId")
    version: Optional[str] = Field(default=None, alias="version")
    health: Optional[
        Literal["BLACKLISTED", "HEALTHY", "RUNNING", "SHUTDOWN", "UNHEALTHY", "UNKNOWN"]
    ] = Field(default=None, alias="health")
    last_health_ping_time: Optional[str] = Field(
        default=None, alias="lastHealthPingTime"
    )
    collection_status: Optional[str] = Field(default=None, alias="collectionStatus")
    agent_type: Optional[str] = Field(default=None, alias="agentType")
    registered_time: Optional[str] = Field(default=None, alias="registeredTime")


class BatchDeleteImportDataResponseModel(BaseModel):
    errors: List[BatchDeleteImportDataErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateApplicationResponseModel(BaseModel):
    configuration_id: str = Field(alias="configurationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationsResponseModel(BaseModel):
    configurations: List[Dict[str, str]] = Field(alias="configurations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportConfigurationsResponseModel(BaseModel):
    export_id: str = Field(alias="exportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConfigurationsResponseModel(BaseModel):
    configurations: List[Dict[str, str]] = Field(alias="configurations")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartContinuousExportResponseModel(BaseModel):
    export_id: str = Field(alias="exportId")
    s3_bucket: str = Field(alias="s3Bucket")
    start_time: datetime = Field(alias="startTime")
    data_source: Literal["AGENT"] = Field(alias="dataSource")
    schema_storage_config: Dict[str, str] = Field(alias="schemaStorageConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDataCollectionByAgentIdsResponseModel(BaseModel):
    agents_configuration_status: List[AgentConfigurationStatusModel] = Field(
        alias="agentsConfigurationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartExportTaskResponseModel(BaseModel):
    export_id: str = Field(alias="exportId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopContinuousExportResponseModel(BaseModel):
    start_time: datetime = Field(alias="startTime")
    stop_time: datetime = Field(alias="stopTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopDataCollectionByAgentIdsResponseModel(BaseModel):
    agents_configuration_status: List[AgentConfigurationStatusModel] = Field(
        alias="agentsConfigurationStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTagsResponseModel(BaseModel):
    tags: List[ConfigurationTagModel] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeContinuousExportsResponseModel(BaseModel):
    descriptions: List[ContinuousExportDescriptionModel] = Field(alias="descriptions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTagsRequestModel(BaseModel):
    configuration_ids: Sequence[str] = Field(alias="configurationIds")
    tags: Sequence[TagModel] = Field(alias="tags")


class DeleteTagsRequestModel(BaseModel):
    configuration_ids: Sequence[str] = Field(alias="configurationIds")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class GetDiscoverySummaryResponseModel(BaseModel):
    servers: int = Field(alias="servers")
    applications: int = Field(alias="applications")
    servers_mapped_to_applications: int = Field(alias="serversMappedToApplications")
    servers_mappedto_tags: int = Field(alias="serversMappedtoTags")
    agent_summary: CustomerAgentInfoModel = Field(alias="agentSummary")
    connector_summary: CustomerConnectorInfoModel = Field(alias="connectorSummary")
    me_collector_summary: CustomerMeCollectorInfoModel = Field(
        alias="meCollectorSummary"
    )
    agentless_collector_summary: CustomerAgentlessCollectorInfoModel = Field(
        alias="agentlessCollectorSummary"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAgentsRequestModel(BaseModel):
    agent_ids: Optional[Sequence[str]] = Field(default=None, alias="agentIds")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeAgentsRequestDescribeAgentsPaginateModel(BaseModel):
    agent_ids: Optional[Sequence[str]] = Field(default=None, alias="agentIds")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeContinuousExportsRequestDescribeContinuousExportsPaginateModel(BaseModel):
    export_ids: Optional[Sequence[str]] = Field(default=None, alias="exportIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateModel(
    BaseModel
):
    export_ids: Optional[Sequence[str]] = Field(default=None, alias="exportIds")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeExportConfigurationsResponseModel(BaseModel):
    exports_info: List[ExportInfoModel] = Field(alias="exportsInfo")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExportTasksResponseModel(BaseModel):
    exports_info: List[ExportInfoModel] = Field(alias="exportsInfo")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExportTasksRequestDescribeExportTasksPaginateModel(BaseModel):
    export_ids: Optional[Sequence[str]] = Field(default=None, alias="exportIds")
    filters: Optional[Sequence[ExportFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeExportTasksRequestModel(BaseModel):
    export_ids: Optional[Sequence[str]] = Field(default=None, alias="exportIds")
    filters: Optional[Sequence[ExportFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class StartExportTaskRequestModel(BaseModel):
    export_data_format: Optional[Sequence[Literal["CSV", "GRAPHML"]]] = Field(
        default=None, alias="exportDataFormat"
    )
    filters: Optional[Sequence[ExportFilterModel]] = Field(
        default=None, alias="filters"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")


class DescribeImportTasksRequestModel(BaseModel):
    filters: Optional[Sequence[ImportTaskFilterModel]] = Field(
        default=None, alias="filters"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class DescribeImportTasksResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    tasks: List[ImportTaskModel] = Field(alias="tasks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImportTaskResponseModel(BaseModel):
    task: ImportTaskModel = Field(alias="task")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTagsRequestDescribeTagsPaginateModel(BaseModel):
    filters: Optional[Sequence[TagFilterModel]] = Field(default=None, alias="filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeTagsRequestModel(BaseModel):
    filters: Optional[Sequence[TagFilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListConfigurationsRequestListConfigurationsPaginateModel(BaseModel):
    configuration_type: Literal[
        "APPLICATION", "CONNECTION", "PROCESS", "SERVER"
    ] = Field(alias="configurationType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    order_by: Optional[Sequence[OrderByElementModel]] = Field(
        default=None, alias="orderBy"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConfigurationsRequestModel(BaseModel):
    configuration_type: Literal[
        "APPLICATION", "CONNECTION", "PROCESS", "SERVER"
    ] = Field(alias="configurationType")
    filters: Optional[Sequence[FilterModel]] = Field(default=None, alias="filters")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    order_by: Optional[Sequence[OrderByElementModel]] = Field(
        default=None, alias="orderBy"
    )


class ListServerNeighborsResponseModel(BaseModel):
    neighbors: List[NeighborConnectionDetailModel] = Field(alias="neighbors")
    next_token: str = Field(alias="nextToken")
    known_dependency_count: int = Field(alias="knownDependencyCount")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAgentsResponseModel(BaseModel):
    agents_info: List[AgentInfoModel] = Field(alias="agentsInfo")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
