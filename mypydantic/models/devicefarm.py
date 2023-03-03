# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TrialMinutesModel(BaseModel):
    total: Optional[float] = Field(default=None, alias="total")
    remaining: Optional[float] = Field(default=None, alias="remaining")


class ArtifactModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[
        Literal[
            "APPIUM_JAVA_OUTPUT",
            "APPIUM_JAVA_XML_OUTPUT",
            "APPIUM_PYTHON_OUTPUT",
            "APPIUM_PYTHON_XML_OUTPUT",
            "APPIUM_SERVER_OUTPUT",
            "APPLICATION_CRASH_REPORT",
            "AUTOMATION_OUTPUT",
            "CALABASH_JAVA_XML_OUTPUT",
            "CALABASH_JSON_OUTPUT",
            "CALABASH_PRETTY_OUTPUT",
            "CALABASH_STANDARD_OUTPUT",
            "CUSTOMER_ARTIFACT",
            "CUSTOMER_ARTIFACT_LOG",
            "DEVICE_LOG",
            "EXERCISER_MONKEY_OUTPUT",
            "EXPLORER_EVENT_LOG",
            "EXPLORER_SUMMARY_LOG",
            "INSTRUMENTATION_OUTPUT",
            "MESSAGE_LOG",
            "RESULT_LOG",
            "SCREENSHOT",
            "SERVICE_LOG",
            "TESTSPEC_OUTPUT",
            "UNKNOWN",
            "VIDEO",
            "VIDEO_LOG",
            "WEBKIT_LOG",
            "XCTEST_LOG",
        ]
    ] = Field(default=None, alias="type")
    extension: Optional[str] = Field(default=None, alias="extension")
    url: Optional[str] = Field(default=None, alias="url")


class CPUModel(BaseModel):
    frequency: Optional[str] = Field(default=None, alias="frequency")
    architecture: Optional[str] = Field(default=None, alias="architecture")
    clock: Optional[float] = Field(default=None, alias="clock")


class CountersModel(BaseModel):
    total: Optional[int] = Field(default=None, alias="total")
    passed: Optional[int] = Field(default=None, alias="passed")
    failed: Optional[int] = Field(default=None, alias="failed")
    warned: Optional[int] = Field(default=None, alias="warned")
    errored: Optional[int] = Field(default=None, alias="errored")
    stopped: Optional[int] = Field(default=None, alias="stopped")
    skipped: Optional[int] = Field(default=None, alias="skipped")


class RuleModel(BaseModel):
    attribute: Optional[
        Literal[
            "APPIUM_VERSION",
            "ARN",
            "AVAILABILITY",
            "FLEET_TYPE",
            "FORM_FACTOR",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "MANUFACTURER",
            "MODEL",
            "OS_VERSION",
            "PLATFORM",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
        ]
    ] = Field(default=None, alias="attribute")
    operator: Optional[
        Literal[
            "CONTAINS",
            "EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "NOT_IN",
        ]
    ] = Field(default=None, alias="operator")
    value: Optional[str] = Field(default=None, alias="value")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateInstanceProfileRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    package_cleanup: Optional[bool] = Field(default=None, alias="packageCleanup")
    exclude_app_packages_from_cleanup: Optional[Sequence[str]] = Field(
        default=None, alias="excludeAppPackagesFromCleanup"
    )
    reboot_after_use: Optional[bool] = Field(default=None, alias="rebootAfterUse")


class InstanceProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    package_cleanup: Optional[bool] = Field(default=None, alias="packageCleanup")
    exclude_app_packages_from_cleanup: Optional[List[str]] = Field(
        default=None, alias="excludeAppPackagesFromCleanup"
    )
    reboot_after_use: Optional[bool] = Field(default=None, alias="rebootAfterUse")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")


class CreateNetworkProfileRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    uplink_bandwidth_bits: Optional[int] = Field(
        default=None, alias="uplinkBandwidthBits"
    )
    downlink_bandwidth_bits: Optional[int] = Field(
        default=None, alias="downlinkBandwidthBits"
    )
    uplink_delay_ms: Optional[int] = Field(default=None, alias="uplinkDelayMs")
    downlink_delay_ms: Optional[int] = Field(default=None, alias="downlinkDelayMs")
    uplink_jitter_ms: Optional[int] = Field(default=None, alias="uplinkJitterMs")
    downlink_jitter_ms: Optional[int] = Field(default=None, alias="downlinkJitterMs")
    uplink_loss_percent: Optional[int] = Field(default=None, alias="uplinkLossPercent")
    downlink_loss_percent: Optional[int] = Field(
        default=None, alias="downlinkLossPercent"
    )


class NetworkProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    uplink_bandwidth_bits: Optional[int] = Field(
        default=None, alias="uplinkBandwidthBits"
    )
    downlink_bandwidth_bits: Optional[int] = Field(
        default=None, alias="downlinkBandwidthBits"
    )
    uplink_delay_ms: Optional[int] = Field(default=None, alias="uplinkDelayMs")
    downlink_delay_ms: Optional[int] = Field(default=None, alias="downlinkDelayMs")
    uplink_jitter_ms: Optional[int] = Field(default=None, alias="uplinkJitterMs")
    downlink_jitter_ms: Optional[int] = Field(default=None, alias="downlinkJitterMs")
    uplink_loss_percent: Optional[int] = Field(default=None, alias="uplinkLossPercent")
    downlink_loss_percent: Optional[int] = Field(
        default=None, alias="downlinkLossPercent"
    )


class VpcConfigModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="securityGroupIds")
    subnet_ids: Sequence[str] = Field(alias="subnetIds")
    vpc_id: str = Field(alias="vpcId")


class CreateRemoteAccessSessionConfigurationModel(BaseModel):
    billing_method: Optional[Literal["METERED", "UNMETERED"]] = Field(
        default=None, alias="billingMethod"
    )
    vpce_configuration_arns: Optional[Sequence[str]] = Field(
        default=None, alias="vpceConfigurationArns"
    )


class TestGridVpcConfigModel(BaseModel):
    security_group_ids: Sequence[str] = Field(alias="securityGroupIds")
    subnet_ids: Sequence[str] = Field(alias="subnetIds")
    vpc_id: str = Field(alias="vpcId")


class CreateTestGridUrlRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    expires_in_seconds: int = Field(alias="expiresInSeconds")


class CreateUploadRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    name: str = Field(alias="name")
    type: Literal[
        "ANDROID_APP",
        "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
        "APPIUM_JAVA_JUNIT_TEST_SPEC",
        "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
        "APPIUM_JAVA_TESTNG_TEST_SPEC",
        "APPIUM_NODE_TEST_PACKAGE",
        "APPIUM_NODE_TEST_SPEC",
        "APPIUM_PYTHON_TEST_PACKAGE",
        "APPIUM_PYTHON_TEST_SPEC",
        "APPIUM_RUBY_TEST_PACKAGE",
        "APPIUM_RUBY_TEST_SPEC",
        "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
        "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
        "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
        "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
        "APPIUM_WEB_NODE_TEST_PACKAGE",
        "APPIUM_WEB_NODE_TEST_SPEC",
        "APPIUM_WEB_PYTHON_TEST_PACKAGE",
        "APPIUM_WEB_PYTHON_TEST_SPEC",
        "APPIUM_WEB_RUBY_TEST_PACKAGE",
        "APPIUM_WEB_RUBY_TEST_SPEC",
        "CALABASH_TEST_PACKAGE",
        "EXTERNAL_DATA",
        "INSTRUMENTATION_TEST_PACKAGE",
        "INSTRUMENTATION_TEST_SPEC",
        "IOS_APP",
        "UIAUTOMATION_TEST_PACKAGE",
        "UIAUTOMATOR_TEST_PACKAGE",
        "WEB_APP",
        "XCTEST_TEST_PACKAGE",
        "XCTEST_UI_TEST_PACKAGE",
        "XCTEST_UI_TEST_SPEC",
    ] = Field(alias="type")
    content_type: Optional[str] = Field(default=None, alias="contentType")


class UploadModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    created: Optional[datetime] = Field(default=None, alias="created")
    type: Optional[
        Literal[
            "ANDROID_APP",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "CALABASH_TEST_PACKAGE",
            "EXTERNAL_DATA",
            "INSTRUMENTATION_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_SPEC",
            "IOS_APP",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "WEB_APP",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "XCTEST_UI_TEST_SPEC",
        ]
    ] = Field(default=None, alias="type")
    status: Optional[
        Literal["FAILED", "INITIALIZED", "PROCESSING", "SUCCEEDED"]
    ] = Field(default=None, alias="status")
    url: Optional[str] = Field(default=None, alias="url")
    metadata: Optional[str] = Field(default=None, alias="metadata")
    content_type: Optional[str] = Field(default=None, alias="contentType")
    message: Optional[str] = Field(default=None, alias="message")
    category: Optional[Literal["CURATED", "PRIVATE"]] = Field(
        default=None, alias="category"
    )


class CreateVPCEConfigurationRequestModel(BaseModel):
    vpce_configuration_name: str = Field(alias="vpceConfigurationName")
    vpce_service_name: str = Field(alias="vpceServiceName")
    service_dns_name: str = Field(alias="serviceDnsName")
    vpce_configuration_description: Optional[str] = Field(
        default=None, alias="vpceConfigurationDescription"
    )


class VPCEConfigurationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    vpce_configuration_name: Optional[str] = Field(
        default=None, alias="vpceConfigurationName"
    )
    vpce_service_name: Optional[str] = Field(default=None, alias="vpceServiceName")
    service_dns_name: Optional[str] = Field(default=None, alias="serviceDnsName")
    vpce_configuration_description: Optional[str] = Field(
        default=None, alias="vpceConfigurationDescription"
    )


class CustomerArtifactPathsModel(BaseModel):
    ios_paths: Optional[Sequence[str]] = Field(default=None, alias="iosPaths")
    android_paths: Optional[Sequence[str]] = Field(default=None, alias="androidPaths")
    device_host_paths: Optional[Sequence[str]] = Field(
        default=None, alias="deviceHostPaths"
    )


class DeleteDevicePoolRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteInstanceProfileRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteNetworkProfileRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteProjectRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteRemoteAccessSessionRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteRunRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteTestGridProjectRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")


class DeleteUploadRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteVPCEConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeviceFilterModel(BaseModel):
    attribute: Literal[
        "ARN",
        "AVAILABILITY",
        "FLEET_TYPE",
        "FORM_FACTOR",
        "INSTANCE_ARN",
        "INSTANCE_LABELS",
        "MANUFACTURER",
        "MODEL",
        "OS_VERSION",
        "PLATFORM",
        "REMOTE_ACCESS_ENABLED",
        "REMOTE_DEBUG_ENABLED",
    ] = Field(alias="attribute")
    operator: Literal[
        "CONTAINS",
        "EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUALS",
        "IN",
        "LESS_THAN",
        "LESS_THAN_OR_EQUALS",
        "NOT_IN",
    ] = Field(alias="operator")
    values: List[str] = Field(alias="values")


class DeviceMinutesModel(BaseModel):
    total: Optional[float] = Field(default=None, alias="total")
    metered: Optional[float] = Field(default=None, alias="metered")
    unmetered: Optional[float] = Field(default=None, alias="unmetered")


class IncompatibilityMessageModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")
    type: Optional[
        Literal[
            "APPIUM_VERSION",
            "ARN",
            "AVAILABILITY",
            "FLEET_TYPE",
            "FORM_FACTOR",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "MANUFACTURER",
            "MODEL",
            "OS_VERSION",
            "PLATFORM",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
        ]
    ] = Field(default=None, alias="type")


class ResolutionModel(BaseModel):
    width: Optional[int] = Field(default=None, alias="width")
    height: Optional[int] = Field(default=None, alias="height")


class ExecutionConfigurationModel(BaseModel):
    job_timeout_minutes: Optional[int] = Field(default=None, alias="jobTimeoutMinutes")
    accounts_cleanup: Optional[bool] = Field(default=None, alias="accountsCleanup")
    app_packages_cleanup: Optional[bool] = Field(
        default=None, alias="appPackagesCleanup"
    )
    video_capture: Optional[bool] = Field(default=None, alias="videoCapture")
    skip_app_resign: Optional[bool] = Field(default=None, alias="skipAppResign")


class GetDeviceInstanceRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class ScheduleRunTestModel(BaseModel):
    type: Literal[
        "APPIUM_JAVA_JUNIT",
        "APPIUM_JAVA_TESTNG",
        "APPIUM_NODE",
        "APPIUM_PYTHON",
        "APPIUM_RUBY",
        "APPIUM_WEB_JAVA_JUNIT",
        "APPIUM_WEB_JAVA_TESTNG",
        "APPIUM_WEB_NODE",
        "APPIUM_WEB_PYTHON",
        "APPIUM_WEB_RUBY",
        "BUILTIN_EXPLORER",
        "BUILTIN_FUZZ",
        "CALABASH",
        "INSTRUMENTATION",
        "REMOTE_ACCESS_RECORD",
        "REMOTE_ACCESS_REPLAY",
        "UIAUTOMATION",
        "UIAUTOMATOR",
        "WEB_PERFORMANCE_PROFILE",
        "XCTEST",
        "XCTEST_UI",
    ] = Field(alias="type")
    test_package_arn: Optional[str] = Field(default=None, alias="testPackageArn")
    test_spec_arn: Optional[str] = Field(default=None, alias="testSpecArn")
    filter: Optional[str] = Field(default=None, alias="filter")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")


class GetDevicePoolRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetDeviceRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetInstanceProfileRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetJobRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetNetworkProfileRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetOfferingStatusRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetProjectRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetRemoteAccessSessionRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetRunRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetSuiteRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetTestGridProjectRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")


class GetTestGridSessionRequestModel(BaseModel):
    project_arn: Optional[str] = Field(default=None, alias="projectArn")
    session_id: Optional[str] = Field(default=None, alias="sessionId")
    session_arn: Optional[str] = Field(default=None, alias="sessionArn")


class TestGridSessionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[Literal["ACTIVE", "CLOSED", "ERRORED"]] = Field(
        default=None, alias="status"
    )
    created: Optional[datetime] = Field(default=None, alias="created")
    ended: Optional[datetime] = Field(default=None, alias="ended")
    billing_minutes: Optional[float] = Field(default=None, alias="billingMinutes")
    selenium_properties: Optional[str] = Field(default=None, alias="seleniumProperties")


class GetTestRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetUploadRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetVPCEConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class InstallToRemoteAccessSessionRequestModel(BaseModel):
    remote_access_session_arn: str = Field(alias="remoteAccessSessionArn")
    app_arn: str = Field(alias="appArn")


class ListArtifactsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Literal["FILE", "LOG", "SCREENSHOT"] = Field(alias="type")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDeviceInstancesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDevicePoolsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListInstanceProfilesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListJobsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListNetworkProfilesRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListOfferingPromotionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class OfferingPromotionModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")


class ListOfferingTransactionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListOfferingsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListProjectsRequestModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRemoteAccessSessionsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListRunsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListSamplesRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class SampleModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    type: Optional[
        Literal[
            "CPU",
            "MEMORY",
            "NATIVE_AVG_DRAWTIME",
            "NATIVE_FPS",
            "NATIVE_FRAMES",
            "NATIVE_MAX_DRAWTIME",
            "NATIVE_MIN_DRAWTIME",
            "OPENGL_AVG_DRAWTIME",
            "OPENGL_FPS",
            "OPENGL_FRAMES",
            "OPENGL_MAX_DRAWTIME",
            "OPENGL_MIN_DRAWTIME",
            "RX",
            "RX_RATE",
            "THREADS",
            "TX",
            "TX_RATE",
        ]
    ] = Field(default=None, alias="type")
    url: Optional[str] = Field(default=None, alias="url")


class ListSuitesRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class ListTestGridProjectsRequestModel(BaseModel):
    max_result: Optional[int] = Field(default=None, alias="maxResult")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTestGridSessionActionsRequestModel(BaseModel):
    session_arn: str = Field(alias="sessionArn")
    max_result: Optional[int] = Field(default=None, alias="maxResult")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TestGridSessionActionModel(BaseModel):
    action: Optional[str] = Field(default=None, alias="action")
    started: Optional[datetime] = Field(default=None, alias="started")
    duration: Optional[int] = Field(default=None, alias="duration")
    status_code: Optional[str] = Field(default=None, alias="statusCode")
    request_method: Optional[str] = Field(default=None, alias="requestMethod")


class ListTestGridSessionArtifactsRequestModel(BaseModel):
    session_arn: str = Field(alias="sessionArn")
    type: Optional[Literal["LOG", "VIDEO"]] = Field(default=None, alias="type")
    max_result: Optional[int] = Field(default=None, alias="maxResult")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class TestGridSessionArtifactModel(BaseModel):
    filename: Optional[str] = Field(default=None, alias="filename")
    type: Optional[Literal["SELENIUM_LOG", "UNKNOWN", "VIDEO"]] = Field(
        default=None, alias="type"
    )
    url: Optional[str] = Field(default=None, alias="url")


class ListTestGridSessionsRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    status: Optional[Literal["ACTIVE", "CLOSED", "ERRORED"]] = Field(
        default=None, alias="status"
    )
    creation_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="creationTimeAfter"
    )
    creation_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="creationTimeBefore"
    )
    end_time_after: Optional[Union[datetime, str]] = Field(
        default=None, alias="endTimeAfter"
    )
    end_time_before: Optional[Union[datetime, str]] = Field(
        default=None, alias="endTimeBefore"
    )
    max_result: Optional[int] = Field(default=None, alias="maxResult")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTestsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListUniqueProblemsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListUploadsRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Optional[
        Literal[
            "ANDROID_APP",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "CALABASH_TEST_PACKAGE",
            "EXTERNAL_DATA",
            "INSTRUMENTATION_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_SPEC",
            "IOS_APP",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "WEB_APP",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "XCTEST_UI_TEST_SPEC",
        ]
    ] = Field(default=None, alias="type")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListVPCEConfigurationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class LocationModel(BaseModel):
    latitude: float = Field(alias="latitude")
    longitude: float = Field(alias="longitude")


class MonetaryAmountModel(BaseModel):
    amount: Optional[float] = Field(default=None, alias="amount")
    currency_code: Optional[Literal["USD"]] = Field(default=None, alias="currencyCode")


class ProblemDetailModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")


class PurchaseOfferingRequestModel(BaseModel):
    offering_id: str = Field(alias="offeringId")
    quantity: int = Field(alias="quantity")
    offering_promotion_id: Optional[str] = Field(
        default=None, alias="offeringPromotionId"
    )


