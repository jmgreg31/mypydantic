# Model Generated: Thu Mar  2 21:56:19 2023

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


class AbortCriteriaModel(BaseModel):
    failure_type: Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"] = Field(
        alias="failureType"
    )
    action: Literal["CANCEL"] = Field(alias="action")
    threshold_percentage: float = Field(alias="thresholdPercentage")
    min_number_of_executed_things: int = Field(alias="minNumberOfExecutedThings")


class AcceptCertificateTransferRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")
    set_as_active: Optional[bool] = Field(default=None, alias="setAsActive")


class CloudwatchAlarmActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    alarm_name: str = Field(alias="alarmName")
    state_reason: str = Field(alias="stateReason")
    state_value: str = Field(alias="stateValue")


class CloudwatchLogsActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    log_group_name: str = Field(alias="logGroupName")
    batch_mode: Optional[bool] = Field(default=None, alias="batchMode")


class CloudwatchMetricActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    metric_namespace: str = Field(alias="metricNamespace")
    metric_name: str = Field(alias="metricName")
    metric_value: str = Field(alias="metricValue")
    metric_unit: str = Field(alias="metricUnit")
    metric_timestamp: Optional[str] = Field(default=None, alias="metricTimestamp")


class DynamoDBActionModel(BaseModel):
    table_name: str = Field(alias="tableName")
    role_arn: str = Field(alias="roleArn")
    hash_key_field: str = Field(alias="hashKeyField")
    hash_key_value: str = Field(alias="hashKeyValue")
    operation: Optional[str] = Field(default=None, alias="operation")
    hash_key_type: Optional[Literal["NUMBER", "STRING"]] = Field(
        default=None, alias="hashKeyType"
    )
    range_key_field: Optional[str] = Field(default=None, alias="rangeKeyField")
    range_key_value: Optional[str] = Field(default=None, alias="rangeKeyValue")
    range_key_type: Optional[Literal["NUMBER", "STRING"]] = Field(
        default=None, alias="rangeKeyType"
    )
    payload_field: Optional[str] = Field(default=None, alias="payloadField")


class ElasticsearchActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    endpoint: str = Field(alias="endpoint")
    index: str = Field(alias="index")
    type: str = Field(alias="type")
    id: str = Field(alias="id")


class FirehoseActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    delivery_stream_name: str = Field(alias="deliveryStreamName")
    separator: Optional[str] = Field(default=None, alias="separator")
    batch_mode: Optional[bool] = Field(default=None, alias="batchMode")


class IotAnalyticsActionModel(BaseModel):
    channel_arn: Optional[str] = Field(default=None, alias="channelArn")
    channel_name: Optional[str] = Field(default=None, alias="channelName")
    batch_mode: Optional[bool] = Field(default=None, alias="batchMode")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class IotEventsActionModel(BaseModel):
    input_name: str = Field(alias="inputName")
    role_arn: str = Field(alias="roleArn")
    message_id: Optional[str] = Field(default=None, alias="messageId")
    batch_mode: Optional[bool] = Field(default=None, alias="batchMode")


class KafkaActionModel(BaseModel):
    destination_arn: str = Field(alias="destinationArn")
    topic: str = Field(alias="topic")
    client_properties: Mapping[str, str] = Field(alias="clientProperties")
    key: Optional[str] = Field(default=None, alias="key")
    partition: Optional[str] = Field(default=None, alias="partition")


class KinesisActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    stream_name: str = Field(alias="streamName")
    partition_key: Optional[str] = Field(default=None, alias="partitionKey")


class LambdaActionModel(BaseModel):
    function_arn: str = Field(alias="functionArn")


class OpenSearchActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    endpoint: str = Field(alias="endpoint")
    index: str = Field(alias="index")
    type: str = Field(alias="type")
    id: str = Field(alias="id")


class S3ActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    bucket_name: str = Field(alias="bucketName")
    key: str = Field(alias="key")
    canned_acl: Optional[
        Literal[
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-full-control",
            "bucket-owner-read",
            "log-delivery-write",
            "private",
            "public-read",
            "public-read-write",
        ]
    ] = Field(default=None, alias="cannedAcl")


class SalesforceActionModel(BaseModel):
    token: str = Field(alias="token")
    url: str = Field(alias="url")


class SnsActionModel(BaseModel):
    target_arn: str = Field(alias="targetArn")
    role_arn: str = Field(alias="roleArn")
    message_format: Optional[Literal["JSON", "RAW"]] = Field(
        default=None, alias="messageFormat"
    )


class SqsActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    queue_url: str = Field(alias="queueUrl")
    use_base64: Optional[bool] = Field(default=None, alias="useBase64")


class StepFunctionsActionModel(BaseModel):
    state_machine_name: str = Field(alias="stateMachineName")
    role_arn: str = Field(alias="roleArn")
    execution_name_prefix: Optional[str] = Field(
        default=None, alias="executionNamePrefix"
    )


class MetricValueModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    cidrs: Optional[Sequence[str]] = Field(default=None, alias="cidrs")
    ports: Optional[Sequence[int]] = Field(default=None, alias="ports")
    number: Optional[float] = Field(default=None, alias="number")
    numbers: Optional[Sequence[float]] = Field(default=None, alias="numbers")
    strings: Optional[Sequence[str]] = Field(default=None, alias="strings")


class ViolationEventAdditionalInfoModel(BaseModel):
    confidence_level: Optional[Literal["HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="confidenceLevel"
    )


class AddThingToBillingGroupRequestModel(BaseModel):
    billing_group_name: Optional[str] = Field(default=None, alias="billingGroupName")
    billing_group_arn: Optional[str] = Field(default=None, alias="billingGroupArn")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")


class AddThingToThingGroupRequestModel(BaseModel):
    thing_group_name: Optional[str] = Field(default=None, alias="thingGroupName")
    thing_group_arn: Optional[str] = Field(default=None, alias="thingGroupArn")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")
    override_dynamic_groups: Optional[bool] = Field(
        default=None, alias="overrideDynamicGroups"
    )


class AddThingsToThingGroupParamsModel(BaseModel):
    thing_group_names: Sequence[str] = Field(alias="thingGroupNames")
    override_dynamic_groups: Optional[bool] = Field(
        default=None, alias="overrideDynamicGroups"
    )


class AggregationTypeModel(BaseModel):
    name: Literal["Cardinality", "Percentiles", "Statistics"] = Field(alias="name")
    values: Optional[Sequence[str]] = Field(default=None, alias="values")


class AlertTargetModel(BaseModel):
    alert_target_arn: str = Field(alias="alertTargetArn")
    role_arn: str = Field(alias="roleArn")


class PolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="policyName")
    policy_arn: Optional[str] = Field(default=None, alias="policyArn")


class AssetPropertyTimestampModel(BaseModel):
    time_in_seconds: str = Field(alias="timeInSeconds")
    offset_in_nanos: Optional[str] = Field(default=None, alias="offsetInNanos")


class AssetPropertyVariantModel(BaseModel):
    string_value: Optional[str] = Field(default=None, alias="stringValue")
    integer_value: Optional[str] = Field(default=None, alias="integerValue")
    double_value: Optional[str] = Field(default=None, alias="doubleValue")
    boolean_value: Optional[str] = Field(default=None, alias="booleanValue")


class AssociateTargetsWithJobRequestModel(BaseModel):
    targets: Sequence[str] = Field(alias="targets")
    job_id: str = Field(alias="jobId")
    comment: Optional[str] = Field(default=None, alias="comment")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AttachPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    target: str = Field(alias="target")


class AttachPrincipalPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    principal: str = Field(alias="principal")


class AttachSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    security_profile_target_arn: str = Field(alias="securityProfileTargetArn")


class AttachThingPrincipalRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    principal: str = Field(alias="principal")


class AttributePayloadModel(BaseModel):
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")
    merge: Optional[bool] = Field(default=None, alias="merge")


class AuditCheckConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")


class AuditCheckDetailsModel(BaseModel):
    check_run_status: Optional[
        Literal[
            "CANCELED",
            "COMPLETED_COMPLIANT",
            "COMPLETED_NON_COMPLIANT",
            "FAILED",
            "IN_PROGRESS",
            "WAITING_FOR_DATA_COLLECTION",
        ]
    ] = Field(default=None, alias="checkRunStatus")
    check_compliant: Optional[bool] = Field(default=None, alias="checkCompliant")
    total_resources_count: Optional[int] = Field(
        default=None, alias="totalResourcesCount"
    )
    non_compliant_resources_count: Optional[int] = Field(
        default=None, alias="nonCompliantResourcesCount"
    )
    suppressed_non_compliant_resources_count: Optional[int] = Field(
        default=None, alias="suppressedNonCompliantResourcesCount"
    )
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    message: Optional[str] = Field(default=None, alias="message")


class AuditMitigationActionExecutionMetadataModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    finding_id: Optional[str] = Field(default=None, alias="findingId")
    action_name: Optional[str] = Field(default=None, alias="actionName")
    action_id: Optional[str] = Field(default=None, alias="actionId")
    status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "SKIPPED"]
    ] = Field(default=None, alias="status")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    message: Optional[str] = Field(default=None, alias="message")


class AuditMitigationActionsTaskMetadataModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    task_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="taskStatus")


class AuditMitigationActionsTaskTargetModel(BaseModel):
    audit_task_id: Optional[str] = Field(default=None, alias="auditTaskId")
    finding_ids: Optional[List[str]] = Field(default=None, alias="findingIds")
    audit_check_to_reason_code_filter: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="auditCheckToReasonCodeFilter"
    )


class AuditNotificationTargetModel(BaseModel):
    target_arn: Optional[str] = Field(default=None, alias="targetArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    enabled: Optional[bool] = Field(default=None, alias="enabled")


class AuditTaskMetadataModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    task_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="taskStatus")
    task_type: Optional[
        Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"]
    ] = Field(default=None, alias="taskType")


class AuthInfoModel(BaseModel):
    resources: Sequence[str] = Field(alias="resources")
    action_type: Optional[
        Literal["CONNECT", "PUBLISH", "RECEIVE", "SUBSCRIBE"]
    ] = Field(default=None, alias="actionType")


class AuthorizerConfigModel(BaseModel):
    default_authorizer_name: Optional[str] = Field(
        default=None, alias="defaultAuthorizerName"
    )
    allow_authorizer_override: Optional[bool] = Field(
        default=None, alias="allowAuthorizerOverride"
    )


class AuthorizerDescriptionModel(BaseModel):
    authorizer_name: Optional[str] = Field(default=None, alias="authorizerName")
    authorizer_arn: Optional[str] = Field(default=None, alias="authorizerArn")
    authorizer_function_arn: Optional[str] = Field(
        default=None, alias="authorizerFunctionArn"
    )
    token_key_name: Optional[str] = Field(default=None, alias="tokenKeyName")
    token_signing_public_keys: Optional[Dict[str, str]] = Field(
        default=None, alias="tokenSigningPublicKeys"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    signing_disabled: Optional[bool] = Field(default=None, alias="signingDisabled")
    enable_caching_for_http: Optional[bool] = Field(
        default=None, alias="enableCachingForHttp"
    )


class AuthorizerSummaryModel(BaseModel):
    authorizer_name: Optional[str] = Field(default=None, alias="authorizerName")
    authorizer_arn: Optional[str] = Field(default=None, alias="authorizerArn")


class AwsJobAbortCriteriaModel(BaseModel):
    failure_type: Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"] = Field(
        alias="failureType"
    )
    action: Literal["CANCEL"] = Field(alias="action")
    threshold_percentage: float = Field(alias="thresholdPercentage")
    min_number_of_executed_things: int = Field(alias="minNumberOfExecutedThings")


class AwsJobRateIncreaseCriteriaModel(BaseModel):
    number_of_notified_things: Optional[int] = Field(
        default=None, alias="numberOfNotifiedThings"
    )
    number_of_succeeded_things: Optional[int] = Field(
        default=None, alias="numberOfSucceededThings"
    )


class AwsJobPresignedUrlConfigModel(BaseModel):
    expires_in_sec: Optional[int] = Field(default=None, alias="expiresInSec")


class AwsJobTimeoutConfigModel(BaseModel):
    in_progress_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="inProgressTimeoutInMinutes"
    )


class MachineLearningDetectionConfigModel(BaseModel):
    confidence_level: Literal["HIGH", "LOW", "MEDIUM"] = Field(alias="confidenceLevel")


class StatisticalThresholdModel(BaseModel):
    statistic: Optional[str] = Field(default=None, alias="statistic")


class BehaviorModelTrainingSummaryModel(BaseModel):
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior_name: Optional[str] = Field(default=None, alias="behaviorName")
    training_data_collection_start_date: Optional[datetime] = Field(
        default=None, alias="trainingDataCollectionStartDate"
    )
    model_status: Optional[Literal["ACTIVE", "EXPIRED", "PENDING_BUILD"]] = Field(
        default=None, alias="modelStatus"
    )
    datapoints_collection_percentage: Optional[float] = Field(
        default=None, alias="datapointsCollectionPercentage"
    )
    last_model_refresh_date: Optional[datetime] = Field(
        default=None, alias="lastModelRefreshDate"
    )


class MetricDimensionModel(BaseModel):
    dimension_name: str = Field(alias="dimensionName")
    operator: Optional[Literal["IN", "NOT_IN"]] = Field(default=None, alias="operator")


class BillingGroupMetadataModel(BaseModel):
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class BillingGroupPropertiesModel(BaseModel):
    billing_group_description: Optional[str] = Field(
        default=None, alias="billingGroupDescription"
    )


class BucketModel(BaseModel):
    key_value: Optional[str] = Field(default=None, alias="keyValue")
    count: Optional[int] = Field(default=None, alias="count")


class TermsAggregationModel(BaseModel):
    max_buckets: Optional[int] = Field(default=None, alias="maxBuckets")


class CertificateValidityModel(BaseModel):
    not_before: Optional[datetime] = Field(default=None, alias="notBefore")
    not_after: Optional[datetime] = Field(default=None, alias="notAfter")


class CACertificateModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_id: Optional[str] = Field(default=None, alias="certificateId")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class CancelAuditMitigationActionsTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class CancelAuditTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class CancelCertificateTransferRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")


class CancelDetectMitigationActionsTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class CancelJobExecutionRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    thing_name: str = Field(alias="thingName")
    force: Optional[bool] = Field(default=None, alias="force")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")
    status_details: Optional[Mapping[str, str]] = Field(
        default=None, alias="statusDetails"
    )


class CancelJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    reason_code: Optional[str] = Field(default=None, alias="reasonCode")
    comment: Optional[str] = Field(default=None, alias="comment")
    force: Optional[bool] = Field(default=None, alias="force")


class TransferDataModel(BaseModel):
    transfer_message: Optional[str] = Field(default=None, alias="transferMessage")
    reject_reason: Optional[str] = Field(default=None, alias="rejectReason")
    transfer_date: Optional[datetime] = Field(default=None, alias="transferDate")
    accept_date: Optional[datetime] = Field(default=None, alias="acceptDate")
    reject_date: Optional[datetime] = Field(default=None, alias="rejectDate")


class CertificateModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_id: Optional[str] = Field(default=None, alias="certificateId")
    status: Optional[
        Literal[
            "ACTIVE",
            "INACTIVE",
            "PENDING_ACTIVATION",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "REVOKED",
        ]
    ] = Field(default=None, alias="status")
    certificate_mode: Optional[Literal["DEFAULT", "SNI_ONLY"]] = Field(
        default=None, alias="certificateMode"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class CodeSigningCertificateChainModel(BaseModel):
    certificate_name: Optional[str] = Field(default=None, alias="certificateName")
    inline_document: Optional[str] = Field(default=None, alias="inlineDocument")


class CodeSigningSignatureModel(BaseModel):
    inline_document: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="inlineDocument")


class ConfigurationModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class ConfirmTopicRuleDestinationRequestModel(BaseModel):
    confirmation_token: str = Field(alias="confirmationToken")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class CreateCertificateFromCsrRequestModel(BaseModel):
    certificate_signing_request: str = Field(alias="certificateSigningRequest")
    set_as_active: Optional[bool] = Field(default=None, alias="setAsActive")


class PresignedUrlConfigModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    expires_in_sec: Optional[int] = Field(default=None, alias="expiresInSec")


class SchedulingConfigModel(BaseModel):
    start_time: Optional[str] = Field(default=None, alias="startTime")
    end_time: Optional[str] = Field(default=None, alias="endTime")
    end_behavior: Optional[Literal["CANCEL", "FORCE_CANCEL", "STOP_ROLLOUT"]] = Field(
        default=None, alias="endBehavior"
    )


class TimeoutConfigModel(BaseModel):
    in_progress_timeout_in_minutes: Optional[int] = Field(
        default=None, alias="inProgressTimeoutInMinutes"
    )


class CreateKeysAndCertificateRequestModel(BaseModel):
    set_as_active: Optional[bool] = Field(default=None, alias="setAsActive")


class KeyPairModel(BaseModel):
    public_key: Optional[str] = Field(default=None, alias="PublicKey")
    private_key: Optional[str] = Field(default=None, alias="PrivateKey")


class CreatePolicyVersionRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    policy_document: str = Field(alias="policyDocument")
    set_as_default: Optional[bool] = Field(default=None, alias="setAsDefault")


class CreateProvisioningClaimRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")


class ProvisioningHookModel(BaseModel):
    target_arn: str = Field(alias="targetArn")
    payload_version: Optional[str] = Field(default=None, alias="payloadVersion")


class CreateProvisioningTemplateVersionRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    template_body: str = Field(alias="templateBody")
    set_as_default: Optional[bool] = Field(default=None, alias="setAsDefault")


class ThingTypePropertiesModel(BaseModel):
    thing_type_description: Optional[str] = Field(
        default=None, alias="thingTypeDescription"
    )
    searchable_attributes: Optional[Sequence[str]] = Field(
        default=None, alias="searchableAttributes"
    )


class DeleteAccountAuditConfigurationRequestModel(BaseModel):
    delete_scheduled_audits: Optional[bool] = Field(
        default=None, alias="deleteScheduledAudits"
    )


class DeleteAuthorizerRequestModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")


class DeleteBillingGroupRequestModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class DeleteCACertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")


class DeleteCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")
    force_delete: Optional[bool] = Field(default=None, alias="forceDelete")


class DeleteCustomMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")


class DeleteDimensionRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteDomainConfigurationRequestModel(BaseModel):
    domain_configuration_name: str = Field(alias="domainConfigurationName")


class DeleteDynamicThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class DeleteFleetMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class DeleteJobExecutionRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    thing_name: str = Field(alias="thingName")
    execution_number: int = Field(alias="executionNumber")
    force: Optional[bool] = Field(default=None, alias="force")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")


class DeleteJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    force: Optional[bool] = Field(default=None, alias="force")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")


class DeleteJobTemplateRequestModel(BaseModel):
    job_template_id: str = Field(alias="jobTemplateId")


