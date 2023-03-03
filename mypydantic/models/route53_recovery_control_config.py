# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class RuleConfigModel(BaseModel):
    inverted: bool = Field(alias="Inverted")
    threshold: int = Field(alias="Threshold")
    type: Literal["AND", "ATLEAST", "OR"] = Field(alias="Type")


class AssertionRuleUpdateModel(BaseModel):
    name: str = Field(alias="Name")
    safety_rule_arn: str = Field(alias="SafetyRuleArn")
    wait_period_ms: int = Field(alias="WaitPeriodMs")


class ClusterEndpointModel(BaseModel):
    endpoint: Optional[str] = Field(default=None, alias="Endpoint")
    region: Optional[str] = Field(default=None, alias="Region")


class ControlPanelModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    control_panel_arn: Optional[str] = Field(default=None, alias="ControlPanelArn")
    default_control_panel: Optional[bool] = Field(
        default=None, alias="DefaultControlPanel"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    routing_control_count: Optional[int] = Field(
        default=None, alias="RoutingControlCount"
    )
    status: Optional[Literal["DEPLOYED", "PENDING", "PENDING_DELETION"]] = Field(
        default=None, alias="Status"
    )


class CreateClusterRequestModel(BaseModel):
    cluster_name: str = Field(alias="ClusterName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateControlPanelRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    control_panel_name: str = Field(alias="ControlPanelName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateRoutingControlRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    routing_control_name: str = Field(alias="RoutingControlName")
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    control_panel_arn: Optional[str] = Field(default=None, alias="ControlPanelArn")


class RoutingControlModel(BaseModel):
    control_panel_arn: Optional[str] = Field(default=None, alias="ControlPanelArn")
    name: Optional[str] = Field(default=None, alias="Name")
    routing_control_arn: Optional[str] = Field(default=None, alias="RoutingControlArn")
    status: Optional[Literal["DEPLOYED", "PENDING", "PENDING_DELETION"]] = Field(
        default=None, alias="Status"
    )


class DeleteClusterRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")


class DeleteControlPanelRequestModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")


class DeleteRoutingControlRequestModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")


class DeleteSafetyRuleRequestModel(BaseModel):
    safety_rule_arn: str = Field(alias="SafetyRuleArn")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeClusterRequestModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")


class DescribeControlPanelRequestModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")


class DescribeRoutingControlRequestModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")


class DescribeSafetyRuleRequestModel(BaseModel):
    safety_rule_arn: str = Field(alias="SafetyRuleArn")


class GatingRuleUpdateModel(BaseModel):
    name: str = Field(alias="Name")
    safety_rule_arn: str = Field(alias="SafetyRuleArn")
    wait_period_ms: int = Field(alias="WaitPeriodMs")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAssociatedRoute53HealthChecksRequestModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListClustersRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListControlPanelsRequestModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListRoutingControlsRequestModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListSafetyRulesRequestModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateControlPanelRequestModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    control_panel_name: str = Field(alias="ControlPanelName")


class UpdateRoutingControlRequestModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    routing_control_name: str = Field(alias="RoutingControlName")


class AssertionRuleModel(BaseModel):
    asserted_controls: List[str] = Field(alias="AssertedControls")
    control_panel_arn: str = Field(alias="ControlPanelArn")
    name: str = Field(alias="Name")
    rule_config: RuleConfigModel = Field(alias="RuleConfig")
    safety_rule_arn: str = Field(alias="SafetyRuleArn")
    status: Literal["DEPLOYED", "PENDING", "PENDING_DELETION"] = Field(alias="Status")
    wait_period_ms: int = Field(alias="WaitPeriodMs")


class GatingRuleModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    gating_controls: List[str] = Field(alias="GatingControls")
    name: str = Field(alias="Name")
    rule_config: RuleConfigModel = Field(alias="RuleConfig")
    safety_rule_arn: str = Field(alias="SafetyRuleArn")
    status: Literal["DEPLOYED", "PENDING", "PENDING_DELETION"] = Field(alias="Status")
    target_controls: List[str] = Field(alias="TargetControls")
    wait_period_ms: int = Field(alias="WaitPeriodMs")


class NewAssertionRuleModel(BaseModel):
    asserted_controls: Sequence[str] = Field(alias="AssertedControls")
    control_panel_arn: str = Field(alias="ControlPanelArn")
    name: str = Field(alias="Name")
    rule_config: RuleConfigModel = Field(alias="RuleConfig")
    wait_period_ms: int = Field(alias="WaitPeriodMs")


class NewGatingRuleModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    gating_controls: Sequence[str] = Field(alias="GatingControls")
    name: str = Field(alias="Name")
    rule_config: RuleConfigModel = Field(alias="RuleConfig")
    target_controls: Sequence[str] = Field(alias="TargetControls")
    wait_period_ms: int = Field(alias="WaitPeriodMs")


class ClusterModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    cluster_endpoints: Optional[List[ClusterEndpointModel]] = Field(
        default=None, alias="ClusterEndpoints"
    )
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[Literal["DEPLOYED", "PENDING", "PENDING_DELETION"]] = Field(
        default=None, alias="Status"
    )


class CreateControlPanelResponseModel(BaseModel):
    control_panel: ControlPanelModel = Field(alias="ControlPanel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeControlPanelResponseModel(BaseModel):
    control_panel: ControlPanelModel = Field(alias="ControlPanel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAssociatedRoute53HealthChecksResponseModel(BaseModel):
    health_check_ids: List[str] = Field(alias="HealthCheckIds")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListControlPanelsResponseModel(BaseModel):
    control_panels: List[ControlPanelModel] = Field(alias="ControlPanels")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateControlPanelResponseModel(BaseModel):
    control_panel: ControlPanelModel = Field(alias="ControlPanel")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRoutingControlResponseModel(BaseModel):
    routing_control: RoutingControlModel = Field(alias="RoutingControl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeRoutingControlResponseModel(BaseModel):
    routing_control: RoutingControlModel = Field(alias="RoutingControl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRoutingControlsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    routing_controls: List[RoutingControlModel] = Field(alias="RoutingControls")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRoutingControlResponseModel(BaseModel):
    routing_control: RoutingControlModel = Field(alias="RoutingControl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClusterRequestClusterCreatedWaitModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeClusterRequestClusterDeletedWaitModel(BaseModel):
    cluster_arn: str = Field(alias="ClusterArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeControlPanelRequestControlPanelCreatedWaitModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeControlPanelRequestControlPanelDeletedWaitModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeRoutingControlRequestRoutingControlCreatedWaitModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeRoutingControlRequestRoutingControlDeletedWaitModel(BaseModel):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class UpdateSafetyRuleRequestModel(BaseModel):
    assertion_rule_update: Optional[AssertionRuleUpdateModel] = Field(
        default=None, alias="AssertionRuleUpdate"
    )
    gating_rule_update: Optional[GatingRuleUpdateModel] = Field(
        default=None, alias="GatingRuleUpdate"
    )


class ListAssociatedRoute53HealthChecksRequestListAssociatedRoute53HealthChecksPaginateModel(
    BaseModel
):
    routing_control_arn: str = Field(alias="RoutingControlArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListClustersRequestListClustersPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListControlPanelsRequestListControlPanelsPaginateModel(BaseModel):
    cluster_arn: Optional[str] = Field(default=None, alias="ClusterArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListRoutingControlsRequestListRoutingControlsPaginateModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListSafetyRulesRequestListSafetyRulesPaginateModel(BaseModel):
    control_panel_arn: str = Field(alias="ControlPanelArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class CreateSafetyRuleResponseModel(BaseModel):
    assertion_rule: AssertionRuleModel = Field(alias="AssertionRule")
    gating_rule: GatingRuleModel = Field(alias="GatingRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSafetyRuleResponseModel(BaseModel):
    assertion_rule: AssertionRuleModel = Field(alias="AssertionRule")
    gating_rule: GatingRuleModel = Field(alias="GatingRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuleModel(BaseModel):
    as_s_ertion: Optional[AssertionRuleModel] = Field(default=None, alias="ASSERTION")
    gating: Optional[GatingRuleModel] = Field(default=None, alias="GATING")


class UpdateSafetyRuleResponseModel(BaseModel):
    assertion_rule: AssertionRuleModel = Field(alias="AssertionRule")
    gating_rule: GatingRuleModel = Field(alias="GatingRule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateSafetyRuleRequestModel(BaseModel):
    assertion_rule: Optional[NewAssertionRuleModel] = Field(
        default=None, alias="AssertionRule"
    )
    client_token: Optional[str] = Field(default=None, alias="ClientToken")
    gating_rule: Optional[NewGatingRuleModel] = Field(default=None, alias="GatingRule")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeClusterResponseModel(BaseModel):
    cluster: ClusterModel = Field(alias="Cluster")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListClustersResponseModel(BaseModel):
    clusters: List[ClusterModel] = Field(alias="Clusters")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSafetyRulesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    safety_rules: List[RuleModel] = Field(alias="SafetyRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
