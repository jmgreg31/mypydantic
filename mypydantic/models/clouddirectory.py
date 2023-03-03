# Model Generated: Thu Mar  2 21:56:17 2023

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


class ObjectReferenceModel(BaseModel):
    selector: Optional[str] = Field(default=None, alias="Selector")


class SchemaFacetModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    facet_name: Optional[str] = Field(default=None, alias="FacetName")


class ApplySchemaRequestModel(BaseModel):
    published_schema_arn: str = Field(alias="PublishedSchemaArn")
    directory_arn: str = Field(alias="DirectoryArn")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class TypedLinkSchemaAndFacetNameModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    typed_link_name: str = Field(alias="TypedLinkName")


class AttributeKeyModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    facet_name: str = Field(alias="FacetName")
    name: str = Field(alias="Name")


class TypedAttributeValueModel(BaseModel):
    string_value: Optional[str] = Field(default=None, alias="StringValue")
    binary_value: Optional[
        Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]
    ] = Field(default=None, alias="BinaryValue")
    boolean_value: Optional[bool] = Field(default=None, alias="BooleanValue")
    number_value: Optional[str] = Field(default=None, alias="NumberValue")
    datetime_value: Optional[Union[datetime, str]] = Field(
        default=None, alias="DatetimeValue"
    )


class BatchAttachObjectResponseModel(BaseModel):
    attached_object_identifier: Optional[str] = Field(
        default=None, alias="attachedObjectIdentifier"
    )


class BatchAttachToIndexResponseModel(BaseModel):
    attached_object_identifier: Optional[str] = Field(
        default=None, alias="AttachedObjectIdentifier"
    )


class BatchCreateIndexResponseModel(BaseModel):
    object_identifier: Optional[str] = Field(default=None, alias="ObjectIdentifier")


class BatchCreateObjectResponseModel(BaseModel):
    object_identifier: Optional[str] = Field(default=None, alias="ObjectIdentifier")


class BatchDetachFromIndexResponseModel(BaseModel):
    detached_object_identifier: Optional[str] = Field(
        default=None, alias="DetachedObjectIdentifier"
    )


class BatchDetachObjectResponseModel(BaseModel):
    detached_object_identifier: Optional[str] = Field(
        default=None, alias="detachedObjectIdentifier"
    )


class BatchListObjectChildrenResponseModel(BaseModel):
    children: Optional[Dict[str, str]] = Field(default=None, alias="Children")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PathToObjectIdentifiersModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    object_identifiers: Optional[List[str]] = Field(
        default=None, alias="ObjectIdentifiers"
    )


class ObjectIdentifierAndLinkNameTupleModel(BaseModel):
    object_identifier: Optional[str] = Field(default=None, alias="ObjectIdentifier")
    link_name: Optional[str] = Field(default=None, alias="LinkName")