class DeleteMitigationActionRequestModel(BaseModel):
    action_name: str = Field(alias="actionName")


class DeleteOTAUpdateRequestModel(BaseModel):
    ota_update_id: str = Field(alias="otaUpdateId")
    delete_stream: Optional[bool] = Field(default=None, alias="deleteStream")
    force_delete_aws_job: Optional[bool] = Field(
        default=None, alias="forceDeleteAWSJob"
    )


class DeletePolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")


class DeletePolicyVersionRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    policy_version_id: str = Field(alias="policyVersionId")


class DeleteProvisioningTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")


class DeleteProvisioningTemplateVersionRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    version_id: int = Field(alias="versionId")


class DeleteRoleAliasRequestModel(BaseModel):
    role_alias: str = Field(alias="roleAlias")


class DeleteScheduledAuditRequestModel(BaseModel):
    scheduled_audit_name: str = Field(alias="scheduledAuditName")


class DeleteSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class DeleteStreamRequestModel(BaseModel):
    stream_id: str = Field(alias="streamId")


class DeleteThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class DeleteThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class DeleteThingTypeRequestModel(BaseModel):
    thing_type_name: str = Field(alias="thingTypeName")


class DeleteTopicRuleDestinationRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class DeleteTopicRuleRequestModel(BaseModel):
    rule_name: str = Field(alias="ruleName")


class DeleteV2LoggingLevelRequestModel(BaseModel):
    target_type: Literal[
        "CLIENT_ID", "DEFAULT", "PRINCIPAL_ID", "SOURCE_IP", "THING_GROUP"
    ] = Field(alias="targetType")
    target_name: str = Field(alias="targetName")


class DeprecateThingTypeRequestModel(BaseModel):
    thing_type_name: str = Field(alias="thingTypeName")
    undo_deprecate: Optional[bool] = Field(default=None, alias="undoDeprecate")


class DescribeAuditFindingRequestModel(BaseModel):
    finding_id: str = Field(alias="findingId")


class DescribeAuditMitigationActionsTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class TaskStatisticsForAuditCheckModel(BaseModel):
    total_findings_count: Optional[int] = Field(
        default=None, alias="totalFindingsCount"
    )
    failed_findings_count: Optional[int] = Field(
        default=None, alias="failedFindingsCount"
    )
    succeeded_findings_count: Optional[int] = Field(
        default=None, alias="succeededFindingsCount"
    )
    skipped_findings_count: Optional[int] = Field(
        default=None, alias="skippedFindingsCount"
    )
    canceled_findings_count: Optional[int] = Field(
        default=None, alias="canceledFindingsCount"
    )


class DescribeAuditTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class TaskStatisticsModel(BaseModel):
    total_checks: Optional[int] = Field(default=None, alias="totalChecks")
    in_progress_checks: Optional[int] = Field(default=None, alias="inProgressChecks")
    waiting_for_data_collection_checks: Optional[int] = Field(
        default=None, alias="waitingForDataCollectionChecks"
    )
    compliant_checks: Optional[int] = Field(default=None, alias="compliantChecks")
    non_compliant_checks: Optional[int] = Field(
        default=None, alias="nonCompliantChecks"
    )
    failed_checks: Optional[int] = Field(default=None, alias="failedChecks")
    canceled_checks: Optional[int] = Field(default=None, alias="canceledChecks")


class DescribeAuthorizerRequestModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")


class DescribeBillingGroupRequestModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")


class DescribeCACertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")


class RegistrationConfigModel(BaseModel):
    template_body: Optional[str] = Field(default=None, alias="templateBody")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    template_name: Optional[str] = Field(default=None, alias="templateName")


class DescribeCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")


class DescribeCustomMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")


class DescribeDetectMitigationActionsTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class DescribeDimensionRequestModel(BaseModel):
    name: str = Field(alias="name")


class DescribeDomainConfigurationRequestModel(BaseModel):
    domain_configuration_name: str = Field(alias="domainConfigurationName")


class ServerCertificateSummaryModel(BaseModel):
    server_certificate_arn: Optional[str] = Field(
        default=None, alias="serverCertificateArn"
    )
    server_certificate_status: Optional[Literal["INVALID", "VALID"]] = Field(
        default=None, alias="serverCertificateStatus"
    )
    server_certificate_status_detail: Optional[str] = Field(
        default=None, alias="serverCertificateStatusDetail"
    )


class DescribeEndpointRequestModel(BaseModel):
    endpoint_type: Optional[str] = Field(default=None, alias="endpointType")


class DescribeFleetMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")


class DescribeIndexRequestModel(BaseModel):
    index_name: str = Field(alias="indexName")


class DescribeJobExecutionRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    thing_name: str = Field(alias="thingName")
    execution_number: Optional[int] = Field(default=None, alias="executionNumber")


class DescribeJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class DescribeJobTemplateRequestModel(BaseModel):
    job_template_id: str = Field(alias="jobTemplateId")


class DescribeManagedJobTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    template_version: Optional[str] = Field(default=None, alias="templateVersion")


class DocumentParameterModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    description: Optional[str] = Field(default=None, alias="description")
    regex: Optional[str] = Field(default=None, alias="regex")
    example: Optional[str] = Field(default=None, alias="example")
    optional: Optional[bool] = Field(default=None, alias="optional")


class DescribeMitigationActionRequestModel(BaseModel):
    action_name: str = Field(alias="actionName")


class DescribeProvisioningTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")


class DescribeProvisioningTemplateVersionRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    version_id: int = Field(alias="versionId")


class DescribeRoleAliasRequestModel(BaseModel):
    role_alias: str = Field(alias="roleAlias")


class RoleAliasDescriptionModel(BaseModel):
    role_alias: Optional[str] = Field(default=None, alias="roleAlias")
    role_alias_arn: Optional[str] = Field(default=None, alias="roleAliasArn")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    owner: Optional[str] = Field(default=None, alias="owner")
    credential_duration_seconds: Optional[int] = Field(
        default=None, alias="credentialDurationSeconds"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )


class DescribeScheduledAuditRequestModel(BaseModel):
    scheduled_audit_name: str = Field(alias="scheduledAuditName")


class DescribeSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")


class DescribeStreamRequestModel(BaseModel):
    stream_id: str = Field(alias="streamId")


class DescribeThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")


class DescribeThingRegistrationTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class DescribeThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")


class DescribeThingTypeRequestModel(BaseModel):
    thing_type_name: str = Field(alias="thingTypeName")


class ThingTypeMetadataModel(BaseModel):
    deprecated: Optional[bool] = Field(default=None, alias="deprecated")
    deprecation_date: Optional[datetime] = Field(default=None, alias="deprecationDate")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class S3DestinationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    prefix: Optional[str] = Field(default=None, alias="prefix")


class DetachPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    target: str = Field(alias="target")


class DetachPrincipalPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    principal: str = Field(alias="principal")


class DetachSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    security_profile_target_arn: str = Field(alias="securityProfileTargetArn")


class DetachThingPrincipalRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    principal: str = Field(alias="principal")


class DetectMitigationActionExecutionModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    violation_id: Optional[str] = Field(default=None, alias="violationId")
    action_name: Optional[str] = Field(default=None, alias="actionName")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    execution_start_date: Optional[datetime] = Field(
        default=None, alias="executionStartDate"
    )
    execution_end_date: Optional[datetime] = Field(
        default=None, alias="executionEndDate"
    )
    status: Optional[Literal["FAILED", "IN_PROGRESS", "SKIPPED", "SUCCESSFUL"]] = Field(
        default=None, alias="status"
    )
    error_code: Optional[str] = Field(default=None, alias="errorCode")
    message: Optional[str] = Field(default=None, alias="message")


class DetectMitigationActionsTaskStatisticsModel(BaseModel):
    actions_executed: Optional[int] = Field(default=None, alias="actionsExecuted")
    actions_skipped: Optional[int] = Field(default=None, alias="actionsSkipped")
    actions_failed: Optional[int] = Field(default=None, alias="actionsFailed")


class DetectMitigationActionsTaskTargetModel(BaseModel):
    violation_ids: Optional[List[str]] = Field(default=None, alias="violationIds")
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior_name: Optional[str] = Field(default=None, alias="behaviorName")


class ViolationEventOccurrenceRangeModel(BaseModel):
    start_time: datetime = Field(alias="startTime")
    end_time: datetime = Field(alias="endTime")


class DisableTopicRuleRequestModel(BaseModel):
    rule_name: str = Field(alias="ruleName")


class DomainConfigurationSummaryModel(BaseModel):
    domain_configuration_name: Optional[str] = Field(
        default=None, alias="domainConfigurationName"
    )
    domain_configuration_arn: Optional[str] = Field(
        default=None, alias="domainConfigurationArn"
    )
    service_type: Optional[Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"]] = Field(
        default=None, alias="serviceType"
    )


class PutItemInputModel(BaseModel):
    table_name: str = Field(alias="tableName")


class EffectivePolicyModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="policyName")
    policy_arn: Optional[str] = Field(default=None, alias="policyArn")
    policy_document: Optional[str] = Field(default=None, alias="policyDocument")


class EnableIoTLoggingParamsModel(BaseModel):
    role_arn_for_logging: str = Field(alias="roleArnForLogging")
    log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"] = Field(
        alias="logLevel"
    )


class EnableTopicRuleRequestModel(BaseModel):
    rule_name: str = Field(alias="ruleName")


class ErrorInfoModel(BaseModel):
    code: Optional[str] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")


class RateIncreaseCriteriaModel(BaseModel):
    number_of_notified_things: Optional[int] = Field(
        default=None, alias="numberOfNotifiedThings"
    )
    number_of_succeeded_things: Optional[int] = Field(
        default=None, alias="numberOfSucceededThings"
    )


class FieldModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[Literal["Boolean", "Number", "String"]] = Field(
        default=None, alias="type"
    )


class S3LocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    key: Optional[str] = Field(default=None, alias="key")
    version: Optional[str] = Field(default=None, alias="version")


class StreamModel(BaseModel):
    stream_id: Optional[str] = Field(default=None, alias="streamId")
    file_id: Optional[int] = Field(default=None, alias="fileId")


class FleetMetricNameAndArnModel(BaseModel):
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    metric_arn: Optional[str] = Field(default=None, alias="metricArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class GetBehaviorModelTrainingSummariesRequestModel(BaseModel):
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetCardinalityRequestModel(BaseModel):
    query_string: str = Field(alias="queryString")
    index_name: Optional[str] = Field(default=None, alias="indexName")
    aggregation_field: Optional[str] = Field(default=None, alias="aggregationField")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")


class GetEffectivePoliciesRequestModel(BaseModel):
    principal: Optional[str] = Field(default=None, alias="principal")
    cognito_identity_pool_id: Optional[str] = Field(
        default=None, alias="cognitoIdentityPoolId"
    )
    thing_name: Optional[str] = Field(default=None, alias="thingName")


class GetJobDocumentRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")


class GetOTAUpdateRequestModel(BaseModel):
    ota_update_id: str = Field(alias="otaUpdateId")


class GetPercentilesRequestModel(BaseModel):
    query_string: str = Field(alias="queryString")
    index_name: Optional[str] = Field(default=None, alias="indexName")
    aggregation_field: Optional[str] = Field(default=None, alias="aggregationField")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")
    percents: Optional[Sequence[float]] = Field(default=None, alias="percents")


class PercentPairModel(BaseModel):
    percent: Optional[float] = Field(default=None, alias="percent")
    value: Optional[float] = Field(default=None, alias="value")


class GetPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")


class GetPolicyVersionRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    policy_version_id: str = Field(alias="policyVersionId")


class GetStatisticsRequestModel(BaseModel):
    query_string: str = Field(alias="queryString")
    index_name: Optional[str] = Field(default=None, alias="indexName")
    aggregation_field: Optional[str] = Field(default=None, alias="aggregationField")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")


class StatisticsModel(BaseModel):
    count: Optional[int] = Field(default=None, alias="count")
    average: Optional[float] = Field(default=None, alias="average")
    sum: Optional[float] = Field(default=None, alias="sum")
    minimum: Optional[float] = Field(default=None, alias="minimum")
    maximum: Optional[float] = Field(default=None, alias="maximum")
    sum_of_squares: Optional[float] = Field(default=None, alias="sumOfSquares")
    variance: Optional[float] = Field(default=None, alias="variance")
    std_deviation: Optional[float] = Field(default=None, alias="stdDeviation")


class GetTopicRuleDestinationRequestModel(BaseModel):
    arn: str = Field(alias="arn")


class GetTopicRuleRequestModel(BaseModel):
    rule_name: str = Field(alias="ruleName")


class GroupNameAndArnModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="groupName")
    group_arn: Optional[str] = Field(default=None, alias="groupArn")


class HttpActionHeaderModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class SigV4AuthorizationModel(BaseModel):
    signing_region: str = Field(alias="signingRegion")
    service_name: str = Field(alias="serviceName")
    role_arn: str = Field(alias="roleArn")


class HttpContextModel(BaseModel):
    headers: Optional[Mapping[str, str]] = Field(default=None, alias="headers")
    query_string: Optional[str] = Field(default=None, alias="queryString")


class HttpUrlDestinationConfigurationModel(BaseModel):
    confirmation_url: str = Field(alias="confirmationUrl")


class HttpUrlDestinationPropertiesModel(BaseModel):
    confirmation_url: Optional[str] = Field(default=None, alias="confirmationUrl")


class HttpUrlDestinationSummaryModel(BaseModel):
    confirmation_url: Optional[str] = Field(default=None, alias="confirmationUrl")


class IndexingFilterModel(BaseModel):
    named_shadow_names: Optional[List[str]] = Field(
        default=None, alias="namedShadowNames"
    )


class IssuerCertificateIdentifierModel(BaseModel):
    issuer_certificate_subject: Optional[str] = Field(
        default=None, alias="issuerCertificateSubject"
    )
    issuer_id: Optional[str] = Field(default=None, alias="issuerId")
    issuer_certificate_serial_number: Optional[str] = Field(
        default=None, alias="issuerCertificateSerialNumber"
    )


class JobExecutionStatusDetailsModel(BaseModel):
    details_map: Optional[Dict[str, str]] = Field(default=None, alias="detailsMap")


class JobExecutionSummaryModel(BaseModel):
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    queued_at: Optional[datetime] = Field(default=None, alias="queuedAt")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    execution_number: Optional[int] = Field(default=None, alias="executionNumber")
    retry_attempt: Optional[int] = Field(default=None, alias="retryAttempt")


class RetryCriteriaModel(BaseModel):
    failure_type: Literal["ALL", "FAILED", "TIMED_OUT"] = Field(alias="failureType")
    number_of_retries: int = Field(alias="numberOfRetries")


class JobProcessDetailsModel(BaseModel):
    processing_targets: Optional[List[str]] = Field(
        default=None, alias="processingTargets"
    )
    number_of_canceled_things: Optional[int] = Field(
        default=None, alias="numberOfCanceledThings"
    )
    number_of_succeeded_things: Optional[int] = Field(
        default=None, alias="numberOfSucceededThings"
    )
    number_of_failed_things: Optional[int] = Field(
        default=None, alias="numberOfFailedThings"
    )
    number_of_rejected_things: Optional[int] = Field(
        default=None, alias="numberOfRejectedThings"
    )
    number_of_queued_things: Optional[int] = Field(
        default=None, alias="numberOfQueuedThings"
    )
    number_of_in_progress_things: Optional[int] = Field(
        default=None, alias="numberOfInProgressThings"
    )
    number_of_removed_things: Optional[int] = Field(
        default=None, alias="numberOfRemovedThings"
    )
    number_of_timed_out_things: Optional[int] = Field(
        default=None, alias="numberOfTimedOutThings"
    )


class JobSummaryModel(BaseModel):
    job_arn: Optional[str] = Field(default=None, alias="jobArn")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    thing_group_id: Optional[str] = Field(default=None, alias="thingGroupId")
    target_selection: Optional[Literal["CONTINUOUS", "SNAPSHOT"]] = Field(
        default=None, alias="targetSelection"
    )
    status: Optional[
        Literal[
            "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS", "IN_PROGRESS", "SCHEDULED"
        ]
    ] = Field(default=None, alias="status")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    completed_at: Optional[datetime] = Field(default=None, alias="completedAt")
    is_concurrent: Optional[bool] = Field(default=None, alias="isConcurrent")


class JobTemplateSummaryModel(BaseModel):
    job_template_arn: Optional[str] = Field(default=None, alias="jobTemplateArn")
    job_template_id: Optional[str] = Field(default=None, alias="jobTemplateId")
    description: Optional[str] = Field(default=None, alias="description")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")


class ListActiveViolationsRequestModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior_criteria_type: Optional[
        Literal["MACHINE_LEARNING", "STATIC", "STATISTICAL"]
    ] = Field(default=None, alias="behaviorCriteriaType")
    list_suppressed_alerts: Optional[bool] = Field(
        default=None, alias="listSuppressedAlerts"
    )
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="verificationState")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAttachedPoliciesRequestModel(BaseModel):
    target: str = Field(alias="target")
    recursive: Optional[bool] = Field(default=None, alias="recursive")
    marker: Optional[str] = Field(default=None, alias="marker")
    page_size: Optional[int] = Field(default=None, alias="pageSize")


class ListAuditMitigationActionsExecutionsRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")
    finding_id: str = Field(alias="findingId")
    action_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "SKIPPED"]
    ] = Field(default=None, alias="actionStatus")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAuditMitigationActionsTasksRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    audit_task_id: Optional[str] = Field(default=None, alias="auditTaskId")
    finding_id: Optional[str] = Field(default=None, alias="findingId")
    task_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="taskStatus")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListAuditTasksRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    task_type: Optional[
        Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"]
    ] = Field(default=None, alias="taskType")
    task_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="taskStatus")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListAuthorizersRequestModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    marker: Optional[str] = Field(default=None, alias="marker")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )


class ListBillingGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    name_prefix_filter: Optional[str] = Field(default=None, alias="namePrefixFilter")


class ListCACertificatesRequestModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    marker: Optional[str] = Field(default=None, alias="marker")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    template_name: Optional[str] = Field(default=None, alias="templateName")


class ListCertificatesByCARequestModel(BaseModel):
    ca_certificate_id: str = Field(alias="caCertificateId")
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    marker: Optional[str] = Field(default=None, alias="marker")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class ListCertificatesRequestModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    marker: Optional[str] = Field(default=None, alias="marker")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class ListCustomMetricsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDetectMitigationActionsExecutionsRequestModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    violation_id: Optional[str] = Field(default=None, alias="violationId")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDetectMitigationActionsTasksRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListDimensionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListDomainConfigurationsRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="marker")
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    service_type: Optional[Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"]] = Field(
        default=None, alias="serviceType"
    )


class ListFleetMetricsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListIndicesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListJobExecutionsForJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListJobExecutionsForThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    job_id: Optional[str] = Field(default=None, alias="jobId")


class ListJobTemplatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListJobsRequestModel(BaseModel):
    status: Optional[
        Literal[
            "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS", "IN_PROGRESS", "SCHEDULED"
        ]
    ] = Field(default=None, alias="status")
    target_selection: Optional[Literal["CONTINUOUS", "SNAPSHOT"]] = Field(
        default=None, alias="targetSelection"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    thing_group_name: Optional[str] = Field(default=None, alias="thingGroupName")
    thing_group_id: Optional[str] = Field(default=None, alias="thingGroupId")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")


class ListManagedJobTemplatesRequestModel(BaseModel):
    template_name: Optional[str] = Field(default=None, alias="templateName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ManagedJobTemplateSummaryModel(BaseModel):
    template_arn: Optional[str] = Field(default=None, alias="templateArn")
    template_name: Optional[str] = Field(default=None, alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    environments: Optional[List[str]] = Field(default=None, alias="environments")
    template_version: Optional[str] = Field(default=None, alias="templateVersion")


class ListMetricValuesRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    metric_name: str = Field(alias="metricName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    dimension_name: Optional[str] = Field(default=None, alias="dimensionName")
    dimension_value_operator: Optional[Literal["IN", "NOT_IN"]] = Field(
        default=None, alias="dimensionValueOperator"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListMitigationActionsRequestModel(BaseModel):
    action_type: Optional[
        Literal[
            "ADD_THINGS_TO_THING_GROUP",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "UPDATE_CA_CERTIFICATE",
            "UPDATE_DEVICE_CERTIFICATE",
        ]
    ] = Field(default=None, alias="actionType")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class MitigationActionIdentifierModel(BaseModel):
    action_name: Optional[str] = Field(default=None, alias="actionName")
    action_arn: Optional[str] = Field(default=None, alias="actionArn")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class ListOTAUpdatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    ota_update_status: Optional[
        Literal[
            "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_PENDING"
        ]
    ] = Field(default=None, alias="otaUpdateStatus")


class OTAUpdateSummaryModel(BaseModel):
    ota_update_id: Optional[str] = Field(default=None, alias="otaUpdateId")
    ota_update_arn: Optional[str] = Field(default=None, alias="otaUpdateArn")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class ListOutgoingCertificatesRequestModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    marker: Optional[str] = Field(default=None, alias="marker")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class OutgoingCertificateModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_id: Optional[str] = Field(default=None, alias="certificateId")
    transferred_to: Optional[str] = Field(default=None, alias="transferredTo")
    transfer_date: Optional[datetime] = Field(default=None, alias="transferDate")
    transfer_message: Optional[str] = Field(default=None, alias="transferMessage")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class ListPoliciesRequestModel(BaseModel):
    marker: Optional[str] = Field(default=None, alias="marker")
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class ListPolicyPrincipalsRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    marker: Optional[str] = Field(default=None, alias="marker")
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class ListPolicyVersionsRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")


class PolicyVersionModel(BaseModel):
    version_id: Optional[str] = Field(default=None, alias="versionId")
    is_default_version: Optional[bool] = Field(default=None, alias="isDefaultVersion")
    create_date: Optional[datetime] = Field(default=None, alias="createDate")


class ListPrincipalPoliciesRequestModel(BaseModel):
    principal: str = Field(alias="principal")
    marker: Optional[str] = Field(default=None, alias="marker")
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class ListPrincipalThingsRequestModel(BaseModel):
    principal: str = Field(alias="principal")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListProvisioningTemplateVersionsRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ProvisioningTemplateVersionSummaryModel(BaseModel):
    version_id: Optional[int] = Field(default=None, alias="versionId")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    is_default_version: Optional[bool] = Field(default=None, alias="isDefaultVersion")


class ListProvisioningTemplatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ProvisioningTemplateSummaryModel(BaseModel):
    template_arn: Optional[str] = Field(default=None, alias="templateArn")
    template_name: Optional[str] = Field(default=None, alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    type: Optional[Literal["FLEET_PROVISIONING", "JITP"]] = Field(
        default=None, alias="type"
    )


class ListRelatedResourcesForAuditFindingRequestModel(BaseModel):
    finding_id: str = Field(alias="findingId")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListRoleAliasesRequestModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    marker: Optional[str] = Field(default=None, alias="marker")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class ListScheduledAuditsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ScheduledAuditMetadataModel(BaseModel):
    scheduled_audit_name: Optional[str] = Field(
        default=None, alias="scheduledAuditName"
    )
    scheduled_audit_arn: Optional[str] = Field(default=None, alias="scheduledAuditArn")
    frequency: Optional[Literal["BIWEEKLY", "DAILY", "MONTHLY", "WEEKLY"]] = Field(
        default=None, alias="frequency"
    )
    day_of_month: Optional[str] = Field(default=None, alias="dayOfMonth")
    day_of_week: Optional[
        Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"]
    ] = Field(default=None, alias="dayOfWeek")


class ListSecurityProfilesForTargetRequestModel(BaseModel):
    security_profile_target_arn: str = Field(alias="securityProfileTargetArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    recursive: Optional[bool] = Field(default=None, alias="recursive")


class ListSecurityProfilesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    dimension_name: Optional[str] = Field(default=None, alias="dimensionName")
    metric_name: Optional[str] = Field(default=None, alias="metricName")


class SecurityProfileIdentifierModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")


class ListStreamsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")


class StreamSummaryModel(BaseModel):
    stream_id: Optional[str] = Field(default=None, alias="streamId")
    stream_arn: Optional[str] = Field(default=None, alias="streamArn")
    stream_version: Optional[int] = Field(default=None, alias="streamVersion")
    description: Optional[str] = Field(default=None, alias="description")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTargetsForPolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    marker: Optional[str] = Field(default=None, alias="marker")
    page_size: Optional[int] = Field(default=None, alias="pageSize")


class ListTargetsForSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class SecurityProfileTargetModel(BaseModel):
    arn: str = Field(alias="arn")


class ListThingGroupsForThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListThingGroupsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    parent_group: Optional[str] = Field(default=None, alias="parentGroup")
    name_prefix_filter: Optional[str] = Field(default=None, alias="namePrefixFilter")
    recursive: Optional[bool] = Field(default=None, alias="recursive")


class ListThingPrincipalsRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListThingRegistrationTaskReportsRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")
    report_type: Literal["ERRORS", "RESULTS"] = Field(alias="reportType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListThingRegistrationTasksRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    status: Optional[
        Literal["Cancelled", "Cancelling", "Completed", "Failed", "InProgress"]
    ] = Field(default=None, alias="status")


class ListThingTypesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")


class ListThingsInBillingGroupRequestModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListThingsInThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    recursive: Optional[bool] = Field(default=None, alias="recursive")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListThingsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    attribute_name: Optional[str] = Field(default=None, alias="attributeName")
    attribute_value: Optional[str] = Field(default=None, alias="attributeValue")
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    use_prefix_attribute_value: Optional[bool] = Field(
        default=None, alias="usePrefixAttributeValue"
    )


class ThingAttributeModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="attributes")
    version: Optional[int] = Field(default=None, alias="version")


class ListTopicRuleDestinationsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTopicRulesRequestModel(BaseModel):
    topic: Optional[str] = Field(default=None, alias="topic")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    rule_disabled: Optional[bool] = Field(default=None, alias="ruleDisabled")


class TopicRuleListItemModel(BaseModel):
    rule_arn: Optional[str] = Field(default=None, alias="ruleArn")
    rule_name: Optional[str] = Field(default=None, alias="ruleName")
    topic_pattern: Optional[str] = Field(default=None, alias="topicPattern")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    rule_disabled: Optional[bool] = Field(default=None, alias="ruleDisabled")


class ListV2LoggingLevelsRequestModel(BaseModel):
    target_type: Optional[
        Literal["CLIENT_ID", "DEFAULT", "PRINCIPAL_ID", "SOURCE_IP", "THING_GROUP"]
    ] = Field(default=None, alias="targetType")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class ListViolationEventsRequestModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior_criteria_type: Optional[
        Literal["MACHINE_LEARNING", "STATIC", "STATISTICAL"]
    ] = Field(default=None, alias="behaviorCriteriaType")
    list_suppressed_alerts: Optional[bool] = Field(
        default=None, alias="listSuppressedAlerts"
    )
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="verificationState")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class LocationTimestampModel(BaseModel):
    value: str = Field(alias="value")
    unit: Optional[str] = Field(default=None, alias="unit")


class LogTargetModel(BaseModel):
    target_type: Literal[
        "CLIENT_ID", "DEFAULT", "PRINCIPAL_ID", "SOURCE_IP", "THING_GROUP"
    ] = Field(alias="targetType")
    target_name: Optional[str] = Field(default=None, alias="targetName")


class LoggingOptionsPayloadModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    log_level: Optional[Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="logLevel"
    )


class PublishFindingToSnsParamsModel(BaseModel):
    topic_arn: str = Field(alias="topicArn")


class ReplaceDefaultPolicyVersionParamsModel(BaseModel):
    template_name: Literal["BLANK_POLICY"] = Field(alias="templateName")


class UpdateCACertificateParamsModel(BaseModel):
    action: Literal["DEACTIVATE"] = Field(alias="action")


class UpdateDeviceCertificateParamsModel(BaseModel):
    action: Literal["DEACTIVATE"] = Field(alias="action")


class MqttContextModel(BaseModel):
    username: Optional[str] = Field(default=None, alias="username")
    password: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="password"
    )
    client_id: Optional[str] = Field(default=None, alias="clientId")


class UserPropertyModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class PolicyVersionIdentifierModel(BaseModel):
    policy_name: Optional[str] = Field(default=None, alias="policyName")
    policy_version_id: Optional[str] = Field(default=None, alias="policyVersionId")


class PutVerificationStateOnViolationRequestModel(BaseModel):
    violation_id: str = Field(alias="violationId")
    verification_state: Literal[
        "BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"
    ] = Field(alias="verificationState")
    verification_state_description: Optional[str] = Field(
        default=None, alias="verificationStateDescription"
    )


class RegisterCertificateRequestModel(BaseModel):
    certificate_pem: str = Field(alias="certificatePem")
    ca_certificate_pem: Optional[str] = Field(default=None, alias="caCertificatePem")
    set_as_active: Optional[bool] = Field(default=None, alias="setAsActive")
    status: Optional[
        Literal[
            "ACTIVE",
            "INACTIVE",
            "PENDING_ACTIVATION",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "REVOKED",
        ]
    ] = Field(default=None, alias="status")


class RegisterCertificateWithoutCARequestModel(BaseModel):
    certificate_pem: str = Field(alias="certificatePem")
    status: Optional[
        Literal[
            "ACTIVE",
            "INACTIVE",
            "PENDING_ACTIVATION",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "REVOKED",
        ]
    ] = Field(default=None, alias="status")


class RegisterThingRequestModel(BaseModel):
    template_body: str = Field(alias="templateBody")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="parameters")


class RejectCertificateTransferRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")
    reject_reason: Optional[str] = Field(default=None, alias="rejectReason")


class RemoveThingFromBillingGroupRequestModel(BaseModel):
    billing_group_name: Optional[str] = Field(default=None, alias="billingGroupName")
    billing_group_arn: Optional[str] = Field(default=None, alias="billingGroupArn")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")


class RemoveThingFromThingGroupRequestModel(BaseModel):
    thing_group_name: Optional[str] = Field(default=None, alias="thingGroupName")
    thing_group_arn: Optional[str] = Field(default=None, alias="thingGroupArn")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")


class SearchIndexRequestModel(BaseModel):
    query_string: str = Field(alias="queryString")
    index_name: Optional[str] = Field(default=None, alias="indexName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")


class ThingGroupDocumentModel(BaseModel):
    thing_group_name: Optional[str] = Field(default=None, alias="thingGroupName")
    thing_group_id: Optional[str] = Field(default=None, alias="thingGroupId")
    thing_group_description: Optional[str] = Field(
        default=None, alias="thingGroupDescription"
    )
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="attributes")
    parent_group_names: Optional[List[str]] = Field(
        default=None, alias="parentGroupNames"
    )


class SetDefaultAuthorizerRequestModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")


class SetDefaultPolicyVersionRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    policy_version_id: str = Field(alias="policyVersionId")


class SetV2LoggingOptionsRequestModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    default_log_level: Optional[
        Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"]
    ] = Field(default=None, alias="defaultLogLevel")
    disable_all_logs: Optional[bool] = Field(default=None, alias="disableAllLogs")


class SigningProfileParameterModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    platform: Optional[str] = Field(default=None, alias="platform")
    certificate_path_on_device: Optional[str] = Field(
        default=None, alias="certificatePathOnDevice"
    )


class StartOnDemandAuditTaskRequestModel(BaseModel):
    target_check_names: Sequence[str] = Field(alias="targetCheckNames")


class StartThingRegistrationTaskRequestModel(BaseModel):
    template_body: str = Field(alias="templateBody")
    input_file_bucket: str = Field(alias="inputFileBucket")
    input_file_key: str = Field(alias="inputFileKey")
    role_arn: str = Field(alias="roleArn")


class StopThingRegistrationTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")


class TlsContextModel(BaseModel):
    server_name: Optional[str] = Field(default=None, alias="serverName")


class ThingConnectivityModel(BaseModel):
    connected: Optional[bool] = Field(default=None, alias="connected")
    timestamp: Optional[int] = Field(default=None, alias="timestamp")
    disconnect_reason: Optional[str] = Field(default=None, alias="disconnectReason")


class TimestreamDimensionModel(BaseModel):
    name: str = Field(alias="name")
    value: str = Field(alias="value")


class TimestreamTimestampModel(BaseModel):
    value: str = Field(alias="value")
    unit: str = Field(alias="unit")


class VpcDestinationConfigurationModel(BaseModel):
    subnet_ids: Sequence[str] = Field(alias="subnetIds")
    vpc_id: str = Field(alias="vpcId")
    role_arn: str = Field(alias="roleArn")
    security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroups"
    )


class VpcDestinationSummaryModel(BaseModel):
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    security_groups: Optional[List[str]] = Field(default=None, alias="securityGroups")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class VpcDestinationPropertiesModel(BaseModel):
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    security_groups: Optional[List[str]] = Field(default=None, alias="securityGroups")
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class TransferCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")
    target_aws_account: str = Field(alias="targetAwsAccount")
    transfer_message: Optional[str] = Field(default=None, alias="transferMessage")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAuthorizerRequestModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")
    authorizer_function_arn: Optional[str] = Field(
        default=None, alias="authorizerFunctionArn"
    )
    token_key_name: Optional[str] = Field(default=None, alias="tokenKeyName")
    token_signing_public_keys: Optional[Mapping[str, str]] = Field(
        default=None, alias="tokenSigningPublicKeys"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    enable_caching_for_http: Optional[bool] = Field(
        default=None, alias="enableCachingForHttp"
    )


class UpdateCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")
    new_status: Literal[
        "ACTIVE",
        "INACTIVE",
        "PENDING_ACTIVATION",
        "PENDING_TRANSFER",
        "REGISTER_INACTIVE",
        "REVOKED",
    ] = Field(alias="newStatus")


class UpdateCustomMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    display_name: str = Field(alias="displayName")


class UpdateDimensionRequestModel(BaseModel):
    name: str = Field(alias="name")
    string_values: Sequence[str] = Field(alias="stringValues")


class UpdateRoleAliasRequestModel(BaseModel):
    role_alias: str = Field(alias="roleAlias")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    credential_duration_seconds: Optional[int] = Field(
        default=None, alias="credentialDurationSeconds"
    )


class UpdateScheduledAuditRequestModel(BaseModel):
    scheduled_audit_name: str = Field(alias="scheduledAuditName")
    frequency: Optional[Literal["BIWEEKLY", "DAILY", "MONTHLY", "WEEKLY"]] = Field(
        default=None, alias="frequency"
    )
    day_of_month: Optional[str] = Field(default=None, alias="dayOfMonth")
    day_of_week: Optional[
        Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"]
    ] = Field(default=None, alias="dayOfWeek")
    target_check_names: Optional[Sequence[str]] = Field(
        default=None, alias="targetCheckNames"
    )


class UpdateThingGroupsForThingRequestModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    thing_groups_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="thingGroupsToAdd"
    )
    thing_groups_to_remove: Optional[Sequence[str]] = Field(
        default=None, alias="thingGroupsToRemove"
    )
    override_dynamic_groups: Optional[bool] = Field(
        default=None, alias="overrideDynamicGroups"
    )


class UpdateTopicRuleDestinationRequestModel(BaseModel):
    arn: str = Field(alias="arn")
    status: Literal["DELETING", "DISABLED", "ENABLED", "ERROR", "IN_PROGRESS"] = Field(
        alias="status"
    )


class ValidationErrorModel(BaseModel):
    error_message: Optional[str] = Field(default=None, alias="errorMessage")


class AbortConfigModel(BaseModel):
    criteria_list: Sequence[AbortCriteriaModel] = Field(alias="criteriaList")


class MetricDatumModel(BaseModel):
    timestamp: Optional[datetime] = Field(default=None, alias="timestamp")
    value: Optional[MetricValueModel] = Field(default=None, alias="value")


class UpdateFleetMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    index_name: str = Field(alias="indexName")
    query_string: Optional[str] = Field(default=None, alias="queryString")
    aggregation_type: Optional[AggregationTypeModel] = Field(
        default=None, alias="aggregationType"
    )
    period: Optional[int] = Field(default=None, alias="period")
    aggregation_field: Optional[str] = Field(default=None, alias="aggregationField")
    description: Optional[str] = Field(default=None, alias="description")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="unit")
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class AllowedModel(BaseModel):
    policies: Optional[List[PolicyModel]] = Field(default=None, alias="policies")


class ExplicitDenyModel(BaseModel):
    policies: Optional[List[PolicyModel]] = Field(default=None, alias="policies")


class ImplicitDenyModel(BaseModel):
    policies: Optional[List[PolicyModel]] = Field(default=None, alias="policies")


class AssetPropertyValueModel(BaseModel):
    value: AssetPropertyVariantModel = Field(alias="value")
    timestamp: AssetPropertyTimestampModel = Field(alias="timestamp")
    quality: Optional[str] = Field(default=None, alias="quality")


