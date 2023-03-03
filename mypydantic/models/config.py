# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountAggregationSourceModel(BaseModel):
    account_ids: List[str] = Field(alias="AccountIds")
    all_aws_regions: Optional[bool] = Field(default=None, alias="AllAwsRegions")
    aws_regions: Optional[List[str]] = Field(default=None, alias="AwsRegions")


class AggregateConformancePackComplianceModel(BaseModel):
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
    ] = Field(default=None, alias="ComplianceType")
    compliant_rule_count: Optional[int] = Field(
        default=None, alias="CompliantRuleCount"
    )
    non_compliant_rule_count: Optional[int] = Field(
        default=None, alias="NonCompliantRuleCount"
    )
    total_rule_count: Optional[int] = Field(default=None, alias="TotalRuleCount")


class AggregateConformancePackComplianceCountModel(BaseModel):
    compliant_conformance_pack_count: Optional[int] = Field(
        default=None, alias="CompliantConformancePackCount"
    )
    non_compliant_conformance_pack_count: Optional[int] = Field(
        default=None, alias="NonCompliantConformancePackCount"
    )


class AggregateConformancePackComplianceFiltersModel(BaseModel):
    conformance_pack_name: Optional[str] = Field(
        default=None, alias="ConformancePackName"
    )
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
    ] = Field(default=None, alias="ComplianceType")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class AggregateConformancePackComplianceSummaryFiltersModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class AggregateResourceIdentifierModel(BaseModel):
    source_account_id: str = Field(alias="SourceAccountId")
    source_region: str = Field(alias="SourceRegion")
    resource_id: str = Field(alias="ResourceId")
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="ResourceType")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")


class AggregatedSourceStatusModel(BaseModel):
    source_id: Optional[str] = Field(default=None, alias="SourceId")
    source_type: Optional[Literal["ACCOUNT", "ORGANIZATION"]] = Field(
        default=None, alias="SourceType"
    )
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")
    last_update_status: Optional[Literal["FAILED", "OUTDATED", "SUCCEEDED"]] = Field(
        default=None, alias="LastUpdateStatus"
    )
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")
    last_error_code: Optional[str] = Field(default=None, alias="LastErrorCode")
    last_error_message: Optional[str] = Field(default=None, alias="LastErrorMessage")


class AggregationAuthorizationModel(BaseModel):
    aggregation_authorization_arn: Optional[str] = Field(
        default=None, alias="AggregationAuthorizationArn"
    )
    authorized_account_id: Optional[str] = Field(
        default=None, alias="AuthorizedAccountId"
    )
    authorized_aws_region: Optional[str] = Field(
        default=None, alias="AuthorizedAwsRegion"
    )
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")


class BaseConfigurationItemModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="version")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    configuration_item_capture_time: Optional[datetime] = Field(
        default=None, alias="configurationItemCaptureTime"
    )
    configuration_item_status: Optional[
        Literal[
            "OK",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
            "ResourceDiscovered",
            "ResourceNotRecorded",
        ]
    ] = Field(default=None, alias="configurationItemStatus")
    configuration_state_id: Optional[str] = Field(
        default=None, alias="configurationStateId"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    resource_type: Optional[
        Literal[
            "AWS::ACM::Certificate",
            "AWS::AccessAnalyzer::Analyzer",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::ApiGatewayV2::Stage",
            "AWS::AppConfig::Application",
            "AWS::AppSync::GraphQLApi",
            "AWS::Athena::DataCatalog",
            "AWS::Athena::WorkGroup",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::Backup::BackupPlan",
            "AWS::Backup::BackupSelection",
            "AWS::Backup::BackupVault",
            "AWS::Backup::RecoveryPoint",
            "AWS::Batch::ComputeEnvironment",
            "AWS::Batch::JobQueue",
            "AWS::CloudFormation::Stack",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::CloudTrail::Trail",
            "AWS::CloudWatch::Alarm",
            "AWS::CodeBuild::Project",
            "AWS::CodeDeploy::Application",
            "AWS::CodeDeploy::DeploymentConfig",
            "AWS::CodeDeploy::DeploymentGroup",
            "AWS::CodePipeline::Pipeline",
            "AWS::Config::ConformancePackCompliance",
            "AWS::Config::ResourceCompliance",
            "AWS::DMS::Certificate",
            "AWS::DMS::EventSubscription",
            "AWS::DMS::ReplicationSubnetGroup",
            "AWS::DataSync::LocationEFS",
            "AWS::DataSync::LocationFSxLustre",
            "AWS::DataSync::LocationNFS",
            "AWS::DataSync::LocationS3",
            "AWS::DataSync::LocationSMB",
            "AWS::DataSync::Task",
            "AWS::Detective::Graph",
            "AWS::DynamoDB::Table",
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::FlowLog",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::LaunchTemplate",
            "AWS::EC2::NatGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::EC2::TransitGateway",
            "AWS::EC2::TransitGatewayAttachment",
            "AWS::EC2::TransitGatewayRouteTable",
            "AWS::EC2::VPC",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::Volume",
            "AWS::ECR::PublicRepository",
            "AWS::ECR::Repository",
            "AWS::ECS::Cluster",
            "AWS::ECS::Service",
            "AWS::ECS::TaskDefinition",
            "AWS::EFS::AccessPoint",
            "AWS::EFS::FileSystem",
            "AWS::EKS::Cluster",
            "AWS::EKS::FargateProfile",
            "AWS::EMR::SecurityConfiguration",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::ElasticLoadBalancingV2::Listener",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::Elasticsearch::Domain",
            "AWS::GlobalAccelerator::Accelerator",
            "AWS::GlobalAccelerator::EndpointGroup",
            "AWS::GlobalAccelerator::Listener",
            "AWS::Glue::Job",
            "AWS::GuardDuty::Detector",
            "AWS::GuardDuty::IPSet",
            "AWS::GuardDuty::ThreatIntelSet",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::KMS::Key",
            "AWS::Kinesis::Stream",
            "AWS::Kinesis::StreamConsumer",
            "AWS::Lambda::Function",
            "AWS::MSK::Cluster",
            "AWS::NetworkFirewall::Firewall",
            "AWS::NetworkFirewall::FirewallPolicy",
            "AWS::NetworkFirewall::RuleGroup",
            "AWS::OpenSearch::Domain",
            "AWS::QLDB::Ledger",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::EventSubscription",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::Route53::HostedZone",
            "AWS::Route53Resolver::ResolverEndpoint",
            "AWS::Route53Resolver::ResolverRule",
            "AWS::Route53Resolver::ResolverRuleAssociation",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::S3::Bucket",
            "AWS::SES::ConfigurationSet",
            "AWS::SES::ContactList",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::FileData",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::SSM::PatchCompliance",
            "AWS::SageMaker::CodeRepository",
            "AWS::SageMaker::Model",
            "AWS::SageMaker::NotebookInstanceLifecycleConfig",
            "AWS::SageMaker::Workteam",
            "AWS::SecretsManager::Secret",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::ServiceDiscovery::PublicDnsNamespace",
            "AWS::ServiceDiscovery::Service",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::StepFunctions::Activity",
            "AWS::StepFunctions::StateMachine",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::WebACL",
            "AWS::WorkSpaces::ConnectionAlias",
            "AWS::WorkSpaces::Workspace",
            "AWS::XRay::EncryptionConfig",
        ]
    ] = Field(default=None, alias="resourceType")
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    resource_creation_time: Optional[datetime] = Field(
        default=None, alias="resourceCreationTime"
    )
    configuration: Optional[str] = Field(default=None, alias="configuration")
    supplementary_configuration: Optional[Dict[str, str]] = Field(
        default=None, alias="supplementaryConfiguration"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ResourceKeyModel(BaseModel):
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="resourceType")
    resource_id: str = Field(alias="resourceId")


class ComplianceContributorCountModel(BaseModel):
    capped_count: Optional[int] = Field(default=None, alias="CappedCount")
    cap_exceeded: Optional[bool] = Field(default=None, alias="CapExceeded")


class ConfigExportDeliveryInfoModel(BaseModel):
    last_status: Optional[Literal["Failure", "Not_Applicable", "Success"]] = Field(
        default=None, alias="lastStatus"
    )
    last_error_code: Optional[str] = Field(default=None, alias="lastErrorCode")
    last_error_message: Optional[str] = Field(default=None, alias="lastErrorMessage")
    last_attempt_time: Optional[datetime] = Field(default=None, alias="lastAttemptTime")
    last_successful_time: Optional[datetime] = Field(
        default=None, alias="lastSuccessfulTime"
    )
    next_delivery_time: Optional[datetime] = Field(
        default=None, alias="nextDeliveryTime"
    )


class ConfigRuleComplianceFiltersModel(BaseModel):
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
    ] = Field(default=None, alias="ComplianceType")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class ConfigRuleComplianceSummaryFiltersModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class ConfigRuleEvaluationStatusModel(BaseModel):
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")
    config_rule_arn: Optional[str] = Field(default=None, alias="ConfigRuleArn")
    config_rule_id: Optional[str] = Field(default=None, alias="ConfigRuleId")
    last_successful_invocation_time: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulInvocationTime"
    )
    last_failed_invocation_time: Optional[datetime] = Field(
        default=None, alias="LastFailedInvocationTime"
    )
    last_successful_evaluation_time: Optional[datetime] = Field(
        default=None, alias="LastSuccessfulEvaluationTime"
    )
    last_failed_evaluation_time: Optional[datetime] = Field(
        default=None, alias="LastFailedEvaluationTime"
    )
    first_activated_time: Optional[datetime] = Field(
        default=None, alias="FirstActivatedTime"
    )
    last_deactivated_time: Optional[datetime] = Field(
        default=None, alias="LastDeactivatedTime"
    )
    last_error_code: Optional[str] = Field(default=None, alias="LastErrorCode")
    last_error_message: Optional[str] = Field(default=None, alias="LastErrorMessage")
    first_evaluation_started: Optional[bool] = Field(
        default=None, alias="FirstEvaluationStarted"
    )
    last_debug_log_delivery_status: Optional[str] = Field(
        default=None, alias="LastDebugLogDeliveryStatus"
    )
    last_debug_log_delivery_status_reason: Optional[str] = Field(
        default=None, alias="LastDebugLogDeliveryStatusReason"
    )
    last_debug_log_delivery_time: Optional[datetime] = Field(
        default=None, alias="LastDebugLogDeliveryTime"
    )


class EvaluationModeConfigurationModel(BaseModel):
    mode: Optional[Literal["DETECTIVE", "PROACTIVE"]] = Field(
        default=None, alias="Mode"
    )


class ScopeModel(BaseModel):
    compliance_resource_types: Optional[List[str]] = Field(
        default=None, alias="ComplianceResourceTypes"
    )
    tag_key: Optional[str] = Field(default=None, alias="TagKey")
    tag_value: Optional[str] = Field(default=None, alias="TagValue")
    compliance_resource_id: Optional[str] = Field(
        default=None, alias="ComplianceResourceId"
    )


