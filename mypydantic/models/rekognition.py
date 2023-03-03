# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import (
    Any,
    Dict,
    IO,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AgeRangeModel(BaseModel):
    low: Optional[int] = Field(default=None, alias="Low")
    high: Optional[int] = Field(default=None, alias="High")


class AudioMetadataModel(BaseModel):
    codec: Optional[str] = Field(default=None, alias="Codec")
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")
    number_of_channels: Optional[int] = Field(default=None, alias="NumberOfChannels")


class BeardModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class BlackFrameModel(BaseModel):
    max_pixel_threshold: Optional[float] = Field(
        default=None, alias="MaxPixelThreshold"
    )
    min_coverage_percentage: Optional[float] = Field(
        default=None, alias="MinCoveragePercentage"
    )


class BoundingBoxModel(BaseModel):
    width: Optional[float] = Field(default=None, alias="Width")
    height: Optional[float] = Field(default=None, alias="Height")
    left: Optional[float] = Field(default=None, alias="Left")
    top: Optional[float] = Field(default=None, alias="Top")


class KnownGenderModel(BaseModel):
    type: Optional[Literal["Female", "Male", "Nonbinary", "Unlisted"]] = Field(
        default=None, alias="Type"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class EmotionModel(BaseModel):
    type: Optional[
        Literal[
            "ANGRY",
            "CALM",
            "CONFUSED",
            "DISGUSTED",
            "FEAR",
            "HAPPY",
            "SAD",
            "SURPRISED",
            "UNKNOWN",
        ]
    ] = Field(default=None, alias="Type")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class ImageQualityModel(BaseModel):
    brightness: Optional[float] = Field(default=None, alias="Brightness")
    sharpness: Optional[float] = Field(default=None, alias="Sharpness")


class LandmarkModel(BaseModel):
    type: Optional[
        Literal[
            "chinBottom",
            "eyeLeft",
            "eyeRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "leftEyeDown",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftPupil",
            "midJawlineLeft",
            "midJawlineRight",
            "mouthDown",
            "mouthLeft",
            "mouthRight",
            "mouthUp",
            "nose",
            "noseLeft",
            "noseRight",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "rightEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightPupil",
            "upperJawlineLeft",
            "upperJawlineRight",
        ]
    ] = Field(default=None, alias="Type")
    x: Optional[float] = Field(default=None, alias="X")
    y: Optional[float] = Field(default=None, alias="Y")


class PoseModel(BaseModel):
    roll: Optional[float] = Field(default=None, alias="Roll")
    yaw: Optional[float] = Field(default=None, alias="Yaw")
    pitch: Optional[float] = Field(default=None, alias="Pitch")


class SmileModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class ConnectedHomeSettingsForUpdateModel(BaseModel):
    labels: Optional[Sequence[str]] = Field(default=None, alias="Labels")
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")


class ConnectedHomeSettingsModel(BaseModel):
    labels: Sequence[str] = Field(alias="Labels")
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")


class ModerationLabelModel(BaseModel):
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    name: Optional[str] = Field(default=None, alias="Name")
    parent_name: Optional[str] = Field(default=None, alias="ParentName")


class OutputConfigModel(BaseModel):
    s3_bucket: Optional[str] = Field(default=None, alias="S3Bucket")
    s3_key_prefix: Optional[str] = Field(default=None, alias="S3KeyPrefix")


class CoversBodyPartModel(BaseModel):
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    value: Optional[bool] = Field(default=None, alias="Value")


class CreateCollectionRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class CreateProjectRequestModel(BaseModel):
    project_name: str = Field(alias="ProjectName")


class StreamProcessorDataSharingPreferenceModel(BaseModel):
    opt_in: bool = Field(alias="OptIn")


class StreamProcessorNotificationChannelModel(BaseModel):
    s_ns_topic_arn: str = Field(alias="SNSTopicArn")


class DatasetChangesModel(BaseModel):
    ground_truth: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="GroundTruth"
    )


class DatasetStatsModel(BaseModel):
    labeled_entries: Optional[int] = Field(default=None, alias="LabeledEntries")
    total_entries: Optional[int] = Field(default=None, alias="TotalEntries")
    total_labels: Optional[int] = Field(default=None, alias="TotalLabels")
    error_entries: Optional[int] = Field(default=None, alias="ErrorEntries")


class DatasetLabelStatsModel(BaseModel):
    entry_count: Optional[int] = Field(default=None, alias="EntryCount")
    bounding_box_count: Optional[int] = Field(default=None, alias="BoundingBoxCount")