class RadiosModel(BaseModel):
    wifi: Optional[bool] = Field(default=None, alias="wifi")
    bluetooth: Optional[bool] = Field(default=None, alias="bluetooth")
    nfc: Optional[bool] = Field(default=None, alias="nfc")
    gps: Optional[bool] = Field(default=None, alias="gps")


class RenewOfferingRequestModel(BaseModel):
    offering_id: str = Field(alias="offeringId")
    quantity: int = Field(alias="quantity")


class StopJobRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class StopRemoteAccessSessionRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class StopRunRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateDeviceInstanceRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    profile_arn: Optional[str] = Field(default=None, alias="profileArn")
    labels: Optional[Sequence[str]] = Field(default=None, alias="labels")


class UpdateInstanceProfileRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    package_cleanup: Optional[bool] = Field(default=None, alias="packageCleanup")
    exclude_app_packages_from_cleanup: Optional[Sequence[str]] = Field(
        default=None, alias="excludeAppPackagesFromCleanup"
    )
    reboot_after_use: Optional[bool] = Field(default=None, alias="rebootAfterUse")


class UpdateNetworkProfileRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    uplink_bandwidth_bits: Optional[int] = Field(
        default=None, alias="uplinkBandwidthBits"
    )
    downlink_bandwidth_bits: Optional[int] = Field(
        default=None, alias="downlinkBandwidthBits"
    )
    uplink_delay_ms: Optional[int] = Field(default=None, alias="uplinkDelayMs")
    downlink_delay_ms: Optional[int] = Field(default=None, alias="downlinkDelayMs")
    uplink_jitter_ms: Optional[int] = Field(default=None, alias="uplinkJitterMs")
    downlink_jitter_ms: Optional[int] = Field(default=None, alias="downlinkJitterMs")
    uplink_loss_percent: Optional[int] = Field(default=None, alias="uplinkLossPercent")
    downlink_loss_percent: Optional[int] = Field(
        default=None, alias="downlinkLossPercent"
    )


class UpdateUploadRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    content_type: Optional[str] = Field(default=None, alias="contentType")
    edit_content: Optional[bool] = Field(default=None, alias="editContent")


class UpdateVPCEConfigurationRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    vpce_configuration_name: Optional[str] = Field(
        default=None, alias="vpceConfigurationName"
    )
    vpce_service_name: Optional[str] = Field(default=None, alias="vpceServiceName")
    service_dns_name: Optional[str] = Field(default=None, alias="serviceDnsName")
    vpce_configuration_description: Optional[str] = Field(
        default=None, alias="vpceConfigurationDescription"
    )


class AccountSettingsModel(BaseModel):
    aws_account_number: Optional[str] = Field(default=None, alias="awsAccountNumber")
    unmetered_devices: Optional[Dict[Literal["ANDROID", "IOS"], int]] = Field(
        default=None, alias="unmeteredDevices"
    )
    unmetered_remote_access_devices: Optional[
        Dict[Literal["ANDROID", "IOS"], int]
    ] = Field(default=None, alias="unmeteredRemoteAccessDevices")
    max_job_timeout_minutes: Optional[int] = Field(
        default=None, alias="maxJobTimeoutMinutes"
    )
    trial_minutes: Optional[TrialMinutesModel] = Field(
        default=None, alias="trialMinutes"
    )
    max_slots: Optional[Dict[str, int]] = Field(default=None, alias="maxSlots")
    default_job_timeout_minutes: Optional[int] = Field(
        default=None, alias="defaultJobTimeoutMinutes"
    )
    skip_app_resign: Optional[bool] = Field(default=None, alias="skipAppResign")


class CreateDevicePoolRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    name: str = Field(alias="name")
    rules: Sequence[RuleModel] = Field(alias="rules")
    description: Optional[str] = Field(default=None, alias="description")
    max_devices: Optional[int] = Field(default=None, alias="maxDevices")


class DevicePoolModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    rules: Optional[List[RuleModel]] = Field(default=None, alias="rules")
    max_devices: Optional[int] = Field(default=None, alias="maxDevices")


class UpdateDevicePoolRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    rules: Optional[Sequence[RuleModel]] = Field(default=None, alias="rules")
    max_devices: Optional[int] = Field(default=None, alias="maxDevices")
    clear_max_devices: Optional[bool] = Field(default=None, alias="clearMaxDevices")


