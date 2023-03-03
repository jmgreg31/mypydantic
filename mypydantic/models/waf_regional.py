# Model Generated: Thu Mar  2 21:56:24 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ExcludedRuleModel(BaseModel):
    rule_id: str = Field(alias="RuleId")


class WafActionModel(BaseModel):
    type: Literal["ALLOW", "BLOCK", "COUNT"] = Field(alias="Type")


class WafOverrideActionModel(BaseModel):
    type: Literal["COUNT", "NONE"] = Field(alias="Type")


class AssociateWebACLRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    resource_arn: str = Field(alias="ResourceArn")


class ByteMatchSetSummaryModel(BaseModel):
    byte_match_set_id: str = Field(alias="ByteMatchSetId")
    name: str = Field(alias="Name")


class FieldToMatchModel(BaseModel):
    type: Literal[
        "ALL_QUERY_ARGS",
        "BODY",
        "HEADER",
        "METHOD",
        "QUERY_STRING",
        "SINGLE_QUERY_ARG",
        "URI",
    ] = Field(alias="Type")
    data: Optional[str] = Field(default=None, alias="Data")


class CreateByteMatchSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CreateGeoMatchSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class CreateIPSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateRegexMatchSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class CreateRegexPatternSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class RegexPatternSetModel(BaseModel):
    regex_pattern_set_id: str = Field(alias="RegexPatternSetId")
    regex_pattern_strings: List[str] = Field(alias="RegexPatternStrings")
    name: Optional[str] = Field(default=None, alias="Name")


class RuleGroupModel(BaseModel):
    rule_group_id: str = Field(alias="RuleGroupId")
    name: Optional[str] = Field(default=None, alias="Name")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")


class CreateSizeConstraintSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class CreateSqlInjectionMatchSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class CreateWebACLMigrationStackRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    s3_bucket_name: str = Field(alias="S3BucketName")
    ignore_unsupported_type: bool = Field(alias="IgnoreUnsupportedType")


class CreateXssMatchSetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    change_token: str = Field(alias="ChangeToken")


class DeleteByteMatchSetRequestModel(BaseModel):
    byte_match_set_id: str = Field(alias="ByteMatchSetId")
    change_token: str = Field(alias="ChangeToken")


class DeleteGeoMatchSetRequestModel(BaseModel):
    geo_match_set_id: str = Field(alias="GeoMatchSetId")
    change_token: str = Field(alias="ChangeToken")


class DeleteIPSetRequestModel(BaseModel):
    ip_set_id: str = Field(alias="IPSetId")
    change_token: str = Field(alias="ChangeToken")


class DeleteLoggingConfigurationRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeletePermissionPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class DeleteRateBasedRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    change_token: str = Field(alias="ChangeToken")


class DeleteRegexMatchSetRequestModel(BaseModel):
    regex_match_set_id: str = Field(alias="RegexMatchSetId")
    change_token: str = Field(alias="ChangeToken")


class DeleteRegexPatternSetRequestModel(BaseModel):
    regex_pattern_set_id: str = Field(alias="RegexPatternSetId")
    change_token: str = Field(alias="ChangeToken")


class DeleteRuleGroupRequestModel(BaseModel):
    rule_group_id: str = Field(alias="RuleGroupId")
    change_token: str = Field(alias="ChangeToken")


class DeleteRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    change_token: str = Field(alias="ChangeToken")


class DeleteSizeConstraintSetRequestModel(BaseModel):
    size_constraint_set_id: str = Field(alias="SizeConstraintSetId")
    change_token: str = Field(alias="ChangeToken")


class DeleteSqlInjectionMatchSetRequestModel(BaseModel):
    sql_injection_match_set_id: str = Field(alias="SqlInjectionMatchSetId")
    change_token: str = Field(alias="ChangeToken")


class DeleteWebACLRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    change_token: str = Field(alias="ChangeToken")


class DeleteXssMatchSetRequestModel(BaseModel):
    xss_match_set_id: str = Field(alias="XssMatchSetId")
    change_token: str = Field(alias="ChangeToken")


class DisassociateWebACLRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GeoMatchConstraintModel(BaseModel):
    type: Literal["Country"] = Field(alias="Type")
    value: Literal[
        "AD",
        "AE",
        "AF",
        "AG",
        "AI",
        "AL",
        "AM",
        "AO",
        "AQ",
        "AR",
        "AS",
        "AT",
        "AU",
        "AW",
        "AX",
        "AZ",
        "BA",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BI",
        "BJ",
        "BL",
        "BM",
        "BN",
        "BO",
        "BQ",
        "BR",
        "BS",
        "BT",
        "BV",
        "BW",
        "BY",
        "BZ",
        "CA",
        "CC",
        "CD",
        "CF",
        "CG",
        "CH",
        "CI",
        "CK",
        "CL",
        "CM",
        "CN",
        "CO",
        "CR",
        "CU",
        "CV",
        "CW",
        "CX",
        "CY",
        "CZ",
        "DE",
        "DJ",
        "DK",
        "DM",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "EH",
        "ER",
        "ES",
        "ET",
        "FI",
        "FJ",
        "FK",
        "FM",
        "FO",
        "FR",
        "GA",
        "GB",
        "GD",
        "GE",
        "GF",
        "GG",
        "GH",
        "GI",
        "GL",
        "GM",
        "GN",
        "GP",
        "GQ",
        "GR",
        "GS",
        "GT",
        "GU",
        "GW",
        "GY",
        "HK",
        "HM",
        "HN",
        "HR",
        "HT",
        "HU",
        "ID",
        "IE",
        "IL",
        "IM",
        "IN",
        "Type[IO]",
        "IQ",
        "IR",
        "IS",
        "IT",
        "JE",
        "JM",
        "JO",
        "JP",
        "KE",
        "KG",
        "KH",
        "KI",
        "KM",
        "KN",
        "KP",
        "KR",
        "KW",
        "KY",
        "KZ",
        "LA",
        "LB",
        "LC",
        "LI",
        "LK",
        "LR",
        "LS",
        "LT",
        "LU",
        "LV",
        "LY",
        "MA",
        "MC",
        "MD",
        "ME",
        "MF",
        "MG",
        "MH",
        "MK",
        "ML",
        "MM",
        "MN",
        "MO",
        "MP",
        "MQ",
        "MR",
        "MS",
        "MT",
        "MU",
        "MV",
        "MW",
        "MX",
        "MY",
        "MZ",
        "NA",
        "NC",
        "NE",
        "NF",
        "NG",
        "NI",
        "NL",
        "NO",
        "NP",
        "NR",
        "NU",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PF",
        "PG",
        "PH",
        "PK",
        "PL",
        "PM",
        "PN",
        "PR",
        "PS",
        "PT",
        "PW",
        "PY",
        "QA",
        "RE",
        "RO",
        "RS",
        "RU",
        "RW",
        "SA",
        "SB",
        "SC",
        "SD",
        "SE",
        "SG",
        "SH",
        "SI",
        "SJ",
        "SK",
        "SL",
        "SM",
        "SN",
        "SO",
        "SR",
        "SS",
        "ST",
        "SV",
        "SX",
        "SY",
        "SZ",
        "TC",
        "TD",
        "TF",
        "TG",
        "TH",
        "TJ",
        "TK",
        "TL",
        "TM",
        "TN",
        "TO",
        "TR",
        "TT",
        "TV",
        "TW",
        "TZ",
        "UA",
        "UG",
        "UM",
        "US",
        "UY",
        "UZ",
        "VA",
        "VC",
        "VE",
        "VG",
        "VI",
        "VN",
        "VU",
        "WF",
        "WS",
        "YE",
        "YT",
        "ZA",
        "ZM",
        "ZW",
    ] = Field(alias="Value")


class GeoMatchSetSummaryModel(BaseModel):
    geo_match_set_id: str = Field(alias="GeoMatchSetId")
    name: str = Field(alias="Name")