class DatasetMetadataModel(BaseModel):
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    dataset_type: Optional[Literal["TEST", "TRAIN"]] = Field(
        default=None, alias="DatasetType"
    )
    dataset_arn: Optional[str] = Field(default=None, alias="DatasetArn")
    status: Optional[
        Literal[
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    status_message_code: Optional[
        Literal["CLIENT_ERROR", "SERVICE_ERROR", "SUCCESS"]
    ] = Field(default=None, alias="StatusMessageCode")


class DeleteCollectionRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")


class DeleteDatasetRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")


class DeleteFacesRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    face_ids: Sequence[str] = Field(alias="FaceIds")


class DeleteProjectPolicyRequestModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    policy_name: str = Field(alias="PolicyName")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")


class DeleteProjectRequestModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")


class DeleteProjectVersionRequestModel(BaseModel):
    project_version_arn: str = Field(alias="ProjectVersionArn")


class DeleteStreamProcessorRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DescribeCollectionRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")


class DescribeDatasetRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class WaiterConfigModel(BaseModel):
    delay: Optional[int] = Field(default=None, alias="Delay")
    max_attempts: Optional[int] = Field(default=None, alias="MaxAttempts")


class DescribeProjectVersionsRequestModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    version_names: Optional[Sequence[str]] = Field(default=None, alias="VersionNames")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class DescribeProjectsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    project_names: Optional[Sequence[str]] = Field(default=None, alias="ProjectNames")


class DescribeStreamProcessorRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DetectLabelsImageQualityModel(BaseModel):
    brightness: Optional[float] = Field(default=None, alias="Brightness")
    sharpness: Optional[float] = Field(default=None, alias="Sharpness")
    contrast: Optional[float] = Field(default=None, alias="Contrast")


class DominantColorModel(BaseModel):
    red: Optional[int] = Field(default=None, alias="Red")
    blue: Optional[int] = Field(default=None, alias="Blue")
    green: Optional[int] = Field(default=None, alias="Green")
    hex_code: Optional[str] = Field(default=None, alias="HexCode")
    cs_s_color: Optional[str] = Field(default=None, alias="CSSColor")
    simplified_color: Optional[str] = Field(default=None, alias="SimplifiedColor")
    pixel_percent: Optional[float] = Field(default=None, alias="PixelPercent")


class DetectLabelsImagePropertiesSettingsModel(BaseModel):
    max_dominant_colors: Optional[int] = Field(default=None, alias="MaxDominantColors")


class GeneralLabelsSettingsModel(BaseModel):
    label_inclusion_filters: Optional[Sequence[str]] = Field(
        default=None, alias="LabelInclusionFilters"
    )
    label_exclusion_filters: Optional[Sequence[str]] = Field(
        default=None, alias="LabelExclusionFilters"
    )
    label_category_inclusion_filters: Optional[Sequence[str]] = Field(
        default=None, alias="LabelCategoryInclusionFilters"
    )
    label_category_exclusion_filters: Optional[Sequence[str]] = Field(
        default=None, alias="LabelCategoryExclusionFilters"
    )


class HumanLoopActivationOutputModel(BaseModel):
    human_loop_arn: Optional[str] = Field(default=None, alias="HumanLoopArn")
    human_loop_activation_reasons: Optional[List[str]] = Field(
        default=None, alias="HumanLoopActivationReasons"
    )
    human_loop_activation_conditions_evaluation_results: Optional[str] = Field(
        default=None, alias="HumanLoopActivationConditionsEvaluationResults"
    )


class ProtectiveEquipmentSummarizationAttributesModel(BaseModel):
    min_confidence: float = Field(alias="MinConfidence")
    required_equipment_types: Sequence[
        Literal["FACE_COVER", "HAND_COVER", "HEAD_COVER"]
    ] = Field(alias="RequiredEquipmentTypes")


class ProtectiveEquipmentSummaryModel(BaseModel):
    persons_with_required_equipment: Optional[List[int]] = Field(
        default=None, alias="PersonsWithRequiredEquipment"
    )
    persons_without_required_equipment: Optional[List[int]] = Field(
        default=None, alias="PersonsWithoutRequiredEquipment"
    )
    persons_indeterminate: Optional[List[int]] = Field(
        default=None, alias="PersonsIndeterminate"
    )


class DetectionFilterModel(BaseModel):
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")
    min_bounding_box_height: Optional[float] = Field(
        default=None, alias="MinBoundingBoxHeight"
    )
    min_bounding_box_width: Optional[float] = Field(
        default=None, alias="MinBoundingBoxWidth"
    )


class DistributeDatasetModel(BaseModel):
    arn: str = Field(alias="Arn")


class EyeOpenModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class EyeglassesModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class GenderModel(BaseModel):
    value: Optional[Literal["Female", "Male"]] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class MouthOpenModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class MustacheModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class SunglassesModel(BaseModel):
    value: Optional[bool] = Field(default=None, alias="Value")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class FaceSearchSettingsModel(BaseModel):
    collection_id: Optional[str] = Field(default=None, alias="CollectionId")
    face_match_threshold: Optional[float] = Field(
        default=None, alias="FaceMatchThreshold"
    )


class PointModel(BaseModel):
    x: Optional[float] = Field(default=None, alias="X")
    y: Optional[float] = Field(default=None, alias="Y")


class GetCelebrityInfoRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetCelebrityRecognitionRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["ID", "TIMESTAMP"]] = Field(default=None, alias="SortBy")


class VideoMetadataModel(BaseModel):
    codec: Optional[str] = Field(default=None, alias="Codec")
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")
    format: Optional[str] = Field(default=None, alias="Format")
    frame_rate: Optional[float] = Field(default=None, alias="FrameRate")
    frame_height: Optional[int] = Field(default=None, alias="FrameHeight")
    frame_width: Optional[int] = Field(default=None, alias="FrameWidth")
    color_range: Optional[Literal["FULL", "LIMITED"]] = Field(
        default=None, alias="ColorRange"
    )


class GetContentModerationRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["NAME", "TIMESTAMP"]] = Field(
        default=None, alias="SortBy"
    )


class GetFaceDetectionRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class GetFaceSearchRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["INDEX", "TIMESTAMP"]] = Field(
        default=None, alias="SortBy"
    )


class GetLabelDetectionRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["NAME", "TIMESTAMP"]] = Field(
        default=None, alias="SortBy"
    )
    aggregate_by: Optional[Literal["SEGMENTS", "TIMESTAMPS"]] = Field(
        default=None, alias="AggregateBy"
    )


class GetPersonTrackingRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    sort_by: Optional[Literal["INDEX", "TIMESTAMP"]] = Field(
        default=None, alias="SortBy"
    )


class GetSegmentDetectionRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class SegmentTypeInfoModel(BaseModel):
    type: Optional[Literal["SHOT", "TECHNICAL_CUE"]] = Field(default=None, alias="Type")
    model_version: Optional[str] = Field(default=None, alias="ModelVersion")


class GetTextDetectionRequestModel(BaseModel):
    job_id: str = Field(alias="JobId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class S3ObjectModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[str] = Field(default=None, alias="Version")


class HumanLoopDataAttributesModel(BaseModel):
    content_classifiers: Optional[
        Sequence[
            Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
        ]
    ] = Field(default=None, alias="ContentClassifiers")


class KinesisDataStreamModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class KinesisVideoStreamStartSelectorModel(BaseModel):
    producer_timestamp: Optional[int] = Field(default=None, alias="ProducerTimestamp")
    fragment_number: Optional[str] = Field(default=None, alias="FragmentNumber")


class KinesisVideoStreamModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")


class LabelAliasModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class LabelCategoryModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class ParentModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class ListCollectionsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDatasetEntriesRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    contains_labels: Optional[Sequence[str]] = Field(
        default=None, alias="ContainsLabels"
    )
    labeled: Optional[bool] = Field(default=None, alias="Labeled")
    source_ref_contains: Optional[str] = Field(default=None, alias="SourceRefContains")
    has_errors: Optional[bool] = Field(default=None, alias="HasErrors")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDatasetLabelsRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFacesRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListProjectPoliciesRequestModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ProjectPolicyModel(BaseModel):
    project_arn: Optional[str] = Field(default=None, alias="ProjectArn")
    policy_name: Optional[str] = Field(default=None, alias="PolicyName")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")
    policy_document: Optional[str] = Field(default=None, alias="PolicyDocument")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )


class ListStreamProcessorsRequestModel(BaseModel):
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class StreamProcessorModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal["FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "UPDATING"]
    ] = Field(default=None, alias="Status")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class NotificationChannelModel(BaseModel):
    s_ns_topic_arn: str = Field(alias="SNSTopicArn")
    role_arn: str = Field(alias="RoleArn")


class PutProjectPolicyRequestModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    policy_name: str = Field(alias="PolicyName")
    policy_document: str = Field(alias="PolicyDocument")
    policy_revision_id: Optional[str] = Field(default=None, alias="PolicyRevisionId")