class AssociateTargetsWithJobResponseModel(BaseModel):
    job_arn: str = Field(alias="jobArn")
    job_id: str = Field(alias="jobId")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CancelJobResponseModel(BaseModel):
    job_arn: str = Field(alias="jobArn")
    job_id: str = Field(alias="jobId")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAuthorizerResponseModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")
    authorizer_arn: str = Field(alias="authorizerArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateBillingGroupResponseModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")
    billing_group_arn: str = Field(alias="billingGroupArn")
    billing_group_id: str = Field(alias="billingGroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCertificateFromCsrResponseModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")
    certificate_id: str = Field(alias="certificateId")
    certificate_pem: str = Field(alias="certificatePem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomMetricResponseModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    metric_arn: str = Field(alias="metricArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDimensionResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDomainConfigurationResponseModel(BaseModel):
    domain_configuration_name: str = Field(alias="domainConfigurationName")
    domain_configuration_arn: str = Field(alias="domainConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDynamicThingGroupResponseModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    thing_group_arn: str = Field(alias="thingGroupArn")
    thing_group_id: str = Field(alias="thingGroupId")
    index_name: str = Field(alias="indexName")
    query_string: str = Field(alias="queryString")
    query_version: str = Field(alias="queryVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFleetMetricResponseModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    metric_arn: str = Field(alias="metricArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobResponseModel(BaseModel):
    job_arn: str = Field(alias="jobArn")
    job_id: str = Field(alias="jobId")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobTemplateResponseModel(BaseModel):
    job_template_arn: str = Field(alias="jobTemplateArn")
    job_template_id: str = Field(alias="jobTemplateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMitigationActionResponseModel(BaseModel):
    action_arn: str = Field(alias="actionArn")
    action_id: str = Field(alias="actionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateOTAUpdateResponseModel(BaseModel):
    ota_update_id: str = Field(alias="otaUpdateId")
    aws_iot_job_id: str = Field(alias="awsIotJobId")
    ota_update_arn: str = Field(alias="otaUpdateArn")
    aws_iot_job_arn: str = Field(alias="awsIotJobArn")
    ota_update_status: Literal[
        "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_PENDING"
    ] = Field(alias="otaUpdateStatus")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePolicyResponseModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    policy_arn: str = Field(alias="policyArn")
    policy_document: str = Field(alias="policyDocument")
    policy_version_id: str = Field(alias="policyVersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreatePolicyVersionResponseModel(BaseModel):
    policy_arn: str = Field(alias="policyArn")
    policy_document: str = Field(alias="policyDocument")
    policy_version_id: str = Field(alias="policyVersionId")
    is_default_version: bool = Field(alias="isDefaultVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProvisioningTemplateResponseModel(BaseModel):
    template_arn: str = Field(alias="templateArn")
    template_name: str = Field(alias="templateName")
    default_version_id: int = Field(alias="defaultVersionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProvisioningTemplateVersionResponseModel(BaseModel):
    template_arn: str = Field(alias="templateArn")
    template_name: str = Field(alias="templateName")
    version_id: int = Field(alias="versionId")
    is_default_version: bool = Field(alias="isDefaultVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRoleAliasResponseModel(BaseModel):
    role_alias: str = Field(alias="roleAlias")
    role_alias_arn: str = Field(alias="roleAliasArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateScheduledAuditResponseModel(BaseModel):
    scheduled_audit_arn: str = Field(alias="scheduledAuditArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSecurityProfileResponseModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    security_profile_arn: str = Field(alias="securityProfileArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamResponseModel(BaseModel):
    stream_id: str = Field(alias="streamId")
    stream_arn: str = Field(alias="streamArn")
    description: str = Field(alias="description")
    stream_version: int = Field(alias="streamVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThingGroupResponseModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    thing_group_arn: str = Field(alias="thingGroupArn")
    thing_group_id: str = Field(alias="thingGroupId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThingResponseModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    thing_arn: str = Field(alias="thingArn")
    thing_id: str = Field(alias="thingId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThingTypeResponseModel(BaseModel):
    thing_type_name: str = Field(alias="thingTypeName")
    thing_type_arn: str = Field(alias="thingTypeArn")
    thing_type_id: str = Field(alias="thingTypeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomMetricResponseModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    metric_arn: str = Field(alias="metricArn")
    metric_type: Literal[
        "ip-address-list", "number", "number-list", "string-list"
    ] = Field(alias="metricType")
    display_name: str = Field(alias="displayName")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDimensionResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    type: Literal["TOPIC_FILTER"] = Field(alias="type")
    string_values: List[str] = Field(alias="stringValues")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeEndpointResponseModel(BaseModel):
    endpoint_address: str = Field(alias="endpointAddress")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFleetMetricResponseModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    query_string: str = Field(alias="queryString")
    aggregation_type: AggregationTypeModel = Field(alias="aggregationType")
    period: int = Field(alias="period")
    aggregation_field: str = Field(alias="aggregationField")
    description: str = Field(alias="description")
    query_version: str = Field(alias="queryVersion")
    index_name: str = Field(alias="indexName")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    unit: Literal[
        "Bits",
        "Bits/Second",
        "Bytes",
        "Bytes/Second",
        "Count",
        "Count/Second",
        "Gigabits",
        "Gigabits/Second",
        "Gigabytes",
        "Gigabytes/Second",
        "Kilobits",
        "Kilobits/Second",
        "Kilobytes",
        "Kilobytes/Second",
        "Megabits",
        "Megabits/Second",
        "Megabytes",
        "Megabytes/Second",
        "Microseconds",
        "Milliseconds",
        "None",
        "Percent",
        "Seconds",
        "Terabits",
        "Terabits/Second",
        "Terabytes",
        "Terabytes/Second",
    ] = Field(alias="unit")
    version: int = Field(alias="version")
    metric_arn: str = Field(alias="metricArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIndexResponseModel(BaseModel):
    index_name: str = Field(alias="indexName")
    index_status: Literal["ACTIVE", "BUILDING", "REBUILDING"] = Field(
        alias="indexStatus"
    )
    schema_: str = Field(alias="schema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProvisioningTemplateVersionResponseModel(BaseModel):
    version_id: int = Field(alias="versionId")
    creation_date: datetime = Field(alias="creationDate")
    template_body: str = Field(alias="templateBody")
    is_default_version: bool = Field(alias="isDefaultVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeScheduledAuditResponseModel(BaseModel):
    frequency: Literal["BIWEEKLY", "DAILY", "MONTHLY", "WEEKLY"] = Field(
        alias="frequency"
    )
    day_of_month: str = Field(alias="dayOfMonth")
    day_of_week: Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"] = Field(
        alias="dayOfWeek"
    )
    target_check_names: List[str] = Field(alias="targetCheckNames")
    scheduled_audit_name: str = Field(alias="scheduledAuditName")
    scheduled_audit_arn: str = Field(alias="scheduledAuditArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeThingRegistrationTaskResponseModel(BaseModel):
    task_id: str = Field(alias="taskId")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    template_body: str = Field(alias="templateBody")
    input_file_bucket: str = Field(alias="inputFileBucket")
    input_file_key: str = Field(alias="inputFileKey")
    role_arn: str = Field(alias="roleArn")
    status: Literal[
        "Cancelled", "Cancelling", "Completed", "Failed", "InProgress"
    ] = Field(alias="status")
    message: str = Field(alias="message")
    success_count: int = Field(alias="successCount")
    failure_count: int = Field(alias="failureCount")
    percentage_progress: int = Field(alias="percentageProgress")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeThingResponseModel(BaseModel):
    default_client_id: str = Field(alias="defaultClientId")
    thing_name: str = Field(alias="thingName")
    thing_id: str = Field(alias="thingId")
    thing_arn: str = Field(alias="thingArn")
    thing_type_name: str = Field(alias="thingTypeName")
    attributes: Dict[str, str] = Field(alias="attributes")
    version: int = Field(alias="version")
    billing_group_name: str = Field(alias="billingGroupName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCardinalityResponseModel(BaseModel):
    cardinality: int = Field(alias="cardinality")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobDocumentResponseModel(BaseModel):
    document: str = Field(alias="document")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLoggingOptionsResponseModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"] = Field(
        alias="logLevel"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPolicyResponseModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    policy_arn: str = Field(alias="policyArn")
    policy_document: str = Field(alias="policyDocument")
    default_version_id: str = Field(alias="defaultVersionId")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    generation_id: str = Field(alias="generationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPolicyVersionResponseModel(BaseModel):
    policy_arn: str = Field(alias="policyArn")
    policy_name: str = Field(alias="policyName")
    policy_document: str = Field(alias="policyDocument")
    policy_version_id: str = Field(alias="policyVersionId")
    is_default_version: bool = Field(alias="isDefaultVersion")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    generation_id: str = Field(alias="generationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegistrationCodeResponseModel(BaseModel):
    registration_code: str = Field(alias="registrationCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetV2LoggingOptionsResponseModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    default_log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"] = Field(
        alias="defaultLogLevel"
    )
    disable_all_logs: bool = Field(alias="disableAllLogs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAttachedPoliciesResponseModel(BaseModel):
    policies: List[PolicyModel] = Field(alias="policies")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCustomMetricsResponseModel(BaseModel):
    metric_names: List[str] = Field(alias="metricNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDimensionsResponseModel(BaseModel):
    dimension_names: List[str] = Field(alias="dimensionNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIndicesResponseModel(BaseModel):
    index_names: List[str] = Field(alias="indexNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPoliciesResponseModel(BaseModel):
    policies: List[PolicyModel] = Field(alias="policies")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPolicyPrincipalsResponseModel(BaseModel):
    principals: List[str] = Field(alias="principals")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPrincipalPoliciesResponseModel(BaseModel):
    policies: List[PolicyModel] = Field(alias="policies")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPrincipalThingsResponseModel(BaseModel):
    things: List[str] = Field(alias="things")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoleAliasesResponseModel(BaseModel):
    role_aliases: List[str] = Field(alias="roleAliases")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTargetsForPolicyResponseModel(BaseModel):
    targets: List[str] = Field(alias="targets")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingPrincipalsResponseModel(BaseModel):
    principals: List[str] = Field(alias="principals")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingRegistrationTaskReportsResponseModel(BaseModel):
    resource_links: List[str] = Field(alias="resourceLinks")
    report_type: Literal["ERRORS", "RESULTS"] = Field(alias="reportType")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingRegistrationTasksResponseModel(BaseModel):
    task_ids: List[str] = Field(alias="taskIds")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingsInBillingGroupResponseModel(BaseModel):
    things: List[str] = Field(alias="things")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingsInThingGroupResponseModel(BaseModel):
    things: List[str] = Field(alias="things")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterCACertificateResponseModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")
    certificate_id: str = Field(alias="certificateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterCertificateResponseModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")
    certificate_id: str = Field(alias="certificateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterCertificateWithoutCAResponseModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")
    certificate_id: str = Field(alias="certificateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterThingResponseModel(BaseModel):
    certificate_pem: str = Field(alias="certificatePem")
    resource_arns: Dict[str, str] = Field(alias="resourceArns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SetDefaultAuthorizerResponseModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")
    authorizer_arn: str = Field(alias="authorizerArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAuditMitigationActionsTaskResponseModel(BaseModel):
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDetectMitigationActionsTaskResponseModel(BaseModel):
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartOnDemandAuditTaskResponseModel(BaseModel):
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartThingRegistrationTaskResponseModel(BaseModel):
    task_id: str = Field(alias="taskId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestInvokeAuthorizerResponseModel(BaseModel):
    is_authenticated: bool = Field(alias="isAuthenticated")
    principal_id: str = Field(alias="principalId")
    policy_documents: List[str] = Field(alias="policyDocuments")
    refresh_after_in_seconds: int = Field(alias="refreshAfterInSeconds")
    disconnect_after_in_seconds: int = Field(alias="disconnectAfterInSeconds")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TransferCertificateResponseModel(BaseModel):
    transferred_certificate_arn: str = Field(alias="transferredCertificateArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAuthorizerResponseModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")
    authorizer_arn: str = Field(alias="authorizerArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBillingGroupResponseModel(BaseModel):
    version: int = Field(alias="version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCustomMetricResponseModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    metric_arn: str = Field(alias="metricArn")
    metric_type: Literal[
        "ip-address-list", "number", "number-list", "string-list"
    ] = Field(alias="metricType")
    display_name: str = Field(alias="displayName")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDimensionResponseModel(BaseModel):
    name: str = Field(alias="name")
    arn: str = Field(alias="arn")
    type: Literal["TOPIC_FILTER"] = Field(alias="type")
    string_values: List[str] = Field(alias="stringValues")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainConfigurationResponseModel(BaseModel):
    domain_configuration_name: str = Field(alias="domainConfigurationName")
    domain_configuration_arn: str = Field(alias="domainConfigurationArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDynamicThingGroupResponseModel(BaseModel):
    version: int = Field(alias="version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateMitigationActionResponseModel(BaseModel):
    action_arn: str = Field(alias="actionArn")
    action_id: str = Field(alias="actionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRoleAliasResponseModel(BaseModel):
    role_alias: str = Field(alias="roleAlias")
    role_alias_arn: str = Field(alias="roleAliasArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateScheduledAuditResponseModel(BaseModel):
    scheduled_audit_arn: str = Field(alias="scheduledAuditArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateStreamResponseModel(BaseModel):
    stream_id: str = Field(alias="streamId")
    stream_arn: str = Field(alias="streamArn")
    description: str = Field(alias="description")
    stream_version: int = Field(alias="streamVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateThingGroupResponseModel(BaseModel):
    version: int = Field(alias="version")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    attribute_payload: Optional[AttributePayloadModel] = Field(
        default=None, alias="attributePayload"
    )
    billing_group_name: Optional[str] = Field(default=None, alias="billingGroupName")


class ThingGroupPropertiesModel(BaseModel):
    thing_group_description: Optional[str] = Field(
        default=None, alias="thingGroupDescription"
    )
    attribute_payload: Optional[AttributePayloadModel] = Field(
        default=None, alias="attributePayload"
    )


class UpdateThingRequestModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    attribute_payload: Optional[AttributePayloadModel] = Field(
        default=None, alias="attributePayload"
    )
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")
    remove_thing_type: Optional[bool] = Field(default=None, alias="removeThingType")


class ListAuditMitigationActionsExecutionsResponseModel(BaseModel):
    actions_executions: List[AuditMitigationActionExecutionMetadataModel] = Field(
        alias="actionsExecutions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAuditMitigationActionsTasksResponseModel(BaseModel):
    tasks: List[AuditMitigationActionsTaskMetadataModel] = Field(alias="tasks")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartAuditMitigationActionsTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")
    target: AuditMitigationActionsTaskTargetModel = Field(alias="target")
    audit_check_to_actions_mapping: Mapping[str, Sequence[str]] = Field(
        alias="auditCheckToActionsMapping"
    )
    client_request_token: str = Field(alias="clientRequestToken")


class DescribeAccountAuditConfigurationResponseModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    audit_notification_target_configurations: Dict[
        Literal["SNS"], AuditNotificationTargetModel
    ] = Field(alias="auditNotificationTargetConfigurations")
    audit_check_configurations: Dict[str, AuditCheckConfigurationModel] = Field(
        alias="auditCheckConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountAuditConfigurationRequestModel(BaseModel):
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    audit_notification_target_configurations: Optional[
        Mapping[Literal["SNS"], AuditNotificationTargetModel]
    ] = Field(default=None, alias="auditNotificationTargetConfigurations")
    audit_check_configurations: Optional[
        Mapping[str, AuditCheckConfigurationModel]
    ] = Field(default=None, alias="auditCheckConfigurations")


class ListAuditTasksResponseModel(BaseModel):
    tasks: List[AuditTaskMetadataModel] = Field(alias="tasks")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestAuthorizationRequestModel(BaseModel):
    auth_infos: Sequence[AuthInfoModel] = Field(alias="authInfos")
    principal: Optional[str] = Field(default=None, alias="principal")
    cognito_identity_pool_id: Optional[str] = Field(
        default=None, alias="cognitoIdentityPoolId"
    )
    client_id: Optional[str] = Field(default=None, alias="clientId")
    policy_names_to_add: Optional[Sequence[str]] = Field(
        default=None, alias="policyNamesToAdd"
    )
    policy_names_to_skip: Optional[Sequence[str]] = Field(
        default=None, alias="policyNamesToSkip"
    )


class UpdateDomainConfigurationRequestModel(BaseModel):
    domain_configuration_name: str = Field(alias="domainConfigurationName")
    authorizer_config: Optional[AuthorizerConfigModel] = Field(
        default=None, alias="authorizerConfig"
    )
    domain_configuration_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="domainConfigurationStatus"
    )
    remove_authorizer_config: Optional[bool] = Field(
        default=None, alias="removeAuthorizerConfig"
    )


class DescribeAuthorizerResponseModel(BaseModel):
    authorizer_description: AuthorizerDescriptionModel = Field(
        alias="authorizerDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDefaultAuthorizerResponseModel(BaseModel):
    authorizer_description: AuthorizerDescriptionModel = Field(
        alias="authorizerDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAuthorizersResponseModel(BaseModel):
    authorizers: List[AuthorizerSummaryModel] = Field(alias="authorizers")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AwsJobAbortConfigModel(BaseModel):
    abort_criteria_list: Sequence[AwsJobAbortCriteriaModel] = Field(
        alias="abortCriteriaList"
    )


class AwsJobExponentialRolloutRateModel(BaseModel):
    base_rate_per_minute: int = Field(alias="baseRatePerMinute")
    increment_factor: float = Field(alias="incrementFactor")
    rate_increase_criteria: AwsJobRateIncreaseCriteriaModel = Field(
        alias="rateIncreaseCriteria"
    )


class BehaviorCriteriaModel(BaseModel):
    comparison_operator: Optional[
        Literal[
            "greater-than",
            "greater-than-equals",
            "in-cidr-set",
            "in-port-set",
            "in-set",
            "less-than",
            "less-than-equals",
            "not-in-cidr-set",
            "not-in-port-set",
            "not-in-set",
        ]
    ] = Field(default=None, alias="comparisonOperator")
    value: Optional[MetricValueModel] = Field(default=None, alias="value")
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")
    consecutive_datapoints_to_alarm: Optional[int] = Field(
        default=None, alias="consecutiveDatapointsToAlarm"
    )
    consecutive_datapoints_to_clear: Optional[int] = Field(
        default=None, alias="consecutiveDatapointsToClear"
    )
    statistical_threshold: Optional[StatisticalThresholdModel] = Field(
        default=None, alias="statisticalThreshold"
    )
    ml_detection_config: Optional[MachineLearningDetectionConfigModel] = Field(
        default=None, alias="mlDetectionConfig"
    )


class GetBehaviorModelTrainingSummariesResponseModel(BaseModel):
    summaries: List[BehaviorModelTrainingSummaryModel] = Field(alias="summaries")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MetricToRetainModel(BaseModel):
    metric: str = Field(alias="metric")
    metric_dimension: Optional[MetricDimensionModel] = Field(
        default=None, alias="metricDimension"
    )


class DescribeBillingGroupResponseModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")
    billing_group_id: str = Field(alias="billingGroupId")
    billing_group_arn: str = Field(alias="billingGroupArn")
    version: int = Field(alias="version")
    billing_group_properties: BillingGroupPropertiesModel = Field(
        alias="billingGroupProperties"
    )
    billing_group_metadata: BillingGroupMetadataModel = Field(
        alias="billingGroupMetadata"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBillingGroupRequestModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")
    billing_group_properties: BillingGroupPropertiesModel = Field(
        alias="billingGroupProperties"
    )
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class GetBucketsAggregationResponseModel(BaseModel):
    total_count: int = Field(alias="totalCount")
    buckets: List[BucketModel] = Field(alias="buckets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BucketsAggregationTypeModel(BaseModel):
    terms_aggregation: Optional[TermsAggregationModel] = Field(
        default=None, alias="termsAggregation"
    )


class CACertificateDescriptionModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_id: Optional[str] = Field(default=None, alias="certificateId")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    certificate_pem: Optional[str] = Field(default=None, alias="certificatePem")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    auto_registration_status: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="autoRegistrationStatus"
    )
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    customer_version: Optional[int] = Field(default=None, alias="customerVersion")
    generation_id: Optional[str] = Field(default=None, alias="generationId")
    validity: Optional[CertificateValidityModel] = Field(default=None, alias="validity")
    certificate_mode: Optional[Literal["DEFAULT", "SNI_ONLY"]] = Field(
        default=None, alias="certificateMode"
    )


class ListCACertificatesResponseModel(BaseModel):
    certificates: List[CACertificateModel] = Field(alias="certificates")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CertificateDescriptionModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="certificateArn")
    certificate_id: Optional[str] = Field(default=None, alias="certificateId")
    ca_certificate_id: Optional[str] = Field(default=None, alias="caCertificateId")
    status: Optional[
        Literal[
            "ACTIVE",
            "INACTIVE",
            "PENDING_ACTIVATION",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "REVOKED",
        ]
    ] = Field(default=None, alias="status")
    certificate_pem: Optional[str] = Field(default=None, alias="certificatePem")
    owned_by: Optional[str] = Field(default=None, alias="ownedBy")
    previous_owned_by: Optional[str] = Field(default=None, alias="previousOwnedBy")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    customer_version: Optional[int] = Field(default=None, alias="customerVersion")
    transfer_data: Optional[TransferDataModel] = Field(
        default=None, alias="transferData"
    )
    generation_id: Optional[str] = Field(default=None, alias="generationId")
    validity: Optional[CertificateValidityModel] = Field(default=None, alias="validity")
    certificate_mode: Optional[Literal["DEFAULT", "SNI_ONLY"]] = Field(
        default=None, alias="certificateMode"
    )


class ListCertificatesByCAResponseModel(BaseModel):
    certificates: List[CertificateModel] = Field(alias="certificates")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCertificatesResponseModel(BaseModel):
    certificates: List[CertificateModel] = Field(alias="certificates")
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomCodeSigningModel(BaseModel):
    signature: Optional[CodeSigningSignatureModel] = Field(
        default=None, alias="signature"
    )
    certificate_chain: Optional[CodeSigningCertificateChainModel] = Field(
        default=None, alias="certificateChain"
    )
    hash_algorithm: Optional[str] = Field(default=None, alias="hashAlgorithm")
    signature_algorithm: Optional[str] = Field(default=None, alias="signatureAlgorithm")


class DescribeEventConfigurationsResponseModel(BaseModel):
    event_configurations: Dict[
        Literal[
            "CA_CERTIFICATE",
            "CERTIFICATE",
            "JOB",
            "JOB_EXECUTION",
            "POLICY",
            "THING",
            "THING_GROUP",
            "THING_GROUP_HIERARCHY",
            "THING_GROUP_MEMBERSHIP",
            "THING_TYPE",
            "THING_TYPE_ASSOCIATION",
        ],
        ConfigurationModel,
    ] = Field(alias="eventConfigurations")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEventConfigurationsRequestModel(BaseModel):
    event_configurations: Optional[
        Mapping[
            Literal[
                "CA_CERTIFICATE",
                "CERTIFICATE",
                "JOB",
                "JOB_EXECUTION",
                "POLICY",
                "THING",
                "THING_GROUP",
                "THING_GROUP_HIERARCHY",
                "THING_GROUP_MEMBERSHIP",
                "THING_TYPE",
                "THING_TYPE_ASSOCIATION",
            ],
            ConfigurationModel,
        ]
    ] = Field(default=None, alias="eventConfigurations")


class CreateAuthorizerRequestModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")
    authorizer_function_arn: str = Field(alias="authorizerFunctionArn")
    token_key_name: Optional[str] = Field(default=None, alias="tokenKeyName")
    token_signing_public_keys: Optional[Mapping[str, str]] = Field(
        default=None, alias="tokenSigningPublicKeys"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    signing_disabled: Optional[bool] = Field(default=None, alias="signingDisabled")
    enable_caching_for_http: Optional[bool] = Field(
        default=None, alias="enableCachingForHttp"
    )


class CreateBillingGroupRequestModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")
    billing_group_properties: Optional[BillingGroupPropertiesModel] = Field(
        default=None, alias="billingGroupProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateCustomMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    metric_type: Literal[
        "ip-address-list", "number", "number-list", "string-list"
    ] = Field(alias="metricType")
    client_request_token: str = Field(alias="clientRequestToken")
    display_name: Optional[str] = Field(default=None, alias="displayName")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateDimensionRequestModel(BaseModel):
    name: str = Field(alias="name")
    type: Literal["TOPIC_FILTER"] = Field(alias="type")
    string_values: Sequence[str] = Field(alias="stringValues")
    client_request_token: str = Field(alias="clientRequestToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateDomainConfigurationRequestModel(BaseModel):
    domain_configuration_name: str = Field(alias="domainConfigurationName")
    domain_name: Optional[str] = Field(default=None, alias="domainName")
    server_certificate_arns: Optional[Sequence[str]] = Field(
        default=None, alias="serverCertificateArns"
    )
    validation_certificate_arn: Optional[str] = Field(
        default=None, alias="validationCertificateArn"
    )
    authorizer_config: Optional[AuthorizerConfigModel] = Field(
        default=None, alias="authorizerConfig"
    )
    service_type: Optional[Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"]] = Field(
        default=None, alias="serviceType"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateFleetMetricRequestModel(BaseModel):
    metric_name: str = Field(alias="metricName")
    query_string: str = Field(alias="queryString")
    aggregation_type: AggregationTypeModel = Field(alias="aggregationType")
    period: int = Field(alias="period")
    aggregation_field: str = Field(alias="aggregationField")
    description: Optional[str] = Field(default=None, alias="description")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")
    index_name: Optional[str] = Field(default=None, alias="indexName")
    unit: Optional[
        Literal[
            "Bits",
            "Bits/Second",
            "Bytes",
            "Bytes/Second",
            "Count",
            "Count/Second",
            "Gigabits",
            "Gigabits/Second",
            "Gigabytes",
            "Gigabytes/Second",
            "Kilobits",
            "Kilobits/Second",
            "Kilobytes",
            "Kilobytes/Second",
            "Megabits",
            "Megabits/Second",
            "Megabytes",
            "Megabytes/Second",
            "Microseconds",
            "Milliseconds",
            "None",
            "Percent",
            "Seconds",
            "Terabits",
            "Terabits/Second",
            "Terabytes",
            "Terabytes/Second",
        ]
    ] = Field(default=None, alias="unit")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreatePolicyRequestModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    policy_document: str = Field(alias="policyDocument")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateRoleAliasRequestModel(BaseModel):
    role_alias: str = Field(alias="roleAlias")
    role_arn: str = Field(alias="roleArn")
    credential_duration_seconds: Optional[int] = Field(
        default=None, alias="credentialDurationSeconds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateScheduledAuditRequestModel(BaseModel):
    frequency: Literal["BIWEEKLY", "DAILY", "MONTHLY", "WEEKLY"] = Field(
        alias="frequency"
    )
    target_check_names: Sequence[str] = Field(alias="targetCheckNames")
    scheduled_audit_name: str = Field(alias="scheduledAuditName")
    day_of_month: Optional[str] = Field(default=None, alias="dayOfMonth")
    day_of_week: Optional[
        Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"]
    ] = Field(default=None, alias="dayOfWeek")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CreateKeysAndCertificateResponseModel(BaseModel):
    certificate_arn: str = Field(alias="certificateArn")
    certificate_id: str = Field(alias="certificateId")
    certificate_pem: str = Field(alias="certificatePem")
    key_pair: KeyPairModel = Field(alias="keyPair")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProvisioningClaimResponseModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")
    certificate_pem: str = Field(alias="certificatePem")
    key_pair: KeyPairModel = Field(alias="keyPair")
    expiration: datetime = Field(alias="expiration")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProvisioningTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    template_body: str = Field(alias="templateBody")
    provisioning_role_arn: str = Field(alias="provisioningRoleArn")
    description: Optional[str] = Field(default=None, alias="description")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    pre_provisioning_hook: Optional[ProvisioningHookModel] = Field(
        default=None, alias="preProvisioningHook"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    type: Optional[Literal["FLEET_PROVISIONING", "JITP"]] = Field(
        default=None, alias="type"
    )


class DescribeProvisioningTemplateResponseModel(BaseModel):
    template_arn: str = Field(alias="templateArn")
    template_name: str = Field(alias="templateName")
    description: str = Field(alias="description")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    default_version_id: int = Field(alias="defaultVersionId")
    template_body: str = Field(alias="templateBody")
    enabled: bool = Field(alias="enabled")
    provisioning_role_arn: str = Field(alias="provisioningRoleArn")
    pre_provisioning_hook: ProvisioningHookModel = Field(alias="preProvisioningHook")
    type: Literal["FLEET_PROVISIONING", "JITP"] = Field(alias="type")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProvisioningTemplateRequestModel(BaseModel):
    template_name: str = Field(alias="templateName")
    description: Optional[str] = Field(default=None, alias="description")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    default_version_id: Optional[int] = Field(default=None, alias="defaultVersionId")
    provisioning_role_arn: Optional[str] = Field(
        default=None, alias="provisioningRoleArn"
    )
    pre_provisioning_hook: Optional[ProvisioningHookModel] = Field(
        default=None, alias="preProvisioningHook"
    )
    remove_pre_provisioning_hook: Optional[bool] = Field(
        default=None, alias="removePreProvisioningHook"
    )


class CreateThingTypeRequestModel(BaseModel):
    thing_type_name: str = Field(alias="thingTypeName")
    thing_type_properties: Optional[ThingTypePropertiesModel] = Field(
        default=None, alias="thingTypeProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class DescribeAuditTaskResponseModel(BaseModel):
    task_status: Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"] = Field(
        alias="taskStatus"
    )
    task_type: Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"] = Field(
        alias="taskType"
    )
    task_start_time: datetime = Field(alias="taskStartTime")
    task_statistics: TaskStatisticsModel = Field(alias="taskStatistics")
    scheduled_audit_name: str = Field(alias="scheduledAuditName")
    audit_details: Dict[str, AuditCheckDetailsModel] = Field(alias="auditDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterCACertificateRequestModel(BaseModel):
    ca_certificate: str = Field(alias="caCertificate")
    verification_certificate: Optional[str] = Field(
        default=None, alias="verificationCertificate"
    )
    set_as_active: Optional[bool] = Field(default=None, alias="setAsActive")
    allow_auto_registration: Optional[bool] = Field(
        default=None, alias="allowAutoRegistration"
    )
    registration_config: Optional[RegistrationConfigModel] = Field(
        default=None, alias="registrationConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    certificate_mode: Optional[Literal["DEFAULT", "SNI_ONLY"]] = Field(
        default=None, alias="certificateMode"
    )


class UpdateCACertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="certificateId")
    new_status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="newStatus"
    )
    new_auto_registration_status: Optional[Literal["DISABLE", "ENABLE"]] = Field(
        default=None, alias="newAutoRegistrationStatus"
    )
    registration_config: Optional[RegistrationConfigModel] = Field(
        default=None, alias="registrationConfig"
    )
    remove_auto_registration: Optional[bool] = Field(
        default=None, alias="removeAutoRegistration"
    )


class DescribeDomainConfigurationResponseModel(BaseModel):
    domain_configuration_name: str = Field(alias="domainConfigurationName")
    domain_configuration_arn: str = Field(alias="domainConfigurationArn")
    domain_name: str = Field(alias="domainName")
    server_certificates: List[ServerCertificateSummaryModel] = Field(
        alias="serverCertificates"
    )
    authorizer_config: AuthorizerConfigModel = Field(alias="authorizerConfig")
    domain_configuration_status: Literal["DISABLED", "ENABLED"] = Field(
        alias="domainConfigurationStatus"
    )
    service_type: Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"] = Field(
        alias="serviceType"
    )
    domain_type: Literal["AWS_MANAGED", "CUSTOMER_MANAGED", "ENDPOINT"] = Field(
        alias="domainType"
    )
    last_status_change_date: datetime = Field(alias="lastStatusChangeDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeManagedJobTemplateResponseModel(BaseModel):
    template_name: str = Field(alias="templateName")
    template_arn: str = Field(alias="templateArn")
    description: str = Field(alias="description")
    template_version: str = Field(alias="templateVersion")
    environments: List[str] = Field(alias="environments")
    document_parameters: List[DocumentParameterModel] = Field(
        alias="documentParameters"
    )
    document: str = Field(alias="document")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRoleAliasResponseModel(BaseModel):
    role_alias_description: RoleAliasDescriptionModel = Field(
        alias="roleAliasDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeThingTypeResponseModel(BaseModel):
    thing_type_name: str = Field(alias="thingTypeName")
    thing_type_id: str = Field(alias="thingTypeId")
    thing_type_arn: str = Field(alias="thingTypeArn")
    thing_type_properties: ThingTypePropertiesModel = Field(alias="thingTypeProperties")
    thing_type_metadata: ThingTypeMetadataModel = Field(alias="thingTypeMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ThingModelinitionModel(BaseModel):
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    thing_type_arn: Optional[str] = Field(default=None, alias="thingTypeArn")
    thing_type_properties: Optional[ThingTypePropertiesModel] = Field(
        default=None, alias="thingTypeProperties"
    )
    thing_type_metadata: Optional[ThingTypeMetadataModel] = Field(
        default=None, alias="thingTypeMetadata"
    )


class DestinationModel(BaseModel):
    s3_destination: Optional[S3DestinationModel] = Field(
        default=None, alias="s3Destination"
    )


class ListDetectMitigationActionsExecutionsResponseModel(BaseModel):
    actions_executions: List[DetectMitigationActionExecutionModel] = Field(
        alias="actionsExecutions"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartDetectMitigationActionsTaskRequestModel(BaseModel):
    task_id: str = Field(alias="taskId")
    target: DetectMitigationActionsTaskTargetModel = Field(alias="target")
    actions: Sequence[str] = Field(alias="actions")
    client_request_token: str = Field(alias="clientRequestToken")
    violation_event_occurrence_range: Optional[
        ViolationEventOccurrenceRangeModel
    ] = Field(default=None, alias="violationEventOccurrenceRange")
    include_only_active_violations: Optional[bool] = Field(
        default=None, alias="includeOnlyActiveViolations"
    )
    include_suppressed_alerts: Optional[bool] = Field(
        default=None, alias="includeSuppressedAlerts"
    )


class ListDomainConfigurationsResponseModel(BaseModel):
    domain_configurations: List[DomainConfigurationSummaryModel] = Field(
        alias="domainConfigurations"
    )
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DynamoDBv2ActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    put_item: PutItemInputModel = Field(alias="putItem")


class GetEffectivePoliciesResponseModel(BaseModel):
    effective_policies: List[EffectivePolicyModel] = Field(alias="effectivePolicies")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExponentialRolloutRateModel(BaseModel):
    base_rate_per_minute: int = Field(alias="baseRatePerMinute")
    increment_factor: float = Field(alias="incrementFactor")
    rate_increase_criteria: RateIncreaseCriteriaModel = Field(
        alias="rateIncreaseCriteria"
    )


class ThingGroupIndexingConfigurationModel(BaseModel):
    thing_group_indexing_mode: Literal["OFF", "ON"] = Field(
        alias="thingGroupIndexingMode"
    )
    managed_fields: Optional[List[FieldModel]] = Field(
        default=None, alias="managedFields"
    )
    custom_fields: Optional[List[FieldModel]] = Field(
        default=None, alias="customFields"
    )


class StreamFileModel(BaseModel):
    file_id: Optional[int] = Field(default=None, alias="fileId")
    s3_location: Optional[S3LocationModel] = Field(default=None, alias="s3Location")


class FileLocationModel(BaseModel):
    stream: Optional[StreamModel] = Field(default=None, alias="stream")
    s3_location: Optional[S3LocationModel] = Field(default=None, alias="s3Location")


class ListFleetMetricsResponseModel(BaseModel):
    fleet_metrics: List[FleetMetricNameAndArnModel] = Field(alias="fleetMetrics")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetBehaviorModelTrainingSummariesRequestGetBehaviorModelTrainingSummariesPaginateModel(
    BaseModel
):
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListActiveViolationsRequestListActiveViolationsPaginateModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior_criteria_type: Optional[
        Literal["MACHINE_LEARNING", "STATIC", "STATISTICAL"]
    ] = Field(default=None, alias="behaviorCriteriaType")
    list_suppressed_alerts: Optional[bool] = Field(
        default=None, alias="listSuppressedAlerts"
    )
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="verificationState")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttachedPoliciesRequestListAttachedPoliciesPaginateModel(BaseModel):
    target: str = Field(alias="target")
    recursive: Optional[bool] = Field(default=None, alias="recursive")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateModel(
    BaseModel
):
    task_id: str = Field(alias="taskId")
    finding_id: str = Field(alias="findingId")
    action_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "SKIPPED"]
    ] = Field(default=None, alias="actionStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateModel(
    BaseModel
):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    audit_task_id: Optional[str] = Field(default=None, alias="auditTaskId")
    finding_id: Optional[str] = Field(default=None, alias="findingId")
    task_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="taskStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAuditTasksRequestListAuditTasksPaginateModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    task_type: Optional[
        Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"]
    ] = Field(default=None, alias="taskType")
    task_status: Optional[
        Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
    ] = Field(default=None, alias="taskStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAuthorizersRequestListAuthorizersPaginateModel(BaseModel):
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="status"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListBillingGroupsRequestListBillingGroupsPaginateModel(BaseModel):
    name_prefix_filter: Optional[str] = Field(default=None, alias="namePrefixFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCACertificatesRequestListCACertificatesPaginateModel(BaseModel):
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    template_name: Optional[str] = Field(default=None, alias="templateName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCertificatesByCARequestListCertificatesByCAPaginateModel(BaseModel):
    ca_certificate_id: str = Field(alias="caCertificateId")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCertificatesRequestListCertificatesPaginateModel(BaseModel):
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCustomMetricsRequestListCustomMetricsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDetectMitigationActionsExecutionsRequestListDetectMitigationActionsExecutionsPaginateModel(
    BaseModel
):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    violation_id: Optional[str] = Field(default=None, alias="violationId")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateModel(
    BaseModel
):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDimensionsRequestListDimensionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDomainConfigurationsRequestListDomainConfigurationsPaginateModel(BaseModel):
    service_type: Optional[Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"]] = Field(
        default=None, alias="serviceType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFleetMetricsRequestListFleetMetricsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIndicesRequestListIndicesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobExecutionsForJobRequestListJobExecutionsForJobPaginateModel(BaseModel):
    job_id: str = Field(alias="jobId")
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobExecutionsForThingRequestListJobExecutionsForThingPaginateModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobTemplatesRequestListJobTemplatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestListJobsPaginateModel(BaseModel):
    status: Optional[
        Literal[
            "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS", "IN_PROGRESS", "SCHEDULED"
        ]
    ] = Field(default=None, alias="status")
    target_selection: Optional[Literal["CONTINUOUS", "SNAPSHOT"]] = Field(
        default=None, alias="targetSelection"
    )
    thing_group_name: Optional[str] = Field(default=None, alias="thingGroupName")
    thing_group_id: Optional[str] = Field(default=None, alias="thingGroupId")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMetricValuesRequestListMetricValuesPaginateModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    metric_name: str = Field(alias="metricName")
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    dimension_name: Optional[str] = Field(default=None, alias="dimensionName")
    dimension_value_operator: Optional[Literal["IN", "NOT_IN"]] = Field(
        default=None, alias="dimensionValueOperator"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListMitigationActionsRequestListMitigationActionsPaginateModel(BaseModel):
    action_type: Optional[
        Literal[
            "ADD_THINGS_TO_THING_GROUP",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "UPDATE_CA_CERTIFICATE",
            "UPDATE_DEVICE_CERTIFICATE",
        ]
    ] = Field(default=None, alias="actionType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOTAUpdatesRequestListOTAUpdatesPaginateModel(BaseModel):
    ota_update_status: Optional[
        Literal[
            "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_PENDING"
        ]
    ] = Field(default=None, alias="otaUpdateStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOutgoingCertificatesRequestListOutgoingCertificatesPaginateModel(BaseModel):
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPoliciesRequestListPoliciesPaginateModel(BaseModel):
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPolicyPrincipalsRequestListPolicyPrincipalsPaginateModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPrincipalPoliciesRequestListPrincipalPoliciesPaginateModel(BaseModel):
    principal: str = Field(alias="principal")
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPrincipalThingsRequestListPrincipalThingsPaginateModel(BaseModel):
    principal: str = Field(alias="principal")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateModel(
    BaseModel
):
    template_name: str = Field(alias="templateName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProvisioningTemplatesRequestListProvisioningTemplatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRoleAliasesRequestListRoleAliasesPaginateModel(BaseModel):
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListScheduledAuditsRequestListScheduledAuditsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateModel(
    BaseModel
):
    security_profile_target_arn: str = Field(alias="securityProfileTargetArn")
    recursive: Optional[bool] = Field(default=None, alias="recursive")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityProfilesRequestListSecurityProfilesPaginateModel(BaseModel):
    dimension_name: Optional[str] = Field(default=None, alias="dimensionName")
    metric_name: Optional[str] = Field(default=None, alias="metricName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamsRequestListStreamsPaginateModel(BaseModel):
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTargetsForPolicyRequestListTargetsForPolicyPaginateModel(BaseModel):
    policy_name: str = Field(alias="policyName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateModel(
    BaseModel
):
    security_profile_name: str = Field(alias="securityProfileName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingGroupsForThingRequestListThingGroupsForThingPaginateModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingGroupsRequestListThingGroupsPaginateModel(BaseModel):
    parent_group: Optional[str] = Field(default=None, alias="parentGroup")
    name_prefix_filter: Optional[str] = Field(default=None, alias="namePrefixFilter")
    recursive: Optional[bool] = Field(default=None, alias="recursive")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingPrincipalsRequestListThingPrincipalsPaginateModel(BaseModel):
    thing_name: str = Field(alias="thingName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateModel(
    BaseModel
):
    task_id: str = Field(alias="taskId")
    report_type: Literal["ERRORS", "RESULTS"] = Field(alias="reportType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingRegistrationTasksRequestListThingRegistrationTasksPaginateModel(
    BaseModel
):
    status: Optional[
        Literal["Cancelled", "Cancelling", "Completed", "Failed", "InProgress"]
    ] = Field(default=None, alias="status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingTypesRequestListThingTypesPaginateModel(BaseModel):
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingsInBillingGroupRequestListThingsInBillingGroupPaginateModel(BaseModel):
    billing_group_name: str = Field(alias="billingGroupName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingsInThingGroupRequestListThingsInThingGroupPaginateModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    recursive: Optional[bool] = Field(default=None, alias="recursive")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThingsRequestListThingsPaginateModel(BaseModel):
    attribute_name: Optional[str] = Field(default=None, alias="attributeName")
    attribute_value: Optional[str] = Field(default=None, alias="attributeValue")
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    use_prefix_attribute_value: Optional[bool] = Field(
        default=None, alias="usePrefixAttributeValue"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTopicRuleDestinationsRequestListTopicRuleDestinationsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTopicRulesRequestListTopicRulesPaginateModel(BaseModel):
    topic: Optional[str] = Field(default=None, alias="topic")
    rule_disabled: Optional[bool] = Field(default=None, alias="ruleDisabled")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListV2LoggingLevelsRequestListV2LoggingLevelsPaginateModel(BaseModel):
    target_type: Optional[
        Literal["CLIENT_ID", "DEFAULT", "PRINCIPAL_ID", "SOURCE_IP", "THING_GROUP"]
    ] = Field(default=None, alias="targetType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListViolationEventsRequestListViolationEventsPaginateModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="startTime")
    end_time: Union[datetime, str] = Field(alias="endTime")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior_criteria_type: Optional[
        Literal["MACHINE_LEARNING", "STATIC", "STATISTICAL"]
    ] = Field(default=None, alias="behaviorCriteriaType")
    list_suppressed_alerts: Optional[bool] = Field(
        default=None, alias="listSuppressedAlerts"
    )
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="verificationState")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetPercentilesResponseModel(BaseModel):
    percentiles: List[PercentPairModel] = Field(alias="percentiles")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetStatisticsResponseModel(BaseModel):
    statistics: StatisticsModel = Field(alias="statistics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListBillingGroupsResponseModel(BaseModel):
    billing_groups: List[GroupNameAndArnModel] = Field(alias="billingGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingGroupsForThingResponseModel(BaseModel):
    thing_groups: List[GroupNameAndArnModel] = Field(alias="thingGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingGroupsResponseModel(BaseModel):
    thing_groups: List[GroupNameAndArnModel] = Field(alias="thingGroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ThingGroupMetadataModel(BaseModel):
    parent_group_name: Optional[str] = Field(default=None, alias="parentGroupName")
    root_to_parent_thing_groups: Optional[List[GroupNameAndArnModel]] = Field(
        default=None, alias="rootToParentThingGroups"
    )
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")


class HttpAuthorizationModel(BaseModel):
    sigv4: Optional[SigV4AuthorizationModel] = Field(default=None, alias="sigv4")


class ThingIndexingConfigurationModel(BaseModel):
    thing_indexing_mode: Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"] = Field(
        alias="thingIndexingMode"
    )
    thing_connectivity_indexing_mode: Optional[Literal["OFF", "STATUS"]] = Field(
        default=None, alias="thingConnectivityIndexingMode"
    )
    device_defender_indexing_mode: Optional[Literal["OFF", "VIOLATIONS"]] = Field(
        default=None, alias="deviceDefenderIndexingMode"
    )
    named_shadow_indexing_mode: Optional[Literal["OFF", "ON"]] = Field(
        default=None, alias="namedShadowIndexingMode"
    )
    managed_fields: Optional[List[FieldModel]] = Field(
        default=None, alias="managedFields"
    )
    custom_fields: Optional[List[FieldModel]] = Field(
        default=None, alias="customFields"
    )
    filter: Optional[IndexingFilterModel] = Field(default=None, alias="filter")


class JobExecutionModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    status: Optional[
        Literal[
            "CANCELED",
            "FAILED",
            "IN_PROGRESS",
            "QUEUED",
            "REJECTED",
            "REMOVED",
            "SUCCEEDED",
            "TIMED_OUT",
        ]
    ] = Field(default=None, alias="status")
    force_canceled: Optional[bool] = Field(default=None, alias="forceCanceled")
    status_details: Optional[JobExecutionStatusDetailsModel] = Field(
        default=None, alias="statusDetails"
    )
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")
    queued_at: Optional[datetime] = Field(default=None, alias="queuedAt")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    execution_number: Optional[int] = Field(default=None, alias="executionNumber")
    version_number: Optional[int] = Field(default=None, alias="versionNumber")
    approximate_seconds_before_timed_out: Optional[int] = Field(
        default=None, alias="approximateSecondsBeforeTimedOut"
    )


class JobExecutionSummaryForJobModel(BaseModel):
    thing_arn: Optional[str] = Field(default=None, alias="thingArn")
    job_execution_summary: Optional[JobExecutionSummaryModel] = Field(
        default=None, alias="jobExecutionSummary"
    )


class JobExecutionSummaryForThingModel(BaseModel):
    job_id: Optional[str] = Field(default=None, alias="jobId")
    job_execution_summary: Optional[JobExecutionSummaryModel] = Field(
        default=None, alias="jobExecutionSummary"
    )


class JobExecutionsRetryConfigModel(BaseModel):
    criteria_list: Sequence[RetryCriteriaModel] = Field(alias="criteriaList")


class ListJobsResponseModel(BaseModel):
    jobs: List[JobSummaryModel] = Field(alias="jobs")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobTemplatesResponseModel(BaseModel):
    job_templates: List[JobTemplateSummaryModel] = Field(alias="jobTemplates")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListManagedJobTemplatesResponseModel(BaseModel):
    managed_job_templates: List[ManagedJobTemplateSummaryModel] = Field(
        alias="managedJobTemplates"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMitigationActionsResponseModel(BaseModel):
    action_identifiers: List[MitigationActionIdentifierModel] = Field(
        alias="actionIdentifiers"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOTAUpdatesResponseModel(BaseModel):
    ota_updates: List[OTAUpdateSummaryModel] = Field(alias="otaUpdates")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOutgoingCertificatesResponseModel(BaseModel):
    outgoing_certificates: List[OutgoingCertificateModel] = Field(
        alias="outgoingCertificates"
    )
    next_marker: str = Field(alias="nextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPolicyVersionsResponseModel(BaseModel):
    policy_versions: List[PolicyVersionModel] = Field(alias="policyVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProvisioningTemplateVersionsResponseModel(BaseModel):
    versions: List[ProvisioningTemplateVersionSummaryModel] = Field(alias="versions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProvisioningTemplatesResponseModel(BaseModel):
    templates: List[ProvisioningTemplateSummaryModel] = Field(alias="templates")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListScheduledAuditsResponseModel(BaseModel):
    scheduled_audits: List[ScheduledAuditMetadataModel] = Field(alias="scheduledAudits")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityProfilesResponseModel(BaseModel):
    security_profile_identifiers: List[SecurityProfileIdentifierModel] = Field(
        alias="securityProfileIdentifiers"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamsResponseModel(BaseModel):
    streams: List[StreamSummaryModel] = Field(alias="streams")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTargetsForSecurityProfileResponseModel(BaseModel):
    security_profile_targets: List[SecurityProfileTargetModel] = Field(
        alias="securityProfileTargets"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SecurityProfileTargetMappingModel(BaseModel):
    security_profile_identifier: Optional[SecurityProfileIdentifierModel] = Field(
        default=None, alias="securityProfileIdentifier"
    )
    target: Optional[SecurityProfileTargetModel] = Field(default=None, alias="target")


class ListThingsResponseModel(BaseModel):
    things: List[ThingAttributeModel] = Field(alias="things")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTopicRulesResponseModel(BaseModel):
    rules: List[TopicRuleListItemModel] = Field(alias="rules")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LocationActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    tracker_name: str = Field(alias="trackerName")
    device_id: str = Field(alias="deviceId")
    latitude: str = Field(alias="latitude")
    longitude: str = Field(alias="longitude")
    timestamp: Optional[LocationTimestampModel] = Field(default=None, alias="timestamp")


class LogTargetConfigurationModel(BaseModel):
    log_target: Optional[LogTargetModel] = Field(default=None, alias="logTarget")
    log_level: Optional[Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"]] = Field(
        default=None, alias="logLevel"
    )


class SetV2LoggingLevelRequestModel(BaseModel):
    log_target: LogTargetModel = Field(alias="logTarget")
    log_level: Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"] = Field(
        alias="logLevel"
    )


class SetLoggingOptionsRequestModel(BaseModel):
    logging_options_payload: LoggingOptionsPayloadModel = Field(
        alias="loggingOptionsPayload"
    )


class MitigationActionParamsModel(BaseModel):
    update_device_certificate_params: Optional[
        UpdateDeviceCertificateParamsModel
    ] = Field(default=None, alias="updateDeviceCertificateParams")
    update_cacertificate_params: Optional[UpdateCACertificateParamsModel] = Field(
        default=None, alias="updateCACertificateParams"
    )
    add_things_to_thing_group_params: Optional[
        AddThingsToThingGroupParamsModel
    ] = Field(default=None, alias="addThingsToThingGroupParams")
    replace_default_policy_version_params: Optional[
        ReplaceDefaultPolicyVersionParamsModel
    ] = Field(default=None, alias="replaceDefaultPolicyVersionParams")
    enable_io_tlogging_params: Optional[EnableIoTLoggingParamsModel] = Field(
        default=None, alias="enableIoTLoggingParams"
    )
    publish_finding_to_sns_params: Optional[PublishFindingToSnsParamsModel] = Field(
        default=None, alias="publishFindingToSnsParams"
    )


class MqttHeadersModel(BaseModel):
    payload_format_indicator: Optional[str] = Field(
        default=None, alias="payloadFormatIndicator"
    )
    content_type: Optional[str] = Field(default=None, alias="contentType")
    response_topic: Optional[str] = Field(default=None, alias="responseTopic")
    correlation_data: Optional[str] = Field(default=None, alias="correlationData")
    message_expiry: Optional[str] = Field(default=None, alias="messageExpiry")
    user_properties: Optional[Sequence[UserPropertyModel]] = Field(
        default=None, alias="userProperties"
    )


class ResourceIdentifierModel(BaseModel):
    device_certificate_id: Optional[str] = Field(
        default=None, alias="deviceCertificateId"
    )
    ca_certificate_id: Optional[str] = Field(default=None, alias="caCertificateId")
    cognito_identity_pool_id: Optional[str] = Field(
        default=None, alias="cognitoIdentityPoolId"
    )
    client_id: Optional[str] = Field(default=None, alias="clientId")
    policy_version_identifier: Optional[PolicyVersionIdentifierModel] = Field(
        default=None, alias="policyVersionIdentifier"
    )
    account: Optional[str] = Field(default=None, alias="account")
    iam_role_arn: Optional[str] = Field(default=None, alias="iamRoleArn")
    role_alias_arn: Optional[str] = Field(default=None, alias="roleAliasArn")
    issuer_certificate_identifier: Optional[IssuerCertificateIdentifierModel] = Field(
        default=None, alias="issuerCertificateIdentifier"
    )
    device_certificate_arn: Optional[str] = Field(
        default=None, alias="deviceCertificateArn"
    )


class TestInvokeAuthorizerRequestModel(BaseModel):
    authorizer_name: str = Field(alias="authorizerName")
    token: Optional[str] = Field(default=None, alias="token")
    token_signature: Optional[str] = Field(default=None, alias="tokenSignature")
    http_context: Optional[HttpContextModel] = Field(default=None, alias="httpContext")
    mqtt_context: Optional[MqttContextModel] = Field(default=None, alias="mqttContext")
    tls_context: Optional[TlsContextModel] = Field(default=None, alias="tlsContext")


class ThingDocumentModel(BaseModel):
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    thing_id: Optional[str] = Field(default=None, alias="thingId")
    thing_type_name: Optional[str] = Field(default=None, alias="thingTypeName")
    thing_group_names: Optional[List[str]] = Field(
        default=None, alias="thingGroupNames"
    )
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="attributes")
    shadow: Optional[str] = Field(default=None, alias="shadow")
    device_defender: Optional[str] = Field(default=None, alias="deviceDefender")
    connectivity: Optional[ThingConnectivityModel] = Field(
        default=None, alias="connectivity"
    )


class TimestreamActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    database_name: str = Field(alias="databaseName")
    table_name: str = Field(alias="tableName")
    dimensions: Sequence[TimestreamDimensionModel] = Field(alias="dimensions")
    timestamp: Optional[TimestreamTimestampModel] = Field(
        default=None, alias="timestamp"
    )


class TopicRuleDestinationConfigurationModel(BaseModel):
    http_url_configuration: Optional[HttpUrlDestinationConfigurationModel] = Field(
        default=None, alias="httpUrlConfiguration"
    )
    vpc_configuration: Optional[VpcDestinationConfigurationModel] = Field(
        default=None, alias="vpcConfiguration"
    )


class TopicRuleDestinationSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[
        Literal["DELETING", "DISABLED", "ENABLED", "ERROR", "IN_PROGRESS"]
    ] = Field(default=None, alias="status")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    http_url_summary: Optional[HttpUrlDestinationSummaryModel] = Field(
        default=None, alias="httpUrlSummary"
    )
    vpc_destination_summary: Optional[VpcDestinationSummaryModel] = Field(
        default=None, alias="vpcDestinationSummary"
    )


class TopicRuleDestinationModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="arn")
    status: Optional[
        Literal["DELETING", "DISABLED", "ENABLED", "ERROR", "IN_PROGRESS"]
    ] = Field(default=None, alias="status")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    status_reason: Optional[str] = Field(default=None, alias="statusReason")
    http_url_properties: Optional[HttpUrlDestinationPropertiesModel] = Field(
        default=None, alias="httpUrlProperties"
    )
    vpc_properties: Optional[VpcDestinationPropertiesModel] = Field(
        default=None, alias="vpcProperties"
    )


class ValidateSecurityProfileBehaviorsResponseModel(BaseModel):
    valid: bool = Field(alias="valid")
    validation_errors: List[ValidationErrorModel] = Field(alias="validationErrors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListMetricValuesResponseModel(BaseModel):
    metric_datum_list: List[MetricDatumModel] = Field(alias="metricDatumList")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeniedModel(BaseModel):
    implicit_deny: Optional[ImplicitDenyModel] = Field(
        default=None, alias="implicitDeny"
    )
    explicit_deny: Optional[ExplicitDenyModel] = Field(
        default=None, alias="explicitDeny"
    )


class PutAssetPropertyValueEntryModel(BaseModel):
    property_values: Sequence[AssetPropertyValueModel] = Field(alias="propertyValues")
    entry_id: Optional[str] = Field(default=None, alias="entryId")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    property_id: Optional[str] = Field(default=None, alias="propertyId")
    property_alias: Optional[str] = Field(default=None, alias="propertyAlias")


class CreateDynamicThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    query_string: str = Field(alias="queryString")
    thing_group_properties: Optional[ThingGroupPropertiesModel] = Field(
        default=None, alias="thingGroupProperties"
    )
    index_name: Optional[str] = Field(default=None, alias="indexName")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class CreateThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    parent_group_name: Optional[str] = Field(default=None, alias="parentGroupName")
    thing_group_properties: Optional[ThingGroupPropertiesModel] = Field(
        default=None, alias="thingGroupProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class UpdateDynamicThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    thing_group_properties: ThingGroupPropertiesModel = Field(
        alias="thingGroupProperties"
    )
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")
    index_name: Optional[str] = Field(default=None, alias="indexName")
    query_string: Optional[str] = Field(default=None, alias="queryString")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")


class UpdateThingGroupRequestModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    thing_group_properties: ThingGroupPropertiesModel = Field(
        alias="thingGroupProperties"
    )
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class AwsJobExecutionsRolloutConfigModel(BaseModel):
    maximum_per_minute: Optional[int] = Field(default=None, alias="maximumPerMinute")
    exponential_rate: Optional[AwsJobExponentialRolloutRateModel] = Field(
        default=None, alias="exponentialRate"
    )


class BehaviorModel(BaseModel):
    name: str = Field(alias="name")
    metric: Optional[str] = Field(default=None, alias="metric")
    metric_dimension: Optional[MetricDimensionModel] = Field(
        default=None, alias="metricDimension"
    )
    criteria: Optional[BehaviorCriteriaModel] = Field(default=None, alias="criteria")
    suppress_alerts: Optional[bool] = Field(default=None, alias="suppressAlerts")


class GetBucketsAggregationRequestModel(BaseModel):
    query_string: str = Field(alias="queryString")
    aggregation_field: str = Field(alias="aggregationField")
    buckets_aggregation_type: BucketsAggregationTypeModel = Field(
        alias="bucketsAggregationType"
    )
    index_name: Optional[str] = Field(default=None, alias="indexName")
    query_version: Optional[str] = Field(default=None, alias="queryVersion")


class DescribeCACertificateResponseModel(BaseModel):
    certificate_description: CACertificateDescriptionModel = Field(
        alias="certificateDescription"
    )
    registration_config: RegistrationConfigModel = Field(alias="registrationConfig")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCertificateResponseModel(BaseModel):
    certificate_description: CertificateDescriptionModel = Field(
        alias="certificateDescription"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThingTypesResponseModel(BaseModel):
    thing_types: List[ThingModelinitionModel] = Field(alias="thingTypes")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSigningJobParameterModel(BaseModel):
    signing_profile_parameter: Optional[SigningProfileParameterModel] = Field(
        default=None, alias="signingProfileParameter"
    )
    signing_profile_name: Optional[str] = Field(
        default=None, alias="signingProfileName"
    )
    destination: Optional[DestinationModel] = Field(default=None, alias="destination")


class JobExecutionsRolloutConfigModel(BaseModel):
    maximum_per_minute: Optional[int] = Field(default=None, alias="maximumPerMinute")
    exponential_rate: Optional[ExponentialRolloutRateModel] = Field(
        default=None, alias="exponentialRate"
    )


class CreateStreamRequestModel(BaseModel):
    stream_id: str = Field(alias="streamId")
    files: Sequence[StreamFileModel] = Field(alias="files")
    role_arn: str = Field(alias="roleArn")
    description: Optional[str] = Field(default=None, alias="description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class StreamInfoModel(BaseModel):
    stream_id: Optional[str] = Field(default=None, alias="streamId")
    stream_arn: Optional[str] = Field(default=None, alias="streamArn")
    stream_version: Optional[int] = Field(default=None, alias="streamVersion")
    description: Optional[str] = Field(default=None, alias="description")
    files: Optional[List[StreamFileModel]] = Field(default=None, alias="files")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class UpdateStreamRequestModel(BaseModel):
    stream_id: str = Field(alias="streamId")
    description: Optional[str] = Field(default=None, alias="description")
    files: Optional[Sequence[StreamFileModel]] = Field(default=None, alias="files")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class DescribeThingGroupResponseModel(BaseModel):
    thing_group_name: str = Field(alias="thingGroupName")
    thing_group_id: str = Field(alias="thingGroupId")
    thing_group_arn: str = Field(alias="thingGroupArn")
    version: int = Field(alias="version")
    thing_group_properties: ThingGroupPropertiesModel = Field(
        alias="thingGroupProperties"
    )
    thing_group_metadata: ThingGroupMetadataModel = Field(alias="thingGroupMetadata")
    index_name: str = Field(alias="indexName")
    query_string: str = Field(alias="queryString")
    query_version: str = Field(alias="queryVersion")
    status: Literal["ACTIVE", "BUILDING", "REBUILDING"] = Field(alias="status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HttpActionModel(BaseModel):
    url: str = Field(alias="url")
    confirmation_url: Optional[str] = Field(default=None, alias="confirmationUrl")
    headers: Optional[Sequence[HttpActionHeaderModel]] = Field(
        default=None, alias="headers"
    )
    auth: Optional[HttpAuthorizationModel] = Field(default=None, alias="auth")


class GetIndexingConfigurationResponseModel(BaseModel):
    thing_indexing_configuration: ThingIndexingConfigurationModel = Field(
        alias="thingIndexingConfiguration"
    )
    thing_group_indexing_configuration: ThingGroupIndexingConfigurationModel = Field(
        alias="thingGroupIndexingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIndexingConfigurationRequestModel(BaseModel):
    thing_indexing_configuration: Optional[ThingIndexingConfigurationModel] = Field(
        default=None, alias="thingIndexingConfiguration"
    )
    thing_group_indexing_configuration: Optional[
        ThingGroupIndexingConfigurationModel
    ] = Field(default=None, alias="thingGroupIndexingConfiguration")


class DescribeJobExecutionResponseModel(BaseModel):
    execution: JobExecutionModel = Field(alias="execution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobExecutionsForJobResponseModel(BaseModel):
    execution_summaries: List[JobExecutionSummaryForJobModel] = Field(
        alias="executionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobExecutionsForThingResponseModel(BaseModel):
    execution_summaries: List[JobExecutionSummaryForThingModel] = Field(
        alias="executionSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityProfilesForTargetResponseModel(BaseModel):
    security_profile_target_mappings: List[SecurityProfileTargetMappingModel] = Field(
        alias="securityProfileTargetMappings"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListV2LoggingLevelsResponseModel(BaseModel):
    log_target_configurations: List[LogTargetConfigurationModel] = Field(
        alias="logTargetConfigurations"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateMitigationActionRequestModel(BaseModel):
    action_name: str = Field(alias="actionName")
    role_arn: str = Field(alias="roleArn")
    action_params: MitigationActionParamsModel = Field(alias="actionParams")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class DescribeMitigationActionResponseModel(BaseModel):
    action_name: str = Field(alias="actionName")
    action_type: Literal[
        "ADD_THINGS_TO_THING_GROUP",
        "ENABLE_IOT_LOGGING",
        "PUBLISH_FINDING_TO_SNS",
        "REPLACE_DEFAULT_POLICY_VERSION",
        "UPDATE_CA_CERTIFICATE",
        "UPDATE_DEVICE_CERTIFICATE",
    ] = Field(alias="actionType")
    action_arn: str = Field(alias="actionArn")
    action_id: str = Field(alias="actionId")
    role_arn: str = Field(alias="roleArn")
    action_params: MitigationActionParamsModel = Field(alias="actionParams")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MitigationActionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    id: Optional[str] = Field(default=None, alias="id")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    action_params: Optional[MitigationActionParamsModel] = Field(
        default=None, alias="actionParams"
    )


class UpdateMitigationActionRequestModel(BaseModel):
    action_name: str = Field(alias="actionName")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    action_params: Optional[MitigationActionParamsModel] = Field(
        default=None, alias="actionParams"
    )


class RepublishActionModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    topic: str = Field(alias="topic")
    qos: Optional[int] = Field(default=None, alias="qos")
    headers: Optional[MqttHeadersModel] = Field(default=None, alias="headers")


class AuditSuppressionModel(BaseModel):
    check_name: str = Field(alias="checkName")
    resource_identifier: ResourceIdentifierModel = Field(alias="resourceIdentifier")
    expiration_date: Optional[datetime] = Field(default=None, alias="expirationDate")
    suppress_indefinitely: Optional[bool] = Field(
        default=None, alias="suppressIndefinitely"
    )
    description: Optional[str] = Field(default=None, alias="description")


class CreateAuditSuppressionRequestModel(BaseModel):
    check_name: str = Field(alias="checkName")
    resource_identifier: ResourceIdentifierModel = Field(alias="resourceIdentifier")
    client_request_token: str = Field(alias="clientRequestToken")
    expiration_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="expirationDate"
    )
    suppress_indefinitely: Optional[bool] = Field(
        default=None, alias="suppressIndefinitely"
    )
    description: Optional[str] = Field(default=None, alias="description")


class DeleteAuditSuppressionRequestModel(BaseModel):
    check_name: str = Field(alias="checkName")
    resource_identifier: ResourceIdentifierModel = Field(alias="resourceIdentifier")


class DescribeAuditSuppressionRequestModel(BaseModel):
    check_name: str = Field(alias="checkName")
    resource_identifier: ResourceIdentifierModel = Field(alias="resourceIdentifier")


class DescribeAuditSuppressionResponseModel(BaseModel):
    check_name: str = Field(alias="checkName")
    resource_identifier: ResourceIdentifierModel = Field(alias="resourceIdentifier")
    expiration_date: datetime = Field(alias="expirationDate")
    suppress_indefinitely: bool = Field(alias="suppressIndefinitely")
    description: str = Field(alias="description")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAuditFindingsRequestListAuditFindingsPaginateModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    check_name: Optional[str] = Field(default=None, alias="checkName")
    resource_identifier: Optional[ResourceIdentifierModel] = Field(
        default=None, alias="resourceIdentifier"
    )
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    list_suppressed_findings: Optional[bool] = Field(
        default=None, alias="listSuppressedFindings"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAuditFindingsRequestModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    check_name: Optional[str] = Field(default=None, alias="checkName")
    resource_identifier: Optional[ResourceIdentifierModel] = Field(
        default=None, alias="resourceIdentifier"
    )
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="startTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="endTime")
    list_suppressed_findings: Optional[bool] = Field(
        default=None, alias="listSuppressedFindings"
    )


class ListAuditSuppressionsRequestListAuditSuppressionsPaginateModel(BaseModel):
    check_name: Optional[str] = Field(default=None, alias="checkName")
    resource_identifier: Optional[ResourceIdentifierModel] = Field(
        default=None, alias="resourceIdentifier"
    )
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAuditSuppressionsRequestModel(BaseModel):
    check_name: Optional[str] = Field(default=None, alias="checkName")
    resource_identifier: Optional[ResourceIdentifierModel] = Field(
        default=None, alias="resourceIdentifier"
    )
    ascending_order: Optional[bool] = Field(default=None, alias="ascendingOrder")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class NonCompliantResourceModel(BaseModel):
    resource_type: Optional[
        Literal[
            "ACCOUNT_SETTINGS",
            "CA_CERTIFICATE",
            "CLIENT_ID",
            "COGNITO_IDENTITY_POOL",
            "DEVICE_CERTIFICATE",
            "IAM_ROLE",
            "IOT_POLICY",
            "ISSUER_CERTIFICATE",
            "ROLE_ALIAS",
        ]
    ] = Field(default=None, alias="resourceType")
    resource_identifier: Optional[ResourceIdentifierModel] = Field(
        default=None, alias="resourceIdentifier"
    )
    additional_info: Optional[Dict[str, str]] = Field(
        default=None, alias="additionalInfo"
    )


class RelatedResourceModel(BaseModel):
    resource_type: Optional[
        Literal[
            "ACCOUNT_SETTINGS",
            "CA_CERTIFICATE",
            "CLIENT_ID",
            "COGNITO_IDENTITY_POOL",
            "DEVICE_CERTIFICATE",
            "IAM_ROLE",
            "IOT_POLICY",
            "ISSUER_CERTIFICATE",
            "ROLE_ALIAS",
        ]
    ] = Field(default=None, alias="resourceType")
    resource_identifier: Optional[ResourceIdentifierModel] = Field(
        default=None, alias="resourceIdentifier"
    )
    additional_info: Optional[Dict[str, str]] = Field(
        default=None, alias="additionalInfo"
    )


class UpdateAuditSuppressionRequestModel(BaseModel):
    check_name: str = Field(alias="checkName")
    resource_identifier: ResourceIdentifierModel = Field(alias="resourceIdentifier")
    expiration_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="expirationDate"
    )
    suppress_indefinitely: Optional[bool] = Field(
        default=None, alias="suppressIndefinitely"
    )
    description: Optional[str] = Field(default=None, alias="description")


class SearchIndexResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    things: List[ThingDocumentModel] = Field(alias="things")
    thing_groups: List[ThingGroupDocumentModel] = Field(alias="thingGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTopicRuleDestinationRequestModel(BaseModel):
    destination_configuration: TopicRuleDestinationConfigurationModel = Field(
        alias="destinationConfiguration"
    )


class ListTopicRuleDestinationsResponseModel(BaseModel):
    destination_summaries: List[TopicRuleDestinationSummaryModel] = Field(
        alias="destinationSummaries"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTopicRuleDestinationResponseModel(BaseModel):
    topic_rule_destination: TopicRuleDestinationModel = Field(
        alias="topicRuleDestination"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTopicRuleDestinationResponseModel(BaseModel):
    topic_rule_destination: TopicRuleDestinationModel = Field(
        alias="topicRuleDestination"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuthResultModel(BaseModel):
    auth_info: Optional[AuthInfoModel] = Field(default=None, alias="authInfo")
    allowed: Optional[AllowedModel] = Field(default=None, alias="allowed")
    denied: Optional[DeniedModel] = Field(default=None, alias="denied")
    auth_decision: Optional[
        Literal["ALLOWED", "EXPLICIT_DENY", "IMPLICIT_DENY"]
    ] = Field(default=None, alias="authDecision")
    missing_context_values: Optional[List[str]] = Field(
        default=None, alias="missingContextValues"
    )


class IotSiteWiseActionModel(BaseModel):
    put_asset_property_value_entries: Sequence[PutAssetPropertyValueEntryModel] = Field(
        alias="putAssetPropertyValueEntries"
    )
    role_arn: str = Field(alias="roleArn")


class ActiveViolationModel(BaseModel):
    violation_id: Optional[str] = Field(default=None, alias="violationId")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior: Optional[BehaviorModel] = Field(default=None, alias="behavior")
    last_violation_value: Optional[MetricValueModel] = Field(
        default=None, alias="lastViolationValue"
    )
    violation_event_additional_info: Optional[
        ViolationEventAdditionalInfoModel
    ] = Field(default=None, alias="violationEventAdditionalInfo")
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="verificationState")
    verification_state_description: Optional[str] = Field(
        default=None, alias="verificationStateDescription"
    )
    last_violation_time: Optional[datetime] = Field(
        default=None, alias="lastViolationTime"
    )
    violation_start_time: Optional[datetime] = Field(
        default=None, alias="violationStartTime"
    )


class CreateSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    security_profile_description: Optional[str] = Field(
        default=None, alias="securityProfileDescription"
    )
    behaviors: Optional[Sequence[BehaviorModel]] = Field(
        default=None, alias="behaviors"
    )
    alert_targets: Optional[Mapping[Literal["SNS"], AlertTargetModel]] = Field(
        default=None, alias="alertTargets"
    )
    additional_metrics_to_retain: Optional[Sequence[str]] = Field(
        default=None, alias="additionalMetricsToRetain"
    )
    additional_metrics_to_retain_v2: Optional[Sequence[MetricToRetainModel]] = Field(
        default=None, alias="additionalMetricsToRetainV2"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class DescribeSecurityProfileResponseModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    security_profile_arn: str = Field(alias="securityProfileArn")
    security_profile_description: str = Field(alias="securityProfileDescription")
    behaviors: List[BehaviorModel] = Field(alias="behaviors")
    alert_targets: Dict[Literal["SNS"], AlertTargetModel] = Field(alias="alertTargets")
    additional_metrics_to_retain: List[str] = Field(alias="additionalMetricsToRetain")
    additional_metrics_to_retain_v2: List[MetricToRetainModel] = Field(
        alias="additionalMetricsToRetainV2"
    )
    version: int = Field(alias="version")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSecurityProfileRequestModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    security_profile_description: Optional[str] = Field(
        default=None, alias="securityProfileDescription"
    )
    behaviors: Optional[Sequence[BehaviorModel]] = Field(
        default=None, alias="behaviors"
    )
    alert_targets: Optional[Mapping[Literal["SNS"], AlertTargetModel]] = Field(
        default=None, alias="alertTargets"
    )
    additional_metrics_to_retain: Optional[Sequence[str]] = Field(
        default=None, alias="additionalMetricsToRetain"
    )
    additional_metrics_to_retain_v2: Optional[Sequence[MetricToRetainModel]] = Field(
        default=None, alias="additionalMetricsToRetainV2"
    )
    delete_behaviors: Optional[bool] = Field(default=None, alias="deleteBehaviors")
    delete_alert_targets: Optional[bool] = Field(
        default=None, alias="deleteAlertTargets"
    )
    delete_additional_metrics_to_retain: Optional[bool] = Field(
        default=None, alias="deleteAdditionalMetricsToRetain"
    )
    expected_version: Optional[int] = Field(default=None, alias="expectedVersion")


class UpdateSecurityProfileResponseModel(BaseModel):
    security_profile_name: str = Field(alias="securityProfileName")
    security_profile_arn: str = Field(alias="securityProfileArn")
    security_profile_description: str = Field(alias="securityProfileDescription")
    behaviors: List[BehaviorModel] = Field(alias="behaviors")
    alert_targets: Dict[Literal["SNS"], AlertTargetModel] = Field(alias="alertTargets")
    additional_metrics_to_retain: List[str] = Field(alias="additionalMetricsToRetain")
    additional_metrics_to_retain_v2: List[MetricToRetainModel] = Field(
        alias="additionalMetricsToRetainV2"
    )
    version: int = Field(alias="version")
    creation_date: datetime = Field(alias="creationDate")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ValidateSecurityProfileBehaviorsRequestModel(BaseModel):
    behaviors: Sequence[BehaviorModel] = Field(alias="behaviors")


class ViolationEventModel(BaseModel):
    violation_id: Optional[str] = Field(default=None, alias="violationId")
    thing_name: Optional[str] = Field(default=None, alias="thingName")
    security_profile_name: Optional[str] = Field(
        default=None, alias="securityProfileName"
    )
    behavior: Optional[BehaviorModel] = Field(default=None, alias="behavior")
    metric_value: Optional[MetricValueModel] = Field(default=None, alias="metricValue")
    violation_event_additional_info: Optional[
        ViolationEventAdditionalInfoModel
    ] = Field(default=None, alias="violationEventAdditionalInfo")
    violation_event_type: Optional[
        Literal["alarm-cleared", "alarm-invalidated", "in-alarm"]
    ] = Field(default=None, alias="violationEventType")
    verification_state: Optional[
        Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
    ] = Field(default=None, alias="verificationState")
    verification_state_description: Optional[str] = Field(
        default=None, alias="verificationStateDescription"
    )
    violation_event_time: Optional[datetime] = Field(
        default=None, alias="violationEventTime"
    )


class CodeSigningModel(BaseModel):
    aws_signer_job_id: Optional[str] = Field(default=None, alias="awsSignerJobId")
    start_signing_job_parameter: Optional[StartSigningJobParameterModel] = Field(
        default=None, alias="startSigningJobParameter"
    )
    custom_code_signing: Optional[CustomCodeSigningModel] = Field(
        default=None, alias="customCodeSigning"
    )


class CreateJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    targets: Sequence[str] = Field(alias="targets")
    document_source: Optional[str] = Field(default=None, alias="documentSource")
    document: Optional[str] = Field(default=None, alias="document")
    description: Optional[str] = Field(default=None, alias="description")
    presigned_url_config: Optional[PresignedUrlConfigModel] = Field(
        default=None, alias="presignedUrlConfig"
    )
    target_selection: Optional[Literal["CONTINUOUS", "SNAPSHOT"]] = Field(
        default=None, alias="targetSelection"
    )
    job_executions_rollout_config: Optional[JobExecutionsRolloutConfigModel] = Field(
        default=None, alias="jobExecutionsRolloutConfig"
    )
    abort_config: Optional[AbortConfigModel] = Field(default=None, alias="abortConfig")
    timeout_config: Optional[TimeoutConfigModel] = Field(
        default=None, alias="timeoutConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")
    job_template_arn: Optional[str] = Field(default=None, alias="jobTemplateArn")
    job_executions_retry_config: Optional[JobExecutionsRetryConfigModel] = Field(
        default=None, alias="jobExecutionsRetryConfig"
    )
    document_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="documentParameters"
    )
    scheduling_config: Optional[SchedulingConfigModel] = Field(
        default=None, alias="schedulingConfig"
    )


class CreateJobTemplateRequestModel(BaseModel):
    job_template_id: str = Field(alias="jobTemplateId")
    description: str = Field(alias="description")
    job_arn: Optional[str] = Field(default=None, alias="jobArn")
    document_source: Optional[str] = Field(default=None, alias="documentSource")
    document: Optional[str] = Field(default=None, alias="document")
    presigned_url_config: Optional[PresignedUrlConfigModel] = Field(
        default=None, alias="presignedUrlConfig"
    )
    job_executions_rollout_config: Optional[JobExecutionsRolloutConfigModel] = Field(
        default=None, alias="jobExecutionsRolloutConfig"
    )
    abort_config: Optional[AbortConfigModel] = Field(default=None, alias="abortConfig")
    timeout_config: Optional[TimeoutConfigModel] = Field(
        default=None, alias="timeoutConfig"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")
    job_executions_retry_config: Optional[JobExecutionsRetryConfigModel] = Field(
        default=None, alias="jobExecutionsRetryConfig"
    )


class DescribeJobTemplateResponseModel(BaseModel):
    job_template_arn: str = Field(alias="jobTemplateArn")
    job_template_id: str = Field(alias="jobTemplateId")
    description: str = Field(alias="description")
    document_source: str = Field(alias="documentSource")
    document: str = Field(alias="document")
    created_at: datetime = Field(alias="createdAt")
    presigned_url_config: PresignedUrlConfigModel = Field(alias="presignedUrlConfig")
    job_executions_rollout_config: JobExecutionsRolloutConfigModel = Field(
        alias="jobExecutionsRolloutConfig"
    )
    abort_config: AbortConfigModel = Field(alias="abortConfig")
    timeout_config: TimeoutConfigModel = Field(alias="timeoutConfig")
    job_executions_retry_config: JobExecutionsRetryConfigModel = Field(
        alias="jobExecutionsRetryConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobModel(BaseModel):
    job_arn: Optional[str] = Field(default=None, alias="jobArn")
    job_id: Optional[str] = Field(default=None, alias="jobId")
    target_selection: Optional[Literal["CONTINUOUS", "SNAPSHOT"]] = Field(
        default=None, alias="targetSelection"
    )
    status: Optional[
        Literal[
            "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS", "IN_PROGRESS", "SCHEDULED"
        ]
    ] = Field(default=None, alias="status")
    force_canceled: Optional[bool] = Field(default=None, alias="forceCanceled")
    reason_code: Optional[str] = Field(default=None, alias="reasonCode")
    comment: Optional[str] = Field(default=None, alias="comment")
    targets: Optional[List[str]] = Field(default=None, alias="targets")
    description: Optional[str] = Field(default=None, alias="description")
    presigned_url_config: Optional[PresignedUrlConfigModel] = Field(
        default=None, alias="presignedUrlConfig"
    )
    job_executions_rollout_config: Optional[JobExecutionsRolloutConfigModel] = Field(
        default=None, alias="jobExecutionsRolloutConfig"
    )
    abort_config: Optional[AbortConfigModel] = Field(default=None, alias="abortConfig")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="lastUpdatedAt")
    completed_at: Optional[datetime] = Field(default=None, alias="completedAt")
    job_process_details: Optional[JobProcessDetailsModel] = Field(
        default=None, alias="jobProcessDetails"
    )
    timeout_config: Optional[TimeoutConfigModel] = Field(
        default=None, alias="timeoutConfig"
    )
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")
    job_template_arn: Optional[str] = Field(default=None, alias="jobTemplateArn")
    job_executions_retry_config: Optional[JobExecutionsRetryConfigModel] = Field(
        default=None, alias="jobExecutionsRetryConfig"
    )
    document_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="documentParameters"
    )
    is_concurrent: Optional[bool] = Field(default=None, alias="isConcurrent")
    scheduling_config: Optional[SchedulingConfigModel] = Field(
        default=None, alias="schedulingConfig"
    )


class UpdateJobRequestModel(BaseModel):
    job_id: str = Field(alias="jobId")
    description: Optional[str] = Field(default=None, alias="description")
    presigned_url_config: Optional[PresignedUrlConfigModel] = Field(
        default=None, alias="presignedUrlConfig"
    )
    job_executions_rollout_config: Optional[JobExecutionsRolloutConfigModel] = Field(
        default=None, alias="jobExecutionsRolloutConfig"
    )
    abort_config: Optional[AbortConfigModel] = Field(default=None, alias="abortConfig")
    timeout_config: Optional[TimeoutConfigModel] = Field(
        default=None, alias="timeoutConfig"
    )
    namespace_id: Optional[str] = Field(default=None, alias="namespaceId")
    job_executions_retry_config: Optional[JobExecutionsRetryConfigModel] = Field(
        default=None, alias="jobExecutionsRetryConfig"
    )


class DescribeStreamResponseModel(BaseModel):
    stream_info: StreamInfoModel = Field(alias="streamInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAuditMitigationActionsTaskResponseModel(BaseModel):
    task_status: Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"] = Field(
        alias="taskStatus"
    )
    start_time: datetime = Field(alias="startTime")
    end_time: datetime = Field(alias="endTime")
    task_statistics: Dict[str, TaskStatisticsForAuditCheckModel] = Field(
        alias="taskStatistics"
    )
    target: AuditMitigationActionsTaskTargetModel = Field(alias="target")
    audit_check_to_actions_mapping: Dict[str, List[str]] = Field(
        alias="auditCheckToActionsMapping"
    )
    actions_definition: List[MitigationActionModel] = Field(alias="actionsDefinition")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectMitigationActionsTaskSummaryModel(BaseModel):
    task_id: Optional[str] = Field(default=None, alias="taskId")
    task_status: Optional[
        Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCESSFUL"]
    ] = Field(default=None, alias="taskStatus")
    task_start_time: Optional[datetime] = Field(default=None, alias="taskStartTime")
    task_end_time: Optional[datetime] = Field(default=None, alias="taskEndTime")
    target: Optional[DetectMitigationActionsTaskTargetModel] = Field(
        default=None, alias="target"
    )
    violation_event_occurrence_range: Optional[
        ViolationEventOccurrenceRangeModel
    ] = Field(default=None, alias="violationEventOccurrenceRange")
    only_active_violations_included: Optional[bool] = Field(
        default=None, alias="onlyActiveViolationsIncluded"
    )
    suppressed_alerts_included: Optional[bool] = Field(
        default=None, alias="suppressedAlertsIncluded"
    )
    actions_definition: Optional[List[MitigationActionModel]] = Field(
        default=None, alias="actionsDefinition"
    )
    task_statistics: Optional[DetectMitigationActionsTaskStatisticsModel] = Field(
        default=None, alias="taskStatistics"
    )


class ListAuditSuppressionsResponseModel(BaseModel):
    suppressions: List[AuditSuppressionModel] = Field(alias="suppressions")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AuditFindingModel(BaseModel):
    finding_id: Optional[str] = Field(default=None, alias="findingId")
    task_id: Optional[str] = Field(default=None, alias="taskId")
    check_name: Optional[str] = Field(default=None, alias="checkName")
    task_start_time: Optional[datetime] = Field(default=None, alias="taskStartTime")
    finding_time: Optional[datetime] = Field(default=None, alias="findingTime")
    severity: Optional[Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]] = Field(
        default=None, alias="severity"
    )
    non_compliant_resource: Optional[NonCompliantResourceModel] = Field(
        default=None, alias="nonCompliantResource"
    )
    related_resources: Optional[List[RelatedResourceModel]] = Field(
        default=None, alias="relatedResources"
    )
    reason_for_non_compliance: Optional[str] = Field(
        default=None, alias="reasonForNonCompliance"
    )
    reason_for_non_compliance_code: Optional[str] = Field(
        default=None, alias="reasonForNonComplianceCode"
    )
    is_suppressed: Optional[bool] = Field(default=None, alias="isSuppressed")


class ListRelatedResourcesForAuditFindingResponseModel(BaseModel):
    related_resources: List[RelatedResourceModel] = Field(alias="relatedResources")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestAuthorizationResponseModel(BaseModel):
    auth_results: List[AuthResultModel] = Field(alias="authResults")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionModel(BaseModel):
    dynamo_db: Optional[DynamoDBActionModel] = Field(default=None, alias="dynamoDB")
    dynamo_dbv2: Optional[DynamoDBv2ActionModel] = Field(
        default=None, alias="dynamoDBv2"
    )
    lambda_: Optional[LambdaActionModel] = Field(default=None, alias="lambda")
    sns: Optional[SnsActionModel] = Field(default=None, alias="sns")
    sqs: Optional[SqsActionModel] = Field(default=None, alias="sqs")
    kinesis: Optional[KinesisActionModel] = Field(default=None, alias="kinesis")
    republish: Optional[RepublishActionModel] = Field(default=None, alias="republish")
    s3: Optional[S3ActionModel] = Field(default=None, alias="s3")
    firehose: Optional[FirehoseActionModel] = Field(default=None, alias="firehose")
    cloudwatch_metric: Optional[CloudwatchMetricActionModel] = Field(
        default=None, alias="cloudwatchMetric"
    )
    cloudwatch_alarm: Optional[CloudwatchAlarmActionModel] = Field(
        default=None, alias="cloudwatchAlarm"
    )
    cloudwatch_logs: Optional[CloudwatchLogsActionModel] = Field(
        default=None, alias="cloudwatchLogs"
    )
    elasticsearch: Optional[ElasticsearchActionModel] = Field(
        default=None, alias="elasticsearch"
    )
    salesforce: Optional[SalesforceActionModel] = Field(
        default=None, alias="salesforce"
    )
    iot_analytics: Optional[IotAnalyticsActionModel] = Field(
        default=None, alias="iotAnalytics"
    )
    iot_events: Optional[IotEventsActionModel] = Field(default=None, alias="iotEvents")
    iot_site_wise: Optional[IotSiteWiseActionModel] = Field(
        default=None, alias="iotSiteWise"
    )
    step_functions: Optional[StepFunctionsActionModel] = Field(
        default=None, alias="stepFunctions"
    )
    timestream: Optional[TimestreamActionModel] = Field(
        default=None, alias="timestream"
    )
    http: Optional[HttpActionModel] = Field(default=None, alias="http")
    kafka: Optional[KafkaActionModel] = Field(default=None, alias="kafka")
    open_search: Optional[OpenSearchActionModel] = Field(
        default=None, alias="openSearch"
    )
    location: Optional[LocationActionModel] = Field(default=None, alias="location")


class ListActiveViolationsResponseModel(BaseModel):
    active_violations: List[ActiveViolationModel] = Field(alias="activeViolations")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListViolationEventsResponseModel(BaseModel):
    violation_events: List[ViolationEventModel] = Field(alias="violationEvents")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OTAUpdateFileModel(BaseModel):
    file_name: Optional[str] = Field(default=None, alias="fileName")
    file_type: Optional[int] = Field(default=None, alias="fileType")
    file_version: Optional[str] = Field(default=None, alias="fileVersion")
    file_location: Optional[FileLocationModel] = Field(
        default=None, alias="fileLocation"
    )
    code_signing: Optional[CodeSigningModel] = Field(default=None, alias="codeSigning")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="attributes")


class DescribeJobResponseModel(BaseModel):
    document_source: str = Field(alias="documentSource")
    job: JobModel = Field(alias="job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDetectMitigationActionsTaskResponseModel(BaseModel):
    task_summary: DetectMitigationActionsTaskSummaryModel = Field(alias="taskSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDetectMitigationActionsTasksResponseModel(BaseModel):
    tasks: List[DetectMitigationActionsTaskSummaryModel] = Field(alias="tasks")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAuditFindingResponseModel(BaseModel):
    finding: AuditFindingModel = Field(alias="finding")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAuditFindingsResponseModel(BaseModel):
    findings: List[AuditFindingModel] = Field(alias="findings")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TopicRulePayloadModel(BaseModel):
    sql: str = Field(alias="sql")
    actions: Sequence[ActionModel] = Field(alias="actions")
    description: Optional[str] = Field(default=None, alias="description")
    rule_disabled: Optional[bool] = Field(default=None, alias="ruleDisabled")
    aws_iot_sql_version: Optional[str] = Field(default=None, alias="awsIotSqlVersion")
    error_action: Optional[ActionModel] = Field(default=None, alias="errorAction")


class TopicRuleModel(BaseModel):
    rule_name: Optional[str] = Field(default=None, alias="ruleName")
    sql: Optional[str] = Field(default=None, alias="sql")
    description: Optional[str] = Field(default=None, alias="description")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    actions: Optional[List[ActionModel]] = Field(default=None, alias="actions")
    rule_disabled: Optional[bool] = Field(default=None, alias="ruleDisabled")
    aws_iot_sql_version: Optional[str] = Field(default=None, alias="awsIotSqlVersion")
    error_action: Optional[ActionModel] = Field(default=None, alias="errorAction")


class CreateOTAUpdateRequestModel(BaseModel):
    ota_update_id: str = Field(alias="otaUpdateId")
    targets: Sequence[str] = Field(alias="targets")
    files: Sequence[OTAUpdateFileModel] = Field(alias="files")
    role_arn: str = Field(alias="roleArn")
    description: Optional[str] = Field(default=None, alias="description")
    protocols: Optional[Sequence[Literal["HTTP", "MQTT"]]] = Field(
        default=None, alias="protocols"
    )
    target_selection: Optional[Literal["CONTINUOUS", "SNAPSHOT"]] = Field(
        default=None, alias="targetSelection"
    )
    aws_job_executions_rollout_config: Optional[
        AwsJobExecutionsRolloutConfigModel
    ] = Field(default=None, alias="awsJobExecutionsRolloutConfig")
    aws_job_presigned_url_config: Optional[AwsJobPresignedUrlConfigModel] = Field(
        default=None, alias="awsJobPresignedUrlConfig"
    )
    aws_job_abort_config: Optional[AwsJobAbortConfigModel] = Field(
        default=None, alias="awsJobAbortConfig"
    )
    aws_job_timeout_config: Optional[AwsJobTimeoutConfigModel] = Field(
        default=None, alias="awsJobTimeoutConfig"
    )
    additional_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="additionalParameters"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class OTAUpdateInfoModel(BaseModel):
    ota_update_id: Optional[str] = Field(default=None, alias="otaUpdateId")
    ota_update_arn: Optional[str] = Field(default=None, alias="otaUpdateArn")
    creation_date: Optional[datetime] = Field(default=None, alias="creationDate")
    last_modified_date: Optional[datetime] = Field(
        default=None, alias="lastModifiedDate"
    )
    description: Optional[str] = Field(default=None, alias="description")
    targets: Optional[List[str]] = Field(default=None, alias="targets")
    protocols: Optional[List[Literal["HTTP", "MQTT"]]] = Field(
        default=None, alias="protocols"
    )
    aws_job_executions_rollout_config: Optional[
        AwsJobExecutionsRolloutConfigModel
    ] = Field(default=None, alias="awsJobExecutionsRolloutConfig")
    aws_job_presigned_url_config: Optional[AwsJobPresignedUrlConfigModel] = Field(
        default=None, alias="awsJobPresignedUrlConfig"
    )
    target_selection: Optional[Literal["CONTINUOUS", "SNAPSHOT"]] = Field(
        default=None, alias="targetSelection"
    )
    ota_update_files: Optional[List[OTAUpdateFileModel]] = Field(
        default=None, alias="otaUpdateFiles"
    )
    ota_update_status: Optional[
        Literal[
            "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_PENDING"
        ]
    ] = Field(default=None, alias="otaUpdateStatus")
    aws_iot_job_id: Optional[str] = Field(default=None, alias="awsIotJobId")
    aws_iot_job_arn: Optional[str] = Field(default=None, alias="awsIotJobArn")
    error_info: Optional[ErrorInfoModel] = Field(default=None, alias="errorInfo")
    additional_parameters: Optional[Dict[str, str]] = Field(
        default=None, alias="additionalParameters"
    )


class CreateTopicRuleRequestModel(BaseModel):
    rule_name: str = Field(alias="ruleName")
    topic_rule_payload: TopicRulePayloadModel = Field(alias="topicRulePayload")
    tags: Optional[str] = Field(default=None, alias="tags")


class ReplaceTopicRuleRequestModel(BaseModel):
    rule_name: str = Field(alias="ruleName")
    topic_rule_payload: TopicRulePayloadModel = Field(alias="topicRulePayload")


class GetTopicRuleResponseModel(BaseModel):
    rule_arn: str = Field(alias="ruleArn")
    rule: TopicRuleModel = Field(alias="rule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOTAUpdateResponseModel(BaseModel):
    ota_update_info: OTAUpdateInfoModel = Field(alias="otaUpdateInfo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
