# Model Generated: Thu Mar  2 21:56:20 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class DeleteSuiteDefinitionRequestModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")


class DeviceUnderTestModel(BaseModel):
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")


class GetEndpointRequestModel(BaseModel):
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")


class GetSuiteDefinitionRequestModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_definition_version: Optional[str] = Field(
        default=None, alias="suiteDefinitionVersion"
    )


class GetSuiteRunReportRequestModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_run_id: str = Field(alias="suiteRunId")


class GetSuiteRunRequestModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_run_id: str = Field(alias="suiteRunId")


class ListSuiteDefinitionsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSuiteRunsRequestModel(BaseModel):
    suite_definition_id: Optional[str] = Field(default=None, alias="suiteDefinitionId")
    suite_definition_version: Optional[str] = Field(
        default=None, alias="suiteDefinitionVersion"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SuiteRunInformationModel(BaseModel):
    suite_definition_id: Optional[str] = Field(default=None, alias="suiteDefinitionId")
    suite_definition_version: Optional[str] = Field(
        default=None, alias="suiteDefinitionVersion"
    )
    suite_definition_name: Optional[str] = Field(
        default=None, alias="suiteDefinitionName"
    )
    suite_run_id: Optional[str] = Field(default=None, alias="suiteRunId")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    end_at: Optional[datetime] = Field(default=None, alias="endAt")
    status: Optional[
        Literal[
            "CANCELED",
            "ERROR",
            "FAIL",
            "PASS",
            "PASS_WITH_WARNINGS",
            "PENDING",
            "RUNNING",
            "STOPPED",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    passed: Optional[int] = Field(default=None, alias="passed")
    failed: Optional[int] = Field(default=None, alias="failed")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class StopSuiteRunRequestModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_run_id: str = Field(alias="suiteRunId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class TestCaseScenarioModel(BaseModel):
    test_case_scenario_id: Optional[str] = Field(
        default=None, alias="testCaseScenarioId"
    )
    test_case_scenario_type: Optional[Literal["Advanced", "Basic"]] = Field(
        default=None, alias="testCaseScenarioType"
    )
    status: Optional[
        Literal[
            "CANCELED",
            "ERROR",
            "FAIL",
            "PASS",
            "PASS_WITH_WARNINGS",
            "PENDING",
            "RUNNING",
            "STOPPED",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    failure: Optional[str] = Field(default=None, alias="failure")
    system_message: Optional[str] = Field(default=None, alias="systemMessage")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class CreateSuiteDefinitionResponseModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_definition_arn: str = Field(alias="suiteDefinitionArn")
    suite_definition_name: str = Field(alias="suiteDefinitionName")
    created_at: datetime = Field(alias="createdAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetEndpointResponseModel(BaseModel):
    endpoint: str = Field(alias="endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSuiteRunReportResponseModel(BaseModel):
    qualification_report_download_url: str = Field(
        alias="qualificationReportDownloadUrl"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSuiteRunResponseModel(BaseModel):
    suite_run_id: str = Field(alias="suiteRunId")
    suite_run_arn: str = Field(alias="suiteRunArn")
    created_at: datetime = Field(alias="createdAt")
    endpoint: str = Field(alias="endpoint")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSuiteDefinitionResponseModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_definition_arn: str = Field(alias="suiteDefinitionArn")
    suite_definition_name: str = Field(alias="suiteDefinitionName")
    suite_definition_version: str = Field(alias="suiteDefinitionVersion")
    created_at: datetime = Field(alias="createdAt")
    last_updated_at: datetime = Field(alias="lastUpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SuiteDefinitionConfigurationModel(BaseModel):
    suite_definition_name: str = Field(alias="suiteDefinitionName")
    root_group: str = Field(alias="rootGroup")
    device_permission_role_arn: str = Field(alias="devicePermissionRoleArn")
    devices: Optional[Sequence[DeviceUnderTestModel]] = Field(
        default=None, alias="devices"
    )
    intended_for_qualification: Optional[bool] = Field(
        default=None, alias="intendedForQualification"
    )
    is_long_duration_test: Optional[bool] = Field(
        default=None, alias="isLongDurationTest"
    )
    protocol: Optional[Literal["MqttV3_1_1", "MqttV5"]] = Field(
        default=None, alias="protocol"
    )


class SuiteDefinitionInformationModel(BaseModel):
    suite_definition_id: Optional[str] = Field(default=None, alias="suiteDefinitionId")
    suite_definition_name: Optional[str] = Field(
        default=None, alias="suiteDefinitionName"
    )
    default_devices: Optional[List[DeviceUnderTestModel]] = Field(
        default=None, alias="defaultDevices"
    )
    intended_for_qualification: Optional[bool] = Field(
        default=None, alias="intendedForQualification"
    )
    is_long_duration_test: Optional[bool] = Field(
        default=None, alias="isLongDurationTest"
    )
    protocol: Optional[Literal["MqttV3_1_1", "MqttV5"]] = Field(
        default=None, alias="protocol"
    )
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class SuiteRunConfigurationModel(BaseModel):
    primary_device: DeviceUnderTestModel = Field(alias="primaryDevice")
    selected_test_list: Optional[List[str]] = Field(
        default=None, alias="selectedTestList"
    )
    parallel_run: Optional[bool] = Field(default=None, alias="parallelRun")


class ListSuiteRunsResponseModel(BaseModel):
    suite_runs_list: List[SuiteRunInformationModel] = Field(alias="suiteRunsList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestCaseRunModel(BaseModel):
    test_case_run_id: Optional[str] = Field(default=None, alias="testCaseRunId")
    test_case_definition_id: Optional[str] = Field(
        default=None, alias="testCaseDefinitionId"
    )
    test_case_definition_name: Optional[str] = Field(
        default=None, alias="testCaseDefinitionName"
    )
    status: Optional[
        Literal[
            "CANCELED",
            "ERROR",
            "FAIL",
            "PASS",
            "PASS_WITH_WARNINGS",
            "PENDING",
            "RUNNING",
            "STOPPED",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    log_url: Optional[str] = Field(default=None, alias="logUrl")
    warnings: Optional[str] = Field(default=None, alias="warnings")
    failure: Optional[str] = Field(default=None, alias="failure")
    test_scenarios: Optional[List[TestCaseScenarioModel]] = Field(
        default=None, alias="testScenarios"
    )


class CreateSuiteDefinitionRequestModel(BaseModel):
    suite_definition_configuration: SuiteDefinitionConfigurationModel = Field(
        alias="suiteDefinitionConfiguration"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GetSuiteDefinitionResponseModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_definition_arn: str = Field(alias="suiteDefinitionArn")
    suite_definition_version: str = Field(alias="suiteDefinitionVersion")
    latest_version: str = Field(alias="latestVersion")
    suite_definition_configuration: SuiteDefinitionConfigurationModel = Field(
        alias="suiteDefinitionConfiguration"
    )
    created_at: datetime = Field(alias="createdAt")
    last_modified_at: datetime = Field(alias="lastModifiedAt")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSuiteDefinitionRequestModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_definition_configuration: SuiteDefinitionConfigurationModel = Field(
        alias="suiteDefinitionConfiguration"
    )


class ListSuiteDefinitionsResponseModel(BaseModel):
    suite_definition_information_list: List[SuiteDefinitionInformationModel] = Field(
        alias="suiteDefinitionInformationList"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSuiteRunRequestModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_run_configuration: SuiteRunConfigurationModel = Field(
        alias="suiteRunConfiguration"
    )
    suite_definition_version: Optional[str] = Field(
        default=None, alias="suiteDefinitionVersion"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class GroupResultModel(BaseModel):
    group_id: Optional[str] = Field(default=None, alias="groupId")
    group_name: Optional[str] = Field(default=None, alias="groupName")
    tests: Optional[List[TestCaseRunModel]] = Field(default=None, alias="tests")


class TestResultModel(BaseModel):
    groups: Optional[List[GroupResultModel]] = Field(default=None, alias="groups")


class GetSuiteRunResponseModel(BaseModel):
    suite_definition_id: str = Field(alias="suiteDefinitionId")
    suite_definition_version: str = Field(alias="suiteDefinitionVersion")
    suite_run_id: str = Field(alias="suiteRunId")
    suite_run_arn: str = Field(alias="suiteRunArn")
    suite_run_configuration: SuiteRunConfigurationModel = Field(
        alias="suiteRunConfiguration"
    )
    test_result: TestResultModel = Field(alias="testResult")
    start_time: datetime = Field(alias="startTime")
    end_time: datetime = Field(alias="endTime")
    status: Literal[
        "CANCELED",
        "ERROR",
        "FAIL",
        "PASS",
        "PASS_WITH_WARNINGS",
        "PENDING",
        "RUNNING",
        "STOPPED",
        "STOPPING",
    ] = Field(alias="status")
    error_reason: str = Field(alias="errorReason")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
