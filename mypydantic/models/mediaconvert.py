# Model Generated: Thu Mar  2 21:56:21 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AacSettingsModel(BaseModel):
    audio_description_broadcaster_mix: Optional[
        Literal["BROADCASTER_MIXED_AD", "NORMAL"]
    ] = Field(default=None, alias="AudioDescriptionBroadcasterMix")
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    codec_profile: Optional[Literal["HEV1", "HEV2", "LC"]] = Field(
        default=None, alias="CodecProfile"
    )
    coding_mode: Optional[
        Literal[
            "AD_RECEIVER_MIX",
            "CODING_MODE_1_0",
            "CODING_MODE_1_1",
            "CODING_MODE_2_0",
            "CODING_MODE_5_1",
        ]
    ] = Field(default=None, alias="CodingMode")
    rate_control_mode: Optional[Literal["CBR", "VBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    raw_format: Optional[Literal["LATM_LOAS", "NONE"]] = Field(
        default=None, alias="RawFormat"
    )
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")
    specification: Optional[Literal["MPEG2", "MPEG4"]] = Field(
        default=None, alias="Specification"
    )
    vbr_quality: Optional[Literal["HIGH", "LOW", "MEDIUM_HIGH", "MEDIUM_LOW"]] = Field(
        default=None, alias="VbrQuality"
    )


class Ac3SettingsModel(BaseModel):
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    bitstream_mode: Optional[
        Literal[
            "COMMENTARY",
            "COMPLETE_MAIN",
            "DIALOGUE",
            "EMERGENCY",
            "HEARING_IMPAIRED",
            "MUSIC_AND_EFFECTS",
            "VISUALLY_IMPAIRED",
            "VOICE_OVER",
        ]
    ] = Field(default=None, alias="BitstreamMode")
    coding_mode: Optional[
        Literal[
            "CODING_MODE_1_0",
            "CODING_MODE_1_1",
            "CODING_MODE_2_0",
            "CODING_MODE_3_2_LFE",
        ]
    ] = Field(default=None, alias="CodingMode")
    dialnorm: Optional[int] = Field(default=None, alias="Dialnorm")
    dynamic_range_compression_line: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DynamicRangeCompressionLine")
    dynamic_range_compression_profile: Optional[
        Literal["FILM_STANDARD", "NONE"]
    ] = Field(default=None, alias="DynamicRangeCompressionProfile")
    dynamic_range_compression_rf: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DynamicRangeCompressionRf")
    lfe_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="LfeFilter"
    )
    metadata_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="MetadataControl"
    )
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")


class AccelerationSettingsModel(BaseModel):
    mode: Literal["DISABLED", "ENABLED", "PREFERRED"] = Field(alias="Mode")


class AiffSettingsModel(BaseModel):
    bit_depth: Optional[int] = Field(default=None, alias="BitDepth")
    channels: Optional[int] = Field(default=None, alias="Channels")
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")


class AllowedRenditionSizeModel(BaseModel):
    height: Optional[int] = Field(default=None, alias="Height")
    required: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Required"
    )
    width: Optional[int] = Field(default=None, alias="Width")


class AncillarySourceSettingsModel(BaseModel):
    convert608_to708: Optional[Literal["DISABLED", "UPCONVERT"]] = Field(
        default=None, alias="Convert608To708"
    )
    source_ancillary_channel_number: Optional[int] = Field(
        default=None, alias="SourceAncillaryChannelNumber"
    )
    terminate_captions: Optional[Literal["DISABLED", "END_OF_INPUT"]] = Field(
        default=None, alias="TerminateCaptions"
    )


class AssociateCertificateRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class AudioChannelTaggingSettingsModel(BaseModel):
    channel_tag: Optional[
        Literal[
            "C",
            "CS",
            "L",
            "LC",
            "LFE",
            "LS",
            "LSD",
            "R",
            "RC",
            "RS",
            "RSD",
            "TCS",
            "VHC",
            "VHL",
            "VHR",
        ]
    ] = Field(default=None, alias="ChannelTag")


class Eac3AtmosSettingsModel(BaseModel):
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    bitstream_mode: Optional[Literal["COMPLETE_MAIN"]] = Field(
        default=None, alias="BitstreamMode"
    )
    coding_mode: Optional[
        Literal[
            "CODING_MODE_5_1_4",
            "CODING_MODE_7_1_4",
            "CODING_MODE_9_1_6",
            "CODING_MODE_AUTO",
        ]
    ] = Field(default=None, alias="CodingMode")
    dialogue_intelligence: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DialogueIntelligence"
    )
    downmix_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="DownmixControl"
    )
    dynamic_range_compression_line: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DynamicRangeCompressionLine")
    dynamic_range_compression_rf: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DynamicRangeCompressionRf")
    dynamic_range_control: Optional[
        Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
    ] = Field(default=None, alias="DynamicRangeControl")
    lo_ro_center_mix_level: Optional[float] = Field(
        default=None, alias="LoRoCenterMixLevel"
    )
    lo_ro_surround_mix_level: Optional[float] = Field(
        default=None, alias="LoRoSurroundMixLevel"
    )
    lt_rt_center_mix_level: Optional[float] = Field(
        default=None, alias="LtRtCenterMixLevel"
    )
    lt_rt_surround_mix_level: Optional[float] = Field(
        default=None, alias="LtRtSurroundMixLevel"
    )
    metering_mode: Optional[
        Literal[
            "ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4", "LEQ_A"
        ]
    ] = Field(default=None, alias="MeteringMode")
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")
    speech_threshold: Optional[int] = Field(default=None, alias="SpeechThreshold")
    stereo_downmix: Optional[
        Literal["DPL2", "NOT_INDICATED", "STEREO", "SURROUND"]
    ] = Field(default=None, alias="StereoDownmix")
    surround_ex_mode: Optional[Literal["DISABLED", "ENABLED", "NOT_INDICATED"]] = Field(
        default=None, alias="SurroundExMode"
    )


class Eac3SettingsModel(BaseModel):
    attenuation_control: Optional[Literal["ATTENUATE_3_DB", "NONE"]] = Field(
        default=None, alias="AttenuationControl"
    )
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    bitstream_mode: Optional[
        Literal[
            "COMMENTARY",
            "COMPLETE_MAIN",
            "EMERGENCY",
            "HEARING_IMPAIRED",
            "VISUALLY_IMPAIRED",
        ]
    ] = Field(default=None, alias="BitstreamMode")
    coding_mode: Optional[
        Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
    ] = Field(default=None, alias="CodingMode")
    dc_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DcFilter"
    )
    dialnorm: Optional[int] = Field(default=None, alias="Dialnorm")
    dynamic_range_compression_line: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DynamicRangeCompressionLine")
    dynamic_range_compression_rf: Optional[
        Literal[
            "FILM_LIGHT",
            "FILM_STANDARD",
            "MUSIC_LIGHT",
            "MUSIC_STANDARD",
            "NONE",
            "SPEECH",
        ]
    ] = Field(default=None, alias="DynamicRangeCompressionRf")
    lfe_control: Optional[Literal["LFE", "NO_LFE"]] = Field(
        default=None, alias="LfeControl"
    )
    lfe_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="LfeFilter"
    )
    lo_ro_center_mix_level: Optional[float] = Field(
        default=None, alias="LoRoCenterMixLevel"
    )
    lo_ro_surround_mix_level: Optional[float] = Field(
        default=None, alias="LoRoSurroundMixLevel"
    )
    lt_rt_center_mix_level: Optional[float] = Field(
        default=None, alias="LtRtCenterMixLevel"
    )
    lt_rt_surround_mix_level: Optional[float] = Field(
        default=None, alias="LtRtSurroundMixLevel"
    )
    metadata_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="MetadataControl"
    )
    passthrough_control: Optional[Literal["NO_PASSTHROUGH", "WHEN_POSSIBLE"]] = Field(
        default=None, alias="PassthroughControl"
    )
    phase_control: Optional[Literal["NO_SHIFT", "SHIFT_90_DEGREES"]] = Field(
        default=None, alias="PhaseControl"
    )
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")
    stereo_downmix: Optional[
        Literal["DPL2", "LO_RO", "LT_RT", "NOT_INDICATED"]
    ] = Field(default=None, alias="StereoDownmix")
    surround_ex_mode: Optional[Literal["DISABLED", "ENABLED", "NOT_INDICATED"]] = Field(
        default=None, alias="SurroundExMode"
    )
    surround_mode: Optional[Literal["DISABLED", "ENABLED", "NOT_INDICATED"]] = Field(
        default=None, alias="SurroundMode"
    )


class Mp2SettingsModel(BaseModel):
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    channels: Optional[int] = Field(default=None, alias="Channels")
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")


class Mp3SettingsModel(BaseModel):
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    channels: Optional[int] = Field(default=None, alias="Channels")
    rate_control_mode: Optional[Literal["CBR", "VBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")
    vbr_quality: Optional[int] = Field(default=None, alias="VbrQuality")


class OpusSettingsModel(BaseModel):
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    channels: Optional[int] = Field(default=None, alias="Channels")
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")


class VorbisSettingsModel(BaseModel):
    channels: Optional[int] = Field(default=None, alias="Channels")
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")
    vbr_quality: Optional[int] = Field(default=None, alias="VbrQuality")


class WavSettingsModel(BaseModel):
    bit_depth: Optional[int] = Field(default=None, alias="BitDepth")
    channels: Optional[int] = Field(default=None, alias="Channels")
    format: Optional[Literal["RF64", "RIFF"]] = Field(default=None, alias="Format")
    sample_rate: Optional[int] = Field(default=None, alias="SampleRate")


class AudioNormalizationSettingsModel(BaseModel):
    algorithm: Optional[
        Literal["ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4"]
    ] = Field(default=None, alias="Algorithm")
    algorithm_control: Optional[Literal["CORRECT_AUDIO", "MEASURE_ONLY"]] = Field(
        default=None, alias="AlgorithmControl"
    )
    correction_gate_level: Optional[int] = Field(
        default=None, alias="CorrectionGateLevel"
    )
    loudness_logging: Optional[Literal["DONT_LOG", "LOG"]] = Field(
        default=None, alias="LoudnessLogging"
    )
    peak_calculation: Optional[Literal["NONE", "TRUE_PEAK"]] = Field(
        default=None, alias="PeakCalculation"
    )
    target_lkfs: Optional[float] = Field(default=None, alias="TargetLkfs")
    true_peak_limiter_threshold: Optional[float] = Field(
        default=None, alias="TruePeakLimiterThreshold"
    )


class AudioSelectorGroupModel(BaseModel):
    audio_selector_names: Optional[Sequence[str]] = Field(
        default=None, alias="AudioSelectorNames"
    )


class HlsRenditionGroupSettingsModel(BaseModel):
    rendition_group_id: Optional[str] = Field(default=None, alias="RenditionGroupId")
    rendition_language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="RenditionLanguageCode")
    rendition_name: Optional[str] = Field(default=None, alias="RenditionName")


class ForceIncludeRenditionSizeModel(BaseModel):
    height: Optional[int] = Field(default=None, alias="Height")
    width: Optional[int] = Field(default=None, alias="Width")


class MinBottomRenditionSizeModel(BaseModel):
    height: Optional[int] = Field(default=None, alias="Height")
    width: Optional[int] = Field(default=None, alias="Width")


class MinTopRenditionSizeModel(BaseModel):
    height: Optional[int] = Field(default=None, alias="Height")
    width: Optional[int] = Field(default=None, alias="Width")


class Av1QvbrSettingsModel(BaseModel):
    qvbr_quality_level: Optional[int] = Field(default=None, alias="QvbrQualityLevel")
    qvbr_quality_level_fine_tune: Optional[float] = Field(
        default=None, alias="QvbrQualityLevelFineTune"
    )


class AvailBlankingModel(BaseModel):
    avail_blanking_image: Optional[str] = Field(
        default=None, alias="AvailBlankingImage"
    )


class AvcIntraUhdSettingsModel(BaseModel):
    quality_tuning_level: Optional[Literal["MULTI_PASS", "SINGLE_PASS"]] = Field(
        default=None, alias="QualityTuningLevel"
    )


class BandwidthReductionFilterModel(BaseModel):
    sharpening: Optional[Literal["HIGH", "LOW", "MEDIUM", "OFF"]] = Field(
        default=None, alias="Sharpening"
    )
    strength: Optional[Literal["AUTO", "HIGH", "LOW", "MEDIUM", "OFF"]] = Field(
        default=None, alias="Strength"
    )


class BurninDestinationSettingsModel(BaseModel):
    alignment: Optional[Literal["AUTO", "CENTERED", "LEFT"]] = Field(
        default=None, alias="Alignment"
    )
    apply_font_color: Optional[Literal["ALL_TEXT", "WHITE_TEXT_ONLY"]] = Field(
        default=None, alias="ApplyFontColor"
    )
    background_color: Optional[Literal["AUTO", "BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="BackgroundColor"
    )
    background_opacity: Optional[int] = Field(default=None, alias="BackgroundOpacity")
    fallback_font: Optional[
        Literal[
            "BEST_MATCH",
            "MONOSPACED_SANSSERIF",
            "MONOSPACED_SERIF",
            "PROPORTIONAL_SANSSERIF",
            "PROPORTIONAL_SERIF",
        ]
    ] = Field(default=None, alias="FallbackFont")
    font_color: Optional[
        Literal["AUTO", "BLACK", "BLUE", "GREEN", "HEX", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="FontColor")
    font_opacity: Optional[int] = Field(default=None, alias="FontOpacity")
    font_resolution: Optional[int] = Field(default=None, alias="FontResolution")
    font_script: Optional[Literal["AUTOMATIC", "HANS", "HANT"]] = Field(
        default=None, alias="FontScript"
    )
    font_size: Optional[int] = Field(default=None, alias="FontSize")
    hex_font_color: Optional[str] = Field(default=None, alias="HexFontColor")
    outline_color: Optional[
        Literal["AUTO", "BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="OutlineColor")
    outline_size: Optional[int] = Field(default=None, alias="OutlineSize")
    shadow_color: Optional[Literal["AUTO", "BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="ShadowColor"
    )
    shadow_opacity: Optional[int] = Field(default=None, alias="ShadowOpacity")
    shadow_xoffset: Optional[int] = Field(default=None, alias="ShadowXOffset")
    shadow_yoffset: Optional[int] = Field(default=None, alias="ShadowYOffset")
    style_passthrough: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="StylePassthrough"
    )
    teletext_spacing: Optional[Literal["AUTO", "FIXED_GRID", "PROPORTIONAL"]] = Field(
        default=None, alias="TeletextSpacing"
    )
    xposition: Optional[int] = Field(default=None, alias="XPosition")
    yposition: Optional[int] = Field(default=None, alias="YPosition")


class CancelJobRequestModel(BaseModel):
    id: str = Field(alias="Id")


class DvbSubDestinationSettingsModel(BaseModel):
    alignment: Optional[Literal["AUTO", "CENTERED", "LEFT"]] = Field(
        default=None, alias="Alignment"
    )
    apply_font_color: Optional[Literal["ALL_TEXT", "WHITE_TEXT_ONLY"]] = Field(
        default=None, alias="ApplyFontColor"
    )
    background_color: Optional[Literal["AUTO", "BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="BackgroundColor"
    )
    background_opacity: Optional[int] = Field(default=None, alias="BackgroundOpacity")
    dds_handling: Optional[Literal["NONE", "NO_DISPLAY_WINDOW", "SPECIFIED"]] = Field(
        default=None, alias="DdsHandling"
    )
    dds_xcoordinate: Optional[int] = Field(default=None, alias="DdsXCoordinate")
    dds_ycoordinate: Optional[int] = Field(default=None, alias="DdsYCoordinate")
    fallback_font: Optional[
        Literal[
            "BEST_MATCH",
            "MONOSPACED_SANSSERIF",
            "MONOSPACED_SERIF",
            "PROPORTIONAL_SANSSERIF",
            "PROPORTIONAL_SERIF",
        ]
    ] = Field(default=None, alias="FallbackFont")
    font_color: Optional[
        Literal["AUTO", "BLACK", "BLUE", "GREEN", "HEX", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="FontColor")
    font_opacity: Optional[int] = Field(default=None, alias="FontOpacity")
    font_resolution: Optional[int] = Field(default=None, alias="FontResolution")
    font_script: Optional[Literal["AUTOMATIC", "HANS", "HANT"]] = Field(
        default=None, alias="FontScript"
    )
    font_size: Optional[int] = Field(default=None, alias="FontSize")
    height: Optional[int] = Field(default=None, alias="Height")
    hex_font_color: Optional[str] = Field(default=None, alias="HexFontColor")
    outline_color: Optional[
        Literal["AUTO", "BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
    ] = Field(default=None, alias="OutlineColor")
    outline_size: Optional[int] = Field(default=None, alias="OutlineSize")
    shadow_color: Optional[Literal["AUTO", "BLACK", "NONE", "WHITE"]] = Field(
        default=None, alias="ShadowColor"
    )
    shadow_opacity: Optional[int] = Field(default=None, alias="ShadowOpacity")
    shadow_xoffset: Optional[int] = Field(default=None, alias="ShadowXOffset")
    shadow_yoffset: Optional[int] = Field(default=None, alias="ShadowYOffset")
    style_passthrough: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="StylePassthrough"
    )
    subtitling_type: Optional[Literal["HEARING_IMPAIRED", "STANDARD"]] = Field(
        default=None, alias="SubtitlingType"
    )
    teletext_spacing: Optional[Literal["AUTO", "FIXED_GRID", "PROPORTIONAL"]] = Field(
        default=None, alias="TeletextSpacing"
    )
    width: Optional[int] = Field(default=None, alias="Width")
    xposition: Optional[int] = Field(default=None, alias="XPosition")
    yposition: Optional[int] = Field(default=None, alias="YPosition")


class EmbeddedDestinationSettingsModel(BaseModel):
    destination608_channel_number: Optional[int] = Field(
        default=None, alias="Destination608ChannelNumber"
    )
    destination708_service_number: Optional[int] = Field(
        default=None, alias="Destination708ServiceNumber"
    )


class ImscDestinationSettingsModel(BaseModel):
    accessibility: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Accessibility"
    )
    style_passthrough: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="StylePassthrough"
    )


class SccDestinationSettingsModel(BaseModel):
    framerate: Optional[
        Literal[
            "FRAMERATE_23_97",
            "FRAMERATE_24",
            "FRAMERATE_25",
            "FRAMERATE_29_97_DROPFRAME",
            "FRAMERATE_29_97_NON_DROPFRAME",
        ]
    ] = Field(default=None, alias="Framerate")


class SrtDestinationSettingsModel(BaseModel):
    style_passthrough: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="StylePassthrough"
    )


class TeletextDestinationSettingsModel(BaseModel):
    page_number: Optional[str] = Field(default=None, alias="PageNumber")
    page_types: Optional[
        Sequence[
            Literal[
                "PAGE_TYPE_ADDL_INFO",
                "PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE",
                "PAGE_TYPE_INITIAL",
                "PAGE_TYPE_PROGRAM_SCHEDULE",
                "PAGE_TYPE_SUBTITLE",
            ]
        ]
    ] = Field(default=None, alias="PageTypes")


class TtmlDestinationSettingsModel(BaseModel):
    style_passthrough: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="StylePassthrough"
    )


class WebvttDestinationSettingsModel(BaseModel):
    accessibility: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Accessibility"
    )
    style_passthrough: Optional[Literal["DISABLED", "ENABLED", "STRICT"]] = Field(
        default=None, alias="StylePassthrough"
    )


class CaptionSourceFramerateModel(BaseModel):
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")


class DvbSubSourceSettingsModel(BaseModel):
    pid: Optional[int] = Field(default=None, alias="Pid")


class EmbeddedSourceSettingsModel(BaseModel):
    convert608_to708: Optional[Literal["DISABLED", "UPCONVERT"]] = Field(
        default=None, alias="Convert608To708"
    )
    source608_channel_number: Optional[int] = Field(
        default=None, alias="Source608ChannelNumber"
    )
    source608_track_number: Optional[int] = Field(
        default=None, alias="Source608TrackNumber"
    )
    terminate_captions: Optional[Literal["DISABLED", "END_OF_INPUT"]] = Field(
        default=None, alias="TerminateCaptions"
    )


class TeletextSourceSettingsModel(BaseModel):
    page_number: Optional[str] = Field(default=None, alias="PageNumber")


class TrackSourceSettingsModel(BaseModel):
    track_number: Optional[int] = Field(default=None, alias="TrackNumber")


class WebvttHlsSourceSettingsModel(BaseModel):
    rendition_group_id: Optional[str] = Field(default=None, alias="RenditionGroupId")
    rendition_language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="RenditionLanguageCode")
    rendition_name: Optional[str] = Field(default=None, alias="RenditionName")


