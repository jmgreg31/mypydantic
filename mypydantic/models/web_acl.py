# pylint: disable = no-name-in-module
# generated by datamodel-codegen:
#   filename:  web_acl_snake.json

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

from mypydantic.helpers.parsers import convert_all_keys
from mypydantic.models.empty import Empty


class ImmunityTimeProperty(BaseModel):
    immunity_time: int


class CaptchaConfig(BaseModel):
    immunity_time_property: ImmunityTimeProperty


class ChallengeConfig(BaseModel):
    immunity_time_property: ImmunityTimeProperty


class String(BaseModel):
    content: str
    content_type: str


class CustomResponseBodies(BaseModel):
    string: String


class InsertHeader(BaseModel):
    name: str
    value: str


class CustomRequestHandling(BaseModel):
    insert_headers: List[InsertHeader]


class Allow(BaseModel):
    custom_request_handling: Optional[CustomRequestHandling] = None


class Block(BaseModel):
    custom_response: Optional[CustomResponse] = None


class DefaultAction(BaseModel):
    allow: Union[Allow, Empty, None]
    block: Union[Block, Empty, None]


class Action(BaseModel):
    allow: Union[Allow, Empty, None]
    block: Union[Block, Empty, None]
    captcha: Optional[Captcha] = None
    challenge: Optional[Challenge] = None
    count: Optional[Count] = None


class ResponseHeader(BaseModel):
    name: str
    value: str


class CustomResponse(BaseModel):
    custom_response_body_key: str
    response_code: int
    response_headers: List[ResponseHeader]


class Captcha(BaseModel):
    custom_request_handling: CustomRequestHandling


class Challenge(BaseModel):
    custom_request_handling: CustomRequestHandling


class Count(BaseModel):
    custom_request_handling: CustomRequestHandling


class OverrideAction(BaseModel):
    count: Count
    none: Dict[str, Any]


class RuleLabel(BaseModel):
    name: str


class AndStatement(BaseModel):
    statements: List[str]


class Body(BaseModel):
    oversize_handling: str


class MatchCookies(BaseModel):
    all: Dict[str, Any]
    excluded_cookies: List[str]
    included_cookies: List[str]


class Cookies(BaseModel):
    match_pattern: MatchCookies
    match_scope: str
    oversize_handling: str


class MatchHeaders(BaseModel):
    all: Dict[str, Any]
    excluded_headers: List[str]
    included_headers: List[str]


class Headers(BaseModel):
    match_pattern: MatchHeaders
    match_scope: str
    oversize_handling: str


class MatchPaths(BaseModel):
    all: Dict[str, Any]
    included_paths: List[str]


class JsonBody(BaseModel):
    invalid_fallback_behavior: str
    match_pattern: MatchPaths
    match_scope: str
    oversize_handling: str


class SingleHeader(BaseModel):
    name: str


class SingleQueryArgument(BaseModel):
    name: str


class FieldToMatch(BaseModel):
    method: Dict[str, Any]
    all_query_arguments: Optional[Dict[str, Any]] = None
    body: Optional[Body] = None
    cookies: Optional[Cookies] = None
    headers: Optional[Headers] = None
    json_body: Optional[JsonBody] = None
    query_string: Optional[Dict[str, Any]] = None
    single_header: Optional[SingleHeader] = None
    single_query_argument: Optional[SingleQueryArgument] = None
    uri_path: Optional[Dict[str, Any]] = None


class TextTransformation(BaseModel):
    priority: int
    type: str


class ByteMatchStatement(BaseModel):
    field_to_match: FieldToMatch
    positional_constraint: str
    search_string: str
    text_transformations: List[TextTransformation]


class ForwardedIpConfig(BaseModel):
    fallback_behavior: str
    header_name: str


class GeoMatchStatement(BaseModel):
    country_codes: List[str]
    forwarded_ip_config: ForwardedIpConfig


class IpSetForwardedIpConfig(BaseModel):
    fallback_behavior: str
    header_name: str
    position: str


class IpSetReferenceStatement(BaseModel):
    arn: Optional[str] = None
    ip_set_forwarded_ip_config: Optional[IpSetForwardedIpConfig] = None


class LabelMatchStatement(BaseModel):
    key: str
    scope: str


class ExcludedRule(BaseModel):
    name: str


class PasswordField(BaseModel):
    identifier: str


class UsernameField(BaseModel):
    identifier: str


class RequestInspection(BaseModel):
    password_field: PasswordField
    payload_type: str
    username_field: UsernameField


class BodyContains(BaseModel):
    failure_strings: List[str]
    success_strings: List[str]


class Header(BaseModel):
    failure_values: List[str]
    name: str
    success_values: List[str]


class Json(BaseModel):
    failure_values: List[str]
    identifier: str
    success_values: List[str]


class StatusCode(BaseModel):
    failure_codes: List[int]
    success_codes: List[int]


class ResponseInspection(BaseModel):
    body_contains: BodyContains
    header: Header
    json_: Json = Field(..., alias="json")
    status_code: StatusCode


class AwsManagedRulesAtpRuleSet(BaseModel):
    login_path: str
    request_inspection: RequestInspection
    response_inspection: ResponseInspection


class AwsManagedRulesBotControlRuleSet(BaseModel):
    inspection_level: str


class ManagedRuleGroupConfig(BaseModel):
    aws_managed_rules_atp_rule_set: AwsManagedRulesAtpRuleSet
    aws_managed_rules_bot_control_rule_set: AwsManagedRulesBotControlRuleSet
    login_path: str
    password_field: PasswordField
    payload_type: str
    username_field: UsernameField