class S3DestinationModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="Bucket")
    key_prefix: Optional[str] = Field(default=None, alias="KeyPrefix")


class SearchFacesRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    face_id: str = Field(alias="FaceId")
    max_faces: Optional[int] = Field(default=None, alias="MaxFaces")
    face_match_threshold: Optional[float] = Field(
        default=None, alias="FaceMatchThreshold"
    )


class ShotSegmentModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class TechnicalCueSegmentModel(BaseModel):
    type: Optional[
        Literal[
            "BlackFrames",
            "ColorBars",
            "Content",
            "EndCredits",
            "OpeningCredits",
            "Slate",
            "StudioLogo",
        ]
    ] = Field(default=None, alias="Type")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class StartProjectVersionRequestModel(BaseModel):
    project_version_arn: str = Field(alias="ProjectVersionArn")
    min_inference_units: int = Field(alias="MinInferenceUnits")
    max_inference_units: Optional[int] = Field(default=None, alias="MaxInferenceUnits")


class StartShotDetectionFilterModel(BaseModel):
    min_segment_confidence: Optional[float] = Field(
        default=None, alias="MinSegmentConfidence"
    )


class StreamProcessingStopSelectorModel(BaseModel):
    max_duration_in_seconds: Optional[int] = Field(
        default=None, alias="MaxDurationInSeconds"
    )


class StopProjectVersionRequestModel(BaseModel):
    project_version_arn: str = Field(alias="ProjectVersionArn")


class StopStreamProcessorRequestModel(BaseModel):
    name: str = Field(alias="Name")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Mapping[str, str] = Field(alias="Tags")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class StartTechnicalCueDetectionFilterModel(BaseModel):
    min_segment_confidence: Optional[float] = Field(
        default=None, alias="MinSegmentConfidence"
    )
    black_frame: Optional[BlackFrameModel] = Field(default=None, alias="BlackFrame")


class ComparedSourceImageFaceModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class FaceModel(BaseModel):
    face_id: Optional[str] = Field(default=None, alias="FaceId")
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    image_id: Optional[str] = Field(default=None, alias="ImageId")
    external_image_id: Optional[str] = Field(default=None, alias="ExternalImageId")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    index_faces_model_version: Optional[str] = Field(
        default=None, alias="IndexFacesModelVersion"
    )