class GetByteMatchSetRequestModel(BaseModel):
    byte_match_set_id: str = Field(alias="ByteMatchSetId")


class GetChangeTokenStatusRequestModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")


class GetGeoMatchSetRequestModel(BaseModel):
    geo_match_set_id: str = Field(alias="GeoMatchSetId")


class GetIPSetRequestModel(BaseModel):
    ip_set_id: str = Field(alias="IPSetId")


class GetLoggingConfigurationRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetPermissionPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class GetRateBasedRuleManagedKeysRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")


class GetRateBasedRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")


class GetRegexMatchSetRequestModel(BaseModel):
    regex_match_set_id: str = Field(alias="RegexMatchSetId")


class GetRegexPatternSetRequestModel(BaseModel):
    regex_pattern_set_id: str = Field(alias="RegexPatternSetId")


class GetRuleGroupRequestModel(BaseModel):
    rule_group_id: str = Field(alias="RuleGroupId")


class GetRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")


class TimeWindowModel(BaseModel):
    start_time: Union[datetime, str] = Field(alias="StartTime")
    end_time: Union[datetime, str] = Field(alias="EndTime")


class GetSizeConstraintSetRequestModel(BaseModel):
    size_constraint_set_id: str = Field(alias="SizeConstraintSetId")


class GetSqlInjectionMatchSetRequestModel(BaseModel):
    sql_injection_match_set_id: str = Field(alias="SqlInjectionMatchSetId")


class GetWebACLForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class WebACLSummaryModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    name: str = Field(alias="Name")


class GetWebACLRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")


class GetXssMatchSetRequestModel(BaseModel):
    xss_match_set_id: str = Field(alias="XssMatchSetId")


class HTTPHeaderModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class IPSetDescriptorModel(BaseModel):
    type: Literal["IPV4", "IPV6"] = Field(alias="Type")
    value: str = Field(alias="Value")


class IPSetSummaryModel(BaseModel):
    ip_set_id: str = Field(alias="IPSetId")
    name: str = Field(alias="Name")


class ListActivatedRulesInRuleGroupRequestModel(BaseModel):
    rule_group_id: Optional[str] = Field(default=None, alias="RuleGroupId")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListByteMatchSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListGeoMatchSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListIPSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListLoggingConfigurationsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListRateBasedRulesRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class RuleSummaryModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    name: str = Field(alias="Name")


class ListRegexMatchSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class RegexMatchSetSummaryModel(BaseModel):
    regex_match_set_id: str = Field(alias="RegexMatchSetId")
    name: str = Field(alias="Name")


class ListRegexPatternSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class RegexPatternSetSummaryModel(BaseModel):
    regex_pattern_set_id: str = Field(alias="RegexPatternSetId")
    name: str = Field(alias="Name")


class ListResourcesForWebACLRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    resource_type: Optional[
        Literal["API_GATEWAY", "APPLICATION_LOAD_BALANCER"]
    ] = Field(default=None, alias="ResourceType")


class ListRuleGroupsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class RuleGroupSummaryModel(BaseModel):
    rule_group_id: str = Field(alias="RuleGroupId")
    name: str = Field(alias="Name")


class ListRulesRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListSizeConstraintSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class SizeConstraintSetSummaryModel(BaseModel):
    size_constraint_set_id: str = Field(alias="SizeConstraintSetId")
    name: str = Field(alias="Name")


class ListSqlInjectionMatchSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class SqlInjectionMatchSetSummaryModel(BaseModel):
    sql_injection_match_set_id: str = Field(alias="SqlInjectionMatchSetId")
    name: str = Field(alias="Name")


class ListSubscribedRuleGroupsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class SubscribedRuleGroupSummaryModel(BaseModel):
    rule_group_id: str = Field(alias="RuleGroupId")
    name: str = Field(alias="Name")
    metric_name: str = Field(alias="MetricName")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListWebACLsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class ListXssMatchSetsRequestModel(BaseModel):
    next_marker: Optional[str] = Field(default=None, alias="NextMarker")
    limit: Optional[int] = Field(default=None, alias="Limit")