class ConfigSnapshotDeliveryPropertiesModel(BaseModel):
    delivery_frequency: Optional[
        Literal[
            "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    ] = Field(default=None, alias="deliveryFrequency")


class ConfigStreamDeliveryInfoModel(BaseModel):
    last_status: Optional[Literal["Failure", "Not_Applicable", "Success"]] = Field(
        default=None, alias="lastStatus"
    )
    last_error_code: Optional[str] = Field(default=None, alias="lastErrorCode")
    last_error_message: Optional[str] = Field(default=None, alias="lastErrorMessage")
    last_status_change_time: Optional[datetime] = Field(
        default=None, alias="lastStatusChangeTime"
    )


class OrganizationAggregationSourceModel(BaseModel):
    role_arn: str = Field(alias="RoleArn")
    aws_regions: Optional[List[str]] = Field(default=None, alias="AwsRegions")
    all_aws_regions: Optional[bool] = Field(default=None, alias="AllAwsRegions")


class RelationshipModel(BaseModel):
    resource_type: Optional[
        Literal[
            "AWS::ACM::Certificate",
            "AWS::AccessAnalyzer::Analyzer",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::ApiGatewayV2::Stage",
            "AWS::AppConfig::Application",
            "AWS::AppSync::GraphQLApi",
            "AWS::Athena::DataCatalog",
            "AWS::Athena::WorkGroup",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::Backup::BackupPlan",
            "AWS::Backup::BackupSelection",
            "AWS::Backup::BackupVault",
            "AWS::Backup::RecoveryPoint",
            "AWS::Batch::ComputeEnvironment",
            "AWS::Batch::JobQueue",
            "AWS::CloudFormation::Stack",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::CloudTrail::Trail",
            "AWS::CloudWatch::Alarm",
            "AWS::CodeBuild::Project",
            "AWS::CodeDeploy::Application",
            "AWS::CodeDeploy::DeploymentConfig",
            "AWS::CodeDeploy::DeploymentGroup",
            "AWS::CodePipeline::Pipeline",
            "AWS::Config::ConformancePackCompliance",
            "AWS::Config::ResourceCompliance",
            "AWS::DMS::Certificate",
            "AWS::DMS::EventSubscription",
            "AWS::DMS::ReplicationSubnetGroup",
            "AWS::DataSync::LocationEFS",
            "AWS::DataSync::LocationFSxLustre",
            "AWS::DataSync::LocationNFS",
            "AWS::DataSync::LocationS3",
            "AWS::DataSync::LocationSMB",
            "AWS::DataSync::Task",
            "AWS::Detective::Graph",
            "AWS::DynamoDB::Table",
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::FlowLog",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::LaunchTemplate",
            "AWS::EC2::NatGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::EC2::TransitGateway",
            "AWS::EC2::TransitGatewayAttachment",
            "AWS::EC2::TransitGatewayRouteTable",
            "AWS::EC2::VPC",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::Volume",
            "AWS::ECR::PublicRepository",
            "AWS::ECR::Repository",
            "AWS::ECS::Cluster",
            "AWS::ECS::Service",
            "AWS::ECS::TaskDefinition",
            "AWS::EFS::AccessPoint",
            "AWS::EFS::FileSystem",
            "AWS::EKS::Cluster",
            "AWS::EKS::FargateProfile",
            "AWS::EMR::SecurityConfiguration",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::ElasticLoadBalancingV2::Listener",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::Elasticsearch::Domain",
            "AWS::GlobalAccelerator::Accelerator",
            "AWS::GlobalAccelerator::EndpointGroup",
            "AWS::GlobalAccelerator::Listener",
            "AWS::Glue::Job",
            "AWS::GuardDuty::Detector",
            "AWS::GuardDuty::IPSet",
            "AWS::GuardDuty::ThreatIntelSet",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::KMS::Key",
            "AWS::Kinesis::Stream",
            "AWS::Kinesis::StreamConsumer",
            "AWS::Lambda::Function",
            "AWS::MSK::Cluster",
            "AWS::NetworkFirewall::Firewall",
            "AWS::NetworkFirewall::FirewallPolicy",
            "AWS::NetworkFirewall::RuleGroup",
            "AWS::OpenSearch::Domain",
            "AWS::QLDB::Ledger",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::EventSubscription",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::Route53::HostedZone",
            "AWS::Route53Resolver::ResolverEndpoint",
            "AWS::Route53Resolver::ResolverRule",
            "AWS::Route53Resolver::ResolverRuleAssociation",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::S3::Bucket",
            "AWS::SES::ConfigurationSet",
            "AWS::SES::ContactList",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::FileData",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::SSM::PatchCompliance",
            "AWS::SageMaker::CodeRepository",
            "AWS::SageMaker::Model",
            "AWS::SageMaker::NotebookInstanceLifecycleConfig",
            "AWS::SageMaker::Workteam",
            "AWS::SecretsManager::Secret",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::ServiceDiscovery::PublicDnsNamespace",
            "AWS::ServiceDiscovery::Service",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::StepFunctions::Activity",
            "AWS::StepFunctions::StateMachine",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::WebACL",
            "AWS::WorkSpaces::ConnectionAlias",
            "AWS::WorkSpaces::Workspace",
            "AWS::XRay::EncryptionConfig",
        ]
    ] = Field(default=None, alias="resourceType")
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    relationship_name: Optional[str] = Field(default=None, alias="relationshipName")


class ConfigurationRecorderStatusModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    last_start_time: Optional[datetime] = Field(default=None, alias="lastStartTime")
    last_stop_time: Optional[datetime] = Field(default=None, alias="lastStopTime")
    recording: Optional[bool] = Field(default=None, alias="recording")
    last_status: Optional[Literal["Failure", "Pending", "Success"]] = Field(
        default=None, alias="lastStatus"
    )
    last_error_code: Optional[str] = Field(default=None, alias="lastErrorCode")
    last_error_message: Optional[str] = Field(default=None, alias="lastErrorMessage")
    last_status_change_time: Optional[datetime] = Field(
        default=None, alias="lastStatusChangeTime"
    )


class RecordingGroupModel(BaseModel):
    all_supported: Optional[bool] = Field(default=None, alias="allSupported")
    include_global_resource_types: Optional[bool] = Field(
        default=None, alias="includeGlobalResourceTypes"
    )
    resource_types: Optional[
        List[
            Literal[
                "AWS::ACM::Certificate",
                "AWS::AccessAnalyzer::Analyzer",
                "AWS::ApiGateway::RestApi",
                "AWS::ApiGateway::Stage",
                "AWS::ApiGatewayV2::Api",
                "AWS::ApiGatewayV2::Stage",
                "AWS::AppConfig::Application",
                "AWS::AppSync::GraphQLApi",
                "AWS::Athena::DataCatalog",
                "AWS::Athena::WorkGroup",
                "AWS::AutoScaling::AutoScalingGroup",
                "AWS::AutoScaling::LaunchConfiguration",
                "AWS::AutoScaling::ScalingPolicy",
                "AWS::AutoScaling::ScheduledAction",
                "AWS::Backup::BackupPlan",
                "AWS::Backup::BackupSelection",
                "AWS::Backup::BackupVault",
                "AWS::Backup::RecoveryPoint",
                "AWS::Batch::ComputeEnvironment",
                "AWS::Batch::JobQueue",
                "AWS::CloudFormation::Stack",
                "AWS::CloudFront::Distribution",
                "AWS::CloudFront::StreamingDistribution",
                "AWS::CloudTrail::Trail",
                "AWS::CloudWatch::Alarm",
                "AWS::CodeBuild::Project",
                "AWS::CodeDeploy::Application",
                "AWS::CodeDeploy::DeploymentConfig",
                "AWS::CodeDeploy::DeploymentGroup",
                "AWS::CodePipeline::Pipeline",
                "AWS::Config::ConformancePackCompliance",
                "AWS::Config::ResourceCompliance",
                "AWS::DMS::Certificate",
                "AWS::DMS::EventSubscription",
                "AWS::DMS::ReplicationSubnetGroup",
                "AWS::DataSync::LocationEFS",
                "AWS::DataSync::LocationFSxLustre",
                "AWS::DataSync::LocationNFS",
                "AWS::DataSync::LocationS3",
                "AWS::DataSync::LocationSMB",
                "AWS::DataSync::Task",
                "AWS::Detective::Graph",
                "AWS::DynamoDB::Table",
                "AWS::EC2::CustomerGateway",
                "AWS::EC2::EIP",
                "AWS::EC2::EgressOnlyInternetGateway",
                "AWS::EC2::FlowLog",
                "AWS::EC2::Host",
                "AWS::EC2::Instance",
                "AWS::EC2::InternetGateway",
                "AWS::EC2::LaunchTemplate",
                "AWS::EC2::NatGateway",
                "AWS::EC2::NetworkAcl",
                "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
                "AWS::EC2::NetworkInterface",
                "AWS::EC2::RegisteredHAInstance",
                "AWS::EC2::RouteTable",
                "AWS::EC2::SecurityGroup",
                "AWS::EC2::Subnet",
                "AWS::EC2::TransitGateway",
                "AWS::EC2::TransitGatewayAttachment",
                "AWS::EC2::TransitGatewayRouteTable",
                "AWS::EC2::VPC",
                "AWS::EC2::VPCEndpoint",
                "AWS::EC2::VPCEndpointService",
                "AWS::EC2::VPCPeeringConnection",
                "AWS::EC2::VPNConnection",
                "AWS::EC2::VPNGateway",
                "AWS::EC2::Volume",
                "AWS::ECR::PublicRepository",
                "AWS::ECR::Repository",
                "AWS::ECS::Cluster",
                "AWS::ECS::Service",
                "AWS::ECS::TaskDefinition",
                "AWS::EFS::AccessPoint",
                "AWS::EFS::FileSystem",
                "AWS::EKS::Cluster",
                "AWS::EKS::FargateProfile",
                "AWS::EMR::SecurityConfiguration",
                "AWS::ElasticBeanstalk::Application",
                "AWS::ElasticBeanstalk::ApplicationVersion",
                "AWS::ElasticBeanstalk::Environment",
                "AWS::ElasticLoadBalancing::LoadBalancer",
                "AWS::ElasticLoadBalancingV2::Listener",
                "AWS::ElasticLoadBalancingV2::LoadBalancer",
                "AWS::Elasticsearch::Domain",
                "AWS::GlobalAccelerator::Accelerator",
                "AWS::GlobalAccelerator::EndpointGroup",
                "AWS::GlobalAccelerator::Listener",
                "AWS::Glue::Job",
                "AWS::GuardDuty::Detector",
                "AWS::GuardDuty::IPSet",
                "AWS::GuardDuty::ThreatIntelSet",
                "AWS::IAM::Group",
                "AWS::IAM::Policy",
                "AWS::IAM::Role",
                "AWS::IAM::User",
                "AWS::KMS::Key",
                "AWS::Kinesis::Stream",
                "AWS::Kinesis::StreamConsumer",
                "AWS::Lambda::Function",
                "AWS::MSK::Cluster",
                "AWS::NetworkFirewall::Firewall",
                "AWS::NetworkFirewall::FirewallPolicy",
                "AWS::NetworkFirewall::RuleGroup",
                "AWS::OpenSearch::Domain",
                "AWS::QLDB::Ledger",
                "AWS::RDS::DBCluster",
                "AWS::RDS::DBClusterSnapshot",
                "AWS::RDS::DBInstance",
                "AWS::RDS::DBSecurityGroup",
                "AWS::RDS::DBSnapshot",
                "AWS::RDS::DBSubnetGroup",
                "AWS::RDS::EventSubscription",
                "AWS::Redshift::Cluster",
                "AWS::Redshift::ClusterParameterGroup",
                "AWS::Redshift::ClusterSecurityGroup",
                "AWS::Redshift::ClusterSnapshot",
                "AWS::Redshift::ClusterSubnetGroup",
                "AWS::Redshift::EventSubscription",
                "AWS::Route53::HostedZone",
                "AWS::Route53Resolver::ResolverEndpoint",
                "AWS::Route53Resolver::ResolverRule",
                "AWS::Route53Resolver::ResolverRuleAssociation",
                "AWS::S3::AccountPublicAccessBlock",
                "AWS::S3::Bucket",
                "AWS::SES::ConfigurationSet",
                "AWS::SES::ContactList",
                "AWS::SNS::Topic",
                "AWS::SQS::Queue",
                "AWS::SSM::AssociationCompliance",
                "AWS::SSM::FileData",
                "AWS::SSM::ManagedInstanceInventory",
                "AWS::SSM::PatchCompliance",
                "AWS::SageMaker::CodeRepository",
                "AWS::SageMaker::Model",
                "AWS::SageMaker::NotebookInstanceLifecycleConfig",
                "AWS::SageMaker::Workteam",
                "AWS::SecretsManager::Secret",
                "AWS::ServiceCatalog::CloudFormationProduct",
                "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
                "AWS::ServiceCatalog::Portfolio",
                "AWS::ServiceDiscovery::PublicDnsNamespace",
                "AWS::ServiceDiscovery::Service",
                "AWS::Shield::Protection",
                "AWS::ShieldRegional::Protection",
                "AWS::StepFunctions::Activity",
                "AWS::StepFunctions::StateMachine",
                "AWS::WAF::RateBasedRule",
                "AWS::WAF::Rule",
                "AWS::WAF::RuleGroup",
                "AWS::WAF::WebACL",
                "AWS::WAFRegional::RateBasedRule",
                "AWS::WAFRegional::Rule",
                "AWS::WAFRegional::RuleGroup",
                "AWS::WAFRegional::WebACL",
                "AWS::WAFv2::IPSet",
                "AWS::WAFv2::ManagedRuleSet",
                "AWS::WAFv2::RegexPatternSet",
                "AWS::WAFv2::RuleGroup",
                "AWS::WAFv2::WebACL",
                "AWS::WorkSpaces::ConnectionAlias",
                "AWS::WorkSpaces::Workspace",
                "AWS::XRay::EncryptionConfig",
            ]
        ]
    ] = Field(default=None, alias="resourceTypes")


class ConformancePackComplianceFiltersModel(BaseModel):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
    ] = Field(default=None, alias="ComplianceType")


class ConformancePackComplianceScoreModel(BaseModel):
    score: Optional[str] = Field(default=None, alias="Score")
    conformance_pack_name: Optional[str] = Field(
        default=None, alias="ConformancePackName"
    )
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class ConformancePackComplianceScoresFiltersModel(BaseModel):
    conformance_pack_names: Sequence[str] = Field(alias="ConformancePackNames")


class ConformancePackComplianceSummaryModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    conformance_pack_compliance_status: Literal[
        "COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"
    ] = Field(alias="ConformancePackComplianceStatus")


class ConformancePackInputParameterModel(BaseModel):
    parameter_name: str = Field(alias="ParameterName")
    parameter_value: str = Field(alias="ParameterValue")


class TemplateSSMDocumentDetailsModel(BaseModel):
    document_name: str = Field(alias="DocumentName")
    document_version: Optional[str] = Field(default=None, alias="DocumentVersion")


class ConformancePackEvaluationFiltersModel(BaseModel):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
    ] = Field(default=None, alias="ComplianceType")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_ids: Optional[Sequence[str]] = Field(default=None, alias="ResourceIds")


class ConformancePackRuleComplianceModel(BaseModel):
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
    ] = Field(default=None, alias="ComplianceType")
    controls: Optional[List[str]] = Field(default=None, alias="Controls")


class ConformancePackStatusDetailModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    conformance_pack_id: str = Field(alias="ConformancePackId")
    conformance_pack_arn: str = Field(alias="ConformancePackArn")
    conformance_pack_state: Literal[
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
    ] = Field(alias="ConformancePackState")
    stack_arn: str = Field(alias="StackArn")
    last_update_requested_time: datetime = Field(alias="LastUpdateRequestedTime")
    conformance_pack_status_reason: Optional[str] = Field(
        default=None, alias="ConformancePackStatusReason"
    )
    last_update_completed_time: Optional[datetime] = Field(
        default=None, alias="LastUpdateCompletedTime"
    )


class CustomPolicyDetailsModel(BaseModel):
    policy_runtime: str = Field(alias="PolicyRuntime")
    policy_text: str = Field(alias="PolicyText")
    enable_debug_log_delivery: Optional[bool] = Field(
        default=None, alias="EnableDebugLogDelivery"
    )


class DeleteAggregationAuthorizationRequestModel(BaseModel):
    authorized_account_id: str = Field(alias="AuthorizedAccountId")
    authorized_aws_region: str = Field(alias="AuthorizedAwsRegion")


class DeleteConfigRuleRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")


class DeleteConfigurationAggregatorRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")


class DeleteConfigurationRecorderRequestModel(BaseModel):
    configuration_recorder_name: str = Field(alias="ConfigurationRecorderName")


class DeleteConformancePackRequestModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")


class DeleteDeliveryChannelRequestModel(BaseModel):
    delivery_channel_name: str = Field(alias="DeliveryChannelName")


class DeleteEvaluationResultsRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")


class DeleteOrganizationConfigRuleRequestModel(BaseModel):
    organization_config_rule_name: str = Field(alias="OrganizationConfigRuleName")


class DeleteOrganizationConformancePackRequestModel(BaseModel):
    organization_conformance_pack_name: str = Field(
        alias="OrganizationConformancePackName"
    )


class DeletePendingAggregationRequestRequestModel(BaseModel):
    requester_account_id: str = Field(alias="RequesterAccountId")
    requester_aws_region: str = Field(alias="RequesterAwsRegion")


class DeleteRemediationConfigurationRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")


class RemediationExceptionResourceKeyModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")


class DeleteResourceConfigRequestModel(BaseModel):
    resource_type: str = Field(alias="ResourceType")
    resource_id: str = Field(alias="ResourceId")


class DeleteRetentionConfigurationRequestModel(BaseModel):
    retention_configuration_name: str = Field(alias="RetentionConfigurationName")


class DeleteStoredQueryRequestModel(BaseModel):
    query_name: str = Field(alias="QueryName")


class DeliverConfigSnapshotRequestModel(BaseModel):
    delivery_channel_name: str = Field(alias="deliveryChannelName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeAggregationAuthorizationsRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeComplianceByConfigRuleRequestModel(BaseModel):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeComplianceByResourceRequestModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeConfigRuleEvaluationStatusRequestModel(BaseModel):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeConfigRulesFiltersModel(BaseModel):
    evaluation_mode: Optional[Literal["DETECTIVE", "PROACTIVE"]] = Field(
        default=None, alias="EvaluationMode"
    )


class DescribeConfigurationAggregatorSourcesStatusRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    update_status: Optional[
        Sequence[Literal["FAILED", "OUTDATED", "SUCCEEDED"]]
    ] = Field(default=None, alias="UpdateStatus")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeConfigurationAggregatorsRequestModel(BaseModel):
    configuration_aggregator_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigurationAggregatorNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    limit: Optional[int] = Field(default=None, alias="Limit")


class DescribeConfigurationRecorderStatusRequestModel(BaseModel):
    configuration_recorder_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigurationRecorderNames"
    )


class DescribeConfigurationRecordersRequestModel(BaseModel):
    configuration_recorder_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigurationRecorderNames"
    )


class DescribeConformancePackStatusRequestModel(BaseModel):
    conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConformancePackNames"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeConformancePacksRequestModel(BaseModel):
    conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConformancePackNames"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeDeliveryChannelStatusRequestModel(BaseModel):
    delivery_channel_names: Optional[Sequence[str]] = Field(
        default=None, alias="DeliveryChannelNames"
    )


class DescribeDeliveryChannelsRequestModel(BaseModel):
    delivery_channel_names: Optional[Sequence[str]] = Field(
        default=None, alias="DeliveryChannelNames"
    )


class DescribeOrganizationConfigRuleStatusesRequestModel(BaseModel):
    organization_config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConfigRuleNames"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OrganizationConfigRuleStatusModel(BaseModel):
    organization_config_rule_name: str = Field(alias="OrganizationConfigRuleName")
    organization_rule_status: Literal[
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "CREATE_SUCCESSFUL",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SUCCESSFUL",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="OrganizationRuleStatus")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")


class DescribeOrganizationConfigRulesRequestModel(BaseModel):
    organization_config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConfigRuleNames"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeOrganizationConformancePackStatusesRequestModel(BaseModel):
    organization_conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConformancePackNames"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class OrganizationConformancePackStatusModel(BaseModel):
    organization_conformance_pack_name: str = Field(
        alias="OrganizationConformancePackName"
    )
    status: Literal[
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "CREATE_SUCCESSFUL",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SUCCESSFUL",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="Status")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")


class DescribeOrganizationConformancePacksRequestModel(BaseModel):
    organization_conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConformancePackNames"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribePendingAggregationRequestsRequestModel(BaseModel):
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class PendingAggregationRequestModel(BaseModel):
    requester_account_id: Optional[str] = Field(
        default=None, alias="RequesterAccountId"
    )
    requester_aws_region: Optional[str] = Field(
        default=None, alias="RequesterAwsRegion"
    )


class DescribeRemediationConfigurationsRequestModel(BaseModel):
    config_rule_names: Sequence[str] = Field(alias="ConfigRuleNames")


class RemediationExceptionModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_type: str = Field(alias="ResourceType")
    resource_id: str = Field(alias="ResourceId")
    message: Optional[str] = Field(default=None, alias="Message")
    expiration_time: Optional[datetime] = Field(default=None, alias="ExpirationTime")


class DescribeRetentionConfigurationsRequestModel(BaseModel):
    retention_configuration_names: Optional[Sequence[str]] = Field(
        default=None, alias="RetentionConfigurationNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class RetentionConfigurationModel(BaseModel):
    name: str = Field(alias="Name")
    retention_period_in_days: int = Field(alias="RetentionPeriodInDays")


class EvaluationContextModel(BaseModel):
    evaluation_context_identifier: Optional[str] = Field(
        default=None, alias="EvaluationContextIdentifier"
    )


class EvaluationResultQualifierModel(BaseModel):
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    evaluation_mode: Optional[Literal["DETECTIVE", "PROACTIVE"]] = Field(
        default=None, alias="EvaluationMode"
    )


class EvaluationStatusModel(BaseModel):
    status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="Status")
    failure_reason: Optional[str] = Field(default=None, alias="FailureReason")


class EvaluationModel(BaseModel):
    compliance_resource_type: str = Field(alias="ComplianceResourceType")
    compliance_resource_id: str = Field(alias="ComplianceResourceId")
    compliance_type: Literal[
        "COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"
    ] = Field(alias="ComplianceType")
    ordering_timestamp: Union[datetime, str] = Field(alias="OrderingTimestamp")
    annotation: Optional[str] = Field(default=None, alias="Annotation")


class SsmControlsModel(BaseModel):
    concurrent_execution_rate_percentage: Optional[int] = Field(
        default=None, alias="ConcurrentExecutionRatePercentage"
    )
    error_percentage: Optional[int] = Field(default=None, alias="ErrorPercentage")


class ExternalEvaluationModel(BaseModel):
    compliance_resource_type: str = Field(alias="ComplianceResourceType")
    compliance_resource_id: str = Field(alias="ComplianceResourceId")
    compliance_type: Literal[
        "COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"
    ] = Field(alias="ComplianceType")
    ordering_timestamp: Union[datetime, str] = Field(alias="OrderingTimestamp")
    annotation: Optional[str] = Field(default=None, alias="Annotation")


class FieldInfoModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class GetAggregateComplianceDetailsByConfigRuleRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    config_rule_name: str = Field(alias="ConfigRuleName")
    account_id: str = Field(alias="AccountId")
    aws_region: str = Field(alias="AwsRegion")
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
    ] = Field(default=None, alias="ComplianceType")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResourceCountFiltersModel(BaseModel):
    resource_type: Optional[
        Literal[
            "AWS::ACM::Certificate",
            "AWS::AccessAnalyzer::Analyzer",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::ApiGatewayV2::Stage",
            "AWS::AppConfig::Application",
            "AWS::AppSync::GraphQLApi",
            "AWS::Athena::DataCatalog",
            "AWS::Athena::WorkGroup",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::Backup::BackupPlan",
            "AWS::Backup::BackupSelection",
            "AWS::Backup::BackupVault",
            "AWS::Backup::RecoveryPoint",
            "AWS::Batch::ComputeEnvironment",
            "AWS::Batch::JobQueue",
            "AWS::CloudFormation::Stack",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::CloudTrail::Trail",
            "AWS::CloudWatch::Alarm",
            "AWS::CodeBuild::Project",
            "AWS::CodeDeploy::Application",
            "AWS::CodeDeploy::DeploymentConfig",
            "AWS::CodeDeploy::DeploymentGroup",
            "AWS::CodePipeline::Pipeline",
            "AWS::Config::ConformancePackCompliance",
            "AWS::Config::ResourceCompliance",
            "AWS::DMS::Certificate",
            "AWS::DMS::EventSubscription",
            "AWS::DMS::ReplicationSubnetGroup",
            "AWS::DataSync::LocationEFS",
            "AWS::DataSync::LocationFSxLustre",
            "AWS::DataSync::LocationNFS",
            "AWS::DataSync::LocationS3",
            "AWS::DataSync::LocationSMB",
            "AWS::DataSync::Task",
            "AWS::Detective::Graph",
            "AWS::DynamoDB::Table",
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::FlowLog",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::LaunchTemplate",
            "AWS::EC2::NatGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::EC2::TransitGateway",
            "AWS::EC2::TransitGatewayAttachment",
            "AWS::EC2::TransitGatewayRouteTable",
            "AWS::EC2::VPC",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::Volume",
            "AWS::ECR::PublicRepository",
            "AWS::ECR::Repository",
            "AWS::ECS::Cluster",
            "AWS::ECS::Service",
            "AWS::ECS::TaskDefinition",
            "AWS::EFS::AccessPoint",
            "AWS::EFS::FileSystem",
            "AWS::EKS::Cluster",
            "AWS::EKS::FargateProfile",
            "AWS::EMR::SecurityConfiguration",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::ElasticLoadBalancingV2::Listener",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::Elasticsearch::Domain",
            "AWS::GlobalAccelerator::Accelerator",
            "AWS::GlobalAccelerator::EndpointGroup",
            "AWS::GlobalAccelerator::Listener",
            "AWS::Glue::Job",
            "AWS::GuardDuty::Detector",
            "AWS::GuardDuty::IPSet",
            "AWS::GuardDuty::ThreatIntelSet",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::KMS::Key",
            "AWS::Kinesis::Stream",
            "AWS::Kinesis::StreamConsumer",
            "AWS::Lambda::Function",
            "AWS::MSK::Cluster",
            "AWS::NetworkFirewall::Firewall",
            "AWS::NetworkFirewall::FirewallPolicy",
            "AWS::NetworkFirewall::RuleGroup",
            "AWS::OpenSearch::Domain",
            "AWS::QLDB::Ledger",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::EventSubscription",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::Route53::HostedZone",
            "AWS::Route53Resolver::ResolverEndpoint",
            "AWS::Route53Resolver::ResolverRule",
            "AWS::Route53Resolver::ResolverRuleAssociation",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::S3::Bucket",
            "AWS::SES::ConfigurationSet",
            "AWS::SES::ContactList",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::FileData",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::SSM::PatchCompliance",
            "AWS::SageMaker::CodeRepository",
            "AWS::SageMaker::Model",
            "AWS::SageMaker::NotebookInstanceLifecycleConfig",
            "AWS::SageMaker::Workteam",
            "AWS::SecretsManager::Secret",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::ServiceDiscovery::PublicDnsNamespace",
            "AWS::ServiceDiscovery::Service",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::StepFunctions::Activity",
            "AWS::StepFunctions::StateMachine",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::WebACL",
            "AWS::WorkSpaces::ConnectionAlias",
            "AWS::WorkSpaces::Workspace",
            "AWS::XRay::EncryptionConfig",
        ]
    ] = Field(default=None, alias="ResourceType")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    region: Optional[str] = Field(default=None, alias="Region")


class GroupedResourceCountModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    resource_count: int = Field(alias="ResourceCount")


class GetComplianceDetailsByConfigRuleRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetComplianceDetailsByResourceRequestModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    resource_evaluation_id: Optional[str] = Field(
        default=None, alias="ResourceEvaluationId"
    )


class GetComplianceSummaryByResourceTypeRequestModel(BaseModel):
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="ResourceTypes")


class GetConformancePackComplianceSummaryRequestModel(BaseModel):
    conformance_pack_names: Sequence[str] = Field(alias="ConformancePackNames")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetCustomRulePolicyRequestModel(BaseModel):
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")