class CopyProjectVersionResponseModel(BaseModel):
    project_version_arn: str = Field(alias="ProjectVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateCollectionResponseModel(BaseModel):
    status_code: int = Field(alias="StatusCode")
    collection_arn: str = Field(alias="CollectionArn")
    face_model_version: str = Field(alias="FaceModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDatasetResponseModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectResponseModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectVersionResponseModel(BaseModel):
    project_version_arn: str = Field(alias="ProjectVersionArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateStreamProcessorResponseModel(BaseModel):
    stream_processor_arn: str = Field(alias="StreamProcessorArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteCollectionResponseModel(BaseModel):
    status_code: int = Field(alias="StatusCode")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFacesResponseModel(BaseModel):
    deleted_faces: List[str] = Field(alias="DeletedFaces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProjectResponseModel(BaseModel):
    status: Literal["CREATED", "CREATING", "DELETING"] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteProjectVersionResponseModel(BaseModel):
    status: Literal[
        "COPYING_COMPLETED",
        "COPYING_FAILED",
        "COPYING_IN_PROGRESS",
        "DELETING",
        "FAILED",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "TRAINING_COMPLETED",
        "TRAINING_FAILED",
        "TRAINING_IN_PROGRESS",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeCollectionResponseModel(BaseModel):
    face_count: int = Field(alias="FaceCount")
    face_model_version: str = Field(alias="FaceModelVersion")
    collection_arn: str = Field(alias="CollectionARN")
    creation_timestamp: datetime = Field(alias="CreationTimestamp")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCelebrityInfoResponseModel(BaseModel):
    urls: List[str] = Field(alias="Urls")
    name: str = Field(alias="Name")
    known_gender: KnownGenderModel = Field(alias="KnownGender")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListCollectionsResponseModel(BaseModel):
    collection_ids: List[str] = Field(alias="CollectionIds")
    next_token: str = Field(alias="NextToken")
    face_model_versions: List[str] = Field(alias="FaceModelVersions")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetEntriesResponseModel(BaseModel):
    dataset_entries: List[str] = Field(alias="DatasetEntries")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTagsForResourceResponseModel(BaseModel):
    tags: Dict[str, str] = Field(alias="Tags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutProjectPolicyResponseModel(BaseModel):
    policy_revision_id: str = Field(alias="PolicyRevisionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartCelebrityRecognitionResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartContentModerationResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFaceDetectionResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartFaceSearchResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartLabelDetectionResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartPersonTrackingResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartProjectVersionResponseModel(BaseModel):
    status: Literal[
        "COPYING_COMPLETED",
        "COPYING_FAILED",
        "COPYING_IN_PROGRESS",
        "DELETING",
        "FAILED",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "TRAINING_COMPLETED",
        "TRAINING_FAILED",
        "TRAINING_IN_PROGRESS",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSegmentDetectionResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartStreamProcessorResponseModel(BaseModel):
    session_id: str = Field(alias="SessionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartTextDetectionResponseModel(BaseModel):
    job_id: str = Field(alias="JobId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StopProjectVersionResponseModel(BaseModel):
    status: Literal[
        "COPYING_COMPLETED",
        "COPYING_FAILED",
        "COPYING_IN_PROGRESS",
        "DELETING",
        "FAILED",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "TRAINING_COMPLETED",
        "TRAINING_FAILED",
        "TRAINING_IN_PROGRESS",
    ] = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ComparedFaceModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    landmarks: Optional[List[LandmarkModel]] = Field(default=None, alias="Landmarks")
    pose: Optional[PoseModel] = Field(default=None, alias="Pose")
    quality: Optional[ImageQualityModel] = Field(default=None, alias="Quality")
    emotions: Optional[List[EmotionModel]] = Field(default=None, alias="Emotions")
    smile: Optional[SmileModel] = Field(default=None, alias="Smile")


class StreamProcessorSettingsForUpdateModel(BaseModel):
    connected_home_for_update: Optional[ConnectedHomeSettingsForUpdateModel] = Field(
        default=None, alias="ConnectedHomeForUpdate"
    )


class ContentModerationDetectionModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    moderation_label: Optional[ModerationLabelModel] = Field(
        default=None, alias="ModerationLabel"
    )


class CopyProjectVersionRequestModel(BaseModel):
    source_project_arn: str = Field(alias="SourceProjectArn")
    source_project_version_arn: str = Field(alias="SourceProjectVersionArn")
    destination_project_arn: str = Field(alias="DestinationProjectArn")
    version_name: str = Field(alias="VersionName")
    output_config: OutputConfigModel = Field(alias="OutputConfig")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class EquipmentDetectionModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    type: Optional[Literal["FACE_COVER", "HAND_COVER", "HEAD_COVER"]] = Field(
        default=None, alias="Type"
    )
    covers_body_part: Optional[CoversBodyPartModel] = Field(
        default=None, alias="CoversBodyPart"
    )


class UpdateDatasetEntriesRequestModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    changes: DatasetChangesModel = Field(alias="Changes")


class DatasetDescriptionModel(BaseModel):
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    last_updated_timestamp: Optional[datetime] = Field(
        default=None, alias="LastUpdatedTimestamp"
    )
    status: Optional[
        Literal[
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "CREATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    status_message_code: Optional[
        Literal["CLIENT_ERROR", "SERVICE_ERROR", "SUCCESS"]
    ] = Field(default=None, alias="StatusMessageCode")
    dataset_stats: Optional[DatasetStatsModel] = Field(
        default=None, alias="DatasetStats"
    )


class DatasetLabelDescriptionModel(BaseModel):
    label_name: Optional[str] = Field(default=None, alias="LabelName")
    label_stats: Optional[DatasetLabelStatsModel] = Field(
        default=None, alias="LabelStats"
    )


class ProjectDescriptionModel(BaseModel):
    project_arn: Optional[str] = Field(default=None, alias="ProjectArn")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    status: Optional[Literal["CREATED", "CREATING", "DELETING"]] = Field(
        default=None, alias="Status"
    )
    datasets: Optional[List[DatasetMetadataModel]] = Field(
        default=None, alias="Datasets"
    )


class DescribeProjectVersionsRequestDescribeProjectVersionsPaginateModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    version_names: Optional[Sequence[str]] = Field(default=None, alias="VersionNames")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeProjectsRequestDescribeProjectsPaginateModel(BaseModel):
    project_names: Optional[Sequence[str]] = Field(default=None, alias="ProjectNames")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListCollectionsRequestListCollectionsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetEntriesRequestListDatasetEntriesPaginateModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    contains_labels: Optional[Sequence[str]] = Field(
        default=None, alias="ContainsLabels"
    )
    labeled: Optional[bool] = Field(default=None, alias="Labeled")
    source_ref_contains: Optional[str] = Field(default=None, alias="SourceRefContains")
    has_errors: Optional[bool] = Field(default=None, alias="HasErrors")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDatasetLabelsRequestListDatasetLabelsPaginateModel(BaseModel):
    dataset_arn: str = Field(alias="DatasetArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFacesRequestListFacesPaginateModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListProjectPoliciesRequestListProjectPoliciesPaginateModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListStreamProcessorsRequestListStreamProcessorsPaginateModel(BaseModel):
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeProjectVersionsRequestProjectVersionRunningWaitModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    version_names: Optional[Sequence[str]] = Field(default=None, alias="VersionNames")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DescribeProjectVersionsRequestProjectVersionTrainingCompletedWaitModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    version_names: Optional[Sequence[str]] = Field(default=None, alias="VersionNames")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    waiter_config: Optional[WaiterConfigModel] = Field(
        default=None, alias="WaiterConfig"
    )


class DetectLabelsImageBackgroundModel(BaseModel):
    quality: Optional[DetectLabelsImageQualityModel] = Field(
        default=None, alias="Quality"
    )
    dominant_colors: Optional[List[DominantColorModel]] = Field(
        default=None, alias="DominantColors"
    )


class DetectLabelsImageForegroundModel(BaseModel):
    quality: Optional[DetectLabelsImageQualityModel] = Field(
        default=None, alias="Quality"
    )
    dominant_colors: Optional[List[DominantColorModel]] = Field(
        default=None, alias="DominantColors"
    )


class InstanceModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    dominant_colors: Optional[List[DominantColorModel]] = Field(
        default=None, alias="DominantColors"
    )


class DetectLabelsSettingsModel(BaseModel):
    general_labels: Optional[GeneralLabelsSettingsModel] = Field(
        default=None, alias="GeneralLabels"
    )
    image_properties: Optional[DetectLabelsImagePropertiesSettingsModel] = Field(
        default=None, alias="ImageProperties"
    )


class LabelDetectionSettingsModel(BaseModel):
    general_labels: Optional[GeneralLabelsSettingsModel] = Field(
        default=None, alias="GeneralLabels"
    )


class DetectModerationLabelsResponseModel(BaseModel):
    moderation_labels: List[ModerationLabelModel] = Field(alias="ModerationLabels")
    moderation_model_version: str = Field(alias="ModerationModelVersion")
    human_loop_activation_output: HumanLoopActivationOutputModel = Field(
        alias="HumanLoopActivationOutput"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DistributeDatasetEntriesRequestModel(BaseModel):
    datasets: Sequence[DistributeDatasetModel] = Field(alias="Datasets")


class FaceDetailModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    age_range: Optional[AgeRangeModel] = Field(default=None, alias="AgeRange")
    smile: Optional[SmileModel] = Field(default=None, alias="Smile")
    eyeglasses: Optional[EyeglassesModel] = Field(default=None, alias="Eyeglasses")
    sunglasses: Optional[SunglassesModel] = Field(default=None, alias="Sunglasses")
    gender: Optional[GenderModel] = Field(default=None, alias="Gender")
    beard: Optional[BeardModel] = Field(default=None, alias="Beard")
    mustache: Optional[MustacheModel] = Field(default=None, alias="Mustache")
    eyes_open: Optional[EyeOpenModel] = Field(default=None, alias="EyesOpen")
    mouth_open: Optional[MouthOpenModel] = Field(default=None, alias="MouthOpen")
    emotions: Optional[List[EmotionModel]] = Field(default=None, alias="Emotions")
    landmarks: Optional[List[LandmarkModel]] = Field(default=None, alias="Landmarks")
    pose: Optional[PoseModel] = Field(default=None, alias="Pose")
    quality: Optional[ImageQualityModel] = Field(default=None, alias="Quality")
    confidence: Optional[float] = Field(default=None, alias="Confidence")


class StreamProcessorSettingsModel(BaseModel):
    face_search: Optional[FaceSearchSettingsModel] = Field(
        default=None, alias="FaceSearch"
    )
    connected_home: Optional[ConnectedHomeSettingsModel] = Field(
        default=None, alias="ConnectedHome"
    )


class GeometryModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    polygon: Optional[List[PointModel]] = Field(default=None, alias="Polygon")


class RegionOfInterestModel(BaseModel):
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    polygon: Optional[Sequence[PointModel]] = Field(default=None, alias="Polygon")


class GroundTruthManifestModel(BaseModel):
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="S3Object")


class ImageModel(BaseModel):
    bytes: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="Bytes"
    )
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="S3Object")


class SummaryModel(BaseModel):
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="S3Object")


class VideoModel(BaseModel):
    s3_object: Optional[S3ObjectModel] = Field(default=None, alias="S3Object")


class HumanLoopConfigModel(BaseModel):
    human_loop_name: str = Field(alias="HumanLoopName")
    flow_definition_arn: str = Field(alias="FlowDefinitionArn")
    data_attributes: Optional[HumanLoopDataAttributesModel] = Field(
        default=None, alias="DataAttributes"
    )


class StreamProcessingStartSelectorModel(BaseModel):
    kvs_stream_start_selector: Optional[KinesisVideoStreamStartSelectorModel] = Field(
        default=None, alias="KVSStreamStartSelector"
    )


class StreamProcessorInputModel(BaseModel):
    kinesis_video_stream: Optional[KinesisVideoStreamModel] = Field(
        default=None, alias="KinesisVideoStream"
    )


class ListProjectPoliciesResponseModel(BaseModel):
    project_policies: List[ProjectPolicyModel] = Field(alias="ProjectPolicies")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListStreamProcessorsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    stream_processors: List[StreamProcessorModel] = Field(alias="StreamProcessors")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StreamProcessorOutputModel(BaseModel):
    kinesis_data_stream: Optional[KinesisDataStreamModel] = Field(
        default=None, alias="KinesisDataStream"
    )
    s3_destination: Optional[S3DestinationModel] = Field(
        default=None, alias="S3Destination"
    )


class SegmentDetectionModel(BaseModel):
    type: Optional[Literal["SHOT", "TECHNICAL_CUE"]] = Field(default=None, alias="Type")
    start_timestamp_millis: Optional[int] = Field(
        default=None, alias="StartTimestampMillis"
    )
    end_timestamp_millis: Optional[int] = Field(
        default=None, alias="EndTimestampMillis"
    )
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")
    start_timecode_s_mp_te: Optional[str] = Field(
        default=None, alias="StartTimecodeSMPTE"
    )
    end_timecode_s_mp_te: Optional[str] = Field(default=None, alias="EndTimecodeSMPTE")
    duration_s_mp_te: Optional[str] = Field(default=None, alias="DurationSMPTE")
    technical_cue_segment: Optional[TechnicalCueSegmentModel] = Field(
        default=None, alias="TechnicalCueSegment"
    )
    shot_segment: Optional[ShotSegmentModel] = Field(default=None, alias="ShotSegment")
    start_frame_number: Optional[int] = Field(default=None, alias="StartFrameNumber")
    end_frame_number: Optional[int] = Field(default=None, alias="EndFrameNumber")
    duration_frames: Optional[int] = Field(default=None, alias="DurationFrames")


class StartSegmentDetectionFiltersModel(BaseModel):
    technical_cue_filter: Optional[StartTechnicalCueDetectionFilterModel] = Field(
        default=None, alias="TechnicalCueFilter"
    )
    shot_filter: Optional[StartShotDetectionFilterModel] = Field(
        default=None, alias="ShotFilter"
    )


class FaceMatchModel(BaseModel):
    similarity: Optional[float] = Field(default=None, alias="Similarity")
    face: Optional[FaceModel] = Field(default=None, alias="Face")


class ListFacesResponseModel(BaseModel):
    faces: List[FaceModel] = Field(alias="Faces")
    next_token: str = Field(alias="NextToken")
    face_model_version: str = Field(alias="FaceModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CelebrityModel(BaseModel):
    urls: Optional[List[str]] = Field(default=None, alias="Urls")
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    face: Optional[ComparedFaceModel] = Field(default=None, alias="Face")
    match_confidence: Optional[float] = Field(default=None, alias="MatchConfidence")
    known_gender: Optional[KnownGenderModel] = Field(default=None, alias="KnownGender")


class CompareFacesMatchModel(BaseModel):
    similarity: Optional[float] = Field(default=None, alias="Similarity")
    face: Optional[ComparedFaceModel] = Field(default=None, alias="Face")


class GetContentModerationResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    video_metadata: VideoMetadataModel = Field(alias="VideoMetadata")
    moderation_labels: List[ContentModerationDetectionModel] = Field(
        alias="ModerationLabels"
    )
    next_token: str = Field(alias="NextToken")
    moderation_model_version: str = Field(alias="ModerationModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProtectiveEquipmentBodyPartModel(BaseModel):
    name: Optional[Literal["FACE", "HEAD", "LEFT_HAND", "RIGHT_HAND"]] = Field(
        default=None, alias="Name"
    )
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    equipment_detections: Optional[List[EquipmentDetectionModel]] = Field(
        default=None, alias="EquipmentDetections"
    )


class DescribeDatasetResponseModel(BaseModel):
    dataset_description: DatasetDescriptionModel = Field(alias="DatasetDescription")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDatasetLabelsResponseModel(BaseModel):
    dataset_label_descriptions: List[DatasetLabelDescriptionModel] = Field(
        alias="DatasetLabelDescriptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeProjectsResponseModel(BaseModel):
    project_descriptions: List[ProjectDescriptionModel] = Field(
        alias="ProjectDescriptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectLabelsImagePropertiesModel(BaseModel):
    quality: Optional[DetectLabelsImageQualityModel] = Field(
        default=None, alias="Quality"
    )
    dominant_colors: Optional[List[DominantColorModel]] = Field(
        default=None, alias="DominantColors"
    )
    foreground: Optional[DetectLabelsImageForegroundModel] = Field(
        default=None, alias="Foreground"
    )
    background: Optional[DetectLabelsImageBackgroundModel] = Field(
        default=None, alias="Background"
    )


class LabelModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    instances: Optional[List[InstanceModel]] = Field(default=None, alias="Instances")
    parents: Optional[List[ParentModel]] = Field(default=None, alias="Parents")
    aliases: Optional[List[LabelAliasModel]] = Field(default=None, alias="Aliases")
    categories: Optional[List[LabelCategoryModel]] = Field(
        default=None, alias="Categories"
    )


class CelebrityDetailModel(BaseModel):
    urls: Optional[List[str]] = Field(default=None, alias="Urls")
    name: Optional[str] = Field(default=None, alias="Name")
    id: Optional[str] = Field(default=None, alias="Id")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    face: Optional[FaceDetailModel] = Field(default=None, alias="Face")
    known_gender: Optional[KnownGenderModel] = Field(default=None, alias="KnownGender")


class DetectFacesResponseModel(BaseModel):
    face_details: List[FaceDetailModel] = Field(alias="FaceDetails")
    orientation_correction: Literal[
        "ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"
    ] = Field(alias="OrientationCorrection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FaceDetectionModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    face: Optional[FaceDetailModel] = Field(default=None, alias="Face")


class FaceRecordModel(BaseModel):
    face: Optional[FaceModel] = Field(default=None, alias="Face")
    face_detail: Optional[FaceDetailModel] = Field(default=None, alias="FaceDetail")


class PersonDetailModel(BaseModel):
    index: Optional[int] = Field(default=None, alias="Index")
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    face: Optional[FaceDetailModel] = Field(default=None, alias="Face")


class UnindexedFaceModel(BaseModel):
    reasons: Optional[
        List[
            Literal[
                "EXCEEDS_MAX_FACES",
                "EXTREME_POSE",
                "LOW_BRIGHTNESS",
                "LOW_CONFIDENCE",
                "LOW_FACE_QUALITY",
                "LOW_SHARPNESS",
                "SMALL_BOUNDING_BOX",
            ]
        ]
    ] = Field(default=None, alias="Reasons")
    face_detail: Optional[FaceDetailModel] = Field(default=None, alias="FaceDetail")


class CustomLabelModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    geometry: Optional[GeometryModel] = Field(default=None, alias="Geometry")


class TextDetectionModel(BaseModel):
    detected_text: Optional[str] = Field(default=None, alias="DetectedText")
    type: Optional[Literal["LINE", "WORD"]] = Field(default=None, alias="Type")
    id: Optional[int] = Field(default=None, alias="Id")
    parent_id: Optional[int] = Field(default=None, alias="ParentId")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    geometry: Optional[GeometryModel] = Field(default=None, alias="Geometry")


class DetectTextFiltersModel(BaseModel):
    word_filter: Optional[DetectionFilterModel] = Field(
        default=None, alias="WordFilter"
    )
    regions_of_interest: Optional[Sequence[RegionOfInterestModel]] = Field(
        default=None, alias="RegionsOfInterest"
    )


class StartTextDetectionFiltersModel(BaseModel):
    word_filter: Optional[DetectionFilterModel] = Field(
        default=None, alias="WordFilter"
    )
    regions_of_interest: Optional[Sequence[RegionOfInterestModel]] = Field(
        default=None, alias="RegionsOfInterest"
    )


class UpdateStreamProcessorRequestModel(BaseModel):
    name: str = Field(alias="Name")
    settings_for_update: Optional[StreamProcessorSettingsForUpdateModel] = Field(
        default=None, alias="SettingsForUpdate"
    )
    regions_of_interest_for_update: Optional[Sequence[RegionOfInterestModel]] = Field(
        default=None, alias="RegionsOfInterestForUpdate"
    )
    data_sharing_preference_for_update: Optional[
        StreamProcessorDataSharingPreferenceModel
    ] = Field(default=None, alias="DataSharingPreferenceForUpdate")
    parameters_to_delete: Optional[
        Sequence[Literal["ConnectedHomeMinConfidence", "RegionsOfInterest"]]
    ] = Field(default=None, alias="ParametersToDelete")


class AssetModel(BaseModel):
    ground_truth_manifest: Optional[GroundTruthManifestModel] = Field(
        default=None, alias="GroundTruthManifest"
    )


class DatasetSourceModel(BaseModel):
    ground_truth_manifest: Optional[GroundTruthManifestModel] = Field(
        default=None, alias="GroundTruthManifest"
    )
    dataset_arn: Optional[str] = Field(default=None, alias="DatasetArn")


class CompareFacesRequestModel(BaseModel):
    source_image: ImageModel = Field(alias="SourceImage")
    target_image: ImageModel = Field(alias="TargetImage")
    similarity_threshold: Optional[float] = Field(
        default=None, alias="SimilarityThreshold"
    )
    quality_filter: Optional[Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]] = Field(
        default=None, alias="QualityFilter"
    )


class DetectCustomLabelsRequestModel(BaseModel):
    project_version_arn: str = Field(alias="ProjectVersionArn")
    image: ImageModel = Field(alias="Image")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")


class DetectFacesRequestModel(BaseModel):
    image: ImageModel = Field(alias="Image")
    attributes: Optional[Sequence[Literal["ALL", "DEFAULT"]]] = Field(
        default=None, alias="Attributes"
    )


class DetectLabelsRequestModel(BaseModel):
    image: ImageModel = Field(alias="Image")
    max_labels: Optional[int] = Field(default=None, alias="MaxLabels")
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")
    features: Optional[Sequence[Literal["GENERAL_LABELS", "IMAGE_PROPERTIES"]]] = Field(
        default=None, alias="Features"
    )
    settings: Optional[DetectLabelsSettingsModel] = Field(
        default=None, alias="Settings"
    )


class DetectProtectiveEquipmentRequestModel(BaseModel):
    image: ImageModel = Field(alias="Image")
    summarization_attributes: Optional[
        ProtectiveEquipmentSummarizationAttributesModel
    ] = Field(default=None, alias="SummarizationAttributes")


class IndexFacesRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    image: ImageModel = Field(alias="Image")
    external_image_id: Optional[str] = Field(default=None, alias="ExternalImageId")
    detection_attributes: Optional[Sequence[Literal["ALL", "DEFAULT"]]] = Field(
        default=None, alias="DetectionAttributes"
    )
    max_faces: Optional[int] = Field(default=None, alias="MaxFaces")
    quality_filter: Optional[Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]] = Field(
        default=None, alias="QualityFilter"
    )


class RecognizeCelebritiesRequestModel(BaseModel):
    image: ImageModel = Field(alias="Image")


class SearchFacesByImageRequestModel(BaseModel):
    collection_id: str = Field(alias="CollectionId")
    image: ImageModel = Field(alias="Image")
    max_faces: Optional[int] = Field(default=None, alias="MaxFaces")
    face_match_threshold: Optional[float] = Field(
        default=None, alias="FaceMatchThreshold"
    )
    quality_filter: Optional[Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]] = Field(
        default=None, alias="QualityFilter"
    )


class EvaluationResultModel(BaseModel):
    f1_score: Optional[float] = Field(default=None, alias="F1Score")
    summary: Optional[SummaryModel] = Field(default=None, alias="Summary")


class StartCelebrityRecognitionRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")


class StartContentModerationRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")


class StartFaceDetectionRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    face_attributes: Optional[Literal["ALL", "DEFAULT"]] = Field(
        default=None, alias="FaceAttributes"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")


class StartFaceSearchRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    collection_id: str = Field(alias="CollectionId")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    face_match_threshold: Optional[float] = Field(
        default=None, alias="FaceMatchThreshold"
    )
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")


class StartLabelDetectionRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")
    features: Optional[Sequence[Literal["GENERAL_LABELS"]]] = Field(
        default=None, alias="Features"
    )
    settings: Optional[LabelDetectionSettingsModel] = Field(
        default=None, alias="Settings"
    )


class StartPersonTrackingRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")


class DetectModerationLabelsRequestModel(BaseModel):
    image: ImageModel = Field(alias="Image")
    min_confidence: Optional[float] = Field(default=None, alias="MinConfidence")
    human_loop_config: Optional[HumanLoopConfigModel] = Field(
        default=None, alias="HumanLoopConfig"
    )


class StartStreamProcessorRequestModel(BaseModel):
    name: str = Field(alias="Name")
    start_selector: Optional[StreamProcessingStartSelectorModel] = Field(
        default=None, alias="StartSelector"
    )
    stop_selector: Optional[StreamProcessingStopSelectorModel] = Field(
        default=None, alias="StopSelector"
    )


class CreateStreamProcessorRequestModel(BaseModel):
    input: StreamProcessorInputModel = Field(alias="Input")
    output: StreamProcessorOutputModel = Field(alias="Output")
    name: str = Field(alias="Name")
    settings: StreamProcessorSettingsModel = Field(alias="Settings")
    role_arn: str = Field(alias="RoleArn")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    notification_channel: Optional[StreamProcessorNotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    regions_of_interest: Optional[Sequence[RegionOfInterestModel]] = Field(
        default=None, alias="RegionsOfInterest"
    )
    data_sharing_preference: Optional[
        StreamProcessorDataSharingPreferenceModel
    ] = Field(default=None, alias="DataSharingPreference")


class DescribeStreamProcessorResponseModel(BaseModel):
    name: str = Field(alias="Name")
    stream_processor_arn: str = Field(alias="StreamProcessorArn")
    status: Literal[
        "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "UPDATING"
    ] = Field(alias="Status")
    status_message: str = Field(alias="StatusMessage")
    creation_timestamp: datetime = Field(alias="CreationTimestamp")
    last_update_timestamp: datetime = Field(alias="LastUpdateTimestamp")
    input: StreamProcessorInputModel = Field(alias="Input")
    output: StreamProcessorOutputModel = Field(alias="Output")
    role_arn: str = Field(alias="RoleArn")
    settings: StreamProcessorSettingsModel = Field(alias="Settings")
    notification_channel: StreamProcessorNotificationChannelModel = Field(
        alias="NotificationChannel"
    )
    kms_key_id: str = Field(alias="KmsKeyId")
    regions_of_interest: List[RegionOfInterestModel] = Field(alias="RegionsOfInterest")
    data_sharing_preference: StreamProcessorDataSharingPreferenceModel = Field(
        alias="DataSharingPreference"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSegmentDetectionResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    video_metadata: List[VideoMetadataModel] = Field(alias="VideoMetadata")
    audio_metadata: List[AudioMetadataModel] = Field(alias="AudioMetadata")
    next_token: str = Field(alias="NextToken")
    segments: List[SegmentDetectionModel] = Field(alias="Segments")
    selected_segment_types: List[SegmentTypeInfoModel] = Field(
        alias="SelectedSegmentTypes"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class StartSegmentDetectionRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    segment_types: Sequence[Literal["SHOT", "TECHNICAL_CUE"]] = Field(
        alias="SegmentTypes"
    )
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")
    filters: Optional[StartSegmentDetectionFiltersModel] = Field(
        default=None, alias="Filters"
    )


class SearchFacesByImageResponseModel(BaseModel):
    searched_face_bounding_box: BoundingBoxModel = Field(
        alias="SearchedFaceBoundingBox"
    )
    searched_face_confidence: float = Field(alias="SearchedFaceConfidence")
    face_matches: List[FaceMatchModel] = Field(alias="FaceMatches")
    face_model_version: str = Field(alias="FaceModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchFacesResponseModel(BaseModel):
    searched_face_id: str = Field(alias="SearchedFaceId")
    face_matches: List[FaceMatchModel] = Field(alias="FaceMatches")
    face_model_version: str = Field(alias="FaceModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RecognizeCelebritiesResponseModel(BaseModel):
    celebrity_faces: List[CelebrityModel] = Field(alias="CelebrityFaces")
    unrecognized_faces: List[ComparedFaceModel] = Field(alias="UnrecognizedFaces")
    orientation_correction: Literal[
        "ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"
    ] = Field(alias="OrientationCorrection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CompareFacesResponseModel(BaseModel):
    source_image_face: ComparedSourceImageFaceModel = Field(alias="SourceImageFace")
    face_matches: List[CompareFacesMatchModel] = Field(alias="FaceMatches")
    unmatched_faces: List[ComparedFaceModel] = Field(alias="UnmatchedFaces")
    source_image_orientation_correction: Literal[
        "ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"
    ] = Field(alias="SourceImageOrientationCorrection")
    target_image_orientation_correction: Literal[
        "ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"
    ] = Field(alias="TargetImageOrientationCorrection")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ProtectiveEquipmentPersonModel(BaseModel):
    body_parts: Optional[List[ProtectiveEquipmentBodyPartModel]] = Field(
        default=None, alias="BodyParts"
    )
    bounding_box: Optional[BoundingBoxModel] = Field(default=None, alias="BoundingBox")
    confidence: Optional[float] = Field(default=None, alias="Confidence")
    id: Optional[int] = Field(default=None, alias="Id")


class DetectLabelsResponseModel(BaseModel):
    labels: List[LabelModel] = Field(alias="Labels")
    orientation_correction: Literal[
        "ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"
    ] = Field(alias="OrientationCorrection")
    label_model_version: str = Field(alias="LabelModelVersion")
    image_properties: DetectLabelsImagePropertiesModel = Field(alias="ImageProperties")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LabelDetectionModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    label: Optional[LabelModel] = Field(default=None, alias="Label")
    start_timestamp_millis: Optional[int] = Field(
        default=None, alias="StartTimestampMillis"
    )
    end_timestamp_millis: Optional[int] = Field(
        default=None, alias="EndTimestampMillis"
    )
    duration_millis: Optional[int] = Field(default=None, alias="DurationMillis")


class CelebrityRecognitionModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    celebrity: Optional[CelebrityDetailModel] = Field(default=None, alias="Celebrity")


class GetFaceDetectionResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    video_metadata: VideoMetadataModel = Field(alias="VideoMetadata")
    next_token: str = Field(alias="NextToken")
    faces: List[FaceDetectionModel] = Field(alias="Faces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PersonDetectionModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    person: Optional[PersonDetailModel] = Field(default=None, alias="Person")


class PersonMatchModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    person: Optional[PersonDetailModel] = Field(default=None, alias="Person")
    face_matches: Optional[List[FaceMatchModel]] = Field(
        default=None, alias="FaceMatches"
    )


class IndexFacesResponseModel(BaseModel):
    face_records: List[FaceRecordModel] = Field(alias="FaceRecords")
    orientation_correction: Literal[
        "ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"
    ] = Field(alias="OrientationCorrection")
    face_model_version: str = Field(alias="FaceModelVersion")
    unindexed_faces: List[UnindexedFaceModel] = Field(alias="UnindexedFaces")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectCustomLabelsResponseModel(BaseModel):
    custom_labels: List[CustomLabelModel] = Field(alias="CustomLabels")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DetectTextResponseModel(BaseModel):
    text_detections: List[TextDetectionModel] = Field(alias="TextDetections")
    text_model_version: str = Field(alias="TextModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TextDetectionResultModel(BaseModel):
    timestamp: Optional[int] = Field(default=None, alias="Timestamp")
    text_detection: Optional[TextDetectionModel] = Field(
        default=None, alias="TextDetection"
    )


class DetectTextRequestModel(BaseModel):
    image: ImageModel = Field(alias="Image")
    filters: Optional[DetectTextFiltersModel] = Field(default=None, alias="Filters")


class StartTextDetectionRequestModel(BaseModel):
    video: VideoModel = Field(alias="Video")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    notification_channel: Optional[NotificationChannelModel] = Field(
        default=None, alias="NotificationChannel"
    )
    job_tag: Optional[str] = Field(default=None, alias="JobTag")
    filters: Optional[StartTextDetectionFiltersModel] = Field(
        default=None, alias="Filters"
    )


class TestingDataModel(BaseModel):
    assets: Optional[Sequence[AssetModel]] = Field(default=None, alias="Assets")
    auto_create: Optional[bool] = Field(default=None, alias="AutoCreate")


class TrainingDataModel(BaseModel):
    assets: Optional[Sequence[AssetModel]] = Field(default=None, alias="Assets")


class ValidationDataModel(BaseModel):
    assets: Optional[List[AssetModel]] = Field(default=None, alias="Assets")


class CreateDatasetRequestModel(BaseModel):
    dataset_type: Literal["TEST", "TRAIN"] = Field(alias="DatasetType")
    project_arn: str = Field(alias="ProjectArn")
    dataset_source: Optional[DatasetSourceModel] = Field(
        default=None, alias="DatasetSource"
    )


class DetectProtectiveEquipmentResponseModel(BaseModel):
    protective_equipment_model_version: str = Field(
        alias="ProtectiveEquipmentModelVersion"
    )
    persons: List[ProtectiveEquipmentPersonModel] = Field(alias="Persons")
    summary: ProtectiveEquipmentSummaryModel = Field(alias="Summary")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetLabelDetectionResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    video_metadata: VideoMetadataModel = Field(alias="VideoMetadata")
    next_token: str = Field(alias="NextToken")
    labels: List[LabelDetectionModel] = Field(alias="Labels")
    label_model_version: str = Field(alias="LabelModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetCelebrityRecognitionResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    video_metadata: VideoMetadataModel = Field(alias="VideoMetadata")
    next_token: str = Field(alias="NextToken")
    celebrities: List[CelebrityRecognitionModel] = Field(alias="Celebrities")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPersonTrackingResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    video_metadata: VideoMetadataModel = Field(alias="VideoMetadata")
    next_token: str = Field(alias="NextToken")
    persons: List[PersonDetectionModel] = Field(alias="Persons")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFaceSearchResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    next_token: str = Field(alias="NextToken")
    video_metadata: VideoMetadataModel = Field(alias="VideoMetadata")
    persons: List[PersonMatchModel] = Field(alias="Persons")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetTextDetectionResponseModel(BaseModel):
    job_status: Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"] = Field(alias="JobStatus")
    status_message: str = Field(alias="StatusMessage")
    video_metadata: VideoMetadataModel = Field(alias="VideoMetadata")
    text_detections: List[TextDetectionResultModel] = Field(alias="TextDetections")
    next_token: str = Field(alias="NextToken")
    text_model_version: str = Field(alias="TextModelVersion")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateProjectVersionRequestModel(BaseModel):
    project_arn: str = Field(alias="ProjectArn")
    version_name: str = Field(alias="VersionName")
    output_config: OutputConfigModel = Field(alias="OutputConfig")
    training_data: Optional[TrainingDataModel] = Field(
        default=None, alias="TrainingData"
    )
    testing_data: Optional[TestingDataModel] = Field(default=None, alias="TestingData")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")


class TestingDataResultModel(BaseModel):
    input: Optional[TestingDataModel] = Field(default=None, alias="Input")
    output: Optional[TestingDataModel] = Field(default=None, alias="Output")
    validation: Optional[ValidationDataModel] = Field(default=None, alias="Validation")


class TrainingDataResultModel(BaseModel):
    input: Optional[TrainingDataModel] = Field(default=None, alias="Input")
    output: Optional[TrainingDataModel] = Field(default=None, alias="Output")
    validation: Optional[ValidationDataModel] = Field(default=None, alias="Validation")


class ProjectVersionDescriptionModel(BaseModel):
    project_version_arn: Optional[str] = Field(default=None, alias="ProjectVersionArn")
    creation_timestamp: Optional[datetime] = Field(
        default=None, alias="CreationTimestamp"
    )
    min_inference_units: Optional[int] = Field(default=None, alias="MinInferenceUnits")
    status: Optional[
        Literal[
            "COPYING_COMPLETED",
            "COPYING_FAILED",
            "COPYING_IN_PROGRESS",
            "DELETING",
            "FAILED",
            "RUNNING",
            "STARTING",
            "STOPPED",
            "STOPPING",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "TRAINING_IN_PROGRESS",
        ]
    ] = Field(default=None, alias="Status")
    status_message: Optional[str] = Field(default=None, alias="StatusMessage")
    billable_training_time_in_seconds: Optional[int] = Field(
        default=None, alias="BillableTrainingTimeInSeconds"
    )
    training_end_timestamp: Optional[datetime] = Field(
        default=None, alias="TrainingEndTimestamp"
    )
    output_config: Optional[OutputConfigModel] = Field(
        default=None, alias="OutputConfig"
    )
    training_data_result: Optional[TrainingDataResultModel] = Field(
        default=None, alias="TrainingDataResult"
    )
    testing_data_result: Optional[TestingDataResultModel] = Field(
        default=None, alias="TestingDataResult"
    )
    evaluation_result: Optional[EvaluationResultModel] = Field(
        default=None, alias="EvaluationResult"
    )
    manifest_summary: Optional[GroundTruthManifestModel] = Field(
        default=None, alias="ManifestSummary"
    )
    kms_key_id: Optional[str] = Field(default=None, alias="KmsKeyId")
    max_inference_units: Optional[int] = Field(default=None, alias="MaxInferenceUnits")
    source_project_version_arn: Optional[str] = Field(
        default=None, alias="SourceProjectVersionArn"
    )


class DescribeProjectVersionsResponseModel(BaseModel):
    project_version_descriptions: List[ProjectVersionDescriptionModel] = Field(
        alias="ProjectVersionDescriptions"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