class XssMatchSetSummaryModel(BaseModel):
    xss_match_set_id: str = Field(alias="XssMatchSetId")
    name: str = Field(alias="Name")


class PredicateModel(BaseModel):
    negated: bool = Field(alias="Negated")
    type: Literal[
        "ByteMatch",
        "GeoMatch",
        "IPMatch",
        "RegexMatch",
        "SizeConstraint",
        "SqlInjectionMatch",
        "XssMatch",
    ] = Field(alias="Type")
    data_id: str = Field(alias="DataId")


class PutPermissionPolicyRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    policy: str = Field(alias="Policy")


class RegexPatternSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    regex_pattern_string: str = Field(alias="RegexPatternString")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class ActivatedRuleModel(BaseModel):
    priority: int = Field(alias="Priority")
    rule_id: str = Field(alias="RuleId")
    action: Optional[WafActionModel] = Field(default=None, alias="Action")
    override_action: Optional[WafOverrideActionModel] = Field(
        default=None, alias="OverrideAction"
    )
    type: Optional[Literal["GROUP", "RATE_BASED", "REGULAR"]] = Field(
        default=None, alias="Type"
    )
    excluded_rules: Optional[List[ExcludedRuleModel]] = Field(
        default=None, alias="ExcludedRules"
    )


class ByteMatchTupleModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    target_string: bytes = Field(alias="TargetString")
    text_transformation: Literal[
        "CMD_LINE",
        "COMPRESS_WHITE_SPACE",
        "HTML_ENTITY_DECODE",
        "LOWERCASE",
        "NONE",
        "URL_DECODE",
    ] = Field(alias="TextTransformation")
    positional_constraint: Literal[
        "CONTAINS", "CONTAINS_WORD", "ENDS_WITH", "EXACTLY", "STARTS_WITH"
    ] = Field(alias="PositionalConstraint")


class LoggingConfigurationModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    log_destination_configs: List[str] = Field(alias="LogDestinationConfigs")
    redacted_fields: Optional[List[FieldToMatchModel]] = Field(
        default=None, alias="RedactedFields"
    )


class RegexMatchTupleModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformation: Literal[
        "CMD_LINE",
        "COMPRESS_WHITE_SPACE",
        "HTML_ENTITY_DECODE",
        "LOWERCASE",
        "NONE",
        "URL_DECODE",
    ] = Field(alias="TextTransformation")
    regex_pattern_set_id: str = Field(alias="RegexPatternSetId")


class SizeConstraintModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformation: Literal[
        "CMD_LINE",
        "COMPRESS_WHITE_SPACE",
        "HTML_ENTITY_DECODE",
        "LOWERCASE",
        "NONE",
        "URL_DECODE",
    ] = Field(alias="TextTransformation")
    comparison_operator: Literal["EQ", "GE", "GT", "LE", "LT", "NE"] = Field(
        alias="ComparisonOperator"
    )
    size: int = Field(alias="Size")


class SqlInjectionMatchTupleModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformation: Literal[
        "CMD_LINE",
        "COMPRESS_WHITE_SPACE",
        "HTML_ENTITY_DECODE",
        "LOWERCASE",
        "NONE",
        "URL_DECODE",
    ] = Field(alias="TextTransformation")


class XssMatchTupleModel(BaseModel):
    field_to_match: FieldToMatchModel = Field(alias="FieldToMatch")
    text_transformation: Literal[
        "CMD_LINE",
        "COMPRESS_WHITE_SPACE",
        "HTML_ENTITY_DECODE",
        "LOWERCASE",
        "NONE",
        "URL_DECODE",
    ] = Field(alias="TextTransformation")