class GetDiscoveredResourceCountsRequestModel(BaseModel):
    resource_types: Optional[Sequence[str]] = Field(default=None, alias="resourceTypes")
    limit: Optional[int] = Field(default=None, alias="limit")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ResourceCountModel(BaseModel):
    resource_type: Optional[
        Literal[
            "AWS::ACM::Certificate",
            "AWS::AccessAnalyzer::Analyzer",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::ApiGatewayV2::Stage",
            "AWS::AppConfig::Application",
            "AWS::AppSync::GraphQLApi",
            "AWS::Athena::DataCatalog",
            "AWS::Athena::WorkGroup",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::Backup::BackupPlan",
            "AWS::Backup::BackupSelection",
            "AWS::Backup::BackupVault",
            "AWS::Backup::RecoveryPoint",
            "AWS::Batch::ComputeEnvironment",
            "AWS::Batch::JobQueue",
            "AWS::CloudFormation::Stack",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::CloudTrail::Trail",
            "AWS::CloudWatch::Alarm",
            "AWS::CodeBuild::Project",
            "AWS::CodeDeploy::Application",
            "AWS::CodeDeploy::DeploymentConfig",
            "AWS::CodeDeploy::DeploymentGroup",
            "AWS::CodePipeline::Pipeline",
            "AWS::Config::ConformancePackCompliance",
            "AWS::Config::ResourceCompliance",
            "AWS::DMS::Certificate",
            "AWS::DMS::EventSubscription",
            "AWS::DMS::ReplicationSubnetGroup",
            "AWS::DataSync::LocationEFS",
            "AWS::DataSync::LocationFSxLustre",
            "AWS::DataSync::LocationNFS",
            "AWS::DataSync::LocationS3",
            "AWS::DataSync::LocationSMB",
            "AWS::DataSync::Task",
            "AWS::Detective::Graph",
            "AWS::DynamoDB::Table",
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::FlowLog",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::LaunchTemplate",
            "AWS::EC2::NatGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::EC2::TransitGateway",
            "AWS::EC2::TransitGatewayAttachment",
            "AWS::EC2::TransitGatewayRouteTable",
            "AWS::EC2::VPC",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::Volume",
            "AWS::ECR::PublicRepository",
            "AWS::ECR::Repository",
            "AWS::ECS::Cluster",
            "AWS::ECS::Service",
            "AWS::ECS::TaskDefinition",
            "AWS::EFS::AccessPoint",
            "AWS::EFS::FileSystem",
            "AWS::EKS::Cluster",
            "AWS::EKS::FargateProfile",
            "AWS::EMR::SecurityConfiguration",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::ElasticLoadBalancingV2::Listener",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::Elasticsearch::Domain",
            "AWS::GlobalAccelerator::Accelerator",
            "AWS::GlobalAccelerator::EndpointGroup",
            "AWS::GlobalAccelerator::Listener",
            "AWS::Glue::Job",
            "AWS::GuardDuty::Detector",
            "AWS::GuardDuty::IPSet",
            "AWS::GuardDuty::ThreatIntelSet",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::KMS::Key",
            "AWS::Kinesis::Stream",
            "AWS::Kinesis::StreamConsumer",
            "AWS::Lambda::Function",
            "AWS::MSK::Cluster",
            "AWS::NetworkFirewall::Firewall",
            "AWS::NetworkFirewall::FirewallPolicy",
            "AWS::NetworkFirewall::RuleGroup",
            "AWS::OpenSearch::Domain",
            "AWS::QLDB::Ledger",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::EventSubscription",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::Route53::HostedZone",
            "AWS::Route53Resolver::ResolverEndpoint",
            "AWS::Route53Resolver::ResolverRule",
            "AWS::Route53Resolver::ResolverRuleAssociation",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::S3::Bucket",
            "AWS::SES::ConfigurationSet",
            "AWS::SES::ContactList",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::FileData",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::SSM::PatchCompliance",
            "AWS::SageMaker::CodeRepository",
            "AWS::SageMaker::Model",
            "AWS::SageMaker::NotebookInstanceLifecycleConfig",
            "AWS::SageMaker::Workteam",
            "AWS::SecretsManager::Secret",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::ServiceDiscovery::PublicDnsNamespace",
            "AWS::ServiceDiscovery::Service",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::StepFunctions::Activity",
            "AWS::StepFunctions::StateMachine",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::WebACL",
            "AWS::WorkSpaces::ConnectionAlias",
            "AWS::WorkSpaces::Workspace",
            "AWS::XRay::EncryptionConfig",
        ]
    ] = Field(default=None, alias="resourceType")
    count: Optional[int] = Field(default=None, alias="count")


class StatusDetailFiltersModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    member_account_rule_status: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "CREATE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "DELETE_SUCCESSFUL",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="MemberAccountRuleStatus")


class MemberAccountStatusModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    config_rule_name: str = Field(alias="ConfigRuleName")
    member_account_rule_status: Literal[
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "CREATE_SUCCESSFUL",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SUCCESSFUL",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="MemberAccountRuleStatus")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")


class OrganizationResourceDetailedStatusFiltersModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    status: Optional[
        Literal[
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "CREATE_SUCCESSFUL",
            "DELETE_FAILED",
            "DELETE_IN_PROGRESS",
            "DELETE_SUCCESSFUL",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")


class OrganizationConformancePackDetailedStatusModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    conformance_pack_name: str = Field(alias="ConformancePackName")
    status: Literal[
        "CREATE_FAILED",
        "CREATE_IN_PROGRESS",
        "CREATE_SUCCESSFUL",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_SUCCESSFUL",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="Status")
    error_code: Optional[str] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")


class GetOrganizationCustomRulePolicyRequestModel(BaseModel):
    organization_config_rule_name: str = Field(alias="OrganizationConfigRuleName")


class GetResourceConfigHistoryRequestModel(BaseModel):
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="resourceType")
    resource_id: str = Field(alias="resourceId")
    later_time: Optional[Union[datetime, str]] = Field(default=None, alias="laterTime")
    earlier_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="earlierTime"
    )
    chronological_order: Optional[Literal["Forward", "Reverse"]] = Field(
        default=None, alias="chronologicalOrder"
    )
    limit: Optional[int] = Field(default=None, alias="limit")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class GetResourceEvaluationSummaryRequestModel(BaseModel):
    resource_evaluation_id: str = Field(alias="ResourceEvaluationId")


class ResourceDetailsModel(BaseModel):
    resource_id: str = Field(alias="ResourceId")
    resource_type: str = Field(alias="ResourceType")
    resource_configuration: str = Field(alias="ResourceConfiguration")
    resource_configuration_schema_type: Optional[
        Literal["CFN_RESOURCE_SCHEMA"]
    ] = Field(default=None, alias="ResourceConfigurationSchemaType")


class GetStoredQueryRequestModel(BaseModel):
    query_name: str = Field(alias="QueryName")


class StoredQueryModel(BaseModel):
    query_name: str = Field(alias="QueryName")
    query_id: Optional[str] = Field(default=None, alias="QueryId")
    query_arn: Optional[str] = Field(default=None, alias="QueryArn")
    description: Optional[str] = Field(default=None, alias="Description")
    expression: Optional[str] = Field(default=None, alias="Expression")


class ResourceFiltersModel(BaseModel):
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    region: Optional[str] = Field(default=None, alias="Region")


class ListDiscoveredResourcesRequestModel(BaseModel):
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="resourceType")
    resource_ids: Optional[Sequence[str]] = Field(default=None, alias="resourceIds")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    limit: Optional[int] = Field(default=None, alias="limit")
    include_deleted_resources: Optional[bool] = Field(
        default=None, alias="includeDeletedResources"
    )
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ResourceIdentifierModel(BaseModel):
    resource_type: Optional[
        Literal[
            "AWS::ACM::Certificate",
            "AWS::AccessAnalyzer::Analyzer",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::ApiGatewayV2::Stage",
            "AWS::AppConfig::Application",
            "AWS::AppSync::GraphQLApi",
            "AWS::Athena::DataCatalog",
            "AWS::Athena::WorkGroup",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::Backup::BackupPlan",
            "AWS::Backup::BackupSelection",
            "AWS::Backup::BackupVault",
            "AWS::Backup::RecoveryPoint",
            "AWS::Batch::ComputeEnvironment",
            "AWS::Batch::JobQueue",
            "AWS::CloudFormation::Stack",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::CloudTrail::Trail",
            "AWS::CloudWatch::Alarm",
            "AWS::CodeBuild::Project",
            "AWS::CodeDeploy::Application",
            "AWS::CodeDeploy::DeploymentConfig",
            "AWS::CodeDeploy::DeploymentGroup",
            "AWS::CodePipeline::Pipeline",
            "AWS::Config::ConformancePackCompliance",
            "AWS::Config::ResourceCompliance",
            "AWS::DMS::Certificate",
            "AWS::DMS::EventSubscription",
            "AWS::DMS::ReplicationSubnetGroup",
            "AWS::DataSync::LocationEFS",
            "AWS::DataSync::LocationFSxLustre",
            "AWS::DataSync::LocationNFS",
            "AWS::DataSync::LocationS3",
            "AWS::DataSync::LocationSMB",
            "AWS::DataSync::Task",
            "AWS::Detective::Graph",
            "AWS::DynamoDB::Table",
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::FlowLog",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::LaunchTemplate",
            "AWS::EC2::NatGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::EC2::TransitGateway",
            "AWS::EC2::TransitGatewayAttachment",
            "AWS::EC2::TransitGatewayRouteTable",
            "AWS::EC2::VPC",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::Volume",
            "AWS::ECR::PublicRepository",
            "AWS::ECR::Repository",
            "AWS::ECS::Cluster",
            "AWS::ECS::Service",
            "AWS::ECS::TaskDefinition",
            "AWS::EFS::AccessPoint",
            "AWS::EFS::FileSystem",
            "AWS::EKS::Cluster",
            "AWS::EKS::FargateProfile",
            "AWS::EMR::SecurityConfiguration",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::ElasticLoadBalancingV2::Listener",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::Elasticsearch::Domain",
            "AWS::GlobalAccelerator::Accelerator",
            "AWS::GlobalAccelerator::EndpointGroup",
            "AWS::GlobalAccelerator::Listener",
            "AWS::Glue::Job",
            "AWS::GuardDuty::Detector",
            "AWS::GuardDuty::IPSet",
            "AWS::GuardDuty::ThreatIntelSet",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::KMS::Key",
            "AWS::Kinesis::Stream",
            "AWS::Kinesis::StreamConsumer",
            "AWS::Lambda::Function",
            "AWS::MSK::Cluster",
            "AWS::NetworkFirewall::Firewall",
            "AWS::NetworkFirewall::FirewallPolicy",
            "AWS::NetworkFirewall::RuleGroup",
            "AWS::OpenSearch::Domain",
            "AWS::QLDB::Ledger",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::EventSubscription",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::Route53::HostedZone",
            "AWS::Route53Resolver::ResolverEndpoint",
            "AWS::Route53Resolver::ResolverRule",
            "AWS::Route53Resolver::ResolverRuleAssociation",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::S3::Bucket",
            "AWS::SES::ConfigurationSet",
            "AWS::SES::ContactList",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::FileData",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::SSM::PatchCompliance",
            "AWS::SageMaker::CodeRepository",
            "AWS::SageMaker::Model",
            "AWS::SageMaker::NotebookInstanceLifecycleConfig",
            "AWS::SageMaker::Workteam",
            "AWS::SecretsManager::Secret",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::ServiceDiscovery::PublicDnsNamespace",
            "AWS::ServiceDiscovery::Service",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::StepFunctions::Activity",
            "AWS::StepFunctions::StateMachine",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::WebACL",
            "AWS::WorkSpaces::ConnectionAlias",
            "AWS::WorkSpaces::Workspace",
            "AWS::XRay::EncryptionConfig",
        ]
    ] = Field(default=None, alias="resourceType")
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    resource_deletion_time: Optional[datetime] = Field(
        default=None, alias="resourceDeletionTime"
    )


class ResourceEvaluationModel(BaseModel):
    resource_evaluation_id: Optional[str] = Field(
        default=None, alias="ResourceEvaluationId"
    )
    evaluation_mode: Optional[Literal["DETECTIVE", "PROACTIVE"]] = Field(
        default=None, alias="EvaluationMode"
    )
    evaluation_start_timestamp: Optional[datetime] = Field(
        default=None, alias="EvaluationStartTimestamp"
    )


class ListStoredQueriesRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class StoredQueryMetadataModel(BaseModel):
    query_id: str = Field(alias="QueryId")
    query_arn: str = Field(alias="QueryArn")
    query_name: str = Field(alias="QueryName")
    description: Optional[str] = Field(default=None, alias="Description")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class TagModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="Key")
    value: Optional[str] = Field(default=None, alias="Value")