class OutputChannelMappingModel(BaseModel):
    input_channels: Optional[Sequence[int]] = Field(default=None, alias="InputChannels")
    input_channels_fine_tune: Optional[Sequence[float]] = Field(
        default=None, alias="InputChannelsFineTune"
    )


class ClipLimitsModel(BaseModel):
    maximum_rgbtolerance: Optional[int] = Field(
        default=None, alias="MaximumRGBTolerance"
    )
    maximum_yuv: Optional[int] = Field(default=None, alias="MaximumYUV")
    minimum_rgbtolerance: Optional[int] = Field(
        default=None, alias="MinimumRGBTolerance"
    )
    minimum_yuv: Optional[int] = Field(default=None, alias="MinimumYUV")


class CmafAdditionalManifestModel(BaseModel):
    manifest_name_modifier: Optional[str] = Field(
        default=None, alias="ManifestNameModifier"
    )
    selected_outputs: Optional[Sequence[str]] = Field(
        default=None, alias="SelectedOutputs"
    )


class SpekeKeyProviderCmafModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    dash_signaled_system_ids: Optional[Sequence[str]] = Field(
        default=None, alias="DashSignaledSystemIds"
    )
    hls_signaled_system_ids: Optional[Sequence[str]] = Field(
        default=None, alias="HlsSignaledSystemIds"
    )
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    url: Optional[str] = Field(default=None, alias="Url")


class StaticKeyProviderModel(BaseModel):
    key_format: Optional[str] = Field(default=None, alias="KeyFormat")
    key_format_versions: Optional[str] = Field(default=None, alias="KeyFormatVersions")
    static_key_value: Optional[str] = Field(default=None, alias="StaticKeyValue")
    url: Optional[str] = Field(default=None, alias="Url")


class CmafImageBasedTrickPlaySettingsModel(BaseModel):
    interval_cadence: Optional[Literal["FOLLOW_CUSTOM", "FOLLOW_IFRAME"]] = Field(
        default=None, alias="IntervalCadence"
    )
    thumbnail_height: Optional[int] = Field(default=None, alias="ThumbnailHeight")
    thumbnail_interval: Optional[float] = Field(default=None, alias="ThumbnailInterval")
    thumbnail_width: Optional[int] = Field(default=None, alias="ThumbnailWidth")
    tile_height: Optional[int] = Field(default=None, alias="TileHeight")
    tile_width: Optional[int] = Field(default=None, alias="TileWidth")


class CmfcSettingsModel(BaseModel):
    audio_duration: Optional[
        Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
    ] = Field(default=None, alias="AudioDuration")
    audio_group_id: Optional[str] = Field(default=None, alias="AudioGroupId")
    audio_rendition_sets: Optional[str] = Field(
        default=None, alias="AudioRenditionSets"
    )
    audio_track_type: Optional[
        Literal[
            "ALTERNATE_AUDIO_AUTO_SELECT",
            "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
            "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
        ]
    ] = Field(default=None, alias="AudioTrackType")
    descriptive_video_service_flag: Optional[Literal["DONT_FLAG", "FLAG"]] = Field(
        default=None, alias="DescriptiveVideoServiceFlag"
    )
    iframe_only_manifest: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="IFrameOnlyManifest"
    )
    klv_metadata: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="KlvMetadata"
    )
    manifest_metadata_signaling: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ManifestMetadataSignaling"
    )
    scte35_esam: Optional[Literal["INSERT", "NONE"]] = Field(
        default=None, alias="Scte35Esam"
    )
    scte35_source: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="Scte35Source"
    )
    timed_metadata: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="TimedMetadata"
    )
    timed_metadata_box_version: Optional[Literal["VERSION_0", "VERSION_1"]] = Field(
        default=None, alias="TimedMetadataBoxVersion"
    )
    timed_metadata_scheme_id_uri: Optional[str] = Field(
        default=None, alias="TimedMetadataSchemeIdUri"
    )
    timed_metadata_value: Optional[str] = Field(
        default=None, alias="TimedMetadataValue"
    )


class Hdr10MetadataModel(BaseModel):
    blue_primary_x: Optional[int] = Field(default=None, alias="BluePrimaryX")
    blue_primary_y: Optional[int] = Field(default=None, alias="BluePrimaryY")
    green_primary_x: Optional[int] = Field(default=None, alias="GreenPrimaryX")
    green_primary_y: Optional[int] = Field(default=None, alias="GreenPrimaryY")
    max_content_light_level: Optional[int] = Field(
        default=None, alias="MaxContentLightLevel"
    )
    max_frame_average_light_level: Optional[int] = Field(
        default=None, alias="MaxFrameAverageLightLevel"
    )
    max_luminance: Optional[int] = Field(default=None, alias="MaxLuminance")
    min_luminance: Optional[int] = Field(default=None, alias="MinLuminance")
    red_primary_x: Optional[int] = Field(default=None, alias="RedPrimaryX")
    red_primary_y: Optional[int] = Field(default=None, alias="RedPrimaryY")
    white_point_x: Optional[int] = Field(default=None, alias="WhitePointX")
    white_point_y: Optional[int] = Field(default=None, alias="WhitePointY")


class F4vSettingsModel(BaseModel):
    moov_placement: Optional[Literal["NORMAL", "PROGRESSIVE_DOWNLOAD"]] = Field(
        default=None, alias="MoovPlacement"
    )


class M3u8SettingsModel(BaseModel):
    audio_duration: Optional[
        Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
    ] = Field(default=None, alias="AudioDuration")
    audio_frames_per_pes: Optional[int] = Field(default=None, alias="AudioFramesPerPes")
    audio_pids: Optional[Sequence[int]] = Field(default=None, alias="AudioPids")
    data_p_ts_control: Optional[Literal["ALIGN_TO_VIDEO", "AUTO"]] = Field(
        default=None, alias="DataPTSControl"
    )
    max_pcr_interval: Optional[int] = Field(default=None, alias="MaxPcrInterval")
    nielsen_id3: Optional[Literal["INSERT", "NONE"]] = Field(
        default=None, alias="NielsenId3"
    )
    pat_interval: Optional[int] = Field(default=None, alias="PatInterval")
    pcr_control: Optional[
        Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
    ] = Field(default=None, alias="PcrControl")
    pcr_pid: Optional[int] = Field(default=None, alias="PcrPid")
    pmt_interval: Optional[int] = Field(default=None, alias="PmtInterval")
    pmt_pid: Optional[int] = Field(default=None, alias="PmtPid")
    private_metadata_pid: Optional[int] = Field(
        default=None, alias="PrivateMetadataPid"
    )
    program_number: Optional[int] = Field(default=None, alias="ProgramNumber")
    scte35_pid: Optional[int] = Field(default=None, alias="Scte35Pid")
    scte35_source: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="Scte35Source"
    )
    timed_metadata: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="TimedMetadata"
    )
    timed_metadata_pid: Optional[int] = Field(default=None, alias="TimedMetadataPid")
    transport_stream_id: Optional[int] = Field(default=None, alias="TransportStreamId")
    video_pid: Optional[int] = Field(default=None, alias="VideoPid")


class MovSettingsModel(BaseModel):
    clap_atom: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="ClapAtom"
    )
    cslg_atom: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="CslgAtom"
    )
    mpeg2_four_cccontrol: Optional[Literal["MPEG", "XDCAM"]] = Field(
        default=None, alias="Mpeg2FourCCControl"
    )
    padding_control: Optional[Literal["NONE", "OMNEON"]] = Field(
        default=None, alias="PaddingControl"
    )
    reference: Optional[Literal["EXTERNAL", "SELF_CONTAINED"]] = Field(
        default=None, alias="Reference"
    )


class Mp4SettingsModel(BaseModel):
    audio_duration: Optional[
        Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
    ] = Field(default=None, alias="AudioDuration")
    cslg_atom: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="CslgAtom"
    )
    ctts_version: Optional[int] = Field(default=None, alias="CttsVersion")
    free_space_box: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="FreeSpaceBox"
    )
    moov_placement: Optional[Literal["NORMAL", "PROGRESSIVE_DOWNLOAD"]] = Field(
        default=None, alias="MoovPlacement"
    )
    mp4_major_brand: Optional[str] = Field(default=None, alias="Mp4MajorBrand")


class MpdSettingsModel(BaseModel):
    accessibility_caption_hints: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="AccessibilityCaptionHints"
    )
    audio_duration: Optional[
        Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
    ] = Field(default=None, alias="AudioDuration")
    caption_container_type: Optional[Literal["FRAGMENTED_MP4", "RAW"]] = Field(
        default=None, alias="CaptionContainerType"
    )
    klv_metadata: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="KlvMetadata"
    )
    manifest_metadata_signaling: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ManifestMetadataSignaling"
    )
    scte35_esam: Optional[Literal["INSERT", "NONE"]] = Field(
        default=None, alias="Scte35Esam"
    )
    scte35_source: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="Scte35Source"
    )
    timed_metadata: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="TimedMetadata"
    )
    timed_metadata_box_version: Optional[Literal["VERSION_0", "VERSION_1"]] = Field(
        default=None, alias="TimedMetadataBoxVersion"
    )
    timed_metadata_scheme_id_uri: Optional[str] = Field(
        default=None, alias="TimedMetadataSchemeIdUri"
    )
    timed_metadata_value: Optional[str] = Field(
        default=None, alias="TimedMetadataValue"
    )


class HopDestinationModel(BaseModel):
    priority: Optional[int] = Field(default=None, alias="Priority")
    queue: Optional[str] = Field(default=None, alias="Queue")
    wait_minutes: Optional[int] = Field(default=None, alias="WaitMinutes")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class ReservationPlanSettingsModel(BaseModel):
    commitment: Literal["ONE_YEAR"] = Field(alias="Commitment")
    renewal_type: Literal["AUTO_RENEW", "EXPIRE"] = Field(alias="RenewalType")
    reserved_slots: int = Field(alias="ReservedSlots")


class DashAdditionalManifestModel(BaseModel):
    manifest_name_modifier: Optional[str] = Field(
        default=None, alias="ManifestNameModifier"
    )
    selected_outputs: Optional[Sequence[str]] = Field(
        default=None, alias="SelectedOutputs"
    )


class SpekeKeyProviderModel(BaseModel):
    certificate_arn: Optional[str] = Field(default=None, alias="CertificateArn")
    resource_id: Optional[str] = Field(default=None, alias="ResourceId")
    system_ids: Optional[Sequence[str]] = Field(default=None, alias="SystemIds")
    url: Optional[str] = Field(default=None, alias="Url")


class DashIsoImageBasedTrickPlaySettingsModel(BaseModel):
    interval_cadence: Optional[Literal["FOLLOW_CUSTOM", "FOLLOW_IFRAME"]] = Field(
        default=None, alias="IntervalCadence"
    )
    thumbnail_height: Optional[int] = Field(default=None, alias="ThumbnailHeight")
    thumbnail_interval: Optional[float] = Field(default=None, alias="ThumbnailInterval")
    thumbnail_width: Optional[int] = Field(default=None, alias="ThumbnailWidth")
    tile_height: Optional[int] = Field(default=None, alias="TileHeight")
    tile_width: Optional[int] = Field(default=None, alias="TileWidth")


class DeinterlacerModel(BaseModel):
    algorithm: Optional[
        Literal["BLEND", "BLEND_TICKER", "INTERPOLATE", "INTERPOLATE_TICKER"]
    ] = Field(default=None, alias="Algorithm")
    control: Optional[Literal["FORCE_ALL_FRAMES", "NORMAL"]] = Field(
        default=None, alias="Control"
    )
    mode: Optional[Literal["ADAPTIVE", "DEINTERLACE", "INVERSE_TELECINE"]] = Field(
        default=None, alias="Mode"
    )


class DeleteJobTemplateRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeletePresetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class DeleteQueueRequestModel(BaseModel):
    name: str = Field(alias="Name")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeEndpointsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    mode: Optional[Literal["DEFAULT", "GET_ONLY"]] = Field(default=None, alias="Mode")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class EndpointModel(BaseModel):
    url: Optional[str] = Field(default=None, alias="Url")


class DisassociateCertificateRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class DolbyVisionLevel6MetadataModel(BaseModel):
    max_cll: Optional[int] = Field(default=None, alias="MaxCll")
    max_fall: Optional[int] = Field(default=None, alias="MaxFall")


class DvbNitSettingsModel(BaseModel):
    network_id: Optional[int] = Field(default=None, alias="NetworkId")
    network_name: Optional[str] = Field(default=None, alias="NetworkName")
    nit_interval: Optional[int] = Field(default=None, alias="NitInterval")


class DvbSdtSettingsModel(BaseModel):
    output_sdt: Optional[
        Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
    ] = Field(default=None, alias="OutputSdt")
    sdt_interval: Optional[int] = Field(default=None, alias="SdtInterval")
    service_name: Optional[str] = Field(default=None, alias="ServiceName")
    service_provider_name: Optional[str] = Field(
        default=None, alias="ServiceProviderName"
    )


class DvbTdtSettingsModel(BaseModel):
    tdt_interval: Optional[int] = Field(default=None, alias="TdtInterval")


class EsamManifestConfirmConditionNotificationModel(BaseModel):
    mcc_xml: Optional[str] = Field(default=None, alias="MccXml")


class EsamSignalProcessingNotificationModel(BaseModel):
    scc_xml: Optional[str] = Field(default=None, alias="SccXml")


class ExtendedDataServicesModel(BaseModel):
    copy_protection_action: Optional[Literal["PASSTHROUGH", "STRIP"]] = Field(
        default=None, alias="CopyProtectionAction"
    )
    vchip_action: Optional[Literal["PASSTHROUGH", "STRIP"]] = Field(
        default=None, alias="VchipAction"
    )