class ActionToUse(BaseModel):
    allow: Allow
    block: Block
    captcha: Captcha
    challenge: Challenge
    count: Count


class RuleActionOverride(BaseModel):
    action_to_use: ActionToUse
    name: str


class ManagedRuleGroupStatement(BaseModel):
    excluded_rules: List[ExcludedRule]
    managed_rule_group_configs: List[ManagedRuleGroupConfig]
    name: str
    rule_action_overrides: List[RuleActionOverride]
    scope_down_statement: str
    vendor_name: str
    version: str


class NotStatement(BaseModel):
    statement: str


class OrStatement(BaseModel):
    statements: List[str]


class RateBasedStatement(BaseModel):
    aggregate_key_type: str
    forwarded_ip_config: ForwardedIpConfig
    limit: int
    scope_down_statement: str


class RegexMatchStatement(BaseModel):
    field_to_match: FieldToMatch
    regex_string: str
    text_transformations: List[TextTransformation]


class RegexPatternSetReferenceStatement(BaseModel):
    arn: str
    field_to_match: FieldToMatch
    text_transformations: List[TextTransformation]


class RuleGroupReferenceStatement(BaseModel):
    arn: str
    excluded_rules: List[ExcludedRule]
    rule_action_overrides: List[RuleActionOverride]


class SizeConstraintStatement(BaseModel):
    comparison_operator: str
    field_to_match: FieldToMatch
    size: int
    text_transformations: List[TextTransformation]


class SqliMatchStatement(BaseModel):
    field_to_match: FieldToMatch
    sensitivity_level: str
    text_transformations: List[TextTransformation]


class XssMatchStatement(BaseModel):
    field_to_match: FieldToMatch
    text_transformations: List[TextTransformation]


class Statement(BaseModel):
    and_statement: Optional[AndStatement] = None
    byte_match_statement: Optional[ByteMatchStatement] = None
    geo_match_statement: Optional[GeoMatchStatement] = None
    ip_set_reference_statement: Optional[IpSetReferenceStatement] = None
    label_match_statement: Optional[LabelMatchStatement] = None
    managed_rule_group_statement: Optional[ManagedRuleGroupStatement] = None
    not_statement: Optional[NotStatement] = None
    or_statement: Optional[OrStatement] = None
    rate_based_statement: Optional[RateBasedStatement] = None
    regex_match_statement: Optional[RegexMatchStatement] = None
    regex_pattern_set_reference_statement: Optional[
        RegexPatternSetReferenceStatement
    ] = None
    rule_group_reference_statement: Optional[RuleGroupReferenceStatement] = None
    size_constraint_statement: Optional[SizeConstraintStatement] = None
    sqli_match_statement: Optional[SqliMatchStatement] = None
    xss_match_statement: Optional[XssMatchStatement] = None


class VisibilityConfig(BaseModel):
    cloud_watch_metrics_enabled: bool
    metric_name: str
    sampled_requests_enabled: bool


class Rule(BaseModel):
    name: str
    priority: int
    action: Action
    visibility_config: VisibilityConfig
    statement: Statement
    captcha_config: Optional[CaptchaConfig] = None
    challenge_config: Optional[ChallengeConfig] = None
    override_action: Optional[OverrideAction] = None
    rule_labels: Optional[List[RuleLabel]] = None


class Tag(BaseModel):
    key: str
    value: str


class WebACL(BaseModel):
    name: str
    id: Optional[str] = None
    arn: Optional[str] = None
    scope: Optional[str] = None
    lock_token: Optional[str] = None
    capacity: Optional[int] = None
    default_action: Optional[DefaultAction] = None
    visibility_config: Optional[VisibilityConfig] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    rules: Optional[List[Rule]] = None
    label_namespace: Optional[str] = None
    managed_by_firewall_manager: Optional[bool] = None
    pre_process_firewall_manager_rule_groups: Optional[dict] = None
    post_process_firewall_manager_rule_groups: Optional[dict] = None
    captcha_config: Optional[CaptchaConfig] = None
    challenge_config: Optional[ChallengeConfig] = None
    custom_response_bodies: Optional[CustomResponseBodies] = None
    token_domains: Optional[List[str]] = None

    def create_object(self) -> dict:
        _create_object = {
            "Name": self.name,
            "Scope": self.scope,
            "Description": self.description,
            "Tags": self.tags,
        }
        if self.default_action is not None:
            _create_object.update(
                {
                    "DefaultAction": convert_all_keys(
                        self.default_action.dict(exclude_none=True), "camel"
                    )
                }
            )
        if self.default_action is not None:
            _create_object.update(
                {
                    "DefaultAction": convert_all_keys(
                        self.default_action.dict(exclude_none=True), "camel"
                    )
                }
            )
        if self.visibility_config is not None:
            _create_object.update(
                {
                    "VisibilityConfig": convert_all_keys(
                        self.visibility_config.dict(exclude_none=True), "camel"
                    )
                }
            )
        if self.rules is not None:
            _rules = []
            for rule in self.rules:
                parsed_rule = convert_all_keys(rule.dict(exclude_none=True), "camel")
                _rules.append(parsed_rule)
            _create_object.update({"Rules": _rules})
        if self.custom_response_bodies is not None:
            _create_object.update(
                {
                    "CustomResponseBodies": convert_all_keys(
                        self.custom_response_bodies.dict(exclude_none=True), "camel"
                    )
                }
            )
        if self.captcha_config is not None:
            _create_object.update(
                {
                    "CaptchaConfig": convert_all_keys(
                        self.captcha_config.dict(exclude_none=True), "camel"
                    )
                }
            )
        return _create_object
