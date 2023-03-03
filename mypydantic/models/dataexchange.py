# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ApiGatewayApiAssetModel(BaseModel):
    api_description: Optional[str] = Field(default=None, alias="ApiDescription")
    api_endpoint: Optional[str] = Field(default=None, alias="ApiEndpoint")
    api_id: Optional[str] = Field(default=None, alias="ApiId")
    api_key: Optional[str] = Field(default=None, alias="ApiKey")
    api_name: Optional[str] = Field(default=None, alias="ApiName")
    api_specification_download_url: Optional[str] = Field(
        default=None, alias="ApiSpecificationDownloadUrl"
    )
    api_specification_download_url_expires_at: Optional[datetime] = Field(
        default=None, alias="ApiSpecificationDownloadUrlExpiresAt"
    )
    protocol_type: Optional[Literal["REST"]] = Field(default=None, alias="ProtocolType")
    stage: Optional[str] = Field(default=None, alias="Stage")


class AssetDestinationEntryModel(BaseModel):
    asset_id: str = Field(alias="AssetId")
    bucket: str = Field(alias="Bucket")
    key: Optional[str] = Field(default=None, alias="Key")


class RedshiftDataShareAssetModel(BaseModel):
    arn: str = Field(alias="Arn")


class S3DataAccessAssetModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key_prefixes: Optional[List[str]] = Field(default=None, alias="KeyPrefixes")
    keys: Optional[List[str]] = Field(default=None, alias="Keys")
    s3_access_point_alias: Optional[str] = Field(
        default=None, alias="S3AccessPointAlias"
    )
    s3_access_point_arn: Optional[str] = Field(default=None, alias="S3AccessPointArn")


class S3SnapshotAssetModel(BaseModel):
    size: float = Field(alias="Size")


class AssetSourceEntryModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")


class AutoExportRevisionDestinationEntryModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key_pattern: Optional[str] = Field(default=None, alias="KeyPattern")