class FrameCaptureSettingsModel(BaseModel):
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    max_captures: Optional[int] = Field(default=None, alias="MaxCaptures")
    quality: Optional[int] = Field(default=None, alias="Quality")


class GetJobRequestModel(BaseModel):
    id: str = Field(alias="Id")


class GetJobTemplateRequestModel(BaseModel):
    name: str = Field(alias="Name")


class PolicyModel(BaseModel):
    http_inputs: Optional[Literal["ALLOWED", "DISALLOWED"]] = Field(
        default=None, alias="HttpInputs"
    )
    https_inputs: Optional[Literal["ALLOWED", "DISALLOWED"]] = Field(
        default=None, alias="HttpsInputs"
    )
    s3_inputs: Optional[Literal["ALLOWED", "DISALLOWED"]] = Field(
        default=None, alias="S3Inputs"
    )


class GetPresetRequestModel(BaseModel):
    name: str = Field(alias="Name")


class GetQueueRequestModel(BaseModel):
    name: str = Field(alias="Name")


class H264QvbrSettingsModel(BaseModel):
    max_average_bitrate: Optional[int] = Field(default=None, alias="MaxAverageBitrate")
    qvbr_quality_level: Optional[int] = Field(default=None, alias="QvbrQualityLevel")
    qvbr_quality_level_fine_tune: Optional[float] = Field(
        default=None, alias="QvbrQualityLevelFineTune"
    )


class H265QvbrSettingsModel(BaseModel):
    max_average_bitrate: Optional[int] = Field(default=None, alias="MaxAverageBitrate")
    qvbr_quality_level: Optional[int] = Field(default=None, alias="QvbrQualityLevel")
    qvbr_quality_level_fine_tune: Optional[float] = Field(
        default=None, alias="QvbrQualityLevelFineTune"
    )


class Hdr10PlusModel(BaseModel):
    mastering_monitor_nits: Optional[int] = Field(
        default=None, alias="MasteringMonitorNits"
    )
    target_monitor_nits: Optional[int] = Field(default=None, alias="TargetMonitorNits")


class HlsAdditionalManifestModel(BaseModel):
    manifest_name_modifier: Optional[str] = Field(
        default=None, alias="ManifestNameModifier"
    )
    selected_outputs: Optional[Sequence[str]] = Field(
        default=None, alias="SelectedOutputs"
    )


class HlsCaptionLanguageMappingModel(BaseModel):
    caption_channel: Optional[int] = Field(default=None, alias="CaptionChannel")
    custom_language_code: Optional[str] = Field(
        default=None, alias="CustomLanguageCode"
    )
    language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="LanguageCode")
    language_description: Optional[str] = Field(
        default=None, alias="LanguageDescription"
    )


class HlsImageBasedTrickPlaySettingsModel(BaseModel):
    interval_cadence: Optional[Literal["FOLLOW_CUSTOM", "FOLLOW_IFRAME"]] = Field(
        default=None, alias="IntervalCadence"
    )
    thumbnail_height: Optional[int] = Field(default=None, alias="ThumbnailHeight")
    thumbnail_interval: Optional[float] = Field(default=None, alias="ThumbnailInterval")
    thumbnail_width: Optional[int] = Field(default=None, alias="ThumbnailWidth")
    tile_height: Optional[int] = Field(default=None, alias="TileHeight")
    tile_width: Optional[int] = Field(default=None, alias="TileWidth")


class HlsSettingsModel(BaseModel):
    audio_group_id: Optional[str] = Field(default=None, alias="AudioGroupId")
    audio_only_container: Optional[Literal["AUTOMATIC", "M2TS"]] = Field(
        default=None, alias="AudioOnlyContainer"
    )
    audio_rendition_sets: Optional[str] = Field(
        default=None, alias="AudioRenditionSets"
    )
    audio_track_type: Optional[
        Literal[
            "ALTERNATE_AUDIO_AUTO_SELECT",
            "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
            "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
            "AUDIO_ONLY_VARIANT_STREAM",
        ]
    ] = Field(default=None, alias="AudioTrackType")
    descriptive_video_service_flag: Optional[Literal["DONT_FLAG", "FLAG"]] = Field(
        default=None, alias="DescriptiveVideoServiceFlag"
    )
    iframe_only_manifest: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="IFrameOnlyManifest"
    )
    segment_modifier: Optional[str] = Field(default=None, alias="SegmentModifier")


class Id3InsertionModel(BaseModel):
    id3: Optional[str] = Field(default=None, alias="Id3")
    timecode: Optional[str] = Field(default=None, alias="Timecode")


class InsertableImageModel(BaseModel):
    duration: Optional[int] = Field(default=None, alias="Duration")
    fade_in: Optional[int] = Field(default=None, alias="FadeIn")
    fade_out: Optional[int] = Field(default=None, alias="FadeOut")
    height: Optional[int] = Field(default=None, alias="Height")
    image_inserter_input: Optional[str] = Field(
        default=None, alias="ImageInserterInput"
    )
    image_x: Optional[int] = Field(default=None, alias="ImageX")
    image_y: Optional[int] = Field(default=None, alias="ImageY")
    layer: Optional[int] = Field(default=None, alias="Layer")
    opacity: Optional[int] = Field(default=None, alias="Opacity")
    start_time: Optional[str] = Field(default=None, alias="StartTime")
    width: Optional[int] = Field(default=None, alias="Width")


class InputClippingModel(BaseModel):
    end_timecode: Optional[str] = Field(default=None, alias="EndTimecode")
    start_timecode: Optional[str] = Field(default=None, alias="StartTimecode")


class InputDecryptionSettingsModel(BaseModel):
    decryption_mode: Optional[Literal["AES_CBC", "AES_CTR", "AES_GCM"]] = Field(
        default=None, alias="DecryptionMode"
    )
    encrypted_decryption_key: Optional[str] = Field(
        default=None, alias="EncryptedDecryptionKey"
    )
    initialization_vector: Optional[str] = Field(
        default=None, alias="InitializationVector"
    )
    kms_key_region: Optional[str] = Field(default=None, alias="KmsKeyRegion")


class RectangleModel(BaseModel):
    height: Optional[int] = Field(default=None, alias="Height")
    width: Optional[int] = Field(default=None, alias="Width")
    x: Optional[int] = Field(default=None, alias="X")
    y: Optional[int] = Field(default=None, alias="Y")


class InputVideoGeneratorModel(BaseModel):
    duration: Optional[int] = Field(default=None, alias="Duration")


class JobMessagesModel(BaseModel):
    info: Optional[List[str]] = Field(default=None, alias="Info")
    warning: Optional[List[str]] = Field(default=None, alias="Warning")


class KantarWatermarkSettingsModel(BaseModel):
    channel_name: Optional[str] = Field(default=None, alias="ChannelName")
    content_reference: Optional[str] = Field(default=None, alias="ContentReference")
    credentials_secret_name: Optional[str] = Field(
        default=None, alias="CredentialsSecretName"
    )
    file_offset: Optional[float] = Field(default=None, alias="FileOffset")
    kantar_license_id: Optional[int] = Field(default=None, alias="KantarLicenseId")
    kantar_server_url: Optional[str] = Field(default=None, alias="KantarServerUrl")
    log_destination: Optional[str] = Field(default=None, alias="LogDestination")
    metadata3: Optional[str] = Field(default=None, alias="Metadata3")
    metadata4: Optional[str] = Field(default=None, alias="Metadata4")
    metadata5: Optional[str] = Field(default=None, alias="Metadata5")
    metadata6: Optional[str] = Field(default=None, alias="Metadata6")
    metadata7: Optional[str] = Field(default=None, alias="Metadata7")
    metadata8: Optional[str] = Field(default=None, alias="Metadata8")


class NielsenConfigurationModel(BaseModel):
    breakout_code: Optional[int] = Field(default=None, alias="BreakoutCode")
    distributor_id: Optional[str] = Field(default=None, alias="DistributorId")


class NielsenNonLinearWatermarkSettingsModel(BaseModel):
    active_watermark_process: Optional[
        Literal["CBET", "NAES2_AND_NW", "NAES2_AND_NW_AND_CBET"]
    ] = Field(default=None, alias="ActiveWatermarkProcess")
    adi_filename: Optional[str] = Field(default=None, alias="AdiFilename")
    asset_id: Optional[str] = Field(default=None, alias="AssetId")
    asset_name: Optional[str] = Field(default=None, alias="AssetName")
    cbet_source_id: Optional[str] = Field(default=None, alias="CbetSourceId")
    episode_id: Optional[str] = Field(default=None, alias="EpisodeId")
    metadata_destination: Optional[str] = Field(
        default=None, alias="MetadataDestination"
    )
    source_id: Optional[int] = Field(default=None, alias="SourceId")
    source_watermark_status: Optional[Literal["CLEAN", "WATERMARKED"]] = Field(
        default=None, alias="SourceWatermarkStatus"
    )
    tic_server_url: Optional[str] = Field(default=None, alias="TicServerUrl")
    unique_tic_per_audio_track: Optional[
        Literal["RESERVE_UNIQUE_TICS_PER_TRACK", "SAME_TICS_PER_TRACK"]
    ] = Field(default=None, alias="UniqueTicPerAudioTrack")


class TimecodeConfigModel(BaseModel):
    anchor: Optional[str] = Field(default=None, alias="Anchor")
    source: Optional[Literal["EMBEDDED", "SPECIFIEDSTART", "ZEROBASED"]] = Field(
        default=None, alias="Source"
    )
    start: Optional[str] = Field(default=None, alias="Start")
    timestamp_offset: Optional[str] = Field(default=None, alias="TimestampOffset")


class QueueTransitionModel(BaseModel):
    destination_queue: Optional[str] = Field(default=None, alias="DestinationQueue")
    source_queue: Optional[str] = Field(default=None, alias="SourceQueue")
    timestamp: Optional[datetime] = Field(default=None, alias="Timestamp")


class TimingModel(BaseModel):
    finish_time: Optional[datetime] = Field(default=None, alias="FinishTime")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    submit_time: Optional[datetime] = Field(default=None, alias="SubmitTime")


class ListJobTemplatesRequestModel(BaseModel):
    category: Optional[str] = Field(default=None, alias="Category")
    list_by: Optional[Literal["CREATION_DATE", "NAME", "SYSTEM"]] = Field(
        default=None, alias="ListBy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )


class ListJobsRequestModel(BaseModel):
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    queue: Optional[str] = Field(default=None, alias="Queue")
    status: Optional[
        Literal["CANCELED", "COMPLETE", "ERROR", "PROGRESSING", "SUBMITTED"]
    ] = Field(default=None, alias="Status")


class ListPresetsRequestModel(BaseModel):
    category: Optional[str] = Field(default=None, alias="Category")
    list_by: Optional[Literal["CREATION_DATE", "NAME", "SYSTEM"]] = Field(
        default=None, alias="ListBy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )


class ListQueuesRequestModel(BaseModel):
    list_by: Optional[Literal["CREATION_DATE", "NAME"]] = Field(
        default=None, alias="ListBy"
    )
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )


class ListTagsForResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")


class ResourceTagsModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="Tags")


class M2tsScte35EsamModel(BaseModel):
    scte35_esam_pid: Optional[int] = Field(default=None, alias="Scte35EsamPid")


class MotionImageInsertionFramerateModel(BaseModel):
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")


class MotionImageInsertionOffsetModel(BaseModel):
    image_x: Optional[int] = Field(default=None, alias="ImageX")
    image_y: Optional[int] = Field(default=None, alias="ImageY")


class Mpeg2SettingsModel(BaseModel):
    adaptive_quantization: Optional[Literal["HIGH", "LOW", "MEDIUM", "OFF"]] = Field(
        default=None, alias="AdaptiveQuantization"
    )
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    codec_level: Optional[Literal["AUTO", "HIGH", "HIGH1440", "LOW", "MAIN"]] = Field(
        default=None, alias="CodecLevel"
    )
    codec_profile: Optional[Literal["MAIN", "PROFILE_422"]] = Field(
        default=None, alias="CodecProfile"
    )
    dynamic_sub_gop: Optional[Literal["ADAPTIVE", "STATIC"]] = Field(
        default=None, alias="DynamicSubGop"
    )
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    gop_size_units: Optional[Literal["FRAMES", "SECONDS"]] = Field(
        default=None, alias="GopSizeUnits"
    )
    hrd_buffer_final_fill_percentage: Optional[int] = Field(
        default=None, alias="HrdBufferFinalFillPercentage"
    )
    hrd_buffer_initial_fill_percentage: Optional[int] = Field(
        default=None, alias="HrdBufferInitialFillPercentage"
    )
    hrd_buffer_size: Optional[int] = Field(default=None, alias="HrdBufferSize")
    interlace_mode: Optional[
        Literal[
            "BOTTOM_FIELD",
            "FOLLOW_BOTTOM_FIELD",
            "FOLLOW_TOP_FIELD",
            "PROGRESSIVE",
            "TOP_FIELD",
        ]
    ] = Field(default=None, alias="InterlaceMode")
    intra_dc_precision: Optional[
        Literal[
            "AUTO",
            "INTRA_DC_PRECISION_10",
            "INTRA_DC_PRECISION_11",
            "INTRA_DC_PRECISION_8",
            "INTRA_DC_PRECISION_9",
        ]
    ] = Field(default=None, alias="IntraDcPrecision")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    min_iinterval: Optional[int] = Field(default=None, alias="MinIInterval")
    number_bframes_between_reference_frames: Optional[int] = Field(
        default=None, alias="NumberBFramesBetweenReferenceFrames"
    )
    par_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="ParControl"
    )
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    quality_tuning_level: Optional[Literal["MULTI_PASS", "SINGLE_PASS"]] = Field(
        default=None, alias="QualityTuningLevel"
    )
    rate_control_mode: Optional[Literal["CBR", "VBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    scan_type_conversion_mode: Optional[
        Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
    ] = Field(default=None, alias="ScanTypeConversionMode")
    scene_change_detect: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SceneChangeDetect"
    )
    slow_pal: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SlowPal"
    )
    softness: Optional[int] = Field(default=None, alias="Softness")
    spatial_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SpatialAdaptiveQuantization"
    )
    syntax: Optional[Literal["DEFAULT", "D_10"]] = Field(default=None, alias="Syntax")
    telecine: Optional[Literal["HARD", "NONE", "SOFT"]] = Field(
        default=None, alias="Telecine"
    )
    temporal_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="TemporalAdaptiveQuantization"
    )


class MsSmoothAdditionalManifestModel(BaseModel):
    manifest_name_modifier: Optional[str] = Field(
        default=None, alias="ManifestNameModifier"
    )
    selected_outputs: Optional[Sequence[str]] = Field(
        default=None, alias="SelectedOutputs"
    )


class MxfXavcProfileSettingsModel(BaseModel):
    duration_mode: Optional[
        Literal["ALLOW_ANY_DURATION", "DROP_FRAMES_FOR_COMPLIANCE"]
    ] = Field(default=None, alias="DurationMode")
    max_anc_data_size: Optional[int] = Field(default=None, alias="MaxAncDataSize")


class NexGuardFileMarkerSettingsModel(BaseModel):
    license: Optional[str] = Field(default=None, alias="License")
    payload: Optional[int] = Field(default=None, alias="Payload")
    preset: Optional[str] = Field(default=None, alias="Preset")
    strength: Optional[
        Literal["DEFAULT", "LIGHTER", "LIGHTEST", "STRONGER", "STRONGEST"]
    ] = Field(default=None, alias="Strength")


class NoiseReducerFilterSettingsModel(BaseModel):
    strength: Optional[int] = Field(default=None, alias="Strength")


class NoiseReducerSpatialFilterSettingsModel(BaseModel):
    post_filter_sharpen_strength: Optional[int] = Field(
        default=None, alias="PostFilterSharpenStrength"
    )
    speed: Optional[int] = Field(default=None, alias="Speed")
    strength: Optional[int] = Field(default=None, alias="Strength")


class NoiseReducerTemporalFilterSettingsModel(BaseModel):
    aggressive_mode: Optional[int] = Field(default=None, alias="AggressiveMode")
    post_temporal_sharpening: Optional[Literal["AUTO", "DISABLED", "ENABLED"]] = Field(
        default=None, alias="PostTemporalSharpening"
    )
    post_temporal_sharpening_strength: Optional[
        Literal["HIGH", "LOW", "MEDIUM"]
    ] = Field(default=None, alias="PostTemporalSharpeningStrength")
    speed: Optional[int] = Field(default=None, alias="Speed")
    strength: Optional[int] = Field(default=None, alias="Strength")


class VideoDetailModel(BaseModel):
    height_in_px: Optional[int] = Field(default=None, alias="HeightInPx")
    width_in_px: Optional[int] = Field(default=None, alias="WidthInPx")


