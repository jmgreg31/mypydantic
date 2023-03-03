# Model Generated: Thu Mar  2 21:56:20 2023

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


class ActuatorModel(BaseModel):
    fully_qualified_name: str = Field(alias="fullyQualifiedName")
    data_type: Literal[
        "BOOLEAN",
        "BOOLEAN_ARRAY",
        "DOUBLE",
        "DOUBLE_ARRAY",
        "FLOAT",
        "FLOAT_ARRAY",
        "INT16",
        "INT16_ARRAY",
        "INT32",
        "INT32_ARRAY",
        "INT64",
        "INT64_ARRAY",
        "INT8",
        "INT8_ARRAY",
        "STRING",
        "STRING_ARRAY",
        "UINT16",
        "UINT16_ARRAY",
        "UINT32",
        "UINT32_ARRAY",
        "UINT64",
        "UINT64_ARRAY",
        "UINT8",
        "UINT8_ARRAY",
        "UNIX_TIMESTAMP",
        "UNIX_TIMESTAMP_ARRAY",
        "UNKNOWN",
    ] = Field(alias="dataType")
    description: Optional[str] = Field(default=None, alias="description")
    unit: Optional[str] = Field(default=None, alias="unit")
    allowed_values: Optional[Sequence[str]] = Field(default=None, alias="allowedValues")
    min: Optional[float] = Field(default=None, alias="min")
    max: Optional[float] = Field(default=None, alias="max")
    assigned_value: Optional[str] = Field(default=None, alias="assignedValue")


class AssociateVehicleFleetRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    fleet_id: str = Field(alias="fleetId")


class AttributeModel(BaseModel):
    fully_qualified_name: str = Field(alias="fullyQualifiedName")
    data_type: Literal[
        "BOOLEAN",
        "BOOLEAN_ARRAY",
        "DOUBLE",
        "DOUBLE_ARRAY",
        "FLOAT",
        "FLOAT_ARRAY",
        "INT16",
        "INT16_ARRAY",
        "INT32",
        "INT32_ARRAY",
        "INT64",
        "INT64_ARRAY",
        "INT8",
        "INT8_ARRAY",
        "STRING",
        "STRING_ARRAY",
        "UINT16",
        "UINT16_ARRAY",
        "UINT32",
        "UINT32_ARRAY",
        "UINT64",
        "UINT64_ARRAY",
        "UINT8",
        "UINT8_ARRAY",
        "UNIX_TIMESTAMP",
        "UNIX_TIMESTAMP_ARRAY",
        "UNKNOWN",
    ] = Field(alias="dataType")
    description: Optional[str] = Field(default=None, alias="description")
    unit: Optional[str] = Field(default=None, alias="unit")
    allowed_values: Optional[Sequence[str]] = Field(default=None, alias="allowedValues")
    min: Optional[float] = Field(default=None, alias="min")
    max: Optional[float] = Field(default=None, alias="max")
    assigned_value: Optional[str] = Field(default=None, alias="assignedValue")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")


class CreateVehicleErrorModel(BaseModel):
    vehicle_name: Optional[str] = Field(default=None, alias="vehicleName")
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class CreateVehicleResponseItemModel(BaseModel):
    vehicle_name: Optional[str] = Field(default=None, alias="vehicleName")
    arn: Optional[str] = Field(default=None, alias="arn")
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class UpdateVehicleRequestItemModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    model_manifest_arn: Optional[str] = Field(default=None, alias="modelManifestArn")
    decoder_manifest_arn: Optional[str] = Field(
        default=None, alias="decoderManifestArn"
    )
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")
    attribute_update_mode: Optional[Literal["Merge", "Overwrite"]] = Field(
        default=None, alias="attributeUpdateMode"
    )


class UpdateVehicleErrorModel(BaseModel):
    vehicle_name: Optional[str] = Field(default=None, alias="vehicleName")
    code: Optional[int] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class UpdateVehicleResponseItemModel(BaseModel):
    vehicle_name: Optional[str] = Field(default=None, alias="vehicleName")
    arn: Optional[str] = Field(default=None, alias="arn")


class BranchModel(BaseModel):
    fully_qualified_name: str = Field(alias="fullyQualifiedName")
    description: Optional[str] = Field(default=None, alias="description")


class CampaignSummaryModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    signal_catalog_arn: Optional[str] = Field(default=None, alias="signalCatalogArn")
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    status: Optional[
        Literal["CREATING", "RUNNING", "SUSPENDED", "WAITING_FOR_APPROVAL"]
    ] = Field(default=None, alias="status")


class CanDbcDefinitionModel(BaseModel):
    network_interface: str = Field(alias="networkInterface")
    can_dbc_files: Sequence[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(alias="canDbcFiles")
    signals_map: Optional[Mapping[str, str]] = Field(default=None, alias="signalsMap")


class CanInterfaceModel(BaseModel):
    name: str = Field(alias="name")
    protocol_name: Optional[str] = Field(default=None, alias="protocolName")
    protocol_version: Optional[str] = Field(default=None, alias="protocolVersion")


class CanSignalModel(BaseModel):
    message_id: int = Field(alias="messageId")
    is_big_endian: bool = Field(alias="isBigEndian")
    is_signed: bool = Field(alias="isSigned")
    start_bit: int = Field(alias="startBit")
    offset: float = Field(alias="offset")
    factor: float = Field(alias="factor")
    length: int = Field(alias="length")
    name: Optional[str] = Field(default=None, alias="name")


class CloudWatchLogDeliveryOptionsModel(BaseModel):
    log_type: Literal["ERROR", "OFF"] = Field(alias="logType")
    log_group_name: Optional[str] = Field(default=None, alias="logGroupName")


class ConditionBasedCollectionSchemeModel(BaseModel):
    expression: str = Field(alias="expression")
    minimum_trigger_interval_ms: Optional[int] = Field(
        default=None, alias="minimumTriggerIntervalMs"
    )
    trigger_mode: Optional[Literal["ALWAYS", "RISING_EDGE"]] = Field(
        default=None, alias="triggerMode"
    )
    condition_language_version: Optional[int] = Field(
        default=None, alias="conditionLanguageVersion"
    )


class TimeBasedCollectionSchemeModel(BaseModel):
    period_ms: int = Field(alias="periodMs")


class SignalInformationModel(BaseModel):
    name: str = Field(alias="name")
    max_sample_count: Optional[int] = Field(default=None, alias="maxSampleCount")
    minimum_sampling_interval_ms: Optional[int] = Field(
        default=None, alias="minimumSamplingIntervalMs"
    )


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class DecoderManifestSummaryModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    model_manifest_arn: Optional[str] = Field(default=None, alias="modelManifestArn")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[Literal["ACTIVE", "DRAFT"]] = Field(default=None, alias="status")


class DeleteCampaignRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteDecoderManifestRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteFleetRequestModel(BaseModel):
    fleet_id: str = Field(alias="fleetId")


class DeleteModelManifestRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteSignalCatalogRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteVehicleRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")


class DisassociateVehicleFleetRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    fleet_id: str = Field(alias="fleetId")


class FleetSummaryModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    signal_catalog_arn: str = Field(alias="signalCatalogArn")
    creation_time: datetime = Field(alias="creationTime")
    description: Optional[str] = Field(default=None, alias="description")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="lastModificationTime"
    )


class FormattedVssModel(BaseModel):
    vss_json: Optional[str] = Field(default=None, alias="vssJson")


class GetCampaignRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetDecoderManifestRequestModel(BaseModel):
    name: str = Field(alias="name")


class GetFleetRequestModel(BaseModel):
    fleet_id: str = Field(alias="fleetId")


class GetModelManifestRequestModel(BaseModel):
    name: str = Field(alias="name")


class IamRegistrationResponseModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    registration_status: Literal[
        "REGISTRATION_FAILURE", "REGISTRATION_PENDING", "REGISTRATION_SUCCESS"
    ] = Field(alias="registrationStatus")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class TimestreamRegistrationResponseModel(BaseModel):
    timestream_database_name: str = Field(alias="timestreamDatabaseName")
    timestream_table_name: str = Field(alias="timestreamTableName")
    registration_status: Literal[
        "REGISTRATION_FAILURE", "REGISTRATION_PENDING", "REGISTRATION_SUCCESS"
    ] = Field(alias="registrationStatus")
    timestream_database_arn: Optional[str] = Field(
        default=None, alias="timestreamDatabaseArn"
    )
    timestream_table_arn: Optional[str] = Field(
        default=None, alias="timestreamTableArn"
    )
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class GetSignalCatalogRequestModel(BaseModel):
    name: str = Field(alias="name")


