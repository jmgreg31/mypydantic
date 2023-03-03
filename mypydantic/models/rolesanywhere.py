# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Literal, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TagModel(BaseModel):
    key: str = Field(alias="key")
    value: str = Field(alias="value")


class CredentialSummaryModel(BaseModel):
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    failed: Optional[bool] = Field(default=None, alias="failed")
    issuer: Optional[str] = Field(default=None, alias="issuer")
    seen_at: Optional[datetime] = Field(default=None, alias="seenAt")
    serial_number: Optional[str] = Field(default=None, alias="serialNumber")
    x509_certificate_data: Optional[str] = Field(
        default=None, alias="x509CertificateData"
    )


class CrlDetailModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    crl_arn: Optional[str] = Field(default=None, alias="crlArn")
    crl_data: Optional[bytes] = Field(default=None, alias="crlData")
    crl_id: Optional[str] = Field(default=None, alias="crlId")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    name: Optional[str] = Field(default=None, alias="name")
    trust_anchor_arn: Optional[str] = Field(default=None, alias="trustAnchorArn")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class InstancePropertyModel(BaseModel):
    failed: Optional[bool] = Field(default=None, alias="failed")
    properties: Optional[Dict[str, str]] = Field(default=None, alias="properties")
    seen_at: Optional[datetime] = Field(default=None, alias="seenAt")


class ProfileDetailModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    created_by: Optional[str] = Field(default=None, alias="createdBy")
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    managed_policy_arns: Optional[List[str]] = Field(
        default=None, alias="managedPolicyArns"
    )
    name: Optional[str] = Field(default=None, alias="name")
    profile_arn: Optional[str] = Field(default=None, alias="profileArn")
    profile_id: Optional[str] = Field(default=None, alias="profileId")
    require_instance_properties: Optional[bool] = Field(
        default=None, alias="requireInstanceProperties"
    )
    role_arns: Optional[List[str]] = Field(default=None, alias="roleArns")
    session_policy: Optional[str] = Field(default=None, alias="sessionPolicy")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    page_size: Optional[int] = Field(default=None, alias="pageSize")


class SubjectSummaryModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    last_seen_at: Optional[datetime] = Field(default=None, alias="lastSeenAt")
    subject_arn: Optional[str] = Field(default=None, alias="subjectArn")
    subject_id: Optional[str] = Field(default=None, alias="subjectId")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    x509_subject: Optional[str] = Field(default=None, alias="x509Subject")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ScalarCrlRequestModel(BaseModel):
    crl_id: str = Field(alias="crlId")


class ScalarProfileRequestModel(BaseModel):
    profile_id: str = Field(alias="profileId")


class ScalarSubjectRequestModel(BaseModel):
    subject_id: str = Field(alias="subjectId")


class ScalarTrustAnchorRequestModel(BaseModel):
    trust_anchor_id: str = Field(alias="trustAnchorId")


class SourceDataModel(BaseModel):
    acm_pca_arn: Optional[str] = Field(default=None, alias="acmPcaArn")
    x509_certificate_data: Optional[str] = Field(
        default=None, alias="x509CertificateData"
    )


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateCrlRequestModel(BaseModel):
    crl_id: str = Field(alias="crlId")
    crl_data: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="crlData"
    )
    name: Optional[str] = Field(default=None, alias="name")


class UpdateProfileRequestModel(BaseModel):
    profile_id: str = Field(alias="profileId")
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")
    managed_policy_arns: Optional[Sequence[str]] = Field(
        default=None, alias="managedPolicyArns"
    )
    name: Optional[str] = Field(default=None, alias="name")
    role_arns: Optional[Sequence[str]] = Field(default=None, alias="roleArns")
    session_policy: Optional[str] = Field(default=None, alias="sessionPolicy")


class CreateProfileRequestModel(BaseModel):
    name: str = Field(alias="name")
    role_arns: Sequence[str] = Field(alias="roleArns")
    duration_seconds: Optional[int] = Field(default=None, alias="durationSeconds")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    managed_policy_arns: Optional[Sequence[str]] = Field(
        default=None, alias="managedPolicyArns"
    )
    require_instance_properties: Optional[bool] = Field(
        default=None, alias="requireInstanceProperties"
    )
    session_policy: Optional[str] = Field(default=None, alias="sessionPolicy")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class ImportCrlRequestModel(BaseModel):
    crl_data: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="crlData"
    )
    name: str = Field(alias="name")
    trust_anchor_arn: str = Field(alias="trustAnchorArn")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Sequence[TagModel] = Field(alias="tags")


class CrlDetailResponseModel(BaseModel):
    crl: CrlDetailModel = Field(alias="crl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCrlsResponseModel(BaseModel):
    crls: List[CrlDetailModel] = Field(alias="crls")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SubjectDetailModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    credentials: Optional[List[CredentialSummaryModel]] = Field(
        default=None, alias="credentials"
    )
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    instance_properties: Optional[List[InstancePropertyModel]] = Field(
        default=None, alias="instanceProperties"
    )
    last_seen_at: Optional[datetime] = Field(default=None, alias="lastSeenAt")
    subject_arn: Optional[str] = Field(default=None, alias="subjectArn")
    subject_id: Optional[str] = Field(default=None, alias="subjectId")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    x509_subject: Optional[str] = Field(default=None, alias="x509Subject")


class ListProfilesResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    profiles: List[ProfileDetailModel] = Field(alias="profiles")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProfileDetailResponseModel(BaseModel):
    profile: ProfileDetailModel = Field(alias="profile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRequestListCrlsPaginateModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRequestListProfilesPaginateModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRequestListSubjectsPaginateModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRequestListTrustAnchorsPaginateModel(BaseModel):
    page_size: Optional[int] = Field(default=None, alias="pageSize")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSubjectsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    subjects: List[SubjectSummaryModel] = Field(alias="subjects")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SourceModel(BaseModel):
    source_data: Optional[SourceDataModel] = Field(default=None, alias="sourceData")
    source_type: Optional[
        Literal["AWS_ACM_PCA", "CERTIFICATE_BUNDLE", "SELF_SIGNED_REPOSITORY"]
    ] = Field(default=None, alias="sourceType")


class SubjectDetailResponseModel(BaseModel):
    subject: SubjectDetailModel = Field(alias="subject")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTrustAnchorRequestModel(BaseModel):
    name: str = Field(alias="name")
    source: SourceModel = Field(alias="source")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="tags")


class TrustAnchorDetailModel(BaseModel):
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    enabled: Optional[bool] = Field(default=None, alias="enabled")
    name: Optional[str] = Field(default=None, alias="name")
    source: Optional[SourceModel] = Field(default=None, alias="source")
    trust_anchor_arn: Optional[str] = Field(default=None, alias="trustAnchorArn")
    trust_anchor_id: Optional[str] = Field(default=None, alias="trustAnchorId")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")


class UpdateTrustAnchorRequestModel(BaseModel):
    trust_anchor_id: str = Field(alias="trustAnchorId")
    name: Optional[str] = Field(default=None, alias="name")
    source: Optional[SourceModel] = Field(default=None, alias="source")


class ListTrustAnchorsResponseModel(BaseModel):
    next_token: str = Field(alias="nextToken")
    trust_anchors: List[TrustAnchorDetailModel] = Field(alias="trustAnchors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TrustAnchorDetailResponseModel(BaseModel):
    trust_anchor: TrustAnchorDetailModel = Field(alias="trustAnchor")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