class BatchListObjectPoliciesResponseModel(BaseModel):
    attached_policy_ids: Optional[List[str]] = Field(
        default=None, alias="AttachedPolicyIds"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class BatchListPolicyAttachmentsResponseModel(BaseModel):
    object_identifiers: Optional[List[str]] = Field(
        default=None, alias="ObjectIdentifiers"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class BatchReadExceptionModel(BaseModel):
    type: Optional[
        Literal[
            "AccessDeniedException",
            "CannotListParentOfRootException",
            "DirectoryNotEnabledException",
            "FacetValidationException",
            "InternalServiceException",
            "InvalidArnException",
            "InvalidNextTokenException",
            "LimitExceededException",
            "NotIndexException",
            "NotNodeException",
            "NotPolicyException",
            "ResourceNotFoundException",
            "ValidationException",
        ]
    ] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")


class BatchUpdateObjectAttributesResponseModel(BaseModel):
    object_identifier: Optional[str] = Field(default=None, alias="ObjectIdentifier")


class CreateDirectoryRequestModel(BaseModel):
    name: str = Field(alias="Name")
    schema_arn: str = Field(alias="SchemaArn")


class CreateSchemaRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteDirectoryRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")


class DeleteFacetRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")


class DeleteSchemaRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")


class DeleteTypedLinkFacetRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")


class DirectoryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    directory_arn: Optional[str] = Field(default=None, alias="DirectoryArn")
    state: Optional[Literal["DELETED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="State"
    )
    creation_date_time: Optional[datetime] = Field(
        default=None, alias="CreationDateTime"
    )


class DisableDirectoryRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")


class EnableDirectoryRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")


class RuleModel(BaseModel):
    type: Optional[
        Literal[
            "BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"
        ]
    ] = Field(default=None, alias="Type")
    parameters: Optional[Mapping[str, str]] = Field(default=None, alias="Parameters")


class FacetAttributeReferenceModel(BaseModel):
    target_facet_name: str = Field(alias="TargetFacetName")
    target_attribute_name: str = Field(alias="TargetAttributeName")


class FacetModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    object_type: Optional[Literal["INDEX", "LEAF_NODE", "NODE", "POLICY"]] = Field(
        default=None, alias="ObjectType"
    )
    facet_style: Optional[Literal["DYNAMIC", "STATIC"]] = Field(
        default=None, alias="FacetStyle"
    )


class GetAppliedSchemaVersionRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")


class GetDirectoryRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")


class GetFacetRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")


class GetSchemaAsJsonRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")


class GetTypedLinkFacetInformationRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAppliedSchemaArnsRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDevelopmentSchemaArnsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDirectoriesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    state: Optional[Literal["DELETED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="state"
    )


class ListFacetAttributesRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFacetNamesRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListManagedSchemaArnsRequestModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListPublishedSchemaArnsRequestModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class ListTypedLinkFacetAttributesRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTypedLinkFacetNamesRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class PolicyAttachmentModel(BaseModel):
    policy_id: Optional[str] = Field(default=None, alias="PolicyId")
    object_identifier: Optional[str] = Field(default=None, alias="ObjectIdentifier")
    policy_type: Optional[str] = Field(default=None, alias="PolicyType")


class PublishSchemaRequestModel(BaseModel):
    development_schema_arn: str = Field(alias="DevelopmentSchemaArn")
    version: str = Field(alias="Version")
    minor_version: Optional[str] = Field(default=None, alias="MinorVersion")
    name: Optional[str] = Field(default=None, alias="Name")


class PutSchemaFromJsonRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    document: str = Field(alias="Document")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateSchemaRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")


class UpgradeAppliedSchemaRequestModel(BaseModel):
    published_schema_arn: str = Field(alias="PublishedSchemaArn")
    directory_arn: str = Field(alias="DirectoryArn")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class UpgradePublishedSchemaRequestModel(BaseModel):
    development_schema_arn: str = Field(alias="DevelopmentSchemaArn")
    published_schema_arn: str = Field(alias="PublishedSchemaArn")
    minor_version: str = Field(alias="MinorVersion")
    dry_run: Optional[bool] = Field(default=None, alias="DryRun")


class AttachObjectRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    parent_reference: ObjectReferenceModel = Field(alias="ParentReference")
    child_reference: ObjectReferenceModel = Field(alias="ChildReference")
    link_name: str = Field(alias="LinkName")


class AttachPolicyRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    policy_reference: ObjectReferenceModel = Field(alias="PolicyReference")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class AttachToIndexRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    index_reference: ObjectReferenceModel = Field(alias="IndexReference")
    target_reference: ObjectReferenceModel = Field(alias="TargetReference")


class BatchAttachObjectModel(BaseModel):
    parent_reference: ObjectReferenceModel = Field(alias="ParentReference")
    child_reference: ObjectReferenceModel = Field(alias="ChildReference")
    link_name: str = Field(alias="LinkName")


class BatchAttachPolicyModel(BaseModel):
    policy_reference: ObjectReferenceModel = Field(alias="PolicyReference")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class BatchAttachToIndexModel(BaseModel):
    index_reference: ObjectReferenceModel = Field(alias="IndexReference")
    target_reference: ObjectReferenceModel = Field(alias="TargetReference")


class BatchDeleteObjectModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class BatchDetachFromIndexModel(BaseModel):
    index_reference: ObjectReferenceModel = Field(alias="IndexReference")
    target_reference: ObjectReferenceModel = Field(alias="TargetReference")


class BatchDetachObjectModel(BaseModel):
    parent_reference: ObjectReferenceModel = Field(alias="ParentReference")
    link_name: str = Field(alias="LinkName")
    batch_reference_name: Optional[str] = Field(
        default=None, alias="BatchReferenceName"
    )


class BatchDetachPolicyModel(BaseModel):
    policy_reference: ObjectReferenceModel = Field(alias="PolicyReference")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class BatchGetObjectInformationModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class BatchListAttachedIndicesModel(BaseModel):
    target_reference: ObjectReferenceModel = Field(alias="TargetReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchListObjectChildrenModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchListObjectParentPathsModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchListObjectParentsModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchListObjectPoliciesModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchListPolicyAttachmentsModel(BaseModel):
    policy_reference: ObjectReferenceModel = Field(alias="PolicyReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchLookupPolicyModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DeleteObjectRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class DetachFromIndexRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    index_reference: ObjectReferenceModel = Field(alias="IndexReference")
    target_reference: ObjectReferenceModel = Field(alias="TargetReference")


class DetachObjectRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    parent_reference: ObjectReferenceModel = Field(alias="ParentReference")
    link_name: str = Field(alias="LinkName")


class DetachPolicyRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    policy_reference: ObjectReferenceModel = Field(alias="PolicyReference")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class GetObjectInformationRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class ListAttachedIndicesRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    target_reference: ObjectReferenceModel = Field(alias="TargetReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class ListObjectChildrenRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class ListObjectParentPathsRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListObjectParentsRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    include_all_links_to_each_parent: Optional[bool] = Field(
        default=None, alias="IncludeAllLinksToEachParent"
    )


class ListObjectPoliciesRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class ListPolicyAttachmentsRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    policy_reference: ObjectReferenceModel = Field(alias="PolicyReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class LookupPolicyRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchGetObjectAttributesModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    schema_facet: SchemaFacetModel = Field(alias="SchemaFacet")
    attribute_names: Sequence[str] = Field(alias="AttributeNames")


class BatchGetObjectInformationResponseModel(BaseModel):
    schema_facets: Optional[List[SchemaFacetModel]] = Field(
        default=None, alias="SchemaFacets"
    )
    object_identifier: Optional[str] = Field(default=None, alias="ObjectIdentifier")


class BatchListObjectAttributesModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    facet_filter: Optional[SchemaFacetModel] = Field(default=None, alias="FacetFilter")


class BatchRemoveFacetFromObjectModel(BaseModel):
    schema_facet: SchemaFacetModel = Field(alias="SchemaFacet")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class GetObjectAttributesRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    schema_facet: SchemaFacetModel = Field(alias="SchemaFacet")
    attribute_names: Sequence[str] = Field(alias="AttributeNames")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class ListObjectAttributesRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    facet_filter: Optional[SchemaFacetModel] = Field(default=None, alias="FacetFilter")


class RemoveFacetFromObjectRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    schema_facet: SchemaFacetModel = Field(alias="SchemaFacet")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class ApplySchemaResponseModel(BaseModel):
    applied_schema_arn: str = Field(alias="AppliedSchemaArn")
    directory_arn: str = Field(alias="DirectoryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachObjectResponseModel(BaseModel):
    attached_object_identifier: str = Field(alias="AttachedObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachToIndexResponseModel(BaseModel):
    attached_object_identifier: str = Field(alias="AttachedObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDirectoryResponseModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    name: str = Field(alias="Name")
    object_identifier: str = Field(alias="ObjectIdentifier")
    applied_schema_arn: str = Field(alias="AppliedSchemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIndexResponseModel(BaseModel):
    object_identifier: str = Field(alias="ObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateObjectResponseModel(BaseModel):
    object_identifier: str = Field(alias="ObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSchemaResponseModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDirectoryResponseModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSchemaResponseModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachFromIndexResponseModel(BaseModel):
    detached_object_identifier: str = Field(alias="DetachedObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetachObjectResponseModel(BaseModel):
    detached_object_identifier: str = Field(alias="DetachedObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisableDirectoryResponseModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EnableDirectoryResponseModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAppliedSchemaVersionResponseModel(BaseModel):
    applied_schema_arn: str = Field(alias="AppliedSchemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectInformationResponseModel(BaseModel):
    schema_facets: List[SchemaFacetModel] = Field(alias="SchemaFacets")
    object_identifier: str = Field(alias="ObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSchemaAsJsonResponseModel(BaseModel):
    name: str = Field(alias="Name")
    document: str = Field(alias="Document")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTypedLinkFacetInformationResponseModel(BaseModel):
    identity_attribute_order: List[str] = Field(alias="IdentityAttributeOrder")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppliedSchemaArnsResponseModel(BaseModel):
    schema_arns: List[str] = Field(alias="SchemaArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDevelopmentSchemaArnsResponseModel(BaseModel):
    schema_arns: List[str] = Field(alias="SchemaArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFacetNamesResponseModel(BaseModel):
    facet_names: List[str] = Field(alias="FacetNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListManagedSchemaArnsResponseModel(BaseModel):
    schema_arns: List[str] = Field(alias="SchemaArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListObjectChildrenResponseModel(BaseModel):
    children: Dict[str, str] = Field(alias="Children")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListObjectPoliciesResponseModel(BaseModel):
    attached_policy_ids: List[str] = Field(alias="AttachedPolicyIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPolicyAttachmentsResponseModel(BaseModel):
    object_identifiers: List[str] = Field(alias="ObjectIdentifiers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPublishedSchemaArnsResponseModel(BaseModel):
    schema_arns: List[str] = Field(alias="SchemaArns")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTypedLinkFacetNamesResponseModel(BaseModel):
    facet_names: List[str] = Field(alias="FacetNames")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PublishSchemaResponseModel(BaseModel):
    published_schema_arn: str = Field(alias="PublishedSchemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutSchemaFromJsonResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateObjectAttributesResponseModel(BaseModel):
    object_identifier: str = Field(alias="ObjectIdentifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSchemaResponseModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpgradeAppliedSchemaResponseModel(BaseModel):
    upgraded_schema_arn: str = Field(alias="UpgradedSchemaArn")
    directory_arn: str = Field(alias="DirectoryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpgradePublishedSchemaResponseModel(BaseModel):
    upgraded_schema_arn: str = Field(alias="UpgradedSchemaArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchCreateIndexModel(BaseModel):
    ordered_indexed_attribute_list: Sequence[AttributeKeyModel] = Field(
        alias="OrderedIndexedAttributeList"
    )
    is_unique: bool = Field(alias="IsUnique")
    parent_reference: Optional[ObjectReferenceModel] = Field(
        default=None, alias="ParentReference"
    )
    link_name: Optional[str] = Field(default=None, alias="LinkName")
    batch_reference_name: Optional[str] = Field(
        default=None, alias="BatchReferenceName"
    )


class CreateIndexRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    ordered_indexed_attribute_list: Sequence[AttributeKeyModel] = Field(
        alias="OrderedIndexedAttributeList"
    )
    is_unique: bool = Field(alias="IsUnique")
    parent_reference: Optional[ObjectReferenceModel] = Field(
        default=None, alias="ParentReference"
    )
    link_name: Optional[str] = Field(default=None, alias="LinkName")


class AttributeKeyAndValueModel(BaseModel):
    key: AttributeKeyModel = Field(alias="Key")
    value: TypedAttributeValueModel = Field(alias="Value")


class AttributeNameAndValueModel(BaseModel):
    attribute_name: str = Field(alias="AttributeName")
    value: TypedAttributeValueModel = Field(alias="Value")


class LinkAttributeActionModel(BaseModel):
    attribute_action_type: Optional[Literal["CREATE_OR_UPDATE", "DELETE"]] = Field(
        default=None, alias="AttributeActionType"
    )
    attribute_update_value: Optional[TypedAttributeValueModel] = Field(
        default=None, alias="AttributeUpdateValue"
    )


class ObjectAttributeActionModel(BaseModel):
    object_attribute_action_type: Optional[
        Literal["CREATE_OR_UPDATE", "DELETE"]
    ] = Field(default=None, alias="ObjectAttributeActionType")
    object_attribute_update_value: Optional[TypedAttributeValueModel] = Field(
        default=None, alias="ObjectAttributeUpdateValue"
    )


class TypedAttributeValueRangeModel(BaseModel):
    start_mode: Literal[
        "EXCLUSIVE", "FIRST", "INCLUSIVE", "LAST", "LAST_BEFORE_MISSING_VALUES"
    ] = Field(alias="StartMode")
    end_mode: Literal[
        "EXCLUSIVE", "FIRST", "INCLUSIVE", "LAST", "LAST_BEFORE_MISSING_VALUES"
    ] = Field(alias="EndMode")
    start_value: Optional[TypedAttributeValueModel] = Field(
        default=None, alias="StartValue"
    )
    end_value: Optional[TypedAttributeValueModel] = Field(
        default=None, alias="EndValue"
    )


class BatchListObjectParentPathsResponseModel(BaseModel):
    path_to_object_identifiers_list: Optional[
        List[PathToObjectIdentifiersModel]
    ] = Field(default=None, alias="PathToObjectIdentifiersList")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListObjectParentPathsResponseModel(BaseModel):
    path_to_object_identifiers_list: List[PathToObjectIdentifiersModel] = Field(
        alias="PathToObjectIdentifiersList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchListObjectParentsResponseModel(BaseModel):
    parent_links: Optional[List[ObjectIdentifierAndLinkNameTupleModel]] = Field(
        default=None, alias="ParentLinks"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListObjectParentsResponseModel(BaseModel):
    parents: Dict[str, str] = Field(alias="Parents")
    next_token: str = Field(alias="NextToken")
    parent_links: List[ObjectIdentifierAndLinkNameTupleModel] = Field(
        alias="ParentLinks"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDirectoryResponseModel(BaseModel):
    directory: DirectoryModel = Field(alias="Directory")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDirectoriesResponseModel(BaseModel):
    directories: List[DirectoryModel] = Field(alias="Directories")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FacetAttributeDefinitionModel(BaseModel):
    type: Literal[
        "BINARY", "BOOLEAN", "DATETIME", "NUMBER", "STRING", "VARIANT"
    ] = Field(alias="Type")
    default_value: Optional[TypedAttributeValueModel] = Field(
        default=None, alias="DefaultValue"
    )
    is_immutable: Optional[bool] = Field(default=None, alias="IsImmutable")
    rules: Optional[Mapping[str, RuleModel]] = Field(default=None, alias="Rules")


class TypedLinkAttributeDefinitionModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal[
        "BINARY", "BOOLEAN", "DATETIME", "NUMBER", "STRING", "VARIANT"
    ] = Field(alias="Type")
    required_behavior: Literal["NOT_REQUIRED", "REQUIRED_ALWAYS"] = Field(
        alias="RequiredBehavior"
    )
    default_value: Optional[TypedAttributeValueModel] = Field(
        default=None, alias="DefaultValue"
    )
    is_immutable: Optional[bool] = Field(default=None, alias="IsImmutable")
    rules: Optional[Mapping[str, RuleModel]] = Field(default=None, alias="Rules")


class GetFacetResponseModel(BaseModel):
    facet: FacetModel = Field(alias="Facet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAttachedIndicesRequestListAttachedIndicesPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    target_reference: ObjectReferenceModel = Field(alias="TargetReference")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDirectoriesRequestListDirectoriesPaginateModel(BaseModel):
    state: Optional[Literal["DELETED", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="state"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFacetAttributesRequestListFacetAttributesPaginateModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFacetNamesRequestListFacetNamesPaginateModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListObjectAttributesRequestListObjectAttributesPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    facet_filter: Optional[SchemaFacetModel] = Field(default=None, alias="FacetFilter")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListObjectParentPathsRequestListObjectParentPathsPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListObjectPoliciesRequestListObjectPoliciesPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    policy_reference: ObjectReferenceModel = Field(alias="PolicyReference")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateModel(BaseModel):
    schema_arn: Optional[str] = Field(default=None, alias="SchemaArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateModel(
    BaseModel
):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class LookupPolicyRequestLookupPolicyPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class PolicyToPathModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")
    policies: Optional[List[PolicyAttachmentModel]] = Field(
        default=None, alias="Policies"
    )


class AddFacetToObjectRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    schema_facet: SchemaFacetModel = Field(alias="SchemaFacet")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    object_attribute_list: Optional[Sequence[AttributeKeyAndValueModel]] = Field(
        default=None, alias="ObjectAttributeList"
    )


class BatchAddFacetToObjectModel(BaseModel):
    schema_facet: SchemaFacetModel = Field(alias="SchemaFacet")
    object_attribute_list: Sequence[AttributeKeyAndValueModel] = Field(
        alias="ObjectAttributeList"
    )
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")


class BatchCreateObjectModel(BaseModel):
    schema_facet: Sequence[SchemaFacetModel] = Field(alias="SchemaFacet")
    object_attribute_list: Sequence[AttributeKeyAndValueModel] = Field(
        alias="ObjectAttributeList"
    )
    parent_reference: Optional[ObjectReferenceModel] = Field(
        default=None, alias="ParentReference"
    )
    link_name: Optional[str] = Field(default=None, alias="LinkName")
    batch_reference_name: Optional[str] = Field(
        default=None, alias="BatchReferenceName"
    )


class BatchGetLinkAttributesResponseModel(BaseModel):
    attributes: Optional[List[AttributeKeyAndValueModel]] = Field(
        default=None, alias="Attributes"
    )


class BatchGetObjectAttributesResponseModel(BaseModel):
    attributes: Optional[List[AttributeKeyAndValueModel]] = Field(
        default=None, alias="Attributes"
    )


class BatchListObjectAttributesResponseModel(BaseModel):
    attributes: Optional[List[AttributeKeyAndValueModel]] = Field(
        default=None, alias="Attributes"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CreateObjectRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    schema_facets: Sequence[SchemaFacetModel] = Field(alias="SchemaFacets")
    object_attribute_list: Optional[Sequence[AttributeKeyAndValueModel]] = Field(
        default=None, alias="ObjectAttributeList"
    )
    parent_reference: Optional[ObjectReferenceModel] = Field(
        default=None, alias="ParentReference"
    )
    link_name: Optional[str] = Field(default=None, alias="LinkName")


class GetLinkAttributesResponseModel(BaseModel):
    attributes: List[AttributeKeyAndValueModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetObjectAttributesResponseModel(BaseModel):
    attributes: List[AttributeKeyAndValueModel] = Field(alias="Attributes")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IndexAttachmentModel(BaseModel):
    indexed_attributes: Optional[List[AttributeKeyAndValueModel]] = Field(
        default=None, alias="IndexedAttributes"
    )
    object_identifier: Optional[str] = Field(default=None, alias="ObjectIdentifier")


class ListObjectAttributesResponseModel(BaseModel):
    attributes: List[AttributeKeyAndValueModel] = Field(alias="Attributes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachTypedLinkRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    source_object_reference: ObjectReferenceModel = Field(alias="SourceObjectReference")
    target_object_reference: ObjectReferenceModel = Field(alias="TargetObjectReference")
    typed_link_facet: TypedLinkSchemaAndFacetNameModel = Field(alias="TypedLinkFacet")
    attributes: Sequence[AttributeNameAndValueModel] = Field(alias="Attributes")


class BatchAttachTypedLinkModel(BaseModel):
    source_object_reference: ObjectReferenceModel = Field(alias="SourceObjectReference")
    target_object_reference: ObjectReferenceModel = Field(alias="TargetObjectReference")
    typed_link_facet: TypedLinkSchemaAndFacetNameModel = Field(alias="TypedLinkFacet")
    attributes: Sequence[AttributeNameAndValueModel] = Field(alias="Attributes")


class TypedLinkSpecifierModel(BaseModel):
    typed_link_facet: TypedLinkSchemaAndFacetNameModel = Field(alias="TypedLinkFacet")
    source_object_reference: ObjectReferenceModel = Field(alias="SourceObjectReference")
    target_object_reference: ObjectReferenceModel = Field(alias="TargetObjectReference")
    identity_attribute_values: List[AttributeNameAndValueModel] = Field(
        alias="IdentityAttributeValues"
    )


class LinkAttributeUpdateModel(BaseModel):
    attribute_key: Optional[AttributeKeyModel] = Field(
        default=None, alias="AttributeKey"
    )
    attribute_action: Optional[LinkAttributeActionModel] = Field(
        default=None, alias="AttributeAction"
    )


class ObjectAttributeUpdateModel(BaseModel):
    object_attribute_key: Optional[AttributeKeyModel] = Field(
        default=None, alias="ObjectAttributeKey"
    )
    object_attribute_action: Optional[ObjectAttributeActionModel] = Field(
        default=None, alias="ObjectAttributeAction"
    )


class ObjectAttributeRangeModel(BaseModel):
    attribute_key: Optional[AttributeKeyModel] = Field(
        default=None, alias="AttributeKey"
    )
    range: Optional[TypedAttributeValueRangeModel] = Field(default=None, alias="Range")


class TypedLinkAttributeRangeModel(BaseModel):
    range: TypedAttributeValueRangeModel = Field(alias="Range")
    attribute_name: Optional[str] = Field(default=None, alias="AttributeName")


class FacetAttributeModel(BaseModel):
    name: str = Field(alias="Name")
    attribute_definition: Optional[FacetAttributeDefinitionModel] = Field(
        default=None, alias="AttributeDefinition"
    )
    attribute_reference: Optional[FacetAttributeReferenceModel] = Field(
        default=None, alias="AttributeReference"
    )
    required_behavior: Optional[Literal["NOT_REQUIRED", "REQUIRED_ALWAYS"]] = Field(
        default=None, alias="RequiredBehavior"
    )


class ListTypedLinkFacetAttributesResponseModel(BaseModel):
    attributes: List[TypedLinkAttributeDefinitionModel] = Field(alias="Attributes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TypedLinkFacetAttributeUpdateModel(BaseModel):
    attribute: TypedLinkAttributeDefinitionModel = Field(alias="Attribute")
    action: Literal["CREATE_OR_UPDATE", "DELETE"] = Field(alias="Action")


class TypedLinkFacetModel(BaseModel):
    name: str = Field(alias="Name")
    attributes: Sequence[TypedLinkAttributeDefinitionModel] = Field(alias="Attributes")
    identity_attribute_order: Sequence[str] = Field(alias="IdentityAttributeOrder")


class BatchLookupPolicyResponseModel(BaseModel):
    policy_to_path_list: Optional[List[PolicyToPathModel]] = Field(
        default=None, alias="PolicyToPathList"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class LookupPolicyResponseModel(BaseModel):
    policy_to_path_list: List[PolicyToPathModel] = Field(alias="PolicyToPathList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchListAttachedIndicesResponseModel(BaseModel):
    index_attachments: Optional[List[IndexAttachmentModel]] = Field(
        default=None, alias="IndexAttachments"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class BatchListIndexResponseModel(BaseModel):
    index_attachments: Optional[List[IndexAttachmentModel]] = Field(
        default=None, alias="IndexAttachments"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListAttachedIndicesResponseModel(BaseModel):
    index_attachments: List[IndexAttachmentModel] = Field(alias="IndexAttachments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIndexResponseModel(BaseModel):
    index_attachments: List[IndexAttachmentModel] = Field(alias="IndexAttachments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AttachTypedLinkResponseModel(BaseModel):
    typed_link_specifier: TypedLinkSpecifierModel = Field(alias="TypedLinkSpecifier")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchAttachTypedLinkResponseModel(BaseModel):
    typed_link_specifier: Optional[TypedLinkSpecifierModel] = Field(
        default=None, alias="TypedLinkSpecifier"
    )


class BatchDetachTypedLinkModel(BaseModel):
    typed_link_specifier: TypedLinkSpecifierModel = Field(alias="TypedLinkSpecifier")


class BatchGetLinkAttributesModel(BaseModel):
    typed_link_specifier: TypedLinkSpecifierModel = Field(alias="TypedLinkSpecifier")
    attribute_names: Sequence[str] = Field(alias="AttributeNames")


class BatchListIncomingTypedLinksResponseModel(BaseModel):
    link_specifiers: Optional[List[TypedLinkSpecifierModel]] = Field(
        default=None, alias="LinkSpecifiers"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class BatchListOutgoingTypedLinksResponseModel(BaseModel):
    typed_link_specifiers: Optional[List[TypedLinkSpecifierModel]] = Field(
        default=None, alias="TypedLinkSpecifiers"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DetachTypedLinkRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    typed_link_specifier: TypedLinkSpecifierModel = Field(alias="TypedLinkSpecifier")


class GetLinkAttributesRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    typed_link_specifier: TypedLinkSpecifierModel = Field(alias="TypedLinkSpecifier")
    attribute_names: Sequence[str] = Field(alias="AttributeNames")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class ListIncomingTypedLinksResponseModel(BaseModel):
    link_specifiers: List[TypedLinkSpecifierModel] = Field(alias="LinkSpecifiers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListOutgoingTypedLinksResponseModel(BaseModel):
    typed_link_specifiers: List[TypedLinkSpecifierModel] = Field(
        alias="TypedLinkSpecifiers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchUpdateLinkAttributesModel(BaseModel):
    typed_link_specifier: TypedLinkSpecifierModel = Field(alias="TypedLinkSpecifier")
    attribute_updates: Sequence[LinkAttributeUpdateModel] = Field(
        alias="AttributeUpdates"
    )


class UpdateLinkAttributesRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    typed_link_specifier: TypedLinkSpecifierModel = Field(alias="TypedLinkSpecifier")
    attribute_updates: Sequence[LinkAttributeUpdateModel] = Field(
        alias="AttributeUpdates"
    )


class BatchUpdateObjectAttributesModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    attribute_updates: Sequence[ObjectAttributeUpdateModel] = Field(
        alias="AttributeUpdates"
    )


class UpdateObjectAttributesRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    attribute_updates: Sequence[ObjectAttributeUpdateModel] = Field(
        alias="AttributeUpdates"
    )


class BatchListIndexModel(BaseModel):
    index_reference: ObjectReferenceModel = Field(alias="IndexReference")
    ranges_on_indexed_values: Optional[Sequence[ObjectAttributeRangeModel]] = Field(
        default=None, alias="RangesOnIndexedValues"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListIndexRequestListIndexPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    index_reference: ObjectReferenceModel = Field(alias="IndexReference")
    ranges_on_indexed_values: Optional[Sequence[ObjectAttributeRangeModel]] = Field(
        default=None, alias="RangesOnIndexedValues"
    )
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIndexRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    index_reference: ObjectReferenceModel = Field(alias="IndexReference")
    ranges_on_indexed_values: Optional[Sequence[ObjectAttributeRangeModel]] = Field(
        default=None, alias="RangesOnIndexedValues"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class BatchListIncomingTypedLinksModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    filter_attribute_ranges: Optional[Sequence[TypedLinkAttributeRangeModel]] = Field(
        default=None, alias="FilterAttributeRanges"
    )
    filter_typed_link: Optional[TypedLinkSchemaAndFacetNameModel] = Field(
        default=None, alias="FilterTypedLink"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class BatchListOutgoingTypedLinksModel(BaseModel):
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    filter_attribute_ranges: Optional[Sequence[TypedLinkAttributeRangeModel]] = Field(
        default=None, alias="FilterAttributeRanges"
    )
    filter_typed_link: Optional[TypedLinkSchemaAndFacetNameModel] = Field(
        default=None, alias="FilterTypedLink"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    filter_attribute_ranges: Optional[Sequence[TypedLinkAttributeRangeModel]] = Field(
        default=None, alias="FilterAttributeRanges"
    )
    filter_typed_link: Optional[TypedLinkSchemaAndFacetNameModel] = Field(
        default=None, alias="FilterTypedLink"
    )
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIncomingTypedLinksRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    filter_attribute_ranges: Optional[Sequence[TypedLinkAttributeRangeModel]] = Field(
        default=None, alias="FilterAttributeRanges"
    )
    filter_typed_link: Optional[TypedLinkSchemaAndFacetNameModel] = Field(
        default=None, alias="FilterTypedLink"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    filter_attribute_ranges: Optional[Sequence[TypedLinkAttributeRangeModel]] = Field(
        default=None, alias="FilterAttributeRanges"
    )
    filter_typed_link: Optional[TypedLinkSchemaAndFacetNameModel] = Field(
        default=None, alias="FilterTypedLink"
    )
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListOutgoingTypedLinksRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    object_reference: ObjectReferenceModel = Field(alias="ObjectReference")
    filter_attribute_ranges: Optional[Sequence[TypedLinkAttributeRangeModel]] = Field(
        default=None, alias="FilterAttributeRanges"
    )
    filter_typed_link: Optional[TypedLinkSchemaAndFacetNameModel] = Field(
        default=None, alias="FilterTypedLink"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class CreateFacetRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")
    attributes: Optional[Sequence[FacetAttributeModel]] = Field(
        default=None, alias="Attributes"
    )
    object_type: Optional[Literal["INDEX", "LEAF_NODE", "NODE", "POLICY"]] = Field(
        default=None, alias="ObjectType"
    )
    facet_style: Optional[Literal["DYNAMIC", "STATIC"]] = Field(
        default=None, alias="FacetStyle"
    )


class FacetAttributeUpdateModel(BaseModel):
    attribute: Optional[FacetAttributeModel] = Field(default=None, alias="Attribute")
    action: Optional[Literal["CREATE_OR_UPDATE", "DELETE"]] = Field(
        default=None, alias="Action"
    )


class ListFacetAttributesResponseModel(BaseModel):
    attributes: List[FacetAttributeModel] = Field(alias="Attributes")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTypedLinkFacetRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")
    attribute_updates: Sequence[TypedLinkFacetAttributeUpdateModel] = Field(
        alias="AttributeUpdates"
    )
    identity_attribute_order: Sequence[str] = Field(alias="IdentityAttributeOrder")


class CreateTypedLinkFacetRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    facet: TypedLinkFacetModel = Field(alias="Facet")


class BatchWriteOperationResponseModel(BaseModel):
    create_object: Optional[BatchCreateObjectResponseModel] = Field(
        default=None, alias="CreateObject"
    )
    attach_object: Optional[BatchAttachObjectResponseModel] = Field(
        default=None, alias="AttachObject"
    )
    detach_object: Optional[BatchDetachObjectResponseModel] = Field(
        default=None, alias="DetachObject"
    )
    update_object_attributes: Optional[
        BatchUpdateObjectAttributesResponseModel
    ] = Field(default=None, alias="UpdateObjectAttributes")
    delete_object: Optional[Dict[str, Any]] = Field(default=None, alias="DeleteObject")
    add_facet_to_object: Optional[Dict[str, Any]] = Field(
        default=None, alias="AddFacetToObject"
    )
    remove_facet_from_object: Optional[Dict[str, Any]] = Field(
        default=None, alias="RemoveFacetFromObject"
    )
    attach_policy: Optional[Dict[str, Any]] = Field(default=None, alias="AttachPolicy")
    detach_policy: Optional[Dict[str, Any]] = Field(default=None, alias="DetachPolicy")
    create_index: Optional[BatchCreateIndexResponseModel] = Field(
        default=None, alias="CreateIndex"
    )
    attach_to_index: Optional[BatchAttachToIndexResponseModel] = Field(
        default=None, alias="AttachToIndex"
    )
    detach_from_index: Optional[BatchDetachFromIndexResponseModel] = Field(
        default=None, alias="DetachFromIndex"
    )
    attach_typed_link: Optional[BatchAttachTypedLinkResponseModel] = Field(
        default=None, alias="AttachTypedLink"
    )
    detach_typed_link: Optional[Dict[str, Any]] = Field(
        default=None, alias="DetachTypedLink"
    )
    update_link_attributes: Optional[Dict[str, Any]] = Field(
        default=None, alias="UpdateLinkAttributes"
    )


class BatchReadSuccessfulResponseModel(BaseModel):
    list_object_attributes: Optional[BatchListObjectAttributesResponseModel] = Field(
        default=None, alias="ListObjectAttributes"
    )
    list_object_children: Optional[BatchListObjectChildrenResponseModel] = Field(
        default=None, alias="ListObjectChildren"
    )
    get_object_information: Optional[BatchGetObjectInformationResponseModel] = Field(
        default=None, alias="GetObjectInformation"
    )
    get_object_attributes: Optional[BatchGetObjectAttributesResponseModel] = Field(
        default=None, alias="GetObjectAttributes"
    )
    list_attached_indices: Optional[BatchListAttachedIndicesResponseModel] = Field(
        default=None, alias="ListAttachedIndices"
    )
    list_object_parent_paths: Optional[BatchListObjectParentPathsResponseModel] = Field(
        default=None, alias="ListObjectParentPaths"
    )
    list_object_policies: Optional[BatchListObjectPoliciesResponseModel] = Field(
        default=None, alias="ListObjectPolicies"
    )
    list_policy_attachments: Optional[BatchListPolicyAttachmentsResponseModel] = Field(
        default=None, alias="ListPolicyAttachments"
    )
    lookup_policy: Optional[BatchLookupPolicyResponseModel] = Field(
        default=None, alias="LookupPolicy"
    )
    list_index: Optional[BatchListIndexResponseModel] = Field(
        default=None, alias="ListIndex"
    )
    list_outgoing_typed_links: Optional[
        BatchListOutgoingTypedLinksResponseModel
    ] = Field(default=None, alias="ListOutgoingTypedLinks")
    list_incoming_typed_links: Optional[
        BatchListIncomingTypedLinksResponseModel
    ] = Field(default=None, alias="ListIncomingTypedLinks")
    get_link_attributes: Optional[BatchGetLinkAttributesResponseModel] = Field(
        default=None, alias="GetLinkAttributes"
    )
    list_object_parents: Optional[BatchListObjectParentsResponseModel] = Field(
        default=None, alias="ListObjectParents"
    )


class BatchWriteOperationModel(BaseModel):
    create_object: Optional[BatchCreateObjectModel] = Field(
        default=None, alias="CreateObject"
    )
    attach_object: Optional[BatchAttachObjectModel] = Field(
        default=None, alias="AttachObject"
    )
    detach_object: Optional[BatchDetachObjectModel] = Field(
        default=None, alias="DetachObject"
    )
    update_object_attributes: Optional[BatchUpdateObjectAttributesModel] = Field(
        default=None, alias="UpdateObjectAttributes"
    )
    delete_object: Optional[BatchDeleteObjectModel] = Field(
        default=None, alias="DeleteObject"
    )
    add_facet_to_object: Optional[BatchAddFacetToObjectModel] = Field(
        default=None, alias="AddFacetToObject"
    )
    remove_facet_from_object: Optional[BatchRemoveFacetFromObjectModel] = Field(
        default=None, alias="RemoveFacetFromObject"
    )
    attach_policy: Optional[BatchAttachPolicyModel] = Field(
        default=None, alias="AttachPolicy"
    )
    detach_policy: Optional[BatchDetachPolicyModel] = Field(
        default=None, alias="DetachPolicy"
    )
    create_index: Optional[BatchCreateIndexModel] = Field(
        default=None, alias="CreateIndex"
    )
    attach_to_index: Optional[BatchAttachToIndexModel] = Field(
        default=None, alias="AttachToIndex"
    )
    detach_from_index: Optional[BatchDetachFromIndexModel] = Field(
        default=None, alias="DetachFromIndex"
    )
    attach_typed_link: Optional[BatchAttachTypedLinkModel] = Field(
        default=None, alias="AttachTypedLink"
    )
    detach_typed_link: Optional[BatchDetachTypedLinkModel] = Field(
        default=None, alias="DetachTypedLink"
    )
    update_link_attributes: Optional[BatchUpdateLinkAttributesModel] = Field(
        default=None, alias="UpdateLinkAttributes"
    )


class BatchReadOperationModel(BaseModel):
    list_object_attributes: Optional[BatchListObjectAttributesModel] = Field(
        default=None, alias="ListObjectAttributes"
    )
    list_object_children: Optional[BatchListObjectChildrenModel] = Field(
        default=None, alias="ListObjectChildren"
    )
    list_attached_indices: Optional[BatchListAttachedIndicesModel] = Field(
        default=None, alias="ListAttachedIndices"
    )
    list_object_parent_paths: Optional[BatchListObjectParentPathsModel] = Field(
        default=None, alias="ListObjectParentPaths"
    )
    get_object_information: Optional[BatchGetObjectInformationModel] = Field(
        default=None, alias="GetObjectInformation"
    )
    get_object_attributes: Optional[BatchGetObjectAttributesModel] = Field(
        default=None, alias="GetObjectAttributes"
    )
    list_object_parents: Optional[BatchListObjectParentsModel] = Field(
        default=None, alias="ListObjectParents"
    )
    list_object_policies: Optional[BatchListObjectPoliciesModel] = Field(
        default=None, alias="ListObjectPolicies"
    )
    list_policy_attachments: Optional[BatchListPolicyAttachmentsModel] = Field(
        default=None, alias="ListPolicyAttachments"
    )
    lookup_policy: Optional[BatchLookupPolicyModel] = Field(
        default=None, alias="LookupPolicy"
    )
    list_index: Optional[BatchListIndexModel] = Field(default=None, alias="ListIndex")
    list_outgoing_typed_links: Optional[BatchListOutgoingTypedLinksModel] = Field(
        default=None, alias="ListOutgoingTypedLinks"
    )
    list_incoming_typed_links: Optional[BatchListIncomingTypedLinksModel] = Field(
        default=None, alias="ListIncomingTypedLinks"
    )
    get_link_attributes: Optional[BatchGetLinkAttributesModel] = Field(
        default=None, alias="GetLinkAttributes"
    )


class UpdateFacetRequestModel(BaseModel):
    schema_arn: str = Field(alias="SchemaArn")
    name: str = Field(alias="Name")
    attribute_updates: Optional[Sequence[FacetAttributeUpdateModel]] = Field(
        default=None, alias="AttributeUpdates"
    )
    object_type: Optional[Literal["INDEX", "LEAF_NODE", "NODE", "POLICY"]] = Field(
        default=None, alias="ObjectType"
    )


class BatchWriteResponseModel(BaseModel):
    responses: List[BatchWriteOperationResponseModel] = Field(alias="Responses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchReadOperationResponseModel(BaseModel):
    successful_response: Optional[BatchReadSuccessfulResponseModel] = Field(
        default=None, alias="SuccessfulResponse"
    )
    exception_response: Optional[BatchReadExceptionModel] = Field(
        default=None, alias="ExceptionResponse"
    )


class BatchWriteRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    operations: Sequence[BatchWriteOperationModel] = Field(alias="Operations")


class BatchReadRequestModel(BaseModel):
    directory_arn: str = Field(alias="DirectoryArn")
    operations: Sequence[BatchReadOperationModel] = Field(alias="Operations")
    consistency_level: Optional[Literal["EVENTUAL", "SERIALIZABLE"]] = Field(
        default=None, alias="ConsistencyLevel"
    )


class BatchReadResponseModel(BaseModel):
    responses: List[BatchReadOperationResponseModel] = Field(alias="Responses")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