class ExportServerSideEncryptionModel(BaseModel):
    type: Literal["AES256", "aws:kms"] = Field(alias="Type")
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class CancelJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class CreateDataSetRequestModel(BaseModel):
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    description: str = Field(alias="Description")
    name: str = Field(alias="Name")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class OriginDetailsModel(BaseModel):
    product_id: str = Field(alias="ProductId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateRevisionRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    comment: Optional[str] = Field(default=None, alias="Comment")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class S3DataAccessAssetSourceEntryModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key_prefixes: Optional[Sequence[str]] = Field(default=None, alias="KeyPrefixes")
    keys: Optional[Sequence[str]] = Field(default=None, alias="Keys")


class LFTagModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    tag_values: Sequence[str] = Field(alias="TagValues")


class DeleteAssetRequestModel(BaseModel):
    asset_id: str = Field(alias="AssetId")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class DeleteDataSetRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")


class DeleteEventActionRequestModel(BaseModel):
    event_action_id: str = Field(alias="EventActionId")


class DeleteRevisionRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class ImportAssetFromSignedUrlJobErrorDetailsModel(BaseModel):
    asset_name: str = Field(alias="AssetName")


class RevisionPublishedModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")


class ExportAssetToSignedUrlRequestDetailsModel(BaseModel):
    asset_id: str = Field(alias="AssetId")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class ExportAssetToSignedUrlResponseDetailsModel(BaseModel):
    asset_id: str = Field(alias="AssetId")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    signed_url: Optional[str] = Field(default=None, alias="SignedUrl")
    signed_url_expires_at: Optional[datetime] = Field(
        default=None, alias="SignedUrlExpiresAt"
    )


class RevisionDestinationEntryModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    revision_id: str = Field(alias="RevisionId")
    key_pattern: Optional[str] = Field(default=None, alias="KeyPattern")


class GetAssetRequestModel(BaseModel):
    asset_id: str = Field(alias="AssetId")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class GetDataSetRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")


class GetEventActionRequestModel(BaseModel):
    event_action_id: str = Field(alias="EventActionId")


class GetJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class GetRevisionRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class ImportAssetFromApiGatewayApiRequestDetailsModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    api_name: str = Field(alias="ApiName")
    api_specification_md5_hash: str = Field(alias="ApiSpecificationMd5Hash")
    data_set_id: str = Field(alias="DataSetId")
    protocol_type: Literal["REST"] = Field(alias="ProtocolType")
    revision_id: str = Field(alias="RevisionId")
    stage: str = Field(alias="Stage")
    api_description: Optional[str] = Field(default=None, alias="ApiDescription")
    api_key: Optional[str] = Field(default=None, alias="ApiKey")


class ImportAssetFromApiGatewayApiResponseDetailsModel(BaseModel):
    api_id: str = Field(alias="ApiId")
    api_name: str = Field(alias="ApiName")
    api_specification_md5_hash: str = Field(alias="ApiSpecificationMd5Hash")
    api_specification_upload_url: str = Field(alias="ApiSpecificationUploadUrl")
    api_specification_upload_url_expires_at: datetime = Field(
        alias="ApiSpecificationUploadUrlExpiresAt"
    )
    data_set_id: str = Field(alias="DataSetId")
    protocol_type: Literal["REST"] = Field(alias="ProtocolType")
    revision_id: str = Field(alias="RevisionId")
    stage: str = Field(alias="Stage")
    api_description: Optional[str] = Field(default=None, alias="ApiDescription")
    api_key: Optional[str] = Field(default=None, alias="ApiKey")


class ImportAssetFromSignedUrlRequestDetailsModel(BaseModel):
    asset_name: str = Field(alias="AssetName")
    data_set_id: str = Field(alias="DataSetId")
    md5_hash: str = Field(alias="Md5Hash")
    revision_id: str = Field(alias="RevisionId")


class ImportAssetFromSignedUrlResponseDetailsModel(BaseModel):
    asset_name: str = Field(alias="AssetName")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    md5_hash: Optional[str] = Field(default=None, alias="Md5Hash")
    signed_url: Optional[str] = Field(default=None, alias="SignedUrl")
    signed_url_expires_at: Optional[datetime] = Field(
        default=None, alias="SignedUrlExpiresAt"
    )


class RedshiftDataShareAssetSourceEntryModel(BaseModel):
    data_share_arn: str = Field(alias="DataShareArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListDataSetRevisionsRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RevisionEntryModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    id: str = Field(alias="Id")
    updated_at: datetime = Field(alias="UpdatedAt")
    comment: Optional[str] = Field(default=None, alias="Comment")
    finalized: Optional[bool] = Field(default=None, alias="Finalized")
    source_id: Optional[str] = Field(default=None, alias="SourceId")
    revocation_comment: Optional[str] = Field(default=None, alias="RevocationComment")
    revoked: Optional[bool] = Field(default=None, alias="Revoked")
    revoked_at: Optional[datetime] = Field(default=None, alias="RevokedAt")


class ListDataSetsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    origin: Optional[str] = Field(default=None, alias="Origin")


class ListEventActionsRequestModel(BaseModel):
    event_source_id: Optional[str] = Field(default=None, alias="EventSourceId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListJobsRequestModel(BaseModel):
    data_set_id: Optional[str] = Field(default=None, alias="DataSetId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")


class ListRevisionAssetsRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class RevokeRevisionRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    revocation_comment: str = Field(alias="RevocationComment")


class SendApiAssetRequestModel(BaseModel):
    asset_id: str = Field(alias="AssetId")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    body: Optional[str] = Field(default=None, alias="Body")
    query_string_parameters: Optional[Mapping[str, str]] = Field(
        default=None, alias="QueryStringParameters"
    )
    request_headers: Optional[Mapping[str, str]] = Field(
        default=None, alias="RequestHeaders"
    )
    method: Optional[str] = Field(default=None, alias="Method")
    path: Optional[str] = Field(default=None, alias="Path")


class StartJobRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAssetRequestModel(BaseModel):
    asset_id: str = Field(alias="AssetId")
    data_set_id: str = Field(alias="DataSetId")
    name: str = Field(alias="Name")
    revision_id: str = Field(alias="RevisionId")


class UpdateDataSetRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")


class UpdateRevisionRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    comment: Optional[str] = Field(default=None, alias="Comment")
    finalized: Optional[bool] = Field(default=None, alias="Finalized")


class ImportAssetsFromS3RequestDetailsModel(BaseModel):
    asset_sources: Sequence[AssetSourceEntryModel] = Field(alias="AssetSources")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class ImportAssetsFromS3ResponseDetailsModel(BaseModel):
    asset_sources: List[AssetSourceEntryModel] = Field(alias="AssetSources")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class AutoExportRevisionToS3RequestDetailsModel(BaseModel):
    revision_destination: AutoExportRevisionDestinationEntryModel = Field(
        alias="RevisionDestination"
    )
    encryption: Optional[ExportServerSideEncryptionModel] = Field(
        default=None, alias="Encryption"
    )


class ExportAssetsToS3RequestDetailsModel(BaseModel):
    asset_destinations: Sequence[AssetDestinationEntryModel] = Field(
        alias="AssetDestinations"
    )
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    encryption: Optional[ExportServerSideEncryptionModel] = Field(
        default=None, alias="Encryption"
    )


class ExportAssetsToS3ResponseDetailsModel(BaseModel):
    asset_destinations: List[AssetDestinationEntryModel] = Field(
        alias="AssetDestinations"
    )
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    encryption: Optional[ExportServerSideEncryptionModel] = Field(
        default=None, alias="Encryption"
    )


class DataSetEntryModel(BaseModel):
    arn: str = Field(alias="Arn")
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    created_at: datetime = Field(alias="CreatedAt")
    description: str = Field(alias="Description")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    origin: Literal["ENTITLED", "OWNED"] = Field(alias="Origin")
    updated_at: datetime = Field(alias="UpdatedAt")
    origin_details: Optional[OriginDetailsModel] = Field(
        default=None, alias="OriginDetails"
    )
    source_id: Optional[str] = Field(default=None, alias="SourceId")


class CreateDataSetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    created_at: datetime = Field(alias="CreatedAt")
    description: str = Field(alias="Description")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    origin: Literal["ENTITLED", "OWNED"] = Field(alias="Origin")
    origin_details: OriginDetailsModel = Field(alias="OriginDetails")
    source_id: str = Field(alias="SourceId")
    tags: Dict[str, str] = Field(alias="Tags")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRevisionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    comment: str = Field(alias="Comment")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    finalized: bool = Field(alias="Finalized")
    id: str = Field(alias="Id")
    source_id: str = Field(alias="SourceId")
    tags: Dict[str, str] = Field(alias="Tags")
    updated_at: datetime = Field(alias="UpdatedAt")
    revocation_comment: str = Field(alias="RevocationComment")
    revoked: bool = Field(alias="Revoked")
    revoked_at: datetime = Field(alias="RevokedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDataSetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    created_at: datetime = Field(alias="CreatedAt")
    description: str = Field(alias="Description")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    origin: Literal["ENTITLED", "OWNED"] = Field(alias="Origin")
    origin_details: OriginDetailsModel = Field(alias="OriginDetails")
    source_id: str = Field(alias="SourceId")
    tags: Dict[str, str] = Field(alias="Tags")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRevisionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    comment: str = Field(alias="Comment")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    finalized: bool = Field(alias="Finalized")
    id: str = Field(alias="Id")
    source_id: str = Field(alias="SourceId")
    tags: Dict[str, str] = Field(alias="Tags")
    updated_at: datetime = Field(alias="UpdatedAt")
    revocation_comment: str = Field(alias="RevocationComment")
    revoked: bool = Field(alias="Revoked")
    revoked_at: datetime = Field(alias="RevokedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RevokeRevisionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    comment: str = Field(alias="Comment")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    finalized: bool = Field(alias="Finalized")
    id: str = Field(alias="Id")
    source_id: str = Field(alias="SourceId")
    updated_at: datetime = Field(alias="UpdatedAt")
    revocation_comment: str = Field(alias="RevocationComment")
    revoked: bool = Field(alias="Revoked")
    revoked_at: datetime = Field(alias="RevokedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SendApiAssetResponseModel(BaseModel):
    body: str = Field(alias="Body")
    response_headers: Dict[str, str] = Field(alias="ResponseHeaders")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    created_at: datetime = Field(alias="CreatedAt")
    description: str = Field(alias="Description")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    origin: Literal["ENTITLED", "OWNED"] = Field(alias="Origin")
    origin_details: OriginDetailsModel = Field(alias="OriginDetails")
    source_id: str = Field(alias="SourceId")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRevisionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    comment: str = Field(alias="Comment")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    finalized: bool = Field(alias="Finalized")
    id: str = Field(alias="Id")
    source_id: str = Field(alias="SourceId")
    updated_at: datetime = Field(alias="UpdatedAt")
    revocation_comment: str = Field(alias="RevocationComment")
    revoked: bool = Field(alias="Revoked")
    revoked_at: datetime = Field(alias="RevokedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateS3DataAccessFromS3BucketRequestDetailsModel(BaseModel):
    asset_source: S3DataAccessAssetSourceEntryModel = Field(alias="AssetSource")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class CreateS3DataAccessFromS3BucketResponseDetailsModel(BaseModel):
    asset_source: S3DataAccessAssetSourceEntryModel = Field(alias="AssetSource")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class DatabaseLFTagPolicyAndPermissionsModel(BaseModel):
    expression: Sequence[LFTagModel] = Field(alias="Expression")
    permissions: Sequence[Literal["DESCRIBE"]] = Field(alias="Permissions")


class DatabaseLFTagPolicyModel(BaseModel):
    expression: List[LFTagModel] = Field(alias="Expression")


class TableLFTagPolicyAndPermissionsModel(BaseModel):
    expression: Sequence[LFTagModel] = Field(alias="Expression")
    permissions: Sequence[Literal["DESCRIBE", "SELECT"]] = Field(alias="Permissions")


class TableLFTagPolicyModel(BaseModel):
    expression: List[LFTagModel] = Field(alias="Expression")


class DetailsModel(BaseModel):
    import_asset_from_signed_url_job_error_details: Optional[
        ImportAssetFromSignedUrlJobErrorDetailsModel
    ] = Field(default=None, alias="ImportAssetFromSignedUrlJobErrorDetails")
    import_assets_from_s3_job_error_details: Optional[
        List[AssetSourceEntryModel]
    ] = Field(default=None, alias="ImportAssetsFromS3JobErrorDetails")


class EventModel(BaseModel):
    revision_published: Optional[RevisionPublishedModel] = Field(
        default=None, alias="RevisionPublished"
    )


class ExportRevisionsToS3RequestDetailsModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_destinations: Sequence[RevisionDestinationEntryModel] = Field(
        alias="RevisionDestinations"
    )
    encryption: Optional[ExportServerSideEncryptionModel] = Field(
        default=None, alias="Encryption"
    )


class ExportRevisionsToS3ResponseDetailsModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_destinations: List[RevisionDestinationEntryModel] = Field(
        alias="RevisionDestinations"
    )
    encryption: Optional[ExportServerSideEncryptionModel] = Field(
        default=None, alias="Encryption"
    )
    event_action_arn: Optional[str] = Field(default=None, alias="EventActionArn")


class ImportAssetsFromRedshiftDataSharesRequestDetailsModel(BaseModel):
    asset_sources: Sequence[RedshiftDataShareAssetSourceEntryModel] = Field(
        alias="AssetSources"
    )
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class ImportAssetsFromRedshiftDataSharesResponseDetailsModel(BaseModel):
    asset_sources: List[RedshiftDataShareAssetSourceEntryModel] = Field(
        alias="AssetSources"
    )
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")


class ListDataSetRevisionsRequestListDataSetRevisionsPaginateModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataSetsRequestListDataSetsPaginateModel(BaseModel):
    origin: Optional[str] = Field(default=None, alias="Origin")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListEventActionsRequestListEventActionsPaginateModel(BaseModel):
    event_source_id: Optional[str] = Field(default=None, alias="EventSourceId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestListJobsPaginateModel(BaseModel):
    data_set_id: Optional[str] = Field(default=None, alias="DataSetId")
    revision_id: Optional[str] = Field(default=None, alias="RevisionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRevisionAssetsRequestListRevisionAssetsPaginateModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataSetRevisionsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    revisions: List[RevisionEntryModel] = Field(alias="Revisions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionModel(BaseModel):
    export_revision_to_s3: Optional[AutoExportRevisionToS3RequestDetailsModel] = Field(
        default=None, alias="ExportRevisionToS3"
    )


class ListDataSetsResponseModel(BaseModel):
    data_sets: List[DataSetEntryModel] = Field(alias="DataSets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ImportAssetsFromLakeFormationTagPolicyRequestDetailsModel(BaseModel):
    catalog_id: str = Field(alias="CatalogId")
    role_arn: str = Field(alias="RoleArn")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    database: Optional[DatabaseLFTagPolicyAndPermissionsModel] = Field(
        default=None, alias="Database"
    )
    table: Optional[TableLFTagPolicyAndPermissionsModel] = Field(
        default=None, alias="Table"
    )


class ImportAssetsFromLakeFormationTagPolicyResponseDetailsModel(BaseModel):
    catalog_id: str = Field(alias="CatalogId")
    role_arn: str = Field(alias="RoleArn")
    data_set_id: str = Field(alias="DataSetId")
    revision_id: str = Field(alias="RevisionId")
    database: Optional[DatabaseLFTagPolicyAndPermissionsModel] = Field(
        default=None, alias="Database"
    )
    table: Optional[TableLFTagPolicyAndPermissionsModel] = Field(
        default=None, alias="Table"
    )


class LFResourceDetailsModel(BaseModel):
    database: Optional[DatabaseLFTagPolicyModel] = Field(default=None, alias="Database")
    table: Optional[TableLFTagPolicyModel] = Field(default=None, alias="Table")


class JobErrorModel(BaseModel):
    code: Literal[
        "ACCESS_DENIED_EXCEPTION",
        "INTERNAL_SERVER_EXCEPTION",
        "MALWARE_DETECTED",
        "MALWARE_SCAN_ENCRYPTED_FILE",
        "RESOURCE_NOT_FOUND_EXCEPTION",
        "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
        "VALIDATION_EXCEPTION",
    ] = Field(alias="Code")
    message: str = Field(alias="Message")
    details: Optional[DetailsModel] = Field(default=None, alias="Details")
    limit_name: Optional[
        Literal[
            "AWS Lake Formation data permission assets per revision",
            "Amazon Redshift datashare assets per revision",
            "Amazon S3 data access assets per revision",
            "Asset size in GB",
            "Assets per revision",
        ]
    ] = Field(default=None, alias="LimitName")
    limit_value: Optional[float] = Field(default=None, alias="LimitValue")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_type: Optional[Literal["ASSET", "DATA_SET", "REVISION"]] = Field(
        default=None, alias="ResourceType"
    )


class CreateEventActionRequestModel(BaseModel):
    action: ActionModel = Field(alias="Action")
    event: EventModel = Field(alias="Event")


class CreateEventActionResponseModel(BaseModel):
    action: ActionModel = Field(alias="Action")
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    event: EventModel = Field(alias="Event")
    id: str = Field(alias="Id")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EventActionEntryModel(BaseModel):
    action: ActionModel = Field(alias="Action")
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    event: EventModel = Field(alias="Event")
    id: str = Field(alias="Id")
    updated_at: datetime = Field(alias="UpdatedAt")


class GetEventActionResponseModel(BaseModel):
    action: ActionModel = Field(alias="Action")
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    event: EventModel = Field(alias="Event")
    id: str = Field(alias="Id")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateEventActionRequestModel(BaseModel):
    event_action_id: str = Field(alias="EventActionId")
    action: Optional[ActionModel] = Field(default=None, alias="Action")


class UpdateEventActionResponseModel(BaseModel):
    action: ActionModel = Field(alias="Action")
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    event: EventModel = Field(alias="Event")
    id: str = Field(alias="Id")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RequestDetailsModel(BaseModel):
    export_asset_to_signed_url: Optional[
        ExportAssetToSignedUrlRequestDetailsModel
    ] = Field(default=None, alias="ExportAssetToSignedUrl")
    export_assets_to_s3: Optional[ExportAssetsToS3RequestDetailsModel] = Field(
        default=None, alias="ExportAssetsToS3"
    )
    export_revisions_to_s3: Optional[ExportRevisionsToS3RequestDetailsModel] = Field(
        default=None, alias="ExportRevisionsToS3"
    )
    import_asset_from_signed_url: Optional[
        ImportAssetFromSignedUrlRequestDetailsModel
    ] = Field(default=None, alias="ImportAssetFromSignedUrl")
    import_assets_from_s3: Optional[ImportAssetsFromS3RequestDetailsModel] = Field(
        default=None, alias="ImportAssetsFromS3"
    )
    import_assets_from_redshift_data_shares: Optional[
        ImportAssetsFromRedshiftDataSharesRequestDetailsModel
    ] = Field(default=None, alias="ImportAssetsFromRedshiftDataShares")
    import_asset_from_api_gateway_api: Optional[
        ImportAssetFromApiGatewayApiRequestDetailsModel
    ] = Field(default=None, alias="ImportAssetFromApiGatewayApi")
    create_s3_data_access_from_s3_bucket: Optional[
        CreateS3DataAccessFromS3BucketRequestDetailsModel
    ] = Field(default=None, alias="CreateS3DataAccessFromS3Bucket")
    import_assets_from_lake_formation_tag_policy: Optional[
        ImportAssetsFromLakeFormationTagPolicyRequestDetailsModel
    ] = Field(default=None, alias="ImportAssetsFromLakeFormationTagPolicy")


class ResponseDetailsModel(BaseModel):
    export_asset_to_signed_url: Optional[
        ExportAssetToSignedUrlResponseDetailsModel
    ] = Field(default=None, alias="ExportAssetToSignedUrl")
    export_assets_to_s3: Optional[ExportAssetsToS3ResponseDetailsModel] = Field(
        default=None, alias="ExportAssetsToS3"
    )
    export_revisions_to_s3: Optional[ExportRevisionsToS3ResponseDetailsModel] = Field(
        default=None, alias="ExportRevisionsToS3"
    )
    import_asset_from_signed_url: Optional[
        ImportAssetFromSignedUrlResponseDetailsModel
    ] = Field(default=None, alias="ImportAssetFromSignedUrl")
    import_assets_from_s3: Optional[ImportAssetsFromS3ResponseDetailsModel] = Field(
        default=None, alias="ImportAssetsFromS3"
    )
    import_assets_from_redshift_data_shares: Optional[
        ImportAssetsFromRedshiftDataSharesResponseDetailsModel
    ] = Field(default=None, alias="ImportAssetsFromRedshiftDataShares")
    import_asset_from_api_gateway_api: Optional[
        ImportAssetFromApiGatewayApiResponseDetailsModel
    ] = Field(default=None, alias="ImportAssetFromApiGatewayApi")
    create_s3_data_access_from_s3_bucket: Optional[
        CreateS3DataAccessFromS3BucketResponseDetailsModel
    ] = Field(default=None, alias="CreateS3DataAccessFromS3Bucket")
    import_assets_from_lake_formation_tag_policy: Optional[
        ImportAssetsFromLakeFormationTagPolicyResponseDetailsModel
    ] = Field(default=None, alias="ImportAssetsFromLakeFormationTagPolicy")


class LFTagPolicyDetailsModel(BaseModel):
    catalog_id: str = Field(alias="CatalogId")
    resource_type: Literal["DATABASE", "TABLE"] = Field(alias="ResourceType")
    resource_details: LFResourceDetailsModel = Field(alias="ResourceDetails")


class ListEventActionsResponseModel(BaseModel):
    event_actions: List[EventActionEntryModel] = Field(alias="EventActions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobRequestModel(BaseModel):
    details: RequestDetailsModel = Field(alias="Details")
    type: Literal[
        "CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET",
        "EXPORT_ASSETS_TO_S3",
        "EXPORT_ASSET_TO_SIGNED_URL",
        "EXPORT_REVISIONS_TO_S3",
        "IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY",
        "IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES",
        "IMPORT_ASSETS_FROM_S3",
        "IMPORT_ASSET_FROM_API_GATEWAY_API",
        "IMPORT_ASSET_FROM_SIGNED_URL",
    ] = Field(alias="Type")


class CreateJobResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    details: ResponseDetailsModel = Field(alias="Details")
    errors: List[JobErrorModel] = Field(alias="Errors")
    id: str = Field(alias="Id")
    state: Literal[
        "CANCELLED", "COMPLETED", "ERROR", "IN_PROGRESS", "TIMED_OUT", "WAITING"
    ] = Field(alias="State")
    type: Literal[
        "CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET",
        "EXPORT_ASSETS_TO_S3",
        "EXPORT_ASSET_TO_SIGNED_URL",
        "EXPORT_REVISIONS_TO_S3",
        "IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY",
        "IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES",
        "IMPORT_ASSETS_FROM_S3",
        "IMPORT_ASSET_FROM_API_GATEWAY_API",
        "IMPORT_ASSET_FROM_SIGNED_URL",
    ] = Field(alias="Type")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    details: ResponseDetailsModel = Field(alias="Details")
    errors: List[JobErrorModel] = Field(alias="Errors")
    id: str = Field(alias="Id")
    state: Literal[
        "CANCELLED", "COMPLETED", "ERROR", "IN_PROGRESS", "TIMED_OUT", "WAITING"
    ] = Field(alias="State")
    type: Literal[
        "CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET",
        "EXPORT_ASSETS_TO_S3",
        "EXPORT_ASSET_TO_SIGNED_URL",
        "EXPORT_REVISIONS_TO_S3",
        "IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY",
        "IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES",
        "IMPORT_ASSETS_FROM_S3",
        "IMPORT_ASSET_FROM_API_GATEWAY_API",
        "IMPORT_ASSET_FROM_SIGNED_URL",
    ] = Field(alias="Type")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class JobEntryModel(BaseModel):
    arn: str = Field(alias="Arn")
    created_at: datetime = Field(alias="CreatedAt")
    details: ResponseDetailsModel = Field(alias="Details")
    id: str = Field(alias="Id")
    state: Literal[
        "CANCELLED", "COMPLETED", "ERROR", "IN_PROGRESS", "TIMED_OUT", "WAITING"
    ] = Field(alias="State")
    type: Literal[
        "CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET",
        "EXPORT_ASSETS_TO_S3",
        "EXPORT_ASSET_TO_SIGNED_URL",
        "EXPORT_REVISIONS_TO_S3",
        "IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY",
        "IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES",
        "IMPORT_ASSETS_FROM_S3",
        "IMPORT_ASSET_FROM_API_GATEWAY_API",
        "IMPORT_ASSET_FROM_SIGNED_URL",
    ] = Field(alias="Type")
    updated_at: datetime = Field(alias="UpdatedAt")
    errors: Optional[List[JobErrorModel]] = Field(default=None, alias="Errors")


class LakeFormationDataPermissionDetailsModel(BaseModel):
    l_ftag_policy: Optional[LFTagPolicyDetailsModel] = Field(
        default=None, alias="LFTagPolicy"
    )


class ListJobsResponseModel(BaseModel):
    jobs: List[JobEntryModel] = Field(alias="Jobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LakeFormationDataPermissionAssetModel(BaseModel):
    lake_formation_data_permission_details: LakeFormationDataPermissionDetailsModel = (
        Field(alias="LakeFormationDataPermissionDetails")
    )
    lake_formation_data_permission_type: Literal["LFTagPolicy"] = Field(
        alias="LakeFormationDataPermissionType"
    )
    permissions: List[Literal["DESCRIBE", "SELECT"]] = Field(alias="Permissions")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class AssetDetailsModel(BaseModel):
    s3_snapshot_asset: Optional[S3SnapshotAssetModel] = Field(
        default=None, alias="S3SnapshotAsset"
    )
    redshift_data_share_asset: Optional[RedshiftDataShareAssetModel] = Field(
        default=None, alias="RedshiftDataShareAsset"
    )
    api_gateway_api_asset: Optional[ApiGatewayApiAssetModel] = Field(
        default=None, alias="ApiGatewayApiAsset"
    )
    s3_data_access_asset: Optional[S3DataAccessAssetModel] = Field(
        default=None, alias="S3DataAccessAsset"
    )
    lake_formation_data_permission_asset: Optional[
        LakeFormationDataPermissionAssetModel
    ] = Field(default=None, alias="LakeFormationDataPermissionAsset")


class AssetEntryModel(BaseModel):
    arn: str = Field(alias="Arn")
    asset_details: AssetDetailsModel = Field(alias="AssetDetails")
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    revision_id: str = Field(alias="RevisionId")
    updated_at: datetime = Field(alias="UpdatedAt")
    source_id: Optional[str] = Field(default=None, alias="SourceId")


class GetAssetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    asset_details: AssetDetailsModel = Field(alias="AssetDetails")
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    revision_id: str = Field(alias="RevisionId")
    source_id: str = Field(alias="SourceId")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAssetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    asset_details: AssetDetailsModel = Field(alias="AssetDetails")
    asset_type: Literal[
        "API_GATEWAY_API",
        "LAKE_FORMATION_DATA_PERMISSION",
        "REDSHIFT_DATA_SHARE",
        "S3_DATA_ACCESS",
        "S3_SNAPSHOT",
    ] = Field(alias="AssetType")
    created_at: datetime = Field(alias="CreatedAt")
    data_set_id: str = Field(alias="DataSetId")
    id: str = Field(alias="Id")
    name: str = Field(alias="Name")
    revision_id: str = Field(alias="RevisionId")
    source_id: str = Field(alias="SourceId")
    updated_at: datetime = Field(alias="UpdatedAt")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRevisionAssetsResponseModel(BaseModel):
    assets: List[AssetEntryModel] = Field(alias="Assets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