class ProresSettingsModel(BaseModel):
    chroma_sampling: Optional[
        Literal["PRESERVE_444_SAMPLING", "SUBSAMPLE_TO_422"]
    ] = Field(default=None, alias="ChromaSampling")
    codec_profile: Optional[
        Literal[
            "APPLE_PRORES_422",
            "APPLE_PRORES_422_HQ",
            "APPLE_PRORES_422_LT",
            "APPLE_PRORES_422_PROXY",
            "APPLE_PRORES_4444",
            "APPLE_PRORES_4444_XQ",
        ]
    ] = Field(default=None, alias="CodecProfile")
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    interlace_mode: Optional[
        Literal[
            "BOTTOM_FIELD",
            "FOLLOW_BOTTOM_FIELD",
            "FOLLOW_TOP_FIELD",
            "PROGRESSIVE",
            "TOP_FIELD",
        ]
    ] = Field(default=None, alias="InterlaceMode")
    par_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="ParControl"
    )
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    scan_type_conversion_mode: Optional[
        Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
    ] = Field(default=None, alias="ScanTypeConversionMode")
    slow_pal: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SlowPal"
    )
    telecine: Optional[Literal["HARD", "NONE"]] = Field(default=None, alias="Telecine")


class ReservationPlanModel(BaseModel):
    commitment: Optional[Literal["ONE_YEAR"]] = Field(default=None, alias="Commitment")
    expires_at: Optional[datetime] = Field(default=None, alias="ExpiresAt")
    purchased_at: Optional[datetime] = Field(default=None, alias="PurchasedAt")
    renewal_type: Optional[Literal["AUTO_RENEW", "EXPIRE"]] = Field(
        default=None, alias="RenewalType"
    )
    reserved_slots: Optional[int] = Field(default=None, alias="ReservedSlots")
    status: Optional[Literal["ACTIVE", "EXPIRED"]] = Field(default=None, alias="Status")


class S3DestinationAccessControlModel(BaseModel):
    canned_acl: Optional[
        Literal[
            "AUTHENTICATED_READ",
            "BUCKET_OWNER_FULL_CONTROL",
            "BUCKET_OWNER_READ",
            "PUBLIC_READ",
        ]
    ] = Field(default=None, alias="CannedAcl")


class S3EncryptionSettingsModel(BaseModel):
    encryption_type: Optional[
        Literal["SERVER_SIDE_ENCRYPTION_KMS", "SERVER_SIDE_ENCRYPTION_S3"]
    ] = Field(default=None, alias="EncryptionType")
    kms_encryption_context: Optional[str] = Field(
        default=None, alias="KmsEncryptionContext"
    )
    kms_key_arn: Optional[str] = Field(default=None, alias="KmsKeyArn")


class TagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tags: Mapping[str, str] = Field(alias="Tags")


class TimecodeBurninModel(BaseModel):
    font_size: Optional[int] = Field(default=None, alias="FontSize")
    position: Optional[
        Literal[
            "BOTTOM_CENTER",
            "BOTTOM_LEFT",
            "BOTTOM_RIGHT",
            "MIDDLE_CENTER",
            "MIDDLE_LEFT",
            "MIDDLE_RIGHT",
            "TOP_CENTER",
            "TOP_LEFT",
            "TOP_RIGHT",
        ]
    ] = Field(default=None, alias="Position")
    prefix: Optional[str] = Field(default=None, alias="Prefix")


class UntagResourceRequestModel(BaseModel):
    arn: str = Field(alias="Arn")
    tag_keys: Optional[Sequence[str]] = Field(default=None, alias="TagKeys")


class Vc3SettingsModel(BaseModel):
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    interlace_mode: Optional[Literal["INTERLACED", "PROGRESSIVE"]] = Field(
        default=None, alias="InterlaceMode"
    )
    scan_type_conversion_mode: Optional[
        Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
    ] = Field(default=None, alias="ScanTypeConversionMode")
    slow_pal: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SlowPal"
    )
    telecine: Optional[Literal["HARD", "NONE"]] = Field(default=None, alias="Telecine")
    vc3_class: Optional[
        Literal["CLASS_145_8BIT", "CLASS_220_10BIT", "CLASS_220_8BIT"]
    ] = Field(default=None, alias="Vc3Class")


class Vp8SettingsModel(BaseModel):
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    hrd_buffer_size: Optional[int] = Field(default=None, alias="HrdBufferSize")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    par_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="ParControl"
    )
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    quality_tuning_level: Optional[Literal["MULTI_PASS", "MULTI_PASS_HQ"]] = Field(
        default=None, alias="QualityTuningLevel"
    )
    rate_control_mode: Optional[Literal["VBR"]] = Field(
        default=None, alias="RateControlMode"
    )


class Vp9SettingsModel(BaseModel):
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    hrd_buffer_size: Optional[int] = Field(default=None, alias="HrdBufferSize")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    par_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="ParControl"
    )
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    quality_tuning_level: Optional[Literal["MULTI_PASS", "MULTI_PASS_HQ"]] = Field(
        default=None, alias="QualityTuningLevel"
    )
    rate_control_mode: Optional[Literal["VBR"]] = Field(
        default=None, alias="RateControlMode"
    )


class Xavc4kIntraCbgProfileSettingsModel(BaseModel):
    xavc_class: Optional[Literal["CLASS_100", "CLASS_300", "CLASS_480"]] = Field(
        default=None, alias="XavcClass"
    )


class Xavc4kIntraVbrProfileSettingsModel(BaseModel):
    xavc_class: Optional[Literal["CLASS_100", "CLASS_300", "CLASS_480"]] = Field(
        default=None, alias="XavcClass"
    )


class Xavc4kProfileSettingsModel(BaseModel):
    bitrate_class: Optional[
        Literal["BITRATE_CLASS_100", "BITRATE_CLASS_140", "BITRATE_CLASS_200"]
    ] = Field(default=None, alias="BitrateClass")
    codec_profile: Optional[Literal["HIGH", "HIGH_422"]] = Field(
        default=None, alias="CodecProfile"
    )
    flicker_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FlickerAdaptiveQuantization"
    )
    gop_breference: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="GopBReference"
    )
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    hrd_buffer_size: Optional[int] = Field(default=None, alias="HrdBufferSize")
    quality_tuning_level: Optional[
        Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
    ] = Field(default=None, alias="QualityTuningLevel")
    slices: Optional[int] = Field(default=None, alias="Slices")


class XavcHdIntraCbgProfileSettingsModel(BaseModel):
    xavc_class: Optional[Literal["CLASS_100", "CLASS_200", "CLASS_50"]] = Field(
        default=None, alias="XavcClass"
    )


class XavcHdProfileSettingsModel(BaseModel):
    bitrate_class: Optional[
        Literal["BITRATE_CLASS_25", "BITRATE_CLASS_35", "BITRATE_CLASS_50"]
    ] = Field(default=None, alias="BitrateClass")
    flicker_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FlickerAdaptiveQuantization"
    )
    gop_breference: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="GopBReference"
    )
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    hrd_buffer_size: Optional[int] = Field(default=None, alias="HrdBufferSize")
    interlace_mode: Optional[
        Literal[
            "BOTTOM_FIELD",
            "FOLLOW_BOTTOM_FIELD",
            "FOLLOW_TOP_FIELD",
            "PROGRESSIVE",
            "TOP_FIELD",
        ]
    ] = Field(default=None, alias="InterlaceMode")
    quality_tuning_level: Optional[
        Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
    ] = Field(default=None, alias="QualityTuningLevel")
    slices: Optional[int] = Field(default=None, alias="Slices")
    telecine: Optional[Literal["HARD", "NONE"]] = Field(default=None, alias="Telecine")


class AudioCodecSettingsModel(BaseModel):
    aac_settings: Optional[AacSettingsModel] = Field(default=None, alias="AacSettings")
    ac3_settings: Optional[Ac3SettingsModel] = Field(default=None, alias="Ac3Settings")
    aiff_settings: Optional[AiffSettingsModel] = Field(
        default=None, alias="AiffSettings"
    )
    codec: Optional[
        Literal[
            "AAC",
            "AC3",
            "AIFF",
            "EAC3",
            "EAC3_ATMOS",
            "MP2",
            "MP3",
            "OPUS",
            "PASSTHROUGH",
            "VORBIS",
            "WAV",
        ]
    ] = Field(default=None, alias="Codec")
    eac3_atmos_settings: Optional[Eac3AtmosSettingsModel] = Field(
        default=None, alias="Eac3AtmosSettings"
    )
    eac3_settings: Optional[Eac3SettingsModel] = Field(
        default=None, alias="Eac3Settings"
    )
    mp2_settings: Optional[Mp2SettingsModel] = Field(default=None, alias="Mp2Settings")
    mp3_settings: Optional[Mp3SettingsModel] = Field(default=None, alias="Mp3Settings")
    opus_settings: Optional[OpusSettingsModel] = Field(
        default=None, alias="OpusSettings"
    )
    vorbis_settings: Optional[VorbisSettingsModel] = Field(
        default=None, alias="VorbisSettings"
    )
    wav_settings: Optional[WavSettingsModel] = Field(default=None, alias="WavSettings")


class AutomatedAbrRuleModel(BaseModel):
    allowed_renditions: Optional[Sequence[AllowedRenditionSizeModel]] = Field(
        default=None, alias="AllowedRenditions"
    )
    force_include_renditions: Optional[
        Sequence[ForceIncludeRenditionSizeModel]
    ] = Field(default=None, alias="ForceIncludeRenditions")
    min_bottom_rendition_size: Optional[MinBottomRenditionSizeModel] = Field(
        default=None, alias="MinBottomRenditionSize"
    )
    min_top_rendition_size: Optional[MinTopRenditionSizeModel] = Field(
        default=None, alias="MinTopRenditionSize"
    )
    type: Optional[
        Literal[
            "ALLOWED_RENDITIONS",
            "FORCE_INCLUDE_RENDITIONS",
            "MIN_BOTTOM_RENDITION_SIZE",
            "MIN_TOP_RENDITION_SIZE",
        ]
    ] = Field(default=None, alias="Type")


class Av1SettingsModel(BaseModel):
    adaptive_quantization: Optional[
        Literal["HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
    ] = Field(default=None, alias="AdaptiveQuantization")
    bit_depth: Optional[Literal["BIT_10", "BIT_8"]] = Field(
        default=None, alias="BitDepth"
    )
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    number_bframes_between_reference_frames: Optional[int] = Field(
        default=None, alias="NumberBFramesBetweenReferenceFrames"
    )
    qvbr_settings: Optional[Av1QvbrSettingsModel] = Field(
        default=None, alias="QvbrSettings"
    )
    rate_control_mode: Optional[Literal["QVBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    slices: Optional[int] = Field(default=None, alias="Slices")
    spatial_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SpatialAdaptiveQuantization"
    )


class AvcIntraSettingsModel(BaseModel):
    avc_intra_class: Optional[
        Literal["CLASS_100", "CLASS_200", "CLASS_4K_2K", "CLASS_50"]
    ] = Field(default=None, alias="AvcIntraClass")
    avc_intra_uhd_settings: Optional[AvcIntraUhdSettingsModel] = Field(
        default=None, alias="AvcIntraUhdSettings"
    )
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    interlace_mode: Optional[
        Literal[
            "BOTTOM_FIELD",
            "FOLLOW_BOTTOM_FIELD",
            "FOLLOW_TOP_FIELD",
            "PROGRESSIVE",
            "TOP_FIELD",
        ]
    ] = Field(default=None, alias="InterlaceMode")
    scan_type_conversion_mode: Optional[
        Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
    ] = Field(default=None, alias="ScanTypeConversionMode")
    slow_pal: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SlowPal"
    )
    telecine: Optional[Literal["HARD", "NONE"]] = Field(default=None, alias="Telecine")


class CaptionDestinationSettingsModel(BaseModel):
    burnin_destination_settings: Optional[BurninDestinationSettingsModel] = Field(
        default=None, alias="BurninDestinationSettings"
    )
    destination_type: Optional[
        Literal[
            "BURN_IN",
            "DVB_SUB",
            "EMBEDDED",
            "EMBEDDED_PLUS_SCTE20",
            "IMSC",
            "SCC",
            "SCTE20_PLUS_EMBEDDED",
            "SMI",
            "SRT",
            "TELETEXT",
            "TTML",
            "WEBVTT",
        ]
    ] = Field(default=None, alias="DestinationType")
    dvb_sub_destination_settings: Optional[DvbSubDestinationSettingsModel] = Field(
        default=None, alias="DvbSubDestinationSettings"
    )
    embedded_destination_settings: Optional[EmbeddedDestinationSettingsModel] = Field(
        default=None, alias="EmbeddedDestinationSettings"
    )
    imsc_destination_settings: Optional[ImscDestinationSettingsModel] = Field(
        default=None, alias="ImscDestinationSettings"
    )
    scc_destination_settings: Optional[SccDestinationSettingsModel] = Field(
        default=None, alias="SccDestinationSettings"
    )
    srt_destination_settings: Optional[SrtDestinationSettingsModel] = Field(
        default=None, alias="SrtDestinationSettings"
    )
    teletext_destination_settings: Optional[TeletextDestinationSettingsModel] = Field(
        default=None, alias="TeletextDestinationSettings"
    )
    ttml_destination_settings: Optional[TtmlDestinationSettingsModel] = Field(
        default=None, alias="TtmlDestinationSettings"
    )
    webvtt_destination_settings: Optional[WebvttDestinationSettingsModel] = Field(
        default=None, alias="WebvttDestinationSettings"
    )


class FileSourceSettingsModel(BaseModel):
    convert608_to708: Optional[Literal["DISABLED", "UPCONVERT"]] = Field(
        default=None, alias="Convert608To708"
    )
    framerate: Optional[CaptionSourceFramerateModel] = Field(
        default=None, alias="Framerate"
    )
    source_file: Optional[str] = Field(default=None, alias="SourceFile")
    time_delta: Optional[int] = Field(default=None, alias="TimeDelta")
    time_delta_units: Optional[Literal["MILLISECONDS", "SECONDS"]] = Field(
        default=None, alias="TimeDeltaUnits"
    )


class ChannelMappingModel(BaseModel):
    output_channels: Optional[Sequence[OutputChannelMappingModel]] = Field(
        default=None, alias="OutputChannels"
    )


class CmafEncryptionSettingsModel(BaseModel):
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )
    encryption_method: Optional[Literal["AES_CTR", "SAMPLE_AES"]] = Field(
        default=None, alias="EncryptionMethod"
    )
    initialization_vector_in_manifest: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="InitializationVectorInManifest"
    )
    speke_key_provider: Optional[SpekeKeyProviderCmafModel] = Field(
        default=None, alias="SpekeKeyProvider"
    )
    static_key_provider: Optional[StaticKeyProviderModel] = Field(
        default=None, alias="StaticKeyProvider"
    )
    type: Optional[Literal["SPEKE", "STATIC_KEY"]] = Field(default=None, alias="Type")


class ColorCorrectorModel(BaseModel):
    brightness: Optional[int] = Field(default=None, alias="Brightness")
    clip_limits: Optional[ClipLimitsModel] = Field(default=None, alias="ClipLimits")
    color_space_conversion: Optional[
        Literal[
            "FORCE_601",
            "FORCE_709",
            "FORCE_HDR10",
            "FORCE_HLG_2020",
            "FORCE_P3D65_SDR",
            "FORCE_P3DCI",
            "NONE",
        ]
    ] = Field(default=None, alias="ColorSpaceConversion")
    contrast: Optional[int] = Field(default=None, alias="Contrast")
    hdr10_metadata: Optional[Hdr10MetadataModel] = Field(
        default=None, alias="Hdr10Metadata"
    )
    hdr_to_sdr_tone_mapper: Optional[Literal["PRESERVE_DETAILS", "VIBRANT"]] = Field(
        default=None, alias="HdrToSdrToneMapper"
    )
    hue: Optional[int] = Field(default=None, alias="Hue")
    sample_range_conversion: Optional[
        Literal["LIMITED_RANGE_CLIP", "LIMITED_RANGE_SQUEEZE", "NONE"]
    ] = Field(default=None, alias="SampleRangeConversion")
    saturation: Optional[int] = Field(default=None, alias="Saturation")
    sdr_reference_white_level: Optional[int] = Field(
        default=None, alias="SdrReferenceWhiteLevel"
    )


class VideoSelectorModel(BaseModel):
    alpha_behavior: Optional[Literal["DISCARD", "REMAP_TO_LUMA"]] = Field(
        default=None, alias="AlphaBehavior"
    )
    color_space: Optional[
        Literal[
            "FOLLOW", "HDR10", "HLG_2020", "P3D65_SDR", "P3DCI", "REC_601", "REC_709"
        ]
    ] = Field(default=None, alias="ColorSpace")
    color_space_usage: Optional[Literal["FALLBACK", "FORCE"]] = Field(
        default=None, alias="ColorSpaceUsage"
    )
    embedded_timecode_override: Optional[Literal["NONE", "USE_MDPM"]] = Field(
        default=None, alias="EmbeddedTimecodeOverride"
    )
    hdr10_metadata: Optional[Hdr10MetadataModel] = Field(
        default=None, alias="Hdr10Metadata"
    )
    pad_video: Optional[Literal["BLACK", "DISABLED"]] = Field(
        default=None, alias="PadVideo"
    )
    pid: Optional[int] = Field(default=None, alias="Pid")
    program_number: Optional[int] = Field(default=None, alias="ProgramNumber")
    rotate: Optional[
        Literal["AUTO", "DEGREES_180", "DEGREES_270", "DEGREES_90", "DEGREE_0"]
    ] = Field(default=None, alias="Rotate")
    sample_range: Optional[Literal["FOLLOW", "FULL_RANGE", "LIMITED_RANGE"]] = Field(
        default=None, alias="SampleRange"
    )


class CreateQueueRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    pricing_plan: Optional[Literal["ON_DEMAND", "RESERVED"]] = Field(
        default=None, alias="PricingPlan"
    )
    reservation_plan_settings: Optional[ReservationPlanSettingsModel] = Field(
        default=None, alias="ReservationPlanSettings"
    )
    status: Optional[Literal["ACTIVE", "PAUSED"]] = Field(default=None, alias="Status")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class UpdateQueueRequestModel(BaseModel):
    name: str = Field(alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    reservation_plan_settings: Optional[ReservationPlanSettingsModel] = Field(
        default=None, alias="ReservationPlanSettings"
    )
    status: Optional[Literal["ACTIVE", "PAUSED"]] = Field(default=None, alias="Status")


class DashIsoEncryptionSettingsModel(BaseModel):
    playback_device_compatibility: Optional[
        Literal["CENC_V1", "UNENCRYPTED_SEI"]
    ] = Field(default=None, alias="PlaybackDeviceCompatibility")
    speke_key_provider: Optional[SpekeKeyProviderModel] = Field(
        default=None, alias="SpekeKeyProvider"
    )


class HlsEncryptionSettingsModel(BaseModel):
    constant_initialization_vector: Optional[str] = Field(
        default=None, alias="ConstantInitializationVector"
    )
    encryption_method: Optional[Literal["AES128", "SAMPLE_AES"]] = Field(
        default=None, alias="EncryptionMethod"
    )
    initialization_vector_in_manifest: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="InitializationVectorInManifest"
    )
    offline_encrypted: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="OfflineEncrypted"
    )
    speke_key_provider: Optional[SpekeKeyProviderModel] = Field(
        default=None, alias="SpekeKeyProvider"
    )
    static_key_provider: Optional[StaticKeyProviderModel] = Field(
        default=None, alias="StaticKeyProvider"
    )
    type: Optional[Literal["SPEKE", "STATIC_KEY"]] = Field(default=None, alias="Type")


class MsSmoothEncryptionSettingsModel(BaseModel):
    speke_key_provider: Optional[SpekeKeyProviderModel] = Field(
        default=None, alias="SpekeKeyProvider"
    )


class DescribeEndpointsRequestDescribeEndpointsPaginateModel(BaseModel):
    mode: Optional[Literal["DEFAULT", "GET_ONLY"]] = Field(default=None, alias="Mode")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobTemplatesRequestListJobTemplatesPaginateModel(BaseModel):
    category: Optional[str] = Field(default=None, alias="Category")
    list_by: Optional[Literal["CREATION_DATE", "NAME", "SYSTEM"]] = Field(
        default=None, alias="ListBy"
    )
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListJobsRequestListJobsPaginateModel(BaseModel):
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    queue: Optional[str] = Field(default=None, alias="Queue")
    status: Optional[
        Literal["CANCELED", "COMPLETE", "ERROR", "PROGRESSING", "SUBMITTED"]
    ] = Field(default=None, alias="Status")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListPresetsRequestListPresetsPaginateModel(BaseModel):
    category: Optional[str] = Field(default=None, alias="Category")
    list_by: Optional[Literal["CREATION_DATE", "NAME", "SYSTEM"]] = Field(
        default=None, alias="ListBy"
    )
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListQueuesRequestListQueuesPaginateModel(BaseModel):
    list_by: Optional[Literal["CREATION_DATE", "NAME"]] = Field(
        default=None, alias="ListBy"
    )
    order: Optional[Literal["ASCENDING", "DESCENDING"]] = Field(
        default=None, alias="Order"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeEndpointsResponseModel(BaseModel):
    endpoints: List[EndpointModel] = Field(alias="Endpoints")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DolbyVisionModel(BaseModel):
    l6_metadata: Optional[DolbyVisionLevel6MetadataModel] = Field(
        default=None, alias="L6Metadata"
    )
    l6_mode: Optional[Literal["PASSTHROUGH", "RECALCULATE", "SPECIFY"]] = Field(
        default=None, alias="L6Mode"
    )
    mapping: Optional[Literal["HDR10_1000", "HDR10_NOMAP"]] = Field(
        default=None, alias="Mapping"
    )
    profile: Optional[Literal["PROFILE_5", "PROFILE_8_1"]] = Field(
        default=None, alias="Profile"
    )


class EsamSettingsModel(BaseModel):
    manifest_confirm_condition_notification: Optional[
        EsamManifestConfirmConditionNotificationModel
    ] = Field(default=None, alias="ManifestConfirmConditionNotification")
    response_signal_preroll: Optional[int] = Field(
        default=None, alias="ResponseSignalPreroll"
    )
    signal_processing_notification: Optional[
        EsamSignalProcessingNotificationModel
    ] = Field(default=None, alias="SignalProcessingNotification")


class GetPolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutPolicyRequestModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")


class PutPolicyResponseModel(BaseModel):
    policy: PolicyModel = Field(alias="Policy")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class H264SettingsModel(BaseModel):
    adaptive_quantization: Optional[
        Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
    ] = Field(default=None, alias="AdaptiveQuantization")
    bandwidth_reduction_filter: Optional[BandwidthReductionFilterModel] = Field(
        default=None, alias="BandwidthReductionFilter"
    )
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    codec_level: Optional[
        Literal[
            "AUTO",
            "LEVEL_1",
            "LEVEL_1_1",
            "LEVEL_1_2",
            "LEVEL_1_3",
            "LEVEL_2",
            "LEVEL_2_1",
            "LEVEL_2_2",
            "LEVEL_3",
            "LEVEL_3_1",
            "LEVEL_3_2",
            "LEVEL_4",
            "LEVEL_4_1",
            "LEVEL_4_2",
            "LEVEL_5",
            "LEVEL_5_1",
            "LEVEL_5_2",
        ]
    ] = Field(default=None, alias="CodecLevel")
    codec_profile: Optional[
        Literal["BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"]
    ] = Field(default=None, alias="CodecProfile")
    dynamic_sub_gop: Optional[Literal["ADAPTIVE", "STATIC"]] = Field(
        default=None, alias="DynamicSubGop"
    )
    entropy_encoding: Optional[Literal["CABAC", "CAVLC"]] = Field(
        default=None, alias="EntropyEncoding"
    )
    field_encoding: Optional[Literal["FORCE_FIELD", "MBAFF", "PAFF"]] = Field(
        default=None, alias="FieldEncoding"
    )
    flicker_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FlickerAdaptiveQuantization"
    )
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    gop_breference: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="GopBReference"
    )
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    gop_size_units: Optional[Literal["AUTO", "FRAMES", "SECONDS"]] = Field(
        default=None, alias="GopSizeUnits"
    )
    hrd_buffer_final_fill_percentage: Optional[int] = Field(
        default=None, alias="HrdBufferFinalFillPercentage"
    )
    hrd_buffer_initial_fill_percentage: Optional[int] = Field(
        default=None, alias="HrdBufferInitialFillPercentage"
    )
    hrd_buffer_size: Optional[int] = Field(default=None, alias="HrdBufferSize")
    interlace_mode: Optional[
        Literal[
            "BOTTOM_FIELD",
            "FOLLOW_BOTTOM_FIELD",
            "FOLLOW_TOP_FIELD",
            "PROGRESSIVE",
            "TOP_FIELD",
        ]
    ] = Field(default=None, alias="InterlaceMode")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    min_iinterval: Optional[int] = Field(default=None, alias="MinIInterval")
    number_bframes_between_reference_frames: Optional[int] = Field(
        default=None, alias="NumberBFramesBetweenReferenceFrames"
    )
    number_reference_frames: Optional[int] = Field(
        default=None, alias="NumberReferenceFrames"
    )
    par_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="ParControl"
    )
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    quality_tuning_level: Optional[
        Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
    ] = Field(default=None, alias="QualityTuningLevel")
    qvbr_settings: Optional[H264QvbrSettingsModel] = Field(
        default=None, alias="QvbrSettings"
    )
    rate_control_mode: Optional[Literal["CBR", "QVBR", "VBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    repeat_pps: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="RepeatPps"
    )
    scan_type_conversion_mode: Optional[
        Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
    ] = Field(default=None, alias="ScanTypeConversionMode")
    scene_change_detect: Optional[
        Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"]
    ] = Field(default=None, alias="SceneChangeDetect")
    slices: Optional[int] = Field(default=None, alias="Slices")
    slow_pal: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SlowPal"
    )
    softness: Optional[int] = Field(default=None, alias="Softness")
    spatial_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SpatialAdaptiveQuantization"
    )
    syntax: Optional[Literal["DEFAULT", "RP2027"]] = Field(default=None, alias="Syntax")
    telecine: Optional[Literal["HARD", "NONE", "SOFT"]] = Field(
        default=None, alias="Telecine"
    )
    temporal_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="TemporalAdaptiveQuantization"
    )
    unregistered_sei_timecode: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="UnregisteredSeiTimecode"
    )


class H265SettingsModel(BaseModel):
    adaptive_quantization: Optional[
        Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
    ] = Field(default=None, alias="AdaptiveQuantization")
    alternate_transfer_function_sei: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AlternateTransferFunctionSei"
    )
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    codec_level: Optional[
        Literal[
            "AUTO",
            "LEVEL_1",
            "LEVEL_2",
            "LEVEL_2_1",
            "LEVEL_3",
            "LEVEL_3_1",
            "LEVEL_4",
            "LEVEL_4_1",
            "LEVEL_5",
            "LEVEL_5_1",
            "LEVEL_5_2",
            "LEVEL_6",
            "LEVEL_6_1",
            "LEVEL_6_2",
        ]
    ] = Field(default=None, alias="CodecLevel")
    codec_profile: Optional[
        Literal[
            "MAIN10_HIGH",
            "MAIN10_MAIN",
            "MAIN_422_10BIT_HIGH",
            "MAIN_422_10BIT_MAIN",
            "MAIN_422_8BIT_HIGH",
            "MAIN_422_8BIT_MAIN",
            "MAIN_HIGH",
            "MAIN_MAIN",
        ]
    ] = Field(default=None, alias="CodecProfile")
    dynamic_sub_gop: Optional[Literal["ADAPTIVE", "STATIC"]] = Field(
        default=None, alias="DynamicSubGop"
    )
    flicker_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="FlickerAdaptiveQuantization"
    )
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    gop_breference: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="GopBReference"
    )
    gop_closed_cadence: Optional[int] = Field(default=None, alias="GopClosedCadence")
    gop_size: Optional[float] = Field(default=None, alias="GopSize")
    gop_size_units: Optional[Literal["AUTO", "FRAMES", "SECONDS"]] = Field(
        default=None, alias="GopSizeUnits"
    )
    hrd_buffer_final_fill_percentage: Optional[int] = Field(
        default=None, alias="HrdBufferFinalFillPercentage"
    )
    hrd_buffer_initial_fill_percentage: Optional[int] = Field(
        default=None, alias="HrdBufferInitialFillPercentage"
    )
    hrd_buffer_size: Optional[int] = Field(default=None, alias="HrdBufferSize")
    interlace_mode: Optional[
        Literal[
            "BOTTOM_FIELD",
            "FOLLOW_BOTTOM_FIELD",
            "FOLLOW_TOP_FIELD",
            "PROGRESSIVE",
            "TOP_FIELD",
        ]
    ] = Field(default=None, alias="InterlaceMode")
    max_bitrate: Optional[int] = Field(default=None, alias="MaxBitrate")
    min_iinterval: Optional[int] = Field(default=None, alias="MinIInterval")
    number_bframes_between_reference_frames: Optional[int] = Field(
        default=None, alias="NumberBFramesBetweenReferenceFrames"
    )
    number_reference_frames: Optional[int] = Field(
        default=None, alias="NumberReferenceFrames"
    )
    par_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="ParControl"
    )
    par_denominator: Optional[int] = Field(default=None, alias="ParDenominator")
    par_numerator: Optional[int] = Field(default=None, alias="ParNumerator")
    quality_tuning_level: Optional[
        Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
    ] = Field(default=None, alias="QualityTuningLevel")
    qvbr_settings: Optional[H265QvbrSettingsModel] = Field(
        default=None, alias="QvbrSettings"
    )
    rate_control_mode: Optional[Literal["CBR", "QVBR", "VBR"]] = Field(
        default=None, alias="RateControlMode"
    )
    sample_adaptive_offset_filter_mode: Optional[
        Literal["ADAPTIVE", "DEFAULT", "OFF"]
    ] = Field(default=None, alias="SampleAdaptiveOffsetFilterMode")
    scan_type_conversion_mode: Optional[
        Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
    ] = Field(default=None, alias="ScanTypeConversionMode")
    scene_change_detect: Optional[
        Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"]
    ] = Field(default=None, alias="SceneChangeDetect")
    slices: Optional[int] = Field(default=None, alias="Slices")
    slow_pal: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SlowPal"
    )
    spatial_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SpatialAdaptiveQuantization"
    )
    telecine: Optional[Literal["HARD", "NONE", "SOFT"]] = Field(
        default=None, alias="Telecine"
    )
    temporal_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="TemporalAdaptiveQuantization"
    )
    temporal_ids: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="TemporalIds"
    )
    tiles: Optional[Literal["DISABLED", "ENABLED"]] = Field(default=None, alias="Tiles")
    unregistered_sei_timecode: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="UnregisteredSeiTimecode"
    )
    write_mp4_packaging_type: Optional[Literal["HEV1", "HVC1"]] = Field(
        default=None, alias="WriteMp4PackagingType"
    )


class OutputSettingsModel(BaseModel):
    hls_settings: Optional[HlsSettingsModel] = Field(default=None, alias="HlsSettings")


class TimedMetadataInsertionModel(BaseModel):
    id3_insertions: Optional[Sequence[Id3InsertionModel]] = Field(
        default=None, alias="Id3Insertions"
    )


class ImageInserterModel(BaseModel):
    insertable_images: Optional[Sequence[InsertableImageModel]] = Field(
        default=None, alias="InsertableImages"
    )
    sdr_reference_white_level: Optional[int] = Field(
        default=None, alias="SdrReferenceWhiteLevel"
    )


class ListTagsForResourceResponseModel(BaseModel):
    resource_tags: ResourceTagsModel = Field(alias="ResourceTags")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class M2tsSettingsModel(BaseModel):
    audio_buffer_model: Optional[Literal["ATSC", "DVB"]] = Field(
        default=None, alias="AudioBufferModel"
    )
    audio_duration: Optional[
        Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
    ] = Field(default=None, alias="AudioDuration")
    audio_frames_per_pes: Optional[int] = Field(default=None, alias="AudioFramesPerPes")
    audio_pids: Optional[Sequence[int]] = Field(default=None, alias="AudioPids")
    bitrate: Optional[int] = Field(default=None, alias="Bitrate")
    buffer_model: Optional[Literal["MULTIPLEX", "NONE"]] = Field(
        default=None, alias="BufferModel"
    )
    data_p_ts_control: Optional[Literal["ALIGN_TO_VIDEO", "AUTO"]] = Field(
        default=None, alias="DataPTSControl"
    )
    dvb_nit_settings: Optional[DvbNitSettingsModel] = Field(
        default=None, alias="DvbNitSettings"
    )
    dvb_sdt_settings: Optional[DvbSdtSettingsModel] = Field(
        default=None, alias="DvbSdtSettings"
    )
    dvb_sub_pids: Optional[Sequence[int]] = Field(default=None, alias="DvbSubPids")
    dvb_tdt_settings: Optional[DvbTdtSettingsModel] = Field(
        default=None, alias="DvbTdtSettings"
    )
    dvb_teletext_pid: Optional[int] = Field(default=None, alias="DvbTeletextPid")
    ebp_audio_interval: Optional[
        Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
    ] = Field(default=None, alias="EbpAudioInterval")
    ebp_placement: Optional[Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]] = Field(
        default=None, alias="EbpPlacement"
    )
    es_rate_in_pes: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="EsRateInPes"
    )
    force_ts_video_ebp_order: Optional[Literal["DEFAULT", "FORCE"]] = Field(
        default=None, alias="ForceTsVideoEbpOrder"
    )
    fragment_time: Optional[float] = Field(default=None, alias="FragmentTime")
    klv_metadata: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="KlvMetadata"
    )
    max_pcr_interval: Optional[int] = Field(default=None, alias="MaxPcrInterval")
    min_ebp_interval: Optional[int] = Field(default=None, alias="MinEbpInterval")
    nielsen_id3: Optional[Literal["INSERT", "NONE"]] = Field(
        default=None, alias="NielsenId3"
    )
    null_packet_bitrate: Optional[float] = Field(
        default=None, alias="NullPacketBitrate"
    )
    pat_interval: Optional[int] = Field(default=None, alias="PatInterval")
    pcr_control: Optional[
        Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
    ] = Field(default=None, alias="PcrControl")
    pcr_pid: Optional[int] = Field(default=None, alias="PcrPid")
    pmt_interval: Optional[int] = Field(default=None, alias="PmtInterval")
    pmt_pid: Optional[int] = Field(default=None, alias="PmtPid")
    private_metadata_pid: Optional[int] = Field(
        default=None, alias="PrivateMetadataPid"
    )
    program_number: Optional[int] = Field(default=None, alias="ProgramNumber")
    rate_mode: Optional[Literal["CBR", "VBR"]] = Field(default=None, alias="RateMode")
    scte35_esam: Optional[M2tsScte35EsamModel] = Field(default=None, alias="Scte35Esam")
    scte35_pid: Optional[int] = Field(default=None, alias="Scte35Pid")
    scte35_source: Optional[Literal["NONE", "PASSTHROUGH"]] = Field(
        default=None, alias="Scte35Source"
    )
    segmentation_markers: Optional[
        Literal[
            "EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"
        ]
    ] = Field(default=None, alias="SegmentationMarkers")
    segmentation_style: Optional[Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]] = Field(
        default=None, alias="SegmentationStyle"
    )
    segmentation_time: Optional[float] = Field(default=None, alias="SegmentationTime")
    timed_metadata_pid: Optional[int] = Field(default=None, alias="TimedMetadataPid")
    transport_stream_id: Optional[int] = Field(default=None, alias="TransportStreamId")
    video_pid: Optional[int] = Field(default=None, alias="VideoPid")


