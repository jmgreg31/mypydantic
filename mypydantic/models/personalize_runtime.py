# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Dict, List, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class GetPersonalizedRankingRequestModel(BaseModel):
    campaign_arn: str = Field(alias="campaignArn")
    input_list: Sequence[str] = Field(alias="inputList")
    user_id: str = Field(alias="userId")
    context: Optional[Mapping[str, str]] = Field(default=None, alias="context")
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    filter_values: Optional[Mapping[str, str]] = Field(
        default=None, alias="filterValues"
    )


class PredictedItemModel(BaseModel):
    item_id: Optional[str] = Field(default=None, alias="itemId")
    score: Optional[float] = Field(default=None, alias="score")
    promotion_name: Optional[str] = Field(default=None, alias="promotionName")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class PromotionModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="name")
    percent_promoted_items: Optional[int] = Field(
        default=None, alias="percentPromotedItems"
    )
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    filter_values: Optional[Mapping[str, str]] = Field(
        default=None, alias="filterValues"
    )


class GetPersonalizedRankingResponseModel(BaseModel):
    personalized_ranking: List[PredictedItemModel] = Field(alias="personalizedRanking")
    recommendation_id: str = Field(alias="recommendationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommendationsResponseModel(BaseModel):
    item_list: List[PredictedItemModel] = Field(alias="itemList")
    recommendation_id: str = Field(alias="recommendationId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetRecommendationsRequestModel(BaseModel):
    campaign_arn: Optional[str] = Field(default=None, alias="campaignArn")
    item_id: Optional[str] = Field(default=None, alias="itemId")
    user_id: Optional[str] = Field(default=None, alias="userId")
    num_results: Optional[int] = Field(default=None, alias="numResults")
    context: Optional[Mapping[str, str]] = Field(default=None, alias="context")
    filter_arn: Optional[str] = Field(default=None, alias="filterArn")
    filter_values: Optional[Mapping[str, str]] = Field(
        default=None, alias="filterValues"
    )
    recommender_arn: Optional[str] = Field(default=None, alias="recommenderArn")
    promotions: Optional[Sequence[PromotionModel]] = Field(
        default=None, alias="promotions"
    )
