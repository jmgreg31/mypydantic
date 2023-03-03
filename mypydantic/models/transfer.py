# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class As2ConnectorConfigModel(BaseModel):
    local_profile_id: Optional[str] = Field(default=None, alias="LocalProfileId")
    partner_profile_id: Optional[str] = Field(default=None, alias="PartnerProfileId")
    message_subject: Optional[str] = Field(default=None, alias="MessageSubject")
    compression: Optional[Literal["DISABLED", "ZLIB"]] = Field(
        default=None, alias="Compression"
    )
    encryption_algorithm: Optional[
        Literal["AES128_CBC", "AES192_CBC", "AES256_CBC", "NONE"]
    ] = Field(default=None, alias="EncryptionAlgorithm")
    signing_algorithm: Optional[
        Literal["NONE", "SHA1", "SHA256", "SHA384", "SHA512"]
    ] = Field(default=None, alias="SigningAlgorithm")
    mdn_signing_algorithm: Optional[
        Literal["DEFAULT", "NONE", "SHA1", "SHA256", "SHA384", "SHA512"]
    ] = Field(default=None, alias="MdnSigningAlgorithm")
    mdn_response: Optional[Literal["NONE", "SYNC"]] = Field(
        default=None, alias="MdnResponse"
    )


class HomeDirectoryMapEntryModel(BaseModel):
    entry: str = Field(alias="Entry")
    target: str = Field(alias="Target")


class PosixProfileModel(BaseModel):
    uid: int = Field(alias="Uid")
    gid: int = Field(alias="Gid")
    secondary_gids: Optional[Sequence[int]] = Field(default=None, alias="SecondaryGids")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class EndpointDetailsModel(BaseModel):
    address_allocation_ids: Optional[Sequence[str]] = Field(
        default=None, alias="AddressAllocationIds"
    )
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="SubnetIds")
    vpc_endpoint_id: Optional[str] = Field(default=None, alias="VpcEndpointId")
    vpc_id: Optional[str] = Field(default=None, alias="VpcId")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="SecurityGroupIds"
    )


class IdentityProviderDetailsModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")
    invocation_role: Optional[str] = Field(default=None, alias="InvocationRole")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    function: Optional[str] = Field(default=None, alias="Function")


class ProtocolDetailsModel(BaseModel):
    passive_ip: Optional[str] = Field(default=None, alias="PassiveIp")
    tls_session_resumption_mode: Optional[
        Literal["DISABLED", "ENABLED", "ENFORCED"]
    ] = Field(default=None, alias="TlsSessionResumptionMode")
    set_stat_option: Optional[Literal["DEFAULT", "ENABLE_NO_OP"]] = Field(
        default=None, alias="SetStatOption"
    )
    as2_transports: Optional[Sequence[Literal["HTTP"]]] = Field(
        default=None, alias="As2Transports"
    )


class CustomStepDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    target: Optional[str] = Field(default=None, alias="Target")
    timeout_seconds: Optional[int] = Field(default=None, alias="TimeoutSeconds")
    source_file_location: Optional[str] = Field(
        default=None, alias="SourceFileLocation"
    )


class DeleteAccessRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    external_id: str = Field(alias="ExternalId")


class DeleteAgreementRequestModel(BaseModel):
    agreement_id: str = Field(alias="AgreementId")
    server_id: str = Field(alias="ServerId")


class DeleteCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")


class DeleteConnectorRequestModel(BaseModel):
    connector_id: str = Field(alias="ConnectorId")


class DeleteHostKeyRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    host_key_id: str = Field(alias="HostKeyId")


class DeleteProfileRequestModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")


class DeleteServerRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")


class DeleteSshPublicKeyRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    ssh_public_key_id: str = Field(alias="SshPublicKeyId")
    user_name: str = Field(alias="UserName")


class DeleteStepDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    source_file_location: Optional[str] = Field(
        default=None, alias="SourceFileLocation"
    )


class DeleteUserRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    user_name: str = Field(alias="UserName")


class DeleteWorkflowRequestModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")


class DescribeAccessRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    external_id: str = Field(alias="ExternalId")


class DescribeAgreementRequestModel(BaseModel):
    agreement_id: str = Field(alias="AgreementId")
    server_id: str = Field(alias="ServerId")


class DescribeCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")


class DescribeConnectorRequestModel(BaseModel):
    connector_id: str = Field(alias="ConnectorId")


class DescribeExecutionRequestModel(BaseModel):
    execution_id: str = Field(alias="ExecutionId")
    workflow_id: str = Field(alias="WorkflowId")


class DescribeHostKeyRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    host_key_id: str = Field(alias="HostKeyId")


class DescribeProfileRequestModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")


class DescribeSecurityPolicyRequestModel(BaseModel):
    security_policy_name: str = Field(alias="SecurityPolicyName")


class DescribedSecurityPolicyModel(BaseModel):
    security_policy_name: str = Field(alias="SecurityPolicyName")
    fips: Optional[bool] = Field(default=None, alias="Fips")
    ssh_ciphers: Optional[List[str]] = Field(default=None, alias="SshCiphers")
    ssh_kexs: Optional[List[str]] = Field(default=None, alias="SshKexs")
    ssh_macs: Optional[List[str]] = Field(default=None, alias="SshMacs")
    tls_ciphers: Optional[List[str]] = Field(default=None, alias="TlsCiphers")


class DescribeServerRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeUserRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    user_name: str = Field(alias="UserName")


class DescribeWorkflowRequestModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")


class LoggingConfigurationModel(BaseModel):
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")
    log_group_name: Optional[str] = Field(default=None, alias="LogGroupName")


class SshPublicKeyModel(BaseModel):
    date_imported: datetime = Field(alias="DateImported")
    ssh_public_key_body: str = Field(alias="SshPublicKeyBody")
    ssh_public_key_id: str = Field(alias="SshPublicKeyId")


class EfsFileLocationModel(BaseModel):
    file_system_id: Optional[str] = Field(default=None, alias="FileSystemId")
    path: Optional[str] = Field(default=None, alias="Path")


class ExecutionErrorModel(BaseModel):
    type: Literal[
        "ALREADY_EXISTS",
        "BAD_REQUEST",
        "CUSTOM_STEP_FAILED",
        "INTERNAL_SERVER_ERROR",
        "NOT_FOUND",
        "PERMISSION_DENIED",
        "THROTTLED",
        "TIMEOUT",
    ] = Field(alias="Type")
    message: str = Field(alias="Message")


class S3FileLocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    key: Optional[str] = Field(default=None, alias="Key")
    version_id: Optional[str] = Field(default=None, alias="VersionId")
    etag: Optional[str] = Field(default=None, alias="Etag")


class ImportSshPublicKeyRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    ssh_public_key_body: str = Field(alias="SshPublicKeyBody")
    user_name: str = Field(alias="UserName")


class S3InputFileLocationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    key: Optional[str] = Field(default=None, alias="Key")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAccessesRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedAccessModel(BaseModel):
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    role: Optional[str] = Field(default=None, alias="Role")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")


class ListAgreementsRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedAgreementModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    agreement_id: Optional[str] = Field(default=None, alias="AgreementId")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    server_id: Optional[str] = Field(default=None, alias="ServerId")
    local_profile_id: Optional[str] = Field(default=None, alias="LocalProfileId")
    partner_profile_id: Optional[str] = Field(default=None, alias="PartnerProfileId")


class ListCertificatesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedCertificateModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    certificate_id: Optional[str] = Field(default=None, alias="CertificateId")
    usage: Optional[Literal["ENCRYPTION", "SIGNING"]] = Field(
        default=None, alias="Usage"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE", "PENDING_ROTATION"]] = Field(
        default=None, alias="Status"
    )
    active_date: Optional[datetime] = Field(default=None, alias="ActiveDate")
    inactive_date: Optional[datetime] = Field(default=None, alias="InactiveDate")
    type: Optional[Literal["CERTIFICATE", "CERTIFICATE_WITH_PRIVATE_KEY"]] = Field(
        default=None, alias="Type"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class ListConnectorsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedConnectorModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    connector_id: Optional[str] = Field(default=None, alias="ConnectorId")
    url: Optional[str] = Field(default=None, alias="Url")


class ListExecutionsRequestModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListHostKeysRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedHostKeyModel(BaseModel):
    arn: str = Field(alias="Arn")
    host_key_id: Optional[str] = Field(default=None, alias="HostKeyId")
    fingerprint: Optional[str] = Field(default=None, alias="Fingerprint")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    date_imported: Optional[datetime] = Field(default=None, alias="DateImported")


class ListProfilesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    profile_type: Optional[Literal["LOCAL", "PARTNER"]] = Field(
        default=None, alias="ProfileType"
    )


class ListedProfileModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    profile_id: Optional[str] = Field(default=None, alias="ProfileId")
    as2_id: Optional[str] = Field(default=None, alias="As2Id")
    profile_type: Optional[Literal["LOCAL", "PARTNER"]] = Field(
        default=None, alias="ProfileType"
    )


class ListSecurityPoliciesRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListServersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedServerModel(BaseModel):
    arn: str = Field(alias="Arn")
    domain: Optional[Literal["EFS", "S3"]] = Field(default=None, alias="Domain")
    identity_provider_type: Optional[
        Literal["API_GATEWAY", "AWS_DIRECTORY_SERVICE", "AWS_LAMBDA", "SERVICE_MANAGED"]
    ] = Field(default=None, alias="IdentityProviderType")
    endpoint_type: Optional[Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]] = Field(
        default=None, alias="EndpointType"
    )
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")
    server_id: Optional[str] = Field(default=None, alias="ServerId")
    state: Optional[
        Literal[
            "OFFLINE", "ONLINE", "STARTING", "START_FAILED", "STOPPING", "STOP_FAILED"
        ]
    ] = Field(default=None, alias="State")
    user_count: Optional[int] = Field(default=None, alias="UserCount")


class ListTagsForResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListUsersRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedUserModel(BaseModel):
    arn: str = Field(alias="Arn")
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    role: Optional[str] = Field(default=None, alias="Role")
    ssh_public_key_count: Optional[int] = Field(default=None, alias="SshPublicKeyCount")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class ListWorkflowsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListedWorkflowModel(BaseModel):
    workflow_id: Optional[str] = Field(default=None, alias="WorkflowId")
    description: Optional[str] = Field(default=None, alias="Description")
    arn: Optional[str] = Field(default=None, alias="Arn")


class S3TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class SendWorkflowStepStateRequestModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    execution_id: str = Field(alias="ExecutionId")
    token: str = Field(alias="Token")
    status: Literal["FAILURE", "SUCCESS"] = Field(alias="Status")


class UserDetailsModel(BaseModel):
    user_name: str = Field(alias="UserName")
    server_id: str = Field(alias="ServerId")
    session_id: Optional[str] = Field(default=None, alias="SessionId")


class StartFileTransferRequestModel(BaseModel):
    connector_id: str = Field(alias="ConnectorId")
    send_file_paths: Sequence[str] = Field(alias="SendFilePaths")


class StartServerRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")


class StopServerRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")


class TestIdentityProviderRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    user_name: str = Field(alias="UserName")
    server_protocol: Optional[Literal["AS2", "FTP", "FTPS", "SFTP"]] = Field(
        default=None, alias="ServerProtocol"
    )
    source_ip: Optional[str] = Field(default=None, alias="SourceIp")
    user_password: Optional[str] = Field(default=None, alias="UserPassword")


class UntagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAgreementRequestModel(BaseModel):
    agreement_id: str = Field(alias="AgreementId")
    server_id: str = Field(alias="ServerId")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    local_profile_id: Optional[str] = Field(default=None, alias="LocalProfileId")
    partner_profile_id: Optional[str] = Field(default=None, alias="PartnerProfileId")
    base_directory: Optional[str] = Field(default=None, alias="BaseDirectory")
    access_role: Optional[str] = Field(default=None, alias="AccessRole")


class UpdateCertificateRequestModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")
    active_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ActiveDate"
    )
    inactive_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="InactiveDate"
    )
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateHostKeyRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    host_key_id: str = Field(alias="HostKeyId")
    description: str = Field(alias="Description")


class UpdateProfileRequestModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    certificate_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CertificateIds"
    )


class WorkflowDetailModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    execution_role: str = Field(alias="ExecutionRole")


class UpdateConnectorRequestModel(BaseModel):
    connector_id: str = Field(alias="ConnectorId")
    url: Optional[str] = Field(default=None, alias="Url")
    as2_config: Optional[As2ConnectorConfigModel] = Field(
        default=None, alias="As2Config"
    )
    access_role: Optional[str] = Field(default=None, alias="AccessRole")
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")