class MotionImageInserterModel(BaseModel):
    framerate: Optional[MotionImageInsertionFramerateModel] = Field(
        default=None, alias="Framerate"
    )
    input: Optional[str] = Field(default=None, alias="Input")
    insertion_mode: Optional[Literal["MOV", "PNG"]] = Field(
        default=None, alias="InsertionMode"
    )
    offset: Optional[MotionImageInsertionOffsetModel] = Field(
        default=None, alias="Offset"
    )
    playback: Optional[Literal["ONCE", "REPEAT"]] = Field(
        default=None, alias="Playback"
    )
    start_time: Optional[str] = Field(default=None, alias="StartTime")


class MxfSettingsModel(BaseModel):
    afd_signaling: Optional[Literal["COPY_FROM_VIDEO", "NO_COPY"]] = Field(
        default=None, alias="AfdSignaling"
    )
    profile: Optional[Literal["D_10", "OP1A", "XAVC", "XDCAM"]] = Field(
        default=None, alias="Profile"
    )
    xavc_profile_settings: Optional[MxfXavcProfileSettingsModel] = Field(
        default=None, alias="XavcProfileSettings"
    )


class PartnerWatermarkingModel(BaseModel):
    nexguard_file_marker_settings: Optional[NexGuardFileMarkerSettingsModel] = Field(
        default=None, alias="NexguardFileMarkerSettings"
    )


class NoiseReducerModel(BaseModel):
    filter: Optional[
        Literal[
            "BILATERAL",
            "CONSERVE",
            "GAUSSIAN",
            "LANCZOS",
            "MEAN",
            "SHARPEN",
            "SPATIAL",
            "TEMPORAL",
        ]
    ] = Field(default=None, alias="Filter")
    filter_settings: Optional[NoiseReducerFilterSettingsModel] = Field(
        default=None, alias="FilterSettings"
    )
    spatial_filter_settings: Optional[NoiseReducerSpatialFilterSettingsModel] = Field(
        default=None, alias="SpatialFilterSettings"
    )
    temporal_filter_settings: Optional[NoiseReducerTemporalFilterSettingsModel] = Field(
        default=None, alias="TemporalFilterSettings"
    )


class OutputDetailModel(BaseModel):
    duration_in_ms: Optional[int] = Field(default=None, alias="DurationInMs")
    video_details: Optional[VideoDetailModel] = Field(
        default=None, alias="VideoDetails"
    )


class QueueModel(BaseModel):
    name: str = Field(alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    description: Optional[str] = Field(default=None, alias="Description")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    pricing_plan: Optional[Literal["ON_DEMAND", "RESERVED"]] = Field(
        default=None, alias="PricingPlan"
    )
    progressing_jobs_count: Optional[int] = Field(
        default=None, alias="ProgressingJobsCount"
    )
    reservation_plan: Optional[ReservationPlanModel] = Field(
        default=None, alias="ReservationPlan"
    )
    status: Optional[Literal["ACTIVE", "PAUSED"]] = Field(default=None, alias="Status")
    submitted_jobs_count: Optional[int] = Field(
        default=None, alias="SubmittedJobsCount"
    )
    type: Optional[Literal["CUSTOM", "SYSTEM"]] = Field(default=None, alias="Type")


class S3DestinationSettingsModel(BaseModel):
    access_control: Optional[S3DestinationAccessControlModel] = Field(
        default=None, alias="AccessControl"
    )
    encryption: Optional[S3EncryptionSettingsModel] = Field(
        default=None, alias="Encryption"
    )


class XavcSettingsModel(BaseModel):
    adaptive_quantization: Optional[
        Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
    ] = Field(default=None, alias="AdaptiveQuantization")
    entropy_encoding: Optional[Literal["AUTO", "CABAC", "CAVLC"]] = Field(
        default=None, alias="EntropyEncoding"
    )
    framerate_control: Optional[Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]] = Field(
        default=None, alias="FramerateControl"
    )
    framerate_conversion_algorithm: Optional[
        Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
    ] = Field(default=None, alias="FramerateConversionAlgorithm")
    framerate_denominator: Optional[int] = Field(
        default=None, alias="FramerateDenominator"
    )
    framerate_numerator: Optional[int] = Field(default=None, alias="FramerateNumerator")
    profile: Optional[
        Literal[
            "XAVC_4K",
            "XAVC_4K_INTRA_CBG",
            "XAVC_4K_INTRA_VBR",
            "XAVC_HD",
            "XAVC_HD_INTRA_CBG",
        ]
    ] = Field(default=None, alias="Profile")
    slow_pal: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SlowPal"
    )
    softness: Optional[int] = Field(default=None, alias="Softness")
    spatial_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SpatialAdaptiveQuantization"
    )
    temporal_adaptive_quantization: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="TemporalAdaptiveQuantization"
    )
    xavc4k_intra_cbg_profile_settings: Optional[
        Xavc4kIntraCbgProfileSettingsModel
    ] = Field(default=None, alias="Xavc4kIntraCbgProfileSettings")
    xavc4k_intra_vbr_profile_settings: Optional[
        Xavc4kIntraVbrProfileSettingsModel
    ] = Field(default=None, alias="Xavc4kIntraVbrProfileSettings")
    xavc4k_profile_settings: Optional[Xavc4kProfileSettingsModel] = Field(
        default=None, alias="Xavc4kProfileSettings"
    )
    xavc_hd_intra_cbg_profile_settings: Optional[
        XavcHdIntraCbgProfileSettingsModel
    ] = Field(default=None, alias="XavcHdIntraCbgProfileSettings")
    xavc_hd_profile_settings: Optional[XavcHdProfileSettingsModel] = Field(
        default=None, alias="XavcHdProfileSettings"
    )


class AutomatedAbrSettingsModel(BaseModel):
    max_abr_bitrate: Optional[int] = Field(default=None, alias="MaxAbrBitrate")
    max_renditions: Optional[int] = Field(default=None, alias="MaxRenditions")
    min_abr_bitrate: Optional[int] = Field(default=None, alias="MinAbrBitrate")
    rules: Optional[Sequence[AutomatedAbrRuleModel]] = Field(
        default=None, alias="Rules"
    )


class CaptionDescriptionPresetModel(BaseModel):
    custom_language_code: Optional[str] = Field(
        default=None, alias="CustomLanguageCode"
    )
    destination_settings: Optional[CaptionDestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )
    language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="LanguageCode")
    language_description: Optional[str] = Field(
        default=None, alias="LanguageDescription"
    )


class CaptionDescriptionModel(BaseModel):
    caption_selector_name: Optional[str] = Field(
        default=None, alias="CaptionSelectorName"
    )
    custom_language_code: Optional[str] = Field(
        default=None, alias="CustomLanguageCode"
    )
    destination_settings: Optional[CaptionDestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )
    language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="LanguageCode")
    language_description: Optional[str] = Field(
        default=None, alias="LanguageDescription"
    )


class CaptionSourceSettingsModel(BaseModel):
    ancillary_source_settings: Optional[AncillarySourceSettingsModel] = Field(
        default=None, alias="AncillarySourceSettings"
    )
    dvb_sub_source_settings: Optional[DvbSubSourceSettingsModel] = Field(
        default=None, alias="DvbSubSourceSettings"
    )
    embedded_source_settings: Optional[EmbeddedSourceSettingsModel] = Field(
        default=None, alias="EmbeddedSourceSettings"
    )
    file_source_settings: Optional[FileSourceSettingsModel] = Field(
        default=None, alias="FileSourceSettings"
    )
    source_type: Optional[
        Literal[
            "ANCILLARY",
            "DVB_SUB",
            "EMBEDDED",
            "IMSC",
            "NULL_SOURCE",
            "SCC",
            "SCTE20",
            "SMI",
            "SMPTE_TT",
            "SRT",
            "STL",
            "TELETEXT",
            "TTML",
            "WEBVTT",
        ]
    ] = Field(default=None, alias="SourceType")
    teletext_source_settings: Optional[TeletextSourceSettingsModel] = Field(
        default=None, alias="TeletextSourceSettings"
    )
    track_source_settings: Optional[TrackSourceSettingsModel] = Field(
        default=None, alias="TrackSourceSettings"
    )
    webvtt_hls_source_settings: Optional[WebvttHlsSourceSettingsModel] = Field(
        default=None, alias="WebvttHlsSourceSettings"
    )


class RemixSettingsModel(BaseModel):
    channel_mapping: Optional[ChannelMappingModel] = Field(
        default=None, alias="ChannelMapping"
    )
    channels_in: Optional[int] = Field(default=None, alias="ChannelsIn")
    channels_out: Optional[int] = Field(default=None, alias="ChannelsOut")


class ContainerSettingsModel(BaseModel):
    cmfc_settings: Optional[CmfcSettingsModel] = Field(
        default=None, alias="CmfcSettings"
    )
    container: Optional[
        Literal[
            "CMFC",
            "F4V",
            "ISMV",
            "M2TS",
            "M3U8",
            "MOV",
            "MP4",
            "MPD",
            "MXF",
            "RAW",
            "WEBM",
        ]
    ] = Field(default=None, alias="Container")
    f4v_settings: Optional[F4vSettingsModel] = Field(default=None, alias="F4vSettings")
    m2ts_settings: Optional[M2tsSettingsModel] = Field(
        default=None, alias="M2tsSettings"
    )
    m3u8_settings: Optional[M3u8SettingsModel] = Field(
        default=None, alias="M3u8Settings"
    )
    mov_settings: Optional[MovSettingsModel] = Field(default=None, alias="MovSettings")
    mp4_settings: Optional[Mp4SettingsModel] = Field(default=None, alias="Mp4Settings")
    mpd_settings: Optional[MpdSettingsModel] = Field(default=None, alias="MpdSettings")
    mxf_settings: Optional[MxfSettingsModel] = Field(default=None, alias="MxfSettings")


class VideoPreprocessorModel(BaseModel):
    color_corrector: Optional[ColorCorrectorModel] = Field(
        default=None, alias="ColorCorrector"
    )
    deinterlacer: Optional[DeinterlacerModel] = Field(
        default=None, alias="Deinterlacer"
    )
    dolby_vision: Optional[DolbyVisionModel] = Field(default=None, alias="DolbyVision")
    hdr10_plus: Optional[Hdr10PlusModel] = Field(default=None, alias="Hdr10Plus")
    image_inserter: Optional[ImageInserterModel] = Field(
        default=None, alias="ImageInserter"
    )
    noise_reducer: Optional[NoiseReducerModel] = Field(
        default=None, alias="NoiseReducer"
    )
    partner_watermarking: Optional[PartnerWatermarkingModel] = Field(
        default=None, alias="PartnerWatermarking"
    )
    timecode_burnin: Optional[TimecodeBurninModel] = Field(
        default=None, alias="TimecodeBurnin"
    )


class OutputGroupDetailModel(BaseModel):
    output_details: Optional[List[OutputDetailModel]] = Field(
        default=None, alias="OutputDetails"
    )


class CreateQueueResponseModel(BaseModel):
    queue: QueueModel = Field(alias="Queue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetQueueResponseModel(BaseModel):
    queue: QueueModel = Field(alias="Queue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListQueuesResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    queues: List[QueueModel] = Field(alias="Queues")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateQueueResponseModel(BaseModel):
    queue: QueueModel = Field(alias="Queue")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DestinationSettingsModel(BaseModel):
    s3_settings: Optional[S3DestinationSettingsModel] = Field(
        default=None, alias="S3Settings"
    )


class VideoCodecSettingsModel(BaseModel):
    av1_settings: Optional[Av1SettingsModel] = Field(default=None, alias="Av1Settings")
    avc_intra_settings: Optional[AvcIntraSettingsModel] = Field(
        default=None, alias="AvcIntraSettings"
    )
    codec: Optional[
        Literal[
            "AV1",
            "AVC_INTRA",
            "FRAME_CAPTURE",
            "H_264",
            "H_265",
            "MPEG2",
            "PRORES",
            "VC3",
            "VP8",
            "VP9",
            "XAVC",
        ]
    ] = Field(default=None, alias="Codec")
    frame_capture_settings: Optional[FrameCaptureSettingsModel] = Field(
        default=None, alias="FrameCaptureSettings"
    )
    h264_settings: Optional[H264SettingsModel] = Field(
        default=None, alias="H264Settings"
    )
    h265_settings: Optional[H265SettingsModel] = Field(
        default=None, alias="H265Settings"
    )
    mpeg2_settings: Optional[Mpeg2SettingsModel] = Field(
        default=None, alias="Mpeg2Settings"
    )
    prores_settings: Optional[ProresSettingsModel] = Field(
        default=None, alias="ProresSettings"
    )
    vc3_settings: Optional[Vc3SettingsModel] = Field(default=None, alias="Vc3Settings")
    vp8_settings: Optional[Vp8SettingsModel] = Field(default=None, alias="Vp8Settings")
    vp9_settings: Optional[Vp9SettingsModel] = Field(default=None, alias="Vp9Settings")
    xavc_settings: Optional[XavcSettingsModel] = Field(
        default=None, alias="XavcSettings"
    )


class AutomatedEncodingSettingsModel(BaseModel):
    abr_settings: Optional[AutomatedAbrSettingsModel] = Field(
        default=None, alias="AbrSettings"
    )


class CaptionSelectorModel(BaseModel):
    custom_language_code: Optional[str] = Field(
        default=None, alias="CustomLanguageCode"
    )
    language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="LanguageCode")
    source_settings: Optional[CaptionSourceSettingsModel] = Field(
        default=None, alias="SourceSettings"
    )


class AudioDescriptionModel(BaseModel):
    audio_channel_tagging_settings: Optional[AudioChannelTaggingSettingsModel] = Field(
        default=None, alias="AudioChannelTaggingSettings"
    )
    audio_normalization_settings: Optional[AudioNormalizationSettingsModel] = Field(
        default=None, alias="AudioNormalizationSettings"
    )
    audio_source_name: Optional[str] = Field(default=None, alias="AudioSourceName")
    audio_type: Optional[int] = Field(default=None, alias="AudioType")
    audio_type_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="AudioTypeControl"
    )
    codec_settings: Optional[AudioCodecSettingsModel] = Field(
        default=None, alias="CodecSettings"
    )
    custom_language_code: Optional[str] = Field(
        default=None, alias="CustomLanguageCode"
    )
    language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="LanguageCode")
    language_code_control: Optional[Literal["FOLLOW_INPUT", "USE_CONFIGURED"]] = Field(
        default=None, alias="LanguageCodeControl"
    )
    remix_settings: Optional[RemixSettingsModel] = Field(
        default=None, alias="RemixSettings"
    )
    stream_name: Optional[str] = Field(default=None, alias="StreamName")


