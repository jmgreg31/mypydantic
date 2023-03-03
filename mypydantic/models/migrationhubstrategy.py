# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AntipatternSeveritySummaryModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    severity: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="severity"
    )


class AppUnitErrorModel(BaseModel):
    app_unit_error_category: Optional[
        Literal[
            "CONNECTIVITY_ERROR",
            "CREDENTIAL_ERROR",
            "OTHER_ERROR",
            "PERMISSION_ERROR",
            "UNSUPPORTED_ERROR",
        ]
    ] = Field(default=None, alias="appUnitErrorCategory")


class DatabaseConfigDetailModel(BaseModel):
    secret_name: Optional[str] = Field(default=None, alias="secretName")


class S3ObjectModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3key: Optional[str] = Field(default=None, alias="s3key")


class SourceCodeRepositoryModel(BaseModel):
    branch: Optional[str] = Field(default=None, alias="branch")
    project_name: Optional[str] = Field(default=None, alias="projectName")
    repository: Optional[str] = Field(default=None, alias="repository")
    version_control_type: Optional[str] = Field(
        default=None, alias="versionControlType"
    )


class ApplicationComponentStatusSummaryModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    src_code_or_db_analysis_status: Optional[
        Literal[
            "ANALYSIS_FAILED",
            "ANALYSIS_PARTIAL_SUCCESS",
            "ANALYSIS_STARTED",
            "ANALYSIS_SUCCESS",
            "ANALYSIS_TO_BE_SCHEDULED",
            "CONFIGURED",
            "UNCONFIGURED",
        ]
    ] = Field(default=None, alias="srcCodeOrDbAnalysisStatus")


class ApplicationComponentSummaryModel(BaseModel):
    app_type: Optional[
        Literal[
            "Cassandra",
            "DB2",
            "DotNetFramework",
            "Dotnet",
            "DotnetCore",
            "IBM WebSphere",
            "IIS",
            "JBoss",
            "Java",
            "Maria DB",
            "Mongo DB",
            "MySQL",
            "Oracle",
            "Oracle WebLogic",
            "Other",
            "PostgreSQLServer",
            "SQLServer",
            "Spring",
            "Sybase",
            "Tomcat",
            "Unknown",
            "Visual Basic",
        ]
    ] = Field(default=None, alias="appType")
    count: Optional[int] = Field(default=None, alias="count")


class ServerStatusSummaryModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    run_time_assessment_status: Optional[
        Literal[
            "dataCollectionTaskFailed",
            "dataCollectionTaskPartialSuccess",
            "dataCollectionTaskScheduled",
            "dataCollectionTaskStarted",
            "dataCollectionTaskStopped",
            "dataCollectionTaskSuccess",
            "dataCollectionTaskToBeScheduled",
        ]
    ] = Field(default=None, alias="runTimeAssessmentStatus")


class ServerSummaryModel(BaseModel):
    server_os_type: Optional[
        Literal[
            "AmazonLinux",
            "EndOfSupportWindowsServer",
            "Other",
            "Redhat",
            "WindowsServer",
        ]
    ] = Field(default=None, alias="ServerOsType")
    count: Optional[int] = Field(default=None, alias="count")


class StrategySummaryModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    strategy: Optional[
        Literal[
            "Refactor",
            "Rehost",
            "Relocate",
            "Replatform",
            "Repurchase",
            "Retain",
            "Retirement",
        ]
    ] = Field(default=None, alias="strategy")


class AssessmentTargetModel(BaseModel):
    condition: Literal["CONTAINS", "EQUALS", "NOT_CONTAINS", "NOT_EQUALS"] = Field(
        alias="condition"
    )
    name: str = Field(alias="name")
    values: List[str] = Field(alias="values")


class AssociatedApplicationModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")


class AwsManagedResourcesModel(BaseModel):
    target_destination: List[
        Literal["AWS Elastic BeanStalk", "AWS Fargate", "None specified"]
    ] = Field(alias="targetDestination")


class BusinessGoalsModel(BaseModel):
    license_cost_reduction: Optional[int] = Field(
        default=None, alias="licenseCostReduction"
    )
    modernize_infrastructure_with_cloud_native_technologies: Optional[int] = Field(
        default=None, alias="modernizeInfrastructureWithCloudNativeTechnologies"
    )
    reduce_operational_overhead_with_managed_services: Optional[int] = Field(
        default=None, alias="reduceOperationalOverheadWithManagedServices"
    )
    speed_of_migration: Optional[int] = Field(default=None, alias="speedOfMigration")


