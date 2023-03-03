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


class AliasListEntryModel(BaseModel):
    alias_name: Optional[str] = Field(default=None, alias="AliasName")
    alias_arn: Optional[str] = Field(default=None, alias="AliasArn")
    target_key_id: Optional[str] = Field(default=None, alias="TargetKeyId")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    last_updated_date: Optional[datetime] = Field(default=None, alias="LastUpdatedDate")


class CancelKeyDeletionRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ConnectCustomKeyStoreRequestModel(BaseModel):
    custom_key_store_id: str = Field(alias="CustomKeyStoreId")


class CreateAliasRequestModel(BaseModel):
    alias_name: str = Field(alias="AliasName")
    target_key_id: str = Field(alias="TargetKeyId")


class XksProxyAuthenticationCredentialTypeModel(BaseModel):
    access_key_id: str = Field(alias="AccessKeyId")
    raw_secret_access_key: str = Field(alias="RawSecretAccessKey")


class GrantConstraintsModel(BaseModel):
    encryption_context_subset: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContextSubset"
    )
    encryption_context_equals: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContextEquals"
    )


class TagModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    tag_value: str = Field(alias="TagValue")


class XksProxyConfigurationTypeModel(BaseModel):
    connectivity: Optional[Literal["PUBLIC_ENDPOINT", "VPC_ENDPOINT_SERVICE"]] = Field(
        default=None, alias="Connectivity"
    )
    access_key_id: Optional[str] = Field(default=None, alias="AccessKeyId")
    uri_endpoint: Optional[str] = Field(default=None, alias="UriEndpoint")
    uri_path: Optional[str] = Field(default=None, alias="UriPath")
    vpc_endpoint_service_name: Optional[str] = Field(
        default=None, alias="VpcEndpointServiceName"
    )


class DecryptRequestModel(BaseModel):
    ciphertext_blob: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="CiphertextBlob"
    )
    encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContext"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    encryption_algorithm: Optional[
        Literal["RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"]
    ] = Field(default=None, alias="EncryptionAlgorithm")


class DeleteAliasRequestModel(BaseModel):
    alias_name: str = Field(alias="AliasName")


class DeleteCustomKeyStoreRequestModel(BaseModel):
    custom_key_store_id: str = Field(alias="CustomKeyStoreId")


class DeleteImportedKeyMaterialRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeCustomKeyStoresRequestModel(BaseModel):
    custom_key_store_id: Optional[str] = Field(default=None, alias="CustomKeyStoreId")
    custom_key_store_name: Optional[str] = Field(
        default=None, alias="CustomKeyStoreName"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class DescribeKeyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class DisableKeyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class DisableKeyRotationRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class DisconnectCustomKeyStoreRequestModel(BaseModel):
    custom_key_store_id: str = Field(alias="CustomKeyStoreId")


class EnableKeyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class EnableKeyRotationRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class EncryptRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    plaintext: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Plaintext"
    )
    encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContext"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")
    encryption_algorithm: Optional[
        Literal["RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"]
    ] = Field(default=None, alias="EncryptionAlgorithm")


class GenerateDataKeyPairRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    key_pair_spec: Literal[
        "ECC_NIST_P256",
        "ECC_NIST_P384",
        "ECC_NIST_P521",
        "ECC_SECG_P256K1",
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "SM2",
    ] = Field(alias="KeyPairSpec")
    encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContext"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class GenerateDataKeyPairWithoutPlaintextRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    key_pair_spec: Literal[
        "ECC_NIST_P256",
        "ECC_NIST_P384",
        "ECC_NIST_P521",
        "ECC_SECG_P256K1",
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "SM2",
    ] = Field(alias="KeyPairSpec")
    encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContext"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class GenerateDataKeyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContext"
    )
    number_of_bytes: Optional[int] = Field(default=None, alias="NumberOfBytes")
    key_spec: Optional[Literal["AES_128", "AES_256"]] = Field(
        default=None, alias="KeySpec"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class GenerateDataKeyWithoutPlaintextRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="EncryptionContext"
    )
    key_spec: Optional[Literal["AES_128", "AES_256"]] = Field(
        default=None, alias="KeySpec"
    )
    number_of_bytes: Optional[int] = Field(default=None, alias="NumberOfBytes")
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class GenerateMacRequestModel(BaseModel):
    message: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Message"
    )
    key_id: str = Field(alias="KeyId")
    mac_algorithm: Literal[
        "HMAC_SHA_224", "HMAC_SHA_256", "HMAC_SHA_384", "HMAC_SHA_512"
    ] = Field(alias="MacAlgorithm")
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class GenerateRandomRequestModel(BaseModel):
    number_of_bytes: Optional[int] = Field(default=None, alias="NumberOfBytes")
    custom_key_store_id: Optional[str] = Field(default=None, alias="CustomKeyStoreId")


class GetKeyPolicyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    policy_name: str = Field(alias="PolicyName")


class GetKeyRotationStatusRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")


class GetParametersForImportRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    wrapping_algorithm: Literal[
        "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "RSAES_PKCS1_V1_5"
    ] = Field(alias="WrappingAlgorithm")
    wrapping_key_spec: Literal["RSA_2048"] = Field(alias="WrappingKeySpec")


class GetPublicKeyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class ImportKeyMaterialRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    import_token: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="ImportToken"
    )
    encrypted_key_material: Union[
        str, bytes, Type[IO[Any]], Type[StreamingBody]
    ] = Field(alias="EncryptedKeyMaterial")
    valid_to: Optional[Union[datetime, str]] = Field(default=None, alias="ValidTo")
    expiration_model: Optional[
        Literal["KEY_MATERIAL_DOES_NOT_EXPIRE", "KEY_MATERIAL_EXPIRES"]
    ] = Field(default=None, alias="ExpirationModel")


class KeyListEntryModel(BaseModel):
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    key_arn: Optional[str] = Field(default=None, alias="KeyArn")


class XksKeyConfigurationTypeModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="Id")


class ListAliasesRequestModel(BaseModel):
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListGrantsRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")
    grant_id: Optional[str] = Field(default=None, alias="GrantId")
    grantee_principal: Optional[str] = Field(default=None, alias="GranteePrincipal")


class ListKeyPoliciesRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListKeysRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListResourceTagsRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class ListRetirableGrantsRequestModel(BaseModel):
    retiring_principal: str = Field(alias="RetiringPrincipal")
    limit: Optional[int] = Field(default=None, alias="Limit")
    marker: Optional[str] = Field(default=None, alias="Marker")


class MultiRegionKeyModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    region: Optional[str] = Field(default=None, alias="Region")


class PutKeyPolicyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    policy_name: str = Field(alias="PolicyName")
    policy: str = Field(alias="Policy")
    bypass_policy_lockout_safety_check: Optional[bool] = Field(
        default=None, alias="BypassPolicyLockoutSafetyCheck"
    )


class ReEncryptRequestModel(BaseModel):
    ciphertext_blob: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="CiphertextBlob"
    )
    destination_key_id: str = Field(alias="DestinationKeyId")
    source_encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="SourceEncryptionContext"
    )
    source_key_id: Optional[str] = Field(default=None, alias="SourceKeyId")
    destination_encryption_context: Optional[Mapping[str, str]] = Field(
        default=None, alias="DestinationEncryptionContext"
    )
    source_encryption_algorithm: Optional[
        Literal["RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"]
    ] = Field(default=None, alias="SourceEncryptionAlgorithm")
    destination_encryption_algorithm: Optional[
        Literal["RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"]
    ] = Field(default=None, alias="DestinationEncryptionAlgorithm")
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class RetireGrantRequestModel(BaseModel):
    grant_token: Optional[str] = Field(default=None, alias="GrantToken")
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    grant_id: Optional[str] = Field(default=None, alias="GrantId")


class RevokeGrantRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    grant_id: str = Field(alias="GrantId")


class ScheduleKeyDeletionRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    pending_window_in_days: Optional[int] = Field(
        default=None, alias="PendingWindowInDays"
    )


class SignRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    message: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Message"
    )
    signing_algorithm: Literal[
        "ECDSA_SHA_256",
        "ECDSA_SHA_384",
        "ECDSA_SHA_512",
        "RSASSA_PKCS1_V1_5_SHA_256",
        "RSASSA_PKCS1_V1_5_SHA_384",
        "RSASSA_PKCS1_V1_5_SHA_512",
        "RSASSA_PSS_SHA_256",
        "RSASSA_PSS_SHA_384",
        "RSASSA_PSS_SHA_512",
        "SM2DSA",
    ] = Field(alias="SigningAlgorithm")
    message_type: Optional[Literal["DIGEST", "RAW"]] = Field(
        default=None, alias="MessageType"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class UntagResourceRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAliasRequestModel(BaseModel):
    alias_name: str = Field(alias="AliasName")
    target_key_id: str = Field(alias="TargetKeyId")


class UpdateKeyDescriptionRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    description: str = Field(alias="Description")


class UpdatePrimaryRegionRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    primary_region: str = Field(alias="PrimaryRegion")


class VerifyMacRequestModel(BaseModel):
    message: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Message"
    )
    key_id: str = Field(alias="KeyId")
    mac_algorithm: Literal[
        "HMAC_SHA_224", "HMAC_SHA_256", "HMAC_SHA_384", "HMAC_SHA_512"
    ] = Field(alias="MacAlgorithm")
    mac: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(alias="Mac")
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class VerifyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    message: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Message"
    )
    signature: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="Signature"
    )
    signing_algorithm: Literal[
        "ECDSA_SHA_256",
        "ECDSA_SHA_384",
        "ECDSA_SHA_512",
        "RSASSA_PKCS1_V1_5_SHA_256",
        "RSASSA_PKCS1_V1_5_SHA_384",
        "RSASSA_PKCS1_V1_5_SHA_512",
        "RSASSA_PSS_SHA_256",
        "RSASSA_PSS_SHA_384",
        "RSASSA_PSS_SHA_512",
        "SM2DSA",
    ] = Field(alias="SigningAlgorithm")
    message_type: Optional[Literal["DIGEST", "RAW"]] = Field(
        default=None, alias="MessageType"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")


class CancelKeyDeletionResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomKeyStoreResponseModel(BaseModel):
    custom_key_store_id: str = Field(alias="CustomKeyStoreId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGrantResponseModel(BaseModel):
    grant_token: str = Field(alias="GrantToken")
    grant_id: str = Field(alias="GrantId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DecryptResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    plaintext: bytes = Field(alias="Plaintext")
    encryption_algorithm: Literal[
        "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"
    ] = Field(alias="EncryptionAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EncryptResponseModel(BaseModel):
    ciphertext_blob: bytes = Field(alias="CiphertextBlob")
    key_id: str = Field(alias="KeyId")
    encryption_algorithm: Literal[
        "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"
    ] = Field(alias="EncryptionAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateDataKeyPairResponseModel(BaseModel):
    private_key_ciphertext_blob: bytes = Field(alias="PrivateKeyCiphertextBlob")
    private_key_plaintext: bytes = Field(alias="PrivateKeyPlaintext")
    public_key: bytes = Field(alias="PublicKey")
    key_id: str = Field(alias="KeyId")
    key_pair_spec: Literal[
        "ECC_NIST_P256",
        "ECC_NIST_P384",
        "ECC_NIST_P521",
        "ECC_SECG_P256K1",
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "SM2",
    ] = Field(alias="KeyPairSpec")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateDataKeyPairWithoutPlaintextResponseModel(BaseModel):
    private_key_ciphertext_blob: bytes = Field(alias="PrivateKeyCiphertextBlob")
    public_key: bytes = Field(alias="PublicKey")
    key_id: str = Field(alias="KeyId")
    key_pair_spec: Literal[
        "ECC_NIST_P256",
        "ECC_NIST_P384",
        "ECC_NIST_P521",
        "ECC_SECG_P256K1",
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "SM2",
    ] = Field(alias="KeyPairSpec")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateDataKeyResponseModel(BaseModel):
    ciphertext_blob: bytes = Field(alias="CiphertextBlob")
    plaintext: bytes = Field(alias="Plaintext")
    key_id: str = Field(alias="KeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateDataKeyWithoutPlaintextResponseModel(BaseModel):
    ciphertext_blob: bytes = Field(alias="CiphertextBlob")
    key_id: str = Field(alias="KeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateMacResponseModel(BaseModel):
    mac: bytes = Field(alias="Mac")
    mac_algorithm: Literal[
        "HMAC_SHA_224", "HMAC_SHA_256", "HMAC_SHA_384", "HMAC_SHA_512"
    ] = Field(alias="MacAlgorithm")
    key_id: str = Field(alias="KeyId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateRandomResponseModel(BaseModel):
    plaintext: bytes = Field(alias="Plaintext")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetKeyPolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetKeyRotationStatusResponseModel(BaseModel):
    key_rotation_enabled: bool = Field(alias="KeyRotationEnabled")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetParametersForImportResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    import_token: bytes = Field(alias="ImportToken")
    public_key: bytes = Field(alias="PublicKey")
    parameters_valid_to: datetime = Field(alias="ParametersValidTo")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPublicKeyResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    public_key: bytes = Field(alias="PublicKey")
    customer_master_key_spec: Literal[
        "ECC_NIST_P256",
        "ECC_NIST_P384",
        "ECC_NIST_P521",
        "ECC_SECG_P256K1",
        "HMAC_224",
        "HMAC_256",
        "HMAC_384",
        "HMAC_512",
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "SM2",
        "SYMMETRIC_DEFAULT",
    ] = Field(alias="CustomerMasterKeySpec")
    key_spec: Literal[
        "ECC_NIST_P256",
        "ECC_NIST_P384",
        "ECC_NIST_P521",
        "ECC_SECG_P256K1",
        "HMAC_224",
        "HMAC_256",
        "HMAC_384",
        "HMAC_512",
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "SM2",
        "SYMMETRIC_DEFAULT",
    ] = Field(alias="KeySpec")
    key_usage: Literal["ENCRYPT_DECRYPT", "GENERATE_VERIFY_MAC", "SIGN_VERIFY"] = Field(
        alias="KeyUsage"
    )
    encryption_algorithms: List[
        Literal["RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"]
    ] = Field(alias="EncryptionAlgorithms")
    signing_algorithms: List[
        Literal[
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "SM2DSA",
        ]
    ] = Field(alias="SigningAlgorithms")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAliasesResponseModel(BaseModel):
    aliases: List[AliasListEntryModel] = Field(alias="Aliases")
    next_marker: str = Field(alias="NextMarker")
    truncated: bool = Field(alias="Truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListKeyPoliciesResponseModel(BaseModel):
    policy_names: List[str] = Field(alias="PolicyNames")
    next_marker: str = Field(alias="NextMarker")
    truncated: bool = Field(alias="Truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReEncryptResponseModel(BaseModel):
    ciphertext_blob: bytes = Field(alias="CiphertextBlob")
    source_key_id: str = Field(alias="SourceKeyId")
    key_id: str = Field(alias="KeyId")
    source_encryption_algorithm: Literal[
        "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"
    ] = Field(alias="SourceEncryptionAlgorithm")
    destination_encryption_algorithm: Literal[
        "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"
    ] = Field(alias="DestinationEncryptionAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ScheduleKeyDeletionResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    deletion_date: datetime = Field(alias="DeletionDate")
    key_state: Literal[
        "Creating",
        "Disabled",
        "Enabled",
        "PendingDeletion",
        "PendingImport",
        "PendingReplicaDeletion",
        "Unavailable",
        "Updating",
    ] = Field(alias="KeyState")
    pending_window_in_days: int = Field(alias="PendingWindowInDays")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SignResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    signature: bytes = Field(alias="Signature")
    signing_algorithm: Literal[
        "ECDSA_SHA_256",
        "ECDSA_SHA_384",
        "ECDSA_SHA_512",
        "RSASSA_PKCS1_V1_5_SHA_256",
        "RSASSA_PKCS1_V1_5_SHA_384",
        "RSASSA_PKCS1_V1_5_SHA_512",
        "RSASSA_PSS_SHA_256",
        "RSASSA_PSS_SHA_384",
        "RSASSA_PSS_SHA_512",
        "SM2DSA",
    ] = Field(alias="SigningAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifyMacResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    mac_valid: bool = Field(alias="MacValid")
    mac_algorithm: Literal[
        "HMAC_SHA_224", "HMAC_SHA_256", "HMAC_SHA_384", "HMAC_SHA_512"
    ] = Field(alias="MacAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VerifyResponseModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    signature_valid: bool = Field(alias="SignatureValid")
    signing_algorithm: Literal[
        "ECDSA_SHA_256",
        "ECDSA_SHA_384",
        "ECDSA_SHA_512",
        "RSASSA_PKCS1_V1_5_SHA_256",
        "RSASSA_PKCS1_V1_5_SHA_384",
        "RSASSA_PKCS1_V1_5_SHA_512",
        "RSASSA_PSS_SHA_256",
        "RSASSA_PSS_SHA_384",
        "RSASSA_PSS_SHA_512",
        "SM2DSA",
    ] = Field(alias="SigningAlgorithm")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCustomKeyStoreRequestModel(BaseModel):
    custom_key_store_name: str = Field(alias="CustomKeyStoreName")
    cloud_hsm_cluster_id: Optional[str] = Field(default=None, alias="CloudHsmClusterId")
    trust_anchor_certificate: Optional[str] = Field(
        default=None, alias="TrustAnchorCertificate"
    )
    key_store_password: Optional[str] = Field(default=None, alias="KeyStorePassword")
    custom_key_store_type: Optional[
        Literal["AWS_CLOUDHSM", "EXTERNAL_KEY_STORE"]
    ] = Field(default=None, alias="CustomKeyStoreType")
    xks_proxy_uri_endpoint: Optional[str] = Field(
        default=None, alias="XksProxyUriEndpoint"
    )
    xks_proxy_uri_path: Optional[str] = Field(default=None, alias="XksProxyUriPath")
    xks_proxy_vpc_endpoint_service_name: Optional[str] = Field(
        default=None, alias="XksProxyVpcEndpointServiceName"
    )
    xks_proxy_authentication_credential: Optional[
        XksProxyAuthenticationCredentialTypeModel
    ] = Field(default=None, alias="XksProxyAuthenticationCredential")
    xks_proxy_connectivity: Optional[
        Literal["PUBLIC_ENDPOINT", "VPC_ENDPOINT_SERVICE"]
    ] = Field(default=None, alias="XksProxyConnectivity")


class UpdateCustomKeyStoreRequestModel(BaseModel):
    custom_key_store_id: str = Field(alias="CustomKeyStoreId")
    new_custom_key_store_name: Optional[str] = Field(
        default=None, alias="NewCustomKeyStoreName"
    )
    key_store_password: Optional[str] = Field(default=None, alias="KeyStorePassword")
    cloud_hsm_cluster_id: Optional[str] = Field(default=None, alias="CloudHsmClusterId")
    xks_proxy_uri_endpoint: Optional[str] = Field(
        default=None, alias="XksProxyUriEndpoint"
    )
    xks_proxy_uri_path: Optional[str] = Field(default=None, alias="XksProxyUriPath")
    xks_proxy_vpc_endpoint_service_name: Optional[str] = Field(
        default=None, alias="XksProxyVpcEndpointServiceName"
    )
    xks_proxy_authentication_credential: Optional[
        XksProxyAuthenticationCredentialTypeModel
    ] = Field(default=None, alias="XksProxyAuthenticationCredential")
    xks_proxy_connectivity: Optional[
        Literal["PUBLIC_ENDPOINT", "VPC_ENDPOINT_SERVICE"]
    ] = Field(default=None, alias="XksProxyConnectivity")


class CreateGrantRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    grantee_principal: str = Field(alias="GranteePrincipal")
    operations: Sequence[
        Literal[
            "CreateGrant",
            "Decrypt",
            "DescribeKey",
            "Encrypt",
            "GenerateDataKey",
            "GenerateDataKeyPair",
            "GenerateDataKeyPairWithoutPlaintext",
            "GenerateDataKeyWithoutPlaintext",
            "GenerateMac",
            "GetPublicKey",
            "ReEncryptFrom",
            "ReEncryptTo",
            "RetireGrant",
            "Sign",
            "Verify",
            "VerifyMac",
        ]
    ] = Field(alias="Operations")
    retiring_principal: Optional[str] = Field(default=None, alias="RetiringPrincipal")
    constraints: Optional[GrantConstraintsModel] = Field(
        default=None, alias="Constraints"
    )
    grant_tokens: Optional[Sequence[str]] = Field(default=None, alias="GrantTokens")
    name: Optional[str] = Field(default=None, alias="Name")


class GrantListEntryModel(BaseModel):
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    grant_id: Optional[str] = Field(default=None, alias="GrantId")
    name: Optional[str] = Field(default=None, alias="Name")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    grantee_principal: Optional[str] = Field(default=None, alias="GranteePrincipal")
    retiring_principal: Optional[str] = Field(default=None, alias="RetiringPrincipal")
    issuing_account: Optional[str] = Field(default=None, alias="IssuingAccount")
    operations: Optional[
        List[
            Literal[
                "CreateGrant",
                "Decrypt",
                "DescribeKey",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
                "GenerateDataKeyWithoutPlaintext",
                "GenerateMac",
                "GetPublicKey",
                "ReEncryptFrom",
                "ReEncryptTo",
                "RetireGrant",
                "Sign",
                "Verify",
                "VerifyMac",
            ]
        ]
    ] = Field(default=None, alias="Operations")
    constraints: Optional[GrantConstraintsModel] = Field(
        default=None, alias="Constraints"
    )


class CreateKeyRequestModel(BaseModel):
    policy: Optional[str] = Field(default=None, alias="Policy")
    description: Optional[str] = Field(default=None, alias="Description")
    key_usage: Optional[
        Literal["ENCRYPT_DECRYPT", "GENERATE_VERIFY_MAC", "SIGN_VERIFY"]
    ] = Field(default=None, alias="KeyUsage")
    customer_master_key_spec: Optional[
        Literal[
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "HMAC_224",
            "HMAC_256",
            "HMAC_384",
            "HMAC_512",
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "SM2",
            "SYMMETRIC_DEFAULT",
        ]
    ] = Field(default=None, alias="CustomerMasterKeySpec")
    key_spec: Optional[
        Literal[
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "HMAC_224",
            "HMAC_256",
            "HMAC_384",
            "HMAC_512",
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "SM2",
            "SYMMETRIC_DEFAULT",
        ]
    ] = Field(default=None, alias="KeySpec")
    origin: Optional[
        Literal["AWS_CLOUDHSM", "AWS_KMS", "EXTERNAL", "EXTERNAL_KEY_STORE"]
    ] = Field(default=None, alias="Origin")
    custom_key_store_id: Optional[str] = Field(default=None, alias="CustomKeyStoreId")
    bypass_policy_lockout_safety_check: Optional[bool] = Field(
        default=None, alias="BypassPolicyLockoutSafetyCheck"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    multi_region: Optional[bool] = Field(default=None, alias="MultiRegion")
    xks_key_id: Optional[str] = Field(default=None, alias="XksKeyId")


class ListResourceTagsResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_marker: str = Field(alias="NextMarker")
    truncated: bool = Field(alias="Truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicateKeyRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    replica_region: str = Field(alias="ReplicaRegion")
    policy: Optional[str] = Field(default=None, alias="Policy")
    bypass_policy_lockout_safety_check: Optional[bool] = Field(
        default=None, alias="BypassPolicyLockoutSafetyCheck"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CustomKeyStoresListEntryModel(BaseModel):
    custom_key_store_id: Optional[str] = Field(default=None, alias="CustomKeyStoreId")
    custom_key_store_name: Optional[str] = Field(
        default=None, alias="CustomKeyStoreName"
    )
    cloud_hsm_cluster_id: Optional[str] = Field(default=None, alias="CloudHsmClusterId")
    trust_anchor_certificate: Optional[str] = Field(
        default=None, alias="TrustAnchorCertificate"
    )
    connection_state: Optional[
        Literal["CONNECTED", "CONNECTING", "DISCONNECTED", "DISCONNECTING", "FAILED"]
    ] = Field(default=None, alias="ConnectionState")
    connection_error_code: Optional[
        Literal[
            "CLUSTER_NOT_FOUND",
            "INSUFFICIENT_CLOUDHSM_HSMS",
            "INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET",
            "INTERNAL_ERROR",
            "INVALID_CREDENTIALS",
            "NETWORK_ERRORS",
            "SUBNET_NOT_FOUND",
            "USER_LOCKED_OUT",
            "USER_LOGGED_IN",
            "USER_NOT_FOUND",
            "XKS_PROXY_ACCESS_DENIED",
            "XKS_PROXY_INVALID_CONFIGURATION",
            "XKS_PROXY_INVALID_RESPONSE",
            "XKS_PROXY_INVALID_TLS_CONFIGURATION",
            "XKS_PROXY_NOT_REACHABLE",
            "XKS_PROXY_TIMED_OUT",
            "XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION",
            "XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND",
        ]
    ] = Field(default=None, alias="ConnectionErrorCode")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    custom_key_store_type: Optional[
        Literal["AWS_CLOUDHSM", "EXTERNAL_KEY_STORE"]
    ] = Field(default=None, alias="CustomKeyStoreType")
    xks_proxy_configuration: Optional[XksProxyConfigurationTypeModel] = Field(
        default=None, alias="XksProxyConfiguration"
    )


class DescribeCustomKeyStoresRequestDescribeCustomKeyStoresPaginateModel(BaseModel):
    custom_key_store_id: Optional[str] = Field(default=None, alias="CustomKeyStoreId")
    custom_key_store_name: Optional[str] = Field(
        default=None, alias="CustomKeyStoreName"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAliasesRequestListAliasesPaginateModel(BaseModel):
    key_id: Optional[str] = Field(default=None, alias="KeyId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListGrantsRequestListGrantsPaginateModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    grant_id: Optional[str] = Field(default=None, alias="GrantId")
    grantee_principal: Optional[str] = Field(default=None, alias="GranteePrincipal")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListKeyPoliciesRequestListKeyPoliciesPaginateModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListKeysRequestListKeysPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceTagsRequestListResourceTagsPaginateModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRetirableGrantsRequestListRetirableGrantsPaginateModel(BaseModel):
    retiring_principal: str = Field(alias="RetiringPrincipal")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListKeysResponseModel(BaseModel):
    keys: List[KeyListEntryModel] = Field(alias="Keys")
    next_marker: str = Field(alias="NextMarker")
    truncated: bool = Field(alias="Truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class MultiRegionConfigurationModel(BaseModel):
    multi_region_key_type: Optional[Literal["PRIMARY", "REPLICA"]] = Field(
        default=None, alias="MultiRegionKeyType"
    )
    primary_key: Optional[MultiRegionKeyModel] = Field(default=None, alias="PrimaryKey")
    replica_keys: Optional[List[MultiRegionKeyModel]] = Field(
        default=None, alias="ReplicaKeys"
    )


class ListGrantsResponseModel(BaseModel):
    grants: List[GrantListEntryModel] = Field(alias="Grants")
    next_marker: str = Field(alias="NextMarker")
    truncated: bool = Field(alias="Truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCustomKeyStoresResponseModel(BaseModel):
    custom_key_stores: List[CustomKeyStoresListEntryModel] = Field(
        alias="CustomKeyStores"
    )
    next_marker: str = Field(alias="NextMarker")
    truncated: bool = Field(alias="Truncated")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class KeyMetadataModel(BaseModel):
    key_id: str = Field(alias="KeyId")
    aws_account_id: Optional[str] = Field(default=None, alias="AWSAccountId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    enabled: Optional[bool] = Field(default=None, alias="Enabled")
    description: Optional[str] = Field(default=None, alias="Description")
    key_usage: Optional[
        Literal["ENCRYPT_DECRYPT", "GENERATE_VERIFY_MAC", "SIGN_VERIFY"]
    ] = Field(default=None, alias="KeyUsage")
    key_state: Optional[
        Literal[
            "Creating",
            "Disabled",
            "Enabled",
            "PendingDeletion",
            "PendingImport",
            "PendingReplicaDeletion",
            "Unavailable",
            "Updating",
        ]
    ] = Field(default=None, alias="KeyState")
    deletion_date: Optional[datetime] = Field(default=None, alias="DeletionDate")
    valid_to: Optional[datetime] = Field(default=None, alias="ValidTo")
    origin: Optional[
        Literal["AWS_CLOUDHSM", "AWS_KMS", "EXTERNAL", "EXTERNAL_KEY_STORE"]
    ] = Field(default=None, alias="Origin")
    custom_key_store_id: Optional[str] = Field(default=None, alias="CustomKeyStoreId")
    cloud_hsm_cluster_id: Optional[str] = Field(default=None, alias="CloudHsmClusterId")
    expiration_model: Optional[
        Literal["KEY_MATERIAL_DOES_NOT_EXPIRE", "KEY_MATERIAL_EXPIRES"]
    ] = Field(default=None, alias="ExpirationModel")
    key_manager: Optional[Literal["AWS", "CUSTOMER"]] = Field(
        default=None, alias="KeyManager"
    )
    customer_master_key_spec: Optional[
        Literal[
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "HMAC_224",
            "HMAC_256",
            "HMAC_384",
            "HMAC_512",
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "SM2",
            "SYMMETRIC_DEFAULT",
        ]
    ] = Field(default=None, alias="CustomerMasterKeySpec")
    key_spec: Optional[
        Literal[
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "HMAC_224",
            "HMAC_256",
            "HMAC_384",
            "HMAC_512",
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "SM2",
            "SYMMETRIC_DEFAULT",
        ]
    ] = Field(default=None, alias="KeySpec")
    encryption_algorithms: Optional[
        List[
            Literal[
                "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SM2PKE", "SYMMETRIC_DEFAULT"
            ]
        ]
    ] = Field(default=None, alias="EncryptionAlgorithms")
    signing_algorithms: Optional[
        List[
            Literal[
                "ECDSA_SHA_256",
                "ECDSA_SHA_384",
                "ECDSA_SHA_512",
                "RSASSA_PKCS1_V1_5_SHA_256",
                "RSASSA_PKCS1_V1_5_SHA_384",
                "RSASSA_PKCS1_V1_5_SHA_512",
                "RSASSA_PSS_SHA_256",
                "RSASSA_PSS_SHA_384",
                "RSASSA_PSS_SHA_512",
                "SM2DSA",
            ]
        ]
    ] = Field(default=None, alias="SigningAlgorithms")
    multi_region: Optional[bool] = Field(default=None, alias="MultiRegion")
    multi_region_configuration: Optional[MultiRegionConfigurationModel] = Field(
        default=None, alias="MultiRegionConfiguration"
    )
    pending_deletion_window_in_days: Optional[int] = Field(
        default=None, alias="PendingDeletionWindowInDays"
    )
    mac_algorithms: Optional[
        List[Literal["HMAC_SHA_224", "HMAC_SHA_256", "HMAC_SHA_384", "HMAC_SHA_512"]]
    ] = Field(default=None, alias="MacAlgorithms")
    xks_key_configuration: Optional[XksKeyConfigurationTypeModel] = Field(
        default=None, alias="XksKeyConfiguration"
    )


class CreateKeyResponseModel(BaseModel):
    key_metadata: KeyMetadataModel = Field(alias="KeyMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeKeyResponseModel(BaseModel):
    key_metadata: KeyMetadataModel = Field(alias="KeyMetadata")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReplicateKeyResponseModel(BaseModel):
    replica_key_metadata: KeyMetadataModel = Field(alias="ReplicaKeyMetadata")
    replica_policy: str = Field(alias="ReplicaPolicy")
    replica_tags: List[TagModel] = Field(alias="ReplicaTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
