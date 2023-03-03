# Model Generated: Thu Mar  2 21:56:17 2023

from __future__ import annotations

from typing import Dict, List, Literal, Optional

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class PointOfInterestModel(BaseModel):
    begin_offset_millis: int = Field(alias="BeginOffsetMillis")
    end_offset_millis: int = Field(alias="EndOffsetMillis")


class CharacterOffsetsModel(BaseModel):
    begin_offset_char: int = Field(alias="BeginOffsetChar")
    end_offset_char: int = Field(alias="EndOffsetChar")


class ListRealtimeContactAnalysisSegmentsRequestModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    contact_id: str = Field(alias="ContactId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CategoryDetailsModel(BaseModel):
    points_of_interest: List[PointOfInterestModel] = Field(alias="PointsOfInterest")


class IssueDetectedModel(BaseModel):
    character_offsets: CharacterOffsetsModel = Field(alias="CharacterOffsets")


class CategoriesModel(BaseModel):
    matched_categories: List[str] = Field(alias="MatchedCategories")
    matched_details: Dict[str, CategoryDetailsModel] = Field(alias="MatchedDetails")


class TranscriptModel(BaseModel):
    id: str = Field(alias="Id")
    participant_id: str = Field(alias="ParticipantId")
    participant_role: str = Field(alias="ParticipantRole")
    content: str = Field(alias="Content")
    begin_offset_millis: int = Field(alias="BeginOffsetMillis")
    end_offset_millis: int = Field(alias="EndOffsetMillis")
    sentiment: Literal["NEGATIVE", "NEUTRAL", "POSITIVE"] = Field(alias="Sentiment")
    issues_detected: Optional[List[IssueDetectedModel]] = Field(
        default=None, alias="IssuesDetected"
    )


class RealtimeContactAnalysisSegmentModel(BaseModel):
    transcript: Optional[TranscriptModel] = Field(default=None, alias="Transcript")
    categories: Optional[CategoriesModel] = Field(default=None, alias="Categories")


class ListRealtimeContactAnalysisSegmentsResponseModel(BaseModel):
    segments: List[RealtimeContactAnalysisSegmentModel] = Field(alias="Segments")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