class AudioSelectorModel(BaseModel):
    audio_duration_correction: Optional[
        Literal["AUTO", "DISABLED", "FRAME", "TRACK"]
    ] = Field(default=None, alias="AudioDurationCorrection")
    custom_language_code: Optional[str] = Field(
        default=None, alias="CustomLanguageCode"
    )
    default_selection: Optional[Literal["DEFAULT", "NOT_DEFAULT"]] = Field(
        default=None, alias="DefaultSelection"
    )
    external_audio_file_input: Optional[str] = Field(
        default=None, alias="ExternalAudioFileInput"
    )
    hls_rendition_group_settings: Optional[HlsRenditionGroupSettingsModel] = Field(
        default=None, alias="HlsRenditionGroupSettings"
    )
    language_code: Optional[
        Literal[
            "AAR",
            "ABK",
            "AFR",
            "AKA",
            "AMH",
            "ARA",
            "ARG",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAK",
            "BAM",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOD",
            "BOS",
            "BRE",
            "BUL",
            "CAT",
            "CES",
            "CHA",
            "CHE",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "CYM",
            "DAN",
            "DEU",
            "DIV",
            "DZO",
            "ELL",
            "ENG",
            "ENM",
            "EPO",
            "EST",
            "EUS",
            "EWE",
            "FAO",
            "FAS",
            "FIJ",
            "FIN",
            "FRA",
            "FRM",
            "FRY",
            "FUL",
            "GER",
            "GLA",
            "GLE",
            "GLG",
            "GLV",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HIN",
            "HMO",
            "HRV",
            "HUN",
            "HYE",
            "IBO",
            "IDO",
            "III",
            "IKU",
            "ILE",
            "INA",
            "IND",
            "IPK",
            "ISL",
            "ITA",
            "JAV",
            "JPN",
            "KAL",
            "KAN",
            "KAS",
            "KAT",
            "KAU",
            "KAZ",
            "KHM",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KOR",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LTZ",
            "LUB",
            "LUG",
            "MAH",
            "MAL",
            "MAR",
            "MKD",
            "MLG",
            "MLT",
            "MON",
            "MRI",
            "MSA",
            "MYA",
            "NAU",
            "NAV",
            "NBL",
            "NDE",
            "NDO",
            "NEP",
            "NLD",
            "NNO",
            "NOB",
            "NOR",
            "NYA",
            "OCI",
            "OJI",
            "ORI",
            "ORJ",
            "ORM",
            "OSS",
            "PAN",
            "PLI",
            "POL",
            "POR",
            "PUS",
            "QAA",
            "QPC",
            "QUE",
            "ROH",
            "RON",
            "RUN",
            "RUS",
            "SAG",
            "SAN",
            "SIN",
            "SLK",
            "SLV",
            "SME",
            "SMO",
            "SNA",
            "SND",
            "SOM",
            "SOT",
            "SPA",
            "SQI",
            "SRB",
            "SRD",
            "SRP",
            "SSW",
            "SUN",
            "SWA",
            "SWE",
            "TAH",
            "TAM",
            "TAT",
            "TEL",
            "TGK",
            "TGL",
            "THA",
            "TIR",
            "TNG",
            "TON",
            "TSN",
            "TSO",
            "TUK",
            "TUR",
            "TWI",
            "UIG",
            "UKR",
            "URD",
            "UZB",
            "VEN",
            "VIE",
            "VOL",
            "WLN",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZHO",
            "ZUL",
        ]
    ] = Field(default=None, alias="LanguageCode")
    offset: Optional[int] = Field(default=None, alias="Offset")
    pids: Optional[Sequence[int]] = Field(default=None, alias="Pids")
    program_selection: Optional[int] = Field(default=None, alias="ProgramSelection")
    remix_settings: Optional[RemixSettingsModel] = Field(
        default=None, alias="RemixSettings"
    )
    selector_type: Optional[
        Literal["HLS_RENDITION_GROUP", "LANGUAGE_CODE", "PID", "TRACK"]
    ] = Field(default=None, alias="SelectorType")
    tracks: Optional[Sequence[int]] = Field(default=None, alias="Tracks")


class CmafGroupSettingsModel(BaseModel):
    additional_manifests: Optional[Sequence[CmafAdditionalManifestModel]] = Field(
        default=None, alias="AdditionalManifests"
    )
    base_url: Optional[str] = Field(default=None, alias="BaseUrl")
    client_cache: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ClientCache"
    )
    codec_specification: Optional[Literal["RFC_4281", "RFC_6381"]] = Field(
        default=None, alias="CodecSpecification"
    )
    dash_manifest_style: Optional[Literal["BASIC", "COMPACT", "DISTINCT"]] = Field(
        default=None, alias="DashManifestStyle"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")
    destination_settings: Optional[DestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )
    encryption: Optional[CmafEncryptionSettingsModel] = Field(
        default=None, alias="Encryption"
    )
    fragment_length: Optional[int] = Field(default=None, alias="FragmentLength")
    image_based_trick_play: Optional[
        Literal["ADVANCED", "NONE", "THUMBNAIL", "THUMBNAIL_AND_FULLFRAME"]
    ] = Field(default=None, alias="ImageBasedTrickPlay")
    image_based_trick_play_settings: Optional[
        CmafImageBasedTrickPlaySettingsModel
    ] = Field(default=None, alias="ImageBasedTrickPlaySettings")
    manifest_compression: Optional[Literal["GZIP", "NONE"]] = Field(
        default=None, alias="ManifestCompression"
    )
    manifest_duration_format: Optional[Literal["FLOATING_POINT", "INTEGER"]] = Field(
        default=None, alias="ManifestDurationFormat"
    )
    min_buffer_time: Optional[int] = Field(default=None, alias="MinBufferTime")
    min_final_segment_length: Optional[float] = Field(
        default=None, alias="MinFinalSegmentLength"
    )
    mpd_manifest_bandwidth_type: Optional[Literal["AVERAGE", "MAX"]] = Field(
        default=None, alias="MpdManifestBandwidthType"
    )
    mpd_profile: Optional[Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"]] = Field(
        default=None, alias="MpdProfile"
    )
    pts_offset_handling_for_bframes: Optional[
        Literal["MATCH_INITIAL_PTS", "ZERO_BASED"]
    ] = Field(default=None, alias="PtsOffsetHandlingForBFrames")
    segment_control: Optional[Literal["SEGMENTED_FILES", "SINGLE_FILE"]] = Field(
        default=None, alias="SegmentControl"
    )
    segment_length: Optional[int] = Field(default=None, alias="SegmentLength")
    segment_length_control: Optional[Literal["EXACT", "GOP_MULTIPLE"]] = Field(
        default=None, alias="SegmentLengthControl"
    )
    stream_inf_resolution: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="StreamInfResolution"
    )
    target_duration_compatibility_mode: Optional[
        Literal["LEGACY", "SPEC_COMPLIANT"]
    ] = Field(default=None, alias="TargetDurationCompatibilityMode")
    video_composition_offsets: Optional[Literal["SIGNED", "UNSIGNED"]] = Field(
        default=None, alias="VideoCompositionOffsets"
    )
    write_dash_manifest: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="WriteDashManifest"
    )
    write_hls_manifest: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="WriteHlsManifest"
    )
    write_segment_timeline_in_representation: Optional[
        Literal["DISABLED", "ENABLED"]
    ] = Field(default=None, alias="WriteSegmentTimelineInRepresentation")


class DashIsoGroupSettingsModel(BaseModel):
    additional_manifests: Optional[Sequence[DashAdditionalManifestModel]] = Field(
        default=None, alias="AdditionalManifests"
    )
    audio_channel_config_scheme_id_uri: Optional[
        Literal["DOLBY_CHANNEL_CONFIGURATION", "MPEG_CHANNEL_CONFIGURATION"]
    ] = Field(default=None, alias="AudioChannelConfigSchemeIdUri")
    base_url: Optional[str] = Field(default=None, alias="BaseUrl")
    dash_manifest_style: Optional[Literal["BASIC", "COMPACT", "DISTINCT"]] = Field(
        default=None, alias="DashManifestStyle"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")
    destination_settings: Optional[DestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )
    encryption: Optional[DashIsoEncryptionSettingsModel] = Field(
        default=None, alias="Encryption"
    )
    fragment_length: Optional[int] = Field(default=None, alias="FragmentLength")
    hbbtv_compliance: Optional[Literal["HBBTV_1_5", "NONE"]] = Field(
        default=None, alias="HbbtvCompliance"
    )
    image_based_trick_play: Optional[
        Literal["ADVANCED", "NONE", "THUMBNAIL", "THUMBNAIL_AND_FULLFRAME"]
    ] = Field(default=None, alias="ImageBasedTrickPlay")
    image_based_trick_play_settings: Optional[
        DashIsoImageBasedTrickPlaySettingsModel
    ] = Field(default=None, alias="ImageBasedTrickPlaySettings")
    min_buffer_time: Optional[int] = Field(default=None, alias="MinBufferTime")
    min_final_segment_length: Optional[float] = Field(
        default=None, alias="MinFinalSegmentLength"
    )
    mpd_manifest_bandwidth_type: Optional[Literal["AVERAGE", "MAX"]] = Field(
        default=None, alias="MpdManifestBandwidthType"
    )
    mpd_profile: Optional[Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"]] = Field(
        default=None, alias="MpdProfile"
    )
    pts_offset_handling_for_bframes: Optional[
        Literal["MATCH_INITIAL_PTS", "ZERO_BASED"]
    ] = Field(default=None, alias="PtsOffsetHandlingForBFrames")
    segment_control: Optional[Literal["SEGMENTED_FILES", "SINGLE_FILE"]] = Field(
        default=None, alias="SegmentControl"
    )
    segment_length: Optional[int] = Field(default=None, alias="SegmentLength")
    segment_length_control: Optional[Literal["EXACT", "GOP_MULTIPLE"]] = Field(
        default=None, alias="SegmentLengthControl"
    )
    video_composition_offsets: Optional[Literal["SIGNED", "UNSIGNED"]] = Field(
        default=None, alias="VideoCompositionOffsets"
    )
    write_segment_timeline_in_representation: Optional[
        Literal["DISABLED", "ENABLED"]
    ] = Field(default=None, alias="WriteSegmentTimelineInRepresentation")


class FileGroupSettingsModel(BaseModel):
    destination: Optional[str] = Field(default=None, alias="Destination")
    destination_settings: Optional[DestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )


class HlsGroupSettingsModel(BaseModel):
    ad_markers: Optional[Sequence[Literal["ELEMENTAL", "ELEMENTAL_SCTE35"]]] = Field(
        default=None, alias="AdMarkers"
    )
    additional_manifests: Optional[Sequence[HlsAdditionalManifestModel]] = Field(
        default=None, alias="AdditionalManifests"
    )
    audio_only_header: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="AudioOnlyHeader"
    )
    base_url: Optional[str] = Field(default=None, alias="BaseUrl")
    caption_language_mappings: Optional[
        Sequence[HlsCaptionLanguageMappingModel]
    ] = Field(default=None, alias="CaptionLanguageMappings")
    caption_language_setting: Optional[Literal["INSERT", "NONE", "OMIT"]] = Field(
        default=None, alias="CaptionLanguageSetting"
    )
    caption_segment_length_control: Optional[
        Literal["LARGE_SEGMENTS", "MATCH_VIDEO"]
    ] = Field(default=None, alias="CaptionSegmentLengthControl")
    client_cache: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="ClientCache"
    )
    codec_specification: Optional[Literal["RFC_4281", "RFC_6381"]] = Field(
        default=None, alias="CodecSpecification"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")
    destination_settings: Optional[DestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )
    directory_structure: Optional[
        Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
    ] = Field(default=None, alias="DirectoryStructure")
    encryption: Optional[HlsEncryptionSettingsModel] = Field(
        default=None, alias="Encryption"
    )
    image_based_trick_play: Optional[
        Literal["ADVANCED", "NONE", "THUMBNAIL", "THUMBNAIL_AND_FULLFRAME"]
    ] = Field(default=None, alias="ImageBasedTrickPlay")
    image_based_trick_play_settings: Optional[
        HlsImageBasedTrickPlaySettingsModel
    ] = Field(default=None, alias="ImageBasedTrickPlaySettings")
    manifest_compression: Optional[Literal["GZIP", "NONE"]] = Field(
        default=None, alias="ManifestCompression"
    )
    manifest_duration_format: Optional[Literal["FLOATING_POINT", "INTEGER"]] = Field(
        default=None, alias="ManifestDurationFormat"
    )
    min_final_segment_length: Optional[float] = Field(
        default=None, alias="MinFinalSegmentLength"
    )
    min_segment_length: Optional[int] = Field(default=None, alias="MinSegmentLength")
    output_selection: Optional[
        Literal["MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY"]
    ] = Field(default=None, alias="OutputSelection")
    program_date_time: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="ProgramDateTime"
    )
    program_date_time_period: Optional[int] = Field(
        default=None, alias="ProgramDateTimePeriod"
    )
    segment_control: Optional[Literal["SEGMENTED_FILES", "SINGLE_FILE"]] = Field(
        default=None, alias="SegmentControl"
    )
    segment_length: Optional[int] = Field(default=None, alias="SegmentLength")
    segment_length_control: Optional[Literal["EXACT", "GOP_MULTIPLE"]] = Field(
        default=None, alias="SegmentLengthControl"
    )
    segments_per_subdirectory: Optional[int] = Field(
        default=None, alias="SegmentsPerSubdirectory"
    )
    stream_inf_resolution: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="StreamInfResolution"
    )
    target_duration_compatibility_mode: Optional[
        Literal["LEGACY", "SPEC_COMPLIANT"]
    ] = Field(default=None, alias="TargetDurationCompatibilityMode")
    timed_metadata_id3_frame: Optional[Literal["NONE", "PRIV", "TDRL"]] = Field(
        default=None, alias="TimedMetadataId3Frame"
    )
    timed_metadata_id3_period: Optional[int] = Field(
        default=None, alias="TimedMetadataId3Period"
    )
    timestamp_delta_milliseconds: Optional[int] = Field(
        default=None, alias="TimestampDeltaMilliseconds"
    )


class MsSmoothGroupSettingsModel(BaseModel):
    additional_manifests: Optional[Sequence[MsSmoothAdditionalManifestModel]] = Field(
        default=None, alias="AdditionalManifests"
    )
    audio_deduplication: Optional[Literal["COMBINE_DUPLICATE_STREAMS", "NONE"]] = Field(
        default=None, alias="AudioDeduplication"
    )
    destination: Optional[str] = Field(default=None, alias="Destination")
    destination_settings: Optional[DestinationSettingsModel] = Field(
        default=None, alias="DestinationSettings"
    )
    encryption: Optional[MsSmoothEncryptionSettingsModel] = Field(
        default=None, alias="Encryption"
    )
    fragment_length: Optional[int] = Field(default=None, alias="FragmentLength")
    fragment_length_control: Optional[Literal["EXACT", "GOP_MULTIPLE"]] = Field(
        default=None, alias="FragmentLengthControl"
    )
    manifest_encoding: Optional[Literal["UTF16", "UTF8"]] = Field(
        default=None, alias="ManifestEncoding"
    )


class VideoDescriptionModel(BaseModel):
    afd_signaling: Optional[Literal["AUTO", "FIXED", "NONE"]] = Field(
        default=None, alias="AfdSignaling"
    )
    anti_alias: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AntiAlias"
    )
    codec_settings: Optional[VideoCodecSettingsModel] = Field(
        default=None, alias="CodecSettings"
    )
    color_metadata: Optional[Literal["IGNORE", "INSERT"]] = Field(
        default=None, alias="ColorMetadata"
    )
    crop: Optional[RectangleModel] = Field(default=None, alias="Crop")
    drop_frame_timecode: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DropFrameTimecode"
    )
    fixed_afd: Optional[int] = Field(default=None, alias="FixedAfd")
    height: Optional[int] = Field(default=None, alias="Height")
    position: Optional[RectangleModel] = Field(default=None, alias="Position")
    respond_to_afd: Optional[Literal["NONE", "PASSTHROUGH", "RESPOND"]] = Field(
        default=None, alias="RespondToAfd"
    )
    scaling_behavior: Optional[Literal["DEFAULT", "STRETCH_TO_OUTPUT"]] = Field(
        default=None, alias="ScalingBehavior"
    )
    sharpness: Optional[int] = Field(default=None, alias="Sharpness")
    timecode_insertion: Optional[Literal["DISABLED", "PIC_TIMING_SEI"]] = Field(
        default=None, alias="TimecodeInsertion"
    )
    video_preprocessors: Optional[VideoPreprocessorModel] = Field(
        default=None, alias="VideoPreprocessors"
    )
    width: Optional[int] = Field(default=None, alias="Width")


class InputTemplateModel(BaseModel):
    audio_selector_groups: Optional[Mapping[str, AudioSelectorGroupModel]] = Field(
        default=None, alias="AudioSelectorGroups"
    )
    audio_selectors: Optional[Mapping[str, AudioSelectorModel]] = Field(
        default=None, alias="AudioSelectors"
    )
    caption_selectors: Optional[Mapping[str, CaptionSelectorModel]] = Field(
        default=None, alias="CaptionSelectors"
    )
    crop: Optional[RectangleModel] = Field(default=None, alias="Crop")
    deblock_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DeblockFilter"
    )
    denoise_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DenoiseFilter"
    )
    dolby_vision_metadata_xml: Optional[str] = Field(
        default=None, alias="DolbyVisionMetadataXml"
    )
    filter_enable: Optional[Literal["AUTO", "DISABLE", "FORCE"]] = Field(
        default=None, alias="FilterEnable"
    )
    filter_strength: Optional[int] = Field(default=None, alias="FilterStrength")
    image_inserter: Optional[ImageInserterModel] = Field(
        default=None, alias="ImageInserter"
    )
    input_clippings: Optional[Sequence[InputClippingModel]] = Field(
        default=None, alias="InputClippings"
    )
    input_scan_type: Optional[Literal["AUTO", "PSF"]] = Field(
        default=None, alias="InputScanType"
    )
    position: Optional[RectangleModel] = Field(default=None, alias="Position")
    program_number: Optional[int] = Field(default=None, alias="ProgramNumber")
    psi_control: Optional[Literal["IGNORE_PSI", "USE_PSI"]] = Field(
        default=None, alias="PsiControl"
    )
    timecode_source: Optional[
        Literal["EMBEDDED", "SPECIFIEDSTART", "ZEROBASED"]
    ] = Field(default=None, alias="TimecodeSource")
    timecode_start: Optional[str] = Field(default=None, alias="TimecodeStart")
    video_selector: Optional[VideoSelectorModel] = Field(
        default=None, alias="VideoSelector"
    )


