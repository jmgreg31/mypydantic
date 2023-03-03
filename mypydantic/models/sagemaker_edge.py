# Model Generated: Thu Mar  2 21:56:23 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ChecksumModel(BaseModel):
    type: Optional[Literal["SHA1"]] = Field(default=None, alias="Type")
    sum: Optional[str] = Field(default=None, alias="Sum")


class DeploymentModelModel(BaseModel):
    model_handle: Optional[str] = Field(default=None, alias="ModelHandle")
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    desired_state: Optional[Literal["DEPLOY", "UNDEPLOY"]] = Field(
        default=None, alias="DesiredState"
    )
    state: Optional[Literal["DEPLOY", "UNDEPLOY"]] = Field(default=None, alias="State")
    status: Optional[Literal["FAIL", "SUCCESS"]] = Field(default=None, alias="Status")
    status_reason: Optional[str] = Field(default=None, alias="StatusReason")
    rollback_failure_reason: Optional[str] = Field(
        default=None, alias="RollbackFailureReason"
    )


class EdgeMetricModel(BaseModel):
    dimension: Optional[str] = Field(default=None, alias="Dimension")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    value: Optional[float] = Field(default=None, alias="Value")
    timestamp: Optional[Union[datetime, str]] = Field(default=None, alias="Timestamp")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class GetDeploymentsRequestModel(BaseModel):
    device_name: str = Field(alias="DeviceName")
    device_fleet_name: str = Field(alias="DeviceFleetName")


class GetDeviceRegistrationRequestModel(BaseModel):
    device_name: str = Field(alias="DeviceName")
    device_fleet_name: str = Field(alias="DeviceFleetName")


class DefinitionModel(BaseModel):
    model_handle: Optional[str] = Field(default=None, alias="ModelHandle")
    s3_url: Optional[str] = Field(default=None, alias="S3Url")
    checksum: Optional[ChecksumModel] = Field(default=None, alias="Checksum")
    state: Optional[Literal["DEPLOY", "UNDEPLOY"]] = Field(default=None, alias="State")


class DeploymentResultModel(BaseModel):
    deployment_name: Optional[str] = Field(default=None, alias="DeploymentName")
    deployment_status: Optional[str] = Field(default=None, alias="DeploymentStatus")
    deployment_status_message: Optional[str] = Field(
        default=None, alias="DeploymentStatusMessage"
    )
    deployment_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="DeploymentStartTime"
    )
    deployment_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="DeploymentEndTime"
    )
    deployment_models: Optional[Sequence[DeploymentModelModel]] = Field(
        default=None, alias="DeploymentModels"
    )


class ModelModel(BaseModel):
    model_name: Optional[str] = Field(default=None, alias="ModelName")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")
    latest_sample_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="LatestSampleTime"
    )
    latest_inference: Optional[Union[datetime, str]] = Field(
        default=None, alias="LatestInference"
    )
    model_metrics: Optional[Sequence[EdgeMetricModel]] = Field(
        default=None, alias="ModelMetrics"
    )


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDeviceRegistrationResultModel(BaseModel):
    device_registration: str = Field(alias="DeviceRegistration")
    cache_ttl: str = Field(alias="CacheTTL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EdgeDeploymentModel(BaseModel):
    deployment_name: Optional[str] = Field(default=None, alias="DeploymentName")
    type: Optional[Literal["Model"]] = Field(default=None, alias="Type")
    failure_handling_policy: Optional[
        Literal["DO_NOTHING", "ROLLBACK_ON_FAILURE"]
    ] = Field(default=None, alias="FailureHandlingPolicy")
    definitions: Optional[List[DefinitionModel]] = Field(
        default=None, alias="Definitions"
    )


class SendHeartbeatRequestModel(BaseModel):
    agent_version: str = Field(alias="AgentVersion")
    device_name: str = Field(alias="DeviceName")
    device_fleet_name: str = Field(alias="DeviceFleetName")
    agent_metrics: Optional[Sequence[EdgeMetricModel]] = Field(
        default=None, alias="AgentMetrics"
    )
    models: Optional[Sequence[ModelModel]] = Field(default=None, alias="Models")
    deployment_result: Optional[DeploymentResultModel] = Field(
        default=None, alias="DeploymentResult"
    )


class GetDeploymentsResultModel(BaseModel):
    deployments: List[EdgeDeploymentModel] = Field(alias="Deployments")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