class CreateAccessRequestModel(BaseModel):
    role: str = Field(alias="Role")
    server_id: str = Field(alias="ServerId")
    external_id: str = Field(alias="ExternalId")
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    home_directory_mappings: Optional[Sequence[HomeDirectoryMapEntryModel]] = Field(
        default=None, alias="HomeDirectoryMappings"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    posix_profile: Optional[PosixProfileModel] = Field(
        default=None, alias="PosixProfile"
    )


class DescribedAccessModel(BaseModel):
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_mappings: Optional[List[HomeDirectoryMapEntryModel]] = Field(
        default=None, alias="HomeDirectoryMappings"
    )
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    posix_profile: Optional[PosixProfileModel] = Field(
        default=None, alias="PosixProfile"
    )
    role: Optional[str] = Field(default=None, alias="Role")
    external_id: Optional[str] = Field(default=None, alias="ExternalId")


class UpdateAccessRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    external_id: str = Field(alias="ExternalId")
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    home_directory_mappings: Optional[Sequence[HomeDirectoryMapEntryModel]] = Field(
        default=None, alias="HomeDirectoryMappings"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    posix_profile: Optional[PosixProfileModel] = Field(
        default=None, alias="PosixProfile"
    )
    role: Optional[str] = Field(default=None, alias="Role")


class UpdateUserRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    user_name: str = Field(alias="UserName")
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    home_directory_mappings: Optional[Sequence[HomeDirectoryMapEntryModel]] = Field(
        default=None, alias="HomeDirectoryMappings"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    posix_profile: Optional[PosixProfileModel] = Field(
        default=None, alias="PosixProfile"
    )
    role: Optional[str] = Field(default=None, alias="Role")


class CreateAccessResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    external_id: str = Field(alias="ExternalId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAgreementResponseModel(BaseModel):
    agreement_id: str = Field(alias="AgreementId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateConnectorResponseModel(BaseModel):
    connector_id: str = Field(alias="ConnectorId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProfileResponseModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateServerResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateUserResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    user_name: str = Field(alias="UserName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowResponseModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportCertificateResponseModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportHostKeyResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    host_key_id: str = Field(alias="HostKeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportSshPublicKeyResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    ssh_public_key_id: str = Field(alias="SshPublicKeyId")
    user_name: str = Field(alias="UserName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSecurityPoliciesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    security_policy_names: List[str] = Field(alias="SecurityPolicyNames")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFileTransferResponseModel(BaseModel):
    transfer_id: str = Field(alias="TransferId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TestIdentityProviderResponseModel(BaseModel):
    response: str = Field(alias="Response")
    status_code: int = Field(alias="StatusCode")
    message: str = Field(alias="Message")
    url: str = Field(alias="Url")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccessResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    external_id: str = Field(alias="ExternalId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAgreementResponseModel(BaseModel):
    agreement_id: str = Field(alias="AgreementId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateCertificateResponseModel(BaseModel):
    certificate_id: str = Field(alias="CertificateId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateConnectorResponseModel(BaseModel):
    connector_id: str = Field(alias="ConnectorId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateHostKeyResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    host_key_id: str = Field(alias="HostKeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateProfileResponseModel(BaseModel):
    profile_id: str = Field(alias="ProfileId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateServerResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    user_name: str = Field(alias="UserName")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAgreementRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    local_profile_id: str = Field(alias="LocalProfileId")
    partner_profile_id: str = Field(alias="PartnerProfileId")
    base_directory: str = Field(alias="BaseDirectory")
    access_role: str = Field(alias="AccessRole")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateConnectorRequestModel(BaseModel):
    url: str = Field(alias="Url")
    as2_config: As2ConnectorConfigModel = Field(alias="As2Config")
    access_role: str = Field(alias="AccessRole")
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateProfileRequestModel(BaseModel):
    as2_id: str = Field(alias="As2Id")
    profile_type: Literal["LOCAL", "PARTNER"] = Field(alias="ProfileType")
    certificate_ids: Optional[Sequence[str]] = Field(
        default=None, alias="CertificateIds"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateUserRequestModel(BaseModel):
    role: str = Field(alias="Role")
    server_id: str = Field(alias="ServerId")
    user_name: str = Field(alias="UserName")
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    home_directory_mappings: Optional[Sequence[HomeDirectoryMapEntryModel]] = Field(
        default=None, alias="HomeDirectoryMappings"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    posix_profile: Optional[PosixProfileModel] = Field(
        default=None, alias="PosixProfile"
    )
    ssh_public_key_body: Optional[str] = Field(default=None, alias="SshPublicKeyBody")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribedAgreementModel(BaseModel):
    arn: str = Field(alias="Arn")
    agreement_id: Optional[str] = Field(default=None, alias="AgreementId")
    description: Optional[str] = Field(default=None, alias="Description")
    status: Optional[Literal["ACTIVE", "INACTIVE"]] = Field(
        default=None, alias="Status"
    )
    server_id: Optional[str] = Field(default=None, alias="ServerId")
    local_profile_id: Optional[str] = Field(default=None, alias="LocalProfileId")
    partner_profile_id: Optional[str] = Field(default=None, alias="PartnerProfileId")
    base_directory: Optional[str] = Field(default=None, alias="BaseDirectory")
    access_role: Optional[str] = Field(default=None, alias="AccessRole")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class DescribedCertificateModel(BaseModel):
    arn: str = Field(alias="Arn")
    certificate_id: Optional[str] = Field(default=None, alias="CertificateId")
    usage: Optional[Literal["ENCRYPTION", "SIGNING"]] = Field(
        default=None, alias="Usage"
    )
    status: Optional[Literal["ACTIVE", "INACTIVE", "PENDING_ROTATION"]] = Field(
        default=None, alias="Status"
    )
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    certificate_chain: Optional[str] = Field(default=None, alias="CertificateChain")
    active_date: Optional[datetime] = Field(default=None, alias="ActiveDate")
    inactive_date: Optional[datetime] = Field(default=None, alias="InactiveDate")
    serial: Optional[str] = Field(default=None, alias="Serial")
    not_before_date: Optional[datetime] = Field(default=None, alias="NotBeforeDate")
    not_after_date: Optional[datetime] = Field(default=None, alias="NotAfterDate")
    type: Optional[Literal["CERTIFICATE", "CERTIFICATE_WITH_PRIVATE_KEY"]] = Field(
        default=None, alias="Type"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class DescribedConnectorModel(BaseModel):
    arn: str = Field(alias="Arn")
    connector_id: Optional[str] = Field(default=None, alias="ConnectorId")
    url: Optional[str] = Field(default=None, alias="Url")
    as2_config: Optional[As2ConnectorConfigModel] = Field(
        default=None, alias="As2Config"
    )
    access_role: Optional[str] = Field(default=None, alias="AccessRole")
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class DescribedHostKeyModel(BaseModel):
    arn: str = Field(alias="Arn")
    host_key_id: Optional[str] = Field(default=None, alias="HostKeyId")
    host_key_fingerprint: Optional[str] = Field(
        default=None, alias="HostKeyFingerprint"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[str] = Field(default=None, alias="Type")
    date_imported: Optional[datetime] = Field(default=None, alias="DateImported")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class DescribedProfileModel(BaseModel):
    arn: str = Field(alias="Arn")
    profile_id: Optional[str] = Field(default=None, alias="ProfileId")
    profile_type: Optional[Literal["LOCAL", "PARTNER"]] = Field(
        default=None, alias="ProfileType"
    )
    as2_id: Optional[str] = Field(default=None, alias="As2Id")
    certificate_ids: Optional[List[str]] = Field(default=None, alias="CertificateIds")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class ImportCertificateRequestModel(BaseModel):
    usage: Literal["ENCRYPTION", "SIGNING"] = Field(alias="Usage")
    certificate: str = Field(alias="Certificate")
    certificate_chain: Optional[str] = Field(default=None, alias="CertificateChain")
    private_key: Optional[str] = Field(default=None, alias="PrivateKey")
    active_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="ActiveDate"
    )
    inactive_date: Optional[Union[datetime, str]] = Field(
        default=None, alias="InactiveDate"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ImportHostKeyRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    host_key_body: str = Field(alias="HostKeyBody")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    next_token: str = Field(alias="NextToken")
    tags: List[TagModel] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class DescribeSecurityPolicyResponseModel(BaseModel):
    security_policy: DescribedSecurityPolicyModel = Field(alias="SecurityPolicy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServerRequestServerOfflineWaitModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeServerRequestServerOnlineWaitModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribedUserModel(BaseModel):
    arn: str = Field(alias="Arn")
    home_directory: Optional[str] = Field(default=None, alias="HomeDirectory")
    home_directory_mappings: Optional[List[HomeDirectoryMapEntryModel]] = Field(
        default=None, alias="HomeDirectoryMappings"
    )
    home_directory_type: Optional[Literal["LOGICAL", "PATH"]] = Field(
        default=None, alias="HomeDirectoryType"
    )
    policy: Optional[str] = Field(default=None, alias="Policy")
    posix_profile: Optional[PosixProfileModel] = Field(
        default=None, alias="PosixProfile"
    )
    role: Optional[str] = Field(default=None, alias="Role")
    ssh_public_keys: Optional[List[SshPublicKeyModel]] = Field(
        default=None, alias="SshPublicKeys"
    )
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    user_name: Optional[str] = Field(default=None, alias="UserName")


class ExecutionStepResultModel(BaseModel):
    step_type: Optional[Literal["COPY", "CUSTOM", "DECRYPT", "DELETE", "TAG"]] = Field(
        default=None, alias="StepType"
    )
    outputs: Optional[str] = Field(default=None, alias="Outputs")
    error: Optional[ExecutionErrorModel] = Field(default=None, alias="Error")


class FileLocationModel(BaseModel):
    s3_file_location: Optional[S3FileLocationModel] = Field(
        default=None, alias="S3FileLocation"
    )
    efs_file_location: Optional[EfsFileLocationModel] = Field(
        default=None, alias="EfsFileLocation"
    )


class InputFileLocationModel(BaseModel):
    s3_file_location: Optional[S3InputFileLocationModel] = Field(
        default=None, alias="S3FileLocation"
    )
    efs_file_location: Optional[EfsFileLocationModel] = Field(
        default=None, alias="EfsFileLocation"
    )


class ListAccessesRequestListAccessesPaginateModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAgreementsRequestListAgreementsPaginateModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCertificatesRequestListCertificatesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListConnectorsRequestListConnectorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListExecutionsRequestListExecutionsPaginateModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProfilesRequestListProfilesPaginateModel(BaseModel):
    profile_type: Optional[Literal["LOCAL", "PARTNER"]] = Field(
        default=None, alias="ProfileType"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSecurityPoliciesRequestListSecurityPoliciesPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListServersRequestListServersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    arn: str = Field(alias="Arn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUsersRequestListUsersPaginateModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListWorkflowsRequestListWorkflowsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAccessesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    server_id: str = Field(alias="ServerId")
    accesses: List[ListedAccessModel] = Field(alias="Accesses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAgreementsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    agreements: List[ListedAgreementModel] = Field(alias="Agreements")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCertificatesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    certificates: List[ListedCertificateModel] = Field(alias="Certificates")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConnectorsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    connectors: List[ListedConnectorModel] = Field(alias="Connectors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListHostKeysResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    server_id: str = Field(alias="ServerId")
    host_keys: List[ListedHostKeyModel] = Field(alias="HostKeys")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListProfilesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    profiles: List[ListedProfileModel] = Field(alias="Profiles")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListServersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    servers: List[ListedServerModel] = Field(alias="Servers")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    server_id: str = Field(alias="ServerId")
    users: List[ListedUserModel] = Field(alias="Users")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWorkflowsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    workflows: List[ListedWorkflowModel] = Field(alias="Workflows")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagStepDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    tags: Optional[Sequence[S3TagModel]] = Field(default=None, alias="Tags")
    source_file_location: Optional[str] = Field(
        default=None, alias="SourceFileLocation"
    )


class ServiceMetadataModel(BaseModel):
    user_details: UserDetailsModel = Field(alias="UserDetails")


class WorkflowDetailsModel(BaseModel):
    on_upload: Optional[Sequence[WorkflowDetailModel]] = Field(
        default=None, alias="OnUpload"
    )
    on_partial_upload: Optional[Sequence[WorkflowDetailModel]] = Field(
        default=None, alias="OnPartialUpload"
    )


class DescribeAccessResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    access: DescribedAccessModel = Field(alias="Access")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAgreementResponseModel(BaseModel):
    agreement: DescribedAgreementModel = Field(alias="Agreement")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCertificateResponseModel(BaseModel):
    certificate: DescribedCertificateModel = Field(alias="Certificate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConnectorResponseModel(BaseModel):
    connector: DescribedConnectorModel = Field(alias="Connector")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeHostKeyResponseModel(BaseModel):
    host_key: DescribedHostKeyModel = Field(alias="HostKey")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProfileResponseModel(BaseModel):
    profile: DescribedProfileModel = Field(alias="Profile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserResponseModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    user: DescribedUserModel = Field(alias="User")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecutionResultsModel(BaseModel):
    steps: Optional[List[ExecutionStepResultModel]] = Field(default=None, alias="Steps")
    on_exception_steps: Optional[List[ExecutionStepResultModel]] = Field(
        default=None, alias="OnExceptionSteps"
    )


class CopyStepDetailsModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    destination_file_location: Optional[InputFileLocationModel] = Field(
        default=None, alias="DestinationFileLocation"
    )
    overwrite_existing: Optional[Literal["FALSE", "TRUE"]] = Field(
        default=None, alias="OverwriteExisting"
    )
    source_file_location: Optional[str] = Field(
        default=None, alias="SourceFileLocation"
    )


class DecryptStepDetailsModel(BaseModel):
    type: Literal["PGP"] = Field(alias="Type")
    destination_file_location: InputFileLocationModel = Field(
        alias="DestinationFileLocation"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    source_file_location: Optional[str] = Field(
        default=None, alias="SourceFileLocation"
    )
    overwrite_existing: Optional[Literal["FALSE", "TRUE"]] = Field(
        default=None, alias="OverwriteExisting"
    )


class ListedExecutionModel(BaseModel):
    execution_id: Optional[str] = Field(default=None, alias="ExecutionId")
    initial_file_location: Optional[FileLocationModel] = Field(
        default=None, alias="InitialFileLocation"
    )
    service_metadata: Optional[ServiceMetadataModel] = Field(
        default=None, alias="ServiceMetadata"
    )
    status: Optional[
        Literal["COMPLETED", "EXCEPTION", "HANDLING_EXCEPTION", "IN_PROGRESS"]
    ] = Field(default=None, alias="Status")


class CreateServerRequestModel(BaseModel):
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    domain: Optional[Literal["EFS", "S3"]] = Field(default=None, alias="Domain")
    endpoint_details: Optional[EndpointDetailsModel] = Field(
        default=None, alias="EndpointDetails"
    )
    endpoint_type: Optional[Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]] = Field(
        default=None, alias="EndpointType"
    )
    host_key: Optional[str] = Field(default=None, alias="HostKey")
    identity_provider_details: Optional[IdentityProviderDetailsModel] = Field(
        default=None, alias="IdentityProviderDetails"
    )
    identity_provider_type: Optional[
        Literal["API_GATEWAY", "AWS_DIRECTORY_SERVICE", "AWS_LAMBDA", "SERVICE_MANAGED"]
    ] = Field(default=None, alias="IdentityProviderType")
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")
    post_authentication_login_banner: Optional[str] = Field(
        default=None, alias="PostAuthenticationLoginBanner"
    )
    pre_authentication_login_banner: Optional[str] = Field(
        default=None, alias="PreAuthenticationLoginBanner"
    )
    protocols: Optional[Sequence[Literal["AS2", "FTP", "FTPS", "SFTP"]]] = Field(
        default=None, alias="Protocols"
    )
    protocol_details: Optional[ProtocolDetailsModel] = Field(
        default=None, alias="ProtocolDetails"
    )
    security_policy_name: Optional[str] = Field(
        default=None, alias="SecurityPolicyName"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    workflow_details: Optional[WorkflowDetailsModel] = Field(
        default=None, alias="WorkflowDetails"
    )


class DescribedServerModel(BaseModel):
    arn: str = Field(alias="Arn")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    protocol_details: Optional[ProtocolDetailsModel] = Field(
        default=None, alias="ProtocolDetails"
    )
    domain: Optional[Literal["EFS", "S3"]] = Field(default=None, alias="Domain")
    endpoint_details: Optional[EndpointDetailsModel] = Field(
        default=None, alias="EndpointDetails"
    )
    endpoint_type: Optional[Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]] = Field(
        default=None, alias="EndpointType"
    )
    host_key_fingerprint: Optional[str] = Field(
        default=None, alias="HostKeyFingerprint"
    )
    identity_provider_details: Optional[IdentityProviderDetailsModel] = Field(
        default=None, alias="IdentityProviderDetails"
    )
    identity_provider_type: Optional[
        Literal["API_GATEWAY", "AWS_DIRECTORY_SERVICE", "AWS_LAMBDA", "SERVICE_MANAGED"]
    ] = Field(default=None, alias="IdentityProviderType")
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")
    post_authentication_login_banner: Optional[str] = Field(
        default=None, alias="PostAuthenticationLoginBanner"
    )
    pre_authentication_login_banner: Optional[str] = Field(
        default=None, alias="PreAuthenticationLoginBanner"
    )
    protocols: Optional[List[Literal["AS2", "FTP", "FTPS", "SFTP"]]] = Field(
        default=None, alias="Protocols"
    )
    security_policy_name: Optional[str] = Field(
        default=None, alias="SecurityPolicyName"
    )
    server_id: Optional[str] = Field(default=None, alias="ServerId")
    state: Optional[
        Literal[
            "OFFLINE", "ONLINE", "STARTING", "START_FAILED", "STOPPING", "STOP_FAILED"
        ]
    ] = Field(default=None, alias="State")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")
    user_count: Optional[int] = Field(default=None, alias="UserCount")
    workflow_details: Optional[WorkflowDetailsModel] = Field(
        default=None, alias="WorkflowDetails"
    )


class UpdateServerRequestModel(BaseModel):
    server_id: str = Field(alias="ServerId")
    certificate: Optional[str] = Field(default=None, alias="Certificate")
    protocol_details: Optional[ProtocolDetailsModel] = Field(
        default=None, alias="ProtocolDetails"
    )
    endpoint_details: Optional[EndpointDetailsModel] = Field(
        default=None, alias="EndpointDetails"
    )
    endpoint_type: Optional[Literal["PUBLIC", "VPC", "VPC_ENDPOINT"]] = Field(
        default=None, alias="EndpointType"
    )
    host_key: Optional[str] = Field(default=None, alias="HostKey")
    identity_provider_details: Optional[IdentityProviderDetailsModel] = Field(
        default=None, alias="IdentityProviderDetails"
    )
    logging_role: Optional[str] = Field(default=None, alias="LoggingRole")
    post_authentication_login_banner: Optional[str] = Field(
        default=None, alias="PostAuthenticationLoginBanner"
    )
    pre_authentication_login_banner: Optional[str] = Field(
        default=None, alias="PreAuthenticationLoginBanner"
    )
    protocols: Optional[Sequence[Literal["AS2", "FTP", "FTPS", "SFTP"]]] = Field(
        default=None, alias="Protocols"
    )
    security_policy_name: Optional[str] = Field(
        default=None, alias="SecurityPolicyName"
    )
    workflow_details: Optional[WorkflowDetailsModel] = Field(
        default=None, alias="WorkflowDetails"
    )


class DescribedExecutionModel(BaseModel):
    execution_id: Optional[str] = Field(default=None, alias="ExecutionId")
    initial_file_location: Optional[FileLocationModel] = Field(
        default=None, alias="InitialFileLocation"
    )
    service_metadata: Optional[ServiceMetadataModel] = Field(
        default=None, alias="ServiceMetadata"
    )
    execution_role: Optional[str] = Field(default=None, alias="ExecutionRole")
    logging_configuration: Optional[LoggingConfigurationModel] = Field(
        default=None, alias="LoggingConfiguration"
    )
    posix_profile: Optional[PosixProfileModel] = Field(
        default=None, alias="PosixProfile"
    )
    status: Optional[
        Literal["COMPLETED", "EXCEPTION", "HANDLING_EXCEPTION", "IN_PROGRESS"]
    ] = Field(default=None, alias="Status")
    results: Optional[ExecutionResultsModel] = Field(default=None, alias="Results")


class WorkflowStepModel(BaseModel):
    type: Optional[Literal["COPY", "CUSTOM", "DECRYPT", "DELETE", "TAG"]] = Field(
        default=None, alias="Type"
    )
    copy_step_details: Optional[CopyStepDetailsModel] = Field(
        default=None, alias="CopyStepDetails"
    )
    custom_step_details: Optional[CustomStepDetailsModel] = Field(
        default=None, alias="CustomStepDetails"
    )
    delete_step_details: Optional[DeleteStepDetailsModel] = Field(
        default=None, alias="DeleteStepDetails"
    )
    tag_step_details: Optional[TagStepDetailsModel] = Field(
        default=None, alias="TagStepDetails"
    )
    decrypt_step_details: Optional[DecryptStepDetailsModel] = Field(
        default=None, alias="DecryptStepDetails"
    )


class ListExecutionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    workflow_id: str = Field(alias="WorkflowId")
    executions: List[ListedExecutionModel] = Field(alias="Executions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeServerResponseModel(BaseModel):
    server: DescribedServerModel = Field(alias="Server")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeExecutionResponseModel(BaseModel):
    workflow_id: str = Field(alias="WorkflowId")
    execution: DescribedExecutionModel = Field(alias="Execution")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateWorkflowRequestModel(BaseModel):
    steps: Sequence[WorkflowStepModel] = Field(alias="Steps")
    description: Optional[str] = Field(default=None, alias="Description")
    on_exception_steps: Optional[Sequence[WorkflowStepModel]] = Field(
        default=None, alias="OnExceptionSteps"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribedWorkflowModel(BaseModel):
    arn: str = Field(alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    steps: Optional[List[WorkflowStepModel]] = Field(default=None, alias="Steps")
    on_exception_steps: Optional[List[WorkflowStepModel]] = Field(
        default=None, alias="OnExceptionSteps"
    )
    workflow_id: Optional[str] = Field(default=None, alias="WorkflowId")
    tags: Optional[List[TagModel]] = Field(default=None, alias="Tags")


class DescribeWorkflowResponseModel(BaseModel):
    workflow: DescribedWorkflowModel = Field(alias="Workflow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