class InputModel(BaseModel):
    audio_selector_groups: Optional[Mapping[str, AudioSelectorGroupModel]] = Field(
        default=None, alias="AudioSelectorGroups"
    )
    audio_selectors: Optional[Mapping[str, AudioSelectorModel]] = Field(
        default=None, alias="AudioSelectors"
    )
    caption_selectors: Optional[Mapping[str, CaptionSelectorModel]] = Field(
        default=None, alias="CaptionSelectors"
    )
    crop: Optional[RectangleModel] = Field(default=None, alias="Crop")
    deblock_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DeblockFilter"
    )
    decryption_settings: Optional[InputDecryptionSettingsModel] = Field(
        default=None, alias="DecryptionSettings"
    )
    denoise_filter: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="DenoiseFilter"
    )
    dolby_vision_metadata_xml: Optional[str] = Field(
        default=None, alias="DolbyVisionMetadataXml"
    )
    file_input: Optional[str] = Field(default=None, alias="FileInput")
    filter_enable: Optional[Literal["AUTO", "DISABLE", "FORCE"]] = Field(
        default=None, alias="FilterEnable"
    )
    filter_strength: Optional[int] = Field(default=None, alias="FilterStrength")
    image_inserter: Optional[ImageInserterModel] = Field(
        default=None, alias="ImageInserter"
    )
    input_clippings: Optional[Sequence[InputClippingModel]] = Field(
        default=None, alias="InputClippings"
    )
    input_scan_type: Optional[Literal["AUTO", "PSF"]] = Field(
        default=None, alias="InputScanType"
    )
    position: Optional[RectangleModel] = Field(default=None, alias="Position")
    program_number: Optional[int] = Field(default=None, alias="ProgramNumber")
    psi_control: Optional[Literal["IGNORE_PSI", "USE_PSI"]] = Field(
        default=None, alias="PsiControl"
    )
    supplemental_imps: Optional[Sequence[str]] = Field(
        default=None, alias="SupplementalImps"
    )
    timecode_source: Optional[
        Literal["EMBEDDED", "SPECIFIEDSTART", "ZEROBASED"]
    ] = Field(default=None, alias="TimecodeSource")
    timecode_start: Optional[str] = Field(default=None, alias="TimecodeStart")
    video_generator: Optional[InputVideoGeneratorModel] = Field(
        default=None, alias="VideoGenerator"
    )
    video_selector: Optional[VideoSelectorModel] = Field(
        default=None, alias="VideoSelector"
    )


class OutputGroupSettingsModel(BaseModel):
    cmaf_group_settings: Optional[CmafGroupSettingsModel] = Field(
        default=None, alias="CmafGroupSettings"
    )
    dash_iso_group_settings: Optional[DashIsoGroupSettingsModel] = Field(
        default=None, alias="DashIsoGroupSettings"
    )
    file_group_settings: Optional[FileGroupSettingsModel] = Field(
        default=None, alias="FileGroupSettings"
    )
    hls_group_settings: Optional[HlsGroupSettingsModel] = Field(
        default=None, alias="HlsGroupSettings"
    )
    ms_smooth_group_settings: Optional[MsSmoothGroupSettingsModel] = Field(
        default=None, alias="MsSmoothGroupSettings"
    )
    type: Optional[
        Literal[
            "CMAF_GROUP_SETTINGS",
            "DASH_ISO_GROUP_SETTINGS",
            "FILE_GROUP_SETTINGS",
            "HLS_GROUP_SETTINGS",
            "MS_SMOOTH_GROUP_SETTINGS",
        ]
    ] = Field(default=None, alias="Type")


class OutputModel(BaseModel):
    audio_descriptions: Optional[Sequence[AudioDescriptionModel]] = Field(
        default=None, alias="AudioDescriptions"
    )
    caption_descriptions: Optional[Sequence[CaptionDescriptionModel]] = Field(
        default=None, alias="CaptionDescriptions"
    )
    container_settings: Optional[ContainerSettingsModel] = Field(
        default=None, alias="ContainerSettings"
    )
    extension: Optional[str] = Field(default=None, alias="Extension")
    name_modifier: Optional[str] = Field(default=None, alias="NameModifier")
    output_settings: Optional[OutputSettingsModel] = Field(
        default=None, alias="OutputSettings"
    )
    preset: Optional[str] = Field(default=None, alias="Preset")
    video_description: Optional[VideoDescriptionModel] = Field(
        default=None, alias="VideoDescription"
    )


class PresetSettingsModel(BaseModel):
    audio_descriptions: Optional[Sequence[AudioDescriptionModel]] = Field(
        default=None, alias="AudioDescriptions"
    )
    caption_descriptions: Optional[Sequence[CaptionDescriptionPresetModel]] = Field(
        default=None, alias="CaptionDescriptions"
    )
    container_settings: Optional[ContainerSettingsModel] = Field(
        default=None, alias="ContainerSettings"
    )
    video_description: Optional[VideoDescriptionModel] = Field(
        default=None, alias="VideoDescription"
    )


class OutputGroupModel(BaseModel):
    automated_encoding_settings: Optional[AutomatedEncodingSettingsModel] = Field(
        default=None, alias="AutomatedEncodingSettings"
    )
    custom_name: Optional[str] = Field(default=None, alias="CustomName")
    name: Optional[str] = Field(default=None, alias="Name")
    output_group_settings: Optional[OutputGroupSettingsModel] = Field(
        default=None, alias="OutputGroupSettings"
    )
    outputs: Optional[Sequence[OutputModel]] = Field(default=None, alias="Outputs")


class CreatePresetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    settings: PresetSettingsModel = Field(alias="Settings")
    category: Optional[str] = Field(default=None, alias="Category")
    description: Optional[str] = Field(default=None, alias="Description")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class PresetModel(BaseModel):
    name: str = Field(alias="Name")
    settings: PresetSettingsModel = Field(alias="Settings")
    arn: Optional[str] = Field(default=None, alias="Arn")
    category: Optional[str] = Field(default=None, alias="Category")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    description: Optional[str] = Field(default=None, alias="Description")
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    type: Optional[Literal["CUSTOM", "SYSTEM"]] = Field(default=None, alias="Type")


class UpdatePresetRequestModel(BaseModel):
    name: str = Field(alias="Name")
    category: Optional[str] = Field(default=None, alias="Category")
    description: Optional[str] = Field(default=None, alias="Description")
    settings: Optional[PresetSettingsModel] = Field(default=None, alias="Settings")


class JobSettingsModel(BaseModel):
    ad_avail_offset: Optional[int] = Field(default=None, alias="AdAvailOffset")
    avail_blanking: Optional[AvailBlankingModel] = Field(
        default=None, alias="AvailBlanking"
    )
    esam: Optional[EsamSettingsModel] = Field(default=None, alias="Esam")
    extended_data_services: Optional[ExtendedDataServicesModel] = Field(
        default=None, alias="ExtendedDataServices"
    )
    inputs: Optional[Sequence[InputModel]] = Field(default=None, alias="Inputs")
    kantar_watermark: Optional[KantarWatermarkSettingsModel] = Field(
        default=None, alias="KantarWatermark"
    )
    motion_image_inserter: Optional[MotionImageInserterModel] = Field(
        default=None, alias="MotionImageInserter"
    )
    nielsen_configuration: Optional[NielsenConfigurationModel] = Field(
        default=None, alias="NielsenConfiguration"
    )
    nielsen_non_linear_watermark: Optional[
        NielsenNonLinearWatermarkSettingsModel
    ] = Field(default=None, alias="NielsenNonLinearWatermark")
    output_groups: Optional[Sequence[OutputGroupModel]] = Field(
        default=None, alias="OutputGroups"
    )
    timecode_config: Optional[TimecodeConfigModel] = Field(
        default=None, alias="TimecodeConfig"
    )
    timed_metadata_insertion: Optional[TimedMetadataInsertionModel] = Field(
        default=None, alias="TimedMetadataInsertion"
    )


class JobTemplateSettingsModel(BaseModel):
    ad_avail_offset: Optional[int] = Field(default=None, alias="AdAvailOffset")
    avail_blanking: Optional[AvailBlankingModel] = Field(
        default=None, alias="AvailBlanking"
    )
    esam: Optional[EsamSettingsModel] = Field(default=None, alias="Esam")
    extended_data_services: Optional[ExtendedDataServicesModel] = Field(
        default=None, alias="ExtendedDataServices"
    )
    inputs: Optional[Sequence[InputTemplateModel]] = Field(default=None, alias="Inputs")
    kantar_watermark: Optional[KantarWatermarkSettingsModel] = Field(
        default=None, alias="KantarWatermark"
    )
    motion_image_inserter: Optional[MotionImageInserterModel] = Field(
        default=None, alias="MotionImageInserter"
    )
    nielsen_configuration: Optional[NielsenConfigurationModel] = Field(
        default=None, alias="NielsenConfiguration"
    )
    nielsen_non_linear_watermark: Optional[
        NielsenNonLinearWatermarkSettingsModel
    ] = Field(default=None, alias="NielsenNonLinearWatermark")
    output_groups: Optional[Sequence[OutputGroupModel]] = Field(
        default=None, alias="OutputGroups"
    )
    timecode_config: Optional[TimecodeConfigModel] = Field(
        default=None, alias="TimecodeConfig"
    )
    timed_metadata_insertion: Optional[TimedMetadataInsertionModel] = Field(
        default=None, alias="TimedMetadataInsertion"
    )


class CreatePresetResponseModel(BaseModel):
    preset: PresetModel = Field(alias="Preset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetPresetResponseModel(BaseModel):
    preset: PresetModel = Field(alias="Preset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListPresetsResponseModel(BaseModel):
    next_token: str = Field(alias="NextToken")
    presets: List[PresetModel] = Field(alias="Presets")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePresetResponseModel(BaseModel):
    preset: PresetModel = Field(alias="Preset")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobRequestModel(BaseModel):
    role: str = Field(alias="Role")
    settings: JobSettingsModel = Field(alias="Settings")
    acceleration_settings: Optional[AccelerationSettingsModel] = Field(
        default=None, alias="AccelerationSettings"
    )
    billing_tags_source: Optional[
        Literal["JOB", "JOB_TEMPLATE", "PRESET", "QUEUE"]
    ] = Field(default=None, alias="BillingTagsSource")
    client_request_token: Optional[str] = Field(
        default=None, alias="ClientRequestToken"
    )
    hop_destinations: Optional[Sequence[HopDestinationModel]] = Field(
        default=None, alias="HopDestinations"
    )
    job_template: Optional[str] = Field(default=None, alias="JobTemplate")
    priority: Optional[int] = Field(default=None, alias="Priority")
    queue: Optional[str] = Field(default=None, alias="Queue")
    simulate_reserved_queue: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SimulateReservedQueue"
    )
    status_update_interval: Optional[
        Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_120",
            "SECONDS_15",
            "SECONDS_180",
            "SECONDS_20",
            "SECONDS_240",
            "SECONDS_30",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_60",
            "SECONDS_600",
        ]
    ] = Field(default=None, alias="StatusUpdateInterval")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")
    user_metadata: Optional[Mapping[str, str]] = Field(
        default=None, alias="UserMetadata"
    )


class JobModel(BaseModel):
    role: str = Field(alias="Role")
    settings: JobSettingsModel = Field(alias="Settings")
    acceleration_settings: Optional[AccelerationSettingsModel] = Field(
        default=None, alias="AccelerationSettings"
    )
    acceleration_status: Optional[
        Literal["ACCELERATED", "IN_PROGRESS", "NOT_ACCELERATED", "NOT_APPLICABLE"]
    ] = Field(default=None, alias="AccelerationStatus")
    arn: Optional[str] = Field(default=None, alias="Arn")
    billing_tags_source: Optional[
        Literal["JOB", "JOB_TEMPLATE", "PRESET", "QUEUE"]
    ] = Field(default=None, alias="BillingTagsSource")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    current_phase: Optional[Literal["PROBING", "TRANSCODING", "UPLOADING"]] = Field(
        default=None, alias="CurrentPhase"
    )
    error_code: Optional[int] = Field(default=None, alias="ErrorCode")
    error_message: Optional[str] = Field(default=None, alias="ErrorMessage")
    hop_destinations: Optional[List[HopDestinationModel]] = Field(
        default=None, alias="HopDestinations"
    )
    id: Optional[str] = Field(default=None, alias="Id")
    job_percent_complete: Optional[int] = Field(
        default=None, alias="JobPercentComplete"
    )
    job_template: Optional[str] = Field(default=None, alias="JobTemplate")
    messages: Optional[JobMessagesModel] = Field(default=None, alias="Messages")
    output_group_details: Optional[List[OutputGroupDetailModel]] = Field(
        default=None, alias="OutputGroupDetails"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    queue: Optional[str] = Field(default=None, alias="Queue")
    queue_transitions: Optional[List[QueueTransitionModel]] = Field(
        default=None, alias="QueueTransitions"
    )
    retry_count: Optional[int] = Field(default=None, alias="RetryCount")
    simulate_reserved_queue: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="SimulateReservedQueue"
    )
    status: Optional[
        Literal["CANCELED", "COMPLETE", "ERROR", "PROGRESSING", "SUBMITTED"]
    ] = Field(default=None, alias="Status")
    status_update_interval: Optional[
        Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_120",
            "SECONDS_15",
            "SECONDS_180",
            "SECONDS_20",
            "SECONDS_240",
            "SECONDS_30",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_60",
            "SECONDS_600",
        ]
    ] = Field(default=None, alias="StatusUpdateInterval")
    timing: Optional[TimingModel] = Field(default=None, alias="Timing")
    user_metadata: Optional[Dict[str, str]] = Field(default=None, alias="UserMetadata")


class CreateJobTemplateRequestModel(BaseModel):
    name: str = Field(alias="Name")
    settings: JobTemplateSettingsModel = Field(alias="Settings")
    acceleration_settings: Optional[AccelerationSettingsModel] = Field(
        default=None, alias="AccelerationSettings"
    )
    category: Optional[str] = Field(default=None, alias="Category")
    description: Optional[str] = Field(default=None, alias="Description")
    hop_destinations: Optional[Sequence[HopDestinationModel]] = Field(
        default=None, alias="HopDestinations"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    queue: Optional[str] = Field(default=None, alias="Queue")
    status_update_interval: Optional[
        Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_120",
            "SECONDS_15",
            "SECONDS_180",
            "SECONDS_20",
            "SECONDS_240",
            "SECONDS_30",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_60",
            "SECONDS_600",
        ]
    ] = Field(default=None, alias="StatusUpdateInterval")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="Tags")


class JobTemplateModel(BaseModel):
    name: str = Field(alias="Name")
    settings: JobTemplateSettingsModel = Field(alias="Settings")
    acceleration_settings: Optional[AccelerationSettingsModel] = Field(
        default=None, alias="AccelerationSettings"
    )
    arn: Optional[str] = Field(default=None, alias="Arn")
    category: Optional[str] = Field(default=None, alias="Category")
    created_at: Optional[datetime] = Field(default=None, alias="CreatedAt")
    description: Optional[str] = Field(default=None, alias="Description")
    hop_destinations: Optional[List[HopDestinationModel]] = Field(
        default=None, alias="HopDestinations"
    )
    last_updated: Optional[datetime] = Field(default=None, alias="LastUpdated")
    priority: Optional[int] = Field(default=None, alias="Priority")
    queue: Optional[str] = Field(default=None, alias="Queue")
    status_update_interval: Optional[
        Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_120",
            "SECONDS_15",
            "SECONDS_180",
            "SECONDS_20",
            "SECONDS_240",
            "SECONDS_30",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_60",
            "SECONDS_600",
        ]
    ] = Field(default=None, alias="StatusUpdateInterval")
    type: Optional[Literal["CUSTOM", "SYSTEM"]] = Field(default=None, alias="Type")


class UpdateJobTemplateRequestModel(BaseModel):
    name: str = Field(alias="Name")
    acceleration_settings: Optional[AccelerationSettingsModel] = Field(
        default=None, alias="AccelerationSettings"
    )
    category: Optional[str] = Field(default=None, alias="Category")
    description: Optional[str] = Field(default=None, alias="Description")
    hop_destinations: Optional[Sequence[HopDestinationModel]] = Field(
        default=None, alias="HopDestinations"
    )
    priority: Optional[int] = Field(default=None, alias="Priority")
    queue: Optional[str] = Field(default=None, alias="Queue")
    settings: Optional[JobTemplateSettingsModel] = Field(default=None, alias="Settings")
    status_update_interval: Optional[
        Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_120",
            "SECONDS_15",
            "SECONDS_180",
            "SECONDS_20",
            "SECONDS_240",
            "SECONDS_30",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_60",
            "SECONDS_600",
        ]
    ] = Field(default=None, alias="StatusUpdateInterval")


class CreateJobResponseModel(BaseModel):
    job: JobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobResponseModel(BaseModel):
    job: JobModel = Field(alias="Job")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobsResponseModel(BaseModel):
    jobs: List[JobModel] = Field(alias="Jobs")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateJobTemplateResponseModel(BaseModel):
    job_template: JobTemplateModel = Field(alias="JobTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetJobTemplateResponseModel(BaseModel):
    job_template: JobTemplateModel = Field(alias="JobTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListJobTemplatesResponseModel(BaseModel):
    job_templates: List[JobTemplateModel] = Field(alias="JobTemplates")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateJobTemplateResponseModel(BaseModel):
    job_template: JobTemplateModel = Field(alias="JobTemplate")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