class CreateWebACLMigrationStackResponseModel(BaseModel):
    s3_object_url: str = Field(alias="S3ObjectUrl")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteByteMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGeoMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteIPSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRateBasedRuleResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRegexMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRegexPatternSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRuleGroupResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteRuleResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSizeConstraintSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteSqlInjectionMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteWebACLResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteXssMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChangeTokenResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetChangeTokenStatusResponseModel(BaseModel):
    change_token_status: Literal["INSYNC", "PENDING", "PROVISIONED"] = Field(
        alias="ChangeTokenStatus"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPermissionPolicyResponseModel(BaseModel):
    policy: str = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRateBasedRuleManagedKeysResponseModel(BaseModel):
    managed_keys: List[str] = Field(alias="ManagedKeys")
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListByteMatchSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    byte_match_sets: List[ByteMatchSetSummaryModel] = Field(alias="ByteMatchSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListResourcesForWebACLResponseModel(BaseModel):
    resource_arns: List[str] = Field(alias="ResourceArns")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateByteMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGeoMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIPSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRateBasedRuleResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRegexMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRegexPatternSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRuleGroupResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRuleResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSizeConstraintSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSqlInjectionMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWebACLResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateXssMatchSetResponseModel(BaseModel):
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRateBasedRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    metric_name: str = Field(alias="MetricName")
    rate_key: Literal["IP"] = Field(alias="RateKey")
    rate_limit: int = Field(alias="RateLimit")
    change_token: str = Field(alias="ChangeToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateRuleGroupRequestModel(BaseModel):
    name: str = Field(alias="Name")
    metric_name: str = Field(alias="MetricName")
    change_token: str = Field(alias="ChangeToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateRuleRequestModel(BaseModel):
    name: str = Field(alias="Name")
    metric_name: str = Field(alias="MetricName")
    change_token: str = Field(alias="ChangeToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateWebACLRequestModel(BaseModel):
    name: str = Field(alias="Name")
    metric_name: str = Field(alias="MetricName")
    default_action: WafActionModel = Field(alias="DefaultAction")
    change_token: str = Field(alias="ChangeToken")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class TagInfoForResourceModel(BaseModel):
    resource_arn: Optional[str] = Field(default=None, alias="ResourceARN")
    tag_list: Optional[List[TagModel]] = Field(default=None, alias="TagList")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceARN")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateRegexPatternSetResponseModel(BaseModel):
    regex_pattern_set: RegexPatternSetModel = Field(alias="RegexPatternSet")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegexPatternSetResponseModel(BaseModel):
    regex_pattern_set: RegexPatternSetModel = Field(alias="RegexPatternSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleGroupResponseModel(BaseModel):
    rule_group: RuleGroupModel = Field(alias="RuleGroup")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRuleGroupResponseModel(BaseModel):
    rule_group: RuleGroupModel = Field(alias="RuleGroup")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GeoMatchSetModel(BaseModel):
    geo_match_set_id: str = Field(alias="GeoMatchSetId")
    geo_match_constraints: List[GeoMatchConstraintModel] = Field(
        alias="GeoMatchConstraints"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class GeoMatchSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    geo_match_constraint: GeoMatchConstraintModel = Field(alias="GeoMatchConstraint")


class ListGeoMatchSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    geo_match_sets: List[GeoMatchSetSummaryModel] = Field(alias="GeoMatchSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSampledRequestsRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebAclId")
    rule_id: str = Field(alias="RuleId")
    time_window: TimeWindowModel = Field(alias="TimeWindow")
    max_items: int = Field(alias="MaxItems")


class GetWebACLForResourceResponseModel(BaseModel):
    web_acl_summary: WebACLSummaryModel = Field(alias="WebACLSummary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListWebACLsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    web_acls: List[WebACLSummaryModel] = Field(alias="WebACLs")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class HTTPRequestModel(BaseModel):
    client_ip: Optional[str] = Field(default=None, alias="ClientIP")
    country: Optional[str] = Field(default=None, alias="Country")
    uri: Optional[str] = Field(default=None, alias="URI")
    method: Optional[str] = Field(default=None, alias="Method")
    http_version: Optional[str] = Field(default=None, alias="HTTPVersion")
    headers: Optional[List[HTTPHeaderModel]] = Field(default=None, alias="Headers")


class IPSetModel(BaseModel):
    ip_set_id: str = Field(alias="IPSetId")
    ip_set_descriptors: List[IPSetDescriptorModel] = Field(alias="IPSetDescriptors")
    name: Optional[str] = Field(default=None, alias="Name")


class IPSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    ip_set_descriptor: IPSetDescriptorModel = Field(alias="IPSetDescriptor")


class ListIPSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    ip_sets: List[IPSetSummaryModel] = Field(alias="IPSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRateBasedRulesResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    rules: List[RuleSummaryModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRulesResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    rules: List[RuleSummaryModel] = Field(alias="Rules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRegexMatchSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    regex_match_sets: List[RegexMatchSetSummaryModel] = Field(alias="RegexMatchSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRegexPatternSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    regex_pattern_sets: List[RegexPatternSetSummaryModel] = Field(
        alias="RegexPatternSets"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListRuleGroupsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    rule_groups: List[RuleGroupSummaryModel] = Field(alias="RuleGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSizeConstraintSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    size_constraint_sets: List[SizeConstraintSetSummaryModel] = Field(
        alias="SizeConstraintSets"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSqlInjectionMatchSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    sql_injection_match_sets: List[SqlInjectionMatchSetSummaryModel] = Field(
        alias="SqlInjectionMatchSets"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListSubscribedRuleGroupsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    rule_groups: List[SubscribedRuleGroupSummaryModel] = Field(alias="RuleGroups")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListXssMatchSetsResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    xss_match_sets: List[XssMatchSetSummaryModel] = Field(alias="XssMatchSets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RateBasedRuleModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    match_predicates: List[PredicateModel] = Field(alias="MatchPredicates")
    rate_key: Literal["IP"] = Field(alias="RateKey")
    rate_limit: int = Field(alias="RateLimit")
    name: Optional[str] = Field(default=None, alias="Name")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")


class RuleModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    predicates: List[PredicateModel] = Field(alias="Predicates")
    name: Optional[str] = Field(default=None, alias="Name")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")


class RuleUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    predicate: PredicateModel = Field(alias="Predicate")


class UpdateRegexPatternSetRequestModel(BaseModel):
    regex_pattern_set_id: str = Field(alias="RegexPatternSetId")
    updates: Sequence[RegexPatternSetUpdateModel] = Field(alias="Updates")
    change_token: str = Field(alias="ChangeToken")


class ListActivatedRulesInRuleGroupResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    activated_rules: List[ActivatedRuleModel] = Field(alias="ActivatedRules")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RuleGroupUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    activated_rule: ActivatedRuleModel = Field(alias="ActivatedRule")


class WebACLModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    default_action: WafActionModel = Field(alias="DefaultAction")
    rules: List[ActivatedRuleModel] = Field(alias="Rules")
    name: Optional[str] = Field(default=None, alias="Name")
    metric_name: Optional[str] = Field(default=None, alias="MetricName")
    web_acl_arn: Optional[str] = Field(default=None, alias="WebACLArn")


class WebACLUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    activated_rule: ActivatedRuleModel = Field(alias="ActivatedRule")


class ByteMatchSetModel(BaseModel):
    byte_match_set_id: str = Field(alias="ByteMatchSetId")
    byte_match_tuples: List[ByteMatchTupleModel] = Field(alias="ByteMatchTuples")
    name: Optional[str] = Field(default=None, alias="Name")


class ByteMatchSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    byte_match_tuple: ByteMatchTupleModel = Field(alias="ByteMatchTuple")


class GetLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListLoggingConfigurationsResponseModel(BaseModel):
    logging_configurations: List[LoggingConfigurationModel] = Field(
        alias="LoggingConfigurations"
    )
    next_marker: str = Field(alias="NextMarker")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutLoggingConfigurationRequestModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )


class PutLoggingConfigurationResponseModel(BaseModel):
    logging_configuration: LoggingConfigurationModel = Field(
        alias="LoggingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegexMatchSetModel(BaseModel):
    regex_match_set_id: Optional[str] = Field(default=None, alias="RegexMatchSetId")
    name: Optional[str] = Field(default=None, alias="Name")
    regex_match_tuples: Optional[List[RegexMatchTupleModel]] = Field(
        default=None, alias="RegexMatchTuples"
    )


class RegexMatchSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    regex_match_tuple: RegexMatchTupleModel = Field(alias="RegexMatchTuple")


class SizeConstraintSetModel(BaseModel):
    size_constraint_set_id: str = Field(alias="SizeConstraintSetId")
    size_constraints: List[SizeConstraintModel] = Field(alias="SizeConstraints")
    name: Optional[str] = Field(default=None, alias="Name")


class SizeConstraintSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    size_constraint: SizeConstraintModel = Field(alias="SizeConstraint")


class SqlInjectionMatchSetModel(BaseModel):
    sql_injection_match_set_id: str = Field(alias="SqlInjectionMatchSetId")
    sql_injection_match_tuples: List[SqlInjectionMatchTupleModel] = Field(
        alias="SqlInjectionMatchTuples"
    )
    name: Optional[str] = Field(default=None, alias="Name")


class SqlInjectionMatchSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    sql_injection_match_tuple: SqlInjectionMatchTupleModel = Field(
        alias="SqlInjectionMatchTuple"
    )


class XssMatchSetModel(BaseModel):
    xss_match_set_id: str = Field(alias="XssMatchSetId")
    xss_match_tuples: List[XssMatchTupleModel] = Field(alias="XssMatchTuples")
    name: Optional[str] = Field(default=None, alias="Name")


class XssMatchSetUpdateModel(BaseModel):
    action: Literal["DELETE", "INSERT"] = Field(alias="Action")
    xss_match_tuple: XssMatchTupleModel = Field(alias="XssMatchTuple")


class ListTagsForResourceResponseModel(BaseModel):
    next_marker: str = Field(alias="NextMarker")
    tag_info_for_resource: TagInfoForResourceModel = Field(alias="TagInfoForResource")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGeoMatchSetResponseModel(BaseModel):
    geo_match_set: GeoMatchSetModel = Field(alias="GeoMatchSet")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetGeoMatchSetResponseModel(BaseModel):
    geo_match_set: GeoMatchSetModel = Field(alias="GeoMatchSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGeoMatchSetRequestModel(BaseModel):
    geo_match_set_id: str = Field(alias="GeoMatchSetId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[GeoMatchSetUpdateModel] = Field(alias="Updates")


class SampledHTTPRequestModel(BaseModel):
    request: HTTPRequestModel = Field(alias="Request")
    weight: int = Field(alias="Weight")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")
    action: Optional[str] = Field(default=None, alias="Action")
    rule_within_rule_group: Optional[str] = Field(
        default=None, alias="RuleWithinRuleGroup"
    )


class CreateIPSetResponseModel(BaseModel):
    ip_set: IPSetModel = Field(alias="IPSet")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetIPSetResponseModel(BaseModel):
    ip_set: IPSetModel = Field(alias="IPSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIPSetRequestModel(BaseModel):
    ip_set_id: str = Field(alias="IPSetId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[IPSetUpdateModel] = Field(alias="Updates")


class CreateRateBasedRuleResponseModel(BaseModel):
    rule: RateBasedRuleModel = Field(alias="Rule")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRateBasedRuleResponseModel(BaseModel):
    rule: RateBasedRuleModel = Field(alias="Rule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateRuleResponseModel(BaseModel):
    rule: RuleModel = Field(alias="Rule")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRuleResponseModel(BaseModel):
    rule: RuleModel = Field(alias="Rule")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRateBasedRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[RuleUpdateModel] = Field(alias="Updates")
    rate_limit: int = Field(alias="RateLimit")


class UpdateRuleRequestModel(BaseModel):
    rule_id: str = Field(alias="RuleId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[RuleUpdateModel] = Field(alias="Updates")


class UpdateRuleGroupRequestModel(BaseModel):
    rule_group_id: str = Field(alias="RuleGroupId")
    updates: Sequence[RuleGroupUpdateModel] = Field(alias="Updates")
    change_token: str = Field(alias="ChangeToken")


class CreateWebACLResponseModel(BaseModel):
    web_acl: WebACLModel = Field(alias="WebACL")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetWebACLResponseModel(BaseModel):
    web_acl: WebACLModel = Field(alias="WebACL")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateWebACLRequestModel(BaseModel):
    web_acl_id: str = Field(alias="WebACLId")
    change_token: str = Field(alias="ChangeToken")
    updates: Optional[Sequence[WebACLUpdateModel]] = Field(
        default=None, alias="Updates"
    )
    default_action: Optional[WafActionModel] = Field(
        default=None, alias="DefaultAction"
    )


class CreateByteMatchSetResponseModel(BaseModel):
    byte_match_set: ByteMatchSetModel = Field(alias="ByteMatchSet")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetByteMatchSetResponseModel(BaseModel):
    byte_match_set: ByteMatchSetModel = Field(alias="ByteMatchSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateByteMatchSetRequestModel(BaseModel):
    byte_match_set_id: str = Field(alias="ByteMatchSetId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[ByteMatchSetUpdateModel] = Field(alias="Updates")


class CreateRegexMatchSetResponseModel(BaseModel):
    regex_match_set: RegexMatchSetModel = Field(alias="RegexMatchSet")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRegexMatchSetResponseModel(BaseModel):
    regex_match_set: RegexMatchSetModel = Field(alias="RegexMatchSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateRegexMatchSetRequestModel(BaseModel):
    regex_match_set_id: str = Field(alias="RegexMatchSetId")
    updates: Sequence[RegexMatchSetUpdateModel] = Field(alias="Updates")
    change_token: str = Field(alias="ChangeToken")


class CreateSizeConstraintSetResponseModel(BaseModel):
    size_constraint_set: SizeConstraintSetModel = Field(alias="SizeConstraintSet")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSizeConstraintSetResponseModel(BaseModel):
    size_constraint_set: SizeConstraintSetModel = Field(alias="SizeConstraintSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSizeConstraintSetRequestModel(BaseModel):
    size_constraint_set_id: str = Field(alias="SizeConstraintSetId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[SizeConstraintSetUpdateModel] = Field(alias="Updates")


class CreateSqlInjectionMatchSetResponseModel(BaseModel):
    sql_injection_match_set: SqlInjectionMatchSetModel = Field(
        alias="SqlInjectionMatchSet"
    )
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSqlInjectionMatchSetResponseModel(BaseModel):
    sql_injection_match_set: SqlInjectionMatchSetModel = Field(
        alias="SqlInjectionMatchSet"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateSqlInjectionMatchSetRequestModel(BaseModel):
    sql_injection_match_set_id: str = Field(alias="SqlInjectionMatchSetId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[SqlInjectionMatchSetUpdateModel] = Field(alias="Updates")


class CreateXssMatchSetResponseModel(BaseModel):
    xss_match_set: XssMatchSetModel = Field(alias="XssMatchSet")
    change_token: str = Field(alias="ChangeToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetXssMatchSetResponseModel(BaseModel):
    xss_match_set: XssMatchSetModel = Field(alias="XssMatchSet")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateXssMatchSetRequestModel(BaseModel):
    xss_match_set_id: str = Field(alias="XssMatchSetId")
    change_token: str = Field(alias="ChangeToken")
    updates: Sequence[XssMatchSetUpdateModel] = Field(alias="Updates")


class GetSampledRequestsResponseModel(BaseModel):
    sampled_requests: List[SampledHTTPRequestModel] = Field(alias="SampledRequests")
    population_size: int = Field(alias="PopulationSize")
    time_window: TimeWindowModel = Field(alias="TimeWindow")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
