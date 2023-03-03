# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class CancelResourceRequestInputRequestModel(BaseModel):
    request_token: str = Field(alias="RequestToken")


class ProgressEventModel(BaseModel):
    type_name: Optional[str] = Field(default=None, alias="TypeName")
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    request_token: Optional[str] = Field(default=None, alias="RequestToken")
    operation: Optional[Literal["CREATE", "DELETE", "UPDATE"]] = Field(
        default=None, alias="Operation"
    )
    operation_status: Optional[
        Literal[
            "CANCEL_COMPLETE",
            "CANCEL_IN_PROGRESS",
            "FAILED",
            "IN_PROGRESS",
            "PENDING",
            "SUCCESS",
        ]
    ] = Field(default=None, alias="OperationStatus")
    event_time: Optional[datetime] = Field(default=None, alias="EventTime")
    resource_model: Optional[str] = Field(default=None, alias="ResourceModel")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    error_code: Optional[
        Literal[
            "AccessDenied",
            "AlreadyExists",
            "GeneralServiceException",
            "InternalFailure",
            "InvalidCredentials",
            "InvalidRequest",
            "NetworkFailure",
            "NotFound",
            "NotStabilized",
            "NotUpdatable",
            "ResourceConflict",
            "ServiceInternalError",
            "ServiceLimitExceeded",
            "ServiceTimeout",
            "Throttling",
        ]
    ] = Field(default=None, alias="ErrorCode")
    retry_after: Optional[datetime] = Field(default=None, alias="RetryAfter")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateResourceInputRequestModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    desired_state: str = Field(alias="DesiredState")
    type_version_id: Optional[str] = Field(default=None, alias="TypeVersionId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class DeleteResourceInputRequestModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    identifier: str = Field(alias="Identifier")
    type_version_id: Optional[str] = Field(default=None, alias="TypeVersionId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class GetResourceInputRequestModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    identifier: str = Field(alias="Identifier")
    type_version_id: Optional[str] = Field(default=None, alias="TypeVersionId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class ResourceDescriptionModel(BaseModel):
    identifier: Optional[str] = Field(default=None, alias="Identifier")
    properties: Optional[str] = Field(default=None, alias="Properties")


class GetResourceRequestStatusInputRequestModel(BaseModel):
    request_token: str = Field(alias="RequestToken")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ResourceRequestStatusFilterModel(BaseModel):
    operations: Optional[Sequence[Literal["CREATE", "DELETE", "UPDATE"]]] = Field(
        default=None, alias="Operations"
    )
    operation_statuses: Optional[
        Sequence[
            Literal[
                "CANCEL_COMPLETE",
                "CANCEL_IN_PROGRESS",
                "FAILED",
                "IN_PROGRESS",
                "PENDING",
                "SUCCESS",
            ]
        ]
    ] = Field(default=None, alias="OperationStatuses")


class ListResourcesInputRequestModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    type_version_id: Optional[str] = Field(default=None, alias="TypeVersionId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    resource_model: Optional[str] = Field(default=None, alias="ResourceModel")


class UpdateResourceInputRequestModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    identifier: str = Field(alias="Identifier")
    patch_document: str = Field(alias="PatchDocument")
    type_version_id: Optional[str] = Field(default=None, alias="TypeVersionId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class CancelResourceRequestOutputModel(BaseModel):
    progress_event: ProgressEventModel = Field(alias="ProgressEvent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateResourceOutputModel(BaseModel):
    progress_event: ProgressEventModel = Field(alias="ProgressEvent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteResourceOutputModel(BaseModel):
    progress_event: ProgressEventModel = Field(alias="ProgressEvent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceRequestStatusOutputModel(BaseModel):
    progress_event: ProgressEventModel = Field(alias="ProgressEvent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceRequestsOutputModel(BaseModel):
    resource_request_status_summaries: List[ProgressEventModel] = Field(
        alias="ResourceRequestStatusSummaries"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateResourceOutputModel(BaseModel):
    progress_event: ProgressEventModel = Field(alias="ProgressEvent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceOutputModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    resource_description: ResourceDescriptionModel = Field(alias="ResourceDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesOutputModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    resource_descriptions: List[ResourceDescriptionModel] = Field(
        alias="ResourceDescriptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceRequestStatusInputResourceRequestSuccessWaitModel(BaseModel):
    request_token: str = Field(alias="RequestToken")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class ListResourcesInputListResourcesPaginateModel(BaseModel):
    type_name: str = Field(alias="TypeName")
    type_version_id: Optional[str] = Field(default=None, alias="TypeVersionId")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")
    resource_model: Optional[str] = Field(default=None, alias="ResourceModel")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceRequestsInputListResourceRequestsPaginateModel(BaseModel):
    resource_request_status_filter: Optional[ResourceRequestStatusFilterModel] = Field(
        default=None, alias="ResourceRequestStatusFilter"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceRequestsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    resource_request_status_filter: Optional[ResourceRequestStatusFilterModel] = Field(
        default=None, alias="ResourceRequestStatusFilter"
    )
