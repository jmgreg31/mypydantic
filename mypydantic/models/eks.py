# Model Generated: Thu Mar  2 21:56:18 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AddonIssueModel(BaseModel):
    code: Optional[
        Literal[
            "AccessDenied",
            "AdmissionRequestDenied",
            "ClusterUnreachable",
            "ConfigurationConflict",
            "InsufficientNumberOfReplicas",
            "InternalFailure",
            "K8sResourceNotFound",
            "UnsupportedAddonModification",
        ]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")
    resource_ids: Optional[List[str]] = Field(default=None, alias="resourceIds")


class MarketplaceInformationModel(BaseModel):
    product_id: Optional[str] = Field(default=None, alias="productId")
    product_url: Optional[str] = Field(default=None, alias="productUrl")


class CompatibilityModel(BaseModel):
    cluster_version: Optional[str] = Field(default=None, alias="clusterVersion")
    platform_versions: Optional[List[str]] = Field(
        default=None, alias="platformVersions"
    )
    default_version: Optional[bool] = Field(default=None, alias="defaultVersion")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class OidcIdentityProviderConfigRequestModel(BaseModel):
    identity_provider_config_name: str = Field(alias="identityProviderConfigName")
    issuer_url: str = Field(alias="issuerUrl")
    client_id: str = Field(alias="clientId")
    username_claim: Optional[str] = Field(default=None, alias="usernameClaim")
    username_prefix: Optional[str] = Field(default=None, alias="usernamePrefix")
    groups_claim: Optional[str] = Field(default=None, alias="groupsClaim")
    groups_prefix: Optional[str] = Field(default=None, alias="groupsPrefix")
    required_claims: Optional[Mapping[str, str]] = Field(
        default=None, alias="requiredClaims"
    )


class AutoScalingGroupModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")


class CertificateModel(BaseModel):
    data: Optional[str] = Field(default=None, alias="data")


class ClusterIssueModel(BaseModel):
    code: Optional[
        Literal[
            "AccessDenied",
            "ClusterUnreachable",
            "ConfigurationConflict",
            "InternalFailure",
            "ResourceLimitExceeded",
            "ResourceNotFound",
        ]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")
    resource_ids: Optional[List[str]] = Field(default=None, alias="resourceIds")


class ConnectorConfigResponseModel(BaseModel):
    activation_id: Optional[str] = Field(default=None, alias="activationId")
    activation_code: Optional[str] = Field(default=None, alias="activationCode")
    activation_expiry: Optional[datetime] = Field(
        default=None, alias="activationExpiry"
    )
    provider: Optional[str] = Field(default=None, alias="provider")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")


class KubernetesNetworkConfigResponseModel(BaseModel):
    service_ipv4_cidr: Optional[str] = Field(default=None, alias="serviceIpv4Cidr")
    service_ipv6_cidr: Optional[str] = Field(default=None, alias="serviceIpv6Cidr")
    ip_family: Optional[Literal["ipv4", "ipv6"]] = Field(default=None, alias="ipFamily")


class VpcConfigResponseModel(BaseModel):
    subnet_ids: Optional[List[str]] = Field(default=None, alias="subnetIds")
    security_group_ids: Optional[List[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    cluster_security_group_id: Optional[str] = Field(
        default=None, alias="clusterSecurityGroupId"
    )
    vpc_id: Optional[str] = Field(default=None, alias="vpcId")
    endpoint_public_access: Optional[bool] = Field(
        default=None, alias="endpointPublicAccess"
    )
    endpoint_private_access: Optional[bool] = Field(
        default=None, alias="endpointPrivateAccess"
    )
    public_access_cidrs: Optional[List[str]] = Field(
        default=None, alias="publicAccessCidrs"
    )


class ConnectorConfigRequestModel(BaseModel):
    role_arn: str = Field(alias="roleArn")
    provider: Literal[
        "AKS",
        "ANTHOS",
        "EC2",
        "EKS_ANYWHERE",
        "GKE",
        "OPENSHIFT",
        "OTHER",
        "RANCHER",
        "TANZU",
    ] = Field(alias="provider")


class ControlPlanePlacementRequestModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="groupName")


class ControlPlanePlacementResponseModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="groupName")


class CreateAddonRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    addon_name: str = Field(alias="addonName")
    addon_version: Optional[str] = Field(default=None, alias="addonVersion")
    service_account_role_arn: Optional[str] = Field(
        default=None, alias="serviceAccountRoleArn"
    )
    resolve_conflicts: Optional[Literal["NONE", "OVERWRITE", "PRESERVE"]] = Field(
        default=None, alias="resolveConflicts"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    configuration_values: Optional[str] = Field(
        default=None, alias="configurationValues"
    )


class KubernetesNetworkConfigRequestModel(BaseModel):
    service_ipv4_cidr: Optional[str] = Field(default=None, alias="serviceIpv4Cidr")
    ip_family: Optional[Literal["ipv4", "ipv6"]] = Field(default=None, alias="ipFamily")


class VpcConfigRequestModel(BaseModel):
    subnet_ids: Optional[Sequence[str]] = Field(default=None, alias="subnetIds")
    security_group_ids: Optional[Sequence[str]] = Field(
        default=None, alias="securityGroupIds"
    )
    endpoint_public_access: Optional[bool] = Field(
        default=None, alias="endpointPublicAccess"
    )
    endpoint_private_access: Optional[bool] = Field(
        default=None, alias="endpointPrivateAccess"
    )
    public_access_cidrs: Optional[Sequence[str]] = Field(
        default=None, alias="publicAccessCidrs"
    )


class FargateProfileSelectorModel(BaseModel):
    namespace: Optional[str] = Field(default=None, alias="namespace")
    labels: Optional[Mapping[str, str]] = Field(default=None, alias="labels")


class LaunchTemplateSpecificationModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    version: Optional[str] = Field(default=None, alias="version")
    id: Optional[str] = Field(default=None, alias="id")


class NodegroupScalingConfigModel(BaseModel):
    min_size: Optional[int] = Field(default=None, alias="minSize")
    max_size: Optional[int] = Field(default=None, alias="maxSize")
    desired_size: Optional[int] = Field(default=None, alias="desiredSize")


class NodegroupUpdateConfigModel(BaseModel):
    max_unavailable: Optional[int] = Field(default=None, alias="maxUnavailable")
    max_unavailable_percentage: Optional[int] = Field(
        default=None, alias="maxUnavailablePercentage"
    )


class RemoteAccessConfigModel(BaseModel):
    ec2_ssh_key: Optional[str] = Field(default=None, alias="ec2SshKey")
    source_security_groups: Optional[Sequence[str]] = Field(
        default=None, alias="sourceSecurityGroups"
    )


class TaintModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[str] = Field(default=None, alias="value")
    effect: Optional[
        Literal["NO_EXECUTE", "NO_SCHEDULE", "PREFER_NO_SCHEDULE"]
    ] = Field(default=None, alias="effect")


class DeleteAddonRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    addon_name: str = Field(alias="addonName")
    preserve: Optional[bool] = Field(default=None, alias="preserve")


class DeleteClusterRequestModel(BaseModel):
    name: str = Field(alias="name")


class DeleteFargateProfileRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    fargate_profile_name: str = Field(alias="fargateProfileName")


class DeleteNodegroupRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    nodegroup_name: str = Field(alias="nodegroupName")


class DeregisterClusterRequestModel(BaseModel):
    name: str = Field(alias="name")


class DescribeAddonConfigurationRequestModel(BaseModel):
    addon_name: str = Field(alias="addonName")
    addon_version: str = Field(alias="addonVersion")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeAddonRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    addon_name: str = Field(alias="addonName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAddonVersionsRequestModel(BaseModel):
    kubernetes_version: Optional[str] = Field(default=None, alias="kubernetesVersion")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    addon_name: Optional[str] = Field(default=None, alias="addonName")
    types: Optional[Sequence[str]] = Field(default=None, alias="types")
    publishers: Optional[Sequence[str]] = Field(default=None, alias="publishers")
    owners: Optional[Sequence[str]] = Field(default=None, alias="owners")


class DescribeClusterRequestModel(BaseModel):
    name: str = Field(alias="name")


class DescribeFargateProfileRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    fargate_profile_name: str = Field(alias="fargateProfileName")


class IdentityProviderConfigModel(BaseModel):
    type: str = Field(alias="type")
    name: str = Field(alias="name")


class DescribeNodegroupRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    nodegroup_name: str = Field(alias="nodegroupName")


class DescribeUpdateRequestModel(BaseModel):
    name: str = Field(alias="name")
    update_id: str = Field(alias="updateId")
    nodegroup_name: Optional[str] = Field(default=None, alias="nodegroupName")
    addon_name: Optional[str] = Field(default=None, alias="addonName")


class ProviderModel(BaseModel):
    key_arn: Optional[str] = Field(default=None, alias="keyArn")


class ErrorDetailModel(BaseModel):
    error_code: Optional[
        Literal[
            "AccessDenied",
            "AdmissionRequestDenied",
            "ClusterUnreachable",
            "ConfigurationConflict",
            "EniLimitReached",
            "InsufficientFreeAddresses",
            "InsufficientNumberOfReplicas",
            "IpNotAvailable",
            "K8sResourceNotFound",
            "NodeCreationFailure",
            "OperationNotPermitted",
            "PodEvictionFailure",
            "SecurityGroupNotFound",
            "SubnetNotFound",
            "Unknown",
            "UnsupportedAddonModification",
            "VpcIdNotFound",
        ]
    ] = Field(default=None, alias="errorCode")
    error_message: Optional[str] = Field(default=None, alias="errorMessage")
    resource_ids: Optional[List[str]] = Field(default=None, alias="resourceIds")


class OidcIdentityProviderConfigModel(BaseModel):
    identity_provider_config_name: Optional[str] = Field(
        default=None, alias="identityProviderConfigName"
    )
    identity_provider_config_arn: Optional[str] = Field(
        default=None, alias="identityProviderConfigArn"
    )
    cluster_name: Optional[str] = Field(default=None, alias="clusterName")
    issuer_url: Optional[str] = Field(default=None, alias="issuerUrl")
    client_id: Optional[str] = Field(default=None, alias="clientId")
    username_claim: Optional[str] = Field(default=None, alias="usernameClaim")
    username_prefix: Optional[str] = Field(default=None, alias="usernamePrefix")
    groups_claim: Optional[str] = Field(default=None, alias="groupsClaim")
    groups_prefix: Optional[str] = Field(default=None, alias="groupsPrefix")
    required_claims: Optional[Dict[str, str]] = Field(
        default=None, alias="requiredClaims"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    status: Optional[Literal["ACTIVE", "CREATING", "DELETING"]] = Field(
        default=None, alias="status"
    )


class OIDCModel(BaseModel):
    issuer: Optional[str] = Field(default=None, alias="issuer")


class IssueModel(BaseModel):
    code: Optional[
        Literal[
            "AccessDenied",
            "AsgInstanceLaunchFailures",
            "AutoScalingGroupInvalidConfiguration",
            "AutoScalingGroupNotFound",
            "ClusterUnreachable",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2SecurityGroupNotFound",
            "Ec2SubnetInvalidConfiguration",
            "Ec2SubnetMissingIpv6Assignment",
            "Ec2SubnetNotFound",
            "IamInstanceProfileNotFound",
            "IamLimitExceeded",
            "IamNodeRoleNotFound",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "InternalFailure",
            "NodeCreationFailure",
        ]
    ] = Field(default=None, alias="code")
    message: Optional[str] = Field(default=None, alias="message")
    resource_ids: Optional[List[str]] = Field(default=None, alias="resourceIds")


class ListAddonsRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListClustersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    include: Optional[Sequence[str]] = Field(default=None, alias="include")


class ListFargateProfilesRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListIdentityProviderConfigsRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListNodegroupsRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")


class ListUpdatesRequestModel(BaseModel):
    name: str = Field(alias="name")
    nodegroup_name: Optional[str] = Field(default=None, alias="nodegroupName")
    addon_name: Optional[str] = Field(default=None, alias="addonName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")
    max_results: Optional[int] = Field(default=None, alias="maxResults")


class LogSetupModel(BaseModel):
    types: Optional[
        Sequence[
            Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]
        ]
    ] = Field(default=None, alias="types")
    enabled: Optional[bool] = Field(default=None, alias="enabled")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tags: Mapping[str, str] = Field(alias="tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="resourceArn")
    tag_keys: Sequence[str] = Field(alias="tagKeys")


class UpdateAddonRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    addon_name: str = Field(alias="addonName")
    addon_version: Optional[str] = Field(default=None, alias="addonVersion")
    service_account_role_arn: Optional[str] = Field(
        default=None, alias="serviceAccountRoleArn"
    )
    resolve_conflicts: Optional[Literal["NONE", "OVERWRITE", "PRESERVE"]] = Field(
        default=None, alias="resolveConflicts"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    configuration_values: Optional[str] = Field(
        default=None, alias="configurationValues"
    )


class UpdateClusterVersionRequestModel(BaseModel):
    name: str = Field(alias="name")
    version: str = Field(alias="version")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class UpdateLabelsPayloadModel(BaseModel):
    add_or_update_labels: Optional[Mapping[str, str]] = Field(
        default=None, alias="addOrUpdateLabels"
    )
    remove_labels: Optional[Sequence[str]] = Field(default=None, alias="removeLabels")


class UpdateParamModel(BaseModel):
    type: Optional[
        Literal[
            "AddonVersion",
            "ClusterLogging",
            "DesiredSize",
            "EncryptionConfig",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "IdentityProviderConfig",
            "LabelsToAdd",
            "LabelsToRemove",
            "LaunchTemplateName",
            "LaunchTemplateVersion",
            "MaxSize",
            "MaxUnavailable",
            "MaxUnavailablePercentage",
            "MinSize",
            "PlatformVersion",
            "PublicAccessCidrs",
            "ReleaseVersion",
            "ResolveConflicts",
            "ServiceAccountRoleArn",
            "TaintsToAdd",
            "TaintsToRemove",
            "Version",
        ]
    ] = Field(default=None, alias="type")
    value: Optional[str] = Field(default=None, alias="value")


class AddonHealthModel(BaseModel):
    issues: Optional[List[AddonIssueModel]] = Field(default=None, alias="issues")


class AddonVersionInfoModel(BaseModel):
    addon_version: Optional[str] = Field(default=None, alias="addonVersion")
    architecture: Optional[List[str]] = Field(default=None, alias="architecture")
    compatibilities: Optional[List[CompatibilityModel]] = Field(
        default=None, alias="compatibilities"
    )
    requires_configuration: Optional[bool] = Field(
        default=None, alias="requiresConfiguration"
    )


class DescribeAddonConfigurationResponseModel(BaseModel):
    addon_name: str = Field(alias="addonName")
    addon_version: str = Field(alias="addonVersion")
    configuration_schema: str = Field(alias="configurationSchema")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAddonsResponseModel(BaseModel):
    addons: List[str] = Field(alias="addons")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClustersResponseModel(BaseModel):
    clusters: List[str] = Field(alias="clusters")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListFargateProfilesResponseModel(BaseModel):
    fargate_profile_names: List[str] = Field(alias="fargateProfileNames")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNodegroupsResponseModel(BaseModel):
    nodegroups: List[str] = Field(alias="nodegroups")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUpdatesResponseModel(BaseModel):
    update_ids: List[str] = Field(alias="updateIds")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateIdentityProviderConfigRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    oidc: OidcIdentityProviderConfigRequestModel = Field(alias="oidc")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class NodegroupResourcesModel(BaseModel):
    auto_scaling_groups: Optional[List[AutoScalingGroupModel]] = Field(
        default=None, alias="autoScalingGroups"
    )
    remote_access_security_group: Optional[str] = Field(
        default=None, alias="remoteAccessSecurityGroup"
    )


class ClusterHealthModel(BaseModel):
    issues: Optional[List[ClusterIssueModel]] = Field(default=None, alias="issues")


class RegisterClusterRequestModel(BaseModel):
    name: str = Field(alias="name")
    connector_config: ConnectorConfigRequestModel = Field(alias="connectorConfig")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class OutpostConfigRequestModel(BaseModel):
    outpost_arns: Sequence[str] = Field(alias="outpostArns")
    control_plane_instance_type: str = Field(alias="controlPlaneInstanceType")
    control_plane_placement: Optional[ControlPlanePlacementRequestModel] = Field(
        default=None, alias="controlPlanePlacement"
    )


class OutpostConfigResponseModel(BaseModel):
    outpost_arns: List[str] = Field(alias="outpostArns")
    control_plane_instance_type: str = Field(alias="controlPlaneInstanceType")
    control_plane_placement: Optional[ControlPlanePlacementResponseModel] = Field(
        default=None, alias="controlPlanePlacement"
    )


class CreateFargateProfileRequestModel(BaseModel):
    fargate_profile_name: str = Field(alias="fargateProfileName")
    cluster_name: str = Field(alias="clusterName")
    pod_execution_role_arn: str = Field(alias="podExecutionRoleArn")
    subnets: Optional[Sequence[str]] = Field(default=None, alias="subnets")
    selectors: Optional[Sequence[FargateProfileSelectorModel]] = Field(
        default=None, alias="selectors"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class FargateProfileModel(BaseModel):
    fargate_profile_name: Optional[str] = Field(
        default=None, alias="fargateProfileName"
    )
    fargate_profile_arn: Optional[str] = Field(default=None, alias="fargateProfileArn")
    cluster_name: Optional[str] = Field(default=None, alias="clusterName")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    pod_execution_role_arn: Optional[str] = Field(
        default=None, alias="podExecutionRoleArn"
    )
    subnets: Optional[List[str]] = Field(default=None, alias="subnets")
    selectors: Optional[List[FargateProfileSelectorModel]] = Field(
        default=None, alias="selectors"
    )
    status: Optional[
        Literal["ACTIVE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
    ] = Field(default=None, alias="status")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateNodegroupVersionRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    nodegroup_name: str = Field(alias="nodegroupName")
    version: Optional[str] = Field(default=None, alias="version")
    release_version: Optional[str] = Field(default=None, alias="releaseVersion")
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="launchTemplate"
    )
    force: Optional[bool] = Field(default=None, alias="force")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class CreateNodegroupRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    nodegroup_name: str = Field(alias="nodegroupName")
    subnets: Sequence[str] = Field(alias="subnets")
    node_role: str = Field(alias="nodeRole")
    scaling_config: Optional[NodegroupScalingConfigModel] = Field(
        default=None, alias="scalingConfig"
    )
    disk_size: Optional[int] = Field(default=None, alias="diskSize")
    instance_types: Optional[Sequence[str]] = Field(default=None, alias="instanceTypes")
    ami_type: Optional[
        Literal[
            "AL2_ARM_64",
            "AL2_x86_64",
            "AL2_x86_64_GPU",
            "BOTTLEROCKET_ARM_64",
            "BOTTLEROCKET_ARM_64_NVIDIA",
            "BOTTLEROCKET_x86_64",
            "BOTTLEROCKET_x86_64_NVIDIA",
            "CUSTOM",
            "WINDOWS_CORE_2019_x86_64",
            "WINDOWS_CORE_2022_x86_64",
            "WINDOWS_FULL_2019_x86_64",
            "WINDOWS_FULL_2022_x86_64",
        ]
    ] = Field(default=None, alias="amiType")
    remote_access: Optional[RemoteAccessConfigModel] = Field(
        default=None, alias="remoteAccess"
    )
    labels: Optional[Mapping[str, str]] = Field(default=None, alias="labels")
    taints: Optional[Sequence[TaintModel]] = Field(default=None, alias="taints")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="launchTemplate"
    )
    update_config: Optional[NodegroupUpdateConfigModel] = Field(
        default=None, alias="updateConfig"
    )
    capacity_type: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(
        default=None, alias="capacityType"
    )
    version: Optional[str] = Field(default=None, alias="version")
    release_version: Optional[str] = Field(default=None, alias="releaseVersion")


class UpdateTaintsPayloadModel(BaseModel):
    add_or_update_taints: Optional[Sequence[TaintModel]] = Field(
        default=None, alias="addOrUpdateTaints"
    )
    remove_taints: Optional[Sequence[TaintModel]] = Field(
        default=None, alias="removeTaints"
    )


class DescribeAddonRequestAddonActiveWaitModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    addon_name: str = Field(alias="addonName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeAddonRequestAddonDeletedWaitModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    addon_name: str = Field(alias="addonName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeClusterRequestClusterActiveWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeClusterRequestClusterDeletedWaitModel(BaseModel):
    name: str = Field(alias="name")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeFargateProfileRequestFargateProfileActiveWaitModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    fargate_profile_name: str = Field(alias="fargateProfileName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeFargateProfileRequestFargateProfileDeletedWaitModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    fargate_profile_name: str = Field(alias="fargateProfileName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeNodegroupRequestNodegroupActiveWaitModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    nodegroup_name: str = Field(alias="nodegroupName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeNodegroupRequestNodegroupDeletedWaitModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    nodegroup_name: str = Field(alias="nodegroupName")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeAddonVersionsRequestDescribeAddonVersionsPaginateModel(BaseModel):
    kubernetes_version: Optional[str] = Field(default=None, alias="kubernetesVersion")
    addon_name: Optional[str] = Field(default=None, alias="addonName")
    types: Optional[Sequence[str]] = Field(default=None, alias="types")
    publishers: Optional[Sequence[str]] = Field(default=None, alias="publishers")
    owners: Optional[Sequence[str]] = Field(default=None, alias="owners")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAddonsRequestListAddonsPaginateModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersRequestListClustersPaginateModel(BaseModel):
    include: Optional[Sequence[str]] = Field(default=None, alias="include")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFargateProfilesRequestListFargateProfilesPaginateModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIdentityProviderConfigsRequestListIdentityProviderConfigsPaginateModel(
    BaseModel
):
    cluster_name: str = Field(alias="clusterName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNodegroupsRequestListNodegroupsPaginateModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListUpdatesRequestListUpdatesPaginateModel(BaseModel):
    name: str = Field(alias="name")
    nodegroup_name: Optional[str] = Field(default=None, alias="nodegroupName")
    addon_name: Optional[str] = Field(default=None, alias="addonName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeIdentityProviderConfigRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    identity_provider_config: IdentityProviderConfigModel = Field(
        alias="identityProviderConfig"
    )


class DisassociateIdentityProviderConfigRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    identity_provider_config: IdentityProviderConfigModel = Field(
        alias="identityProviderConfig"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class ListIdentityProviderConfigsResponseModel(BaseModel):
    identity_provider_configs: List[IdentityProviderConfigModel] = Field(
        alias="identityProviderConfigs"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EncryptionConfigModel(BaseModel):
    resources: Optional[Sequence[str]] = Field(default=None, alias="resources")
    provider: Optional[ProviderModel] = Field(default=None, alias="provider")


class IdentityProviderConfigResponseModel(BaseModel):
    oidc: Optional[OidcIdentityProviderConfigModel] = Field(default=None, alias="oidc")


class IdentityModel(BaseModel):
    oidc: Optional[OIDCModel] = Field(default=None, alias="oidc")


class NodegroupHealthModel(BaseModel):
    issues: Optional[List[IssueModel]] = Field(default=None, alias="issues")


class LoggingModel(BaseModel):
    cluster_logging: Optional[Sequence[LogSetupModel]] = Field(
        default=None, alias="clusterLogging"
    )


class UpdateModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    status: Optional[
        Literal["Cancelled", "Failed", "InProgress", "Successful"]
    ] = Field(default=None, alias="status")
    type: Optional[
        Literal[
            "AddonUpdate",
            "AssociateEncryptionConfig",
            "AssociateIdentityProviderConfig",
            "ConfigUpdate",
            "DisassociateIdentityProviderConfig",
            "EndpointAccessUpdate",
            "LoggingUpdate",
            "VersionUpdate",
        ]
    ] = Field(default=None, alias="type")
    params: Optional[List[UpdateParamModel]] = Field(default=None, alias="params")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    errors: Optional[List[ErrorDetailModel]] = Field(default=None, alias="errors")


class AddonModel(BaseModel):
    addon_name: Optional[str] = Field(default=None, alias="addonName")
    cluster_name: Optional[str] = Field(default=None, alias="clusterName")
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATE_FAILED",
            "CREATING",
            "DEGRADED",
            "DELETE_FAILED",
            "DELETING",
            "UPDATE_FAILED",
            "UPDATING",
        ]
    ] = Field(default=None, alias="status")
    addon_version: Optional[str] = Field(default=None, alias="addonVersion")
    health: Optional[AddonHealthModel] = Field(default=None, alias="health")
    addon_arn: Optional[str] = Field(default=None, alias="addonArn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, alias="modifiedAt")
    service_account_role_arn: Optional[str] = Field(
        default=None, alias="serviceAccountRoleArn"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    publisher: Optional[str] = Field(default=None, alias="publisher")
    owner: Optional[str] = Field(default=None, alias="owner")
    marketplace_information: Optional[MarketplaceInformationModel] = Field(
        default=None, alias="marketplaceInformation"
    )
    configuration_values: Optional[str] = Field(
        default=None, alias="configurationValues"
    )


class AddonInfoModel(BaseModel):
    addon_name: Optional[str] = Field(default=None, alias="addonName")
    type: Optional[str] = Field(default=None, alias="type")
    addon_versions: Optional[List[AddonVersionInfoModel]] = Field(
        default=None, alias="addonVersions"
    )
    publisher: Optional[str] = Field(default=None, alias="publisher")
    owner: Optional[str] = Field(default=None, alias="owner")
    marketplace_information: Optional[MarketplaceInformationModel] = Field(
        default=None, alias="marketplaceInformation"
    )


class CreateFargateProfileResponseModel(BaseModel):
    fargate_profile: FargateProfileModel = Field(alias="fargateProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFargateProfileResponseModel(BaseModel):
    fargate_profile: FargateProfileModel = Field(alias="fargateProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFargateProfileResponseModel(BaseModel):
    fargate_profile: FargateProfileModel = Field(alias="fargateProfile")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNodegroupConfigRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    nodegroup_name: str = Field(alias="nodegroupName")
    labels: Optional[UpdateLabelsPayloadModel] = Field(default=None, alias="labels")
    taints: Optional[UpdateTaintsPayloadModel] = Field(default=None, alias="taints")
    scaling_config: Optional[NodegroupScalingConfigModel] = Field(
        default=None, alias="scalingConfig"
    )
    update_config: Optional[NodegroupUpdateConfigModel] = Field(
        default=None, alias="updateConfig"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class AssociateEncryptionConfigRequestModel(BaseModel):
    cluster_name: str = Field(alias="clusterName")
    encryption_config: Sequence[EncryptionConfigModel] = Field(alias="encryptionConfig")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class DescribeIdentityProviderConfigResponseModel(BaseModel):
    identity_provider_config: IdentityProviderConfigResponseModel = Field(
        alias="identityProviderConfig"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class NodegroupModel(BaseModel):
    nodegroup_name: Optional[str] = Field(default=None, alias="nodegroupName")
    nodegroup_arn: Optional[str] = Field(default=None, alias="nodegroupArn")
    cluster_name: Optional[str] = Field(default=None, alias="clusterName")
    version: Optional[str] = Field(default=None, alias="version")
    release_version: Optional[str] = Field(default=None, alias="releaseVersion")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, alias="modifiedAt")
    status: Optional[
        Literal[
            "ACTIVE",
            "CREATE_FAILED",
            "CREATING",
            "DEGRADED",
            "DELETE_FAILED",
            "DELETING",
            "UPDATING",
        ]
    ] = Field(default=None, alias="status")
    capacity_type: Optional[Literal["ON_DEMAND", "SPOT"]] = Field(
        default=None, alias="capacityType"
    )
    scaling_config: Optional[NodegroupScalingConfigModel] = Field(
        default=None, alias="scalingConfig"
    )
    instance_types: Optional[List[str]] = Field(default=None, alias="instanceTypes")
    subnets: Optional[List[str]] = Field(default=None, alias="subnets")
    remote_access: Optional[RemoteAccessConfigModel] = Field(
        default=None, alias="remoteAccess"
    )
    ami_type: Optional[
        Literal[
            "AL2_ARM_64",
            "AL2_x86_64",
            "AL2_x86_64_GPU",
            "BOTTLEROCKET_ARM_64",
            "BOTTLEROCKET_ARM_64_NVIDIA",
            "BOTTLEROCKET_x86_64",
            "BOTTLEROCKET_x86_64_NVIDIA",
            "CUSTOM",
            "WINDOWS_CORE_2019_x86_64",
            "WINDOWS_CORE_2022_x86_64",
            "WINDOWS_FULL_2019_x86_64",
            "WINDOWS_FULL_2022_x86_64",
        ]
    ] = Field(default=None, alias="amiType")
    node_role: Optional[str] = Field(default=None, alias="nodeRole")
    labels: Optional[Dict[str, str]] = Field(default=None, alias="labels")
    taints: Optional[List[TaintModel]] = Field(default=None, alias="taints")
    resources: Optional[NodegroupResourcesModel] = Field(
        default=None, alias="resources"
    )
    disk_size: Optional[int] = Field(default=None, alias="diskSize")
    health: Optional[NodegroupHealthModel] = Field(default=None, alias="health")
    update_config: Optional[NodegroupUpdateConfigModel] = Field(
        default=None, alias="updateConfig"
    )
    launch_template: Optional[LaunchTemplateSpecificationModel] = Field(
        default=None, alias="launchTemplate"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class ClusterModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    arn: Optional[str] = Field(default=None, alias="arn")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    version: Optional[str] = Field(default=None, alias="version")
    endpoint: Optional[str] = Field(default=None, alias="endpoint")
    role_arn: Optional[str] = Field(default=None, alias="roleArn")
    resources_vpc_config: Optional[VpcConfigResponseModel] = Field(
        default=None, alias="resourcesVpcConfig"
    )
    kubernetes_network_config: Optional[KubernetesNetworkConfigResponseModel] = Field(
        default=None, alias="kubernetesNetworkConfig"
    )
    logging: Optional[LoggingModel] = Field(default=None, alias="logging")
    identity: Optional[IdentityModel] = Field(default=None, alias="identity")
    status: Optional[
        Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PENDING", "UPDATING"]
    ] = Field(default=None, alias="status")
    certificate_authority: Optional[CertificateModel] = Field(
        default=None, alias="certificateAuthority"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    platform_version: Optional[str] = Field(default=None, alias="platformVersion")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    encryption_config: Optional[List[EncryptionConfigModel]] = Field(
        default=None, alias="encryptionConfig"
    )
    connector_config: Optional[ConnectorConfigResponseModel] = Field(
        default=None, alias="connectorConfig"
    )
    id: Optional[str] = Field(default=None, alias="id")
    health: Optional[ClusterHealthModel] = Field(default=None, alias="health")
    outpost_config: Optional[OutpostConfigResponseModel] = Field(
        default=None, alias="outpostConfig"
    )


class CreateClusterRequestModel(BaseModel):
    name: str = Field(alias="name")
    role_arn: str = Field(alias="roleArn")
    resources_vpc_config: VpcConfigRequestModel = Field(alias="resourcesVpcConfig")
    version: Optional[str] = Field(default=None, alias="version")
    kubernetes_network_config: Optional[KubernetesNetworkConfigRequestModel] = Field(
        default=None, alias="kubernetesNetworkConfig"
    )
    logging: Optional[LoggingModel] = Field(default=None, alias="logging")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")
    encryption_config: Optional[Sequence[EncryptionConfigModel]] = Field(
        default=None, alias="encryptionConfig"
    )
    outpost_config: Optional[OutpostConfigRequestModel] = Field(
        default=None, alias="outpostConfig"
    )


class UpdateClusterConfigRequestModel(BaseModel):
    name: str = Field(alias="name")
    resources_vpc_config: Optional[VpcConfigRequestModel] = Field(
        default=None, alias="resourcesVpcConfig"
    )
    logging: Optional[LoggingModel] = Field(default=None, alias="logging")
    client_request_token: Optional[str] = Field(
        default=None, alias="clientRequestToken"
    )


class AssociateEncryptionConfigResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AssociateIdentityProviderConfigResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    tags: Dict[str, str] = Field(alias="tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUpdateResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DisassociateIdentityProviderConfigResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAddonResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterConfigResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateClusterVersionResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNodegroupConfigResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateNodegroupVersionResponseModel(BaseModel):
    update: UpdateModel = Field(alias="update")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAddonResponseModel(BaseModel):
    addon: AddonModel = Field(alias="addon")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAddonResponseModel(BaseModel):
    addon: AddonModel = Field(alias="addon")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAddonResponseModel(BaseModel):
    addon: AddonModel = Field(alias="addon")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAddonVersionsResponseModel(BaseModel):
    addons: List[AddonInfoModel] = Field(alias="addons")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNodegroupResponseModel(BaseModel):
    nodegroup: NodegroupModel = Field(alias="nodegroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNodegroupResponseModel(BaseModel):
    nodegroup: NodegroupModel = Field(alias="nodegroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNodegroupResponseModel(BaseModel):
    nodegroup: NodegroupModel = Field(alias="nodegroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeregisterClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
