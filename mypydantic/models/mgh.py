# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApplicationStateModel(BaseModel):
    application_id: Optional[str] = Field(default=None, alias="ApplicationId")
    application_status: Optional[
        Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"]
    ] = Field(default=None, alias="ApplicationStatus")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class CreatedArtifactModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")


class DiscoveredResourceModel(BaseModel):
    configuration_id: str = Field(alias="ConfigurationId")
    description: Optional[str] = Field(default=None, alias="Description")


class CreateProgressUpdateStreamRequestModel(BaseModel):
    progress_update_stream_name: str = Field(alias="ProgressUpdateStreamName")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class DeleteProgressUpdateStreamRequestModel(BaseModel):
    progress_update_stream_name: str = Field(alias="ProgressUpdateStreamName")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class DescribeApplicationStateRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DescribeMigrationTaskRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")


class DisassociateCreatedArtifactRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    created_artifact_name: str = Field(alias="CreatedArtifactName")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class DisassociateDiscoveredResourceRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    configuration_id: str = Field(alias="ConfigurationId")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class ImportMigrationTaskRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListApplicationStatesRequestModel(BaseModel):
    application_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ApplicationIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListCreatedArtifactsRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDiscoveredResourcesRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListMigrationTasksRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class MigrationTaskSummaryModel(BaseModel):
    progress_update_stream: Optional[str] = Field(
        default=None, alias="ProgressUpdateStream"
    )
    migration_task_name: Optional[str] = Field(default=None, alias="MigrationTaskName")
    status: Optional[
        Literal["COMPLETED", "FAILED", "IN_PROGRESS", "NOT_STARTED"]
    ] = Field(default=None, alias="Status")
    progress_percent: Optional[int] = Field(default=None, alias="ProgressPercent")
    status_detail: Optional[str] = Field(default=None, alias="StatusDetail")
    update_date_time: Optional[datetime] = Field(default=None, alias="UpdateDateTime")


class ListProgressUpdateStreamsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ProgressUpdateStreamSummaryModel(BaseModel):
    progress_update_stream_name: Optional[str] = Field(
        default=None, alias="ProgressUpdateStreamName"
    )


class ResourceAttributeModel(BaseModel):
    type: Literal[
        "BIOS_ID",
        "FQDN",
        "IPV4_ADDRESS",
        "IPV6_ADDRESS",
        "MAC_ADDRESS",
        "MOTHERBOARD_SERIAL_NUMBER",
        "VM_MANAGED_OBJECT_REFERENCE",
        "VM_MANAGER_ID",
        "VM_NAME",
        "VM_PATH",
    ] = Field(alias="Type")
    value: str = Field(alias="Value")


class TaskModel(BaseModel):
    status: Literal["COMPLETED", "FAILED", "IN_PROGRESS", "NOT_STARTED"] = Field(
        alias="Status"
    )
    status_detail: Optional[str] = Field(default=None, alias="StatusDetail")
    progress_percent: Optional[int] = Field(default=None, alias="ProgressPercent")


class NotifyApplicationStateRequestModel(BaseModel):
    application_id: str = Field(alias="ApplicationId")
    status: Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"] = Field(alias="Status")
    update_date_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="UpdateDateTime"
    )
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class AssociateCreatedArtifactRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    created_artifact: CreatedArtifactModel = Field(alias="CreatedArtifact")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class AssociateDiscoveredResourceRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    discovered_resource: DiscoveredResourceModel = Field(alias="DiscoveredResource")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class DescribeApplicationStateResultModel(BaseModel):
    application_status: Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"] = Field(
        alias="ApplicationStatus"
    )
    last_updated_time: datetime = Field(alias="LastUpdatedTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationStatesResultModel(BaseModel):
    application_state_list: List[ApplicationStateModel] = Field(
        alias="ApplicationStateList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCreatedArtifactsResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    created_artifact_list: List[CreatedArtifactModel] = Field(
        alias="CreatedArtifactList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDiscoveredResourcesResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    discovered_resource_list: List[DiscoveredResourceModel] = Field(
        alias="DiscoveredResourceList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListApplicationStatesRequestListApplicationStatesPaginateModel(BaseModel):
    application_ids: Optional[Sequence[str]] = Field(
        default=None, alias="ApplicationIds"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCreatedArtifactsRequestListCreatedArtifactsPaginateModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMigrationTasksRequestListMigrationTasksPaginateModel(BaseModel):
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMigrationTasksResultModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    migration_task_summary_list: List[MigrationTaskSummaryModel] = Field(
        alias="MigrationTaskSummaryList"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProgressUpdateStreamsResultModel(BaseModel):
    progress_update_stream_summary_list: List[ProgressUpdateStreamSummaryModel] = Field(
        alias="ProgressUpdateStreamSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutResourceAttributesRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    resource_attribute_list: Sequence[ResourceAttributeModel] = Field(
        alias="ResourceAttributeList"
    )
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class MigrationTaskModel(BaseModel):
    progress_update_stream: Optional[str] = Field(
        default=None, alias="ProgressUpdateStream"
    )
    migration_task_name: Optional[str] = Field(default=None, alias="MigrationTaskName")
    task: Optional[TaskModel] = Field(default=None, alias="Task")
    update_date_time: Optional[datetime] = Field(default=None, alias="UpdateDateTime")
    resource_attribute_list: Optional[List[ResourceAttributeModel]] = Field(
        default=None, alias="ResourceAttributeList"
    )


class NotifyMigrationTaskStateRequestModel(BaseModel):
    progress_update_stream: str = Field(alias="ProgressUpdateStream")
    migration_task_name: str = Field(alias="MigrationTaskName")
    task: TaskModel = Field(alias="Task")
    update_date_time: Union[datetime, str] = Field(alias="UpdateDateTime")
    next_update_seconds: int = Field(alias="NextUpdateSeconds")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class DescribeMigrationTaskResultModel(BaseModel):
    migration_task: MigrationTaskModel = Field(alias="MigrationTask")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