class OrganizationCustomPolicyRuleMetadataNoPolicyModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="Description")
    organization_config_rule_trigger_types: Optional[
        List[
            Literal[
                "ConfigurationItemChangeNotification",
                "OversizedConfigurationItemChangeNotification",
            ]
        ]
    ] = Field(default=None, alias="OrganizationConfigRuleTriggerTypes")
    input_parameters: Optional[str] = Field(default=None, alias="InputParameters")
    maximum_execution_frequency: Optional[
        Literal[
            "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    ] = Field(default=None, alias="MaximumExecutionFrequency")
    resource_types_scope: Optional[List[str]] = Field(
        default=None, alias="ResourceTypesScope"
    )
    resource_id_scope: Optional[str] = Field(default=None, alias="ResourceIdScope")
    tag_key_scope: Optional[str] = Field(default=None, alias="TagKeyScope")
    tag_value_scope: Optional[str] = Field(default=None, alias="TagValueScope")
    policy_runtime: Optional[str] = Field(default=None, alias="PolicyRuntime")
    debug_log_delivery_accounts: Optional[List[str]] = Field(
        default=None, alias="DebugLogDeliveryAccounts"
    )


class OrganizationCustomRuleMetadataModel(BaseModel):
    lambda_function_arn: str = Field(alias="LambdaFunctionArn")
    organization_config_rule_trigger_types: List[
        Literal[
            "ConfigurationItemChangeNotification",
            "OversizedConfigurationItemChangeNotification",
            "ScheduledNotification",
        ]
    ] = Field(alias="OrganizationConfigRuleTriggerTypes")
    description: Optional[str] = Field(default=None, alias="Description")
    input_parameters: Optional[str] = Field(default=None, alias="InputParameters")
    maximum_execution_frequency: Optional[
        Literal[
            "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    ] = Field(default=None, alias="MaximumExecutionFrequency")
    resource_types_scope: Optional[List[str]] = Field(
        default=None, alias="ResourceTypesScope"
    )
    resource_id_scope: Optional[str] = Field(default=None, alias="ResourceIdScope")
    tag_key_scope: Optional[str] = Field(default=None, alias="TagKeyScope")
    tag_value_scope: Optional[str] = Field(default=None, alias="TagValueScope")


class OrganizationManagedRuleMetadataModel(BaseModel):
    rule_identifier: str = Field(alias="RuleIdentifier")
    description: Optional[str] = Field(default=None, alias="Description")
    input_parameters: Optional[str] = Field(default=None, alias="InputParameters")
    maximum_execution_frequency: Optional[
        Literal[
            "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    ] = Field(default=None, alias="MaximumExecutionFrequency")
    resource_types_scope: Optional[List[str]] = Field(
        default=None, alias="ResourceTypesScope"
    )
    resource_id_scope: Optional[str] = Field(default=None, alias="ResourceIdScope")
    tag_key_scope: Optional[str] = Field(default=None, alias="TagKeyScope")
    tag_value_scope: Optional[str] = Field(default=None, alias="TagValueScope")


class OrganizationCustomPolicyRuleMetadataModel(BaseModel):
    policy_runtime: str = Field(alias="PolicyRuntime")
    policy_text: str = Field(alias="PolicyText")
    description: Optional[str] = Field(default=None, alias="Description")
    organization_config_rule_trigger_types: Optional[
        Sequence[
            Literal[
                "ConfigurationItemChangeNotification",
                "OversizedConfigurationItemChangeNotification",
            ]
        ]
    ] = Field(default=None, alias="OrganizationConfigRuleTriggerTypes")
    input_parameters: Optional[str] = Field(default=None, alias="InputParameters")
    maximum_execution_frequency: Optional[
        Literal[
            "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    ] = Field(default=None, alias="MaximumExecutionFrequency")
    resource_types_scope: Optional[Sequence[str]] = Field(
        default=None, alias="ResourceTypesScope"
    )
    resource_id_scope: Optional[str] = Field(default=None, alias="ResourceIdScope")
    tag_key_scope: Optional[str] = Field(default=None, alias="TagKeyScope")
    tag_value_scope: Optional[str] = Field(default=None, alias="TagValueScope")
    debug_log_delivery_accounts: Optional[Sequence[str]] = Field(
        default=None, alias="DebugLogDeliveryAccounts"
    )


class PutResourceConfigRequestModel(BaseModel):
    resource_type: str = Field(alias="ResourceType")
    schema_version_id: str = Field(alias="SchemaVersionId")
    resource_id: str = Field(alias="ResourceId")
    configuration: str = Field(alias="Configuration")
    resource_name: Optional[str] = Field(default=None, alias="ResourceName")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class PutRetentionConfigurationRequestModel(BaseModel):
    retention_period_in_days: int = Field(alias="RetentionPeriodInDays")


class RemediationExecutionStepModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    state: Optional[Literal["FAILED", "PENDING", "SUCCEEDED"]] = Field(
        default=None, alias="State"
    )
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    stop_time: Optional[datetime] = Field(default=None, alias="StopTime")


class ResourceValueModel(BaseModel):
    value: Literal["RESOURCE_ID"] = Field(alias="Value")


class StaticValueModel(BaseModel):
    values: List[str] = Field(alias="Values")


class TimeWindowModel(BaseModel):
    start_time: Optional[Union[datetime, str]] = Field(default=None, alias="StartTime")
    end_time: Optional[Union[datetime, str]] = Field(default=None, alias="EndTime")


class SelectAggregateResourceConfigRequestModel(BaseModel):
    expression: str = Field(alias="Expression")
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    limit: Optional[int] = Field(default=None, alias="Limit")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SelectResourceConfigRequestModel(BaseModel):
    expression: str = Field(alias="Expression")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SourceDetailModel(BaseModel):
    event_source: Optional[Literal["aws.config"]] = Field(
        default=None, alias="EventSource"
    )
    message_type: Optional[
        Literal[
            "ConfigurationItemChangeNotification",
            "ConfigurationSnapshotDeliveryCompleted",
            "OversizedConfigurationItemChangeNotification",
            "ScheduledNotification",
        ]
    ] = Field(default=None, alias="MessageType")
    maximum_execution_frequency: Optional[
        Literal[
            "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    ] = Field(default=None, alias="MaximumExecutionFrequency")


class StartConfigRulesEvaluationRequestModel(BaseModel):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )


class StartConfigurationRecorderRequestModel(BaseModel):
    configuration_recorder_name: str = Field(alias="ConfigurationRecorderName")


class StopConfigurationRecorderRequestModel(BaseModel):
    configuration_recorder_name: str = Field(alias="ConfigurationRecorderName")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class AggregateComplianceByConformancePackModel(BaseModel):
    conformance_pack_name: Optional[str] = Field(
        default=None, alias="ConformancePackName"
    )
    compliance: Optional[AggregateConformancePackComplianceModel] = Field(
        default=None, alias="Compliance"
    )
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class AggregateConformancePackComplianceSummaryModel(BaseModel):
    compliance_summary: Optional[AggregateConformancePackComplianceCountModel] = Field(
        default=None, alias="ComplianceSummary"
    )
    group_name: Optional[str] = Field(default=None, alias="GroupName")


class DescribeAggregateComplianceByConformancePacksRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    filters: Optional[AggregateConformancePackComplianceFiltersModel] = Field(
        default=None, alias="Filters"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetAggregateConformancePackComplianceSummaryRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    filters: Optional[AggregateConformancePackComplianceSummaryFiltersModel] = Field(
        default=None, alias="Filters"
    )
    group_by_key: Optional[Literal["ACCOUNT_ID", "AWS_REGION"]] = Field(
        default=None, alias="GroupByKey"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class BatchGetAggregateResourceConfigRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    resource_identifiers: Sequence[AggregateResourceIdentifierModel] = Field(
        alias="ResourceIdentifiers"
    )


class GetAggregateResourceConfigRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    resource_identifier: AggregateResourceIdentifierModel = Field(
        alias="ResourceIdentifier"
    )


class BatchGetAggregateResourceConfigResponseModel(BaseModel):
    base_configuration_items: List[BaseConfigurationItemModel] = Field(
        alias="BaseConfigurationItems"
    )
    unprocessed_resource_identifiers: List[AggregateResourceIdentifierModel] = Field(
        alias="UnprocessedResourceIdentifiers"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeliverConfigSnapshotResponseModel(BaseModel):
    config_snapshot_id: str = Field(alias="configSnapshotId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAggregationAuthorizationsResponseModel(BaseModel):
    aggregation_authorizations: List[AggregationAuthorizationModel] = Field(
        alias="AggregationAuthorizations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationAggregatorSourcesStatusResponseModel(BaseModel):
    aggregated_source_status_list: List[AggregatedSourceStatusModel] = Field(
        alias="AggregatedSourceStatusList"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCustomRulePolicyResponseModel(BaseModel):
    policy_text: str = Field(alias="PolicyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOrganizationCustomRulePolicyResponseModel(BaseModel):
    policy_text: str = Field(alias="PolicyText")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAggregateDiscoveredResourcesResponseModel(BaseModel):
    resource_identifiers: List[AggregateResourceIdentifierModel] = Field(
        alias="ResourceIdentifiers"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAggregationAuthorizationResponseModel(BaseModel):
    aggregation_authorization: AggregationAuthorizationModel = Field(
        alias="AggregationAuthorization"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutConformancePackResponseModel(BaseModel):
    conformance_pack_arn: str = Field(alias="ConformancePackArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutOrganizationConfigRuleResponseModel(BaseModel):
    organization_config_rule_arn: str = Field(alias="OrganizationConfigRuleArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutOrganizationConformancePackResponseModel(BaseModel):
    organization_conformance_pack_arn: str = Field(
        alias="OrganizationConformancePackArn"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutStoredQueryResponseModel(BaseModel):
    query_arn: str = Field(alias="QueryArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartResourceEvaluationResponseModel(BaseModel):
    resource_evaluation_id: str = Field(alias="ResourceEvaluationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BatchGetResourceConfigRequestModel(BaseModel):
    resource_keys: Sequence[ResourceKeyModel] = Field(alias="resourceKeys")


class BatchGetResourceConfigResponseModel(BaseModel):
    base_configuration_items: List[BaseConfigurationItemModel] = Field(
        alias="baseConfigurationItems"
    )
    unprocessed_resource_keys: List[ResourceKeyModel] = Field(
        alias="unprocessedResourceKeys"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRemediationExecutionStatusRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_keys: Optional[Sequence[ResourceKeyModel]] = Field(
        default=None, alias="ResourceKeys"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class StartRemediationExecutionRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_keys: Sequence[ResourceKeyModel] = Field(alias="ResourceKeys")


class StartRemediationExecutionResponseModel(BaseModel):
    failure_message: str = Field(alias="FailureMessage")
    failed_items: List[ResourceKeyModel] = Field(alias="FailedItems")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComplianceSummaryModel(BaseModel):
    compliant_resource_count: Optional[ComplianceContributorCountModel] = Field(
        default=None, alias="CompliantResourceCount"
    )
    non_compliant_resource_count: Optional[ComplianceContributorCountModel] = Field(
        default=None, alias="NonCompliantResourceCount"
    )
    compliance_summary_timestamp: Optional[datetime] = Field(
        default=None, alias="ComplianceSummaryTimestamp"
    )


class ComplianceModel(BaseModel):
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
    ] = Field(default=None, alias="ComplianceType")
    compliance_contributor_count: Optional[ComplianceContributorCountModel] = Field(
        default=None, alias="ComplianceContributorCount"
    )


class DescribeAggregateComplianceByConfigRulesRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    filters: Optional[ConfigRuleComplianceFiltersModel] = Field(
        default=None, alias="Filters"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetAggregateConfigRuleComplianceSummaryRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    filters: Optional[ConfigRuleComplianceSummaryFiltersModel] = Field(
        default=None, alias="Filters"
    )
    group_by_key: Optional[Literal["ACCOUNT_ID", "AWS_REGION"]] = Field(
        default=None, alias="GroupByKey"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeConfigRuleEvaluationStatusResponseModel(BaseModel):
    config_rules_evaluation_status: List[ConfigRuleEvaluationStatusModel] = Field(
        alias="ConfigRulesEvaluationStatus"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeliveryChannelModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    s3_bucket_name: Optional[str] = Field(default=None, alias="s3BucketName")
    s3_key_prefix: Optional[str] = Field(default=None, alias="s3KeyPrefix")
    s3_kms_key_arn: Optional[str] = Field(default=None, alias="s3KmsKeyArn")
    sns_topic_arn: Optional[str] = Field(default=None, alias="snsTopicARN")
    config_snapshot_delivery_properties: Optional[
        ConfigSnapshotDeliveryPropertiesModel
    ] = Field(default=None, alias="configSnapshotDeliveryProperties")


class DeliveryChannelStatusModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    config_snapshot_delivery_info: Optional[ConfigExportDeliveryInfoModel] = Field(
        default=None, alias="configSnapshotDeliveryInfo"
    )
    config_history_delivery_info: Optional[ConfigExportDeliveryInfoModel] = Field(
        default=None, alias="configHistoryDeliveryInfo"
    )
    config_stream_delivery_info: Optional[ConfigStreamDeliveryInfoModel] = Field(
        default=None, alias="configStreamDeliveryInfo"
    )


class ConfigurationAggregatorModel(BaseModel):
    configuration_aggregator_name: Optional[str] = Field(
        default=None, alias="ConfigurationAggregatorName"
    )
    configuration_aggregator_arn: Optional[str] = Field(
        default=None, alias="ConfigurationAggregatorArn"
    )
    account_aggregation_sources: Optional[List[AccountAggregationSourceModel]] = Field(
        default=None, alias="AccountAggregationSources"
    )
    organization_aggregation_source: Optional[
        OrganizationAggregationSourceModel
    ] = Field(default=None, alias="OrganizationAggregationSource")
    creation_time: Optional[datetime] = Field(default=None, alias="CreationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")


class ConfigurationItemModel(BaseModel):
    version: Optional[str] = Field(default=None, alias="version")
    account_id: Optional[str] = Field(default=None, alias="accountId")
    configuration_item_capture_time: Optional[datetime] = Field(
        default=None, alias="configurationItemCaptureTime"
    )
    configuration_item_status: Optional[
        Literal[
            "OK",
            "ResourceDeleted",
            "ResourceDeletedNotRecorded",
            "ResourceDiscovered",
            "ResourceNotRecorded",
        ]
    ] = Field(default=None, alias="configurationItemStatus")
    configuration_state_id: Optional[str] = Field(
        default=None, alias="configurationStateId"
    )
    configuration_item_md5_hash: Optional[str] = Field(
        default=None, alias="configurationItemMD5Hash"
    )
    arn: Optional[str] = Field(default=None, alias="arn")
    resource_type: Optional[
        Literal[
            "AWS::ACM::Certificate",
            "AWS::AccessAnalyzer::Analyzer",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::ApiGatewayV2::Stage",
            "AWS::AppConfig::Application",
            "AWS::AppSync::GraphQLApi",
            "AWS::Athena::DataCatalog",
            "AWS::Athena::WorkGroup",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::Backup::BackupPlan",
            "AWS::Backup::BackupSelection",
            "AWS::Backup::BackupVault",
            "AWS::Backup::RecoveryPoint",
            "AWS::Batch::ComputeEnvironment",
            "AWS::Batch::JobQueue",
            "AWS::CloudFormation::Stack",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::CloudTrail::Trail",
            "AWS::CloudWatch::Alarm",
            "AWS::CodeBuild::Project",
            "AWS::CodeDeploy::Application",
            "AWS::CodeDeploy::DeploymentConfig",
            "AWS::CodeDeploy::DeploymentGroup",
            "AWS::CodePipeline::Pipeline",
            "AWS::Config::ConformancePackCompliance",
            "AWS::Config::ResourceCompliance",
            "AWS::DMS::Certificate",
            "AWS::DMS::EventSubscription",
            "AWS::DMS::ReplicationSubnetGroup",
            "AWS::DataSync::LocationEFS",
            "AWS::DataSync::LocationFSxLustre",
            "AWS::DataSync::LocationNFS",
            "AWS::DataSync::LocationS3",
            "AWS::DataSync::LocationSMB",
            "AWS::DataSync::Task",
            "AWS::Detective::Graph",
            "AWS::DynamoDB::Table",
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::FlowLog",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::LaunchTemplate",
            "AWS::EC2::NatGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::EC2::TransitGateway",
            "AWS::EC2::TransitGatewayAttachment",
            "AWS::EC2::TransitGatewayRouteTable",
            "AWS::EC2::VPC",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::Volume",
            "AWS::ECR::PublicRepository",
            "AWS::ECR::Repository",
            "AWS::ECS::Cluster",
            "AWS::ECS::Service",
            "AWS::ECS::TaskDefinition",
            "AWS::EFS::AccessPoint",
            "AWS::EFS::FileSystem",
            "AWS::EKS::Cluster",
            "AWS::EKS::FargateProfile",
            "AWS::EMR::SecurityConfiguration",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::ElasticLoadBalancingV2::Listener",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::Elasticsearch::Domain",
            "AWS::GlobalAccelerator::Accelerator",
            "AWS::GlobalAccelerator::EndpointGroup",
            "AWS::GlobalAccelerator::Listener",
            "AWS::Glue::Job",
            "AWS::GuardDuty::Detector",
            "AWS::GuardDuty::IPSet",
            "AWS::GuardDuty::ThreatIntelSet",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::KMS::Key",
            "AWS::Kinesis::Stream",
            "AWS::Kinesis::StreamConsumer",
            "AWS::Lambda::Function",
            "AWS::MSK::Cluster",
            "AWS::NetworkFirewall::Firewall",
            "AWS::NetworkFirewall::FirewallPolicy",
            "AWS::NetworkFirewall::RuleGroup",
            "AWS::OpenSearch::Domain",
            "AWS::QLDB::Ledger",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::EventSubscription",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::Route53::HostedZone",
            "AWS::Route53Resolver::ResolverEndpoint",
            "AWS::Route53Resolver::ResolverRule",
            "AWS::Route53Resolver::ResolverRuleAssociation",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::S3::Bucket",
            "AWS::SES::ConfigurationSet",
            "AWS::SES::ContactList",
            "AWS::SNS::Topic",
            "AWS::SQS::Queue",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::FileData",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::SSM::PatchCompliance",
            "AWS::SageMaker::CodeRepository",
            "AWS::SageMaker::Model",
            "AWS::SageMaker::NotebookInstanceLifecycleConfig",
            "AWS::SageMaker::Workteam",
            "AWS::SecretsManager::Secret",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::ServiceDiscovery::PublicDnsNamespace",
            "AWS::ServiceDiscovery::Service",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::StepFunctions::Activity",
            "AWS::StepFunctions::StateMachine",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::WebACL",
            "AWS::WorkSpaces::ConnectionAlias",
            "AWS::WorkSpaces::Workspace",
            "AWS::XRay::EncryptionConfig",
        ]
    ] = Field(default=None, alias="resourceType")
    resource_id: Optional[str] = Field(default=None, alias="resourceId")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    aws_region: Optional[str] = Field(default=None, alias="awsRegion")
    availability_zone: Optional[str] = Field(default=None, alias="availabilityZone")
    resource_creation_time: Optional[datetime] = Field(
        default=None, alias="resourceCreationTime"
    )
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")
    related_events: Optional[List[str]] = Field(default=None, alias="relatedEvents")
    relationships: Optional[List[RelationshipModel]] = Field(
        default=None, alias="relationships"
    )
    configuration: Optional[str] = Field(default=None, alias="configuration")
    supplementary_configuration: Optional[Dict[str, str]] = Field(
        default=None, alias="supplementaryConfiguration"
    )


class DescribeConfigurationRecorderStatusResponseModel(BaseModel):
    configuration_recorders_status: List[ConfigurationRecorderStatusModel] = Field(
        alias="ConfigurationRecordersStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ConfigurationRecorderModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    role_arn: Optional[str] = Field(default=None, alias="roleARN")
    recording_group: Optional[RecordingGroupModel] = Field(
        default=None, alias="recordingGroup"
    )


class DescribeConformancePackComplianceRequestModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    filters: Optional[ConformancePackComplianceFiltersModel] = Field(
        default=None, alias="Filters"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListConformancePackComplianceScoresResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    conformance_pack_compliance_scores: List[
        ConformancePackComplianceScoreModel
    ] = Field(alias="ConformancePackComplianceScores")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListConformancePackComplianceScoresRequestModel(BaseModel):
    filters: Optional[ConformancePackComplianceScoresFiltersModel] = Field(
        default=None, alias="Filters"
    )
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="SortOrder"
    )
    sort_by: Optional[Literal["SCORE"]] = Field(default=None, alias="SortBy")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetConformancePackComplianceSummaryResponseModel(BaseModel):
    conformance_pack_compliance_summary_list: List[
        ConformancePackComplianceSummaryModel
    ] = Field(alias="ConformancePackComplianceSummaryList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class OrganizationConformancePackModel(BaseModel):
    organization_conformance_pack_name: str = Field(
        alias="OrganizationConformancePackName"
    )
    organization_conformance_pack_arn: str = Field(
        alias="OrganizationConformancePackArn"
    )
    last_update_time: datetime = Field(alias="LastUpdateTime")
    delivery_s3_bucket: Optional[str] = Field(default=None, alias="DeliveryS3Bucket")
    delivery_s3_key_prefix: Optional[str] = Field(
        default=None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: Optional[
        List[ConformancePackInputParameterModel]
    ] = Field(default=None, alias="ConformancePackInputParameters")
    excluded_accounts: Optional[List[str]] = Field(
        default=None, alias="ExcludedAccounts"
    )


class PutOrganizationConformancePackRequestModel(BaseModel):
    organization_conformance_pack_name: str = Field(
        alias="OrganizationConformancePackName"
    )
    template_s3_uri: Optional[str] = Field(default=None, alias="TemplateS3Uri")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    delivery_s3_bucket: Optional[str] = Field(default=None, alias="DeliveryS3Bucket")
    delivery_s3_key_prefix: Optional[str] = Field(
        default=None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: Optional[
        Sequence[ConformancePackInputParameterModel]
    ] = Field(default=None, alias="ConformancePackInputParameters")
    excluded_accounts: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedAccounts"
    )


class ConformancePackDetailModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    conformance_pack_arn: str = Field(alias="ConformancePackArn")
    conformance_pack_id: str = Field(alias="ConformancePackId")
    delivery_s3_bucket: Optional[str] = Field(default=None, alias="DeliveryS3Bucket")
    delivery_s3_key_prefix: Optional[str] = Field(
        default=None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: Optional[
        List[ConformancePackInputParameterModel]
    ] = Field(default=None, alias="ConformancePackInputParameters")
    last_update_requested_time: Optional[datetime] = Field(
        default=None, alias="LastUpdateRequestedTime"
    )
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    template_s_s_mdocument_details: Optional[TemplateSSMDocumentDetailsModel] = Field(
        default=None, alias="TemplateSSMDocumentDetails"
    )


class PutConformancePackRequestModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    template_s3_uri: Optional[str] = Field(default=None, alias="TemplateS3Uri")
    template_body: Optional[str] = Field(default=None, alias="TemplateBody")
    delivery_s3_bucket: Optional[str] = Field(default=None, alias="DeliveryS3Bucket")
    delivery_s3_key_prefix: Optional[str] = Field(
        default=None, alias="DeliveryS3KeyPrefix"
    )
    conformance_pack_input_parameters: Optional[
        Sequence[ConformancePackInputParameterModel]
    ] = Field(default=None, alias="ConformancePackInputParameters")
    template_s_s_mdocument_details: Optional[TemplateSSMDocumentDetailsModel] = Field(
        default=None, alias="TemplateSSMDocumentDetails"
    )


class GetConformancePackComplianceDetailsRequestModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    filters: Optional[ConformancePackEvaluationFiltersModel] = Field(
        default=None, alias="Filters"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeConformancePackComplianceResponseModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    conformance_pack_rule_compliance_list: List[
        ConformancePackRuleComplianceModel
    ] = Field(alias="ConformancePackRuleComplianceList")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConformancePackStatusResponseModel(BaseModel):
    conformance_pack_status_details: List[ConformancePackStatusDetailModel] = Field(
        alias="ConformancePackStatusDetails"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRemediationExceptionsRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_keys: Sequence[RemediationExceptionResourceKeyModel] = Field(
        alias="ResourceKeys"
    )


class DescribeRemediationExceptionsRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_keys: Optional[Sequence[RemediationExceptionResourceKeyModel]] = Field(
        default=None, alias="ResourceKeys"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class FailedDeleteRemediationExceptionsBatchModel(BaseModel):
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")
    failed_items: Optional[List[RemediationExceptionResourceKeyModel]] = Field(
        default=None, alias="FailedItems"
    )


class PutRemediationExceptionsRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_keys: Sequence[RemediationExceptionResourceKeyModel] = Field(
        alias="ResourceKeys"
    )
    message: Optional[str] = Field(default=None, alias="Message")
    expiration_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="ExpirationTime"
    )


class DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateModel(
    BaseModel
):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    filters: Optional[ConfigRuleComplianceFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateModel(
    BaseModel
):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    filters: Optional[AggregateConformancePackComplianceFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeAggregationAuthorizationsRequestDescribeAggregationAuthorizationsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateModel(
    BaseModel
):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateModel(
    BaseModel
):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateModel(
    BaseModel
):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateModel(
    BaseModel
):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    update_status: Optional[
        Sequence[Literal["FAILED", "OUTDATED", "SUCCEEDED"]]
    ] = Field(default=None, alias="UpdateStatus")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateModel(
    BaseModel
):
    configuration_aggregator_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigurationAggregatorNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateModel(
    BaseModel
):
    conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConformancePackNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConformancePacksRequestDescribeConformancePacksPaginateModel(BaseModel):
    conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConformancePackNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateModel(
    BaseModel
):
    organization_config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConfigRuleNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateModel(
    BaseModel
):
    organization_config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConfigRuleNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateModel(
    BaseModel
):
    organization_conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConformancePackNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateModel(
    BaseModel
):
    organization_conformance_pack_names: Optional[Sequence[str]] = Field(
        default=None, alias="OrganizationConformancePackNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateModel(
    BaseModel
):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateModel(
    BaseModel
):
    config_rule_name: str = Field(alias="ConfigRuleName")
    resource_keys: Optional[Sequence[ResourceKeyModel]] = Field(
        default=None, alias="ResourceKeys"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateModel(
    BaseModel
):
    retention_configuration_names: Optional[Sequence[str]] = Field(
        default=None, alias="RetentionConfigurationNames"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateModel(
    BaseModel
):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    config_rule_name: str = Field(alias="ConfigRuleName")
    account_id: str = Field(alias="AccountId")
    aws_region: str = Field(alias="AwsRegion")
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
    ] = Field(default=None, alias="ComplianceType")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateModel(
    BaseModel
):
    config_rule_name: str = Field(alias="ConfigRuleName")
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateModel(
    BaseModel
):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    compliance_types: Optional[
        Sequence[
            Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
        ]
    ] = Field(default=None, alias="ComplianceTypes")
    resource_evaluation_id: Optional[str] = Field(
        default=None, alias="ResourceEvaluationId"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateModel(
    BaseModel
):
    conformance_pack_names: Sequence[str] = Field(alias="ConformancePackNames")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateModel(BaseModel):
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="resourceType")
    resource_id: str = Field(alias="resourceId")
    later_time: Optional[Union[datetime, str]] = Field(default=None, alias="laterTime")
    earlier_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="earlierTime"
    )
    chronological_order: Optional[Literal["Forward", "Reverse"]] = Field(
        default=None, alias="chronologicalOrder"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateModel(BaseModel):
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="resourceType")
    resource_ids: Optional[Sequence[str]] = Field(default=None, alias="resourceIds")
    resource_name: Optional[str] = Field(default=None, alias="resourceName")
    include_deleted_resources: Optional[bool] = Field(
        default=None, alias="includeDeletedResources"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTagsForResourceRequestListTagsForResourcePaginateModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateModel(
    BaseModel
):
    expression: str = Field(alias="Expression")
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SelectResourceConfigRequestSelectResourceConfigPaginateModel(BaseModel):
    expression: str = Field(alias="Expression")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConfigRulesRequestDescribeConfigRulesPaginateModel(BaseModel):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    filters: Optional[DescribeConfigRulesFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeConfigRulesRequestModel(BaseModel):
    config_rule_names: Optional[Sequence[str]] = Field(
        default=None, alias="ConfigRuleNames"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    filters: Optional[DescribeConfigRulesFiltersModel] = Field(
        default=None, alias="Filters"
    )


class DescribeOrganizationConfigRuleStatusesResponseModel(BaseModel):
    organization_config_rule_statuses: List[OrganizationConfigRuleStatusModel] = Field(
        alias="OrganizationConfigRuleStatuses"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationConformancePackStatusesResponseModel(BaseModel):
    organization_conformance_pack_statuses: List[
        OrganizationConformancePackStatusModel
    ] = Field(alias="OrganizationConformancePackStatuses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribePendingAggregationRequestsResponseModel(BaseModel):
    pending_aggregation_requests: List[PendingAggregationRequestModel] = Field(
        alias="PendingAggregationRequests"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRemediationExceptionsResponseModel(BaseModel):
    remediation_exceptions: List[RemediationExceptionModel] = Field(
        alias="RemediationExceptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailedRemediationExceptionBatchModel(BaseModel):
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")
    failed_items: Optional[List[RemediationExceptionModel]] = Field(
        default=None, alias="FailedItems"
    )


class DescribeRetentionConfigurationsResponseModel(BaseModel):
    retention_configurations: List[RetentionConfigurationModel] = Field(
        alias="RetentionConfigurations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRetentionConfigurationResponseModel(BaseModel):
    retention_configuration: RetentionConfigurationModel = Field(
        alias="RetentionConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class EvaluationResultIdentifierModel(BaseModel):
    evaluation_result_qualifier: Optional[EvaluationResultQualifierModel] = Field(
        default=None, alias="EvaluationResultQualifier"
    )
    ordering_timestamp: Optional[datetime] = Field(
        default=None, alias="OrderingTimestamp"
    )
    resource_evaluation_id: Optional[str] = Field(
        default=None, alias="ResourceEvaluationId"
    )


class PutEvaluationsRequestModel(BaseModel):
    result_token: str = Field(alias="ResultToken")
    evaluations: Optional[Sequence[EvaluationModel]] = Field(
        default=None, alias="Evaluations"
    )
    test_mode: Optional[bool] = Field(default=None, alias="TestMode")


class PutEvaluationsResponseModel(BaseModel):
    failed_evaluations: List[EvaluationModel] = Field(alias="FailedEvaluations")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecutionControlsModel(BaseModel):
    ssm_controls: Optional[SsmControlsModel] = Field(default=None, alias="SsmControls")


class PutExternalEvaluationRequestModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    external_evaluation: ExternalEvaluationModel = Field(alias="ExternalEvaluation")


class QueryInfoModel(BaseModel):
    select_fields: Optional[List[FieldInfoModel]] = Field(
        default=None, alias="SelectFields"
    )


class GetAggregateDiscoveredResourceCountsRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    filters: Optional[ResourceCountFiltersModel] = Field(default=None, alias="Filters")
    group_by_key: Optional[
        Literal["ACCOUNT_ID", "AWS_REGION", "RESOURCE_TYPE"]
    ] = Field(default=None, alias="GroupByKey")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetAggregateDiscoveredResourceCountsResponseModel(BaseModel):
    total_discovered_resources: int = Field(alias="TotalDiscoveredResources")
    group_by_key: str = Field(alias="GroupByKey")
    grouped_resource_counts: List[GroupedResourceCountModel] = Field(
        alias="GroupedResourceCounts"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDiscoveredResourceCountsResponseModel(BaseModel):
    total_discovered_resources: int = Field(alias="totalDiscoveredResources")
    resource_counts: List[ResourceCountModel] = Field(alias="resourceCounts")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateModel(
    BaseModel
):
    organization_config_rule_name: str = Field(alias="OrganizationConfigRuleName")
    filters: Optional[StatusDetailFiltersModel] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetOrganizationConfigRuleDetailedStatusRequestModel(BaseModel):
    organization_config_rule_name: str = Field(alias="OrganizationConfigRuleName")
    filters: Optional[StatusDetailFiltersModel] = Field(default=None, alias="Filters")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetOrganizationConfigRuleDetailedStatusResponseModel(BaseModel):
    organization_config_rule_detailed_status: List[MemberAccountStatusModel] = Field(
        alias="OrganizationConfigRuleDetailedStatus"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateModel(
    BaseModel
):
    organization_conformance_pack_name: str = Field(
        alias="OrganizationConformancePackName"
    )
    filters: Optional[OrganizationResourceDetailedStatusFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class GetOrganizationConformancePackDetailedStatusRequestModel(BaseModel):
    organization_conformance_pack_name: str = Field(
        alias="OrganizationConformancePackName"
    )
    filters: Optional[OrganizationResourceDetailedStatusFiltersModel] = Field(
        default=None, alias="Filters"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetOrganizationConformancePackDetailedStatusResponseModel(BaseModel):
    organization_conformance_pack_detailed_statuses: List[
        OrganizationConformancePackDetailedStatusModel
    ] = Field(alias="OrganizationConformancePackDetailedStatuses")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceEvaluationSummaryResponseModel(BaseModel):
    resource_evaluation_id: str = Field(alias="ResourceEvaluationId")
    evaluation_mode: Literal["DETECTIVE", "PROACTIVE"] = Field(alias="EvaluationMode")
    evaluation_status: EvaluationStatusModel = Field(alias="EvaluationStatus")
    evaluation_start_timestamp: datetime = Field(alias="EvaluationStartTimestamp")
    compliance: Literal[
        "COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"
    ] = Field(alias="Compliance")
    evaluation_context: EvaluationContextModel = Field(alias="EvaluationContext")
    resource_details: ResourceDetailsModel = Field(alias="ResourceDetails")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartResourceEvaluationRequestModel(BaseModel):
    resource_details: ResourceDetailsModel = Field(alias="ResourceDetails")
    evaluation_mode: Literal["DETECTIVE", "PROACTIVE"] = Field(alias="EvaluationMode")
    evaluation_context: Optional[EvaluationContextModel] = Field(
        default=None, alias="EvaluationContext"
    )
    evaluation_timeout: Optional[int] = Field(default=None, alias="EvaluationTimeout")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")


class GetStoredQueryResponseModel(BaseModel):
    stored_query: StoredQueryModel = Field(alias="StoredQuery")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateModel(
    BaseModel
):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="ResourceType")
    filters: Optional[ResourceFiltersModel] = Field(default=None, alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListAggregateDiscoveredResourcesRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    resource_type: Literal[
        "AWS::ACM::Certificate",
        "AWS::AccessAnalyzer::Analyzer",
        "AWS::ApiGateway::RestApi",
        "AWS::ApiGateway::Stage",
        "AWS::ApiGatewayV2::Api",
        "AWS::ApiGatewayV2::Stage",
        "AWS::AppConfig::Application",
        "AWS::AppSync::GraphQLApi",
        "AWS::Athena::DataCatalog",
        "AWS::Athena::WorkGroup",
        "AWS::AutoScaling::AutoScalingGroup",
        "AWS::AutoScaling::LaunchConfiguration",
        "AWS::AutoScaling::ScalingPolicy",
        "AWS::AutoScaling::ScheduledAction",
        "AWS::Backup::BackupPlan",
        "AWS::Backup::BackupSelection",
        "AWS::Backup::BackupVault",
        "AWS::Backup::RecoveryPoint",
        "AWS::Batch::ComputeEnvironment",
        "AWS::Batch::JobQueue",
        "AWS::CloudFormation::Stack",
        "AWS::CloudFront::Distribution",
        "AWS::CloudFront::StreamingDistribution",
        "AWS::CloudTrail::Trail",
        "AWS::CloudWatch::Alarm",
        "AWS::CodeBuild::Project",
        "AWS::CodeDeploy::Application",
        "AWS::CodeDeploy::DeploymentConfig",
        "AWS::CodeDeploy::DeploymentGroup",
        "AWS::CodePipeline::Pipeline",
        "AWS::Config::ConformancePackCompliance",
        "AWS::Config::ResourceCompliance",
        "AWS::DMS::Certificate",
        "AWS::DMS::EventSubscription",
        "AWS::DMS::ReplicationSubnetGroup",
        "AWS::DataSync::LocationEFS",
        "AWS::DataSync::LocationFSxLustre",
        "AWS::DataSync::LocationNFS",
        "AWS::DataSync::LocationS3",
        "AWS::DataSync::LocationSMB",
        "AWS::DataSync::Task",
        "AWS::Detective::Graph",
        "AWS::DynamoDB::Table",
        "AWS::EC2::CustomerGateway",
        "AWS::EC2::EIP",
        "AWS::EC2::EgressOnlyInternetGateway",
        "AWS::EC2::FlowLog",
        "AWS::EC2::Host",
        "AWS::EC2::Instance",
        "AWS::EC2::InternetGateway",
        "AWS::EC2::LaunchTemplate",
        "AWS::EC2::NatGateway",
        "AWS::EC2::NetworkAcl",
        "AWS::EC2::NetworkInsightsAccessScopeAnalysis",
        "AWS::EC2::NetworkInterface",
        "AWS::EC2::RegisteredHAInstance",
        "AWS::EC2::RouteTable",
        "AWS::EC2::SecurityGroup",
        "AWS::EC2::Subnet",
        "AWS::EC2::TransitGateway",
        "AWS::EC2::TransitGatewayAttachment",
        "AWS::EC2::TransitGatewayRouteTable",
        "AWS::EC2::VPC",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::VPCEndpointService",
        "AWS::EC2::VPCPeeringConnection",
        "AWS::EC2::VPNConnection",
        "AWS::EC2::VPNGateway",
        "AWS::EC2::Volume",
        "AWS::ECR::PublicRepository",
        "AWS::ECR::Repository",
        "AWS::ECS::Cluster",
        "AWS::ECS::Service",
        "AWS::ECS::TaskDefinition",
        "AWS::EFS::AccessPoint",
        "AWS::EFS::FileSystem",
        "AWS::EKS::Cluster",
        "AWS::EKS::FargateProfile",
        "AWS::EMR::SecurityConfiguration",
        "AWS::ElasticBeanstalk::Application",
        "AWS::ElasticBeanstalk::ApplicationVersion",
        "AWS::ElasticBeanstalk::Environment",
        "AWS::ElasticLoadBalancing::LoadBalancer",
        "AWS::ElasticLoadBalancingV2::Listener",
        "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "AWS::Elasticsearch::Domain",
        "AWS::GlobalAccelerator::Accelerator",
        "AWS::GlobalAccelerator::EndpointGroup",
        "AWS::GlobalAccelerator::Listener",
        "AWS::Glue::Job",
        "AWS::GuardDuty::Detector",
        "AWS::GuardDuty::IPSet",
        "AWS::GuardDuty::ThreatIntelSet",
        "AWS::IAM::Group",
        "AWS::IAM::Policy",
        "AWS::IAM::Role",
        "AWS::IAM::User",
        "AWS::KMS::Key",
        "AWS::Kinesis::Stream",
        "AWS::Kinesis::StreamConsumer",
        "AWS::Lambda::Function",
        "AWS::MSK::Cluster",
        "AWS::NetworkFirewall::Firewall",
        "AWS::NetworkFirewall::FirewallPolicy",
        "AWS::NetworkFirewall::RuleGroup",
        "AWS::OpenSearch::Domain",
        "AWS::QLDB::Ledger",
        "AWS::RDS::DBCluster",
        "AWS::RDS::DBClusterSnapshot",
        "AWS::RDS::DBInstance",
        "AWS::RDS::DBSecurityGroup",
        "AWS::RDS::DBSnapshot",
        "AWS::RDS::DBSubnetGroup",
        "AWS::RDS::EventSubscription",
        "AWS::Redshift::Cluster",
        "AWS::Redshift::ClusterParameterGroup",
        "AWS::Redshift::ClusterSecurityGroup",
        "AWS::Redshift::ClusterSnapshot",
        "AWS::Redshift::ClusterSubnetGroup",
        "AWS::Redshift::EventSubscription",
        "AWS::Route53::HostedZone",
        "AWS::Route53Resolver::ResolverEndpoint",
        "AWS::Route53Resolver::ResolverRule",
        "AWS::Route53Resolver::ResolverRuleAssociation",
        "AWS::S3::AccountPublicAccessBlock",
        "AWS::S3::Bucket",
        "AWS::SES::ConfigurationSet",
        "AWS::SES::ContactList",
        "AWS::SNS::Topic",
        "AWS::SQS::Queue",
        "AWS::SSM::AssociationCompliance",
        "AWS::SSM::FileData",
        "AWS::SSM::ManagedInstanceInventory",
        "AWS::SSM::PatchCompliance",
        "AWS::SageMaker::CodeRepository",
        "AWS::SageMaker::Model",
        "AWS::SageMaker::NotebookInstanceLifecycleConfig",
        "AWS::SageMaker::Workteam",
        "AWS::SecretsManager::Secret",
        "AWS::ServiceCatalog::CloudFormationProduct",
        "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
        "AWS::ServiceCatalog::Portfolio",
        "AWS::ServiceDiscovery::PublicDnsNamespace",
        "AWS::ServiceDiscovery::Service",
        "AWS::Shield::Protection",
        "AWS::ShieldRegional::Protection",
        "AWS::StepFunctions::Activity",
        "AWS::StepFunctions::StateMachine",
        "AWS::WAF::RateBasedRule",
        "AWS::WAF::Rule",
        "AWS::WAF::RuleGroup",
        "AWS::WAF::WebACL",
        "AWS::WAFRegional::RateBasedRule",
        "AWS::WAFRegional::Rule",
        "AWS::WAFRegional::RuleGroup",
        "AWS::WAFRegional::WebACL",
        "AWS::WAFv2::IPSet",
        "AWS::WAFv2::ManagedRuleSet",
        "AWS::WAFv2::RegexPatternSet",
        "AWS::WAFv2::RuleGroup",
        "AWS::WAFv2::WebACL",
        "AWS::WorkSpaces::ConnectionAlias",
        "AWS::WorkSpaces::Workspace",
        "AWS::XRay::EncryptionConfig",
    ] = Field(alias="ResourceType")
    filters: Optional[ResourceFiltersModel] = Field(default=None, alias="Filters")
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListDiscoveredResourcesResponseModel(BaseModel):
    resource_identifiers: List[ResourceIdentifierModel] = Field(
        alias="resourceIdentifiers"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourceEvaluationsResponseModel(BaseModel):
    resource_evaluations: List[ResourceEvaluationModel] = Field(
        alias="ResourceEvaluations"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStoredQueriesResponseModel(BaseModel):
    stored_query_metadata: List[StoredQueryMetadataModel] = Field(
        alias="StoredQueryMetadata"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutAggregationAuthorizationRequestModel(BaseModel):
    authorized_account_id: str = Field(alias="AuthorizedAccountId")
    authorized_aws_region: str = Field(alias="AuthorizedAwsRegion")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class PutConfigurationAggregatorRequestModel(BaseModel):
    configuration_aggregator_name: str = Field(alias="ConfigurationAggregatorName")
    account_aggregation_sources: Optional[
        Sequence[AccountAggregationSourceModel]
    ] = Field(default=None, alias="AccountAggregationSources")
    organization_aggregation_source: Optional[
        OrganizationAggregationSourceModel
    ] = Field(default=None, alias="OrganizationAggregationSource")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class PutStoredQueryRequestModel(BaseModel):
    stored_query: StoredQueryModel = Field(alias="StoredQuery")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class OrganizationConfigRuleModel(BaseModel):
    organization_config_rule_name: str = Field(alias="OrganizationConfigRuleName")
    organization_config_rule_arn: str = Field(alias="OrganizationConfigRuleArn")
    organization_managed_rule_metadata: Optional[
        OrganizationManagedRuleMetadataModel
    ] = Field(default=None, alias="OrganizationManagedRuleMetadata")
    organization_custom_rule_metadata: Optional[
        OrganizationCustomRuleMetadataModel
    ] = Field(default=None, alias="OrganizationCustomRuleMetadata")
    excluded_accounts: Optional[List[str]] = Field(
        default=None, alias="ExcludedAccounts"
    )
    last_update_time: Optional[datetime] = Field(default=None, alias="LastUpdateTime")
    organization_custom_policy_rule_metadata: Optional[
        OrganizationCustomPolicyRuleMetadataNoPolicyModel
    ] = Field(default=None, alias="OrganizationCustomPolicyRuleMetadata")


class PutOrganizationConfigRuleRequestModel(BaseModel):
    organization_config_rule_name: str = Field(alias="OrganizationConfigRuleName")
    organization_managed_rule_metadata: Optional[
        OrganizationManagedRuleMetadataModel
    ] = Field(default=None, alias="OrganizationManagedRuleMetadata")
    organization_custom_rule_metadata: Optional[
        OrganizationCustomRuleMetadataModel
    ] = Field(default=None, alias="OrganizationCustomRuleMetadata")
    excluded_accounts: Optional[Sequence[str]] = Field(
        default=None, alias="ExcludedAccounts"
    )
    organization_custom_policy_rule_metadata: Optional[
        OrganizationCustomPolicyRuleMetadataModel
    ] = Field(default=None, alias="OrganizationCustomPolicyRuleMetadata")


class RemediationExecutionStatusModel(BaseModel):
    resource_key: Optional[ResourceKeyModel] = Field(default=None, alias="ResourceKey")
    state: Optional[Literal["FAILED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]] = Field(
        default=None, alias="State"
    )
    step_details: Optional[List[RemediationExecutionStepModel]] = Field(
        default=None, alias="StepDetails"
    )
    invocation_time: Optional[datetime] = Field(default=None, alias="InvocationTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class RemediationParameterValueModel(BaseModel):
    resource_value: Optional[ResourceValueModel] = Field(
        default=None, alias="ResourceValue"
    )
    static_value: Optional[StaticValueModel] = Field(default=None, alias="StaticValue")


class ResourceEvaluationFiltersModel(BaseModel):
    evaluation_mode: Optional[Literal["DETECTIVE", "PROACTIVE"]] = Field(
        default=None, alias="EvaluationMode"
    )
    time_window: Optional[TimeWindowModel] = Field(default=None, alias="TimeWindow")
    evaluation_context_identifier: Optional[str] = Field(
        default=None, alias="EvaluationContextIdentifier"
    )


class SourceModel(BaseModel):
    owner: Literal["AWS", "CUSTOM_LAMBDA", "CUSTOM_POLICY"] = Field(alias="Owner")
    source_identifier: Optional[str] = Field(default=None, alias="SourceIdentifier")
    source_details: Optional[List[SourceDetailModel]] = Field(
        default=None, alias="SourceDetails"
    )
    custom_policy_details: Optional[CustomPolicyDetailsModel] = Field(
        default=None, alias="CustomPolicyDetails"
    )


class DescribeAggregateComplianceByConformancePacksResponseModel(BaseModel):
    aggregate_compliance_by_conformance_packs: List[
        AggregateComplianceByConformancePackModel
    ] = Field(alias="AggregateComplianceByConformancePacks")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAggregateConformancePackComplianceSummaryResponseModel(BaseModel):
    aggregate_conformance_pack_compliance_summaries: List[
        AggregateConformancePackComplianceSummaryModel
    ] = Field(alias="AggregateConformancePackComplianceSummaries")
    group_by_key: str = Field(alias="GroupByKey")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AggregateComplianceCountModel(BaseModel):
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    compliance_summary: Optional[ComplianceSummaryModel] = Field(
        default=None, alias="ComplianceSummary"
    )


class ComplianceSummaryByResourceTypeModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    compliance_summary: Optional[ComplianceSummaryModel] = Field(
        default=None, alias="ComplianceSummary"
    )


class GetComplianceSummaryByConfigRuleResponseModel(BaseModel):
    compliance_summary: ComplianceSummaryModel = Field(alias="ComplianceSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AggregateComplianceByConfigRuleModel(BaseModel):
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")
    compliance: Optional[ComplianceModel] = Field(default=None, alias="Compliance")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class ComplianceByConfigRuleModel(BaseModel):
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")
    compliance: Optional[ComplianceModel] = Field(default=None, alias="Compliance")


class ComplianceByResourceModel(BaseModel):
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    compliance: Optional[ComplianceModel] = Field(default=None, alias="Compliance")


class DescribeDeliveryChannelsResponseModel(BaseModel):
    delivery_channels: List[DeliveryChannelModel] = Field(alias="DeliveryChannels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutDeliveryChannelRequestModel(BaseModel):
    delivery_channel: DeliveryChannelModel = Field(alias="DeliveryChannel")


class DescribeDeliveryChannelStatusResponseModel(BaseModel):
    delivery_channels_status: List[DeliveryChannelStatusModel] = Field(
        alias="DeliveryChannelsStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationAggregatorsResponseModel(BaseModel):
    configuration_aggregators: List[ConfigurationAggregatorModel] = Field(
        alias="ConfigurationAggregators"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutConfigurationAggregatorResponseModel(BaseModel):
    configuration_aggregator: ConfigurationAggregatorModel = Field(
        alias="ConfigurationAggregator"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAggregateResourceConfigResponseModel(BaseModel):
    configuration_item: ConfigurationItemModel = Field(alias="ConfigurationItem")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetResourceConfigHistoryResponseModel(BaseModel):
    configuration_items: List[ConfigurationItemModel] = Field(
        alias="configurationItems"
    )
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConfigurationRecordersResponseModel(BaseModel):
    configuration_recorders: List[ConfigurationRecorderModel] = Field(
        alias="ConfigurationRecorders"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutConfigurationRecorderRequestModel(BaseModel):
    configuration_recorder: ConfigurationRecorderModel = Field(
        alias="ConfigurationRecorder"
    )


class DescribeOrganizationConformancePacksResponseModel(BaseModel):
    organization_conformance_packs: List[OrganizationConformancePackModel] = Field(
        alias="OrganizationConformancePacks"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeConformancePacksResponseModel(BaseModel):
    conformance_pack_details: List[ConformancePackDetailModel] = Field(
        alias="ConformancePackDetails"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRemediationExceptionsResponseModel(BaseModel):
    failed_batches: List[FailedDeleteRemediationExceptionsBatchModel] = Field(
        alias="FailedBatches"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutRemediationExceptionsResponseModel(BaseModel):
    failed_batches: List[FailedRemediationExceptionBatchModel] = Field(
        alias="FailedBatches"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class AggregateEvaluationResultModel(BaseModel):
    evaluation_result_identifier: Optional[EvaluationResultIdentifierModel] = Field(
        default=None, alias="EvaluationResultIdentifier"
    )
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
    ] = Field(default=None, alias="ComplianceType")
    result_recorded_time: Optional[datetime] = Field(
        default=None, alias="ResultRecordedTime"
    )
    config_rule_invoked_time: Optional[datetime] = Field(
        default=None, alias="ConfigRuleInvokedTime"
    )
    annotation: Optional[str] = Field(default=None, alias="Annotation")
    account_id: Optional[str] = Field(default=None, alias="AccountId")
    aws_region: Optional[str] = Field(default=None, alias="AwsRegion")


class ConformancePackEvaluationResultModel(BaseModel):
    compliance_type: Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"] = Field(
        alias="ComplianceType"
    )
    evaluation_result_identifier: EvaluationResultIdentifierModel = Field(
        alias="EvaluationResultIdentifier"
    )
    config_rule_invoked_time: datetime = Field(alias="ConfigRuleInvokedTime")
    result_recorded_time: datetime = Field(alias="ResultRecordedTime")
    annotation: Optional[str] = Field(default=None, alias="Annotation")


class EvaluationResultModel(BaseModel):
    evaluation_result_identifier: Optional[EvaluationResultIdentifierModel] = Field(
        default=None, alias="EvaluationResultIdentifier"
    )
    compliance_type: Optional[
        Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
    ] = Field(default=None, alias="ComplianceType")
    result_recorded_time: Optional[datetime] = Field(
        default=None, alias="ResultRecordedTime"
    )
    config_rule_invoked_time: Optional[datetime] = Field(
        default=None, alias="ConfigRuleInvokedTime"
    )
    annotation: Optional[str] = Field(default=None, alias="Annotation")
    result_token: Optional[str] = Field(default=None, alias="ResultToken")


class SelectAggregateResourceConfigResponseModel(BaseModel):
    results: List[str] = Field(alias="Results")
    query_info: QueryInfoModel = Field(alias="QueryInfo")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SelectResourceConfigResponseModel(BaseModel):
    results: List[str] = Field(alias="Results")
    query_info: QueryInfoModel = Field(alias="QueryInfo")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeOrganizationConfigRulesResponseModel(BaseModel):
    organization_config_rules: List[OrganizationConfigRuleModel] = Field(
        alias="OrganizationConfigRules"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRemediationExecutionStatusResponseModel(BaseModel):
    remediation_execution_statuses: List[RemediationExecutionStatusModel] = Field(
        alias="RemediationExecutionStatuses"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RemediationConfigurationModel(BaseModel):
    config_rule_name: str = Field(alias="ConfigRuleName")
    target_type: Literal["SSM_DOCUMENT"] = Field(alias="TargetType")
    target_id: str = Field(alias="TargetId")
    target_version: Optional[str] = Field(default=None, alias="TargetVersion")
    parameters: Optional[Dict[str, RemediationParameterValueModel]] = Field(
        default=None, alias="Parameters"
    )
    resource_type: Optional[str] = Field(default=None, alias="ResourceType")
    automatic: Optional[bool] = Field(default=None, alias="Automatic")
    execution_controls: Optional[ExecutionControlsModel] = Field(
        default=None, alias="ExecutionControls"
    )
    maximum_automatic_attempts: Optional[int] = Field(
        default=None, alias="MaximumAutomaticAttempts"
    )
    retry_attempt_seconds: Optional[int] = Field(
        default=None, alias="RetryAttemptSeconds"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_by_service: Optional[str] = Field(default=None, alias="CreatedByService")


class ListResourceEvaluationsRequestListResourceEvaluationsPaginateModel(BaseModel):
    filters: Optional[ResourceEvaluationFiltersModel] = Field(
        default=None, alias="Filters"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListResourceEvaluationsRequestModel(BaseModel):
    filters: Optional[ResourceEvaluationFiltersModel] = Field(
        default=None, alias="Filters"
    )
    limit: Optional[int] = Field(default=None, alias="Limit")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ConfigRuleModel(BaseModel):
    source: SourceModel = Field(alias="Source")
    config_rule_name: Optional[str] = Field(default=None, alias="ConfigRuleName")
    config_rule_arn: Optional[str] = Field(default=None, alias="ConfigRuleArn")
    config_rule_id: Optional[str] = Field(default=None, alias="ConfigRuleId")
    description: Optional[str] = Field(default=None, alias="Description")
    scope: Optional[ScopeModel] = Field(default=None, alias="Scope")
    input_parameters: Optional[str] = Field(default=None, alias="InputParameters")
    maximum_execution_frequency: Optional[
        Literal[
            "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
        ]
    ] = Field(default=None, alias="MaximumExecutionFrequency")
    config_rule_state: Optional[
        Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"]
    ] = Field(default=None, alias="ConfigRuleState")
    created_by: Optional[str] = Field(default=None, alias="CreatedBy")
    evaluation_modes: Optional[List[EvaluationModeConfigurationModel]] = Field(
        default=None, alias="EvaluationModes"
    )


class GetAggregateConfigRuleComplianceSummaryResponseModel(BaseModel):
    group_by_key: str = Field(alias="GroupByKey")
    aggregate_compliance_counts: List[AggregateComplianceCountModel] = Field(
        alias="AggregateComplianceCounts"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComplianceSummaryByResourceTypeResponseModel(BaseModel):
    compliance_summaries_by_resource_type: List[
        ComplianceSummaryByResourceTypeModel
    ] = Field(alias="ComplianceSummariesByResourceType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAggregateComplianceByConfigRulesResponseModel(BaseModel):
    aggregate_compliance_by_config_rules: List[
        AggregateComplianceByConfigRuleModel
    ] = Field(alias="AggregateComplianceByConfigRules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComplianceByConfigRuleResponseModel(BaseModel):
    compliance_by_config_rules: List[ComplianceByConfigRuleModel] = Field(
        alias="ComplianceByConfigRules"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeComplianceByResourceResponseModel(BaseModel):
    compliance_by_resources: List[ComplianceByResourceModel] = Field(
        alias="ComplianceByResources"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetAggregateComplianceDetailsByConfigRuleResponseModel(BaseModel):
    aggregate_evaluation_results: List[AggregateEvaluationResultModel] = Field(
        alias="AggregateEvaluationResults"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetConformancePackComplianceDetailsResponseModel(BaseModel):
    conformance_pack_name: str = Field(alias="ConformancePackName")
    conformance_pack_rule_evaluation_results: List[
        ConformancePackEvaluationResultModel
    ] = Field(alias="ConformancePackRuleEvaluationResults")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComplianceDetailsByConfigRuleResponseModel(BaseModel):
    evaluation_results: List[EvaluationResultModel] = Field(alias="EvaluationResults")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComplianceDetailsByResourceResponseModel(BaseModel):
    evaluation_results: List[EvaluationResultModel] = Field(alias="EvaluationResults")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRemediationConfigurationsResponseModel(BaseModel):
    remediation_configurations: List[RemediationConfigurationModel] = Field(
        alias="RemediationConfigurations"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FailedRemediationBatchModel(BaseModel):
    failure_message: Optional[str] = Field(default=None, alias="FailureMessage")
    failed_items: Optional[List[RemediationConfigurationModel]] = Field(
        default=None, alias="FailedItems"
    )


class PutRemediationConfigurationsRequestModel(BaseModel):
    remediation_configurations: Sequence[RemediationConfigurationModel] = Field(
        alias="RemediationConfigurations"
    )


class DescribeConfigRulesResponseModel(BaseModel):
    config_rules: List[ConfigRuleModel] = Field(alias="ConfigRules")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutConfigRuleRequestModel(BaseModel):
    config_rule: ConfigRuleModel = Field(alias="ConfigRule")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class PutRemediationConfigurationsResponseModel(BaseModel):
    failed_batches: List[FailedRemediationBatchModel] = Field(alias="FailedBatches")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
