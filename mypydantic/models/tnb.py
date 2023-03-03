# Model Generated: Thu Mar  2 21:56:24 2023

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


class CancelSolNetworkOperationInputRequestModel(BaseModel):
    ns_lcm_op_occ_id: str = Field(alias="nsLcmOpOccId")


class CreateSolFunctionPackageInputRequestModel(BaseModel):
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateSolNetworkInstanceInputRequestModel(BaseModel):
    ns_name: str = Field(alias="nsName")
    nsd_info_id: str = Field(alias="nsdInfoId")
    ns_description: Optional[str] = Field(default=None, alias="nsDescription")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class CreateSolNetworkPackageInputRequestModel(BaseModel):
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class DeleteSolFunctionPackageInputRequestModel(BaseModel):
    vnf_pkg_id: str = Field(alias="vnfPkgId")


class DeleteSolNetworkInstanceInputRequestModel(BaseModel):
    ns_instance_id: str = Field(alias="nsInstanceId")


class DeleteSolNetworkPackageInputRequestModel(BaseModel):
    nsd_info_id: str = Field(alias="nsdInfoId")


class ErrorInfoModel(BaseModel):
    cause: Optional[str] = Field(default=None, alias="cause")
    details: Optional[str] = Field(default=None, alias="details")


class ToscaOverrideModel(BaseModel):
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    name: Optional[str] = Field(default=None, alias="name")


class GetSolFunctionInstanceInputRequestModel(BaseModel):
    vnf_instance_id: str = Field(alias="vnfInstanceId")


class GetSolFunctionInstanceMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class GetSolFunctionPackageContentInputRequestModel(BaseModel):
    accept: Literal["application/zip"] = Field(alias="accept")
    vnf_pkg_id: str = Field(alias="vnfPkgId")


class GetSolFunctionPackageDescriptorInputRequestModel(BaseModel):
    accept: Literal["text/plain"] = Field(alias="accept")
    vnf_pkg_id: str = Field(alias="vnfPkgId")


class GetSolFunctionPackageInputRequestModel(BaseModel):
    vnf_pkg_id: str = Field(alias="vnfPkgId")


class GetSolInstantiatedVnfInfoModel(BaseModel):
    vnf_state: Optional[Literal["STARTED", "STOPPED"]] = Field(
        default=None, alias="vnfState"
    )


class GetSolNetworkInstanceInputRequestModel(BaseModel):
    ns_instance_id: str = Field(alias="nsInstanceId")


class GetSolNetworkInstanceMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class LcmOperationInfoModel(BaseModel):
    ns_lcm_op_occ_id: str = Field(alias="nsLcmOpOccId")


class GetSolNetworkOperationInputRequestModel(BaseModel):
    ns_lcm_op_occ_id: str = Field(alias="nsLcmOpOccId")


class GetSolNetworkOperationMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class ProblemDetailsModel(BaseModel):
    detail: str = Field(alias="detail")
    title: Optional[str] = Field(default=None, alias="title")


class GetSolNetworkPackageContentInputRequestModel(BaseModel):
    accept: Literal["application/zip"] = Field(alias="accept")
    nsd_info_id: str = Field(alias="nsdInfoId")


class GetSolNetworkPackageDescriptorInputRequestModel(BaseModel):
    nsd_info_id: str = Field(alias="nsdInfoId")


class GetSolNetworkPackageInputRequestModel(BaseModel):
    nsd_info_id: str = Field(alias="nsdInfoId")


class GetSolVnfcResourceInfoMetadataModel(BaseModel):
    cluster: Optional[str] = Field(default=None, alias="cluster")
    helm_chart: Optional[str] = Field(default=None, alias="helmChart")
    node_group: Optional[str] = Field(default=None, alias="nodeGroup")


class InstantiateSolNetworkInstanceInputRequestModel(BaseModel):
    ns_instance_id: str = Field(alias="nsInstanceId")
    additional_params_for_ns: Optional[Mapping[str, Any]] = Field(
        default=None, alias="additionalParamsForNs"
    )
    dry_run: Optional[bool] = Field(default=None, alias="dryRun")


class ListSolFunctionInstanceMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListSolFunctionInstancesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSolFunctionPackageMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class ListSolFunctionPackagesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSolNetworkInstanceMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class ListSolNetworkInstancesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSolNetworkOperationsMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class ListSolNetworkOperationsInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSolNetworkPackageMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")


class ListSolNetworkPackagesInputRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class PutSolFunctionPackageContentInputRequestModel(BaseModel):
    file: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="file")
    vnf_pkg_id: str = Field(alias="vnfPkgId")
    content_type: Optional[Literal["application/zip"]] = Field(
        default=None, alias="contentType"
    )


class PutSolNetworkPackageContentInputRequestModel(BaseModel):
    file: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="file")
    nsd_info_id: str = Field(alias="nsdInfoId")
    content_type: Optional[Literal["application/zip"]] = Field(
        default=None, alias="contentType"
    )


class TagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TerminateSolNetworkInstanceInputRequestModel(BaseModel):
    ns_instance_id: str = Field(alias="nsInstanceId")


class UntagResourceInputRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateSolFunctionPackageInputRequestModel(BaseModel):
    operational_state: Literal["DISABLED", "ENABLED"] = Field(alias="operationalState")
    vnf_pkg_id: str = Field(alias="vnfPkgId")


class UpdateSolNetworkModifyModel(BaseModel):
    vnf_configurable_properties: Mapping[str, Any] = Field(
        alias="vnfConfigurableProperties"
    )
    vnf_instance_id: str = Field(alias="vnfInstanceId")


class UpdateSolNetworkPackageInputRequestModel(BaseModel):
    nsd_info_id: str = Field(alias="nsdInfoId")
    nsd_operational_state: Literal["DISABLED", "ENABLED"] = Field(
        alias="nsdOperationalState"
    )


class ValidateSolFunctionPackageContentInputRequestModel(BaseModel):
    file: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="file")
    vnf_pkg_id: str = Field(alias="vnfPkgId")
    content_type: Optional[Literal["application/zip"]] = Field(
        default=None, alias="contentType"
    )


class ValidateSolNetworkPackageContentInputRequestModel(BaseModel):
    file: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="file")
    nsd_info_id: str = Field(alias="nsdInfoId")
    content_type: Optional[Literal["application/zip"]] = Field(
        default=None, alias="contentType"
    )


class CreateSolFunctionPackageOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    onboarding_state: Literal["CREATED", "ERROR", "ONBOARDED"] = Field(
        alias="onboardingState"
    )
    operational_state: Literal["DISABLED", "ENABLED"] = Field(alias="operationalState")
    tags: Dict[str, str] = Field(alias="tags")
    usage_state: Literal["IN_USE", "NOT_IN_USE"] = Field(alias="usageState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSolNetworkInstanceOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    ns_instance_name: str = Field(alias="nsInstanceName")
    nsd_info_id: str = Field(alias="nsdInfoId")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSolNetworkPackageOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    nsd_onboarding_state: Literal["CREATED", "ERROR", "ONBOARDED"] = Field(
        alias="nsdOnboardingState"
    )
    nsd_operational_state: Literal["DISABLED", "ENABLED"] = Field(
        alias="nsdOperationalState"
    )
    nsd_usage_state: Literal["IN_USE", "NOT_IN_USE"] = Field(alias="nsdUsageState")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolFunctionPackageContentOutputModel(BaseModel):
    content_type: Literal["application/zip"] = Field(alias="contentType")
    package_content: Type[StreamingBody] = Field(alias="packageContent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolFunctionPackageDescriptorOutputModel(BaseModel):
    content_type: Literal["text/plain"] = Field(alias="contentType")
    vnfd: Type[StreamingBody] = Field(alias="vnfd")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolNetworkPackageContentOutputModel(BaseModel):
    content_type: Literal["application/zip"] = Field(alias="contentType")
    nsd_content: Type[StreamingBody] = Field(alias="nsdContent")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolNetworkPackageDescriptorOutputModel(BaseModel):
    content_type: Literal["text/plain"] = Field(alias="contentType")
    nsd: Type[StreamingBody] = Field(alias="nsd")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstantiateSolNetworkInstanceOutputModel(BaseModel):
    ns_lcm_op_occ_id: str = Field(alias="nsLcmOpOccId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceOutputModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TerminateSolNetworkInstanceOutputModel(BaseModel):
    ns_lcm_op_occ_id: str = Field(alias="nsLcmOpOccId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSolFunctionPackageOutputModel(BaseModel):
    operational_state: Literal["DISABLED", "ENABLED"] = Field(alias="operationalState")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSolNetworkInstanceOutputModel(BaseModel):
    ns_lcm_op_occ_id: str = Field(alias="nsLcmOpOccId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSolNetworkPackageOutputModel(BaseModel):
    nsd_operational_state: Literal["DISABLED", "ENABLED"] = Field(
        alias="nsdOperationalState"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolNetworkOperationTaskDetailsModel(BaseModel):
    task_context: Optional[Dict[str, str]] = Field(default=None, alias="taskContext")
    task_end_time: Optional[datetime] = Field(default=None, alias="taskEndTime")
    task_error_details: Optional[ErrorInfoModel] = Field(
        default=None, alias="taskErrorDetails"
    )
    task_name: Optional[str] = Field(default=None, alias="taskName")
    task_start_time: Optional[datetime] = Field(default=None, alias="taskStartTime")
    task_status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETED",
            "ERROR",
            "IN_PROGRESS",
            "SCHEDULED",
            "SKIPPED",
            "STARTED",
        ]
    ] = Field(default=None, alias="taskStatus")


class FunctionArtifactMetaModel(BaseModel):
    overrides: Optional[List[ToscaOverrideModel]] = Field(
        default=None, alias="overrides"
    )


class NetworkArtifactMetaModel(BaseModel):
    overrides: Optional[List[ToscaOverrideModel]] = Field(
        default=None, alias="overrides"
    )


class GetSolNetworkInstanceOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    lcm_op_info: LcmOperationInfoModel = Field(alias="lcmOpInfo")
    metadata: GetSolNetworkInstanceMetadataModel = Field(alias="metadata")
    ns_instance_description: str = Field(alias="nsInstanceDescription")
    ns_instance_name: str = Field(alias="nsInstanceName")
    ns_state: Literal[
        "DELETED",
        "IMPAIRED",
        "INSTANTIATED",
        "INSTANTIATE_IN_PROGRESS",
        "NOT_INSTANTIATED",
        "STOPPED",
        "TERMINATE_IN_PROGRESS",
        "UPDATE_IN_PROGRESS",
    ] = Field(alias="nsState")
    nsd_id: str = Field(alias="nsdId")
    nsd_info_id: str = Field(alias="nsdInfoId")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolVnfcResourceInfoModel(BaseModel):
    metadata: Optional[GetSolVnfcResourceInfoMetadataModel] = Field(
        default=None, alias="metadata"
    )


class ListSolFunctionInstanceInfoModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    instantiation_state: Literal["INSTANTIATED", "NOT_INSTANTIATED"] = Field(
        alias="instantiationState"
    )
    metadata: ListSolFunctionInstanceMetadataModel = Field(alias="metadata")
    ns_instance_id: str = Field(alias="nsInstanceId")
    vnf_pkg_id: str = Field(alias="vnfPkgId")
    instantiated_vnf_info: Optional[GetSolInstantiatedVnfInfoModel] = Field(
        default=None, alias="instantiatedVnfInfo"
    )
    vnf_pkg_name: Optional[str] = Field(default=None, alias="vnfPkgName")


class ListSolFunctionInstancesInputListSolFunctionInstancesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSolFunctionPackagesInputListSolFunctionPackagesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSolNetworkInstancesInputListSolNetworkInstancesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSolNetworkOperationsInputListSolNetworkOperationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSolNetworkPackagesInputListSolNetworkPackagesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSolFunctionPackageInfoModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    onboarding_state: Literal["CREATED", "ERROR", "ONBOARDED"] = Field(
        alias="onboardingState"
    )
    operational_state: Literal["DISABLED", "ENABLED"] = Field(alias="operationalState")
    usage_state: Literal["IN_USE", "NOT_IN_USE"] = Field(alias="usageState")
    metadata: Optional[ListSolFunctionPackageMetadataModel] = Field(
        default=None, alias="metadata"
    )
    vnf_product_name: Optional[str] = Field(default=None, alias="vnfProductName")
    vnf_provider: Optional[str] = Field(default=None, alias="vnfProvider")
    vnfd_id: Optional[str] = Field(default=None, alias="vnfdId")
    vnfd_version: Optional[str] = Field(default=None, alias="vnfdVersion")


class ListSolNetworkInstanceInfoModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    metadata: ListSolNetworkInstanceMetadataModel = Field(alias="metadata")
    ns_instance_description: str = Field(alias="nsInstanceDescription")
    ns_instance_name: str = Field(alias="nsInstanceName")
    ns_state: Literal[
        "DELETED",
        "IMPAIRED",
        "INSTANTIATED",
        "INSTANTIATE_IN_PROGRESS",
        "NOT_INSTANTIATED",
        "STOPPED",
        "TERMINATE_IN_PROGRESS",
        "UPDATE_IN_PROGRESS",
    ] = Field(alias="nsState")
    nsd_id: str = Field(alias="nsdId")
    nsd_info_id: str = Field(alias="nsdInfoId")


class ListSolNetworkOperationsInfoModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    lcm_operation_type: Literal["INSTANTIATE", "TERMINATE", "UPDATE"] = Field(
        alias="lcmOperationType"
    )
    ns_instance_id: str = Field(alias="nsInstanceId")
    operation_state: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "PROCESSING"
    ] = Field(alias="operationState")
    error: Optional[ProblemDetailsModel] = Field(default=None, alias="error")
    metadata: Optional[ListSolNetworkOperationsMetadataModel] = Field(
        default=None, alias="metadata"
    )


class ListSolNetworkPackageInfoModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    metadata: ListSolNetworkPackageMetadataModel = Field(alias="metadata")
    nsd_onboarding_state: Literal["CREATED", "ERROR", "ONBOARDED"] = Field(
        alias="nsdOnboardingState"
    )
    nsd_operational_state: Literal["DISABLED", "ENABLED"] = Field(
        alias="nsdOperationalState"
    )
    nsd_usage_state: Literal["IN_USE", "NOT_IN_USE"] = Field(alias="nsdUsageState")
    nsd_designer: Optional[str] = Field(default=None, alias="nsdDesigner")
    nsd_id: Optional[str] = Field(default=None, alias="nsdId")
    nsd_invariant_id: Optional[str] = Field(default=None, alias="nsdInvariantId")
    nsd_name: Optional[str] = Field(default=None, alias="nsdName")
    nsd_version: Optional[str] = Field(default=None, alias="nsdVersion")
    vnf_pkg_ids: Optional[List[str]] = Field(default=None, alias="vnfPkgIds")


class UpdateSolNetworkInstanceInputRequestModel(BaseModel):
    ns_instance_id: str = Field(alias="nsInstanceId")
    update_type: Literal["MODIFY_VNF_INFORMATION"] = Field(alias="updateType")
    modify_vnf_info_data: Optional[UpdateSolNetworkModifyModel] = Field(
        default=None, alias="modifyVnfInfoData"
    )


class GetSolNetworkOperationOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    error: ProblemDetailsModel = Field(alias="error")
    id: str = Field(alias="id")
    lcm_operation_type: Literal["INSTANTIATE", "TERMINATE", "UPDATE"] = Field(
        alias="lcmOperationType"
    )
    metadata: GetSolNetworkOperationMetadataModel = Field(alias="metadata")
    ns_instance_id: str = Field(alias="nsInstanceId")
    operation_state: Literal[
        "CANCELLED", "CANCELLING", "COMPLETED", "FAILED", "PROCESSING"
    ] = Field(alias="operationState")
    tags: Dict[str, str] = Field(alias="tags")
    tasks: List[GetSolNetworkOperationTaskDetailsModel] = Field(alias="tasks")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolFunctionPackageMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")
    vnfd: Optional[FunctionArtifactMetaModel] = Field(default=None, alias="vnfd")


class PutSolFunctionPackageContentMetadataModel(BaseModel):
    vnfd: Optional[FunctionArtifactMetaModel] = Field(default=None, alias="vnfd")


class ValidateSolFunctionPackageContentMetadataModel(BaseModel):
    vnfd: Optional[FunctionArtifactMetaModel] = Field(default=None, alias="vnfd")


class GetSolNetworkPackageMetadataModel(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    last_modified: datetime = Field(alias="lastModified")
    nsd: Optional[NetworkArtifactMetaModel] = Field(default=None, alias="nsd")


class PutSolNetworkPackageContentMetadataModel(BaseModel):
    nsd: Optional[NetworkArtifactMetaModel] = Field(default=None, alias="nsd")


class ValidateSolNetworkPackageContentMetadataModel(BaseModel):
    nsd: Optional[NetworkArtifactMetaModel] = Field(default=None, alias="nsd")


class GetSolVnfInfoModel(BaseModel):
    vnf_state: Optional[Literal["STARTED", "STOPPED"]] = Field(
        default=None, alias="vnfState"
    )
    vnfc_resource_info: Optional[List[GetSolVnfcResourceInfoModel]] = Field(
        default=None, alias="vnfcResourceInfo"
    )


class ListSolFunctionInstancesOutputModel(BaseModel):
    function_instances: List[ListSolFunctionInstanceInfoModel] = Field(
        alias="functionInstances"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSolFunctionPackagesOutputModel(BaseModel):
    function_packages: List[ListSolFunctionPackageInfoModel] = Field(
        alias="functionPackages"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSolNetworkInstancesOutputModel(BaseModel):
    network_instances: List[ListSolNetworkInstanceInfoModel] = Field(
        alias="networkInstances"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSolNetworkOperationsOutputModel(BaseModel):
    network_operations: List[ListSolNetworkOperationsInfoModel] = Field(
        alias="networkOperations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSolNetworkPackagesOutputModel(BaseModel):
    network_packages: List[ListSolNetworkPackageInfoModel] = Field(
        alias="networkPackages"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolFunctionPackageOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    metadata: GetSolFunctionPackageMetadataModel = Field(alias="metadata")
    onboarding_state: Literal["CREATED", "ERROR", "ONBOARDED"] = Field(
        alias="onboardingState"
    )
    operational_state: Literal["DISABLED", "ENABLED"] = Field(alias="operationalState")
    tags: Dict[str, str] = Field(alias="tags")
    usage_state: Literal["IN_USE", "NOT_IN_USE"] = Field(alias="usageState")
    vnf_product_name: str = Field(alias="vnfProductName")
    vnf_provider: str = Field(alias="vnfProvider")
    vnfd_id: str = Field(alias="vnfdId")
    vnfd_version: str = Field(alias="vnfdVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSolFunctionPackageContentOutputModel(BaseModel):
    id: str = Field(alias="id")
    metadata: PutSolFunctionPackageContentMetadataModel = Field(alias="metadata")
    vnf_product_name: str = Field(alias="vnfProductName")
    vnf_provider: str = Field(alias="vnfProvider")
    vnfd_id: str = Field(alias="vnfdId")
    vnfd_version: str = Field(alias="vnfdVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidateSolFunctionPackageContentOutputModel(BaseModel):
    id: str = Field(alias="id")
    metadata: ValidateSolFunctionPackageContentMetadataModel = Field(alias="metadata")
    vnf_product_name: str = Field(alias="vnfProductName")
    vnf_provider: str = Field(alias="vnfProvider")
    vnfd_id: str = Field(alias="vnfdId")
    vnfd_version: str = Field(alias="vnfdVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolNetworkPackageOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    metadata: GetSolNetworkPackageMetadataModel = Field(alias="metadata")
    nsd_id: str = Field(alias="nsdId")
    nsd_name: str = Field(alias="nsdName")
    nsd_onboarding_state: Literal["CREATED", "ERROR", "ONBOARDED"] = Field(
        alias="nsdOnboardingState"
    )
    nsd_operational_state: Literal["DISABLED", "ENABLED"] = Field(
        alias="nsdOperationalState"
    )
    nsd_usage_state: Literal["IN_USE", "NOT_IN_USE"] = Field(alias="nsdUsageState")
    nsd_version: str = Field(alias="nsdVersion")
    tags: Dict[str, str] = Field(alias="tags")
    vnf_pkg_ids: List[str] = Field(alias="vnfPkgIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSolNetworkPackageContentOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    metadata: PutSolNetworkPackageContentMetadataModel = Field(alias="metadata")
    nsd_id: str = Field(alias="nsdId")
    nsd_name: str = Field(alias="nsdName")
    nsd_version: str = Field(alias="nsdVersion")
    vnf_pkg_ids: List[str] = Field(alias="vnfPkgIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidateSolNetworkPackageContentOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    metadata: ValidateSolNetworkPackageContentMetadataModel = Field(alias="metadata")
    nsd_id: str = Field(alias="nsdId")
    nsd_name: str = Field(alias="nsdName")
    nsd_version: str = Field(alias="nsdVersion")
    vnf_pkg_ids: List[str] = Field(alias="vnfPkgIds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSolFunctionInstanceOutputModel(BaseModel):
    arn: str = Field(alias="arn")
    id: str = Field(alias="id")
    instantiated_vnf_info: GetSolVnfInfoModel = Field(alias="instantiatedVnfInfo")
    instantiation_state: Literal["INSTANTIATED", "NOT_INSTANTIATED"] = Field(
        alias="instantiationState"
    )
    metadata: GetSolFunctionInstanceMetadataModel = Field(alias="metadata")
    ns_instance_id: str = Field(alias="nsInstanceId")
    tags: Dict[str, str] = Field(alias="tags")
    vnf_pkg_id: str = Field(alias="vnfPkgId")
    vnf_product_name: str = Field(alias="vnfProductName")
    vnf_provider: str = Field(alias="vnfProvider")
    vnfd_id: str = Field(alias="vnfdId")
    vnfd_version: str = Field(alias="vnfdVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
