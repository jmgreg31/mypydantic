# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddProfileKeyRequestModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    key_name: str = Field(alias="KeyName")
    values: Sequence[str] = Field(alias="Values")
    domain_name: str = Field(alias="DomainName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class AdditionalSearchKeyModel(BaseModel):
    key_name: str = Field(alias="KeyName")
    values: Sequence[str] = Field(alias="Values")


class AddressModel(BaseModel):
    address1: Optional[str] = Field(default=None, alias="Address1")
    address2: Optional[str] = Field(default=None, alias="Address2")
    address3: Optional[str] = Field(default=None, alias="Address3")
    address4: Optional[str] = Field(default=None, alias="Address4")
    city: Optional[str] = Field(default=None, alias="City")
    county: Optional[str] = Field(default=None, alias="County")
    state: Optional[str] = Field(default=None, alias="State")
    province: Optional[str] = Field(default=None, alias="Province")
    country: Optional[str] = Field(default=None, alias="Country")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")


class BatchModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")


class AppflowIntegrationWorkflowAttributesModel(BaseModel):
    source_connector_type: Literal[
        "Marketo", "S3", "Salesforce", "Servicenow", "Zendesk"
    ] = Field(alias="SourceConnectorType")
    connector_profile_name: str = Field(alias="ConnectorProfileName")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class AppflowIntegrationWorkflowMetricsModel(BaseModel):
    records_processed: int = Field(alias="RecordsProcessed")
    steps_completed: int = Field(alias="StepsCompleted")
    total_steps: int = Field(alias="TotalSteps")


class AppflowIntegrationWorkflowStepModel(BaseModel):
    flow_name: str = Field(alias="FlowName")
    status: Literal[
        "CANCELLED",
        "COMPLETE",
        "FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "RETRY",
        "SPLIT",
    ] = Field(alias="Status")
    execution_message: str = Field(alias="ExecutionMessage")
    records_processed: int = Field(alias="RecordsProcessed")
    batch_records_start_time: str = Field(alias="BatchRecordsStartTime")
    batch_records_end_time: str = Field(alias="BatchRecordsEndTime")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")


class ConflictResolutionModel(BaseModel):
    conflict_resolving_model: Literal["RECENCY", "SOURCE"] = Field(
        alias="ConflictResolvingModel"
    )
    source_name: Optional[str] = Field(default=None, alias="SourceName")


class ConsolidationModel(BaseModel):
    matching_attributes_list: Sequence[Sequence[str]] = Field(
        alias="MatchingAttributesList"
    )


class ConnectorOperatorModel(BaseModel):
    marketo: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "GREATER_THAN",
            "LESS_THAN",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Marketo")
    s3: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="S3")
    salesforce: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Salesforce")
    service_now: Optional[
        Literal[
            "ADDITION",
            "BETWEEN",
            "CONTAINS",
            "DIVISION",
            "EQUAL_TO",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUAL_TO",
            "LESS_THAN",
            "LESS_THAN_OR_EQUAL_TO",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NOT_EQUAL_TO",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="ServiceNow")
    zendesk: Optional[
        Literal[
            "ADDITION",
            "DIVISION",
            "GREATER_THAN",
            "MASK_ALL",
            "MASK_FIRST_N",
            "MASK_LAST_N",
            "MULTIPLICATION",
            "NO_OP",
            "PROJECTION",
            "SUBTRACTION",
            "VALIDATE_NON_NEGATIVE",
            "VALIDATE_NON_NULL",
            "VALIDATE_NON_ZERO",
            "VALIDATE_NUMERIC",
        ]
    ] = Field(default=None, alias="Zendesk")


class DeleteDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class DeleteIntegrationRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    uri: str = Field(alias="Uri")


class DeleteProfileKeyRequestModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    key_name: str = Field(alias="KeyName")
    values: Sequence[str] = Field(alias="Values")
    domain_name: str = Field(alias="DomainName")


class DeleteProfileObjectRequestModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    profile_object_unique_key: str = Field(alias="ProfileObjectUniqueKey")
    object_type_name: str = Field(alias="ObjectTypeName")
    domain_name: str = Field(alias="DomainName")


class DeleteProfileObjectTypeRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    object_type_name: str = Field(alias="ObjectTypeName")


class DeleteProfileRequestModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    domain_name: str = Field(alias="DomainName")


class DeleteWorkflowRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    workflow_id: str = Field(alias="WorkflowId")


class DomainStatsModel(BaseModel):
    profile_count: Optional[int] = Field(default=None, alias="ProfileCount")
    metering_profile_count: Optional[int] = Field(
        default=None, alias="MeteringProfileCount"
    )
    object_count: Optional[int] = Field(default=None, alias="ObjectCount")
    total_size: Optional[int] = Field(default=None, alias="TotalSize")


class S3ExportingConfigModel(BaseModel):
    s3_bucket_name: str = Field(alias="S3BucketName")
    s3_key_name: Optional[str] = Field(default=None, alias="S3KeyName")


class S3ExportingLocationModel(BaseModel):
    s3_bucket_name: Optional[str] = Field(default=None, alias="S3BucketName")
    s3_key_name: Optional[str] = Field(default=None, alias="S3KeyName")


class FieldSourceProfileIdsModel(BaseModel):
    account_number: Optional[str] = Field(default=None, alias="AccountNumber")
    additional_information: Optional[str] = Field(
        default=None, alias="AdditionalInformation"
    )
    party_type: Optional[str] = Field(default=None, alias="PartyType")
    business_name: Optional[str] = Field(default=None, alias="BusinessName")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    middle_name: Optional[str] = Field(default=None, alias="MiddleName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    birth_date: Optional[str] = Field(default=None, alias="BirthDate")
    gender: Optional[str] = Field(default=None, alias="Gender")
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    mobile_phone_number: Optional[str] = Field(default=None, alias="MobilePhoneNumber")
    home_phone_number: Optional[str] = Field(default=None, alias="HomePhoneNumber")
    business_phone_number: Optional[str] = Field(
        default=None, alias="BusinessPhoneNumber"
    )
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    personal_email_address: Optional[str] = Field(
        default=None, alias="PersonalEmailAddress"
    )
    business_email_address: Optional[str] = Field(
        default=None, alias="BusinessEmailAddress"
    )
    address: Optional[str] = Field(default=None, alias="Address")
    shipping_address: Optional[str] = Field(default=None, alias="ShippingAddress")
    mailing_address: Optional[str] = Field(default=None, alias="MailingAddress")
    billing_address: Optional[str] = Field(default=None, alias="BillingAddress")
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")


class FoundByKeyValueModel(BaseModel):
    key_name: Optional[str] = Field(default=None, alias="KeyName")
    values: Optional[List[str]] = Field(default=None, alias="Values")


class GetDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")


class GetIdentityResolutionJobRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    job_id: str = Field(alias="JobId")


class JobStatsModel(BaseModel):
    number_of_profiles_reviewed: Optional[int] = Field(
        default=None, alias="NumberOfProfilesReviewed"
    )
    number_of_matches_found: Optional[int] = Field(
        default=None, alias="NumberOfMatchesFound"
    )
    number_of_merges_done: Optional[int] = Field(
        default=None, alias="NumberOfMergesDone"
    )


class GetIntegrationRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    uri: str = Field(alias="Uri")


class GetMatchesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MatchItemModel(BaseModel):
    match_id: Optional[str] = Field(default=None, alias="MatchId")
    profile_ids: Optional[List[str]] = Field(default=None, alias="ProfileIds")
    confidence_score: Optional[float] = Field(default=None, alias="ConfidenceScore")


class GetProfileObjectTypeRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    object_type_name: str = Field(alias="ObjectTypeName")


class ObjectTypeFieldModel(BaseModel):
    source: Optional[str] = Field(default=None, alias="Source")
    target: Optional[str] = Field(default=None, alias="Target")
    content_type: Optional[
        Literal["EMAIL_ADDRESS", "NAME", "NUMBER", "PHONE_NUMBER", "STRING"]
    ] = Field(default=None, alias="ContentType")


class ObjectTypeKeyModel(BaseModel):
    standard_identifiers: Optional[
        List[
            Literal[
                "ASSET",
                "CASE",
                "LOOKUP_ONLY",
                "NEW_ONLY",
                "ORDER",
                "PROFILE",
                "SECONDARY",
                "UNIQUE",
            ]
        ]
    ] = Field(default=None, alias="StandardIdentifiers")
    field_names: Optional[List[str]] = Field(default=None, alias="FieldNames")


class GetProfileObjectTypeTemplateRequestModel(BaseModel):
    template_id: str = Field(alias="TemplateId")


class GetWorkflowRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    workflow_id: str = Field(alias="WorkflowId")


class GetWorkflowStepsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    workflow_id: str = Field(alias="WorkflowId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class IncrementalPullConfigModel(BaseModel):
    datetime_type_field_name: Optional[str] = Field(
        default=None, alias="DatetimeTypeFieldName"
    )


class JobScheduleModel(BaseModel):
    day_of_the_week: Literal[
        "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
    ] = Field(alias="DayOfTheWeek")
    time: str = Field(alias="Time")


class ListAccountIntegrationsRequestModel(BaseModel):
    uri: str = Field(alias="Uri")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    include_hidden: Optional[bool] = Field(default=None, alias="IncludeHidden")


class ListIntegrationItemModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    uri: str = Field(alias="Uri")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    object_type_name: Optional[str] = Field(default=None, alias="ObjectTypeName")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")
    object_type_names: Optional[Dict[str, str]] = Field(
        default=None, alias="ObjectTypeNames"
    )
    workflow_id: Optional[str] = Field(default=None, alias="WorkflowId")
    is_unstructured: Optional[bool] = Field(default=None, alias="IsUnstructured")


class ListDomainItemModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListDomainsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIdentityResolutionJobsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIntegrationsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    include_hidden: Optional[bool] = Field(default=None, alias="IncludeHidden")


class ListProfileObjectTypeItemModel(BaseModel):
    object_type_name: str = Field(alias="ObjectTypeName")
    description: str = Field(alias="Description")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, alias="LastUpdatedAt")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class ListProfileObjectTypeTemplateItemModel(BaseModel):
    template_id: Optional[str] = Field(default=None, alias="TemplateId")
    source_name: Optional[str] = Field(default=None, alias="SourceName")
    source_object: Optional[str] = Field(default=None, alias="SourceObject")


class ListProfileObjectTypeTemplatesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListProfileObjectTypesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListProfileObjectsItemModel(BaseModel):
    object_type_name: Optional[str] = Field(default=None, alias="ObjectTypeName")
    profile_object_unique_key: Optional[str] = Field(
        default=None, alias="ProfileObjectUniqueKey"
    )
    object: Optional[str] = Field(default=None, alias="Object")


class ObjectFilterModel(BaseModel):
    key_name: str = Field(alias="KeyName")
    values: Sequence[str] = Field(alias="Values")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListWorkflowsItemModel(BaseModel):
    workflow_type: Literal["APPFLOW_INTEGRATION"] = Field(alias="WorkflowType")
    workflow_id: str = Field(alias="WorkflowId")
    status: Literal[
        "CANCELLED",
        "COMPLETE",
        "FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "RETRY",
        "SPLIT",
    ] = Field(alias="Status")
    status_description: str = Field(alias="StatusDescription")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")


class ListWorkflowsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    workflow_type: Optional[Literal["APPFLOW_INTEGRATION"]] = Field(
        default=None, alias="WorkflowType"
    )
    status: Optional[
        Literal[
            "CANCELLED",
            "COMPLETE",
            "FAILED",
            "IN_PROGRESS",
            "NOT_STARTED",
            "RETRY",
            "SPLIT",
        ]
    ] = Field(default=None, alias="Status")
    query_start_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryStartDate"
    )
    query_end_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="QueryEndDate"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MarketoSourcePropertiesModel(BaseModel):
    object: str = Field(alias="Object")


class PutProfileObjectRequestModel(BaseModel):
    object_type_name: str = Field(alias="ObjectTypeName")
    object: str = Field(alias="Object")
    domain_name: str = Field(alias="DomainName")


class S3SourcePropertiesModel(BaseModel):
    bucket_name: str = Field(alias="BucketName")
    bucket_prefix: Optional[str] = Field(default=None, alias="BucketPrefix")


class SalesforceSourcePropertiesModel(BaseModel):
    object: str = Field(alias="Object")
    enable_dynamic_field_update: Optional[bool] = Field(
        default=None, alias="EnableDynamicFieldUpdate"
    )
    include_deleted_records: Optional[bool] = Field(
        default=None, alias="IncludeDeletedRecords"
    )


class ScheduledTriggerPropertiesModel(BaseModel):
    schedule_expression: str = Field(alias="ScheduleExpression")
    data_pull_mode: Optional[Literal["Complete", "Incremental"]] = Field(
        default=None, alias="DataPullMode"
    )
    schedule_start_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduleStartTime"
    )
    schedule_end_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ScheduleEndTime"
    )
    timezone: Optional[str] = Field(default=None, alias="Timezone")
    schedule_offset: Optional[int] = Field(default=None, alias="ScheduleOffset")
    first_execution_from: Optional[Union[datetime, str]] = Field(
        default=None, alias="FirstExecutionFrom"
    )


