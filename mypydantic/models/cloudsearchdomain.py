# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from typing import Any, Dict, IO, List, Literal, Optional, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class BucketModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="value")
    count: Optional[int] = Field(default=None, alias="count")


class DocumentServiceWarningModel(BaseModel):
    message: Optional[str] = Field(default=None, alias="message")


class FieldStatsModel(BaseModel):
    min: Optional[str] = Field(default=None, alias="min")
    max: Optional[str] = Field(default=None, alias="max")
    count: Optional[int] = Field(default=None, alias="count")
    missing: Optional[int] = Field(default=None, alias="missing")
    sum: Optional[float] = Field(default=None, alias="sum")
    sum_of_squares: Optional[float] = Field(default=None, alias="sumOfSquares")
    mean: Optional[str] = Field(default=None, alias="mean")
    stddev: Optional[float] = Field(default=None, alias="stddev")


class HitModel(BaseModel):
    id: Optional[str] = Field(default=None, alias="id")
    fields: Optional[Dict[str, List[str]]] = Field(default=None, alias="fields")
    exprs: Optional[Dict[str, str]] = Field(default=None, alias="exprs")
    highlights: Optional[Dict[str, str]] = Field(default=None, alias="highlights")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class SearchRequestModel(BaseModel):
    query: str = Field(alias="query")
    cursor: Optional[str] = Field(default=None, alias="cursor")
    expr: Optional[str] = Field(default=None, alias="expr")
    facet: Optional[str] = Field(default=None, alias="facet")
    filter_query: Optional[str] = Field(default=None, alias="filterQuery")
    highlight: Optional[str] = Field(default=None, alias="highlight")
    partial: Optional[bool] = Field(default=None, alias="partial")
    query_options: Optional[str] = Field(default=None, alias="queryOptions")
    query_parser: Optional[Literal["dismax", "lucene", "simple", "structured"]] = Field(
        default=None, alias="queryParser"
    )
    return_fields: Optional[str] = Field(default=None, alias="returnFields")
    size: Optional[int] = Field(default=None, alias="size")
    sort: Optional[str] = Field(default=None, alias="sort")
    start: Optional[int] = Field(default=None, alias="start")
    stats: Optional[str] = Field(default=None, alias="stats")


class SearchStatusModel(BaseModel):
    timems: Optional[int] = Field(default=None, alias="timems")
    rid: Optional[str] = Field(default=None, alias="rid")


class SuggestionMatchModel(BaseModel):
    suggestion: Optional[str] = Field(default=None, alias="suggestion")
    score: Optional[int] = Field(default=None, alias="score")
    id: Optional[str] = Field(default=None, alias="id")


class SuggestRequestModel(BaseModel):
    query: str = Field(alias="query")
    suggester: str = Field(alias="suggester")
    size: Optional[int] = Field(default=None, alias="size")


class SuggestStatusModel(BaseModel):
    timems: Optional[int] = Field(default=None, alias="timems")
    rid: Optional[str] = Field(default=None, alias="rid")


class UploadDocumentsRequestModel(BaseModel):
    documents: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="documents"
    )
    content_type: Literal["application/json", "application/xml"] = Field(
        alias="contentType"
    )


class BucketInfoModel(BaseModel):
    buckets: Optional[List[BucketModel]] = Field(default=None, alias="buckets")


class HitsModel(BaseModel):
    found: Optional[int] = Field(default=None, alias="found")
    start: Optional[int] = Field(default=None, alias="start")
    cursor: Optional[str] = Field(default=None, alias="cursor")
    hit: Optional[List[HitModel]] = Field(default=None, alias="hit")


class UploadDocumentsResponseModel(BaseModel):
    status: str = Field(alias="status")
    adds: int = Field(alias="adds")
    deletes: int = Field(alias="deletes")
    warnings: List[DocumentServiceWarningModel] = Field(alias="warnings")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SuggestModelModel(BaseModel):
    query: Optional[str] = Field(default=None, alias="query")
    found: Optional[int] = Field(default=None, alias="found")
    suggestions: Optional[List[SuggestionMatchModel]] = Field(
        default=None, alias="suggestions"
    )


class SearchResponseModel(BaseModel):
    status: SearchStatusModel = Field(alias="status")
    hits: HitsModel = Field(alias="hits")
    facets: Dict[str, BucketInfoModel] = Field(alias="facets")
    stats: Dict[str, FieldStatsModel] = Field(alias="stats")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SuggestResponseModel(BaseModel):
    status: SuggestStatusModel = Field(alias="status")
    suggest: SuggestModelModel = Field(alias="suggest")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