class IPAddressBasedRemoteInfoModel(BaseModel):
    auth_type: Optional[Literal["CERT", "NTLM", "SSH"]] = Field(
        default=None, alias="authType"
    )
    ip_address_configuration_time_stamp: Optional[str] = Field(
        default=None, alias="ipAddressConfigurationTimeStamp"
    )
    os_type: Optional[Literal["LINUX", "WINDOWS"]] = Field(default=None, alias="osType")


class PipelineInfoModel(BaseModel):
    pipeline_configuration_time_stamp: Optional[str] = Field(
        default=None, alias="pipelineConfigurationTimeStamp"
    )
    pipeline_type: Optional[Literal["AZURE_DEVOPS"]] = Field(
        default=None, alias="pipelineType"
    )


class RemoteSourceCodeAnalysisServerInfoModel(BaseModel):
    remote_source_code_analysis_server_configuration_timestamp: Optional[str] = Field(
        default=None, alias="remoteSourceCodeAnalysisServerConfigurationTimestamp"
    )


class VcenterBasedRemoteInfoModel(BaseModel):
    os_type: Optional[Literal["LINUX", "WINDOWS"]] = Field(default=None, alias="osType")
    vcenter_configuration_time_stamp: Optional[str] = Field(
        default=None, alias="vcenterConfigurationTimeStamp"
    )


class VersionControlInfoModel(BaseModel):
    version_control_configuration_time_stamp: Optional[str] = Field(
        default=None, alias="versionControlConfigurationTimeStamp"
    )
    version_control_type: Optional[
        Literal["AZURE_DEVOPS_GIT", "GITHUB", "GITHUB_ENTERPRISE"]
    ] = Field(default=None, alias="versionControlType")