class ServiceNowSourcePropertiesModel(BaseModel):
    object: str = Field(alias="Object")


class ZendeskSourcePropertiesModel(BaseModel):
    object: str = Field(alias="Object")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAddressModel(BaseModel):
    address1: Optional[str] = Field(default=None, alias="Address1")
    address2: Optional[str] = Field(default=None, alias="Address2")
    address3: Optional[str] = Field(default=None, alias="Address3")
    address4: Optional[str] = Field(default=None, alias="Address4")
    city: Optional[str] = Field(default=None, alias="City")
    county: Optional[str] = Field(default=None, alias="County")
    state: Optional[str] = Field(default=None, alias="State")
    province: Optional[str] = Field(default=None, alias="Province")
    country: Optional[str] = Field(default=None, alias="Country")
    postal_code: Optional[str] = Field(default=None, alias="PostalCode")


class AddProfileKeyResponseModel(BaseModel):
    key_name: str = Field(alias="KeyName")
    values: List[str] = Field(alias="Values")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIntegrationWorkflowResponseModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProfileResponseModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDomainResponseModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteIntegrationResponseModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProfileKeyResponseModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProfileObjectResponseModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProfileObjectTypeResponseModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProfileResponseModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAutoMergingPreviewResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    number_of_matches_in_sample: int = Field(alias="NumberOfMatchesInSample")
    number_of_profiles_in_sample: int = Field(alias="NumberOfProfilesInSample")
    number_of_profiles_will_be_merged: int = Field(alias="NumberOfProfilesWillBeMerged")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIntegrationResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    uri: str = Field(alias="Uri")
    object_type_name: str = Field(alias="ObjectTypeName")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Dict[str, str] = Field(alias="Tags")
    object_type_names: Dict[str, str] = Field(alias="ObjectTypeNames")
    workflow_id: str = Field(alias="WorkflowId")
    is_unstructured: bool = Field(alias="IsUnstructured")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MergeProfilesResponseModel(BaseModel):
    message: str = Field(alias="Message")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutIntegrationResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    uri: str = Field(alias="Uri")
    object_type_name: str = Field(alias="ObjectTypeName")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Dict[str, str] = Field(alias="Tags")
    object_type_names: Dict[str, str] = Field(alias="ObjectTypeNames")
    workflow_id: str = Field(alias="WorkflowId")
    is_unstructured: bool = Field(alias="IsUnstructured")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutProfileObjectResponseModel(BaseModel):
    profile_object_unique_key: str = Field(alias="ProfileObjectUniqueKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProfileResponseModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchProfilesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    key_name: str = Field(alias="KeyName")
    values: Sequence[str] = Field(alias="Values")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    additional_search_keys: Optional[Sequence[AdditionalSearchKeyModel]] = Field(
        default=None, alias="AdditionalSearchKeys"
    )
    logical_operator: Optional[Literal["AND", "OR"]] = Field(
        default=None, alias="LogicalOperator"
    )


class CreateProfileRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    account_number: Optional[str] = Field(default=None, alias="AccountNumber")
    additional_information: Optional[str] = Field(
        default=None, alias="AdditionalInformation"
    )
    party_type: Optional[Literal["BUSINESS", "INDIVIDUAL", "OTHER"]] = Field(
        default=None, alias="PartyType"
    )
    business_name: Optional[str] = Field(default=None, alias="BusinessName")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    middle_name: Optional[str] = Field(default=None, alias="MiddleName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    birth_date: Optional[str] = Field(default=None, alias="BirthDate")
    gender: Optional[Literal["FEMALE", "MALE", "UNSPECIFIED"]] = Field(
        default=None, alias="Gender"
    )
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    mobile_phone_number: Optional[str] = Field(default=None, alias="MobilePhoneNumber")
    home_phone_number: Optional[str] = Field(default=None, alias="HomePhoneNumber")
    business_phone_number: Optional[str] = Field(
        default=None, alias="BusinessPhoneNumber"
    )
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    personal_email_address: Optional[str] = Field(
        default=None, alias="PersonalEmailAddress"
    )
    business_email_address: Optional[str] = Field(
        default=None, alias="BusinessEmailAddress"
    )
    address: Optional[AddressModel] = Field(default=None, alias="Address")
    shipping_address: Optional[AddressModel] = Field(
        default=None, alias="ShippingAddress"
    )
    mailing_address: Optional[AddressModel] = Field(
        default=None, alias="MailingAddress"
    )
    billing_address: Optional[AddressModel] = Field(
        default=None, alias="BillingAddress"
    )
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    party_type_string: Optional[str] = Field(default=None, alias="PartyTypeString")
    gender_string: Optional[str] = Field(default=None, alias="GenderString")


class WorkflowAttributesModel(BaseModel):
    appflow_integration: Optional[AppflowIntegrationWorkflowAttributesModel] = Field(
        default=None, alias="AppflowIntegration"
    )


class WorkflowMetricsModel(BaseModel):
    appflow_integration: Optional[AppflowIntegrationWorkflowMetricsModel] = Field(
        default=None, alias="AppflowIntegration"
    )


class WorkflowStepItemModel(BaseModel):
    appflow_integration: Optional[AppflowIntegrationWorkflowStepModel] = Field(
        default=None, alias="AppflowIntegration"
    )


class AutoMergingModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    consolidation: Optional[ConsolidationModel] = Field(
        default=None, alias="Consolidation"
    )
    conflict_resolution: Optional[ConflictResolutionModel] = Field(
        default=None, alias="ConflictResolution"
    )
    min_allowed_confidence_score_for_merging: Optional[float] = Field(
        default=None, alias="MinAllowedConfidenceScoreForMerging"
    )


class GetAutoMergingPreviewRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    consolidation: ConsolidationModel = Field(alias="Consolidation")
    conflict_resolution: ConflictResolutionModel = Field(alias="ConflictResolution")
    min_allowed_confidence_score_for_merging: Optional[float] = Field(
        default=None, alias="MinAllowedConfidenceScoreForMerging"
    )


class TaskModel(BaseModel):
    source_fields: Sequence[str] = Field(alias="SourceFields")
    task_type: Literal[
        "Arithmetic", "Filter", "Map", "Mask", "Merge", "Truncate", "Validate"
    ] = Field(alias="TaskType")
    connector_operator: Optional[ConnectorOperatorModel] = Field(
        default=None, alias="ConnectorOperator"
    )
    destination_field: Optional[str] = Field(default=None, alias="DestinationField")
    task_properties: Optional[
        Mapping[
            Literal[
                "CONCAT_FORMAT",
                "DATA_TYPE",
                "DESTINATION_DATA_TYPE",
                "LOWER_BOUND",
                "MASK_LENGTH",
                "MASK_VALUE",
                "MATH_OPERATION_FIELDS_ORDER",
                "SOURCE_DATA_TYPE",
                "SUBFIELD_CATEGORY_MAP",
                "TRUNCATE_LENGTH",
                "UPPER_BOUND",
                "VALIDATION_ACTION",
                "VALUE",
                "VALUES",
            ],
            str,
        ]
    ] = Field(default=None, alias="TaskProperties")


class ExportingConfigModel(BaseModel):
    s3_exporting: Optional[S3ExportingConfigModel] = Field(
        default=None, alias="S3Exporting"
    )


class ExportingLocationModel(BaseModel):
    s3_exporting: Optional[S3ExportingLocationModel] = Field(
        default=None, alias="S3Exporting"
    )


class MergeProfilesRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    main_profile_id: str = Field(alias="MainProfileId")
    profile_ids_to_be_merged: Sequence[str] = Field(alias="ProfileIdsToBeMerged")
    field_source_profile_ids: Optional[FieldSourceProfileIdsModel] = Field(
        default=None, alias="FieldSourceProfileIds"
    )


class ProfileModel(BaseModel):
    profile_id: Optional[str] = Field(default=None, alias="ProfileId")
    account_number: Optional[str] = Field(default=None, alias="AccountNumber")
    additional_information: Optional[str] = Field(
        default=None, alias="AdditionalInformation"
    )
    party_type: Optional[Literal["BUSINESS", "INDIVIDUAL", "OTHER"]] = Field(
        default=None, alias="PartyType"
    )
    business_name: Optional[str] = Field(default=None, alias="BusinessName")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    middle_name: Optional[str] = Field(default=None, alias="MiddleName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    birth_date: Optional[str] = Field(default=None, alias="BirthDate")
    gender: Optional[Literal["FEMALE", "MALE", "UNSPECIFIED"]] = Field(
        default=None, alias="Gender"
    )
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    mobile_phone_number: Optional[str] = Field(default=None, alias="MobilePhoneNumber")
    home_phone_number: Optional[str] = Field(default=None, alias="HomePhoneNumber")
    business_phone_number: Optional[str] = Field(
        default=None, alias="BusinessPhoneNumber"
    )
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    personal_email_address: Optional[str] = Field(
        default=None, alias="PersonalEmailAddress"
    )
    business_email_address: Optional[str] = Field(
        default=None, alias="BusinessEmailAddress"
    )
    address: Optional[AddressModel] = Field(default=None, alias="Address")
    shipping_address: Optional[AddressModel] = Field(
        default=None, alias="ShippingAddress"
    )
    mailing_address: Optional[AddressModel] = Field(
        default=None, alias="MailingAddress"
    )
    billing_address: Optional[AddressModel] = Field(
        default=None, alias="BillingAddress"
    )
    attributes: Optional[Dict[str, str]] = Field(default=None, alias="Attributes")
    found_by_items: Optional[List[FoundByKeyValueModel]] = Field(
        default=None, alias="FoundByItems"
    )
    party_type_string: Optional[str] = Field(default=None, alias="PartyTypeString")
    gender_string: Optional[str] = Field(default=None, alias="GenderString")


class GetMatchesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    match_generation_date: datetime = Field(alias="MatchGenerationDate")
    potential_matches: int = Field(alias="PotentialMatches")
    matches: List[MatchItemModel] = Field(alias="Matches")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProfileObjectTypeResponseModel(BaseModel):
    object_type_name: str = Field(alias="ObjectTypeName")
    description: str = Field(alias="Description")
    template_id: str = Field(alias="TemplateId")
    expiration_days: int = Field(alias="ExpirationDays")
    encryption_key: str = Field(alias="EncryptionKey")
    allow_profile_creation: bool = Field(alias="AllowProfileCreation")
    source_last_updated_timestamp_format: str = Field(
        alias="SourceLastUpdatedTimestampFormat"
    )
    fields: Dict[str, ObjectTypeFieldModel] = Field(alias="Fields")
    keys: Dict[str, List[ObjectTypeKeyModel]] = Field(alias="Keys")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetProfileObjectTypeTemplateResponseModel(BaseModel):
    template_id: str = Field(alias="TemplateId")
    source_name: str = Field(alias="SourceName")
    source_object: str = Field(alias="SourceObject")
    allow_profile_creation: bool = Field(alias="AllowProfileCreation")
    source_last_updated_timestamp_format: str = Field(
        alias="SourceLastUpdatedTimestampFormat"
    )
    fields: Dict[str, ObjectTypeFieldModel] = Field(alias="Fields")
    keys: Dict[str, List[ObjectTypeKeyModel]] = Field(alias="Keys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutProfileObjectTypeRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    object_type_name: str = Field(alias="ObjectTypeName")
    description: str = Field(alias="Description")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")
    expiration_days: Optional[int] = Field(default=None, alias="ExpirationDays")
    encryption_key: Optional[str] = Field(default=None, alias="EncryptionKey")
    allow_profile_creation: Optional[bool] = Field(
        default=None, alias="AllowProfileCreation"
    )
    source_last_updated_timestamp_format: Optional[str] = Field(
        default=None, alias="SourceLastUpdatedTimestampFormat"
    )
    fields: Optional[Mapping[str, ObjectTypeFieldModel]] = Field(
        default=None, alias="Fields"
    )
    keys: Optional[Mapping[str, Sequence[ObjectTypeKeyModel]]] = Field(
        default=None, alias="Keys"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class PutProfileObjectTypeResponseModel(BaseModel):
    object_type_name: str = Field(alias="ObjectTypeName")
    description: str = Field(alias="Description")
    template_id: str = Field(alias="TemplateId")
    expiration_days: int = Field(alias="ExpirationDays")
    encryption_key: str = Field(alias="EncryptionKey")
    allow_profile_creation: bool = Field(alias="AllowProfileCreation")
    source_last_updated_timestamp_format: str = Field(
        alias="SourceLastUpdatedTimestampFormat"
    )
    fields: Dict[str, ObjectTypeFieldModel] = Field(alias="Fields")
    keys: Dict[str, List[ObjectTypeKeyModel]] = Field(alias="Keys")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAccountIntegrationsResponseModel(BaseModel):
    items: List[ListIntegrationItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIntegrationsResponseModel(BaseModel):
    items: List[ListIntegrationItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDomainsResponseModel(BaseModel):
    items: List[ListDomainItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProfileObjectTypesResponseModel(BaseModel):
    items: List[ListProfileObjectTypeItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProfileObjectTypeTemplatesResponseModel(BaseModel):
    items: List[ListProfileObjectTypeTemplateItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProfileObjectsResponseModel(BaseModel):
    items: List[ListProfileObjectsItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProfileObjectsRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    object_type_name: str = Field(alias="ObjectTypeName")
    profile_id: str = Field(alias="ProfileId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    object_filter: Optional[ObjectFilterModel] = Field(
        default=None, alias="ObjectFilter"
    )


class ListWorkflowsResponseModel(BaseModel):
    items: List[ListWorkflowsItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TriggerPropertiesModel(BaseModel):
    scheduled: Optional[ScheduledTriggerPropertiesModel] = Field(
        default=None, alias="Scheduled"
    )


class SourceConnectorPropertiesModel(BaseModel):
    marketo: Optional[MarketoSourcePropertiesModel] = Field(
        default=None, alias="Marketo"
    )
    s3: Optional[S3SourcePropertiesModel] = Field(default=None, alias="S3")
    salesforce: Optional[SalesforceSourcePropertiesModel] = Field(
        default=None, alias="Salesforce"
    )
    service_now: Optional[ServiceNowSourcePropertiesModel] = Field(
        default=None, alias="ServiceNow"
    )
    zendesk: Optional[ZendeskSourcePropertiesModel] = Field(
        default=None, alias="Zendesk"
    )


class UpdateProfileRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    profile_id: str = Field(alias="ProfileId")
    additional_information: Optional[str] = Field(
        default=None, alias="AdditionalInformation"
    )
    account_number: Optional[str] = Field(default=None, alias="AccountNumber")
    party_type: Optional[Literal["BUSINESS", "INDIVIDUAL", "OTHER"]] = Field(
        default=None, alias="PartyType"
    )
    business_name: Optional[str] = Field(default=None, alias="BusinessName")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    middle_name: Optional[str] = Field(default=None, alias="MiddleName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    birth_date: Optional[str] = Field(default=None, alias="BirthDate")
    gender: Optional[Literal["FEMALE", "MALE", "UNSPECIFIED"]] = Field(
        default=None, alias="Gender"
    )
    phone_number: Optional[str] = Field(default=None, alias="PhoneNumber")
    mobile_phone_number: Optional[str] = Field(default=None, alias="MobilePhoneNumber")
    home_phone_number: Optional[str] = Field(default=None, alias="HomePhoneNumber")
    business_phone_number: Optional[str] = Field(
        default=None, alias="BusinessPhoneNumber"
    )
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    personal_email_address: Optional[str] = Field(
        default=None, alias="PersonalEmailAddress"
    )
    business_email_address: Optional[str] = Field(
        default=None, alias="BusinessEmailAddress"
    )
    address: Optional[UpdateAddressModel] = Field(default=None, alias="Address")
    shipping_address: Optional[UpdateAddressModel] = Field(
        default=None, alias="ShippingAddress"
    )
    mailing_address: Optional[UpdateAddressModel] = Field(
        default=None, alias="MailingAddress"
    )
    billing_address: Optional[UpdateAddressModel] = Field(
        default=None, alias="BillingAddress"
    )
    attributes: Optional[Mapping[str, str]] = Field(default=None, alias="Attributes")
    party_type_string: Optional[str] = Field(default=None, alias="PartyTypeString")
    gender_string: Optional[str] = Field(default=None, alias="GenderString")


class GetWorkflowResponseModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    workflow_type: Literal["APPFLOW_INTEGRATION"] = Field(alias="WorkflowType")
    status: Literal[
        "CANCELLED",
        "COMPLETE",
        "FAILED",
        "IN_PROGRESS",
        "NOT_STARTED",
        "RETRY",
        "SPLIT",
    ] = Field(alias="Status")
    error_description: str = Field(alias="ErrorDescription")
    start_date: datetime = Field(alias="StartDate")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    attributes: WorkflowAttributesModel = Field(alias="Attributes")
    metrics: WorkflowMetricsModel = Field(alias="Metrics")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWorkflowStepsResponseModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    workflow_type: Literal["APPFLOW_INTEGRATION"] = Field(alias="WorkflowType")
    items: List[WorkflowStepItemModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MatchingRequestModel(BaseModel):
    enabled: bool = Field(alias="Enabled")
    job_schedule: Optional[JobScheduleModel] = Field(default=None, alias="JobSchedule")
    auto_merging: Optional[AutoMergingModel] = Field(default=None, alias="AutoMerging")
    exporting_config: Optional[ExportingConfigModel] = Field(
        default=None, alias="ExportingConfig"
    )


class MatchingResponseModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    job_schedule: Optional[JobScheduleModel] = Field(default=None, alias="JobSchedule")
    auto_merging: Optional[AutoMergingModel] = Field(default=None, alias="AutoMerging")
    exporting_config: Optional[ExportingConfigModel] = Field(
        default=None, alias="ExportingConfig"
    )


class GetIdentityResolutionJobResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    job_id: str = Field(alias="JobId")
    status: Literal[
        "COMPLETED",
        "FAILED",
        "FIND_MATCHING",
        "MERGING",
        "PARTIAL_SUCCESS",
        "PENDING",
        "PREPROCESSING",
    ] = Field(alias="Status")
    message: str = Field(alias="Message")
    job_start_time: datetime = Field(alias="JobStartTime")
    job_end_time: datetime = Field(alias="JobEndTime")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    job_expiration_time: datetime = Field(alias="JobExpirationTime")
    auto_merging: AutoMergingModel = Field(alias="AutoMerging")
    exporting_location: ExportingLocationModel = Field(alias="ExportingLocation")
    job_stats: JobStatsModel = Field(alias="JobStats")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IdentityResolutionJobModel(BaseModel):
    domain_name: Optional[str] = Field(default=None, alias="DomainName")
    job_id: Optional[str] = Field(default=None, alias="JobId")
    status: Optional[
        Literal[
            "COMPLETED",
            "FAILED",
            "FIND_MATCHING",
            "MERGING",
            "PARTIAL_SUCCESS",
            "PENDING",
            "PREPROCESSING",
        ]
    ] = Field(default=None, alias="Status")
    job_start_time: Optional[datetime] = Field(default=None, alias="JobStartTime")
    job_end_time: Optional[datetime] = Field(default=None, alias="JobEndTime")
    job_stats: Optional[JobStatsModel] = Field(default=None, alias="JobStats")
    exporting_location: Optional[ExportingLocationModel] = Field(
        default=None, alias="ExportingLocation"
    )
    message: Optional[str] = Field(default=None, alias="Message")


class SearchProfilesResponseModel(BaseModel):
    items: List[ProfileModel] = Field(alias="Items")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TriggerConfigModel(BaseModel):
    trigger_type: Literal["Event", "OnDemand", "Scheduled"] = Field(alias="TriggerType")
    trigger_properties: Optional[TriggerPropertiesModel] = Field(
        default=None, alias="TriggerProperties"
    )


class SourceFlowConfigModel(BaseModel):
    connector_type: Literal[
        "Marketo", "S3", "Salesforce", "Servicenow", "Zendesk"
    ] = Field(alias="ConnectorType")
    source_connector_properties: SourceConnectorPropertiesModel = Field(
        alias="SourceConnectorProperties"
    )
    connector_profile_name: Optional[str] = Field(
        default=None, alias="ConnectorProfileName"
    )
    incremental_pull_config: Optional[IncrementalPullConfigModel] = Field(
        default=None, alias="IncrementalPullConfig"
    )


class CreateDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    default_expiration_days: int = Field(alias="DefaultExpirationDays")
    default_encryption_key: Optional[str] = Field(
        default=None, alias="DefaultEncryptionKey"
    )
    dead_letter_queue_url: Optional[str] = Field(
        default=None, alias="DeadLetterQueueUrl"
    )
    matching: Optional[MatchingRequestModel] = Field(default=None, alias="Matching")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateDomainRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    default_expiration_days: Optional[int] = Field(
        default=None, alias="DefaultExpirationDays"
    )
    default_encryption_key: Optional[str] = Field(
        default=None, alias="DefaultEncryptionKey"
    )
    dead_letter_queue_url: Optional[str] = Field(
        default=None, alias="DeadLetterQueueUrl"
    )
    matching: Optional[MatchingRequestModel] = Field(default=None, alias="Matching")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateDomainResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    default_expiration_days: int = Field(alias="DefaultExpirationDays")
    default_encryption_key: str = Field(alias="DefaultEncryptionKey")
    dead_letter_queue_url: str = Field(alias="DeadLetterQueueUrl")
    matching: MatchingResponseModel = Field(alias="Matching")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDomainResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    default_expiration_days: int = Field(alias="DefaultExpirationDays")
    default_encryption_key: str = Field(alias="DefaultEncryptionKey")
    dead_letter_queue_url: str = Field(alias="DeadLetterQueueUrl")
    stats: DomainStatsModel = Field(alias="Stats")
    matching: MatchingResponseModel = Field(alias="Matching")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDomainResponseModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    default_expiration_days: int = Field(alias="DefaultExpirationDays")
    default_encryption_key: str = Field(alias="DefaultEncryptionKey")
    dead_letter_queue_url: str = Field(alias="DeadLetterQueueUrl")
    matching: MatchingResponseModel = Field(alias="Matching")
    created_at: datetime = Field(alias="CreatedAt")
    last_updated_at: datetime = Field(alias="LastUpdatedAt")
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIdentityResolutionJobsResponseModel(BaseModel):
    identity_resolution_jobs_list: List[IdentityResolutionJobModel] = Field(
        alias="IdentityResolutionJobsList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FlowDefinitionModel(BaseModel):
    flow_name: str = Field(alias="FlowName")
    kms_arn: str = Field(alias="KmsArn")
    source_flow_config: SourceFlowConfigModel = Field(alias="SourceFlowConfig")
    tasks: Sequence[TaskModel] = Field(alias="Tasks")
    trigger_config: TriggerConfigModel = Field(alias="TriggerConfig")
    description: Optional[str] = Field(default=None, alias="Description")


class AppflowIntegrationModel(BaseModel):
    flow_definition: FlowDefinitionModel = Field(alias="FlowDefinition")
    batches: Optional[Sequence[BatchModel]] = Field(default=None, alias="Batches")


class PutIntegrationRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    uri: Optional[str] = Field(default=None, alias="Uri")
    object_type_name: Optional[str] = Field(default=None, alias="ObjectTypeName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    flow_definition: Optional[FlowDefinitionModel] = Field(
        default=None, alias="FlowDefinition"
    )
    object_type_names: Optional[Mapping[str, str]] = Field(
        default=None, alias="ObjectTypeNames"
    )


class IntegrationConfigModel(BaseModel):
    appflow_integration: Optional[AppflowIntegrationModel] = Field(
        default=None, alias="AppflowIntegration"
    )


class CreateIntegrationWorkflowRequestModel(BaseModel):
    domain_name: str = Field(alias="DomainName")
    workflow_type: Literal["APPFLOW_INTEGRATION"] = Field(alias="WorkflowType")
    integration_config: IntegrationConfigModel = Field(alias="IntegrationConfig")
    object_type_name: str = Field(alias="ObjectTypeName")
    role_arn: str = Field(alias="RoleArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