class CreateTestGridUrlResultModel(BaseModel):
    url: str = Field(alias="url")
    expires: datetime = Field(alias="expires")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListArtifactsResultModel(BaseModel):
    artifacts: List[ArtifactModel] = Field(alias="artifacts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateInstanceProfileResultModel(BaseModel):
    instance_profile: InstanceProfileModel = Field(alias="instanceProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceInstanceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    device_arn: Optional[str] = Field(default=None, alias="deviceArn")
    labels: Optional[List[str]] = Field(default=None, alias="labels")
    status: Optional[
        Literal["AVAILABLE", "IN_USE", "NOT_AVAILABLE", "PREPARING"]
    ] = Field(default=None, alias="status")
    udid: Optional[str] = Field(default=None, alias="udid")
    instance_profile: Optional[InstanceProfileModel] = Field(
        default=None, alias="instanceProfile"
    )


class GetInstanceProfileResultModel(BaseModel):
    instance_profile: InstanceProfileModel = Field(alias="instanceProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListInstanceProfilesResultModel(BaseModel):
    instance_profiles: List[InstanceProfileModel] = Field(alias="instanceProfiles")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateInstanceProfileResultModel(BaseModel):
    instance_profile: InstanceProfileModel = Field(alias="instanceProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNetworkProfileResultModel(BaseModel):
    network_profile: NetworkProfileModel = Field(alias="networkProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetNetworkProfileResultModel(BaseModel):
    network_profile: NetworkProfileModel = Field(alias="networkProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNetworkProfilesResultModel(BaseModel):
    network_profiles: List[NetworkProfileModel] = Field(alias="networkProfiles")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNetworkProfileResultModel(BaseModel):
    network_profile: NetworkProfileModel = Field(alias="networkProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectRequestModel(BaseModel):
    name: str = Field(alias="name")
    default_job_timeout_minutes: Optional[int] = Field(
        default=None, alias="defaultJobTimeoutMinutes"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")


class ProjectModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    default_job_timeout_minutes: Optional[int] = Field(
        default=None, alias="defaultJobTimeoutMinutes"
    )
    created: Optional[datetime] = Field(default=None, alias="created")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")


class UpdateProjectRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    default_job_timeout_minutes: Optional[int] = Field(
        default=None, alias="defaultJobTimeoutMinutes"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")


class CreateRemoteAccessSessionRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    device_arn: str = Field(alias="deviceArn")
    instance_arn: Optional[str] = Field(default=None, alias="instanceArn")
    ssh_public_key: Optional[str] = Field(default=None, alias="sshPublicKey")
    remote_debug_enabled: Optional[bool] = Field(
        default=None, alias="remoteDebugEnabled"
    )
    remote_record_enabled: Optional[bool] = Field(
        default=None, alias="remoteRecordEnabled"
    )
    remote_record_app_arn: Optional[str] = Field(
        default=None, alias="remoteRecordAppArn"
    )
    name: Optional[str] = Field(default=None, alias="name")
    client_id: Optional[str] = Field(default=None, alias="clientId")
    configuration: Optional[CreateRemoteAccessSessionConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    interaction_mode: Optional[
        Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"]
    ] = Field(default=None, alias="interactionMode")
    skip_app_resign: Optional[bool] = Field(default=None, alias="skipAppResign")


class CreateTestGridProjectRequestModel(BaseModel):
    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    vpc_config: Optional[TestGridVpcConfigModel] = Field(
        default=None, alias="vpcConfig"
    )


class TestGridProjectModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    vpc_config: Optional[TestGridVpcConfigModel] = Field(
        default=None, alias="vpcConfig"
    )
    created: Optional[datetime] = Field(default=None, alias="created")


class UpdateTestGridProjectRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    vpc_config: Optional[TestGridVpcConfigModel] = Field(
        default=None, alias="vpcConfig"
    )


class CreateUploadResultModel(BaseModel):
    upload: UploadModel = Field(alias="upload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetUploadResultModel(BaseModel):
    upload: UploadModel = Field(alias="upload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class InstallToRemoteAccessSessionResultModel(BaseModel):
    app_upload: UploadModel = Field(alias="appUpload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUploadsResultModel(BaseModel):
    uploads: List[UploadModel] = Field(alias="uploads")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUploadResultModel(BaseModel):
    upload: UploadModel = Field(alias="upload")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateVPCEConfigurationResultModel(BaseModel):
    vpce_configuration: VPCEConfigurationModel = Field(alias="vpceConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetVPCEConfigurationResultModel(BaseModel):
    vpce_configuration: VPCEConfigurationModel = Field(alias="vpceConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListVPCEConfigurationsResultModel(BaseModel):
    vpce_configurations: List[VPCEConfigurationModel] = Field(
        alias="vpceConfigurations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateVPCEConfigurationResultModel(BaseModel):
    vpce_configuration: VPCEConfigurationModel = Field(alias="vpceConfiguration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceSelectionConfigurationModel(BaseModel):
    filters: Sequence[DeviceFilterModel] = Field(alias="filters")
    max_devices: int = Field(alias="maxDevices")


class DeviceSelectionResultModel(BaseModel):
    filters: Optional[List[DeviceFilterModel]] = Field(default=None, alias="filters")
    matched_devices_count: Optional[int] = Field(
        default=None, alias="matchedDevicesCount"
    )
    max_devices: Optional[int] = Field(default=None, alias="maxDevices")


class ListDevicesRequestModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    filters: Optional[Sequence[DeviceFilterModel]] = Field(
        default=None, alias="filters"
    )


class SuiteModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[
        Literal[
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_NODE",
            "APPIUM_PYTHON",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_RUBY",
            "BUILTIN_EXPLORER",
            "BUILTIN_FUZZ",
            "CALABASH",
            "INSTRUMENTATION",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "WEB_PERFORMANCE_PROFILE",
            "XCTEST",
            "XCTEST_UI",
        ]
    ] = Field(default=None, alias="type")
    created: Optional[datetime] = Field(default=None, alias="created")
    status: Optional[
        Literal[
            "COMPLETED",
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PREPARING",
            "PROCESSING",
            "RUNNING",
            "SCHEDULING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    result: Optional[
        Literal[
            "ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"
        ]
    ] = Field(default=None, alias="result")
    started: Optional[datetime] = Field(default=None, alias="started")
    stopped: Optional[datetime] = Field(default=None, alias="stopped")
    counters: Optional[CountersModel] = Field(default=None, alias="counters")
    message: Optional[str] = Field(default=None, alias="message")
    device_minutes: Optional[DeviceMinutesModel] = Field(
        default=None, alias="deviceMinutes"
    )


class TestModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[
        Literal[
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_NODE",
            "APPIUM_PYTHON",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_RUBY",
            "BUILTIN_EXPLORER",
            "BUILTIN_FUZZ",
            "CALABASH",
            "INSTRUMENTATION",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "WEB_PERFORMANCE_PROFILE",
            "XCTEST",
            "XCTEST_UI",
        ]
    ] = Field(default=None, alias="type")
    created: Optional[datetime] = Field(default=None, alias="created")
    status: Optional[
        Literal[
            "COMPLETED",
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PREPARING",
            "PROCESSING",
            "RUNNING",
            "SCHEDULING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    result: Optional[
        Literal[
            "ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"
        ]
    ] = Field(default=None, alias="result")
    started: Optional[datetime] = Field(default=None, alias="started")
    stopped: Optional[datetime] = Field(default=None, alias="stopped")
    counters: Optional[CountersModel] = Field(default=None, alias="counters")
    message: Optional[str] = Field(default=None, alias="message")
    device_minutes: Optional[DeviceMinutesModel] = Field(
        default=None, alias="deviceMinutes"
    )


class GetOfferingStatusRequestGetOfferingStatusPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListArtifactsRequestListArtifactsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Literal["FILE", "LOG", "SCREENSHOT"] = Field(alias="type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDeviceInstancesRequestListDeviceInstancesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevicePoolsRequestListDevicePoolsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevicesRequestListDevicesPaginateModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    filters: Optional[Sequence[DeviceFilterModel]] = Field(
        default=None, alias="filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListInstanceProfilesRequestListInstanceProfilesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestListJobsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNetworkProfilesRequestListNetworkProfilesPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Optional[Literal["CURATED", "PRIVATE"]] = Field(default=None, alias="type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOfferingPromotionsRequestListOfferingPromotionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOfferingTransactionsRequestListOfferingTransactionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOfferingsRequestListOfferingsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectsRequestListProjectsPaginateModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRunsRequestListRunsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSamplesRequestListSamplesPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSuitesRequestListSuitesPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTestsRequestListTestsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUniqueProblemsRequestListUniqueProblemsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUploadsRequestListUploadsPaginateModel(BaseModel):
    arn: str = Field(alias="arn")
    type: Optional[
        Literal[
            "ANDROID_APP",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "CALABASH_TEST_PACKAGE",
            "EXTERNAL_DATA",
            "INSTRUMENTATION_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_SPEC",
            "IOS_APP",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "WEB_APP",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "XCTEST_UI_TEST_SPEC",
        ]
    ] = Field(default=None, alias="type")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetTestGridSessionResultModel(BaseModel):
    test_grid_session: TestGridSessionModel = Field(alias="testGridSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTestGridSessionsResultModel(BaseModel):
    test_grid_sessions: List[TestGridSessionModel] = Field(alias="testGridSessions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOfferingPromotionsResultModel(BaseModel):
    offering_promotions: List[OfferingPromotionModel] = Field(
        alias="offeringPromotions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSamplesResultModel(BaseModel):
    samples: List[SampleModel] = Field(alias="samples")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class ListTestGridSessionActionsResultModel(BaseModel):
    actions: List[TestGridSessionActionModel] = Field(alias="actions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTestGridSessionArtifactsResultModel(BaseModel):
    artifacts: List[TestGridSessionArtifactModel] = Field(alias="artifacts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecurringChargeModel(BaseModel):
    cost: Optional[MonetaryAmountModel] = Field(default=None, alias="cost")
    frequency: Optional[Literal["MONTHLY"]] = Field(default=None, alias="frequency")


class ScheduleRunConfigurationModel(BaseModel):
    extra_data_package_arn: Optional[str] = Field(
        default=None, alias="extraDataPackageArn"
    )
    network_profile_arn: Optional[str] = Field(default=None, alias="networkProfileArn")
    locale: Optional[str] = Field(default=None, alias="locale")
    location: Optional[LocationModel] = Field(default=None, alias="location")
    vpce_configuration_arns: Optional[Sequence[str]] = Field(
        default=None, alias="vpceConfigurationArns"
    )
    customer_artifact_paths: Optional[CustomerArtifactPathsModel] = Field(
        default=None, alias="customerArtifactPaths"
    )
    radios: Optional[RadiosModel] = Field(default=None, alias="radios")
    auxiliary_apps: Optional[Sequence[str]] = Field(default=None, alias="auxiliaryApps")
    billing_method: Optional[Literal["METERED", "UNMETERED"]] = Field(
        default=None, alias="billingMethod"
    )


class GetAccountSettingsResultModel(BaseModel):
    account_settings: AccountSettingsModel = Field(alias="accountSettings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDevicePoolResultModel(BaseModel):
    device_pool: DevicePoolModel = Field(alias="devicePool")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDevicePoolResultModel(BaseModel):
    device_pool: DevicePoolModel = Field(alias="devicePool")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevicePoolsResultModel(BaseModel):
    device_pools: List[DevicePoolModel] = Field(alias="devicePools")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDevicePoolResultModel(BaseModel):
    device_pool: DevicePoolModel = Field(alias="devicePool")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeviceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    manufacturer: Optional[str] = Field(default=None, alias="manufacturer")
    model: Optional[str] = Field(default=None, alias="model")
    model_id: Optional[str] = Field(default=None, alias="modelId")
    form_factor: Optional[Literal["PHONE", "TABLET"]] = Field(
        default=None, alias="formFactor"
    )
    platform: Optional[Literal["ANDROID", "IOS"]] = Field(
        default=None, alias="platform"
    )
    os: Optional[str] = Field(default=None, alias="os")
    cpu: Optional[CPUModel] = Field(default=None, alias="cpu")
    resolution: Optional[ResolutionModel] = Field(default=None, alias="resolution")
    heap_size: Optional[int] = Field(default=None, alias="heapSize")
    memory: Optional[int] = Field(default=None, alias="memory")
    image: Optional[str] = Field(default=None, alias="image")
    carrier: Optional[str] = Field(default=None, alias="carrier")
    radio: Optional[str] = Field(default=None, alias="radio")
    remote_access_enabled: Optional[bool] = Field(
        default=None, alias="remoteAccessEnabled"
    )
    remote_debug_enabled: Optional[bool] = Field(
        default=None, alias="remoteDebugEnabled"
    )
    fleet_type: Optional[str] = Field(default=None, alias="fleetType")
    fleet_name: Optional[str] = Field(default=None, alias="fleetName")
    instances: Optional[List[DeviceInstanceModel]] = Field(
        default=None, alias="instances"
    )
    availability: Optional[
        Literal["AVAILABLE", "BUSY", "HIGHLY_AVAILABLE", "TEMPORARY_NOT_AVAILABLE"]
    ] = Field(default=None, alias="availability")


class GetDeviceInstanceResultModel(BaseModel):
    device_instance: DeviceInstanceModel = Field(alias="deviceInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDeviceInstancesResultModel(BaseModel):
    device_instances: List[DeviceInstanceModel] = Field(alias="deviceInstances")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDeviceInstanceResultModel(BaseModel):
    device_instance: DeviceInstanceModel = Field(alias="deviceInstance")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResultModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProjectResultModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProjectsResultModel(BaseModel):
    projects: List[ProjectModel] = Field(alias="projects")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProjectResultModel(BaseModel):
    project: ProjectModel = Field(alias="project")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTestGridProjectResultModel(BaseModel):
    test_grid_project: TestGridProjectModel = Field(alias="testGridProject")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTestGridProjectResultModel(BaseModel):
    test_grid_project: TestGridProjectModel = Field(alias="testGridProject")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTestGridProjectsResultModel(BaseModel):
    test_grid_projects: List[TestGridProjectModel] = Field(alias="testGridProjects")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTestGridProjectResultModel(BaseModel):
    test_grid_project: TestGridProjectModel = Field(alias="testGridProject")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RunModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[
        Literal[
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_NODE",
            "APPIUM_PYTHON",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_RUBY",
            "BUILTIN_EXPLORER",
            "BUILTIN_FUZZ",
            "CALABASH",
            "INSTRUMENTATION",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "WEB_PERFORMANCE_PROFILE",
            "XCTEST",
            "XCTEST_UI",
        ]
    ] = Field(default=None, alias="type")
    platform: Optional[Literal["ANDROID", "IOS"]] = Field(
        default=None, alias="platform"
    )
    created: Optional[datetime] = Field(default=None, alias="created")
    status: Optional[
        Literal[
            "COMPLETED",
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PREPARING",
            "PROCESSING",
            "RUNNING",
            "SCHEDULING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    result: Optional[
        Literal[
            "ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"
        ]
    ] = Field(default=None, alias="result")
    started: Optional[datetime] = Field(default=None, alias="started")
    stopped: Optional[datetime] = Field(default=None, alias="stopped")
    counters: Optional[CountersModel] = Field(default=None, alias="counters")
    message: Optional[str] = Field(default=None, alias="message")
    total_jobs: Optional[int] = Field(default=None, alias="totalJobs")
    completed_jobs: Optional[int] = Field(default=None, alias="completedJobs")
    billing_method: Optional[Literal["METERED", "UNMETERED"]] = Field(
        default=None, alias="billingMethod"
    )
    device_minutes: Optional[DeviceMinutesModel] = Field(
        default=None, alias="deviceMinutes"
    )
    network_profile: Optional[NetworkProfileModel] = Field(
        default=None, alias="networkProfile"
    )
    parsing_result_url: Optional[str] = Field(default=None, alias="parsingResultUrl")
    result_code: Optional[
        Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"]
    ] = Field(default=None, alias="resultCode")
    seed: Optional[int] = Field(default=None, alias="seed")
    app_upload: Optional[str] = Field(default=None, alias="appUpload")
    event_count: Optional[int] = Field(default=None, alias="eventCount")
    job_timeout_minutes: Optional[int] = Field(default=None, alias="jobTimeoutMinutes")
    device_pool_arn: Optional[str] = Field(default=None, alias="devicePoolArn")
    locale: Optional[str] = Field(default=None, alias="locale")
    radios: Optional[RadiosModel] = Field(default=None, alias="radios")
    location: Optional[LocationModel] = Field(default=None, alias="location")
    customer_artifact_paths: Optional[CustomerArtifactPathsModel] = Field(
        default=None, alias="customerArtifactPaths"
    )
    web_url: Optional[str] = Field(default=None, alias="webUrl")
    skip_app_resign: Optional[bool] = Field(default=None, alias="skipAppResign")
    test_spec_arn: Optional[str] = Field(default=None, alias="testSpecArn")
    device_selection_result: Optional[DeviceSelectionResultModel] = Field(
        default=None, alias="deviceSelectionResult"
    )
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")


class GetSuiteResultModel(BaseModel):
    suite: SuiteModel = Field(alias="suite")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSuitesResultModel(BaseModel):
    suites: List[SuiteModel] = Field(alias="suites")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTestResultModel(BaseModel):
    test: TestModel = Field(alias="test")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTestsResultModel(BaseModel):
    tests: List[TestModel] = Field(alias="tests")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OfferingModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    description: Optional[str] = Field(default=None, alias="description")
    type: Optional[Literal["RECURRING"]] = Field(default=None, alias="type")
    platform: Optional[Literal["ANDROID", "IOS"]] = Field(
        default=None, alias="platform"
    )
    recurring_charges: Optional[List[RecurringChargeModel]] = Field(
        default=None, alias="recurringCharges"
    )


class GetDevicePoolCompatibilityRequestModel(BaseModel):
    device_pool_arn: str = Field(alias="devicePoolArn")
    app_arn: Optional[str] = Field(default=None, alias="appArn")
    test_type: Optional[
        Literal[
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_NODE",
            "APPIUM_PYTHON",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_RUBY",
            "BUILTIN_EXPLORER",
            "BUILTIN_FUZZ",
            "CALABASH",
            "INSTRUMENTATION",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "WEB_PERFORMANCE_PROFILE",
            "XCTEST",
            "XCTEST_UI",
        ]
    ] = Field(default=None, alias="testType")
    test: Optional[ScheduleRunTestModel] = Field(default=None, alias="test")
    configuration: Optional[ScheduleRunConfigurationModel] = Field(
        default=None, alias="configuration"
    )


class ScheduleRunRequestModel(BaseModel):
    project_arn: str = Field(alias="projectArn")
    test: ScheduleRunTestModel = Field(alias="test")
    app_arn: Optional[str] = Field(default=None, alias="appArn")
    device_pool_arn: Optional[str] = Field(default=None, alias="devicePoolArn")
    device_selection_configuration: Optional[DeviceSelectionConfigurationModel] = Field(
        default=None, alias="deviceSelectionConfiguration"
    )
    name: Optional[str] = Field(default=None, alias="name")
    configuration: Optional[ScheduleRunConfigurationModel] = Field(
        default=None, alias="configuration"
    )
    execution_configuration: Optional[ExecutionConfigurationModel] = Field(
        default=None, alias="executionConfiguration"
    )


class DevicePoolCompatibilityResultModel(BaseModel):
    device: Optional[DeviceModel] = Field(default=None, alias="device")
    compatible: Optional[bool] = Field(default=None, alias="compatible")
    incompatibility_messages: Optional[List[IncompatibilityMessageModel]] = Field(
        default=None, alias="incompatibilityMessages"
    )


class GetDeviceResultModel(BaseModel):
    device: DeviceModel = Field(alias="device")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[
        Literal[
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_NODE",
            "APPIUM_PYTHON",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_RUBY",
            "BUILTIN_EXPLORER",
            "BUILTIN_FUZZ",
            "CALABASH",
            "INSTRUMENTATION",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "WEB_PERFORMANCE_PROFILE",
            "XCTEST",
            "XCTEST_UI",
        ]
    ] = Field(default=None, alias="type")
    created: Optional[datetime] = Field(default=None, alias="created")
    status: Optional[
        Literal[
            "COMPLETED",
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PREPARING",
            "PROCESSING",
            "RUNNING",
            "SCHEDULING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    result: Optional[
        Literal[
            "ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"
        ]
    ] = Field(default=None, alias="result")
    started: Optional[datetime] = Field(default=None, alias="started")
    stopped: Optional[datetime] = Field(default=None, alias="stopped")
    counters: Optional[CountersModel] = Field(default=None, alias="counters")
    message: Optional[str] = Field(default=None, alias="message")
    device: Optional[DeviceModel] = Field(default=None, alias="device")
    instance_arn: Optional[str] = Field(default=None, alias="instanceArn")
    device_minutes: Optional[DeviceMinutesModel] = Field(
        default=None, alias="deviceMinutes"
    )
    video_endpoint: Optional[str] = Field(default=None, alias="videoEndpoint")
    video_capture: Optional[bool] = Field(default=None, alias="videoCapture")


class ListDevicesResultModel(BaseModel):
    devices: List[DeviceModel] = Field(alias="devices")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProblemModel(BaseModel):
    run: Optional[ProblemDetailModel] = Field(default=None, alias="run")
    job: Optional[ProblemDetailModel] = Field(default=None, alias="job")
    suite: Optional[ProblemDetailModel] = Field(default=None, alias="suite")
    test: Optional[ProblemDetailModel] = Field(default=None, alias="test")
    device: Optional[DeviceModel] = Field(default=None, alias="device")
    result: Optional[
        Literal[
            "ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"
        ]
    ] = Field(default=None, alias="result")
    message: Optional[str] = Field(default=None, alias="message")


class RemoteAccessSessionModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    name: Optional[str] = Field(default=None, alias="name")
    created: Optional[datetime] = Field(default=None, alias="created")
    status: Optional[
        Literal[
            "COMPLETED",
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PREPARING",
            "PROCESSING",
            "RUNNING",
            "SCHEDULING",
            "STOPPING",
        ]
    ] = Field(default=None, alias="status")
    result: Optional[
        Literal[
            "ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"
        ]
    ] = Field(default=None, alias="result")
    message: Optional[str] = Field(default=None, alias="message")
    started: Optional[datetime] = Field(default=None, alias="started")
    stopped: Optional[datetime] = Field(default=None, alias="stopped")
    device: Optional[DeviceModel] = Field(default=None, alias="device")
    instance_arn: Optional[str] = Field(default=None, alias="instanceArn")
    remote_debug_enabled: Optional[bool] = Field(
        default=None, alias="remoteDebugEnabled"
    )
    remote_record_enabled: Optional[bool] = Field(
        default=None, alias="remoteRecordEnabled"
    )
    remote_record_app_arn: Optional[str] = Field(
        default=None, alias="remoteRecordAppArn"
    )
    host_address: Optional[str] = Field(default=None, alias="hostAddress")
    client_id: Optional[str] = Field(default=None, alias="clientId")
    billing_method: Optional[Literal["METERED", "UNMETERED"]] = Field(
        default=None, alias="billingMethod"
    )
    device_minutes: Optional[DeviceMinutesModel] = Field(
        default=None, alias="deviceMinutes"
    )
    endpoint: Optional[str] = Field(default=None, alias="endpoint")
    device_udid: Optional[str] = Field(default=None, alias="deviceUdid")
    interaction_mode: Optional[
        Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"]
    ] = Field(default=None, alias="interactionMode")
    skip_app_resign: Optional[bool] = Field(default=None, alias="skipAppResign")
    vpc_config: Optional[VpcConfigModel] = Field(default=None, alias="vpcConfig")


class GetRunResultModel(BaseModel):
    run: RunModel = Field(alias="run")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRunsResultModel(BaseModel):
    runs: List[RunModel] = Field(alias="runs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScheduleRunResultModel(BaseModel):
    run: RunModel = Field(alias="run")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopRunResultModel(BaseModel):
    run: RunModel = Field(alias="run")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOfferingsResultModel(BaseModel):
    offerings: List[OfferingModel] = Field(alias="offerings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OfferingStatusModel(BaseModel):
    type: Optional[Literal["PURCHASE", "RENEW", "SYSTEM"]] = Field(
        default=None, alias="type"
    )
    offering: Optional[OfferingModel] = Field(default=None, alias="offering")
    quantity: Optional[int] = Field(default=None, alias="quantity")
    effective_on: Optional[datetime] = Field(default=None, alias="effectiveOn")


class GetDevicePoolCompatibilityResultModel(BaseModel):
    compatible_devices: List[DevicePoolCompatibilityResultModel] = Field(
        alias="compatibleDevices"
    )
    incompatible_devices: List[DevicePoolCompatibilityResultModel] = Field(
        alias="incompatibleDevices"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobResultModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsResultModel(BaseModel):
    jobs: List[JobModel] = Field(alias="jobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopJobResultModel(BaseModel):
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UniqueProblemModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")
    problems: Optional[List[ProblemModel]] = Field(default=None, alias="problems")


class CreateRemoteAccessSessionResultModel(BaseModel):
    remote_access_session: RemoteAccessSessionModel = Field(alias="remoteAccessSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRemoteAccessSessionResultModel(BaseModel):
    remote_access_session: RemoteAccessSessionModel = Field(alias="remoteAccessSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRemoteAccessSessionsResultModel(BaseModel):
    remote_access_sessions: List[RemoteAccessSessionModel] = Field(
        alias="remoteAccessSessions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopRemoteAccessSessionResultModel(BaseModel):
    remote_access_session: RemoteAccessSessionModel = Field(alias="remoteAccessSession")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOfferingStatusResultModel(BaseModel):
    current: Dict[str, OfferingStatusModel] = Field(alias="current")
    next_period: Dict[str, OfferingStatusModel] = Field(alias="nextPeriod")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OfferingTransactionModel(BaseModel):
    offering_status: Optional[OfferingStatusModel] = Field(
        default=None, alias="offeringStatus"
    )
    transaction_id: Optional[str] = Field(default=None, alias="transactionId")
    offering_promotion_id: Optional[str] = Field(
        default=None, alias="offeringPromotionId"
    )
    created_on: Optional[datetime] = Field(default=None, alias="createdOn")
    cost: Optional[MonetaryAmountModel] = Field(default=None, alias="cost")


class ListUniqueProblemsResultModel(BaseModel):
    unique_problems: Dict[
        Literal[
            "ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"
        ],
        List[UniqueProblemModel],
    ] = Field(alias="uniqueProblems")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOfferingTransactionsResultModel(BaseModel):
    offering_transactions: List[OfferingTransactionModel] = Field(
        alias="offeringTransactions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PurchaseOfferingResultModel(BaseModel):
    offering_transaction: OfferingTransactionModel = Field(alias="offeringTransaction")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RenewOfferingResultModel(BaseModel):
    offering_transaction: OfferingTransactionModel = Field(alias="offeringTransaction")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
