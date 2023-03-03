# mypydantic

mypy boto3 type definitions as pydantic models

Code Documentation: [Link](https://jmgreg31.github.io/mypydantic.html)

Huge thanks to the developers of mypy_boto3 and pydantic!

mypy_boto3: [Link](https://mypy-boto3.readthedocs.io/en/latest/)

pydantic: [Link](https://docs.pydantic.dev/)

## Usage

The following section provides some usage examples.

### Loading a Request Model

```py
from mypydantic.models.wafv2 import (
    CreateWebACLRequestModel,
    DefaultActionModel,
    VisibilityConfigModel,
)

config = {
    "Name": "example",
    "Scope": "REGIONAL",
    "DefaultAction": DefaultActionModel(Allow={}),
    "VisibilityConfig": VisibilityConfigModel(
        SampledRequestsEnabled=False,
        CloudWatchMetricsEnabled=False,
        MetricName="example-metric",
    ),
}
create_web_acl_request = CreateWebACLRequestModel(**config)
print(create_web_acl_request.name)
print(create_web_acl_request.scope)
...
```

### Executing a Boto3 Request

```py
from mypydantic.models.wafv2 import (
    CreateWebACLRequestModel,
    DefaultActionModel,
    VisibilityConfigModel,
)
from mypy_boto3_wafv2.client import WAFV2Client

client: WAFV2Client = boto3.client("wafv2", aws_region="us-east-1")
config = {
    "Name": "example",
    "Scope": "REGIONAL",
    "DefaultAction": DefaultActionModel(Allow={}),
    "VisibilityConfig": VisibilityConfigModel(
        SampledRequestsEnabled=False,
        CloudWatchMetricsEnabled=False,
        MetricName="example-metric",
    ),
}
create_web_acl_request = CreateWebACLRequestModel(**config)

# Using the 'by_alias' option retains the expected AWS request key casing
client.create_web_acl(**create_web_acl_request.dict(by_alias=True, exclude_none=True))
```

### Loading a Response Model

```py
from mypydantic.models.wafv2 import CreateWebACLResponseModel
from mypy_boto3_wafv2.client import WAFV2Client

client: WAFV2Client = boto3.client("wafv2", aws_region="us-east-1")
config = {
    "Name": "example",
    "Scope": "REGIONAL",
    "DefaultAction": {"Allow": {}},
    "VisibilityConfig": {
        "SampledRequestsEnabled": False,
        "CloudWatchMetricsEnabled": False,
        "MetricName": "test",
    },
}

create_web_acl_response = CreateWebACLResponseModel(client.create_web_acl(**config))
web_acl = create_web_acl_response.summary

print(web_acl.name)
print(web_acl.id)
print(web_acl.description)
print(web_acl.lock_token)
print(web_acl.arn)
```