class NodeCountsModel(BaseModel):
    total_nodes: Optional[int] = Field(default=None, alias="totalNodes")
    total_branches: Optional[int] = Field(default=None, alias="totalBranches")
    total_sensors: Optional[int] = Field(default=None, alias="totalSensors")
    total_attributes: Optional[int] = Field(default=None, alias="totalAttributes")
    total_actuators: Optional[int] = Field(default=None, alias="totalActuators")


class GetVehicleRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetVehicleStatusRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class VehicleStatusModel(BaseModel):
    campaign_name: Optional[str] = Field(default=None, alias="campaignName")
    vehicle_name: Optional[str] = Field(default=None, alias="vehicleName")
    status: Optional[
        Literal["CREATED", "DELETING", "HEALTHY", "READY", "SUSPENDED"]
    ] = Field(default=None, alias="status")


class IamResourcesModel(BaseModel):
    role_arn: str = Field(alias="roleArn")


class ListCampaignsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    status: Optional[str] = Field(default=None, alias="status")


class ListDecoderManifestNetworkInterfacesRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDecoderManifestSignalsRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDecoderManifestsRequestModel(BaseModel):
    model_manifest_arn: Optional[str] = Field(default=None, alias="modelManifestArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListFleetsForVehicleRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListFleetsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListModelManifestNodesRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListModelManifestsRequestModel(BaseModel):
    signal_catalog_arn: Optional[str] = Field(default=None, alias="signalCatalogArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ModelManifestSummaryModel(BaseModel):
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    signal_catalog_arn: Optional[str] = Field(default=None, alias="signalCatalogArn")
    description: Optional[str] = Field(default=None, alias="description")
    status: Optional[Literal["ACTIVE", "DRAFT"]] = Field(default=None, alias="status")


class ListSignalCatalogNodesRequestModel(BaseModel):
    name: str = Field(alias="name")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListSignalCatalogsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SignalCatalogSummaryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    last_modification_time: Optional[datetime] = Field(
        default=None, alias="lastModificationTime"
    )


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class ListVehiclesInFleetRequestModel(BaseModel):
    fleet_id: str = Field(alias="fleetId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListVehiclesRequestModel(BaseModel):
    model_manifest_arn: Optional[str] = Field(default=None, alias="modelManifestArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class VehicleSummaryModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    arn: str = Field(alias="arn")
    model_manifest_arn: str = Field(alias="modelManifestArn")
    decoder_manifest_arn: str = Field(alias="decoderManifestArn")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")


class ObdInterfaceModel(BaseModel):
    name: str = Field(alias="name")
    request_message_id: int = Field(alias="requestMessageId")
    obd_standard: Optional[str] = Field(default=None, alias="obdStandard")
    pid_request_interval_seconds: Optional[int] = Field(
        default=None, alias="pidRequestIntervalSeconds"
    )
    dtc_request_interval_seconds: Optional[int] = Field(
        default=None, alias="dtcRequestIntervalSeconds"
    )
    use_extended_ids: Optional[bool] = Field(default=None, alias="useExtendedIds")
    has_transmission_ecu: Optional[bool] = Field(
        default=None, alias="hasTransmissionEcu"
    )


class SensorModel(BaseModel):
    fully_qualified_name: str = Field(alias="fullyQualifiedName")
    data_type: Literal[
        "BOOLEAN",
        "BOOLEAN_ARRAY",
        "DOUBLE",
        "DOUBLE_ARRAY",
        "FLOAT",
        "FLOAT_ARRAY",
        "INT16",
        "INT16_ARRAY",
        "INT32",
        "INT32_ARRAY",
        "INT64",
        "INT64_ARRAY",
        "INT8",
        "INT8_ARRAY",
        "STRING",
        "STRING_ARRAY",
        "UINT16",
        "UINT16_ARRAY",
        "UINT32",
        "UINT32_ARRAY",
        "UINT64",
        "UINT64_ARRAY",
        "UINT8",
        "UINT8_ARRAY",
        "UNIX_TIMESTAMP",
        "UNIX_TIMESTAMP_ARRAY",
        "UNKNOWN",
    ] = Field(alias="dataType")
    description: Optional[str] = Field(default=None, alias="description")
    unit: Optional[str] = Field(default=None, alias="unit")
    allowed_values: Optional[Sequence[str]] = Field(default=None, alias="allowedValues")
    min: Optional[float] = Field(default=None, alias="min")
    max: Optional[float] = Field(default=None, alias="max")


class ObdSignalModel(BaseModel):
    pid_response_length: int = Field(alias="pidResponseLength")
    service_mode: int = Field(alias="serviceMode")
    pid: int = Field(alias="pid")
    scaling: float = Field(alias="scaling")
    offset: float = Field(alias="offset")
    start_byte: int = Field(alias="startByte")
    byte_length: int = Field(alias="byteLength")
    bit_right_shift: Optional[int] = Field(default=None, alias="bitRightShift")
    bit_mask_length: Optional[int] = Field(default=None, alias="bitMaskLength")


class TimestreamResourcesModel(BaseModel):
    timestream_database_name: str = Field(alias="timestreamDatabaseName")
    timestream_table_name: str = Field(alias="timestreamTableName")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateCampaignRequestModel(BaseModel):
    name: str = Field(alias="name")
    action: Literal["APPROVE", "RESUME", "SUSPEND", "UPDATE"] = Field(alias="action")
    description: Optional[str] = Field(default=None, alias="description")
    data_extra_dimensions: Optional[Sequence[str]] = Field(
        default=None, alias="dataExtraDimensions"
    )


class UpdateFleetRequestModel(BaseModel):
    fleet_id: str = Field(alias="fleetId")
    description: Optional[str] = Field(default=None, alias="description")


class UpdateModelManifestRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    nodes_to_add: Optional[Sequence[str]] = Field(default=None, alias="nodesToAdd")
    nodes_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="nodesToRemove"
    )
    status: Optional[Literal["ACTIVE", "DRAFT"]] = Field(default=None, alias="status")


class UpdateVehicleRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    model_manifest_arn: Optional[str] = Field(default=None, alias="modelManifestArn")
    decoder_manifest_arn: Optional[str] = Field(
        default=None, alias="decoderManifestArn"
    )
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")
    attribute_update_mode: Optional[Literal["Merge", "Overwrite"]] = Field(
        default=None, alias="attributeUpdateMode"
    )


class BatchCreateVehicleResponseModel(BaseModel):
    vehicles: List[CreateVehicleResponseItemModel] = Field(alias="vehicles")
    errors: List[CreateVehicleErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCampaignResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDecoderManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFleetResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateModelManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSignalCatalogResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVehicleResponseModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    arn: str = Field(alias="arn")
    thing_arn: str = Field(alias="thingArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCampaignResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDecoderManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFleetResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteModelManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSignalCatalogResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteVehicleResponseModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDecoderManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    model_manifest_arn: str = Field(alias="modelManifestArn")
    status: Literal["ACTIVE", "DRAFT"] = Field(alias="status")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFleetResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    signal_catalog_arn: str = Field(alias="signalCatalogArn")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetModelManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    signal_catalog_arn: str = Field(alias="signalCatalogArn")
    status: Literal["ACTIVE", "DRAFT"] = Field(alias="status")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVehicleResponseModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    arn: str = Field(alias="arn")
    model_manifest_arn: str = Field(alias="modelManifestArn")
    decoder_manifest_arn: str = Field(alias="decoderManifestArn")
    attributes: Dict[str, str] = Field(alias="attributes")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportDecoderManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportSignalCatalogResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFleetsForVehicleResponseModel(BaseModel):
    fleets: List[str] = Field(alias="fleets")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVehiclesInFleetResponseModel(BaseModel):
    vehicles: List[str] = Field(alias="vehicles")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCampaignResponseModel(BaseModel):
    arn: str = Field(alias="arn")
    name: str = Field(alias="name")
    status: Literal["CREATING", "RUNNING", "SUSPENDED", "WAITING_FOR_APPROVAL"] = Field(
        alias="status"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDecoderManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFleetResponseModel(BaseModel):
    id: str = Field(alias="id")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateModelManifestResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSignalCatalogResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVehicleResponseModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateVehicleRequestModel(BaseModel):
    vehicles: Sequence[UpdateVehicleRequestItemModel] = Field(alias="vehicles")


class BatchUpdateVehicleResponseModel(BaseModel):
    vehicles: List[UpdateVehicleResponseItemModel] = Field(alias="vehicles")
    errors: List[UpdateVehicleErrorModel] = Field(alias="errors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCampaignsResponseModel(BaseModel):
    campaign_summaries: List[CampaignSummaryModel] = Field(alias="campaignSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkFileDefinitionModel(BaseModel):
    can_dbc: Optional[CanDbcDefinitionModel] = Field(default=None, alias="canDbc")


class GetLoggingOptionsResponseModel(BaseModel):
    cloud_watch_log_delivery: CloudWatchLogDeliveryOptionsModel = Field(
        alias="cloudWatchLogDelivery"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLoggingOptionsRequestModel(BaseModel):
    cloud_watch_log_delivery: CloudWatchLogDeliveryOptionsModel = Field(
        alias="cloudWatchLogDelivery"
    )


class CollectionSchemeModel(BaseModel):
    time_based_collection_scheme: Optional[TimeBasedCollectionSchemeModel] = Field(
        default=None, alias="timeBasedCollectionScheme"
    )
    condition_based_collection_scheme: Optional[
        ConditionBasedCollectionSchemeModel
    ] = Field(default=None, alias="conditionBasedCollectionScheme")


class CreateFleetRequestModel(BaseModel):
    fleet_id: str = Field(alias="fleetId")
    signal_catalog_arn: str = Field(alias="signalCatalogArn")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateModelManifestRequestModel(BaseModel):
    name: str = Field(alias="name")
    nodes: Sequence[str] = Field(alias="nodes")
    signal_catalog_arn: str = Field(alias="signalCatalogArn")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateVehicleRequestItemModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    model_manifest_arn: str = Field(alias="modelManifestArn")
    decoder_manifest_arn: str = Field(alias="decoderManifestArn")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")
    association_behavior: Optional[
        Literal["CreateIotThing", "ValidateIotThingExists"]
    ] = Field(default=None, alias="associationBehavior")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateVehicleRequestModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    model_manifest_arn: str = Field(alias="modelManifestArn")
    decoder_manifest_arn: str = Field(alias="decoderManifestArn")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")
    association_behavior: Optional[
        Literal["CreateIotThing", "ValidateIotThingExists"]
    ] = Field(default=None, alias="associationBehavior")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListDecoderManifestsResponseModel(BaseModel):
    summaries: List[DecoderManifestSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFleetsResponseModel(BaseModel):
    fleet_summaries: List[FleetSummaryModel] = Field(alias="fleetSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportSignalCatalogRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    vss: Optional[FormattedVssModel] = Field(default=None, alias="vss")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class GetRegisterAccountStatusResponseModel(BaseModel):
    customer_account_id: str = Field(alias="customerAccountId")
    account_status: Literal[
        "REGISTRATION_FAILURE", "REGISTRATION_PENDING", "REGISTRATION_SUCCESS"
    ] = Field(alias="accountStatus")
    timestream_registration_response: TimestreamRegistrationResponseModel = Field(
        alias="timestreamRegistrationResponse"
    )
    iam_registration_response: IamRegistrationResponseModel = Field(
        alias="iamRegistrationResponse"
    )
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSignalCatalogResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    node_counts: NodeCountsModel = Field(alias="nodeCounts")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVehicleStatusRequestGetVehicleStatusPaginateModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCampaignsRequestListCampaignsPaginateModel(BaseModel):
    status: Optional[str] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateModel(
    BaseModel
):
    name: str = Field(alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateModel(
    BaseModel
):
    name: str = Field(alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDecoderManifestsRequestListDecoderManifestsPaginateModel(BaseModel):
    model_manifest_arn: Optional[str] = Field(default=None, alias="modelManifestArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFleetsForVehicleRequestListFleetsForVehiclePaginateModel(BaseModel):
    vehicle_name: str = Field(alias="vehicleName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFleetsRequestListFleetsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelManifestNodesRequestListModelManifestNodesPaginateModel(BaseModel):
    name: str = Field(alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListModelManifestsRequestListModelManifestsPaginateModel(BaseModel):
    signal_catalog_arn: Optional[str] = Field(default=None, alias="signalCatalogArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateModel(BaseModel):
    name: str = Field(alias="name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSignalCatalogsRequestListSignalCatalogsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVehiclesInFleetRequestListVehiclesInFleetPaginateModel(BaseModel):
    fleet_id: str = Field(alias="fleetId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVehiclesRequestListVehiclesPaginateModel(BaseModel):
    model_manifest_arn: Optional[str] = Field(default=None, alias="modelManifestArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetVehicleStatusResponseModel(BaseModel):
    campaigns: List[VehicleStatusModel] = Field(alias="campaigns")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListModelManifestsResponseModel(BaseModel):
    summaries: List[ModelManifestSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSignalCatalogsResponseModel(BaseModel):
    summaries: List[SignalCatalogSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVehiclesResponseModel(BaseModel):
    vehicle_summaries: List[VehicleSummaryModel] = Field(alias="vehicleSummaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NetworkInterfaceModel(BaseModel):
    interface_id: str = Field(alias="interfaceId")
    type: Literal["CAN_INTERFACE", "OBD_INTERFACE"] = Field(alias="type")
    can_interface: Optional[CanInterfaceModel] = Field(
        default=None, alias="canInterface"
    )
    obd_interface: Optional[ObdInterfaceModel] = Field(
        default=None, alias="obdInterface"
    )


class NodeModel(BaseModel):
    branch: Optional[BranchModel] = Field(default=None, alias="branch")
    sensor: Optional[SensorModel] = Field(default=None, alias="sensor")
    actuator: Optional[ActuatorModel] = Field(default=None, alias="actuator")
    attribute: Optional[AttributeModel] = Field(default=None, alias="attribute")


class SignalDecoderModel(BaseModel):
    fully_qualified_name: str = Field(alias="fullyQualifiedName")
    type: Literal["CAN_SIGNAL", "OBD_SIGNAL"] = Field(alias="type")
    interface_id: str = Field(alias="interfaceId")
    can_signal: Optional[CanSignalModel] = Field(default=None, alias="canSignal")
    obd_signal: Optional[ObdSignalModel] = Field(default=None, alias="obdSignal")


class RegisterAccountRequestModel(BaseModel):
    timestream_resources: TimestreamResourcesModel = Field(alias="timestreamResources")
    iam_resources: Optional[IamResourcesModel] = Field(
        default=None, alias="iamResources"
    )


class RegisterAccountResponseModel(BaseModel):
    register_account_status: Literal[
        "REGISTRATION_FAILURE", "REGISTRATION_PENDING", "REGISTRATION_SUCCESS"
    ] = Field(alias="registerAccountStatus")
    timestream_resources: TimestreamResourcesModel = Field(alias="timestreamResources")
    iam_resources: IamResourcesModel = Field(alias="iamResources")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportDecoderManifestRequestModel(BaseModel):
    name: str = Field(alias="name")
    network_file_definitions: Sequence[NetworkFileDefinitionModel] = Field(
        alias="networkFileDefinitions"
    )


class CreateCampaignRequestModel(BaseModel):
    name: str = Field(alias="name")
    signal_catalog_arn: str = Field(alias="signalCatalogArn")
    target_arn: str = Field(alias="targetArn")
    collection_scheme: CollectionSchemeModel = Field(alias="collectionScheme")
    description: Optional[str] = Field(default=None, alias="description")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    expiry_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="expiryTime"
    )
    post_trigger_collection_duration: Optional[int] = Field(
        default=None, alias="postTriggerCollectionDuration"
    )
    diagnostics_mode: Optional[Literal["OFF", "SEND_ACTIVE_DTCS"]] = Field(
        default=None, alias="diagnosticsMode"
    )
    spooling_mode: Optional[Literal["OFF", "TO_DISK"]] = Field(
        default=None, alias="spoolingMode"
    )
    compression: Optional[Literal["OFF", "SNAPPY"]] = Field(
        default=None, alias="compression"
    )
    priority: Optional[int] = Field(default=None, alias="priority")
    signals_to_collect: Optional[Sequence[SignalInformationModel]] = Field(
        default=None, alias="signalsToCollect"
    )
    data_extra_dimensions: Optional[Sequence[str]] = Field(
        default=None, alias="dataExtraDimensions"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class GetCampaignResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    description: str = Field(alias="description")
    signal_catalog_arn: str = Field(alias="signalCatalogArn")
    target_arn: str = Field(alias="targetArn")
    status: Literal["CREATING", "RUNNING", "SUSPENDED", "WAITING_FOR_APPROVAL"] = Field(
        alias="status"
    )
    start_time: datetime = Field(alias="startTime")
    expiry_time: datetime = Field(alias="expiryTime")
    post_trigger_collection_duration: int = Field(alias="postTriggerCollectionDuration")
    diagnostics_mode: Literal["OFF", "SEND_ACTIVE_DTCS"] = Field(
        alias="diagnosticsMode"
    )
    spooling_mode: Literal["OFF", "TO_DISK"] = Field(alias="spoolingMode")
    compression: Literal["OFF", "SNAPPY"] = Field(alias="compression")
    priority: int = Field(alias="priority")
    signals_to_collect: List[SignalInformationModel] = Field(alias="signalsToCollect")
    collection_scheme: CollectionSchemeModel = Field(alias="collectionScheme")
    data_extra_dimensions: List[str] = Field(alias="dataExtraDimensions")
    creation_time: datetime = Field(alias="creationTime")
    last_modification_time: datetime = Field(alias="lastModificationTime")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateVehicleRequestModel(BaseModel):
    vehicles: Sequence[CreateVehicleRequestItemModel] = Field(alias="vehicles")


class ListDecoderManifestNetworkInterfacesResponseModel(BaseModel):
    network_interfaces: List[NetworkInterfaceModel] = Field(alias="networkInterfaces")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSignalCatalogRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    nodes: Optional[Sequence[NodeModel]] = Field(default=None, alias="nodes")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListModelManifestNodesResponseModel(BaseModel):
    nodes: List[NodeModel] = Field(alias="nodes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSignalCatalogNodesResponseModel(BaseModel):
    nodes: List[NodeModel] = Field(alias="nodes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSignalCatalogRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    nodes_to_add: Optional[Sequence[NodeModel]] = Field(
        default=None, alias="nodesToAdd"
    )
    nodes_to_update: Optional[Sequence[NodeModel]] = Field(
        default=None, alias="nodesToUpdate"
    )
    nodes_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="nodesToRemove"
    )


class CreateDecoderManifestRequestModel(BaseModel):
    name: str = Field(alias="name")
    model_manifest_arn: str = Field(alias="modelManifestArn")
    description: Optional[str] = Field(default=None, alias="description")
    signal_decoders: Optional[Sequence[SignalDecoderModel]] = Field(
        default=None, alias="signalDecoders"
    )
    network_interfaces: Optional[Sequence[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfaces"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListDecoderManifestSignalsResponseModel(BaseModel):
    signal_decoders: List[SignalDecoderModel] = Field(alias="signalDecoders")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDecoderManifestRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    signal_decoders_to_add: Optional[Sequence[SignalDecoderModel]] = Field(
        default=None, alias="signalDecodersToAdd"
    )
    signal_decoders_to_update: Optional[Sequence[SignalDecoderModel]] = Field(
        default=None, alias="signalDecodersToUpdate"
    )
    signal_decoders_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="signalDecodersToRemove"
    )
    network_interfaces_to_add: Optional[Sequence[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfacesToAdd"
    )
    network_interfaces_to_update: Optional[Sequence[NetworkInterfaceModel]] = Field(
        default=None, alias="networkInterfacesToUpdate"
    )
    network_interfaces_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="networkInterfacesToRemove"
    )
    status: Optional[Literal["ACTIVE", "DRAFT"]] = Field(default=None, alias="status")