class DataCollectionDetailsModel(BaseModel):
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")
    failed: Optional[int] = Field(default=None, alias="failed")
    in_progress: Optional[int] = Field(default=None, alias="inProgress")
    servers: Optional[int] = Field(default=None, alias="servers")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    status: Optional[Literal["COMPLETE", "FAILED", "IN_PROGRESS", "STOPPED"]] = Field(
        default=None, alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    success: Optional[int] = Field(default=None, alias="success")


class HeterogeneousModel(BaseModel):
    target_database_engine: List[
        Literal[
            "AWS PostgreSQL",
            "Amazon Aurora",
            "Db2 LUW",
            "MariaDB",
            "Microsoft SQL Server",
            "MongoDB",
            "MySQL",
            "None specified",
            "Oracle Database",
            "SAP",
        ]
    ] = Field(alias="targetDatabaseEngine")


class HomogeneousModel(BaseModel):
    target_database_engine: Optional[List[Literal["None specified"]]] = Field(
        default=None, alias="targetDatabaseEngine"
    )


class NoDatabaseMigrationPreferenceModel(BaseModel):
    target_database_engine: List[
        Literal[
            "AWS PostgreSQL",
            "Amazon Aurora",
            "Db2 LUW",
            "MariaDB",
            "Microsoft SQL Server",
            "MongoDB",
            "MySQL",
            "None specified",
            "Oracle Database",
            "SAP",
        ]
    ] = Field(alias="targetDatabaseEngine")


class GetApplicationComponentDetailsRequestModel(BaseModel):
    application_component_id: str = Field(alias="applicationComponentId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetApplicationComponentStrategiesRequestModel(BaseModel):
    application_component_id: str = Field(alias="applicationComponentId")


class GetAssessmentRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetImportFileTaskRequestModel(BaseModel):
    id: str = Field(alias="id")


class GetRecommendationReportDetailsRequestModel(BaseModel):
    id: str = Field(alias="id")


class RecommendationReportDetailsModel(BaseModel):
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")
    s3_bucket: Optional[str] = Field(default=None, alias="s3Bucket")
    s3_keys: Optional[List[str]] = Field(default=None, alias="s3Keys")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SUCCESS"]] = Field(
        default=None, alias="status"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetServerDetailsRequestModel(BaseModel):
    server_id: str = Field(alias="serverId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetServerStrategiesRequestModel(BaseModel):
    server_id: str = Field(alias="serverId")


class GroupModel(BaseModel):
    name: Optional[Literal["ExternalId"]] = Field(default=None, alias="name")
    value: Optional[str] = Field(default=None, alias="value")


class ImportFileTaskInformationModel(BaseModel):
    completion_time: Optional[datetime] = Field(default=None, alias="completionTime")
    id: Optional[str] = Field(default=None, alias="id")
    import_name: Optional[str] = Field(default=None, alias="importName")
    input_s3_bucket: Optional[str] = Field(default=None, alias="inputS3Bucket")
    input_s3_key: Optional[str] = Field(default=None, alias="inputS3Key")
    number_of_records_failed: Optional[int] = Field(
        default=None, alias="numberOfRecordsFailed"
    )
    number_of_records_success: Optional[int] = Field(
        default=None, alias="numberOfRecordsSuccess"
    )
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    status: Optional[
        Literal[
            "DeleteFailed",
            "DeleteInProgress",
            "DeletePartialSuccess",
            "DeleteSuccess",
            "ImportFailed",
            "ImportInProgress",
            "ImportPartialSuccess",
            "ImportSuccess",
        ]
    ] = Field(default=None, alias="status")
    status_report_s3_bucket: Optional[str] = Field(
        default=None, alias="statusReportS3Bucket"
    )
    status_report_s3_key: Optional[str] = Field(default=None, alias="statusReportS3Key")


class ListCollectorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListImportFileTaskRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class NoManagementPreferenceModel(BaseModel):
    target_destination: List[
        Literal[
            "AWS Elastic BeanStalk",
            "AWS Fargate",
            "Amazon Elastic Cloud Compute (EC2)",
            "Amazon Elastic Container Service (ECS)",
            "Amazon Elastic Kubernetes Service (EKS)",
            "None specified",
        ]
    ] = Field(alias="targetDestination")


class SelfManageResourcesModel(BaseModel):
    target_destination: List[
        Literal[
            "Amazon Elastic Cloud Compute (EC2)",
            "Amazon Elastic Container Service (ECS)",
            "Amazon Elastic Kubernetes Service (EKS)",
            "None specified",
        ]
    ] = Field(alias="targetDestination")


class NetworkInfoModel(BaseModel):
    interface_name: str = Field(alias="interfaceName")
    ip_address: str = Field(alias="ipAddress")
    mac_address: str = Field(alias="macAddress")
    net_mask: str = Field(alias="netMask")


class OSInfoModel(BaseModel):
    type: Optional[Literal["LINUX", "WINDOWS"]] = Field(default=None, alias="type")
    version: Optional[str] = Field(default=None, alias="version")


class TransformationToolModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    name: Optional[
        Literal[
            "App2Container",
            "Application Migration Service",
            "Database Migration Service",
            "End of Support Migration",
            "In Place Operating System Upgrade",
            "Native SQL Server Backup/Restore",
            "Porting Assistant For .NET",
            "Schema Conversion Tool",
            "Strategy Recommendation Support",
            "Windows Web Application Migration Assistant",
        ]
    ] = Field(default=None, alias="name")
    tranformation_tool_installation_link: Optional[str] = Field(
        default=None, alias="tranformationToolInstallationLink"
    )


class ServerErrorModel(BaseModel):
    server_error_category: Optional[
        Literal[
            "ARCHITECTURE_ERROR",
            "CONNECTIVITY_ERROR",
            "CREDENTIAL_ERROR",
            "OTHER_ERROR",
            "PERMISSION_ERROR",
        ]
    ] = Field(default=None, alias="serverErrorCategory")


class SourceCodeModel(BaseModel):
    location: Optional[str] = Field(default=None, alias="location")
    project_name: Optional[str] = Field(default=None, alias="projectName")
    source_version: Optional[str] = Field(default=None, alias="sourceVersion")
    version_control: Optional[
        Literal["AZURE_DEVOPS_GIT", "GITHUB", "GITHUB_ENTERPRISE"]
    ] = Field(default=None, alias="versionControl")


class StopAssessmentRequestModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")


class StrategyOptionModel(BaseModel):
    is_preferred: Optional[bool] = Field(default=None, alias="isPreferred")
    strategy: Optional[
        Literal[
            "Refactor",
            "Rehost",
            "Relocate",
            "Replatform",
            "Repurchase",
            "Retain",
            "Retirement",
        ]
    ] = Field(default=None, alias="strategy")
    target_destination: Optional[
        Literal[
            "AWS Elastic BeanStalk",
            "AWS Fargate",
            "Amazon DocumentDB",
            "Amazon DynamoDB",
            "Amazon Elastic Cloud Compute (EC2)",
            "Amazon Elastic Container Service (ECS)",
            "Amazon Elastic Kubernetes Service (EKS)",
            "Amazon Relational Database Service",
            "Amazon Relational Database Service on MySQL",
            "Amazon Relational Database Service on PostgreSQL",
            "Aurora MySQL",
            "Aurora PostgreSQL",
            "Babelfish for Aurora PostgreSQL",
            "None specified",
        ]
    ] = Field(default=None, alias="targetDestination")
    tool_name: Optional[
        Literal[
            "App2Container",
            "Application Migration Service",
            "Database Migration Service",
            "End of Support Migration",
            "In Place Operating System Upgrade",
            "Native SQL Server Backup/Restore",
            "Porting Assistant For .NET",
            "Schema Conversion Tool",
            "Strategy Recommendation Support",
            "Windows Web Application Migration Assistant",
        ]
    ] = Field(default=None, alias="toolName")


class AssessmentSummaryModel(BaseModel):
    antipattern_report_s3_object: Optional[S3ObjectModel] = Field(
        default=None, alias="antipatternReportS3Object"
    )
    antipattern_report_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
    ] = Field(default=None, alias="antipatternReportStatus")
    antipattern_report_status_message: Optional[str] = Field(
        default=None, alias="antipatternReportStatusMessage"
    )
    last_analyzed_timestamp: Optional[datetime] = Field(
        default=None, alias="lastAnalyzedTimestamp"
    )
    list_antipattern_severity_summary: Optional[
        List[AntipatternSeveritySummaryModel]
    ] = Field(default=None, alias="listAntipatternSeveritySummary")
    list_application_component_status_summary: Optional[
        List[ApplicationComponentStatusSummaryModel]
    ] = Field(default=None, alias="listApplicationComponentStatusSummary")
    list_application_component_strategy_summary: Optional[
        List[StrategySummaryModel]
    ] = Field(default=None, alias="listApplicationComponentStrategySummary")
    list_application_component_summary: Optional[
        List[ApplicationComponentSummaryModel]
    ] = Field(default=None, alias="listApplicationComponentSummary")
    list_server_status_summary: Optional[List[ServerStatusSummaryModel]] = Field(
        default=None, alias="listServerStatusSummary"
    )
    list_server_strategy_summary: Optional[List[StrategySummaryModel]] = Field(
        default=None, alias="listServerStrategySummary"
    )
    list_server_summary: Optional[List[ServerSummaryModel]] = Field(
        default=None, alias="listServerSummary"
    )


class StartAssessmentRequestModel(BaseModel):
    assessment_targets: Optional[Sequence[AssessmentTargetModel]] = Field(
        default=None, alias="assessmentTargets"
    )
    s3bucket_for_analysis_data: Optional[str] = Field(
        default=None, alias="s3bucketForAnalysisData"
    )
    s3bucket_for_report_data: Optional[str] = Field(
        default=None, alias="s3bucketForReportData"
    )


class PrioritizeBusinessGoalsModel(BaseModel):
    business_goals: Optional[BusinessGoalsModel] = Field(
        default=None, alias="businessGoals"
    )


class ConfigurationSummaryModel(BaseModel):
    ip_address_based_remote_info_list: Optional[
        List[IPAddressBasedRemoteInfoModel]
    ] = Field(default=None, alias="ipAddressBasedRemoteInfoList")
    pipeline_info_list: Optional[List[PipelineInfoModel]] = Field(
        default=None, alias="pipelineInfoList"
    )
    remote_source_code_analysis_server_info: Optional[
        RemoteSourceCodeAnalysisServerInfoModel
    ] = Field(default=None, alias="remoteSourceCodeAnalysisServerInfo")
    vcenter_based_remote_info_list: Optional[List[VcenterBasedRemoteInfoModel]] = Field(
        default=None, alias="vcenterBasedRemoteInfoList"
    )
    version_control_info_list: Optional[List[VersionControlInfoModel]] = Field(
        default=None, alias="versionControlInfoList"
    )


class DatabaseMigrationPreferenceModel(BaseModel):
    heterogeneous: Optional[HeterogeneousModel] = Field(
        default=None, alias="heterogeneous"
    )
    homogeneous: Optional[HomogeneousModel] = Field(default=None, alias="homogeneous")
    no_preference: Optional[NoDatabaseMigrationPreferenceModel] = Field(
        default=None, alias="noPreference"
    )


class GetAssessmentResponseModel(BaseModel):
    assessment_targets: List[AssessmentTargetModel] = Field(alias="assessmentTargets")
    data_collection_details: DataCollectionDetailsModel = Field(
        alias="dataCollectionDetails"
    )
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetImportFileTaskResponseModel(BaseModel):
    completion_time: datetime = Field(alias="completionTime")
    id: str = Field(alias="id")
    import_name: str = Field(alias="importName")
    input_s3_bucket: str = Field(alias="inputS3Bucket")
    input_s3_key: str = Field(alias="inputS3Key")
    number_of_records_failed: int = Field(alias="numberOfRecordsFailed")
    number_of_records_success: int = Field(alias="numberOfRecordsSuccess")
    start_time: datetime = Field(alias="startTime")
    status: Literal[
        "DeleteFailed",
        "DeleteInProgress",
        "DeletePartialSuccess",
        "DeleteSuccess",
        "ImportFailed",
        "ImportInProgress",
        "ImportPartialSuccess",
        "ImportSuccess",
    ] = Field(alias="status")
    status_report_s3_bucket: str = Field(alias="statusReportS3Bucket")
    status_report_s3_key: str = Field(alias="statusReportS3Key")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLatestAssessmentIdResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAssessmentResponseModel(BaseModel):
    assessment_id: str = Field(alias="assessmentId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartImportFileTaskResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartRecommendationReportGenerationResponseModel(BaseModel):
    id: str = Field(alias="id")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommendationReportDetailsResponseModel(BaseModel):
    id: str = Field(alias="id")
    recommendation_report_details: RecommendationReportDetailsModel = Field(
        alias="recommendationReportDetails"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServerDetailsRequestGetServerDetailsPaginateModel(BaseModel):
    server_id: str = Field(alias="serverId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCollectorsRequestListCollectorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListImportFileTaskRequestListImportFileTaskPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationComponentsRequestListApplicationComponentsPaginateModel(BaseModel):
    application_component_criteria: Optional[
        Literal[
            "ANALYSIS_STATUS",
            "APP_NAME",
            "APP_TYPE",
            "DESTINATION",
            "ERROR_CATEGORY",
            "NOT_DEFINED",
            "SERVER_ID",
            "STRATEGY",
        ]
    ] = Field(default=None, alias="applicationComponentCriteria")
    filter_value: Optional[str] = Field(default=None, alias="filterValue")
    group_id_filter: Optional[Sequence[GroupModel]] = Field(
        default=None, alias="groupIdFilter"
    )
    sort: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="sort")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListApplicationComponentsRequestModel(BaseModel):
    application_component_criteria: Optional[
        Literal[
            "ANALYSIS_STATUS",
            "APP_NAME",
            "APP_TYPE",
            "DESTINATION",
            "ERROR_CATEGORY",
            "NOT_DEFINED",
            "SERVER_ID",
            "STRATEGY",
        ]
    ] = Field(default=None, alias="applicationComponentCriteria")
    filter_value: Optional[str] = Field(default=None, alias="filterValue")
    group_id_filter: Optional[Sequence[GroupModel]] = Field(
        default=None, alias="groupIdFilter"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    sort: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="sort")


class ListServersRequestListServersPaginateModel(BaseModel):
    filter_value: Optional[str] = Field(default=None, alias="filterValue")
    group_id_filter: Optional[Sequence[GroupModel]] = Field(
        default=None, alias="groupIdFilter"
    )
    server_criteria: Optional[
        Literal[
            "ANALYSIS_STATUS",
            "DESTINATION",
            "ERROR_CATEGORY",
            "NOT_DEFINED",
            "OS_NAME",
            "SERVER_ID",
            "STRATEGY",
        ]
    ] = Field(default=None, alias="serverCriteria")
    sort: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="sort")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServersRequestModel(BaseModel):
    filter_value: Optional[str] = Field(default=None, alias="filterValue")
    group_id_filter: Optional[Sequence[GroupModel]] = Field(
        default=None, alias="groupIdFilter"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    server_criteria: Optional[
        Literal[
            "ANALYSIS_STATUS",
            "DESTINATION",
            "ERROR_CATEGORY",
            "NOT_DEFINED",
            "OS_NAME",
            "SERVER_ID",
            "STRATEGY",
        ]
    ] = Field(default=None, alias="serverCriteria")
    sort: Optional[Literal["ASC", "DESC"]] = Field(default=None, alias="sort")


class StartImportFileTaskRequestModel(BaseModel):
    s3_bucket: str = Field(alias="S3Bucket")
    name: str = Field(alias="name")
    s3key: str = Field(alias="s3key")
    data_source_type: Optional[Literal["ApplicationDiscoveryService", "MPA"]] = Field(
        default=None, alias="dataSourceType"
    )
    group_id: Optional[Sequence[GroupModel]] = Field(default=None, alias="groupId")
    s3bucket_for_report_data: Optional[str] = Field(
        default=None, alias="s3bucketForReportData"
    )


class StartRecommendationReportGenerationRequestModel(BaseModel):
    group_id_filter: Optional[Sequence[GroupModel]] = Field(
        default=None, alias="groupIdFilter"
    )
    output_format: Optional[Literal["Excel", "Json"]] = Field(
        default=None, alias="outputFormat"
    )


class ListImportFileTaskResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    task_infos: List[ImportFileTaskInformationModel] = Field(alias="taskInfos")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ManagementPreferenceModel(BaseModel):
    aws_managed_resources: Optional[AwsManagedResourcesModel] = Field(
        default=None, alias="awsManagedResources"
    )
    no_preference: Optional[NoManagementPreferenceModel] = Field(
        default=None, alias="noPreference"
    )
    self_manage_resources: Optional[SelfManageResourcesModel] = Field(
        default=None, alias="selfManageResources"
    )


class SystemInfoModel(BaseModel):
    cpu_architecture: Optional[str] = Field(default=None, alias="cpuArchitecture")
    file_system_type: Optional[str] = Field(default=None, alias="fileSystemType")
    network_info_list: Optional[List[NetworkInfoModel]] = Field(
        default=None, alias="networkInfoList"
    )
    os_info: Optional[OSInfoModel] = Field(default=None, alias="osInfo")


class RecommendationSetModel(BaseModel):
    strategy: Optional[
        Literal[
            "Refactor",
            "Rehost",
            "Relocate",
            "Replatform",
            "Repurchase",
            "Retain",
            "Retirement",
        ]
    ] = Field(default=None, alias="strategy")
    target_destination: Optional[
        Literal[
            "AWS Elastic BeanStalk",
            "AWS Fargate",
            "Amazon DocumentDB",
            "Amazon DynamoDB",
            "Amazon Elastic Cloud Compute (EC2)",
            "Amazon Elastic Container Service (ECS)",
            "Amazon Elastic Kubernetes Service (EKS)",
            "Amazon Relational Database Service",
            "Amazon Relational Database Service on MySQL",
            "Amazon Relational Database Service on PostgreSQL",
            "Aurora MySQL",
            "Aurora PostgreSQL",
            "Babelfish for Aurora PostgreSQL",
            "None specified",
        ]
    ] = Field(default=None, alias="targetDestination")
    transformation_tool: Optional[TransformationToolModel] = Field(
        default=None, alias="transformationTool"
    )


class UpdateApplicationComponentConfigRequestModel(BaseModel):
    application_component_id: str = Field(alias="applicationComponentId")
    app_type: Optional[
        Literal[
            "Cassandra",
            "DB2",
            "DotNetFramework",
            "Dotnet",
            "DotnetCore",
            "IBM WebSphere",
            "IIS",
            "JBoss",
            "Java",
            "Maria DB",
            "Mongo DB",
            "MySQL",
            "Oracle",
            "Oracle WebLogic",
            "Other",
            "PostgreSQLServer",
            "SQLServer",
            "Spring",
            "Sybase",
            "Tomcat",
            "Unknown",
            "Visual Basic",
        ]
    ] = Field(default=None, alias="appType")
    configure_only: Optional[bool] = Field(default=None, alias="configureOnly")
    inclusion_status: Optional[
        Literal["excludeFromAssessment", "includeInAssessment"]
    ] = Field(default=None, alias="inclusionStatus")
    secrets_manager_key: Optional[str] = Field(default=None, alias="secretsManagerKey")
    source_code_list: Optional[Sequence[SourceCodeModel]] = Field(
        default=None, alias="sourceCodeList"
    )
    strategy_option: Optional[StrategyOptionModel] = Field(
        default=None, alias="strategyOption"
    )


class UpdateServerConfigRequestModel(BaseModel):
    server_id: str = Field(alias="serverId")
    strategy_option: Optional[StrategyOptionModel] = Field(
        default=None, alias="strategyOption"
    )


class GetPortfolioSummaryResponseModel(BaseModel):
    assessment_summary: AssessmentSummaryModel = Field(alias="assessmentSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CollectorModel(BaseModel):
    collector_health: Optional[
        Literal["COLLECTOR_HEALTHY", "COLLECTOR_UNHEALTHY"]
    ] = Field(default=None, alias="collectorHealth")
    collector_id: Optional[str] = Field(default=None, alias="collectorId")
    collector_version: Optional[str] = Field(default=None, alias="collectorVersion")
    configuration_summary: Optional[ConfigurationSummaryModel] = Field(
        default=None, alias="configurationSummary"
    )
    host_name: Optional[str] = Field(default=None, alias="hostName")
    ip_address: Optional[str] = Field(default=None, alias="ipAddress")
    last_activity_time_stamp: Optional[str] = Field(
        default=None, alias="lastActivityTimeStamp"
    )
    registered_time_stamp: Optional[str] = Field(
        default=None, alias="registeredTimeStamp"
    )


class DatabasePreferencesModel(BaseModel):
    database_management_preference: Optional[
        Literal["AWS-managed", "No preference", "Self-manage"]
    ] = Field(default=None, alias="databaseManagementPreference")
    database_migration_preference: Optional[DatabaseMigrationPreferenceModel] = Field(
        default=None, alias="databaseMigrationPreference"
    )


class ApplicationPreferencesModel(BaseModel):
    management_preference: Optional[ManagementPreferenceModel] = Field(
        default=None, alias="managementPreference"
    )


class ApplicationComponentDetailModel(BaseModel):
    analysis_status: Optional[
        Literal[
            "ANALYSIS_FAILED",
            "ANALYSIS_PARTIAL_SUCCESS",
            "ANALYSIS_STARTED",
            "ANALYSIS_SUCCESS",
            "ANALYSIS_TO_BE_SCHEDULED",
            "CONFIGURED",
            "UNCONFIGURED",
        ]
    ] = Field(default=None, alias="analysisStatus")
    antipattern_report_s3_object: Optional[S3ObjectModel] = Field(
        default=None, alias="antipatternReportS3Object"
    )
    antipattern_report_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
    ] = Field(default=None, alias="antipatternReportStatus")
    antipattern_report_status_message: Optional[str] = Field(
        default=None, alias="antipatternReportStatusMessage"
    )
    app_type: Optional[
        Literal[
            "Cassandra",
            "DB2",
            "DotNetFramework",
            "Dotnet",
            "DotnetCore",
            "IBM WebSphere",
            "IIS",
            "JBoss",
            "Java",
            "Maria DB",
            "Mongo DB",
            "MySQL",
            "Oracle",
            "Oracle WebLogic",
            "Other",
            "PostgreSQLServer",
            "SQLServer",
            "Spring",
            "Sybase",
            "Tomcat",
            "Unknown",
            "Visual Basic",
        ]
    ] = Field(default=None, alias="appType")
    app_unit_error: Optional[AppUnitErrorModel] = Field(
        default=None, alias="appUnitError"
    )
    associated_server_id: Optional[str] = Field(
        default=None, alias="associatedServerId"
    )
    database_config_detail: Optional[DatabaseConfigDetailModel] = Field(
        default=None, alias="databaseConfigDetail"
    )
    id: Optional[str] = Field(default=None, alias="id")
    inclusion_status: Optional[
        Literal["excludeFromAssessment", "includeInAssessment"]
    ] = Field(default=None, alias="inclusionStatus")
    last_analyzed_timestamp: Optional[datetime] = Field(
        default=None, alias="lastAnalyzedTimestamp"
    )
    list_antipattern_severity_summary: Optional[
        List[AntipatternSeveritySummaryModel]
    ] = Field(default=None, alias="listAntipatternSeveritySummary")
    more_server_association_exists: Optional[bool] = Field(
        default=None, alias="moreServerAssociationExists"
    )
    name: Optional[str] = Field(default=None, alias="name")
    os_driver: Optional[str] = Field(default=None, alias="osDriver")
    os_version: Optional[str] = Field(default=None, alias="osVersion")
    recommendation_set: Optional[RecommendationSetModel] = Field(
        default=None, alias="recommendationSet"
    )
    resource_sub_type: Optional[
        Literal["Database", "DatabaseProcess", "Process"]
    ] = Field(default=None, alias="resourceSubType")
    runtime_status: Optional[
        Literal[
            "ANALYSIS_FAILED",
            "ANALYSIS_STARTED",
            "ANALYSIS_SUCCESS",
            "ANALYSIS_TO_BE_SCHEDULED",
        ]
    ] = Field(default=None, alias="runtimeStatus")
    runtime_status_message: Optional[str] = Field(
        default=None, alias="runtimeStatusMessage"
    )
    source_code_repositories: Optional[List[SourceCodeRepositoryModel]] = Field(
        default=None, alias="sourceCodeRepositories"
    )
    status_message: Optional[str] = Field(default=None, alias="statusMessage")


class ApplicationComponentStrategyModel(BaseModel):
    is_preferred: Optional[bool] = Field(default=None, alias="isPreferred")
    recommendation: Optional[RecommendationSetModel] = Field(
        default=None, alias="recommendation"
    )
    status: Optional[
        Literal["notRecommended", "potential", "recommended", "viableOption"]
    ] = Field(default=None, alias="status")


class ServerDetailModel(BaseModel):
    antipattern_report_s3_object: Optional[S3ObjectModel] = Field(
        default=None, alias="antipatternReportS3Object"
    )
    antipattern_report_status: Optional[
        Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
    ] = Field(default=None, alias="antipatternReportStatus")
    antipattern_report_status_message: Optional[str] = Field(
        default=None, alias="antipatternReportStatusMessage"
    )
    application_component_strategy_summary: Optional[
        List[StrategySummaryModel]
    ] = Field(default=None, alias="applicationComponentStrategySummary")
    data_collection_status: Optional[
        Literal[
            "dataCollectionTaskFailed",
            "dataCollectionTaskPartialSuccess",
            "dataCollectionTaskScheduled",
            "dataCollectionTaskStarted",
            "dataCollectionTaskStopped",
            "dataCollectionTaskSuccess",
            "dataCollectionTaskToBeScheduled",
        ]
    ] = Field(default=None, alias="dataCollectionStatus")
    id: Optional[str] = Field(default=None, alias="id")
    last_analyzed_timestamp: Optional[datetime] = Field(
        default=None, alias="lastAnalyzedTimestamp"
    )
    list_antipattern_severity_summary: Optional[
        List[AntipatternSeveritySummaryModel]
    ] = Field(default=None, alias="listAntipatternSeveritySummary")
    name: Optional[str] = Field(default=None, alias="name")
    recommendation_set: Optional[RecommendationSetModel] = Field(
        default=None, alias="recommendationSet"
    )
    server_error: Optional[ServerErrorModel] = Field(default=None, alias="serverError")
    server_type: Optional[str] = Field(default=None, alias="serverType")
    status_message: Optional[str] = Field(default=None, alias="statusMessage")
    system_info: Optional[SystemInfoModel] = Field(default=None, alias="systemInfo")


class ServerStrategyModel(BaseModel):
    is_preferred: Optional[bool] = Field(default=None, alias="isPreferred")
    number_of_application_components: Optional[int] = Field(
        default=None, alias="numberOfApplicationComponents"
    )
    recommendation: Optional[RecommendationSetModel] = Field(
        default=None, alias="recommendation"
    )
    status: Optional[
        Literal["notRecommended", "potential", "recommended", "viableOption"]
    ] = Field(default=None, alias="status")


class ListCollectorsResponseModel(BaseModel):
    collectors: List[CollectorModel] = Field(alias="Collectors")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPortfolioPreferencesResponseModel(BaseModel):
    application_mode: Literal["ALL", "KNOWN", "UNKNOWN"] = Field(
        alias="applicationMode"
    )
    application_preferences: ApplicationPreferencesModel = Field(
        alias="applicationPreferences"
    )
    database_preferences: DatabasePreferencesModel = Field(alias="databasePreferences")
    prioritize_business_goals: PrioritizeBusinessGoalsModel = Field(
        alias="prioritizeBusinessGoals"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPortfolioPreferencesRequestModel(BaseModel):
    application_mode: Optional[Literal["ALL", "KNOWN", "UNKNOWN"]] = Field(
        default=None, alias="applicationMode"
    )
    application_preferences: Optional[ApplicationPreferencesModel] = Field(
        default=None, alias="applicationPreferences"
    )
    database_preferences: Optional[DatabasePreferencesModel] = Field(
        default=None, alias="databasePreferences"
    )
    prioritize_business_goals: Optional[PrioritizeBusinessGoalsModel] = Field(
        default=None, alias="prioritizeBusinessGoals"
    )


class GetApplicationComponentDetailsResponseModel(BaseModel):
    application_component_detail: ApplicationComponentDetailModel = Field(
        alias="applicationComponentDetail"
    )
    associated_applications: List[AssociatedApplicationModel] = Field(
        alias="associatedApplications"
    )
    associated_server_ids: List[str] = Field(alias="associatedServerIds")
    more_application_resource: bool = Field(alias="moreApplicationResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationComponentsResponseModel(BaseModel):
    application_component_infos: List[ApplicationComponentDetailModel] = Field(
        alias="applicationComponentInfos"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetApplicationComponentStrategiesResponseModel(BaseModel):
    application_component_strategies: List[ApplicationComponentStrategyModel] = Field(
        alias="applicationComponentStrategies"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServerDetailsResponseModel(BaseModel):
    associated_applications: List[AssociatedApplicationModel] = Field(
        alias="associatedApplications"
    )
    next_token: str = Field(alias="nextToken")
    server_detail: ServerDetailModel = Field(alias="serverDetail")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServersResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    server_infos: List[ServerDetailModel] = Field(alias="serverInfos")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetServerStrategiesResponseModel(BaseModel):
    server_strategies: List[ServerStrategyModel] = Field(alias="serverStrategies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
