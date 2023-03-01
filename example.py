from mypydantic.helpers.logger import CustomLogger
from mypydantic.models.wafv2 import (
    CaptchaConfig,
    ChallengeConfig,
    CreateWebACLRequest,
    CreateWebACLResponse,
    CustomResponseBody,
    DefaultAction,
    ImmunityTimeProperty,
    IPSetReferenceStatement,
    Rule,
    Statement,
    Tag,
    VisibilityConfig,
)

LOG = CustomLogger()
LOG.local = True


def build_with_aws_keys() -> CreateWebACLRequest:
    config = {
        "Name": "Example WebACL AWS Keys",
        "Scope": "REGIONAL",
        "VisibilityConfig": VisibilityConfig(
            SampledRequestsEnabled=False,
            CloudWatchMetricsEnabled=False,
            MetricName="test",
        ),
        "DefaultAction": DefaultAction(Allow={}),
        "Description": "example model",
        "Rules": [
            Rule(
                Name="example rule",
                Priority=0,
                VisibilityConfig=VisibilityConfig(
                    SampledRequestsEnabled=False,
                    CloudWatchMetricsEnabled=False,
                    MetricName="test",
                ),
                Statement=Statement(
                    IPSetReferenceStatement=IPSetReferenceStatement(ARN="ipset:arn")
                ),
            )
        ],
        "Tags": [Tag(Key="TAG_KEY", Value="TAG_VALUE")],
        "CustomResponseBodies": {
            "success_code": CustomResponseBody(
                ContentType="APPLICATION_JSON", Content="Success"
            ),
        },
        "CaptchaConfig": CaptchaConfig(
            ImmunityTimeProperty=ImmunityTimeProperty(ImmunityTime=1)
        ),
        "ChallengeConfig": ChallengeConfig(
            ImmunityTimeProperty=ImmunityTimeProperty(ImmunityTime=1)
        ),
        "TokenDomains": ["example.com"],
    }
    create_web_acl_request = CreateWebACLRequest(**config)
    LOG.debug(create_web_acl_request)
    LOG.debug(create_web_acl_request.dict(by_alias=True, exclude_none=True))
    return create_web_acl_request


def build_with_snake_keys() -> CreateWebACLRequest:
    config = {
        "name": "Example WebACL Snake Keys",
        "scope": "REGIONAL",
        "visibility_config": VisibilityConfig(
            SampledRequestsEnabled=False,
            CloudWatchMetricsEnabled=False,
            MetricName="test",
        ),
        "default_action": DefaultAction(Allow={}),
        "description": "example model",
        "rules": [
            Rule(
                Name="example rule",
                Priority=0,
                VisibilityConfig=VisibilityConfig(
                    SampledRequestsEnabled=False,
                    CloudWatchMetricsEnabled=False,
                    MetricName="test",
                ),
                Statement=Statement(
                    IPSetReferenceStatement=IPSetReferenceStatement(ARN="ipset:arn")
                ),
            )
        ],
        "tags": [Tag(Key="TAG_KEY", Value="TAG_VALUE")],
        "custom_response_bodies": {
            "success_code": CustomResponseBody(
                ContentType="APPLICATION_JSON", Content="Success"
            ),
        },
        "captcha_config": CaptchaConfig(
            ImmunityTimeProperty=ImmunityTimeProperty(ImmunityTime=1)
        ),
        "challenge_config": ChallengeConfig(
            ImmunityTimeProperty=ImmunityTimeProperty(ImmunityTime=1)
        ),
        "token_domains": ["example.com"],
    }
    create_web_acl_request = CreateWebACLRequest(**config)
    LOG.debug(create_web_acl_request)
    LOG.debug(create_web_acl_request.dict(by_alias=True, exclude_none=True))
    return create_web_acl_request


def main() -> None:
    create_web_acl_aws_keys = build_with_aws_keys()
    create_web_acl_snake_keys = build_with_snake_keys()
    LOG.info(create_web_acl_aws_keys.name)
    LOG.info(create_web_acl_snake_keys.name)
    # #####
    # import boto3
    # from mypy_boto3_wafv2.client import WAFV2Client
    # client: WAFV2Client = boto3.client("wafv2", aws_region="us-east-1")

    # # Using 'by_alias' will keep the AWS expected keys
    # client.create_web_acl(
    #     create_web_acl_snake_keys.dict(by_alias=True, exclude_none=True)
    # )
    # ######


if __name__ == "__main__":
    main()
