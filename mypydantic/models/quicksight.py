# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class AccountCustomizationModel(BaseModel):
    default_theme: Optional[str] = Field(default=None, alias="DefaultTheme")
    default_email_customization_template: Optional[str] = Field(
        default=None, alias="DefaultEmailCustomizationTemplate"
    )


class AccountInfoModel(BaseModel):
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    edition: Optional[Literal["ENTERPRISE", "ENTERPRISE_AND_Q", "STANDARD"]] = Field(
        default=None, alias="Edition"
    )
    notification_email: Optional[str] = Field(default=None, alias="NotificationEmail")
    authentication_type: Optional[str] = Field(default=None, alias="AuthenticationType")
    account_subscription_status: Optional[str] = Field(
        default=None, alias="AccountSubscriptionStatus"
    )


class AccountSettingsModel(BaseModel):
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    edition: Optional[Literal["ENTERPRISE", "ENTERPRISE_AND_Q", "STANDARD"]] = Field(
        default=None, alias="Edition"
    )
    default_namespace: Optional[str] = Field(default=None, alias="DefaultNamespace")
    notification_email: Optional[str] = Field(default=None, alias="NotificationEmail")
    public_sharing_enabled: Optional[bool] = Field(
        default=None, alias="PublicSharingEnabled"
    )
    termination_protection_enabled: Optional[bool] = Field(
        default=None, alias="TerminationProtectionEnabled"
    )


class ActiveIAMPolicyAssignmentModel(BaseModel):
    assignment_name: Optional[str] = Field(default=None, alias="AssignmentName")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")


class AdHocFilteringOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class ColumnIdentifierModel(BaseModel):
    data_set_identifier: str = Field(alias="DataSetIdentifier")
    column_name: str = Field(alias="ColumnName")


class AmazonElasticsearchParametersModel(BaseModel):
    domain: str = Field(alias="Domain")


class AmazonOpenSearchParametersModel(BaseModel):
    domain: str = Field(alias="Domain")


class CalculatedFieldModel(BaseModel):
    data_set_identifier: str = Field(alias="DataSetIdentifier")
    name: str = Field(alias="Name")
    expression: str = Field(alias="Expression")


class DataSetIdentifierDeclarationModel(BaseModel):
    identifier: str = Field(alias="Identifier")
    data_set_arn: str = Field(alias="DataSetArn")


class EntityModel(BaseModel):
    path: Optional[str] = Field(default=None, alias="Path")


class AnalysisSearchFilterModel(BaseModel):
    operator: Optional[Literal["StringEquals", "StringLike"]] = Field(
        default=None, alias="Operator"
    )
    name: Optional[
        Literal[
            "ANALYSIS_NAME",
            "DIRECT_QUICKSIGHT_OWNER",
            "DIRECT_QUICKSIGHT_SOLE_OWNER",
            "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
            "QUICKSIGHT_OWNER",
            "QUICKSIGHT_USER",
            "QUICKSIGHT_VIEWER_OR_OWNER",
        ]
    ] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class DataSetReferenceModel(BaseModel):
    data_set_placeholder: str = Field(alias="DataSetPlaceholder")
    data_set_arn: str = Field(alias="DataSetArn")


class AnalysisSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    analysis_id: Optional[str] = Field(default=None, alias="AnalysisId")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class SheetModel(BaseModel):
    sheet_id: Optional[str] = Field(default=None, alias="SheetId")
    name: Optional[str] = Field(default=None, alias="Name")


class AnchorDateConfigurationModel(BaseModel):
    anchor_option: Optional[Literal["NOW"]] = Field(default=None, alias="AnchorOption")
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")


class AnonymousUserDashboardEmbeddingConfigurationModel(BaseModel):
    initial_dashboard_id: str = Field(alias="InitialDashboardId")


class DashboardVisualIdModel(BaseModel):
    dashboard_id: str = Field(alias="DashboardId")
    sheet_id: str = Field(alias="SheetId")
    visual_id: str = Field(alias="VisualId")


class AnonymousUserQSearchBarEmbeddingConfigurationModel(BaseModel):
    initial_topic_id: str = Field(alias="InitialTopicId")


class ArcAxisDisplayRangeModel(BaseModel):
    min: Optional[float] = Field(default=None, alias="Min")
    max: Optional[float] = Field(default=None, alias="Max")


class ArcConfigurationModel(BaseModel):
    arc_angle: Optional[float] = Field(default=None, alias="ArcAngle")
    arc_thickness: Optional[Literal["LARGE", "MEDIUM", "SMALL"]] = Field(
        default=None, alias="ArcThickness"
    )


class ArcOptionsModel(BaseModel):
    arc_thickness: Optional[Literal["LARGE", "MEDIUM", "SMALL", "WHOLE"]] = Field(
        default=None, alias="ArcThickness"
    )


class AthenaParametersModel(BaseModel):
    work_group: Optional[str] = Field(default=None, alias="WorkGroup")
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class AuroraParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class AuroraPostgreSqlParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class AwsIotAnalyticsParametersModel(BaseModel):
    data_set_name: str = Field(alias="DataSetName")


class DateAxisOptionsModel(BaseModel):
    missing_date_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="MissingDateVisibility"
    )


class AxisDisplayMinMaxRangeModel(BaseModel):
    minimum: Optional[float] = Field(default=None, alias="Minimum")
    maximum: Optional[float] = Field(default=None, alias="Maximum")


class AxisLinearScaleModel(BaseModel):
    step_count: Optional[int] = Field(default=None, alias="StepCount")
    step_size: Optional[float] = Field(default=None, alias="StepSize")


class AxisLogarithmicScaleModel(BaseModel):
    base: Optional[float] = Field(default=None, alias="Base")


class ItemsLimitConfigurationModel(BaseModel):
    items_limit: Optional[int] = Field(default=None, alias="ItemsLimit")
    other_categories: Optional[Literal["EXCLUDE", "INCLUDE"]] = Field(
        default=None, alias="OtherCategories"
    )


class BinCountOptionsModel(BaseModel):
    value: Optional[int] = Field(default=None, alias="Value")


class BinWidthOptionsModel(BaseModel):
    value: Optional[float] = Field(default=None, alias="Value")
    bin_count_limit: Optional[int] = Field(default=None, alias="BinCountLimit")


class BorderStyleModel(BaseModel):
    show: Optional[bool] = Field(default=None, alias="Show")


class BoxPlotStyleOptionsModel(BaseModel):
    fill_style: Optional[Literal["SOLID", "TRANSPARENT"]] = Field(
        default=None, alias="FillStyle"
    )


class PaginationConfigurationModel(BaseModel):
    page_size: int = Field(alias="PageSize")
    page_number: int = Field(alias="PageNumber")


class CalculatedColumnModel(BaseModel):
    column_name: str = Field(alias="ColumnName")
    column_id: str = Field(alias="ColumnId")
    expression: str = Field(alias="Expression")


class CalculatedMeasureFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    expression: str = Field(alias="Expression")


class CancelIngestionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")
    ingestion_id: str = Field(alias="IngestionId")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class CastColumnTypeOperationModel(BaseModel):
    column_name: str = Field(alias="ColumnName")
    new_column_type: Literal["DATETIME", "DECIMAL", "INTEGER", "STRING"] = Field(
        alias="NewColumnType"
    )
    format: Optional[str] = Field(default=None, alias="Format")


class CustomFilterConfigurationModel(BaseModel):
    match_operator: Literal[
        "CONTAINS",
        "DOES_NOT_CONTAIN",
        "DOES_NOT_EQUAL",
        "ENDS_WITH",
        "EQUALS",
        "STARTS_WITH",
    ] = Field(alias="MatchOperator")
    null_option: Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"] = Field(
        alias="NullOption"
    )
    category_value: Optional[str] = Field(default=None, alias="CategoryValue")
    select_all_options: Optional[Literal["FILTER_ALL_VALUES"]] = Field(
        default=None, alias="SelectAllOptions"
    )
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")


class CustomFilterListConfigurationModel(BaseModel):
    match_operator: Literal[
        "CONTAINS",
        "DOES_NOT_CONTAIN",
        "DOES_NOT_EQUAL",
        "ENDS_WITH",
        "EQUALS",
        "STARTS_WITH",
    ] = Field(alias="MatchOperator")
    null_option: Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"] = Field(
        alias="NullOption"
    )
    category_values: Optional[Sequence[str]] = Field(
        default=None, alias="CategoryValues"
    )
    select_all_options: Optional[Literal["FILTER_ALL_VALUES"]] = Field(
        default=None, alias="SelectAllOptions"
    )


class FilterListConfigurationModel(BaseModel):
    match_operator: Literal[
        "CONTAINS",
        "DOES_NOT_CONTAIN",
        "DOES_NOT_EQUAL",
        "ENDS_WITH",
        "EQUALS",
        "STARTS_WITH",
    ] = Field(alias="MatchOperator")
    category_values: Optional[Sequence[str]] = Field(
        default=None, alias="CategoryValues"
    )
    select_all_options: Optional[Literal["FILTER_ALL_VALUES"]] = Field(
        default=None, alias="SelectAllOptions"
    )


class SimpleClusterMarkerModel(BaseModel):
    color: Optional[str] = Field(default=None, alias="Color")


class DataColorModel(BaseModel):
    color: Optional[str] = Field(default=None, alias="Color")
    data_value: Optional[float] = Field(default=None, alias="DataValue")


class ColumnDescriptionModel(BaseModel):
    text: Optional[str] = Field(default=None, alias="Text")


class ColumnGroupColumnSchemaModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")


class GeoSpatialColumnGroupModel(BaseModel):
    name: str = Field(alias="Name")
    columns: Sequence[str] = Field(alias="Columns")
    country_code: Optional[Literal["US"]] = Field(default=None, alias="CountryCode")


class ColumnLevelPermissionRuleModel(BaseModel):
    principals: Optional[Sequence[str]] = Field(default=None, alias="Principals")
    column_names: Optional[Sequence[str]] = Field(default=None, alias="ColumnNames")


class ColumnSchemaModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    data_type: Optional[str] = Field(default=None, alias="DataType")
    geographic_role: Optional[str] = Field(default=None, alias="GeographicRole")


class ConditionalFormattingSolidColorModel(BaseModel):
    expression: str = Field(alias="Expression")
    color: Optional[str] = Field(default=None, alias="Color")


class ConditionalFormattingCustomIconOptionsModel(BaseModel):
    icon: Optional[
        Literal[
            "ARROW_DOWN",
            "ARROW_DOWN_LEFT",
            "ARROW_DOWN_RIGHT",
            "ARROW_LEFT",
            "ARROW_RIGHT",
            "ARROW_UP",
            "ARROW_UP_LEFT",
            "ARROW_UP_RIGHT",
            "CARET_DOWN",
            "CARET_UP",
            "CHECKMARK",
            "CIRCLE",
            "FACE_DOWN",
            "FACE_FLAT",
            "FACE_UP",
            "FLAG",
            "MINUS",
            "ONE_BAR",
            "PLUS",
            "SQUARE",
            "THREE_BAR",
            "THUMBS_DOWN",
            "THUMBS_UP",
            "TRIANGLE",
            "TWO_BAR",
            "X",
        ]
    ] = Field(default=None, alias="Icon")
    unicode_icon: Optional[str] = Field(default=None, alias="UnicodeIcon")


class ConditionalFormattingIconDisplayConfigurationModel(BaseModel):
    icon_display_option: Optional[Literal["ICON_ONLY"]] = Field(
        default=None, alias="IconDisplayOption"
    )


class ConditionalFormattingIconSetModel(BaseModel):
    expression: str = Field(alias="Expression")
    icon_set_type: Optional[
        Literal[
            "BARS",
            "CARET_UP_MINUS_DOWN",
            "CHECK_X",
            "FLAGS",
            "FOUR_COLOR_ARROW",
            "FOUR_GRAY_ARROW",
            "PLUS_MINUS",
            "THREE_CIRCLE",
            "THREE_COLOR_ARROW",
            "THREE_GRAY_ARROW",
            "THREE_SHAPE",
        ]
    ] = Field(default=None, alias="IconSetType")


class TagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class CreateAccountSubscriptionRequestModel(BaseModel):
    edition: Literal["ENTERPRISE", "ENTERPRISE_AND_Q", "STANDARD"] = Field(
        alias="Edition"
    )
    authentication_method: Literal[
        "ACTIVE_DIRECTORY", "IAM_AND_QUICKSIGHT", "IAM_ONLY"
    ] = Field(alias="AuthenticationMethod")
    aws_account_id: str = Field(alias="AwsAccountId")
    account_name: str = Field(alias="AccountName")
    notification_email: str = Field(alias="NotificationEmail")
    active_directory_name: Optional[str] = Field(
        default=None, alias="ActiveDirectoryName"
    )
    realm: Optional[str] = Field(default=None, alias="Realm")
    directory_id: Optional[str] = Field(default=None, alias="DirectoryId")
    admin_group: Optional[Sequence[str]] = Field(default=None, alias="AdminGroup")
    author_group: Optional[Sequence[str]] = Field(default=None, alias="AuthorGroup")
    reader_group: Optional[Sequence[str]] = Field(default=None, alias="ReaderGroup")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    email_address: Optional[str] = Field(default=None, alias="EmailAddress")
    contact_number: Optional[str] = Field(default=None, alias="ContactNumber")


class SignupResponseModel(BaseModel):
    iamuser: Optional[bool] = Field(default=None, alias="IAMUser")
    user_login_name: Optional[str] = Field(default=None, alias="userLoginName")
    account_name: Optional[str] = Field(default=None, alias="accountName")
    directory_type: Optional[str] = Field(default=None, alias="directoryType")


class ResourcePermissionModel(BaseModel):
    principal: str = Field(alias="Principal")
    actions: Sequence[str] = Field(alias="Actions")


class DataSetUsageConfigurationModel(BaseModel):
    disable_use_as_direct_query_source: Optional[bool] = Field(
        default=None, alias="DisableUseAsDirectQuerySource"
    )
    disable_use_as_imported_source: Optional[bool] = Field(
        default=None, alias="DisableUseAsImportedSource"
    )


class FieldFolderModel(BaseModel):
    description: Optional[str] = Field(default=None, alias="description")
    columns: Optional[Sequence[str]] = Field(default=None, alias="columns")


class RowLevelPermissionDataSetModel(BaseModel):
    arn: str = Field(alias="Arn")
    permission_policy: Literal["DENY_ACCESS", "GRANT_ACCESS"] = Field(
        alias="PermissionPolicy"
    )
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    format_version: Optional[Literal["VERSION_1", "VERSION_2"]] = Field(
        default=None, alias="FormatVersion"
    )
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class SslPropertiesModel(BaseModel):
    disable_ssl: Optional[bool] = Field(default=None, alias="DisableSsl")


class VpcConnectionPropertiesModel(BaseModel):
    vpc_connection_arn: str = Field(alias="VpcConnectionArn")


class CreateFolderMembershipRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")
    member_id: str = Field(alias="MemberId")
    member_type: Literal["ANALYSIS", "DASHBOARD", "DATASET"] = Field(alias="MemberType")


class FolderMemberModel(BaseModel):
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    member_type: Optional[Literal["ANALYSIS", "DASHBOARD", "DATASET"]] = Field(
        default=None, alias="MemberType"
    )


class CreateGroupMembershipRequestModel(BaseModel):
    member_name: str = Field(alias="MemberName")
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class GroupMemberModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    member_name: Optional[str] = Field(default=None, alias="MemberName")


class CreateGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    description: Optional[str] = Field(default=None, alias="Description")


class GroupModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    group_name: Optional[str] = Field(default=None, alias="GroupName")
    description: Optional[str] = Field(default=None, alias="Description")
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")


class CreateIAMPolicyAssignmentRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    assignment_name: str = Field(alias="AssignmentName")
    assignment_status: Literal["DISABLED", "DRAFT", "ENABLED"] = Field(
        alias="AssignmentStatus"
    )
    namespace: str = Field(alias="Namespace")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")
    identities: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Identities"
    )


class CreateIngestionRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    ingestion_id: str = Field(alias="IngestionId")
    aws_account_id: str = Field(alias="AwsAccountId")
    ingestion_type: Optional[Literal["FULL_REFRESH", "INCREMENTAL_REFRESH"]] = Field(
        default=None, alias="IngestionType"
    )


class CreateTemplateAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    alias_name: str = Field(alias="AliasName")
    template_version_number: int = Field(alias="TemplateVersionNumber")


class TemplateAliasModel(BaseModel):
    alias_name: Optional[str] = Field(default=None, alias="AliasName")
    arn: Optional[str] = Field(default=None, alias="Arn")
    template_version_number: Optional[int] = Field(
        default=None, alias="TemplateVersionNumber"
    )


class CreateThemeAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    alias_name: str = Field(alias="AliasName")
    theme_version_number: int = Field(alias="ThemeVersionNumber")


class ThemeAliasModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    alias_name: Optional[str] = Field(default=None, alias="AliasName")
    theme_version_number: Optional[int] = Field(
        default=None, alias="ThemeVersionNumber"
    )


class DecimalPlacesConfigurationModel(BaseModel):
    decimal_places: int = Field(alias="DecimalPlaces")


class NegativeValueConfigurationModel(BaseModel):
    display_mode: Literal["NEGATIVE", "POSITIVE"] = Field(alias="DisplayMode")


class NullValueFormatConfigurationModel(BaseModel):
    null_string: str = Field(alias="NullString")


class FilterOperationSelectedFieldsConfigurationModel(BaseModel):
    selected_fields: Optional[Sequence[str]] = Field(
        default=None, alias="SelectedFields"
    )
    selected_field_options: Optional[Literal["ALL_FIELDS"]] = Field(
        default=None, alias="SelectedFieldOptions"
    )


class LocalNavigationConfigurationModel(BaseModel):
    target_sheet_id: str = Field(alias="TargetSheetId")


class CustomActionURLOperationModel(BaseModel):
    url_template: str = Field(alias="URLTemplate")
    url_target: Literal["NEW_TAB", "NEW_WINDOW", "SAME_TAB"] = Field(alias="URLTarget")


class CustomContentConfigurationModel(BaseModel):
    content_url: Optional[str] = Field(default=None, alias="ContentUrl")
    content_type: Optional[Literal["IMAGE", "OTHER_EMBEDDED_CONTENT"]] = Field(
        default=None, alias="ContentType"
    )
    image_scaling: Optional[
        Literal["DO_NOT_SCALE", "FIT_TO_HEIGHT", "FIT_TO_WIDTH", "SCALE_TO_VISUAL"]
    ] = Field(default=None, alias="ImageScaling")


class CustomNarrativeOptionsModel(BaseModel):
    narrative: str = Field(alias="Narrative")


class CustomParameterValuesModel(BaseModel):
    string_values: Optional[Sequence[str]] = Field(default=None, alias="StringValues")
    integer_values: Optional[Sequence[int]] = Field(default=None, alias="IntegerValues")
    decimal_values: Optional[Sequence[float]] = Field(
        default=None, alias="DecimalValues"
    )
    date_time_values: Optional[Sequence[Union[datetime, str]]] = Field(
        default=None, alias="DateTimeValues"
    )


class InputColumnModel(BaseModel):
    name: str = Field(alias="Name")
    type: Literal[
        "BIT", "BOOLEAN", "DATETIME", "DECIMAL", "INTEGER", "JSON", "STRING"
    ] = Field(alias="Type")


class DataPointDrillUpDownOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class DataPointMenuLabelOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class DataPointTooltipOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class ExportToCSVOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class ExportWithHiddenFieldsOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class SheetControlsOptionModel(BaseModel):
    visibility_state: Optional[Literal["COLLAPSED", "EXPANDED"]] = Field(
        default=None, alias="VisibilityState"
    )


class SheetLayoutElementMaximizationOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class VisualAxisSortOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class VisualMenuOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class DashboardSearchFilterModel(BaseModel):
    operator: Literal["StringEquals", "StringLike"] = Field(alias="Operator")
    name: Optional[
        Literal[
            "DASHBOARD_NAME",
            "DIRECT_QUICKSIGHT_OWNER",
            "DIRECT_QUICKSIGHT_SOLE_OWNER",
            "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
            "QUICKSIGHT_OWNER",
            "QUICKSIGHT_USER",
            "QUICKSIGHT_VIEWER_OR_OWNER",
        ]
    ] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class DashboardSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    dashboard_id: Optional[str] = Field(default=None, alias="DashboardId")
    name: Optional[str] = Field(default=None, alias="Name")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    published_version_number: Optional[int] = Field(
        default=None, alias="PublishedVersionNumber"
    )
    last_published_time: Optional[datetime] = Field(
        default=None, alias="LastPublishedTime"
    )


class DashboardVersionSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")
    source_entity_arn: Optional[str] = Field(default=None, alias="SourceEntityArn")
    description: Optional[str] = Field(default=None, alias="Description")


class ExportHiddenFieldsOptionModel(BaseModel):
    availability_status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="AvailabilityStatus"
    )


class DataBarsOptionsModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    positive_color: Optional[str] = Field(default=None, alias="PositiveColor")
    negative_color: Optional[str] = Field(default=None, alias="NegativeColor")


class DataColorPaletteModel(BaseModel):
    colors: Optional[Sequence[str]] = Field(default=None, alias="Colors")
    min_max_gradient: Optional[Sequence[str]] = Field(
        default=None, alias="MinMaxGradient"
    )
    empty_fill_color: Optional[str] = Field(default=None, alias="EmptyFillColor")


class DataPathLabelTypeModel(BaseModel):
    field_id: Optional[str] = Field(default=None, alias="FieldId")
    field_value: Optional[str] = Field(default=None, alias="FieldValue")
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class FieldLabelTypeModel(BaseModel):
    field_id: Optional[str] = Field(default=None, alias="FieldId")
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class MaximumLabelTypeModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class MinimumLabelTypeModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class RangeEndsLabelTypeModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class DataPathValueModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    field_value: str = Field(alias="FieldValue")


class DataSetSearchFilterModel(BaseModel):
    operator: Literal["StringEquals", "StringLike"] = Field(alias="Operator")
    name: Literal[
        "DATASET_NAME",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "QUICKSIGHT_OWNER",
        "QUICKSIGHT_VIEWER_OR_OWNER",
    ] = Field(alias="Name")
    value: str = Field(alias="Value")


class OutputColumnModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    description: Optional[str] = Field(default=None, alias="Description")
    type: Optional[Literal["DATETIME", "DECIMAL", "INTEGER", "STRING"]] = Field(
        default=None, alias="Type"
    )


class DataSourceErrorInfoModel(BaseModel):
    type: Optional[
        Literal[
            "ACCESS_DENIED",
            "CONFLICT",
            "COPY_SOURCE_NOT_FOUND",
            "ENGINE_VERSION_NOT_SUPPORTED",
            "GENERIC_SQL_FAILURE",
            "TIMEOUT",
            "UNKNOWN",
            "UNKNOWN_HOST",
        ]
    ] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")


class DatabricksParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    sql_endpoint_path: str = Field(alias="SqlEndpointPath")


class ExasolParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")


class JiraParametersModel(BaseModel):
    site_base_url: str = Field(alias="SiteBaseUrl")


class MariaDbParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class MySqlParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class OracleParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class PostgreSqlParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class PrestoParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    catalog: str = Field(alias="Catalog")


class RdsParametersModel(BaseModel):
    instance_id: str = Field(alias="InstanceId")
    database: str = Field(alias="Database")


class RedshiftParametersModel(BaseModel):
    database: str = Field(alias="Database")
    host: Optional[str] = Field(default=None, alias="Host")
    port: Optional[int] = Field(default=None, alias="Port")
    cluster_id: Optional[str] = Field(default=None, alias="ClusterId")


class ServiceNowParametersModel(BaseModel):
    site_base_url: str = Field(alias="SiteBaseUrl")


class SnowflakeParametersModel(BaseModel):
    host: str = Field(alias="Host")
    database: str = Field(alias="Database")
    warehouse: str = Field(alias="Warehouse")


class SparkParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")


class SqlServerParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class TeradataParametersModel(BaseModel):
    host: str = Field(alias="Host")
    port: int = Field(alias="Port")
    database: str = Field(alias="Database")


class TwitterParametersModel(BaseModel):
    query: str = Field(alias="Query")
    max_rows: int = Field(alias="MaxRows")


class DataSourceSearchFilterModel(BaseModel):
    operator: Literal["StringEquals", "StringLike"] = Field(alias="Operator")
    name: Literal[
        "DATASOURCE_NAME",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    ] = Field(alias="Name")
    value: str = Field(alias="Value")


class DataSourceSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[
        Literal[
            "ADOBE_ANALYTICS",
            "AMAZON_ELASTICSEARCH",
            "AMAZON_OPENSEARCH",
            "ATHENA",
            "AURORA",
            "AURORA_POSTGRESQL",
            "AWS_IOT_ANALYTICS",
            "DATABRICKS",
            "EXASOL",
            "GITHUB",
            "JIRA",
            "MARIADB",
            "MYSQL",
            "ORACLE",
            "POSTGRESQL",
            "PRESTO",
            "REDSHIFT",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SNOWFLAKE",
            "SPARK",
            "SQLSERVER",
            "TERADATA",
            "TIMESTREAM",
            "TWITTER",
        ]
    ] = Field(default=None, alias="Type")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class RollingDateConfigurationModel(BaseModel):
    expression: str = Field(alias="Expression")
    data_set_identifier: Optional[str] = Field(default=None, alias="DataSetIdentifier")


class DateTimeValueWhenUnsetConfigurationModel(BaseModel):
    value_when_unset_option: Optional[Literal["NULL", "RECOMMENDED_VALUE"]] = Field(
        default=None, alias="ValueWhenUnsetOption"
    )
    custom_value: Optional[Union[datetime, str]] = Field(
        default=None, alias="CustomValue"
    )


class DateTimeParameterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[Union[datetime, str]] = Field(alias="Values")


class DecimalValueWhenUnsetConfigurationModel(BaseModel):
    value_when_unset_option: Optional[Literal["NULL", "RECOMMENDED_VALUE"]] = Field(
        default=None, alias="ValueWhenUnsetOption"
    )
    custom_value: Optional[float] = Field(default=None, alias="CustomValue")


class DecimalParameterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[float] = Field(alias="Values")


class DeleteAccountCustomizationRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: Optional[str] = Field(default=None, alias="Namespace")


class DeleteAccountSubscriptionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")


class DeleteAnalysisRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")
    recovery_window_in_days: Optional[int] = Field(
        default=None, alias="RecoveryWindowInDays"
    )
    force_delete_without_recovery: Optional[bool] = Field(
        default=None, alias="ForceDeleteWithoutRecovery"
    )


class DeleteDashboardRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")


class DeleteDataSetRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")


class DeleteDataSourceRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_source_id: str = Field(alias="DataSourceId")


class DeleteFolderMembershipRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")
    member_id: str = Field(alias="MemberId")
    member_type: Literal["ANALYSIS", "DASHBOARD", "DATASET"] = Field(alias="MemberType")


class DeleteFolderRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")


class DeleteGroupMembershipRequestModel(BaseModel):
    member_name: str = Field(alias="MemberName")
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DeleteGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DeleteIAMPolicyAssignmentRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    assignment_name: str = Field(alias="AssignmentName")
    namespace: str = Field(alias="Namespace")


class DeleteNamespaceRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DeleteTemplateAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    alias_name: str = Field(alias="AliasName")


class DeleteTemplateRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")


class DeleteThemeAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    alias_name: str = Field(alias="AliasName")


class DeleteThemeRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")


class DeleteUserByPrincipalIdRequestModel(BaseModel):
    principal_id: str = Field(alias="PrincipalId")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DeleteUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DescribeAccountCustomizationRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    resolved: Optional[bool] = Field(default=None, alias="Resolved")


class DescribeAccountSettingsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")


class DescribeAccountSubscriptionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")


class DescribeAnalysisDefinitionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")


class DescribeAnalysisPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")


class DescribeAnalysisRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")


class DescribeDashboardDefinitionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    alias_name: Optional[str] = Field(default=None, alias="AliasName")


class DescribeDashboardPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")


class DescribeDashboardRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    alias_name: Optional[str] = Field(default=None, alias="AliasName")


class DescribeDataSetPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")


class DescribeDataSetRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")


class DescribeDataSourcePermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_source_id: str = Field(alias="DataSourceId")


class DescribeDataSourceRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_source_id: str = Field(alias="DataSourceId")


class DescribeFolderPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")


class DescribeFolderRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")


class DescribeFolderResolvedPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")


class FolderModel(BaseModel):
    folder_id: Optional[str] = Field(default=None, alias="FolderId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    folder_type: Optional[Literal["SHARED"]] = Field(default=None, alias="FolderType")
    folder_path: Optional[List[str]] = Field(default=None, alias="FolderPath")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class DescribeGroupMembershipRequestModel(BaseModel):
    member_name: str = Field(alias="MemberName")
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DescribeGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DescribeIAMPolicyAssignmentRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    assignment_name: str = Field(alias="AssignmentName")
    namespace: str = Field(alias="Namespace")


class IAMPolicyAssignmentModel(BaseModel):
    aws_account_id: Optional[str] = Field(default=None, alias="AwsAccountId")
    assignment_id: Optional[str] = Field(default=None, alias="AssignmentId")
    assignment_name: Optional[str] = Field(default=None, alias="AssignmentName")
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")
    identities: Optional[Dict[str, List[str]]] = Field(default=None, alias="Identities")
    assignment_status: Optional[Literal["DISABLED", "DRAFT", "ENABLED"]] = Field(
        default=None, alias="AssignmentStatus"
    )


class DescribeIngestionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")
    ingestion_id: str = Field(alias="IngestionId")


class DescribeIpRestrictionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")


class DescribeNamespaceRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class DescribeTemplateAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    alias_name: str = Field(alias="AliasName")


class DescribeTemplateDefinitionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    alias_name: Optional[str] = Field(default=None, alias="AliasName")


class DescribeTemplatePermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")


class DescribeTemplateRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    alias_name: Optional[str] = Field(default=None, alias="AliasName")


class DescribeThemeAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    alias_name: str = Field(alias="AliasName")


class DescribeThemePermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")


class DescribeThemeRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    alias_name: Optional[str] = Field(default=None, alias="AliasName")


class DescribeUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")


class UserModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    email: Optional[str] = Field(default=None, alias="Email")
    role: Optional[
        Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"]
    ] = Field(default=None, alias="Role")
    identity_type: Optional[Literal["IAM", "QUICKSIGHT"]] = Field(
        default=None, alias="IdentityType"
    )
    active: Optional[bool] = Field(default=None, alias="Active")
    principal_id: Optional[str] = Field(default=None, alias="PrincipalId")
    custom_permissions_name: Optional[str] = Field(
        default=None, alias="CustomPermissionsName"
    )
    external_login_federation_provider_type: Optional[str] = Field(
        default=None, alias="ExternalLoginFederationProviderType"
    )
    external_login_federation_provider_url: Optional[str] = Field(
        default=None, alias="ExternalLoginFederationProviderUrl"
    )
    external_login_id: Optional[str] = Field(default=None, alias="ExternalLoginId")


class DonutCenterOptionsModel(BaseModel):
    label_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="LabelVisibility"
    )


class ListControlSelectAllOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class ErrorInfoModel(BaseModel):
    type: Optional[
        Literal[
            "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
            "CONNECTION_FAILURE",
            "CURSOR_NOT_ENABLED",
            "CUSTOMER_ERROR",
            "DATA_SET_DELETED",
            "DATA_SET_NOT_SPICE",
            "DATA_SET_SIZE_LIMIT_EXCEEDED",
            "DATA_SOURCE_AUTH_FAILED",
            "DATA_SOURCE_CONNECTION_FAILED",
            "DATA_SOURCE_NOT_FOUND",
            "DATA_TOLERANCE_EXCEPTION",
            "ELASTICSEARCH_CURSOR_NOT_ENABLED",
            "FAILURE_TO_ASSUME_ROLE",
            "FAILURE_TO_PROCESS_JSON_FILE",
            "IAM_ROLE_NOT_AVAILABLE",
            "INGESTION_CANCELED",
            "INGESTION_SUPERSEDED",
            "INTERNAL_SERVICE_ERROR",
            "INVALID_DATAPREP_SYNTAX",
            "INVALID_DATA_SOURCE_CONFIG",
            "INVALID_DATE_FORMAT",
            "IOT_DATA_SET_FILE_EMPTY",
            "IOT_FILE_NOT_FOUND",
            "OAUTH_TOKEN_FAILURE",
            "PASSWORD_AUTHENTICATION_FAILURE",
            "PERMISSION_DENIED",
            "PERMISSION_NOT_FOUND",
            "QUERY_TIMEOUT",
            "REFRESH_SUPPRESSED_BY_EDIT",
            "ROW_SIZE_LIMIT_EXCEEDED",
            "S3_FILE_INACCESSIBLE",
            "S3_MANIFEST_ERROR",
            "S3_UPLOADED_FILE_DELETED",
            "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
            "SOURCE_RESOURCE_LIMIT_EXCEEDED",
            "SPICE_TABLE_NOT_FOUND",
            "SQL_EXCEPTION",
            "SQL_INVALID_PARAMETER_VALUE",
            "SQL_NUMERIC_OVERFLOW",
            "SQL_SCHEMA_MISMATCH_ERROR",
            "SQL_TABLE_NOT_FOUND",
            "SSL_CERTIFICATE_VALIDATION_FAILURE",
            "UNRESOLVABLE_HOST",
            "UNROUTABLE_HOST",
        ]
    ] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")


class ExcludePeriodConfigurationModel(BaseModel):
    amount: int = Field(alias="Amount")
    granularity: Literal[
        "DAY",
        "HOUR",
        "MILLISECOND",
        "MINUTE",
        "MONTH",
        "QUARTER",
        "SECOND",
        "WEEK",
        "YEAR",
    ] = Field(alias="Granularity")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class FieldSortModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    direction: Literal["ASC", "DESC"] = Field(alias="Direction")


class FieldTooltipItemModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    label: Optional[str] = Field(default=None, alias="Label")
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class GeospatialMapStyleOptionsModel(BaseModel):
    base_map_style: Optional[
        Literal["DARK_GRAY", "IMAGERY", "LIGHT_GRAY", "STREET"]
    ] = Field(default=None, alias="BaseMapStyle")


class FilterSelectableValuesModel(BaseModel):
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")


class SameSheetTargetVisualConfigurationModel(BaseModel):
    target_visuals: Optional[Sequence[str]] = Field(default=None, alias="TargetVisuals")
    target_visual_options: Optional[Literal["ALL_VISUALS"]] = Field(
        default=None, alias="TargetVisualOptions"
    )


class FilterOperationModel(BaseModel):
    condition_expression: str = Field(alias="ConditionExpression")


class FolderSearchFilterModel(BaseModel):
    operator: Optional[Literal["StringEquals", "StringLike"]] = Field(
        default=None, alias="Operator"
    )
    name: Optional[
        Literal[
            "DIRECT_QUICKSIGHT_OWNER",
            "DIRECT_QUICKSIGHT_SOLE_OWNER",
            "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
            "FOLDER_NAME",
            "PARENT_FOLDER_ARN",
            "QUICKSIGHT_OWNER",
            "QUICKSIGHT_VIEWER_OR_OWNER",
        ]
    ] = Field(default=None, alias="Name")
    value: Optional[str] = Field(default=None, alias="Value")


class FolderSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    folder_id: Optional[str] = Field(default=None, alias="FolderId")
    name: Optional[str] = Field(default=None, alias="Name")
    folder_type: Optional[Literal["SHARED"]] = Field(default=None, alias="FolderType")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class FontSizeModel(BaseModel):
    relative: Optional[
        Literal["EXTRA_LARGE", "EXTRA_SMALL", "LARGE", "MEDIUM", "SMALL"]
    ] = Field(default=None, alias="Relative")


class FontWeightModel(BaseModel):
    name: Optional[Literal["BOLD", "NORMAL"]] = Field(default=None, alias="Name")


class FontModel(BaseModel):
    font_family: Optional[str] = Field(default=None, alias="FontFamily")


class TimeBasedForecastPropertiesModel(BaseModel):
    periods_forward: Optional[int] = Field(default=None, alias="PeriodsForward")
    periods_backward: Optional[int] = Field(default=None, alias="PeriodsBackward")
    upper_boundary: Optional[float] = Field(default=None, alias="UpperBoundary")
    lower_boundary: Optional[float] = Field(default=None, alias="LowerBoundary")
    prediction_interval: Optional[int] = Field(default=None, alias="PredictionInterval")
    seasonality: Optional[int] = Field(default=None, alias="Seasonality")


class WhatIfPointScenarioModel(BaseModel):
    date: Union[datetime, str] = Field(alias="Date")
    value: float = Field(alias="Value")


class WhatIfRangeScenarioModel(BaseModel):
    start_date: Union[datetime, str] = Field(alias="StartDate")
    end_date: Union[datetime, str] = Field(alias="EndDate")
    value: float = Field(alias="Value")


class FreeFormLayoutScreenCanvasSizeOptionsModel(BaseModel):
    optimized_view_port_width: str = Field(alias="OptimizedViewPortWidth")


class FreeFormLayoutElementBackgroundStyleModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    color: Optional[str] = Field(default=None, alias="Color")


class FreeFormLayoutElementBorderStyleModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    color: Optional[str] = Field(default=None, alias="Color")


class LoadingAnimationModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class SessionTagModel(BaseModel):
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")


class GeospatialCoordinateBoundsModel(BaseModel):
    north: float = Field(alias="North")
    south: float = Field(alias="South")
    west: float = Field(alias="West")
    east: float = Field(alias="East")


class GetDashboardEmbedUrlRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    identity_type: Literal["ANONYMOUS", "IAM", "QUICKSIGHT"] = Field(
        alias="IdentityType"
    )
    session_lifetime_in_minutes: Optional[int] = Field(
        default=None, alias="SessionLifetimeInMinutes"
    )
    undo_redo_disabled: Optional[bool] = Field(default=None, alias="UndoRedoDisabled")
    reset_disabled: Optional[bool] = Field(default=None, alias="ResetDisabled")
    state_persistence_enabled: Optional[bool] = Field(
        default=None, alias="StatePersistenceEnabled"
    )
    user_arn: Optional[str] = Field(default=None, alias="UserArn")
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    additional_dashboard_ids: Optional[Sequence[str]] = Field(
        default=None, alias="AdditionalDashboardIds"
    )


class GetSessionEmbedUrlRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    entry_point: Optional[str] = Field(default=None, alias="EntryPoint")
    session_lifetime_in_minutes: Optional[int] = Field(
        default=None, alias="SessionLifetimeInMinutes"
    )
    user_arn: Optional[str] = Field(default=None, alias="UserArn")


class TableBorderOptionsModel(BaseModel):
    color: Optional[str] = Field(default=None, alias="Color")
    thickness: Optional[int] = Field(default=None, alias="Thickness")
    style: Optional[Literal["NONE", "SOLID"]] = Field(default=None, alias="Style")


class GradientStopModel(BaseModel):
    gradient_offset: float = Field(alias="GradientOffset")
    data_value: Optional[float] = Field(default=None, alias="DataValue")
    color: Optional[str] = Field(default=None, alias="Color")


class GridLayoutScreenCanvasSizeOptionsModel(BaseModel):
    resize_option: Literal["FIXED", "RESPONSIVE"] = Field(alias="ResizeOption")
    optimized_view_port_width: Optional[str] = Field(
        default=None, alias="OptimizedViewPortWidth"
    )


class GridLayoutElementModel(BaseModel):
    element_id: str = Field(alias="ElementId")
    element_type: Literal[
        "FILTER_CONTROL", "PARAMETER_CONTROL", "TEXT_BOX", "VISUAL"
    ] = Field(alias="ElementType")
    column_span: int = Field(alias="ColumnSpan")
    row_span: int = Field(alias="RowSpan")
    column_index: Optional[int] = Field(default=None, alias="ColumnIndex")
    row_index: Optional[int] = Field(default=None, alias="RowIndex")


class GroupSearchFilterModel(BaseModel):
    operator: Literal["StartsWith"] = Field(alias="Operator")
    name: Literal["GROUP_NAME"] = Field(alias="Name")
    value: str = Field(alias="Value")


class GutterStyleModel(BaseModel):
    show: Optional[bool] = Field(default=None, alias="Show")


class IAMPolicyAssignmentSummaryModel(BaseModel):
    assignment_name: Optional[str] = Field(default=None, alias="AssignmentName")
    assignment_status: Optional[Literal["DISABLED", "DRAFT", "ENABLED"]] = Field(
        default=None, alias="AssignmentStatus"
    )


class QueueInfoModel(BaseModel):
    waiting_on_ingestion: str = Field(alias="WaitingOnIngestion")
    queued_ingestion: str = Field(alias="QueuedIngestion")


class RowInfoModel(BaseModel):
    rows_ingested: Optional[int] = Field(default=None, alias="RowsIngested")
    rows_dropped: Optional[int] = Field(default=None, alias="RowsDropped")
    total_rows_in_dataset: Optional[int] = Field(
        default=None, alias="TotalRowsInDataset"
    )


class IntegerValueWhenUnsetConfigurationModel(BaseModel):
    value_when_unset_option: Optional[Literal["NULL", "RECOMMENDED_VALUE"]] = Field(
        default=None, alias="ValueWhenUnsetOption"
    )
    custom_value: Optional[int] = Field(default=None, alias="CustomValue")


class IntegerParameterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[int] = Field(alias="Values")


class JoinKeyPropertiesModel(BaseModel):
    unique_key: Optional[bool] = Field(default=None, alias="UniqueKey")


class ProgressBarOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class SecondaryValueOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class TrendArrowOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class LineChartLineStyleSettingsModel(BaseModel):
    line_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="LineVisibility"
    )
    line_interpolation: Optional[Literal["LINEAR", "SMOOTH", "STEPPED"]] = Field(
        default=None, alias="LineInterpolation"
    )
    line_style: Optional[Literal["DASHED", "DOTTED", "SOLID"]] = Field(
        default=None, alias="LineStyle"
    )
    line_width: Optional[str] = Field(default=None, alias="LineWidth")


class LineChartMarkerStyleSettingsModel(BaseModel):
    marker_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="MarkerVisibility"
    )
    marker_shape: Optional[
        Literal["CIRCLE", "DIAMOND", "ROUNDED_SQUARE", "SQUARE", "TRIANGLE"]
    ] = Field(default=None, alias="MarkerShape")
    marker_size: Optional[str] = Field(default=None, alias="MarkerSize")
    marker_color: Optional[str] = Field(default=None, alias="MarkerColor")


class MissingDataConfigurationModel(BaseModel):
    treatment_option: Optional[
        Literal["INTERPOLATE", "SHOW_AS_BLANK", "SHOW_AS_ZERO"]
    ] = Field(default=None, alias="TreatmentOption")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ListAnalysesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListControlSearchOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class ListDashboardVersionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDashboardsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDataSetsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDataSourcesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFolderMembersRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class MemberIdArnPairModel(BaseModel):
    member_id: Optional[str] = Field(default=None, alias="MemberId")
    member_arn: Optional[str] = Field(default=None, alias="MemberArn")


class ListFoldersRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGroupMembershipsRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListGroupsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIAMPolicyAssignmentsForUserRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    user_name: str = Field(alias="UserName")
    namespace: str = Field(alias="Namespace")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIAMPolicyAssignmentsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    assignment_status: Optional[Literal["DISABLED", "DRAFT", "ENABLED"]] = Field(
        default=None, alias="AssignmentStatus"
    )
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIngestionsRequestModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListNamespacesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTagsForResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")


class ListTemplateAliasesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListTemplateVersionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class TemplateVersionSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")
    description: Optional[str] = Field(default=None, alias="Description")


class ListTemplatesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class TemplateSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")
    name: Optional[str] = Field(default=None, alias="Name")
    latest_version_number: Optional[int] = Field(
        default=None, alias="LatestVersionNumber"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class ListThemeAliasesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListThemeVersionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ThemeVersionSummaryModel(BaseModel):
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")


class ListThemesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    type: Optional[Literal["ALL", "CUSTOM", "QUICKSIGHT"]] = Field(
        default=None, alias="Type"
    )


class ThemeSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    theme_id: Optional[str] = Field(default=None, alias="ThemeId")
    latest_version_number: Optional[int] = Field(
        default=None, alias="LatestVersionNumber"
    )
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class ListUserGroupsRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListUsersRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class LongFormatTextModel(BaseModel):
    plain_text: Optional[str] = Field(default=None, alias="PlainText")
    rich_text: Optional[str] = Field(default=None, alias="RichText")


class ManifestFileLocationModel(BaseModel):
    bucket: str = Field(alias="Bucket")
    key: str = Field(alias="Key")


class MarginStyleModel(BaseModel):
    show: Optional[bool] = Field(default=None, alias="Show")


class NamespaceErrorModel(BaseModel):
    type: Optional[Literal["INTERNAL_SERVICE_ERROR", "PERMISSION_DENIED"]] = Field(
        default=None, alias="Type"
    )
    message: Optional[str] = Field(default=None, alias="Message")


class NumericRangeFilterValueModel(BaseModel):
    static_value: Optional[float] = Field(default=None, alias="StaticValue")
    parameter: Optional[str] = Field(default=None, alias="Parameter")


class ThousandSeparatorOptionsModel(BaseModel):
    symbol: Optional[Literal["COMMA", "DOT", "SPACE"]] = Field(
        default=None, alias="Symbol"
    )
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class PercentileAggregationModel(BaseModel):
    percentile_value: Optional[float] = Field(default=None, alias="PercentileValue")


class StringParameterModel(BaseModel):
    name: str = Field(alias="Name")
    values: Sequence[str] = Field(alias="Values")


class PercentVisibleRangeModel(BaseModel):
    from_: Optional[float] = Field(default=None, alias="From")
    to: Optional[float] = Field(default=None, alias="To")


class PivotTableConditionalFormattingScopeModel(BaseModel):
    role: Optional[Literal["FIELD", "FIELD_TOTAL", "GRAND_TOTAL"]] = Field(
        default=None, alias="Role"
    )


class PivotTablePaginatedReportOptionsModel(BaseModel):
    vertical_overflow_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="VerticalOverflowVisibility"
    )
    overflow_column_header_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="OverflowColumnHeaderVisibility"
    )


class PivotTableFieldOptionModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    custom_label: Optional[str] = Field(default=None, alias="CustomLabel")
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class PivotTableFieldSubtotalOptionsModel(BaseModel):
    field_id: Optional[str] = Field(default=None, alias="FieldId")


class RowAlternateColorOptionsModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )
    row_alternate_colors: Optional[Sequence[str]] = Field(
        default=None, alias="RowAlternateColors"
    )


class ProjectOperationModel(BaseModel):
    projected_columns: Sequence[str] = Field(alias="ProjectedColumns")


class RadarChartAreaStyleSettingsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class ReferenceLineCustomLabelConfigurationModel(BaseModel):
    custom_label: str = Field(alias="CustomLabel")


class ReferenceLineStaticDataConfigurationModel(BaseModel):
    value: float = Field(alias="Value")


class ReferenceLineStyleConfigurationModel(BaseModel):
    pattern: Optional[Literal["DASHED", "DOTTED", "SOLID"]] = Field(
        default=None, alias="Pattern"
    )
    color: Optional[str] = Field(default=None, alias="Color")


class RegisterUserRequestModel(BaseModel):
    identity_type: Literal["IAM", "QUICKSIGHT"] = Field(alias="IdentityType")
    email: str = Field(alias="Email")
    user_role: Literal[
        "ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"
    ] = Field(alias="UserRole")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    iam_arn: Optional[str] = Field(default=None, alias="IamArn")
    session_name: Optional[str] = Field(default=None, alias="SessionName")
    user_name: Optional[str] = Field(default=None, alias="UserName")
    custom_permissions_name: Optional[str] = Field(
        default=None, alias="CustomPermissionsName"
    )
    external_login_federation_provider_type: Optional[str] = Field(
        default=None, alias="ExternalLoginFederationProviderType"
    )
    custom_federation_provider_url: Optional[str] = Field(
        default=None, alias="CustomFederationProviderUrl"
    )
    external_login_id: Optional[str] = Field(default=None, alias="ExternalLoginId")


class RegisteredUserDashboardEmbeddingConfigurationModel(BaseModel):
    initial_dashboard_id: str = Field(alias="InitialDashboardId")


class RegisteredUserQSearchBarEmbeddingConfigurationModel(BaseModel):
    initial_topic_id: Optional[str] = Field(default=None, alias="InitialTopicId")


class RegisteredUserQuickSightConsoleEmbeddingConfigurationModel(BaseModel):
    initial_path: Optional[str] = Field(default=None, alias="InitialPath")


class RenameColumnOperationModel(BaseModel):
    column_name: str = Field(alias="ColumnName")
    new_column_name: str = Field(alias="NewColumnName")


class RestoreAnalysisRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")


class RowLevelPermissionTagRuleModel(BaseModel):
    tag_key: str = Field(alias="TagKey")
    column_name: str = Field(alias="ColumnName")
    tag_multi_value_delimiter: Optional[str] = Field(
        default=None, alias="TagMultiValueDelimiter"
    )
    match_all_value: Optional[str] = Field(default=None, alias="MatchAllValue")


class UploadSettingsModel(BaseModel):
    format: Optional[Literal["CLF", "CSV", "ELF", "JSON", "TSV", "XLSX"]] = Field(
        default=None, alias="Format"
    )
    start_from_row: Optional[int] = Field(default=None, alias="StartFromRow")
    contains_header: Optional[bool] = Field(default=None, alias="ContainsHeader")
    text_qualifier: Optional[Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"]] = Field(
        default=None, alias="TextQualifier"
    )
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")


class SectionAfterPageBreakModel(BaseModel):
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class SpacingModel(BaseModel):
    top: Optional[str] = Field(default=None, alias="Top")
    bottom: Optional[str] = Field(default=None, alias="Bottom")
    left: Optional[str] = Field(default=None, alias="Left")
    right: Optional[str] = Field(default=None, alias="Right")


class SheetVisualScopingConfigurationModel(BaseModel):
    sheet_id: str = Field(alias="SheetId")
    scope: Literal["ALL_VISUALS", "SELECTED_VISUALS"] = Field(alias="Scope")
    visual_ids: Optional[Sequence[str]] = Field(default=None, alias="VisualIds")


class SheetTextBoxModel(BaseModel):
    sheet_text_box_id: str = Field(alias="SheetTextBoxId")
    content: Optional[str] = Field(default=None, alias="Content")


class SheetElementConfigurationOverridesModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class ShortFormatTextModel(BaseModel):
    plain_text: Optional[str] = Field(default=None, alias="PlainText")
    rich_text: Optional[str] = Field(default=None, alias="RichText")


class StringValueWhenUnsetConfigurationModel(BaseModel):
    value_when_unset_option: Optional[Literal["NULL", "RECOMMENDED_VALUE"]] = Field(
        default=None, alias="ValueWhenUnsetOption"
    )
    custom_value: Optional[str] = Field(default=None, alias="CustomValue")


class TableCellImageSizingConfigurationModel(BaseModel):
    table_cell_image_scaling_configuration: Optional[
        Literal["DO_NOT_SCALE", "FIT_TO_CELL_HEIGHT", "FIT_TO_CELL_WIDTH"]
    ] = Field(default=None, alias="TableCellImageScalingConfiguration")


class TablePaginatedReportOptionsModel(BaseModel):
    vertical_overflow_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="VerticalOverflowVisibility"
    )
    overflow_column_header_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="OverflowColumnHeaderVisibility"
    )


class TableFieldCustomIconContentModel(BaseModel):
    icon: Optional[Literal["LINK"]] = Field(default=None, alias="Icon")


class TemplateSourceTemplateModel(BaseModel):
    arn: str = Field(alias="Arn")


class TextControlPlaceholderOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )


class UIColorPaletteModel(BaseModel):
    primary_foreground: Optional[str] = Field(default=None, alias="PrimaryForeground")
    primary_background: Optional[str] = Field(default=None, alias="PrimaryBackground")
    secondary_foreground: Optional[str] = Field(
        default=None, alias="SecondaryForeground"
    )
    secondary_background: Optional[str] = Field(
        default=None, alias="SecondaryBackground"
    )
    accent: Optional[str] = Field(default=None, alias="Accent")
    accent_foreground: Optional[str] = Field(default=None, alias="AccentForeground")
    danger: Optional[str] = Field(default=None, alias="Danger")
    danger_foreground: Optional[str] = Field(default=None, alias="DangerForeground")
    warning: Optional[str] = Field(default=None, alias="Warning")
    warning_foreground: Optional[str] = Field(default=None, alias="WarningForeground")
    success: Optional[str] = Field(default=None, alias="Success")
    success_foreground: Optional[str] = Field(default=None, alias="SuccessForeground")
    dimension: Optional[str] = Field(default=None, alias="Dimension")
    dimension_foreground: Optional[str] = Field(
        default=None, alias="DimensionForeground"
    )
    measure: Optional[str] = Field(default=None, alias="Measure")
    measure_foreground: Optional[str] = Field(default=None, alias="MeasureForeground")


class ThemeErrorModel(BaseModel):
    type: Optional[Literal["INTERNAL_FAILURE"]] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")


class UntagColumnOperationModel(BaseModel):
    column_name: str = Field(alias="ColumnName")
    tag_names: Sequence[
        Literal["COLUMN_DESCRIPTION", "COLUMN_GEOGRAPHIC_ROLE"]
    ] = Field(alias="TagNames")


class UntagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tag_keys: Sequence[str] = Field(alias="TagKeys")


class UpdateAccountSettingsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    default_namespace: str = Field(alias="DefaultNamespace")
    notification_email: Optional[str] = Field(default=None, alias="NotificationEmail")
    termination_protection_enabled: Optional[bool] = Field(
        default=None, alias="TerminationProtectionEnabled"
    )


class UpdateDashboardPublishedVersionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    version_number: int = Field(alias="VersionNumber")


class UpdateFolderRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")
    name: str = Field(alias="Name")


class UpdateGroupRequestModel(BaseModel):
    group_name: str = Field(alias="GroupName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    description: Optional[str] = Field(default=None, alias="Description")


class UpdateIAMPolicyAssignmentRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    assignment_name: str = Field(alias="AssignmentName")
    namespace: str = Field(alias="Namespace")
    assignment_status: Optional[Literal["DISABLED", "DRAFT", "ENABLED"]] = Field(
        default=None, alias="AssignmentStatus"
    )
    policy_arn: Optional[str] = Field(default=None, alias="PolicyArn")
    identities: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="Identities"
    )


class UpdateIpRestrictionRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    ip_restriction_rule_map: Optional[Mapping[str, str]] = Field(
        default=None, alias="IpRestrictionRuleMap"
    )
    enabled: Optional[bool] = Field(default=None, alias="Enabled")


class UpdatePublicSharingSettingsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    public_sharing_enabled: Optional[bool] = Field(
        default=None, alias="PublicSharingEnabled"
    )


class UpdateTemplateAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    alias_name: str = Field(alias="AliasName")
    template_version_number: int = Field(alias="TemplateVersionNumber")


class UpdateThemeAliasRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    alias_name: str = Field(alias="AliasName")
    theme_version_number: int = Field(alias="ThemeVersionNumber")


class UpdateUserRequestModel(BaseModel):
    user_name: str = Field(alias="UserName")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    email: str = Field(alias="Email")
    role: Literal[
        "ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"
    ] = Field(alias="Role")
    custom_permissions_name: Optional[str] = Field(
        default=None, alias="CustomPermissionsName"
    )
    unapply_custom_permissions: Optional[bool] = Field(
        default=None, alias="UnapplyCustomPermissions"
    )
    external_login_federation_provider_type: Optional[str] = Field(
        default=None, alias="ExternalLoginFederationProviderType"
    )
    custom_federation_provider_url: Optional[str] = Field(
        default=None, alias="CustomFederationProviderUrl"
    )
    external_login_id: Optional[str] = Field(default=None, alias="ExternalLoginId")


class WaterfallChartOptionsModel(BaseModel):
    total_bar_label: Optional[str] = Field(default=None, alias="TotalBarLabel")


class WordCloudOptionsModel(BaseModel):
    word_orientation: Optional[
        Literal["HORIZONTAL", "HORIZONTAL_AND_VERTICAL"]
    ] = Field(default=None, alias="WordOrientation")
    word_scaling: Optional[Literal["EMPHASIZE", "NORMAL"]] = Field(
        default=None, alias="WordScaling"
    )
    cloud_layout: Optional[Literal["FLUID", "NORMAL"]] = Field(
        default=None, alias="CloudLayout"
    )
    word_casing: Optional[Literal["EXISTING_CASE", "LOWER_CASE"]] = Field(
        default=None, alias="WordCasing"
    )
    word_padding: Optional[Literal["LARGE", "MEDIUM", "NONE", "SMALL"]] = Field(
        default=None, alias="WordPadding"
    )
    maximum_string_length: Optional[int] = Field(
        default=None, alias="MaximumStringLength"
    )


class UpdateAccountCustomizationRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    account_customization: AccountCustomizationModel = Field(
        alias="AccountCustomization"
    )
    namespace: Optional[str] = Field(default=None, alias="Namespace")


class AxisLabelReferenceOptionsModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")


class CascadingControlSourceModel(BaseModel):
    source_sheet_control_id: Optional[str] = Field(
        default=None, alias="SourceSheetControlId"
    )
    column_to_match: Optional[ColumnIdentifierModel] = Field(
        default=None, alias="ColumnToMatch"
    )


class CategoryDrillDownFilterModel(BaseModel):
    column: ColumnIdentifierModel = Field(alias="Column")
    category_values: Sequence[str] = Field(alias="CategoryValues")


class ContributionAnalysisDefaultModel(BaseModel):
    measure_field_id: str = Field(alias="MeasureFieldId")
    contributor_dimensions: Sequence[ColumnIdentifierModel] = Field(
        alias="ContributorDimensions"
    )


class DynamicDefaultValueModel(BaseModel):
    default_value_column: ColumnIdentifierModel = Field(alias="DefaultValueColumn")
    user_name_column: Optional[ColumnIdentifierModel] = Field(
        default=None, alias="UserNameColumn"
    )
    group_name_column: Optional[ColumnIdentifierModel] = Field(
        default=None, alias="GroupNameColumn"
    )


class NumericEqualityDrillDownFilterModel(BaseModel):
    column: ColumnIdentifierModel = Field(alias="Column")
    value: float = Field(alias="Value")


class ParameterSelectableValuesModel(BaseModel):
    values: Optional[Sequence[str]] = Field(default=None, alias="Values")
    link_to_data_set_column: Optional[ColumnIdentifierModel] = Field(
        default=None, alias="LinkToDataSetColumn"
    )


class TimeEqualityFilterModel(BaseModel):
    filter_id: str = Field(alias="FilterId")
    column: ColumnIdentifierModel = Field(alias="Column")
    value: Optional[Union[datetime, str]] = Field(default=None, alias="Value")
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    time_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="TimeGranularity")


class TimeRangeDrillDownFilterModel(BaseModel):
    column: ColumnIdentifierModel = Field(alias="Column")
    range_minimum: Union[datetime, str] = Field(alias="RangeMinimum")
    range_maximum: Union[datetime, str] = Field(alias="RangeMaximum")
    time_granularity: Literal[
        "DAY",
        "HOUR",
        "MILLISECOND",
        "MINUTE",
        "MONTH",
        "QUARTER",
        "SECOND",
        "WEEK",
        "YEAR",
    ] = Field(alias="TimeGranularity")


class AnalysisErrorModel(BaseModel):
    type: Optional[
        Literal[
            "ACCESS_DENIED",
            "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
            "COLUMN_REPLACEMENT_MISSING",
            "COLUMN_TYPE_MISMATCH",
            "DATA_SET_NOT_FOUND",
            "INTERNAL_FAILURE",
            "PARAMETER_NOT_FOUND",
            "PARAMETER_TYPE_INVALID",
            "PARAMETER_VALUE_INCOMPATIBLE",
            "SOURCE_NOT_FOUND",
        ]
    ] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")
    violated_entities: Optional[List[EntityModel]] = Field(
        default=None, alias="ViolatedEntities"
    )


class DashboardErrorModel(BaseModel):
    type: Optional[
        Literal[
            "ACCESS_DENIED",
            "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
            "COLUMN_REPLACEMENT_MISSING",
            "COLUMN_TYPE_MISMATCH",
            "DATA_SET_NOT_FOUND",
            "INTERNAL_FAILURE",
            "PARAMETER_NOT_FOUND",
            "PARAMETER_TYPE_INVALID",
            "PARAMETER_VALUE_INCOMPATIBLE",
            "SOURCE_NOT_FOUND",
        ]
    ] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")
    violated_entities: Optional[List[EntityModel]] = Field(
        default=None, alias="ViolatedEntities"
    )


class TemplateErrorModel(BaseModel):
    type: Optional[
        Literal[
            "ACCESS_DENIED",
            "DATA_SET_NOT_FOUND",
            "INTERNAL_FAILURE",
            "SOURCE_NOT_FOUND",
        ]
    ] = Field(default=None, alias="Type")
    message: Optional[str] = Field(default=None, alias="Message")
    violated_entities: Optional[List[EntityModel]] = Field(
        default=None, alias="ViolatedEntities"
    )


class SearchAnalysesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[AnalysisSearchFilterModel] = Field(alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class AnalysisSourceTemplateModel(BaseModel):
    data_set_references: Sequence[DataSetReferenceModel] = Field(
        alias="DataSetReferences"
    )
    arn: str = Field(alias="Arn")


class DashboardSourceTemplateModel(BaseModel):
    data_set_references: Sequence[DataSetReferenceModel] = Field(
        alias="DataSetReferences"
    )
    arn: str = Field(alias="Arn")


class TemplateSourceAnalysisModel(BaseModel):
    arn: str = Field(alias="Arn")
    data_set_references: Sequence[DataSetReferenceModel] = Field(
        alias="DataSetReferences"
    )


class AnonymousUserDashboardVisualEmbeddingConfigurationModel(BaseModel):
    initial_dashboard_visual_id: DashboardVisualIdModel = Field(
        alias="InitialDashboardVisualId"
    )


class RegisteredUserDashboardVisualEmbeddingConfigurationModel(BaseModel):
    initial_dashboard_visual_id: DashboardVisualIdModel = Field(
        alias="InitialDashboardVisualId"
    )


class ArcAxisConfigurationModel(BaseModel):
    range: Optional[ArcAxisDisplayRangeModel] = Field(default=None, alias="Range")
    reserve_range: Optional[int] = Field(default=None, alias="ReserveRange")


class AxisDisplayRangeModel(BaseModel):
    min_max: Optional[AxisDisplayMinMaxRangeModel] = Field(default=None, alias="MinMax")
    data_driven: Optional[Mapping[str, Any]] = Field(default=None, alias="DataDriven")


class AxisScaleModel(BaseModel):
    linear: Optional[AxisLinearScaleModel] = Field(default=None, alias="Linear")
    logarithmic: Optional[AxisLogarithmicScaleModel] = Field(
        default=None, alias="Logarithmic"
    )


class HistogramBinOptionsModel(BaseModel):
    selected_bin_type: Optional[Literal["BIN_COUNT", "BIN_WIDTH"]] = Field(
        default=None, alias="SelectedBinType"
    )
    bin_count: Optional[BinCountOptionsModel] = Field(default=None, alias="BinCount")
    bin_width: Optional[BinWidthOptionsModel] = Field(default=None, alias="BinWidth")
    start_value: Optional[float] = Field(default=None, alias="StartValue")


class TileStyleModel(BaseModel):
    border: Optional[BorderStyleModel] = Field(default=None, alias="Border")


class BoxPlotOptionsModel(BaseModel):
    style_options: Optional[BoxPlotStyleOptionsModel] = Field(
        default=None, alias="StyleOptions"
    )
    outlier_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="OutlierVisibility"
    )
    all_data_points_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="AllDataPointsVisibility"
    )


class CreateColumnsOperationModel(BaseModel):
    columns: Sequence[CalculatedColumnModel] = Field(alias="Columns")


class CancelIngestionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    ingestion_id: str = Field(alias="IngestionId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAccountCustomizationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    account_customization: AccountCustomizationModel = Field(
        alias="AccountCustomization"
    )
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateAnalysisResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    analysis_id: str = Field(alias="AnalysisId")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDashboardResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    version_arn: str = Field(alias="VersionArn")
    dashboard_id: str = Field(alias="DashboardId")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    data_set_id: str = Field(alias="DataSetId")
    ingestion_arn: str = Field(alias="IngestionArn")
    ingestion_id: str = Field(alias="IngestionId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateDataSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    data_source_id: str = Field(alias="DataSourceId")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFolderResponseModel(BaseModel):
    status: int = Field(alias="Status")
    arn: str = Field(alias="Arn")
    folder_id: str = Field(alias="FolderId")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIAMPolicyAssignmentResponseModel(BaseModel):
    assignment_name: str = Field(alias="AssignmentName")
    assignment_id: str = Field(alias="AssignmentId")
    assignment_status: Literal["DISABLED", "DRAFT", "ENABLED"] = Field(
        alias="AssignmentStatus"
    )
    policy_arn: str = Field(alias="PolicyArn")
    identities: Dict[str, List[str]] = Field(alias="Identities")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateIngestionResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    ingestion_id: str = Field(alias="IngestionId")
    ingestion_status: Literal[
        "CANCELLED", "COMPLETED", "FAILED", "INITIALIZED", "QUEUED", "RUNNING"
    ] = Field(alias="IngestionStatus")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateNamespaceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    name: str = Field(alias="Name")
    capacity_region: str = Field(alias="CapacityRegion")
    creation_status: Literal[
        "CREATED", "CREATING", "DELETING", "NON_RETRYABLE_FAILURE", "RETRYABLE_FAILURE"
    ] = Field(alias="CreationStatus")
    identity_store: Literal["QUICKSIGHT"] = Field(alias="IdentityStore")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTemplateResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    version_arn: str = Field(alias="VersionArn")
    template_id: str = Field(alias="TemplateId")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThemeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    version_arn: str = Field(alias="VersionArn")
    theme_id: str = Field(alias="ThemeId")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAccountCustomizationResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAccountSubscriptionResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteAnalysisResponseModel(BaseModel):
    status: int = Field(alias="Status")
    arn: str = Field(alias="Arn")
    analysis_id: str = Field(alias="AnalysisId")
    deletion_time: datetime = Field(alias="DeletionTime")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDashboardResponseModel(BaseModel):
    status: int = Field(alias="Status")
    arn: str = Field(alias="Arn")
    dashboard_id: str = Field(alias="DashboardId")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDataSetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    data_set_id: str = Field(alias="DataSetId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteDataSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    data_source_id: str = Field(alias="DataSourceId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFolderMembershipResponseModel(BaseModel):
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteFolderResponseModel(BaseModel):
    status: int = Field(alias="Status")
    arn: str = Field(alias="Arn")
    folder_id: str = Field(alias="FolderId")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGroupMembershipResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteGroupResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteIAMPolicyAssignmentResponseModel(BaseModel):
    assignment_name: str = Field(alias="AssignmentName")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteNamespaceResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTemplateAliasResponseModel(BaseModel):
    status: int = Field(alias="Status")
    template_id: str = Field(alias="TemplateId")
    alias_name: str = Field(alias="AliasName")
    arn: str = Field(alias="Arn")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteTemplateResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    arn: str = Field(alias="Arn")
    template_id: str = Field(alias="TemplateId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteThemeAliasResponseModel(BaseModel):
    alias_name: str = Field(alias="AliasName")
    arn: str = Field(alias="Arn")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    theme_id: str = Field(alias="ThemeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteThemeResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    theme_id: str = Field(alias="ThemeId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteUserByPrincipalIdResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DeleteUserResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountCustomizationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    account_customization: AccountCustomizationModel = Field(
        alias="AccountCustomization"
    )
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountSettingsResponseModel(BaseModel):
    account_settings: AccountSettingsModel = Field(alias="AccountSettings")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeAccountSubscriptionResponseModel(BaseModel):
    account_info: AccountInfoModel = Field(alias="AccountInfo")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIpRestrictionResponseModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    ip_restriction_rule_map: Dict[str, str] = Field(alias="IpRestrictionRuleMap")
    enabled: bool = Field(alias="Enabled")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateEmbedUrlForAnonymousUserResponseModel(BaseModel):
    embed_url: str = Field(alias="EmbedUrl")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    anonymous_user_arn: str = Field(alias="AnonymousUserArn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GenerateEmbedUrlForRegisteredUserResponseModel(BaseModel):
    embed_url: str = Field(alias="EmbedUrl")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetDashboardEmbedUrlResponseModel(BaseModel):
    embed_url: str = Field(alias="EmbedUrl")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetSessionEmbedUrlResponseModel(BaseModel):
    embed_url: str = Field(alias="EmbedUrl")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListAnalysesResponseModel(BaseModel):
    analysis_summary_list: List[AnalysisSummaryModel] = Field(
        alias="AnalysisSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIAMPolicyAssignmentsForUserResponseModel(BaseModel):
    active_assignments: List[ActiveIAMPolicyAssignmentModel] = Field(
        alias="ActiveAssignments"
    )
    request_id: str = Field(alias="RequestId")
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RestoreAnalysisResponseModel(BaseModel):
    status: int = Field(alias="Status")
    arn: str = Field(alias="Arn")
    analysis_id: str = Field(alias="AnalysisId")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchAnalysesResponseModel(BaseModel):
    analysis_summary_list: List[AnalysisSummaryModel] = Field(
        alias="AnalysisSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UntagResourceResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountCustomizationResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    account_customization: AccountCustomizationModel = Field(
        alias="AccountCustomization"
    )
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAccountSettingsResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAnalysisResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    analysis_id: str = Field(alias="AnalysisId")
    update_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="UpdateStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDashboardPublishedVersionResponseModel(BaseModel):
    dashboard_id: str = Field(alias="DashboardId")
    dashboard_arn: str = Field(alias="DashboardArn")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDashboardResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    version_arn: str = Field(alias="VersionArn")
    dashboard_id: str = Field(alias="DashboardId")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSetPermissionsResponseModel(BaseModel):
    data_set_arn: str = Field(alias="DataSetArn")
    data_set_id: str = Field(alias="DataSetId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSetResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    data_set_id: str = Field(alias="DataSetId")
    ingestion_arn: str = Field(alias="IngestionArn")
    ingestion_id: str = Field(alias="IngestionId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSourcePermissionsResponseModel(BaseModel):
    data_source_arn: str = Field(alias="DataSourceArn")
    data_source_id: str = Field(alias="DataSourceId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDataSourceResponseModel(BaseModel):
    arn: str = Field(alias="Arn")
    data_source_id: str = Field(alias="DataSourceId")
    update_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="UpdateStatus")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFolderResponseModel(BaseModel):
    status: int = Field(alias="Status")
    arn: str = Field(alias="Arn")
    folder_id: str = Field(alias="FolderId")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIAMPolicyAssignmentResponseModel(BaseModel):
    assignment_name: str = Field(alias="AssignmentName")
    assignment_id: str = Field(alias="AssignmentId")
    policy_arn: str = Field(alias="PolicyArn")
    identities: Dict[str, List[str]] = Field(alias="Identities")
    assignment_status: Literal["DISABLED", "DRAFT", "ENABLED"] = Field(
        alias="AssignmentStatus"
    )
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateIpRestrictionResponseModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdatePublicSharingSettingsResponseModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTemplateResponseModel(BaseModel):
    template_id: str = Field(alias="TemplateId")
    arn: str = Field(alias="Arn")
    version_arn: str = Field(alias="VersionArn")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateThemeResponseModel(BaseModel):
    theme_id: str = Field(alias="ThemeId")
    arn: str = Field(alias="Arn")
    version_arn: str = Field(alias="VersionArn")
    creation_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="CreationStatus")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CategoryFilterConfigurationModel(BaseModel):
    filter_list_configuration: Optional[FilterListConfigurationModel] = Field(
        default=None, alias="FilterListConfiguration"
    )
    custom_filter_list_configuration: Optional[
        CustomFilterListConfigurationModel
    ] = Field(default=None, alias="CustomFilterListConfiguration")
    custom_filter_configuration: Optional[CustomFilterConfigurationModel] = Field(
        default=None, alias="CustomFilterConfiguration"
    )


class ClusterMarkerModel(BaseModel):
    simple_cluster_marker: Optional[SimpleClusterMarkerModel] = Field(
        default=None, alias="SimpleClusterMarker"
    )


class ColorScaleModel(BaseModel):
    colors: Sequence[DataColorModel] = Field(alias="Colors")
    color_fill_type: Literal["DISCRETE", "GRADIENT"] = Field(alias="ColorFillType")
    null_value_color: Optional[DataColorModel] = Field(
        default=None, alias="NullValueColor"
    )


class ColumnTagModel(BaseModel):
    column_geographic_role: Optional[
        Literal[
            "CITY", "COUNTRY", "COUNTY", "LATITUDE", "LONGITUDE", "POSTCODE", "STATE"
        ]
    ] = Field(default=None, alias="ColumnGeographicRole")
    column_description: Optional[ColumnDescriptionModel] = Field(
        default=None, alias="ColumnDescription"
    )


class ColumnGroupSchemaModel(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    column_group_column_schema_list: Optional[
        Sequence[ColumnGroupColumnSchemaModel]
    ] = Field(default=None, alias="ColumnGroupColumnSchemaList")


class ColumnGroupModel(BaseModel):
    geo_spatial_column_group: Optional[GeoSpatialColumnGroupModel] = Field(
        default=None, alias="GeoSpatialColumnGroup"
    )


class DataSetSchemaModel(BaseModel):
    column_schema_list: Optional[Sequence[ColumnSchemaModel]] = Field(
        default=None, alias="ColumnSchemaList"
    )


class ConditionalFormattingCustomIconConditionModel(BaseModel):
    expression: str = Field(alias="Expression")
    icon_options: ConditionalFormattingCustomIconOptionsModel = Field(
        alias="IconOptions"
    )
    color: Optional[str] = Field(default=None, alias="Color")
    display_configuration: Optional[
        ConditionalFormattingIconDisplayConfigurationModel
    ] = Field(default=None, alias="DisplayConfiguration")


class CreateAccountCustomizationRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    account_customization: AccountCustomizationModel = Field(
        alias="AccountCustomization"
    )
    namespace: Optional[str] = Field(default=None, alias="Namespace")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class CreateNamespaceRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    identity_store: Literal["QUICKSIGHT"] = Field(alias="IdentityStore")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ListTagsForResourceResponseModel(BaseModel):
    tags: List[TagModel] = Field(alias="Tags")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TagResourceRequestModel(BaseModel):
    resource_arn: str = Field(alias="ResourceArn")
    tags: Sequence[TagModel] = Field(alias="Tags")


class CreateAccountSubscriptionResponseModel(BaseModel):
    signup_response: SignupResponseModel = Field(alias="SignupResponse")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateFolderRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")
    name: Optional[str] = Field(default=None, alias="Name")
    folder_type: Optional[Literal["SHARED"]] = Field(default=None, alias="FolderType")
    parent_folder_arn: Optional[str] = Field(default=None, alias="ParentFolderArn")
    permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class DescribeAnalysisPermissionsResponseModel(BaseModel):
    analysis_id: str = Field(alias="AnalysisId")
    analysis_arn: str = Field(alias="AnalysisArn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataSetPermissionsResponseModel(BaseModel):
    data_set_arn: str = Field(alias="DataSetArn")
    data_set_id: str = Field(alias="DataSetId")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeDataSourcePermissionsResponseModel(BaseModel):
    data_source_arn: str = Field(alias="DataSourceArn")
    data_source_id: str = Field(alias="DataSourceId")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFolderPermissionsResponseModel(BaseModel):
    status: int = Field(alias="Status")
    folder_id: str = Field(alias="FolderId")
    arn: str = Field(alias="Arn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeFolderResolvedPermissionsResponseModel(BaseModel):
    status: int = Field(alias="Status")
    folder_id: str = Field(alias="FolderId")
    arn: str = Field(alias="Arn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTemplatePermissionsResponseModel(BaseModel):
    template_id: str = Field(alias="TemplateId")
    template_arn: str = Field(alias="TemplateArn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeThemePermissionsResponseModel(BaseModel):
    theme_id: str = Field(alias="ThemeId")
    theme_arn: str = Field(alias="ThemeArn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LinkSharingConfigurationModel(BaseModel):
    permissions: Optional[List[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )


class UpdateAnalysisPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")
    grant_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantPermissions"
    )
    revoke_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokePermissions"
    )


class UpdateAnalysisPermissionsResponseModel(BaseModel):
    analysis_arn: str = Field(alias="AnalysisArn")
    analysis_id: str = Field(alias="AnalysisId")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDashboardPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    grant_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantPermissions"
    )
    revoke_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokePermissions"
    )
    grant_link_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantLinkPermissions"
    )
    revoke_link_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokeLinkPermissions"
    )


class UpdateDataSetPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")
    grant_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantPermissions"
    )
    revoke_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokePermissions"
    )


class UpdateDataSourcePermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_source_id: str = Field(alias="DataSourceId")
    grant_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantPermissions"
    )
    revoke_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokePermissions"
    )


class UpdateFolderPermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    folder_id: str = Field(alias="FolderId")
    grant_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantPermissions"
    )
    revoke_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokePermissions"
    )


class UpdateFolderPermissionsResponseModel(BaseModel):
    status: int = Field(alias="Status")
    arn: str = Field(alias="Arn")
    folder_id: str = Field(alias="FolderId")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTemplatePermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    grant_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantPermissions"
    )
    revoke_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokePermissions"
    )


class UpdateTemplatePermissionsResponseModel(BaseModel):
    template_id: str = Field(alias="TemplateId")
    template_arn: str = Field(alias="TemplateArn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateThemePermissionsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    grant_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="GrantPermissions"
    )
    revoke_permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="RevokePermissions"
    )


class UpdateThemePermissionsResponseModel(BaseModel):
    theme_id: str = Field(alias="ThemeId")
    theme_arn: str = Field(alias="ThemeArn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DataSetSummaryModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    data_set_id: Optional[str] = Field(default=None, alias="DataSetId")
    name: Optional[str] = Field(default=None, alias="Name")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    import_mode: Optional[Literal["DIRECT_QUERY", "SPICE"]] = Field(
        default=None, alias="ImportMode"
    )
    row_level_permission_data_set: Optional[RowLevelPermissionDataSetModel] = Field(
        default=None, alias="RowLevelPermissionDataSet"
    )
    row_level_permission_tag_configuration_applied: Optional[bool] = Field(
        default=None, alias="RowLevelPermissionTagConfigurationApplied"
    )
    column_level_permission_rules_applied: Optional[bool] = Field(
        default=None, alias="ColumnLevelPermissionRulesApplied"
    )


class CreateFolderMembershipResponseModel(BaseModel):
    status: int = Field(alias="Status")
    folder_member: FolderMemberModel = Field(alias="FolderMember")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupMembershipResponseModel(BaseModel):
    group_member: GroupMemberModel = Field(alias="GroupMember")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGroupMembershipResponseModel(BaseModel):
    group_member: GroupMemberModel = Field(alias="GroupMember")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupMembershipsResponseModel(BaseModel):
    group_member_list: List[GroupMemberModel] = Field(alias="GroupMemberList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateGroupResponseModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeGroupResponseModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListGroupsResponseModel(BaseModel):
    group_list: List[GroupModel] = Field(alias="GroupList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUserGroupsResponseModel(BaseModel):
    group_list: List[GroupModel] = Field(alias="GroupList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchGroupsResponseModel(BaseModel):
    group_list: List[GroupModel] = Field(alias="GroupList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateGroupResponseModel(BaseModel):
    group: GroupModel = Field(alias="Group")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateTemplateAliasResponseModel(BaseModel):
    template_alias: TemplateAliasModel = Field(alias="TemplateAlias")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeTemplateAliasResponseModel(BaseModel):
    template_alias: TemplateAliasModel = Field(alias="TemplateAlias")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTemplateAliasesResponseModel(BaseModel):
    template_alias_list: List[TemplateAliasModel] = Field(alias="TemplateAliasList")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTemplateAliasResponseModel(BaseModel):
    template_alias: TemplateAliasModel = Field(alias="TemplateAlias")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThemeAliasResponseModel(BaseModel):
    theme_alias: ThemeAliasModel = Field(alias="ThemeAlias")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeThemeAliasResponseModel(BaseModel):
    theme_alias: ThemeAliasModel = Field(alias="ThemeAlias")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThemeAliasesResponseModel(BaseModel):
    theme_alias_list: List[ThemeAliasModel] = Field(alias="ThemeAliasList")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateThemeAliasResponseModel(BaseModel):
    theme_alias: ThemeAliasModel = Field(alias="ThemeAlias")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CustomActionNavigationOperationModel(BaseModel):
    local_navigation_configuration: Optional[LocalNavigationConfigurationModel] = Field(
        default=None, alias="LocalNavigationConfiguration"
    )


class CustomValuesConfigurationModel(BaseModel):
    custom_values: CustomParameterValuesModel = Field(alias="CustomValues")
    include_null_value: Optional[bool] = Field(default=None, alias="IncludeNullValue")


class CustomSqlModel(BaseModel):
    data_source_arn: str = Field(alias="DataSourceArn")
    name: str = Field(alias="Name")
    sql_query: str = Field(alias="SqlQuery")
    columns: Optional[Sequence[InputColumnModel]] = Field(default=None, alias="Columns")


class RelationalTableModel(BaseModel):
    data_source_arn: str = Field(alias="DataSourceArn")
    name: str = Field(alias="Name")
    input_columns: Sequence[InputColumnModel] = Field(alias="InputColumns")
    catalog: Optional[str] = Field(default=None, alias="Catalog")
    schema_: Optional[str] = Field(default=None, alias="Schema")


class SearchDashboardsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[DashboardSearchFilterModel] = Field(alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListDashboardsResponseModel(BaseModel):
    dashboard_summary_list: List[DashboardSummaryModel] = Field(
        alias="DashboardSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchDashboardsResponseModel(BaseModel):
    dashboard_summary_list: List[DashboardSummaryModel] = Field(
        alias="DashboardSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDashboardVersionsResponseModel(BaseModel):
    dashboard_version_summary_list: List[DashboardVersionSummaryModel] = Field(
        alias="DashboardVersionSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DashboardVisualPublishOptionsModel(BaseModel):
    export_hidden_fields_option: Optional[ExportHiddenFieldsOptionModel] = Field(
        default=None, alias="ExportHiddenFieldsOption"
    )


class TableInlineVisualizationModel(BaseModel):
    data_bars: Optional[DataBarsOptionsModel] = Field(default=None, alias="DataBars")


class DataLabelTypeModel(BaseModel):
    field_label_type: Optional[FieldLabelTypeModel] = Field(
        default=None, alias="FieldLabelType"
    )
    data_path_label_type: Optional[DataPathLabelTypeModel] = Field(
        default=None, alias="DataPathLabelType"
    )
    range_ends_label_type: Optional[RangeEndsLabelTypeModel] = Field(
        default=None, alias="RangeEndsLabelType"
    )
    minimum_label_type: Optional[MinimumLabelTypeModel] = Field(
        default=None, alias="MinimumLabelType"
    )
    maximum_label_type: Optional[MaximumLabelTypeModel] = Field(
        default=None, alias="MaximumLabelType"
    )


class DataPathColorModel(BaseModel):
    element: DataPathValueModel = Field(alias="Element")
    color: str = Field(alias="Color")
    time_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="TimeGranularity")


class DataPathSortModel(BaseModel):
    direction: Literal["ASC", "DESC"] = Field(alias="Direction")
    sort_paths: Sequence[DataPathValueModel] = Field(alias="SortPaths")


class PivotTableDataPathOptionModel(BaseModel):
    data_path_list: Sequence[DataPathValueModel] = Field(alias="DataPathList")
    width: Optional[str] = Field(default=None, alias="Width")


class SearchDataSetsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[DataSetSearchFilterModel] = Field(alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchDataSourcesRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[DataSourceSearchFilterModel] = Field(alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class SearchDataSourcesResponseModel(BaseModel):
    data_source_summaries: List[DataSourceSummaryModel] = Field(
        alias="DataSourceSummaries"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class TimeRangeFilterValueModel(BaseModel):
    static_value: Optional[Union[datetime, str]] = Field(
        default=None, alias="StaticValue"
    )
    rolling_date: Optional[RollingDateConfigurationModel] = Field(
        default=None, alias="RollingDate"
    )
    parameter: Optional[str] = Field(default=None, alias="Parameter")


class DescribeFolderResponseModel(BaseModel):
    status: int = Field(alias="Status")
    folder: FolderModel = Field(alias="Folder")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeIAMPolicyAssignmentResponseModel(BaseModel):
    iampolicy_assignment: IAMPolicyAssignmentModel = Field(alias="IAMPolicyAssignment")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListUsersResponseModel(BaseModel):
    user_list: List[UserModel] = Field(alias="UserList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RegisterUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    user_invitation_url: str = Field(alias="UserInvitationUrl")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateUserResponseModel(BaseModel):
    user: UserModel = Field(alias="User")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DonutOptionsModel(BaseModel):
    arc_options: Optional[ArcOptionsModel] = Field(default=None, alias="ArcOptions")
    donut_center_options: Optional[DonutCenterOptionsModel] = Field(
        default=None, alias="DonutCenterOptions"
    )


class RelativeDatesFilterModel(BaseModel):
    filter_id: str = Field(alias="FilterId")
    column: ColumnIdentifierModel = Field(alias="Column")
    anchor_date_configuration: AnchorDateConfigurationModel = Field(
        alias="AnchorDateConfiguration"
    )
    time_granularity: Literal[
        "DAY",
        "HOUR",
        "MILLISECOND",
        "MINUTE",
        "MONTH",
        "QUARTER",
        "SECOND",
        "WEEK",
        "YEAR",
    ] = Field(alias="TimeGranularity")
    relative_date_type: Literal["LAST", "NEXT", "NOW", "PREVIOUS", "THIS"] = Field(
        alias="RelativeDateType"
    )
    null_option: Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"] = Field(
        alias="NullOption"
    )
    minimum_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="MinimumGranularity")
    relative_date_value: Optional[int] = Field(default=None, alias="RelativeDateValue")
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")
    exclude_period_configuration: Optional[ExcludePeriodConfigurationModel] = Field(
        default=None, alias="ExcludePeriodConfiguration"
    )


class FilterOperationTargetVisualsConfigurationModel(BaseModel):
    same_sheet_target_visual_configuration: Optional[
        SameSheetTargetVisualConfigurationModel
    ] = Field(default=None, alias="SameSheetTargetVisualConfiguration")


class SearchFoldersRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[FolderSearchFilterModel] = Field(alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListFoldersResponseModel(BaseModel):
    status: int = Field(alias="Status")
    folder_summary_list: List[FolderSummaryModel] = Field(alias="FolderSummaryList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchFoldersResponseModel(BaseModel):
    status: int = Field(alias="Status")
    folder_summary_list: List[FolderSummaryModel] = Field(alias="FolderSummaryList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FontConfigurationModel(BaseModel):
    font_size: Optional[FontSizeModel] = Field(default=None, alias="FontSize")
    font_decoration: Optional[Literal["NONE", "UNDERLINE"]] = Field(
        default=None, alias="FontDecoration"
    )
    font_color: Optional[str] = Field(default=None, alias="FontColor")
    font_weight: Optional[FontWeightModel] = Field(default=None, alias="FontWeight")
    font_style: Optional[Literal["ITALIC", "NORMAL"]] = Field(
        default=None, alias="FontStyle"
    )


class TypographyModel(BaseModel):
    font_families: Optional[Sequence[FontModel]] = Field(
        default=None, alias="FontFamilies"
    )


class ForecastScenarioModel(BaseModel):
    what_if_point_scenario: Optional[WhatIfPointScenarioModel] = Field(
        default=None, alias="WhatIfPointScenario"
    )
    what_if_range_scenario: Optional[WhatIfRangeScenarioModel] = Field(
        default=None, alias="WhatIfRangeScenario"
    )


class FreeFormLayoutCanvasSizeOptionsModel(BaseModel):
    screen_canvas_size_options: Optional[
        FreeFormLayoutScreenCanvasSizeOptionsModel
    ] = Field(default=None, alias="ScreenCanvasSizeOptions")


class GeospatialWindowOptionsModel(BaseModel):
    bounds: Optional[GeospatialCoordinateBoundsModel] = Field(
        default=None, alias="Bounds"
    )
    map_zoom_mode: Optional[Literal["AUTO", "MANUAL"]] = Field(
        default=None, alias="MapZoomMode"
    )


class TableSideBorderOptionsModel(BaseModel):
    inner_vertical: Optional[TableBorderOptionsModel] = Field(
        default=None, alias="InnerVertical"
    )
    inner_horizontal: Optional[TableBorderOptionsModel] = Field(
        default=None, alias="InnerHorizontal"
    )
    left: Optional[TableBorderOptionsModel] = Field(default=None, alias="Left")
    right: Optional[TableBorderOptionsModel] = Field(default=None, alias="Right")
    top: Optional[TableBorderOptionsModel] = Field(default=None, alias="Top")
    bottom: Optional[TableBorderOptionsModel] = Field(default=None, alias="Bottom")


class GradientColorModel(BaseModel):
    stops: Optional[Sequence[GradientStopModel]] = Field(default=None, alias="Stops")


class GridLayoutCanvasSizeOptionsModel(BaseModel):
    screen_canvas_size_options: Optional[
        GridLayoutScreenCanvasSizeOptionsModel
    ] = Field(default=None, alias="ScreenCanvasSizeOptions")


class SearchGroupsRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    filters: Sequence[GroupSearchFilterModel] = Field(alias="Filters")
    next_token: Optional[str] = Field(default=None, alias="NextToken")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")


class ListIAMPolicyAssignmentsResponseModel(BaseModel):
    iampolicy_assignments: List[IAMPolicyAssignmentSummaryModel] = Field(
        alias="IAMPolicyAssignments"
    )
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class IngestionModel(BaseModel):
    arn: str = Field(alias="Arn")
    ingestion_status: Literal[
        "CANCELLED", "COMPLETED", "FAILED", "INITIALIZED", "QUEUED", "RUNNING"
    ] = Field(alias="IngestionStatus")
    created_time: datetime = Field(alias="CreatedTime")
    ingestion_id: Optional[str] = Field(default=None, alias="IngestionId")
    error_info: Optional[ErrorInfoModel] = Field(default=None, alias="ErrorInfo")
    row_info: Optional[RowInfoModel] = Field(default=None, alias="RowInfo")
    queue_info: Optional[QueueInfoModel] = Field(default=None, alias="QueueInfo")
    ingestion_time_in_seconds: Optional[int] = Field(
        default=None, alias="IngestionTimeInSeconds"
    )
    ingestion_size_in_bytes: Optional[int] = Field(
        default=None, alias="IngestionSizeInBytes"
    )
    request_source: Optional[Literal["MANUAL", "SCHEDULED"]] = Field(
        default=None, alias="RequestSource"
    )
    request_type: Optional[
        Literal["EDIT", "FULL_REFRESH", "INCREMENTAL_REFRESH", "INITIAL_INGESTION"]
    ] = Field(default=None, alias="RequestType")


class JoinInstructionModel(BaseModel):
    left_operand: str = Field(alias="LeftOperand")
    right_operand: str = Field(alias="RightOperand")
    type: Literal["INNER", "LEFT", "OUTER", "RIGHT"] = Field(alias="Type")
    on_clause: str = Field(alias="OnClause")
    left_join_key_properties: Optional[JoinKeyPropertiesModel] = Field(
        default=None, alias="LeftJoinKeyProperties"
    )
    right_join_key_properties: Optional[JoinKeyPropertiesModel] = Field(
        default=None, alias="RightJoinKeyProperties"
    )


class LineChartDefaultSeriesSettingsModel(BaseModel):
    axis_binding: Optional[Literal["PRIMARY_YAXIS", "SECONDARY_YAXIS"]] = Field(
        default=None, alias="AxisBinding"
    )
    line_style_settings: Optional[LineChartLineStyleSettingsModel] = Field(
        default=None, alias="LineStyleSettings"
    )
    marker_style_settings: Optional[LineChartMarkerStyleSettingsModel] = Field(
        default=None, alias="MarkerStyleSettings"
    )


class LineChartSeriesSettingsModel(BaseModel):
    line_style_settings: Optional[LineChartLineStyleSettingsModel] = Field(
        default=None, alias="LineStyleSettings"
    )
    marker_style_settings: Optional[LineChartMarkerStyleSettingsModel] = Field(
        default=None, alias="MarkerStyleSettings"
    )


class ListAnalysesRequestListAnalysesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDashboardVersionsRequestListDashboardVersionsPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDashboardsRequestListDashboardsPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataSetsRequestListDataSetsPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListDataSourcesRequestListDataSourcesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListIngestionsRequestListIngestionsPaginateModel(BaseModel):
    data_set_id: str = Field(alias="DataSetId")
    aws_account_id: str = Field(alias="AwsAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListNamespacesRequestListNamespacesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplateAliasesRequestListTemplateAliasesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplateVersionsRequestListTemplateVersionsPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListTemplatesRequestListTemplatesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThemeVersionsRequestListThemeVersionsPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThemesRequestListThemesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    type: Optional[Literal["ALL", "CUSTOM", "QUICKSIGHT"]] = Field(
        default=None, alias="Type"
    )
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchAnalysesRequestSearchAnalysesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[AnalysisSearchFilterModel] = Field(alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchDashboardsRequestSearchDashboardsPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[DashboardSearchFilterModel] = Field(alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchDataSetsRequestSearchDataSetsPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[DataSetSearchFilterModel] = Field(alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class SearchDataSourcesRequestSearchDataSourcesPaginateModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    filters: Sequence[DataSourceSearchFilterModel] = Field(alias="Filters")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFolderMembersResponseModel(BaseModel):
    status: int = Field(alias="Status")
    folder_member_list: List[MemberIdArnPairModel] = Field(alias="FolderMemberList")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTemplateVersionsResponseModel(BaseModel):
    template_version_summary_list: List[TemplateVersionSummaryModel] = Field(
        alias="TemplateVersionSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListTemplatesResponseModel(BaseModel):
    template_summary_list: List[TemplateSummaryModel] = Field(
        alias="TemplateSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThemeVersionsResponseModel(BaseModel):
    theme_version_summary_list: List[ThemeVersionSummaryModel] = Field(
        alias="ThemeVersionSummaryList"
    )
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListThemesResponseModel(BaseModel):
    theme_summary_list: List[ThemeSummaryModel] = Field(alias="ThemeSummaryList")
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VisualSubtitleLabelOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    format_text: Optional[LongFormatTextModel] = Field(default=None, alias="FormatText")


class S3ParametersModel(BaseModel):
    manifest_file_location: ManifestFileLocationModel = Field(
        alias="ManifestFileLocation"
    )
    role_arn: Optional[str] = Field(default=None, alias="RoleArn")


class TileLayoutStyleModel(BaseModel):
    gutter: Optional[GutterStyleModel] = Field(default=None, alias="Gutter")
    margin: Optional[MarginStyleModel] = Field(default=None, alias="Margin")


class NamespaceInfoV2Model(BaseModel):
    name: Optional[str] = Field(default=None, alias="Name")
    arn: Optional[str] = Field(default=None, alias="Arn")
    capacity_region: Optional[str] = Field(default=None, alias="CapacityRegion")
    creation_status: Optional[
        Literal[
            "CREATED",
            "CREATING",
            "DELETING",
            "NON_RETRYABLE_FAILURE",
            "RETRYABLE_FAILURE",
        ]
    ] = Field(default=None, alias="CreationStatus")
    identity_store: Optional[Literal["QUICKSIGHT"]] = Field(
        default=None, alias="IdentityStore"
    )
    namespace_error: Optional[NamespaceErrorModel] = Field(
        default=None, alias="NamespaceError"
    )


class NumericSeparatorConfigurationModel(BaseModel):
    decimal_separator: Optional[Literal["COMMA", "DOT", "SPACE"]] = Field(
        default=None, alias="DecimalSeparator"
    )
    thousands_separator: Optional[ThousandSeparatorOptionsModel] = Field(
        default=None, alias="ThousandsSeparator"
    )


class NumericalAggregationFunctionModel(BaseModel):
    simple_numerical_aggregation: Optional[
        Literal[
            "AVERAGE",
            "COUNT",
            "DISTINCT_COUNT",
            "MAX",
            "MEDIAN",
            "MIN",
            "STDEV",
            "STDEVP",
            "SUM",
            "VAR",
            "VARP",
        ]
    ] = Field(default=None, alias="SimpleNumericalAggregation")
    percentile_aggregation: Optional[PercentileAggregationModel] = Field(
        default=None, alias="PercentileAggregation"
    )


class ParametersModel(BaseModel):
    string_parameters: Optional[Sequence[StringParameterModel]] = Field(
        default=None, alias="StringParameters"
    )
    integer_parameters: Optional[Sequence[IntegerParameterModel]] = Field(
        default=None, alias="IntegerParameters"
    )
    decimal_parameters: Optional[Sequence[DecimalParameterModel]] = Field(
        default=None, alias="DecimalParameters"
    )
    date_time_parameters: Optional[Sequence[DateTimeParameterModel]] = Field(
        default=None, alias="DateTimeParameters"
    )


class VisibleRangeOptionsModel(BaseModel):
    percent_range: Optional[PercentVisibleRangeModel] = Field(
        default=None, alias="PercentRange"
    )


class RadarChartSeriesSettingsModel(BaseModel):
    area_style_settings: Optional[RadarChartAreaStyleSettingsModel] = Field(
        default=None, alias="AreaStyleSettings"
    )


class RowLevelPermissionTagConfigurationModel(BaseModel):
    tag_rules: Sequence[RowLevelPermissionTagRuleModel] = Field(alias="TagRules")
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class S3SourceModel(BaseModel):
    data_source_arn: str = Field(alias="DataSourceArn")
    input_columns: Sequence[InputColumnModel] = Field(alias="InputColumns")
    upload_settings: Optional[UploadSettingsModel] = Field(
        default=None, alias="UploadSettings"
    )


class SectionPageBreakConfigurationModel(BaseModel):
    after: Optional[SectionAfterPageBreakModel] = Field(default=None, alias="After")


class SectionBasedLayoutPaperCanvasSizeOptionsModel(BaseModel):
    paper_size: Optional[
        Literal[
            "A0",
            "A1",
            "A2",
            "A3",
            "A4",
            "A5",
            "JIS_B4",
            "JIS_B5",
            "US_LEGAL",
            "US_LETTER",
            "US_TABLOID_LEDGER",
        ]
    ] = Field(default=None, alias="PaperSize")
    paper_orientation: Optional[Literal["LANDSCAPE", "PORTRAIT"]] = Field(
        default=None, alias="PaperOrientation"
    )
    paper_margin: Optional[SpacingModel] = Field(default=None, alias="PaperMargin")


class SectionStyleModel(BaseModel):
    height: Optional[str] = Field(default=None, alias="Height")
    padding: Optional[SpacingModel] = Field(default=None, alias="Padding")


class SelectedSheetsFilterScopeConfigurationModel(BaseModel):
    sheet_visual_scoping_configurations: Optional[
        Sequence[SheetVisualScopingConfigurationModel]
    ] = Field(default=None, alias="SheetVisualScopingConfigurations")


class SheetElementRenderingRuleModel(BaseModel):
    expression: str = Field(alias="Expression")
    configuration_overrides: SheetElementConfigurationOverridesModel = Field(
        alias="ConfigurationOverrides"
    )


class VisualTitleLabelOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    format_text: Optional[ShortFormatTextModel] = Field(
        default=None, alias="FormatText"
    )


class TableFieldImageConfigurationModel(BaseModel):
    sizing_options: Optional[TableCellImageSizingConfigurationModel] = Field(
        default=None, alias="SizingOptions"
    )


class CascadingControlConfigurationModel(BaseModel):
    source_controls: Optional[Sequence[CascadingControlSourceModel]] = Field(
        default=None, alias="SourceControls"
    )


class DateTimeDefaultValuesModel(BaseModel):
    dynamic_value: Optional[DynamicDefaultValueModel] = Field(
        default=None, alias="DynamicValue"
    )
    static_values: Optional[Sequence[Union[datetime, str]]] = Field(
        default=None, alias="StaticValues"
    )
    rolling_date: Optional[RollingDateConfigurationModel] = Field(
        default=None, alias="RollingDate"
    )


class DecimalDefaultValuesModel(BaseModel):
    dynamic_value: Optional[DynamicDefaultValueModel] = Field(
        default=None, alias="DynamicValue"
    )
    static_values: Optional[Sequence[float]] = Field(default=None, alias="StaticValues")


class IntegerDefaultValuesModel(BaseModel):
    dynamic_value: Optional[DynamicDefaultValueModel] = Field(
        default=None, alias="DynamicValue"
    )
    static_values: Optional[Sequence[int]] = Field(default=None, alias="StaticValues")


class StringDefaultValuesModel(BaseModel):
    dynamic_value: Optional[DynamicDefaultValueModel] = Field(
        default=None, alias="DynamicValue"
    )
    static_values: Optional[Sequence[str]] = Field(default=None, alias="StaticValues")


class DrillDownFilterModel(BaseModel):
    numeric_equality_filter: Optional[NumericEqualityDrillDownFilterModel] = Field(
        default=None, alias="NumericEqualityFilter"
    )
    category_filter: Optional[CategoryDrillDownFilterModel] = Field(
        default=None, alias="CategoryFilter"
    )
    time_range_filter: Optional[TimeRangeDrillDownFilterModel] = Field(
        default=None, alias="TimeRangeFilter"
    )


class AnalysisModel(BaseModel):
    analysis_id: Optional[str] = Field(default=None, alias="AnalysisId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")
    errors: Optional[List[AnalysisErrorModel]] = Field(default=None, alias="Errors")
    data_set_arns: Optional[List[str]] = Field(default=None, alias="DataSetArns")
    theme_arn: Optional[str] = Field(default=None, alias="ThemeArn")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    sheets: Optional[List[SheetModel]] = Field(default=None, alias="Sheets")


class DashboardVersionModel(BaseModel):
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    errors: Optional[List[DashboardErrorModel]] = Field(default=None, alias="Errors")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")
    arn: Optional[str] = Field(default=None, alias="Arn")
    source_entity_arn: Optional[str] = Field(default=None, alias="SourceEntityArn")
    data_set_arns: Optional[List[str]] = Field(default=None, alias="DataSetArns")
    description: Optional[str] = Field(default=None, alias="Description")
    theme_arn: Optional[str] = Field(default=None, alias="ThemeArn")
    sheets: Optional[List[SheetModel]] = Field(default=None, alias="Sheets")


class AnalysisSourceEntityModel(BaseModel):
    source_template: Optional[AnalysisSourceTemplateModel] = Field(
        default=None, alias="SourceTemplate"
    )


class DashboardSourceEntityModel(BaseModel):
    source_template: Optional[DashboardSourceTemplateModel] = Field(
        default=None, alias="SourceTemplate"
    )


class TemplateSourceEntityModel(BaseModel):
    source_analysis: Optional[TemplateSourceAnalysisModel] = Field(
        default=None, alias="SourceAnalysis"
    )
    source_template: Optional[TemplateSourceTemplateModel] = Field(
        default=None, alias="SourceTemplate"
    )


class AnonymousUserEmbeddingExperienceConfigurationModel(BaseModel):
    dashboard: Optional[AnonymousUserDashboardEmbeddingConfigurationModel] = Field(
        default=None, alias="Dashboard"
    )
    dashboard_visual: Optional[
        AnonymousUserDashboardVisualEmbeddingConfigurationModel
    ] = Field(default=None, alias="DashboardVisual")
    qsearch_bar: Optional[AnonymousUserQSearchBarEmbeddingConfigurationModel] = Field(
        default=None, alias="QSearchBar"
    )


class RegisteredUserEmbeddingExperienceConfigurationModel(BaseModel):
    dashboard: Optional[RegisteredUserDashboardEmbeddingConfigurationModel] = Field(
        default=None, alias="Dashboard"
    )
    quick_sight_console: Optional[
        RegisteredUserQuickSightConsoleEmbeddingConfigurationModel
    ] = Field(default=None, alias="QuickSightConsole")
    qsearch_bar: Optional[RegisteredUserQSearchBarEmbeddingConfigurationModel] = Field(
        default=None, alias="QSearchBar"
    )
    dashboard_visual: Optional[
        RegisteredUserDashboardVisualEmbeddingConfigurationModel
    ] = Field(default=None, alias="DashboardVisual")


class NumericAxisOptionsModel(BaseModel):
    scale: Optional[AxisScaleModel] = Field(default=None, alias="Scale")
    range: Optional[AxisDisplayRangeModel] = Field(default=None, alias="Range")


class CategoryFilterModel(BaseModel):
    filter_id: str = Field(alias="FilterId")
    column: ColumnIdentifierModel = Field(alias="Column")
    configuration: CategoryFilterConfigurationModel = Field(alias="Configuration")


class ClusterMarkerConfigurationModel(BaseModel):
    cluster_marker: Optional[ClusterMarkerModel] = Field(
        default=None, alias="ClusterMarker"
    )


class TagColumnOperationModel(BaseModel):
    column_name: str = Field(alias="ColumnName")
    tags: Sequence[ColumnTagModel] = Field(alias="Tags")


class DataSetConfigurationModel(BaseModel):
    placeholder: Optional[str] = Field(default=None, alias="Placeholder")
    data_set_schema: Optional[DataSetSchemaModel] = Field(
        default=None, alias="DataSetSchema"
    )
    column_group_schema_list: Optional[Sequence[ColumnGroupSchemaModel]] = Field(
        default=None, alias="ColumnGroupSchemaList"
    )


class ConditionalFormattingIconModel(BaseModel):
    icon_set: Optional[ConditionalFormattingIconSetModel] = Field(
        default=None, alias="IconSet"
    )
    custom_condition: Optional[ConditionalFormattingCustomIconConditionModel] = Field(
        default=None, alias="CustomCondition"
    )


class DescribeDashboardPermissionsResponseModel(BaseModel):
    dashboard_id: str = Field(alias="DashboardId")
    dashboard_arn: str = Field(alias="DashboardArn")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    link_sharing_configuration: LinkSharingConfigurationModel = Field(
        alias="LinkSharingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDashboardPermissionsResponseModel(BaseModel):
    dashboard_arn: str = Field(alias="DashboardArn")
    dashboard_id: str = Field(alias="DashboardId")
    permissions: List[ResourcePermissionModel] = Field(alias="Permissions")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    link_sharing_configuration: LinkSharingConfigurationModel = Field(
        alias="LinkSharingConfiguration"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataSetsResponseModel(BaseModel):
    data_set_summaries: List[DataSetSummaryModel] = Field(alias="DataSetSummaries")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class SearchDataSetsResponseModel(BaseModel):
    data_set_summaries: List[DataSetSummaryModel] = Field(alias="DataSetSummaries")
    next_token: str = Field(alias="NextToken")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DestinationParameterValueConfigurationModel(BaseModel):
    custom_values_configuration: Optional[CustomValuesConfigurationModel] = Field(
        default=None, alias="CustomValuesConfiguration"
    )
    select_all_value_options: Optional[Literal["ALL_VALUES"]] = Field(
        default=None, alias="SelectAllValueOptions"
    )
    source_parameter_name: Optional[str] = Field(
        default=None, alias="SourceParameterName"
    )
    source_field: Optional[str] = Field(default=None, alias="SourceField")


class DashboardPublishOptionsModel(BaseModel):
    ad_hoc_filtering_option: Optional[AdHocFilteringOptionModel] = Field(
        default=None, alias="AdHocFilteringOption"
    )
    export_to_cs_voption: Optional[ExportToCSVOptionModel] = Field(
        default=None, alias="ExportToCSVOption"
    )
    sheet_controls_option: Optional[SheetControlsOptionModel] = Field(
        default=None, alias="SheetControlsOption"
    )
    visual_publish_options: Optional[DashboardVisualPublishOptionsModel] = Field(
        default=None, alias="VisualPublishOptions"
    )
    sheet_layout_element_maximization_option: Optional[
        SheetLayoutElementMaximizationOptionModel
    ] = Field(default=None, alias="SheetLayoutElementMaximizationOption")
    visual_menu_option: Optional[VisualMenuOptionModel] = Field(
        default=None, alias="VisualMenuOption"
    )
    visual_axis_sort_option: Optional[VisualAxisSortOptionModel] = Field(
        default=None, alias="VisualAxisSortOption"
    )
    export_with_hidden_fields_option: Optional[
        ExportWithHiddenFieldsOptionModel
    ] = Field(default=None, alias="ExportWithHiddenFieldsOption")
    data_point_drill_up_down_option: Optional[DataPointDrillUpDownOptionModel] = Field(
        default=None, alias="DataPointDrillUpDownOption"
    )
    data_point_menu_label_option: Optional[DataPointMenuLabelOptionModel] = Field(
        default=None, alias="DataPointMenuLabelOption"
    )
    data_point_tooltip_option: Optional[DataPointTooltipOptionModel] = Field(
        default=None, alias="DataPointTooltipOption"
    )


class VisualPaletteModel(BaseModel):
    chart_color: Optional[str] = Field(default=None, alias="ChartColor")
    color_map: Optional[Sequence[DataPathColorModel]] = Field(
        default=None, alias="ColorMap"
    )


class PivotTableFieldOptionsModel(BaseModel):
    selected_field_options: Optional[Sequence[PivotTableFieldOptionModel]] = Field(
        default=None, alias="SelectedFieldOptions"
    )
    data_path_options: Optional[Sequence[PivotTableDataPathOptionModel]] = Field(
        default=None, alias="DataPathOptions"
    )


class TimeRangeFilterModel(BaseModel):
    filter_id: str = Field(alias="FilterId")
    column: ColumnIdentifierModel = Field(alias="Column")
    null_option: Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"] = Field(
        alias="NullOption"
    )
    include_minimum: Optional[bool] = Field(default=None, alias="IncludeMinimum")
    include_maximum: Optional[bool] = Field(default=None, alias="IncludeMaximum")
    range_minimum_value: Optional[TimeRangeFilterValueModel] = Field(
        default=None, alias="RangeMinimumValue"
    )
    range_maximum_value: Optional[TimeRangeFilterValueModel] = Field(
        default=None, alias="RangeMaximumValue"
    )
    exclude_period_configuration: Optional[ExcludePeriodConfigurationModel] = Field(
        default=None, alias="ExcludePeriodConfiguration"
    )
    time_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="TimeGranularity")


class CustomActionFilterOperationModel(BaseModel):
    selected_fields_configuration: FilterOperationSelectedFieldsConfigurationModel = (
        Field(alias="SelectedFieldsConfiguration")
    )
    target_visuals_configuration: FilterOperationTargetVisualsConfigurationModel = (
        Field(alias="TargetVisualsConfiguration")
    )


class AxisLabelOptionsModel(BaseModel):
    font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="FontConfiguration"
    )
    custom_label: Optional[str] = Field(default=None, alias="CustomLabel")
    apply_to: Optional[AxisLabelReferenceOptionsModel] = Field(
        default=None, alias="ApplyTo"
    )


class DataLabelOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    category_label_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="CategoryLabelVisibility"
    )
    measure_label_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="MeasureLabelVisibility"
    )
    data_label_types: Optional[Sequence[DataLabelTypeModel]] = Field(
        default=None, alias="DataLabelTypes"
    )
    position: Optional[
        Literal["BOTTOM", "INSIDE", "LEFT", "OUTSIDE", "RIGHT", "TOP"]
    ] = Field(default=None, alias="Position")
    label_content: Optional[Literal["PERCENT", "VALUE", "VALUE_AND_PERCENT"]] = Field(
        default=None, alias="LabelContent"
    )
    label_font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="LabelFontConfiguration"
    )
    label_color: Optional[str] = Field(default=None, alias="LabelColor")
    overlap: Optional[Literal["DISABLE_OVERLAP", "ENABLE_OVERLAP"]] = Field(
        default=None, alias="Overlap"
    )


class FunnelChartDataLabelOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    category_label_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="CategoryLabelVisibility"
    )
    measure_label_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="MeasureLabelVisibility"
    )
    position: Optional[
        Literal["BOTTOM", "INSIDE", "LEFT", "OUTSIDE", "RIGHT", "TOP"]
    ] = Field(default=None, alias="Position")
    label_font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="LabelFontConfiguration"
    )
    label_color: Optional[str] = Field(default=None, alias="LabelColor")
    measure_data_label_style: Optional[
        Literal[
            "PERCENTAGE_BY_FIRST_STAGE",
            "PERCENTAGE_BY_PREVIOUS_STAGE",
            "VALUE_AND_PERCENTAGE_BY_FIRST_STAGE",
            "VALUE_AND_PERCENTAGE_BY_PREVIOUS_STAGE",
            "VALUE_ONLY",
        ]
    ] = Field(default=None, alias="MeasureDataLabelStyle")


class LabelOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="FontConfiguration"
    )
    custom_label: Optional[str] = Field(default=None, alias="CustomLabel")


class PanelTitleOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="FontConfiguration"
    )
    horizontal_text_alignment: Optional[
        Literal["AUTO", "CENTER", "LEFT", "RIGHT"]
    ] = Field(default=None, alias="HorizontalTextAlignment")


class TableFieldCustomTextContentModel(BaseModel):
    font_configuration: FontConfigurationModel = Field(alias="FontConfiguration")
    value: Optional[str] = Field(default=None, alias="Value")


class ForecastConfigurationModel(BaseModel):
    forecast_properties: Optional[TimeBasedForecastPropertiesModel] = Field(
        default=None, alias="ForecastProperties"
    )
    scenario: Optional[ForecastScenarioModel] = Field(default=None, alias="Scenario")


class DefaultFreeFormLayoutConfigurationModel(BaseModel):
    canvas_size_options: FreeFormLayoutCanvasSizeOptionsModel = Field(
        alias="CanvasSizeOptions"
    )


class GlobalTableBorderOptionsModel(BaseModel):
    uniform_border: Optional[TableBorderOptionsModel] = Field(
        default=None, alias="UniformBorder"
    )
    side_specific_border: Optional[TableSideBorderOptionsModel] = Field(
        default=None, alias="SideSpecificBorder"
    )


class ConditionalFormattingGradientColorModel(BaseModel):
    expression: str = Field(alias="Expression")
    color: GradientColorModel = Field(alias="Color")


class DefaultGridLayoutConfigurationModel(BaseModel):
    canvas_size_options: GridLayoutCanvasSizeOptionsModel = Field(
        alias="CanvasSizeOptions"
    )


class GridLayoutConfigurationModel(BaseModel):
    elements: Sequence[GridLayoutElementModel] = Field(alias="Elements")
    canvas_size_options: Optional[GridLayoutCanvasSizeOptionsModel] = Field(
        default=None, alias="CanvasSizeOptions"
    )


class DescribeIngestionResponseModel(BaseModel):
    ingestion: IngestionModel = Field(alias="Ingestion")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListIngestionsResponseModel(BaseModel):
    ingestions: List[IngestionModel] = Field(alias="Ingestions")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LogicalTableSourceModel(BaseModel):
    join_instruction: Optional[JoinInstructionModel] = Field(
        default=None, alias="JoinInstruction"
    )
    physical_table_id: Optional[str] = Field(default=None, alias="PhysicalTableId")
    data_set_arn: Optional[str] = Field(default=None, alias="DataSetArn")


class DataFieldSeriesItemModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    axis_binding: Literal["PRIMARY_YAXIS", "SECONDARY_YAXIS"] = Field(
        alias="AxisBinding"
    )
    field_value: Optional[str] = Field(default=None, alias="FieldValue")
    settings: Optional[LineChartSeriesSettingsModel] = Field(
        default=None, alias="Settings"
    )


class FieldSeriesItemModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    axis_binding: Literal["PRIMARY_YAXIS", "SECONDARY_YAXIS"] = Field(
        alias="AxisBinding"
    )
    settings: Optional[LineChartSeriesSettingsModel] = Field(
        default=None, alias="Settings"
    )


class DataSourceParametersModel(BaseModel):
    amazon_elasticsearch_parameters: Optional[
        AmazonElasticsearchParametersModel
    ] = Field(default=None, alias="AmazonElasticsearchParameters")
    athena_parameters: Optional[AthenaParametersModel] = Field(
        default=None, alias="AthenaParameters"
    )
    aurora_parameters: Optional[AuroraParametersModel] = Field(
        default=None, alias="AuroraParameters"
    )
    aurora_postgre_sql_parameters: Optional[AuroraPostgreSqlParametersModel] = Field(
        default=None, alias="AuroraPostgreSqlParameters"
    )
    aws_iot_analytics_parameters: Optional[AwsIotAnalyticsParametersModel] = Field(
        default=None, alias="AwsIotAnalyticsParameters"
    )
    jira_parameters: Optional[JiraParametersModel] = Field(
        default=None, alias="JiraParameters"
    )
    maria_db_parameters: Optional[MariaDbParametersModel] = Field(
        default=None, alias="MariaDbParameters"
    )
    my_sql_parameters: Optional[MySqlParametersModel] = Field(
        default=None, alias="MySqlParameters"
    )
    oracle_parameters: Optional[OracleParametersModel] = Field(
        default=None, alias="OracleParameters"
    )
    postgre_sql_parameters: Optional[PostgreSqlParametersModel] = Field(
        default=None, alias="PostgreSqlParameters"
    )
    presto_parameters: Optional[PrestoParametersModel] = Field(
        default=None, alias="PrestoParameters"
    )
    rds_parameters: Optional[RdsParametersModel] = Field(
        default=None, alias="RdsParameters"
    )
    redshift_parameters: Optional[RedshiftParametersModel] = Field(
        default=None, alias="RedshiftParameters"
    )
    s3_parameters: Optional[S3ParametersModel] = Field(
        default=None, alias="S3Parameters"
    )
    service_now_parameters: Optional[ServiceNowParametersModel] = Field(
        default=None, alias="ServiceNowParameters"
    )
    snowflake_parameters: Optional[SnowflakeParametersModel] = Field(
        default=None, alias="SnowflakeParameters"
    )
    spark_parameters: Optional[SparkParametersModel] = Field(
        default=None, alias="SparkParameters"
    )
    sql_server_parameters: Optional[SqlServerParametersModel] = Field(
        default=None, alias="SqlServerParameters"
    )
    teradata_parameters: Optional[TeradataParametersModel] = Field(
        default=None, alias="TeradataParameters"
    )
    twitter_parameters: Optional[TwitterParametersModel] = Field(
        default=None, alias="TwitterParameters"
    )
    amazon_open_search_parameters: Optional[AmazonOpenSearchParametersModel] = Field(
        default=None, alias="AmazonOpenSearchParameters"
    )
    exasol_parameters: Optional[ExasolParametersModel] = Field(
        default=None, alias="ExasolParameters"
    )
    databricks_parameters: Optional[DatabricksParametersModel] = Field(
        default=None, alias="DatabricksParameters"
    )


class SheetStyleModel(BaseModel):
    tile: Optional[TileStyleModel] = Field(default=None, alias="Tile")
    tile_layout: Optional[TileLayoutStyleModel] = Field(
        default=None, alias="TileLayout"
    )


class DescribeNamespaceResponseModel(BaseModel):
    namespace: NamespaceInfoV2Model = Field(alias="Namespace")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListNamespacesResponseModel(BaseModel):
    namespaces: List[NamespaceInfoV2Model] = Field(alias="Namespaces")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CurrencyDisplayFormatConfigurationModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    suffix: Optional[str] = Field(default=None, alias="Suffix")
    separator_configuration: Optional[NumericSeparatorConfigurationModel] = Field(
        default=None, alias="SeparatorConfiguration"
    )
    symbol: Optional[str] = Field(default=None, alias="Symbol")
    decimal_places_configuration: Optional[DecimalPlacesConfigurationModel] = Field(
        default=None, alias="DecimalPlacesConfiguration"
    )
    number_scale: Optional[
        Literal["AUTO", "BILLIONS", "MILLIONS", "NONE", "THOUSANDS", "TRILLIONS"]
    ] = Field(default=None, alias="NumberScale")
    negative_value_configuration: Optional[NegativeValueConfigurationModel] = Field(
        default=None, alias="NegativeValueConfiguration"
    )
    null_value_format_configuration: Optional[
        NullValueFormatConfigurationModel
    ] = Field(default=None, alias="NullValueFormatConfiguration")


class NumberDisplayFormatConfigurationModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    suffix: Optional[str] = Field(default=None, alias="Suffix")
    separator_configuration: Optional[NumericSeparatorConfigurationModel] = Field(
        default=None, alias="SeparatorConfiguration"
    )
    decimal_places_configuration: Optional[DecimalPlacesConfigurationModel] = Field(
        default=None, alias="DecimalPlacesConfiguration"
    )
    number_scale: Optional[
        Literal["AUTO", "BILLIONS", "MILLIONS", "NONE", "THOUSANDS", "TRILLIONS"]
    ] = Field(default=None, alias="NumberScale")
    negative_value_configuration: Optional[NegativeValueConfigurationModel] = Field(
        default=None, alias="NegativeValueConfiguration"
    )
    null_value_format_configuration: Optional[
        NullValueFormatConfigurationModel
    ] = Field(default=None, alias="NullValueFormatConfiguration")


class PercentageDisplayFormatConfigurationModel(BaseModel):
    prefix: Optional[str] = Field(default=None, alias="Prefix")
    suffix: Optional[str] = Field(default=None, alias="Suffix")
    separator_configuration: Optional[NumericSeparatorConfigurationModel] = Field(
        default=None, alias="SeparatorConfiguration"
    )
    decimal_places_configuration: Optional[DecimalPlacesConfigurationModel] = Field(
        default=None, alias="DecimalPlacesConfiguration"
    )
    negative_value_configuration: Optional[NegativeValueConfigurationModel] = Field(
        default=None, alias="NegativeValueConfiguration"
    )
    null_value_format_configuration: Optional[
        NullValueFormatConfigurationModel
    ] = Field(default=None, alias="NullValueFormatConfiguration")


class AggregationFunctionModel(BaseModel):
    numerical_aggregation_function: Optional[NumericalAggregationFunctionModel] = Field(
        default=None, alias="NumericalAggregationFunction"
    )
    categorical_aggregation_function: Optional[
        Literal["COUNT", "DISTINCT_COUNT"]
    ] = Field(default=None, alias="CategoricalAggregationFunction")
    date_aggregation_function: Optional[
        Literal["COUNT", "DISTINCT_COUNT", "MAX", "MIN"]
    ] = Field(default=None, alias="DateAggregationFunction")


class ScrollBarOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    visible_range: Optional[VisibleRangeOptionsModel] = Field(
        default=None, alias="VisibleRange"
    )


class PhysicalTableModel(BaseModel):
    relational_table: Optional[RelationalTableModel] = Field(
        default=None, alias="RelationalTable"
    )
    custom_sql: Optional[CustomSqlModel] = Field(default=None, alias="CustomSql")
    s3_source: Optional[S3SourceModel] = Field(default=None, alias="S3Source")


class SectionBasedLayoutCanvasSizeOptionsModel(BaseModel):
    paper_canvas_size_options: Optional[
        SectionBasedLayoutPaperCanvasSizeOptionsModel
    ] = Field(default=None, alias="PaperCanvasSizeOptions")


class FilterScopeConfigurationModel(BaseModel):
    selected_sheets: Optional[SelectedSheetsFilterScopeConfigurationModel] = Field(
        default=None, alias="SelectedSheets"
    )


class FreeFormLayoutElementModel(BaseModel):
    element_id: str = Field(alias="ElementId")
    element_type: Literal[
        "FILTER_CONTROL", "PARAMETER_CONTROL", "TEXT_BOX", "VISUAL"
    ] = Field(alias="ElementType")
    xaxis_location: str = Field(alias="XAxisLocation")
    yaxis_location: str = Field(alias="YAxisLocation")
    width: str = Field(alias="Width")
    height: str = Field(alias="Height")
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    rendering_rules: Optional[Sequence[SheetElementRenderingRuleModel]] = Field(
        default=None, alias="RenderingRules"
    )
    border_style: Optional[FreeFormLayoutElementBorderStyleModel] = Field(
        default=None, alias="BorderStyle"
    )
    selected_border_style: Optional[FreeFormLayoutElementBorderStyleModel] = Field(
        default=None, alias="SelectedBorderStyle"
    )
    background_style: Optional[FreeFormLayoutElementBackgroundStyleModel] = Field(
        default=None, alias="BackgroundStyle"
    )
    loading_animation: Optional[LoadingAnimationModel] = Field(
        default=None, alias="LoadingAnimation"
    )


class DateTimeParameterDeclarationModel(BaseModel):
    name: str = Field(alias="Name")
    default_values: Optional[DateTimeDefaultValuesModel] = Field(
        default=None, alias="DefaultValues"
    )
    time_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="TimeGranularity")
    value_when_unset: Optional[DateTimeValueWhenUnsetConfigurationModel] = Field(
        default=None, alias="ValueWhenUnset"
    )


class DecimalParameterDeclarationModel(BaseModel):
    parameter_value_type: Literal["MULTI_VALUED", "SINGLE_VALUED"] = Field(
        alias="ParameterValueType"
    )
    name: str = Field(alias="Name")
    default_values: Optional[DecimalDefaultValuesModel] = Field(
        default=None, alias="DefaultValues"
    )
    value_when_unset: Optional[DecimalValueWhenUnsetConfigurationModel] = Field(
        default=None, alias="ValueWhenUnset"
    )


class IntegerParameterDeclarationModel(BaseModel):
    parameter_value_type: Literal["MULTI_VALUED", "SINGLE_VALUED"] = Field(
        alias="ParameterValueType"
    )
    name: str = Field(alias="Name")
    default_values: Optional[IntegerDefaultValuesModel] = Field(
        default=None, alias="DefaultValues"
    )
    value_when_unset: Optional[IntegerValueWhenUnsetConfigurationModel] = Field(
        default=None, alias="ValueWhenUnset"
    )


class StringParameterDeclarationModel(BaseModel):
    parameter_value_type: Literal["MULTI_VALUED", "SINGLE_VALUED"] = Field(
        alias="ParameterValueType"
    )
    name: str = Field(alias="Name")
    default_values: Optional[StringDefaultValuesModel] = Field(
        default=None, alias="DefaultValues"
    )
    value_when_unset: Optional[StringValueWhenUnsetConfigurationModel] = Field(
        default=None, alias="ValueWhenUnset"
    )


class DateTimeHierarchyModel(BaseModel):
    hierarchy_id: str = Field(alias="HierarchyId")
    drill_down_filters: Optional[Sequence[DrillDownFilterModel]] = Field(
        default=None, alias="DrillDownFilters"
    )


class ExplicitHierarchyModel(BaseModel):
    hierarchy_id: str = Field(alias="HierarchyId")
    columns: Sequence[ColumnIdentifierModel] = Field(alias="Columns")
    drill_down_filters: Optional[Sequence[DrillDownFilterModel]] = Field(
        default=None, alias="DrillDownFilters"
    )


class PredefinedHierarchyModel(BaseModel):
    hierarchy_id: str = Field(alias="HierarchyId")
    columns: Sequence[ColumnIdentifierModel] = Field(alias="Columns")
    drill_down_filters: Optional[Sequence[DrillDownFilterModel]] = Field(
        default=None, alias="DrillDownFilters"
    )


class DescribeAnalysisResponseModel(BaseModel):
    analysis: AnalysisModel = Field(alias="Analysis")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DashboardModel(BaseModel):
    dashboard_id: Optional[str] = Field(default=None, alias="DashboardId")
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[DashboardVersionModel] = Field(default=None, alias="Version")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_published_time: Optional[datetime] = Field(
        default=None, alias="LastPublishedTime"
    )
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")


class GenerateEmbedUrlForAnonymousUserRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    namespace: str = Field(alias="Namespace")
    authorized_resource_arns: Sequence[str] = Field(alias="AuthorizedResourceArns")
    experience_configuration: AnonymousUserEmbeddingExperienceConfigurationModel = (
        Field(alias="ExperienceConfiguration")
    )
    session_lifetime_in_minutes: Optional[int] = Field(
        default=None, alias="SessionLifetimeInMinutes"
    )
    session_tags: Optional[Sequence[SessionTagModel]] = Field(
        default=None, alias="SessionTags"
    )
    allowed_domains: Optional[Sequence[str]] = Field(
        default=None, alias="AllowedDomains"
    )


class GenerateEmbedUrlForRegisteredUserRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    user_arn: str = Field(alias="UserArn")
    experience_configuration: RegisteredUserEmbeddingExperienceConfigurationModel = (
        Field(alias="ExperienceConfiguration")
    )
    session_lifetime_in_minutes: Optional[int] = Field(
        default=None, alias="SessionLifetimeInMinutes"
    )
    allowed_domains: Optional[Sequence[str]] = Field(
        default=None, alias="AllowedDomains"
    )


class AxisDataOptionsModel(BaseModel):
    numeric_axis_options: Optional[NumericAxisOptionsModel] = Field(
        default=None, alias="NumericAxisOptions"
    )
    date_axis_options: Optional[DateAxisOptionsModel] = Field(
        default=None, alias="DateAxisOptions"
    )


class GeospatialPointStyleOptionsModel(BaseModel):
    selected_point_style: Optional[Literal["CLUSTER", "POINT"]] = Field(
        default=None, alias="SelectedPointStyle"
    )
    cluster_marker_configuration: Optional[ClusterMarkerConfigurationModel] = Field(
        default=None, alias="ClusterMarkerConfiguration"
    )


class TransformOperationModel(BaseModel):
    project_operation: Optional[ProjectOperationModel] = Field(
        default=None, alias="ProjectOperation"
    )
    filter_operation: Optional[FilterOperationModel] = Field(
        default=None, alias="FilterOperation"
    )
    create_columns_operation: Optional[CreateColumnsOperationModel] = Field(
        default=None, alias="CreateColumnsOperation"
    )
    rename_column_operation: Optional[RenameColumnOperationModel] = Field(
        default=None, alias="RenameColumnOperation"
    )
    cast_column_type_operation: Optional[CastColumnTypeOperationModel] = Field(
        default=None, alias="CastColumnTypeOperation"
    )
    tag_column_operation: Optional[TagColumnOperationModel] = Field(
        default=None, alias="TagColumnOperation"
    )
    untag_column_operation: Optional[UntagColumnOperationModel] = Field(
        default=None, alias="UntagColumnOperation"
    )


class TemplateVersionModel(BaseModel):
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    errors: Optional[List[TemplateErrorModel]] = Field(default=None, alias="Errors")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")
    data_set_configurations: Optional[List[DataSetConfigurationModel]] = Field(
        default=None, alias="DataSetConfigurations"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    source_entity_arn: Optional[str] = Field(default=None, alias="SourceEntityArn")
    theme_arn: Optional[str] = Field(default=None, alias="ThemeArn")
    sheets: Optional[List[SheetModel]] = Field(default=None, alias="Sheets")


class SetParameterValueConfigurationModel(BaseModel):
    destination_parameter_name: str = Field(alias="DestinationParameterName")
    value: DestinationParameterValueConfigurationModel = Field(alias="Value")


class ChartAxisLabelOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    sort_icon_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="SortIconVisibility"
    )
    axis_label_options: Optional[Sequence[AxisLabelOptionsModel]] = Field(
        default=None, alias="AxisLabelOptions"
    )


class AxisTickLabelOptionsModel(BaseModel):
    label_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="LabelOptions"
    )
    rotation_angle: Optional[float] = Field(default=None, alias="RotationAngle")


class DateTimePickerControlDisplayOptionsModel(BaseModel):
    title_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="TitleOptions"
    )
    date_time_format: Optional[str] = Field(default=None, alias="DateTimeFormat")


class DropDownControlDisplayOptionsModel(BaseModel):
    select_all_options: Optional[ListControlSelectAllOptionsModel] = Field(
        default=None, alias="SelectAllOptions"
    )
    title_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="TitleOptions"
    )


class LegendOptionsModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    title: Optional[LabelOptionsModel] = Field(default=None, alias="Title")
    position: Optional[Literal["AUTO", "BOTTOM", "RIGHT", "TOP"]] = Field(
        default=None, alias="Position"
    )
    width: Optional[str] = Field(default=None, alias="Width")
    height: Optional[str] = Field(default=None, alias="Height")


class ListControlDisplayOptionsModel(BaseModel):
    search_options: Optional[ListControlSearchOptionsModel] = Field(
        default=None, alias="SearchOptions"
    )
    select_all_options: Optional[ListControlSelectAllOptionsModel] = Field(
        default=None, alias="SelectAllOptions"
    )
    title_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="TitleOptions"
    )


class RelativeDateTimeControlDisplayOptionsModel(BaseModel):
    title_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="TitleOptions"
    )
    date_time_format: Optional[str] = Field(default=None, alias="DateTimeFormat")


class SliderControlDisplayOptionsModel(BaseModel):
    title_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="TitleOptions"
    )


class TextAreaControlDisplayOptionsModel(BaseModel):
    title_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="TitleOptions"
    )
    placeholder_options: Optional[TextControlPlaceholderOptionsModel] = Field(
        default=None, alias="PlaceholderOptions"
    )


class TextFieldControlDisplayOptionsModel(BaseModel):
    title_options: Optional[LabelOptionsModel] = Field(
        default=None, alias="TitleOptions"
    )
    placeholder_options: Optional[TextControlPlaceholderOptionsModel] = Field(
        default=None, alias="PlaceholderOptions"
    )


class PanelConfigurationModel(BaseModel):
    title: Optional[PanelTitleOptionsModel] = Field(default=None, alias="Title")
    border_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="BorderVisibility"
    )
    border_thickness: Optional[str] = Field(default=None, alias="BorderThickness")
    border_style: Optional[Literal["DASHED", "DOTTED", "SOLID"]] = Field(
        default=None, alias="BorderStyle"
    )
    border_color: Optional[str] = Field(default=None, alias="BorderColor")
    gutter_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="GutterVisibility"
    )
    gutter_spacing: Optional[str] = Field(default=None, alias="GutterSpacing")
    background_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="BackgroundVisibility"
    )
    background_color: Optional[str] = Field(default=None, alias="BackgroundColor")


class TableFieldLinkContentConfigurationModel(BaseModel):
    custom_text_content: Optional[TableFieldCustomTextContentModel] = Field(
        default=None, alias="CustomTextContent"
    )
    custom_icon_content: Optional[TableFieldCustomIconContentModel] = Field(
        default=None, alias="CustomIconContent"
    )


class TableCellStyleModel(BaseModel):
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="FontConfiguration"
    )
    text_wrap: Optional[Literal["NONE", "WRAP"]] = Field(default=None, alias="TextWrap")
    horizontal_text_alignment: Optional[
        Literal["AUTO", "CENTER", "LEFT", "RIGHT"]
    ] = Field(default=None, alias="HorizontalTextAlignment")
    vertical_text_alignment: Optional[Literal["BOTTOM", "MIDDLE", "TOP"]] = Field(
        default=None, alias="VerticalTextAlignment"
    )
    background_color: Optional[str] = Field(default=None, alias="BackgroundColor")
    height: Optional[int] = Field(default=None, alias="Height")
    border: Optional[GlobalTableBorderOptionsModel] = Field(
        default=None, alias="Border"
    )


class ConditionalFormattingColorModel(BaseModel):
    solid: Optional[ConditionalFormattingSolidColorModel] = Field(
        default=None, alias="Solid"
    )
    gradient: Optional[ConditionalFormattingGradientColorModel] = Field(
        default=None, alias="Gradient"
    )


class DefaultInteractiveLayoutConfigurationModel(BaseModel):
    grid: Optional[DefaultGridLayoutConfigurationModel] = Field(
        default=None, alias="Grid"
    )
    free_form: Optional[DefaultFreeFormLayoutConfigurationModel] = Field(
        default=None, alias="FreeForm"
    )


class SheetControlLayoutConfigurationModel(BaseModel):
    grid_layout: Optional[GridLayoutConfigurationModel] = Field(
        default=None, alias="GridLayout"
    )


class SeriesItemModel(BaseModel):
    field_series_item: Optional[FieldSeriesItemModel] = Field(
        default=None, alias="FieldSeriesItem"
    )
    data_field_series_item: Optional[DataFieldSeriesItemModel] = Field(
        default=None, alias="DataFieldSeriesItem"
    )


class CredentialPairModel(BaseModel):
    username: str = Field(alias="Username")
    password: str = Field(alias="Password")
    alternate_data_source_parameters: Optional[
        Sequence[DataSourceParametersModel]
    ] = Field(default=None, alias="AlternateDataSourceParameters")


class DataSourceModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    data_source_id: Optional[str] = Field(default=None, alias="DataSourceId")
    name: Optional[str] = Field(default=None, alias="Name")
    type: Optional[
        Literal[
            "ADOBE_ANALYTICS",
            "AMAZON_ELASTICSEARCH",
            "AMAZON_OPENSEARCH",
            "ATHENA",
            "AURORA",
            "AURORA_POSTGRESQL",
            "AWS_IOT_ANALYTICS",
            "DATABRICKS",
            "EXASOL",
            "GITHUB",
            "JIRA",
            "MARIADB",
            "MYSQL",
            "ORACLE",
            "POSTGRESQL",
            "PRESTO",
            "REDSHIFT",
            "S3",
            "SALESFORCE",
            "SERVICENOW",
            "SNOWFLAKE",
            "SPARK",
            "SQLSERVER",
            "TERADATA",
            "TIMESTREAM",
            "TWITTER",
        ]
    ] = Field(default=None, alias="Type")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    data_source_parameters: Optional[DataSourceParametersModel] = Field(
        default=None, alias="DataSourceParameters"
    )
    alternate_data_source_parameters: Optional[List[DataSourceParametersModel]] = Field(
        default=None, alias="AlternateDataSourceParameters"
    )
    vpc_connection_properties: Optional[VpcConnectionPropertiesModel] = Field(
        default=None, alias="VpcConnectionProperties"
    )
    ssl_properties: Optional[SslPropertiesModel] = Field(
        default=None, alias="SslProperties"
    )
    error_info: Optional[DataSourceErrorInfoModel] = Field(
        default=None, alias="ErrorInfo"
    )
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")


class ThemeConfigurationModel(BaseModel):
    data_color_palette: Optional[DataColorPaletteModel] = Field(
        default=None, alias="DataColorPalette"
    )
    uicolor_palette: Optional[UIColorPaletteModel] = Field(
        default=None, alias="UIColorPalette"
    )
    sheet: Optional[SheetStyleModel] = Field(default=None, alias="Sheet")
    typography: Optional[TypographyModel] = Field(default=None, alias="Typography")


class ComparisonFormatConfigurationModel(BaseModel):
    number_display_format_configuration: Optional[
        NumberDisplayFormatConfigurationModel
    ] = Field(default=None, alias="NumberDisplayFormatConfiguration")
    percentage_display_format_configuration: Optional[
        PercentageDisplayFormatConfigurationModel
    ] = Field(default=None, alias="PercentageDisplayFormatConfiguration")


class NumericFormatConfigurationModel(BaseModel):
    number_display_format_configuration: Optional[
        NumberDisplayFormatConfigurationModel
    ] = Field(default=None, alias="NumberDisplayFormatConfiguration")
    currency_display_format_configuration: Optional[
        CurrencyDisplayFormatConfigurationModel
    ] = Field(default=None, alias="CurrencyDisplayFormatConfiguration")
    percentage_display_format_configuration: Optional[
        PercentageDisplayFormatConfigurationModel
    ] = Field(default=None, alias="PercentageDisplayFormatConfiguration")


class AggregationSortConfigurationModel(BaseModel):
    column: ColumnIdentifierModel = Field(alias="Column")
    sort_direction: Literal["ASC", "DESC"] = Field(alias="SortDirection")
    aggregation_function: AggregationFunctionModel = Field(alias="AggregationFunction")


class ColumnSortModel(BaseModel):
    sort_by: ColumnIdentifierModel = Field(alias="SortBy")
    direction: Literal["ASC", "DESC"] = Field(alias="Direction")
    aggregation_function: Optional[AggregationFunctionModel] = Field(
        default=None, alias="AggregationFunction"
    )


class ColumnTooltipItemModel(BaseModel):
    column: ColumnIdentifierModel = Field(alias="Column")
    label: Optional[str] = Field(default=None, alias="Label")
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    aggregation: Optional[AggregationFunctionModel] = Field(
        default=None, alias="Aggregation"
    )


class NumericEqualityFilterModel(BaseModel):
    filter_id: str = Field(alias="FilterId")
    column: ColumnIdentifierModel = Field(alias="Column")
    match_operator: Literal["DOES_NOT_EQUAL", "EQUALS"] = Field(alias="MatchOperator")
    null_option: Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"] = Field(
        alias="NullOption"
    )
    value: Optional[float] = Field(default=None, alias="Value")
    select_all_options: Optional[Literal["FILTER_ALL_VALUES"]] = Field(
        default=None, alias="SelectAllOptions"
    )
    aggregation_function: Optional[AggregationFunctionModel] = Field(
        default=None, alias="AggregationFunction"
    )
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")


class NumericRangeFilterModel(BaseModel):
    filter_id: str = Field(alias="FilterId")
    column: ColumnIdentifierModel = Field(alias="Column")
    null_option: Literal["ALL_VALUES", "NON_NULLS_ONLY", "NULLS_ONLY"] = Field(
        alias="NullOption"
    )
    include_minimum: Optional[bool] = Field(default=None, alias="IncludeMinimum")
    include_maximum: Optional[bool] = Field(default=None, alias="IncludeMaximum")
    range_minimum: Optional[NumericRangeFilterValueModel] = Field(
        default=None, alias="RangeMinimum"
    )
    range_maximum: Optional[NumericRangeFilterValueModel] = Field(
        default=None, alias="RangeMaximum"
    )
    select_all_options: Optional[Literal["FILTER_ALL_VALUES"]] = Field(
        default=None, alias="SelectAllOptions"
    )
    aggregation_function: Optional[AggregationFunctionModel] = Field(
        default=None, alias="AggregationFunction"
    )


class ReferenceLineDynamicDataConfigurationModel(BaseModel):
    column: ColumnIdentifierModel = Field(alias="Column")
    measure_aggregation_function: AggregationFunctionModel = Field(
        alias="MeasureAggregationFunction"
    )
    calculation: NumericalAggregationFunctionModel = Field(alias="Calculation")


class DefaultSectionBasedLayoutConfigurationModel(BaseModel):
    canvas_size_options: SectionBasedLayoutCanvasSizeOptionsModel = Field(
        alias="CanvasSizeOptions"
    )


class FreeFormLayoutConfigurationModel(BaseModel):
    elements: Sequence[FreeFormLayoutElementModel] = Field(alias="Elements")
    canvas_size_options: Optional[FreeFormLayoutCanvasSizeOptionsModel] = Field(
        default=None, alias="CanvasSizeOptions"
    )


class FreeFormSectionLayoutConfigurationModel(BaseModel):
    elements: Sequence[FreeFormLayoutElementModel] = Field(alias="Elements")


class ParameterDeclarationModel(BaseModel):
    string_parameter_declaration: Optional[StringParameterDeclarationModel] = Field(
        default=None, alias="StringParameterDeclaration"
    )
    decimal_parameter_declaration: Optional[DecimalParameterDeclarationModel] = Field(
        default=None, alias="DecimalParameterDeclaration"
    )
    integer_parameter_declaration: Optional[IntegerParameterDeclarationModel] = Field(
        default=None, alias="IntegerParameterDeclaration"
    )
    date_time_parameter_declaration: Optional[
        DateTimeParameterDeclarationModel
    ] = Field(default=None, alias="DateTimeParameterDeclaration")


class ColumnHierarchyModel(BaseModel):
    explicit_hierarchy: Optional[ExplicitHierarchyModel] = Field(
        default=None, alias="ExplicitHierarchy"
    )
    date_time_hierarchy: Optional[DateTimeHierarchyModel] = Field(
        default=None, alias="DateTimeHierarchy"
    )
    predefined_hierarchy: Optional[PredefinedHierarchyModel] = Field(
        default=None, alias="PredefinedHierarchy"
    )


class DescribeDashboardResponseModel(BaseModel):
    dashboard: DashboardModel = Field(alias="Dashboard")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class LogicalTableModel(BaseModel):
    alias: str = Field(alias="Alias")
    source: LogicalTableSourceModel = Field(alias="Source")
    data_transforms: Optional[Sequence[TransformOperationModel]] = Field(
        default=None, alias="DataTransforms"
    )


class TemplateModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    version: Optional[TemplateVersionModel] = Field(default=None, alias="Version")
    template_id: Optional[str] = Field(default=None, alias="TemplateId")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")


class CustomActionSetParametersOperationModel(BaseModel):
    parameter_value_configurations: Sequence[
        SetParameterValueConfigurationModel
    ] = Field(alias="ParameterValueConfigurations")


class AxisDisplayOptionsModel(BaseModel):
    tick_label_options: Optional[AxisTickLabelOptionsModel] = Field(
        default=None, alias="TickLabelOptions"
    )
    axis_line_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="AxisLineVisibility"
    )
    grid_line_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="GridLineVisibility"
    )
    data_options: Optional[AxisDataOptionsModel] = Field(
        default=None, alias="DataOptions"
    )
    scrollbar_options: Optional[ScrollBarOptionsModel] = Field(
        default=None, alias="ScrollbarOptions"
    )
    axis_offset: Optional[str] = Field(default=None, alias="AxisOffset")


class FilterDateTimePickerControlModel(BaseModel):
    filter_control_id: str = Field(alias="FilterControlId")
    title: str = Field(alias="Title")
    source_filter_id: str = Field(alias="SourceFilterId")
    display_options: Optional[DateTimePickerControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )
    type: Optional[Literal["DATE_RANGE", "SINGLE_VALUED"]] = Field(
        default=None, alias="Type"
    )


class ParameterDateTimePickerControlModel(BaseModel):
    parameter_control_id: str = Field(alias="ParameterControlId")
    title: str = Field(alias="Title")
    source_parameter_name: str = Field(alias="SourceParameterName")
    display_options: Optional[DateTimePickerControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )


class FilterDropDownControlModel(BaseModel):
    filter_control_id: str = Field(alias="FilterControlId")
    title: str = Field(alias="Title")
    source_filter_id: str = Field(alias="SourceFilterId")
    display_options: Optional[DropDownControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )
    type: Optional[Literal["MULTI_SELECT", "SINGLE_SELECT"]] = Field(
        default=None, alias="Type"
    )
    selectable_values: Optional[FilterSelectableValuesModel] = Field(
        default=None, alias="SelectableValues"
    )
    cascading_control_configuration: Optional[
        CascadingControlConfigurationModel
    ] = Field(default=None, alias="CascadingControlConfiguration")


class ParameterDropDownControlModel(BaseModel):
    parameter_control_id: str = Field(alias="ParameterControlId")
    title: str = Field(alias="Title")
    source_parameter_name: str = Field(alias="SourceParameterName")
    display_options: Optional[DropDownControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )
    type: Optional[Literal["MULTI_SELECT", "SINGLE_SELECT"]] = Field(
        default=None, alias="Type"
    )
    selectable_values: Optional[ParameterSelectableValuesModel] = Field(
        default=None, alias="SelectableValues"
    )
    cascading_control_configuration: Optional[
        CascadingControlConfigurationModel
    ] = Field(default=None, alias="CascadingControlConfiguration")


class FilterListControlModel(BaseModel):
    filter_control_id: str = Field(alias="FilterControlId")
    title: str = Field(alias="Title")
    source_filter_id: str = Field(alias="SourceFilterId")
    display_options: Optional[ListControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )
    type: Optional[Literal["MULTI_SELECT", "SINGLE_SELECT"]] = Field(
        default=None, alias="Type"
    )
    selectable_values: Optional[FilterSelectableValuesModel] = Field(
        default=None, alias="SelectableValues"
    )
    cascading_control_configuration: Optional[
        CascadingControlConfigurationModel
    ] = Field(default=None, alias="CascadingControlConfiguration")


class ParameterListControlModel(BaseModel):
    parameter_control_id: str = Field(alias="ParameterControlId")
    title: str = Field(alias="Title")
    source_parameter_name: str = Field(alias="SourceParameterName")
    display_options: Optional[ListControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )
    type: Optional[Literal["MULTI_SELECT", "SINGLE_SELECT"]] = Field(
        default=None, alias="Type"
    )
    selectable_values: Optional[ParameterSelectableValuesModel] = Field(
        default=None, alias="SelectableValues"
    )
    cascading_control_configuration: Optional[
        CascadingControlConfigurationModel
    ] = Field(default=None, alias="CascadingControlConfiguration")


class FilterRelativeDateTimeControlModel(BaseModel):
    filter_control_id: str = Field(alias="FilterControlId")
    title: str = Field(alias="Title")
    source_filter_id: str = Field(alias="SourceFilterId")
    display_options: Optional[RelativeDateTimeControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )


class FilterSliderControlModel(BaseModel):
    filter_control_id: str = Field(alias="FilterControlId")
    title: str = Field(alias="Title")
    source_filter_id: str = Field(alias="SourceFilterId")
    maximum_value: float = Field(alias="MaximumValue")
    minimum_value: float = Field(alias="MinimumValue")
    step_size: float = Field(alias="StepSize")
    display_options: Optional[SliderControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )
    type: Optional[Literal["RANGE", "SINGLE_POINT"]] = Field(default=None, alias="Type")


class ParameterSliderControlModel(BaseModel):
    parameter_control_id: str = Field(alias="ParameterControlId")
    title: str = Field(alias="Title")
    source_parameter_name: str = Field(alias="SourceParameterName")
    maximum_value: float = Field(alias="MaximumValue")
    minimum_value: float = Field(alias="MinimumValue")
    step_size: float = Field(alias="StepSize")
    display_options: Optional[SliderControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )


class FilterTextAreaControlModel(BaseModel):
    filter_control_id: str = Field(alias="FilterControlId")
    title: str = Field(alias="Title")
    source_filter_id: str = Field(alias="SourceFilterId")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    display_options: Optional[TextAreaControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )


class ParameterTextAreaControlModel(BaseModel):
    parameter_control_id: str = Field(alias="ParameterControlId")
    title: str = Field(alias="Title")
    source_parameter_name: str = Field(alias="SourceParameterName")
    delimiter: Optional[str] = Field(default=None, alias="Delimiter")
    display_options: Optional[TextAreaControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )


class FilterTextFieldControlModel(BaseModel):
    filter_control_id: str = Field(alias="FilterControlId")
    title: str = Field(alias="Title")
    source_filter_id: str = Field(alias="SourceFilterId")
    display_options: Optional[TextFieldControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )


class ParameterTextFieldControlModel(BaseModel):
    parameter_control_id: str = Field(alias="ParameterControlId")
    title: str = Field(alias="Title")
    source_parameter_name: str = Field(alias="SourceParameterName")
    display_options: Optional[TextFieldControlDisplayOptionsModel] = Field(
        default=None, alias="DisplayOptions"
    )


class SmallMultiplesOptionsModel(BaseModel):
    max_visible_rows: Optional[int] = Field(default=None, alias="MaxVisibleRows")
    max_visible_columns: Optional[int] = Field(default=None, alias="MaxVisibleColumns")
    panel_configuration: Optional[PanelConfigurationModel] = Field(
        default=None, alias="PanelConfiguration"
    )


class TableFieldLinkConfigurationModel(BaseModel):
    target: Literal["NEW_TAB", "NEW_WINDOW", "SAME_TAB"] = Field(alias="Target")
    content: TableFieldLinkContentConfigurationModel = Field(alias="Content")


class PivotTableOptionsModel(BaseModel):
    metric_placement: Optional[Literal["COLUMN", "ROW"]] = Field(
        default=None, alias="MetricPlacement"
    )
    single_metric_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="SingleMetricVisibility"
    )
    column_names_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="ColumnNamesVisibility"
    )
    toggle_buttons_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="ToggleButtonsVisibility"
    )
    column_header_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="ColumnHeaderStyle"
    )
    row_header_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="RowHeaderStyle"
    )
    cell_style: Optional[TableCellStyleModel] = Field(default=None, alias="CellStyle")
    row_field_names_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="RowFieldNamesStyle"
    )
    row_alternate_color_options: Optional[RowAlternateColorOptionsModel] = Field(
        default=None, alias="RowAlternateColorOptions"
    )


class PivotTotalOptionsModel(BaseModel):
    totals_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="TotalsVisibility"
    )
    placement: Optional[Literal["END", "START"]] = Field(
        default=None, alias="Placement"
    )
    scroll_status: Optional[Literal["PINNED", "SCROLLED"]] = Field(
        default=None, alias="ScrollStatus"
    )
    custom_label: Optional[str] = Field(default=None, alias="CustomLabel")
    total_cell_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="TotalCellStyle"
    )
    value_cell_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="ValueCellStyle"
    )
    metric_header_cell_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="MetricHeaderCellStyle"
    )


class SubtotalOptionsModel(BaseModel):
    totals_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="TotalsVisibility"
    )
    custom_label: Optional[str] = Field(default=None, alias="CustomLabel")
    field_level: Optional[Literal["ALL", "CUSTOM", "LAST"]] = Field(
        default=None, alias="FieldLevel"
    )
    field_level_options: Optional[
        Sequence[PivotTableFieldSubtotalOptionsModel]
    ] = Field(default=None, alias="FieldLevelOptions")
    total_cell_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="TotalCellStyle"
    )
    value_cell_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="ValueCellStyle"
    )
    metric_header_cell_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="MetricHeaderCellStyle"
    )


class TableOptionsModel(BaseModel):
    orientation: Optional[Literal["HORIZONTAL", "VERTICAL"]] = Field(
        default=None, alias="Orientation"
    )
    header_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="HeaderStyle"
    )
    cell_style: Optional[TableCellStyleModel] = Field(default=None, alias="CellStyle")
    row_alternate_color_options: Optional[RowAlternateColorOptionsModel] = Field(
        default=None, alias="RowAlternateColorOptions"
    )


class TotalOptionsModel(BaseModel):
    totals_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="TotalsVisibility"
    )
    placement: Optional[Literal["END", "START"]] = Field(
        default=None, alias="Placement"
    )
    scroll_status: Optional[Literal["PINNED", "SCROLLED"]] = Field(
        default=None, alias="ScrollStatus"
    )
    custom_label: Optional[str] = Field(default=None, alias="CustomLabel")
    total_cell_style: Optional[TableCellStyleModel] = Field(
        default=None, alias="TotalCellStyle"
    )


class GaugeChartArcConditionalFormattingModel(BaseModel):
    foreground_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="ForegroundColor"
    )


class GaugeChartPrimaryValueConditionalFormattingModel(BaseModel):
    text_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="TextColor"
    )
    icon: Optional[ConditionalFormattingIconModel] = Field(default=None, alias="Icon")


class KPIPrimaryValueConditionalFormattingModel(BaseModel):
    text_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="TextColor"
    )
    icon: Optional[ConditionalFormattingIconModel] = Field(default=None, alias="Icon")


class KPIProgressBarConditionalFormattingModel(BaseModel):
    foreground_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="ForegroundColor"
    )


class ShapeConditionalFormatModel(BaseModel):
    background_color: ConditionalFormattingColorModel = Field(alias="BackgroundColor")


class TableRowConditionalFormattingModel(BaseModel):
    background_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="BackgroundColor"
    )
    text_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="TextColor"
    )


class TextConditionalFormatModel(BaseModel):
    background_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="BackgroundColor"
    )
    text_color: Optional[ConditionalFormattingColorModel] = Field(
        default=None, alias="TextColor"
    )
    icon: Optional[ConditionalFormattingIconModel] = Field(default=None, alias="Icon")


class SheetControlLayoutModel(BaseModel):
    configuration: SheetControlLayoutConfigurationModel = Field(alias="Configuration")


class DataSourceCredentialsModel(BaseModel):
    credential_pair: Optional[CredentialPairModel] = Field(
        default=None, alias="CredentialPair"
    )
    copy_source_arn: Optional[str] = Field(default=None, alias="CopySourceArn")
    secret_arn: Optional[str] = Field(default=None, alias="SecretArn")


class DescribeDataSourceResponseModel(BaseModel):
    data_source: DataSourceModel = Field(alias="DataSource")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListDataSourcesResponseModel(BaseModel):
    data_sources: List[DataSourceModel] = Field(alias="DataSources")
    next_token: str = Field(alias="NextToken")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateThemeRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    name: str = Field(alias="Name")
    base_theme_id: str = Field(alias="BaseThemeId")
    configuration: ThemeConfigurationModel = Field(alias="Configuration")
    version_description: Optional[str] = Field(default=None, alias="VersionDescription")
    permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class ThemeVersionModel(BaseModel):
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    arn: Optional[str] = Field(default=None, alias="Arn")
    description: Optional[str] = Field(default=None, alias="Description")
    base_theme_id: Optional[str] = Field(default=None, alias="BaseThemeId")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    configuration: Optional[ThemeConfigurationModel] = Field(
        default=None, alias="Configuration"
    )
    errors: Optional[List[ThemeErrorModel]] = Field(default=None, alias="Errors")
    status: Optional[
        Literal[
            "CREATION_FAILED",
            "CREATION_IN_PROGRESS",
            "CREATION_SUCCESSFUL",
            "DELETED",
            "UPDATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_SUCCESSFUL",
        ]
    ] = Field(default=None, alias="Status")


class UpdateThemeRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    theme_id: str = Field(alias="ThemeId")
    base_theme_id: str = Field(alias="BaseThemeId")
    name: Optional[str] = Field(default=None, alias="Name")
    version_description: Optional[str] = Field(default=None, alias="VersionDescription")
    configuration: Optional[ThemeConfigurationModel] = Field(
        default=None, alias="Configuration"
    )


class ComparisonConfigurationModel(BaseModel):
    comparison_method: Optional[
        Literal["DIFFERENCE", "PERCENT", "PERCENT_DIFFERENCE"]
    ] = Field(default=None, alias="ComparisonMethod")
    comparison_format: Optional[ComparisonFormatConfigurationModel] = Field(
        default=None, alias="ComparisonFormat"
    )


class DateTimeFormatConfigurationModel(BaseModel):
    date_time_format: Optional[str] = Field(default=None, alias="DateTimeFormat")
    null_value_format_configuration: Optional[
        NullValueFormatConfigurationModel
    ] = Field(default=None, alias="NullValueFormatConfiguration")
    numeric_format_configuration: Optional[NumericFormatConfigurationModel] = Field(
        default=None, alias="NumericFormatConfiguration"
    )


class NumberFormatConfigurationModel(BaseModel):
    format_configuration: Optional[NumericFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class ReferenceLineValueLabelConfigurationModel(BaseModel):
    relative_position: Optional[
        Literal["AFTER_CUSTOM_LABEL", "BEFORE_CUSTOM_LABEL"]
    ] = Field(default=None, alias="RelativePosition")
    format_configuration: Optional[NumericFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class StringFormatConfigurationModel(BaseModel):
    null_value_format_configuration: Optional[
        NullValueFormatConfigurationModel
    ] = Field(default=None, alias="NullValueFormatConfiguration")
    numeric_format_configuration: Optional[NumericFormatConfigurationModel] = Field(
        default=None, alias="NumericFormatConfiguration"
    )


class TopBottomFilterModel(BaseModel):
    filter_id: str = Field(alias="FilterId")
    column: ColumnIdentifierModel = Field(alias="Column")
    aggregation_sort_configurations: Sequence[
        AggregationSortConfigurationModel
    ] = Field(alias="AggregationSortConfigurations")
    limit: Optional[int] = Field(default=None, alias="Limit")
    time_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="TimeGranularity")
    parameter_name: Optional[str] = Field(default=None, alias="ParameterName")


class FieldSortOptionsModel(BaseModel):
    field_sort: Optional[FieldSortModel] = Field(default=None, alias="FieldSort")
    column_sort: Optional[ColumnSortModel] = Field(default=None, alias="ColumnSort")


class PivotTableSortByModel(BaseModel):
    field: Optional[FieldSortModel] = Field(default=None, alias="Field")
    column: Optional[ColumnSortModel] = Field(default=None, alias="Column")
    data_path: Optional[DataPathSortModel] = Field(default=None, alias="DataPath")


class TooltipItemModel(BaseModel):
    field_tooltip_item: Optional[FieldTooltipItemModel] = Field(
        default=None, alias="FieldTooltipItem"
    )
    column_tooltip_item: Optional[ColumnTooltipItemModel] = Field(
        default=None, alias="ColumnTooltipItem"
    )


class ReferenceLineDataConfigurationModel(BaseModel):
    static_configuration: Optional[ReferenceLineStaticDataConfigurationModel] = Field(
        default=None, alias="StaticConfiguration"
    )
    dynamic_configuration: Optional[ReferenceLineDynamicDataConfigurationModel] = Field(
        default=None, alias="DynamicConfiguration"
    )
    axis_binding: Optional[Literal["PRIMARY_YAXIS", "SECONDARY_YAXIS"]] = Field(
        default=None, alias="AxisBinding"
    )


class DefaultPaginatedLayoutConfigurationModel(BaseModel):
    section_based: Optional[DefaultSectionBasedLayoutConfigurationModel] = Field(
        default=None, alias="SectionBased"
    )


class SectionLayoutConfigurationModel(BaseModel):
    free_form_layout: FreeFormSectionLayoutConfigurationModel = Field(
        alias="FreeFormLayout"
    )


class CreateDataSetRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")
    name: str = Field(alias="Name")
    physical_table_map: Mapping[str, PhysicalTableModel] = Field(
        alias="PhysicalTableMap"
    )
    import_mode: Literal["DIRECT_QUERY", "SPICE"] = Field(alias="ImportMode")
    logical_table_map: Optional[Mapping[str, LogicalTableModel]] = Field(
        default=None, alias="LogicalTableMap"
    )
    column_groups: Optional[Sequence[ColumnGroupModel]] = Field(
        default=None, alias="ColumnGroups"
    )
    field_folders: Optional[Mapping[str, FieldFolderModel]] = Field(
        default=None, alias="FieldFolders"
    )
    permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )
    row_level_permission_data_set: Optional[RowLevelPermissionDataSetModel] = Field(
        default=None, alias="RowLevelPermissionDataSet"
    )
    row_level_permission_tag_configuration: Optional[
        RowLevelPermissionTagConfigurationModel
    ] = Field(default=None, alias="RowLevelPermissionTagConfiguration")
    column_level_permission_rules: Optional[
        Sequence[ColumnLevelPermissionRuleModel]
    ] = Field(default=None, alias="ColumnLevelPermissionRules")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    data_set_usage_configuration: Optional[DataSetUsageConfigurationModel] = Field(
        default=None, alias="DataSetUsageConfiguration"
    )


class DataSetModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    data_set_id: Optional[str] = Field(default=None, alias="DataSetId")
    name: Optional[str] = Field(default=None, alias="Name")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    physical_table_map: Optional[Dict[str, PhysicalTableModel]] = Field(
        default=None, alias="PhysicalTableMap"
    )
    logical_table_map: Optional[Dict[str, LogicalTableModel]] = Field(
        default=None, alias="LogicalTableMap"
    )
    output_columns: Optional[List[OutputColumnModel]] = Field(
        default=None, alias="OutputColumns"
    )
    import_mode: Optional[Literal["DIRECT_QUERY", "SPICE"]] = Field(
        default=None, alias="ImportMode"
    )
    consumed_spice_capacity_in_bytes: Optional[int] = Field(
        default=None, alias="ConsumedSpiceCapacityInBytes"
    )
    column_groups: Optional[List[ColumnGroupModel]] = Field(
        default=None, alias="ColumnGroups"
    )
    field_folders: Optional[Dict[str, FieldFolderModel]] = Field(
        default=None, alias="FieldFolders"
    )
    row_level_permission_data_set: Optional[RowLevelPermissionDataSetModel] = Field(
        default=None, alias="RowLevelPermissionDataSet"
    )
    row_level_permission_tag_configuration: Optional[
        RowLevelPermissionTagConfigurationModel
    ] = Field(default=None, alias="RowLevelPermissionTagConfiguration")
    column_level_permission_rules: Optional[
        List[ColumnLevelPermissionRuleModel]
    ] = Field(default=None, alias="ColumnLevelPermissionRules")
    data_set_usage_configuration: Optional[DataSetUsageConfigurationModel] = Field(
        default=None, alias="DataSetUsageConfiguration"
    )


class UpdateDataSetRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_set_id: str = Field(alias="DataSetId")
    name: str = Field(alias="Name")
    physical_table_map: Mapping[str, PhysicalTableModel] = Field(
        alias="PhysicalTableMap"
    )
    import_mode: Literal["DIRECT_QUERY", "SPICE"] = Field(alias="ImportMode")
    logical_table_map: Optional[Mapping[str, LogicalTableModel]] = Field(
        default=None, alias="LogicalTableMap"
    )
    column_groups: Optional[Sequence[ColumnGroupModel]] = Field(
        default=None, alias="ColumnGroups"
    )
    field_folders: Optional[Mapping[str, FieldFolderModel]] = Field(
        default=None, alias="FieldFolders"
    )
    row_level_permission_data_set: Optional[RowLevelPermissionDataSetModel] = Field(
        default=None, alias="RowLevelPermissionDataSet"
    )
    row_level_permission_tag_configuration: Optional[
        RowLevelPermissionTagConfigurationModel
    ] = Field(default=None, alias="RowLevelPermissionTagConfiguration")
    column_level_permission_rules: Optional[
        Sequence[ColumnLevelPermissionRuleModel]
    ] = Field(default=None, alias="ColumnLevelPermissionRules")
    data_set_usage_configuration: Optional[DataSetUsageConfigurationModel] = Field(
        default=None, alias="DataSetUsageConfiguration"
    )


class DescribeTemplateResponseModel(BaseModel):
    template: TemplateModel = Field(alias="Template")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VisualCustomActionOperationModel(BaseModel):
    filter_operation: Optional[CustomActionFilterOperationModel] = Field(
        default=None, alias="FilterOperation"
    )
    navigation_operation: Optional[CustomActionNavigationOperationModel] = Field(
        default=None, alias="NavigationOperation"
    )
    url_operation: Optional[CustomActionURLOperationModel] = Field(
        default=None, alias="URLOperation"
    )
    set_parameters_operation: Optional[CustomActionSetParametersOperationModel] = Field(
        default=None, alias="SetParametersOperation"
    )


class LineSeriesAxisDisplayOptionsModel(BaseModel):
    axis_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="AxisOptions"
    )
    missing_data_configurations: Optional[
        Sequence[MissingDataConfigurationModel]
    ] = Field(default=None, alias="MissingDataConfigurations")


class FilterControlModel(BaseModel):
    date_time_picker: Optional[FilterDateTimePickerControlModel] = Field(
        default=None, alias="DateTimePicker"
    )
    list: Optional[FilterListControlModel] = Field(default=None, alias="List")
    dropdown: Optional[FilterDropDownControlModel] = Field(
        default=None, alias="Dropdown"
    )
    text_field: Optional[FilterTextFieldControlModel] = Field(
        default=None, alias="TextField"
    )
    text_area: Optional[FilterTextAreaControlModel] = Field(
        default=None, alias="TextArea"
    )
    slider: Optional[FilterSliderControlModel] = Field(default=None, alias="Slider")
    relative_date_time: Optional[FilterRelativeDateTimeControlModel] = Field(
        default=None, alias="RelativeDateTime"
    )


class ParameterControlModel(BaseModel):
    date_time_picker: Optional[ParameterDateTimePickerControlModel] = Field(
        default=None, alias="DateTimePicker"
    )
    list: Optional[ParameterListControlModel] = Field(default=None, alias="List")
    dropdown: Optional[ParameterDropDownControlModel] = Field(
        default=None, alias="Dropdown"
    )
    text_field: Optional[ParameterTextFieldControlModel] = Field(
        default=None, alias="TextField"
    )
    text_area: Optional[ParameterTextAreaControlModel] = Field(
        default=None, alias="TextArea"
    )
    slider: Optional[ParameterSliderControlModel] = Field(default=None, alias="Slider")


class TableFieldURLConfigurationModel(BaseModel):
    link_configuration: Optional[TableFieldLinkConfigurationModel] = Field(
        default=None, alias="LinkConfiguration"
    )
    image_configuration: Optional[TableFieldImageConfigurationModel] = Field(
        default=None, alias="ImageConfiguration"
    )


class PivotTableTotalOptionsModel(BaseModel):
    row_subtotal_options: Optional[SubtotalOptionsModel] = Field(
        default=None, alias="RowSubtotalOptions"
    )
    column_subtotal_options: Optional[SubtotalOptionsModel] = Field(
        default=None, alias="ColumnSubtotalOptions"
    )
    row_total_options: Optional[PivotTotalOptionsModel] = Field(
        default=None, alias="RowTotalOptions"
    )
    column_total_options: Optional[PivotTotalOptionsModel] = Field(
        default=None, alias="ColumnTotalOptions"
    )


class GaugeChartConditionalFormattingOptionModel(BaseModel):
    primary_value: Optional[GaugeChartPrimaryValueConditionalFormattingModel] = Field(
        default=None, alias="PrimaryValue"
    )
    arc: Optional[GaugeChartArcConditionalFormattingModel] = Field(
        default=None, alias="Arc"
    )


class KPIConditionalFormattingOptionModel(BaseModel):
    primary_value: Optional[KPIPrimaryValueConditionalFormattingModel] = Field(
        default=None, alias="PrimaryValue"
    )
    progress_bar: Optional[KPIProgressBarConditionalFormattingModel] = Field(
        default=None, alias="ProgressBar"
    )


class FilledMapShapeConditionalFormattingModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    format: Optional[ShapeConditionalFormatModel] = Field(default=None, alias="Format")


class PivotTableCellConditionalFormattingModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    text_format: Optional[TextConditionalFormatModel] = Field(
        default=None, alias="TextFormat"
    )
    scope: Optional[PivotTableConditionalFormattingScopeModel] = Field(
        default=None, alias="Scope"
    )


class TableCellConditionalFormattingModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    text_format: Optional[TextConditionalFormatModel] = Field(
        default=None, alias="TextFormat"
    )


class CreateDataSourceRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_source_id: str = Field(alias="DataSourceId")
    name: str = Field(alias="Name")
    type: Literal[
        "ADOBE_ANALYTICS",
        "AMAZON_ELASTICSEARCH",
        "AMAZON_OPENSEARCH",
        "ATHENA",
        "AURORA",
        "AURORA_POSTGRESQL",
        "AWS_IOT_ANALYTICS",
        "DATABRICKS",
        "EXASOL",
        "GITHUB",
        "JIRA",
        "MARIADB",
        "MYSQL",
        "ORACLE",
        "POSTGRESQL",
        "PRESTO",
        "REDSHIFT",
        "S3",
        "SALESFORCE",
        "SERVICENOW",
        "SNOWFLAKE",
        "SPARK",
        "SQLSERVER",
        "TERADATA",
        "TIMESTREAM",
        "TWITTER",
    ] = Field(alias="Type")
    data_source_parameters: Optional[DataSourceParametersModel] = Field(
        default=None, alias="DataSourceParameters"
    )
    credentials: Optional[DataSourceCredentialsModel] = Field(
        default=None, alias="Credentials"
    )
    permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )
    vpc_connection_properties: Optional[VpcConnectionPropertiesModel] = Field(
        default=None, alias="VpcConnectionProperties"
    )
    ssl_properties: Optional[SslPropertiesModel] = Field(
        default=None, alias="SslProperties"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")


class UpdateDataSourceRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    data_source_id: str = Field(alias="DataSourceId")
    name: str = Field(alias="Name")
    data_source_parameters: Optional[DataSourceParametersModel] = Field(
        default=None, alias="DataSourceParameters"
    )
    credentials: Optional[DataSourceCredentialsModel] = Field(
        default=None, alias="Credentials"
    )
    vpc_connection_properties: Optional[VpcConnectionPropertiesModel] = Field(
        default=None, alias="VpcConnectionProperties"
    )
    ssl_properties: Optional[SslPropertiesModel] = Field(
        default=None, alias="SslProperties"
    )


class ThemeModel(BaseModel):
    arn: Optional[str] = Field(default=None, alias="Arn")
    name: Optional[str] = Field(default=None, alias="Name")
    theme_id: Optional[str] = Field(default=None, alias="ThemeId")
    version: Optional[ThemeVersionModel] = Field(default=None, alias="Version")
    created_time: Optional[datetime] = Field(default=None, alias="CreatedTime")
    last_updated_time: Optional[datetime] = Field(default=None, alias="LastUpdatedTime")
    type: Optional[Literal["ALL", "CUSTOM", "QUICKSIGHT"]] = Field(
        default=None, alias="Type"
    )


class GaugeChartOptionsModel(BaseModel):
    primary_value_display_type: Optional[
        Literal["ACTUAL", "COMPARISON", "HIDDEN"]
    ] = Field(default=None, alias="PrimaryValueDisplayType")
    comparison: Optional[ComparisonConfigurationModel] = Field(
        default=None, alias="Comparison"
    )
    arc_axis: Optional[ArcAxisConfigurationModel] = Field(default=None, alias="ArcAxis")
    arc: Optional[ArcConfigurationModel] = Field(default=None, alias="Arc")
    primary_value_font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="PrimaryValueFontConfiguration"
    )


class KPIOptionsModel(BaseModel):
    progress_bar: Optional[ProgressBarOptionsModel] = Field(
        default=None, alias="ProgressBar"
    )
    trend_arrows: Optional[TrendArrowOptionsModel] = Field(
        default=None, alias="TrendArrows"
    )
    secondary_value: Optional[SecondaryValueOptionsModel] = Field(
        default=None, alias="SecondaryValue"
    )
    comparison: Optional[ComparisonConfigurationModel] = Field(
        default=None, alias="Comparison"
    )
    primary_value_display_type: Optional[
        Literal["ACTUAL", "COMPARISON", "HIDDEN"]
    ] = Field(default=None, alias="PrimaryValueDisplayType")
    primary_value_font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="PrimaryValueFontConfiguration"
    )
    secondary_value_font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="SecondaryValueFontConfiguration"
    )


class DateDimensionFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")
    date_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="DateGranularity")
    hierarchy_id: Optional[str] = Field(default=None, alias="HierarchyId")
    format_configuration: Optional[DateTimeFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class DateMeasureFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")
    aggregation_function: Optional[
        Literal["COUNT", "DISTINCT_COUNT", "MAX", "MIN"]
    ] = Field(default=None, alias="AggregationFunction")
    format_configuration: Optional[DateTimeFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class NumericalDimensionFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")
    hierarchy_id: Optional[str] = Field(default=None, alias="HierarchyId")
    format_configuration: Optional[NumberFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class NumericalMeasureFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")
    aggregation_function: Optional[NumericalAggregationFunctionModel] = Field(
        default=None, alias="AggregationFunction"
    )
    format_configuration: Optional[NumberFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class ReferenceLineLabelConfigurationModel(BaseModel):
    value_label_configuration: Optional[
        ReferenceLineValueLabelConfigurationModel
    ] = Field(default=None, alias="ValueLabelConfiguration")
    custom_label_configuration: Optional[
        ReferenceLineCustomLabelConfigurationModel
    ] = Field(default=None, alias="CustomLabelConfiguration")
    font_configuration: Optional[FontConfigurationModel] = Field(
        default=None, alias="FontConfiguration"
    )
    font_color: Optional[str] = Field(default=None, alias="FontColor")
    horizontal_position: Optional[Literal["CENTER", "LEFT", "RIGHT"]] = Field(
        default=None, alias="HorizontalPosition"
    )
    vertical_position: Optional[Literal["ABOVE", "BELOW"]] = Field(
        default=None, alias="VerticalPosition"
    )


class CategoricalDimensionFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")
    hierarchy_id: Optional[str] = Field(default=None, alias="HierarchyId")
    format_configuration: Optional[StringFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class CategoricalMeasureFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")
    aggregation_function: Optional[Literal["COUNT", "DISTINCT_COUNT"]] = Field(
        default=None, alias="AggregationFunction"
    )
    format_configuration: Optional[StringFormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class FormatConfigurationModel(BaseModel):
    string_format_configuration: Optional[StringFormatConfigurationModel] = Field(
        default=None, alias="StringFormatConfiguration"
    )
    number_format_configuration: Optional[NumberFormatConfigurationModel] = Field(
        default=None, alias="NumberFormatConfiguration"
    )
    date_time_format_configuration: Optional[DateTimeFormatConfigurationModel] = Field(
        default=None, alias="DateTimeFormatConfiguration"
    )


class FilterModel(BaseModel):
    category_filter: Optional[CategoryFilterModel] = Field(
        default=None, alias="CategoryFilter"
    )
    numeric_range_filter: Optional[NumericRangeFilterModel] = Field(
        default=None, alias="NumericRangeFilter"
    )
    numeric_equality_filter: Optional[NumericEqualityFilterModel] = Field(
        default=None, alias="NumericEqualityFilter"
    )
    time_equality_filter: Optional[TimeEqualityFilterModel] = Field(
        default=None, alias="TimeEqualityFilter"
    )
    time_range_filter: Optional[TimeRangeFilterModel] = Field(
        default=None, alias="TimeRangeFilter"
    )
    relative_dates_filter: Optional[RelativeDatesFilterModel] = Field(
        default=None, alias="RelativeDatesFilter"
    )
    top_bottom_filter: Optional[TopBottomFilterModel] = Field(
        default=None, alias="TopBottomFilter"
    )


class BarChartSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    category_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="CategoryItemsLimit"
    )
    color_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="ColorSort"
    )
    color_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="ColorItemsLimit"
    )
    small_multiples_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="SmallMultiplesSort"
    )
    small_multiples_limit_configuration: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="SmallMultiplesLimitConfiguration"
    )


class BoxPlotSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    pagination_configuration: Optional[PaginationConfigurationModel] = Field(
        default=None, alias="PaginationConfiguration"
    )


class ComboChartSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    category_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="CategoryItemsLimit"
    )
    color_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="ColorSort"
    )
    color_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="ColorItemsLimit"
    )


class FilledMapSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )


class FunnelChartSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    category_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="CategoryItemsLimit"
    )


class HeatMapSortConfigurationModel(BaseModel):
    heat_map_row_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="HeatMapRowSort"
    )
    heat_map_column_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="HeatMapColumnSort"
    )
    heat_map_row_items_limit_configuration: Optional[
        ItemsLimitConfigurationModel
    ] = Field(default=None, alias="HeatMapRowItemsLimitConfiguration")
    heat_map_column_items_limit_configuration: Optional[
        ItemsLimitConfigurationModel
    ] = Field(default=None, alias="HeatMapColumnItemsLimitConfiguration")


class KPISortConfigurationModel(BaseModel):
    trend_group_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="TrendGroupSort"
    )


class LineChartSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    category_items_limit_configuration: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="CategoryItemsLimitConfiguration"
    )
    color_items_limit_configuration: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="ColorItemsLimitConfiguration"
    )
    small_multiples_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="SmallMultiplesSort"
    )
    small_multiples_limit_configuration: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="SmallMultiplesLimitConfiguration"
    )


class PieChartSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    category_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="CategoryItemsLimit"
    )
    small_multiples_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="SmallMultiplesSort"
    )
    small_multiples_limit_configuration: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="SmallMultiplesLimitConfiguration"
    )


class RadarChartSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    category_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="CategoryItemsLimit"
    )
    color_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="ColorSort"
    )
    color_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="ColorItemsLimit"
    )


class SankeyDiagramSortConfigurationModel(BaseModel):
    weight_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="WeightSort"
    )
    source_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="SourceItemsLimit"
    )
    destination_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="DestinationItemsLimit"
    )


class TableSortConfigurationModel(BaseModel):
    row_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="RowSort"
    )
    pagination_configuration: Optional[PaginationConfigurationModel] = Field(
        default=None, alias="PaginationConfiguration"
    )


class TreeMapSortConfigurationModel(BaseModel):
    tree_map_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="TreeMapSort"
    )
    tree_map_group_items_limit_configuration: Optional[
        ItemsLimitConfigurationModel
    ] = Field(default=None, alias="TreeMapGroupItemsLimitConfiguration")


class WaterfallChartSortConfigurationModel(BaseModel):
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )
    breakdown_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="BreakdownItemsLimit"
    )


class WordCloudSortConfigurationModel(BaseModel):
    category_items_limit: Optional[ItemsLimitConfigurationModel] = Field(
        default=None, alias="CategoryItemsLimit"
    )
    category_sort: Optional[Sequence[FieldSortOptionsModel]] = Field(
        default=None, alias="CategorySort"
    )


class PivotFieldSortOptionsModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    sort_by: PivotTableSortByModel = Field(alias="SortBy")


class FieldBasedTooltipModel(BaseModel):
    aggregation_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="AggregationVisibility"
    )
    tooltip_title_type: Optional[Literal["NONE", "PRIMARY_VALUE"]] = Field(
        default=None, alias="TooltipTitleType"
    )
    tooltip_fields: Optional[Sequence[TooltipItemModel]] = Field(
        default=None, alias="TooltipFields"
    )


class DefaultNewSheetConfigurationModel(BaseModel):
    interactive_layout_configuration: Optional[
        DefaultInteractiveLayoutConfigurationModel
    ] = Field(default=None, alias="InteractiveLayoutConfiguration")
    paginated_layout_configuration: Optional[
        DefaultPaginatedLayoutConfigurationModel
    ] = Field(default=None, alias="PaginatedLayoutConfiguration")
    sheet_content_type: Optional[Literal["INTERACTIVE", "PAGINATED"]] = Field(
        default=None, alias="SheetContentType"
    )


class BodySectionContentModel(BaseModel):
    layout: Optional[SectionLayoutConfigurationModel] = Field(
        default=None, alias="Layout"
    )


class HeaderFooterSectionConfigurationModel(BaseModel):
    section_id: str = Field(alias="SectionId")
    layout: SectionLayoutConfigurationModel = Field(alias="Layout")
    style: Optional[SectionStyleModel] = Field(default=None, alias="Style")


class DescribeDataSetResponseModel(BaseModel):
    data_set: DataSetModel = Field(alias="DataSet")
    request_id: str = Field(alias="RequestId")
    status: int = Field(alias="Status")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class VisualCustomActionModel(BaseModel):
    custom_action_id: str = Field(alias="CustomActionId")
    name: str = Field(alias="Name")
    trigger: Literal["DATA_POINT_CLICK", "DATA_POINT_MENU"] = Field(alias="Trigger")
    action_operations: Sequence[VisualCustomActionOperationModel] = Field(
        alias="ActionOperations"
    )
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class TableFieldOptionModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    width: Optional[str] = Field(default=None, alias="Width")
    custom_label: Optional[str] = Field(default=None, alias="CustomLabel")
    visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="Visibility"
    )
    url_styling: Optional[TableFieldURLConfigurationModel] = Field(
        default=None, alias="URLStyling"
    )


class GaugeChartConditionalFormattingModel(BaseModel):
    conditional_formatting_options: Optional[
        Sequence[GaugeChartConditionalFormattingOptionModel]
    ] = Field(default=None, alias="ConditionalFormattingOptions")


class KPIConditionalFormattingModel(BaseModel):
    conditional_formatting_options: Optional[
        Sequence[KPIConditionalFormattingOptionModel]
    ] = Field(default=None, alias="ConditionalFormattingOptions")


class FilledMapConditionalFormattingOptionModel(BaseModel):
    shape: FilledMapShapeConditionalFormattingModel = Field(alias="Shape")


class PivotTableConditionalFormattingOptionModel(BaseModel):
    cell: Optional[PivotTableCellConditionalFormattingModel] = Field(
        default=None, alias="Cell"
    )


class TableConditionalFormattingOptionModel(BaseModel):
    cell: Optional[TableCellConditionalFormattingModel] = Field(
        default=None, alias="Cell"
    )
    row: Optional[TableRowConditionalFormattingModel] = Field(default=None, alias="Row")


class DescribeThemeResponseModel(BaseModel):
    theme: ThemeModel = Field(alias="Theme")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ReferenceLineModel(BaseModel):
    data_configuration: ReferenceLineDataConfigurationModel = Field(
        alias="DataConfiguration"
    )
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )
    style_configuration: Optional[ReferenceLineStyleConfigurationModel] = Field(
        default=None, alias="StyleConfiguration"
    )
    label_configuration: Optional[ReferenceLineLabelConfigurationModel] = Field(
        default=None, alias="LabelConfiguration"
    )


class DimensionFieldModel(BaseModel):
    numerical_dimension_field: Optional[NumericalDimensionFieldModel] = Field(
        default=None, alias="NumericalDimensionField"
    )
    categorical_dimension_field: Optional[CategoricalDimensionFieldModel] = Field(
        default=None, alias="CategoricalDimensionField"
    )
    date_dimension_field: Optional[DateDimensionFieldModel] = Field(
        default=None, alias="DateDimensionField"
    )


class MeasureFieldModel(BaseModel):
    numerical_measure_field: Optional[NumericalMeasureFieldModel] = Field(
        default=None, alias="NumericalMeasureField"
    )
    categorical_measure_field: Optional[CategoricalMeasureFieldModel] = Field(
        default=None, alias="CategoricalMeasureField"
    )
    date_measure_field: Optional[DateMeasureFieldModel] = Field(
        default=None, alias="DateMeasureField"
    )
    calculated_measure_field: Optional[CalculatedMeasureFieldModel] = Field(
        default=None, alias="CalculatedMeasureField"
    )


class ColumnConfigurationModel(BaseModel):
    column: ColumnIdentifierModel = Field(alias="Column")
    format_configuration: Optional[FormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )
    role: Optional[Literal["DIMENSION", "MEASURE"]] = Field(default=None, alias="Role")


class UnaggregatedFieldModel(BaseModel):
    field_id: str = Field(alias="FieldId")
    column: ColumnIdentifierModel = Field(alias="Column")
    format_configuration: Optional[FormatConfigurationModel] = Field(
        default=None, alias="FormatConfiguration"
    )


class FilterGroupModel(BaseModel):
    filter_group_id: str = Field(alias="FilterGroupId")
    filters: Sequence[FilterModel] = Field(alias="Filters")
    scope_configuration: FilterScopeConfigurationModel = Field(
        alias="ScopeConfiguration"
    )
    cross_dataset: Literal["ALL_DATASETS", "SINGLE_DATASET"] = Field(
        alias="CrossDataset"
    )
    status: Optional[Literal["DISABLED", "ENABLED"]] = Field(
        default=None, alias="Status"
    )


class PivotTableSortConfigurationModel(BaseModel):
    field_sort_options: Optional[Sequence[PivotFieldSortOptionsModel]] = Field(
        default=None, alias="FieldSortOptions"
    )


class TooltipOptionsModel(BaseModel):
    tooltip_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="TooltipVisibility"
    )
    selected_tooltip_type: Optional[Literal["BASIC", "DETAILED"]] = Field(
        default=None, alias="SelectedTooltipType"
    )
    field_based_tooltip: Optional[FieldBasedTooltipModel] = Field(
        default=None, alias="FieldBasedTooltip"
    )


class AnalysisDefaultsModel(BaseModel):
    default_new_sheet_configuration: DefaultNewSheetConfigurationModel = Field(
        alias="DefaultNewSheetConfiguration"
    )


class BodySectionConfigurationModel(BaseModel):
    section_id: str = Field(alias="SectionId")
    content: BodySectionContentModel = Field(alias="Content")
    style: Optional[SectionStyleModel] = Field(default=None, alias="Style")
    page_break_configuration: Optional[SectionPageBreakConfigurationModel] = Field(
        default=None, alias="PageBreakConfiguration"
    )


class CustomContentVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    data_set_identifier: str = Field(alias="DataSetIdentifier")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[CustomContentConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class EmptyVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    data_set_identifier: str = Field(alias="DataSetIdentifier")
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class TableFieldOptionsModel(BaseModel):
    selected_field_options: Optional[Sequence[TableFieldOptionModel]] = Field(
        default=None, alias="SelectedFieldOptions"
    )
    order: Optional[Sequence[str]] = Field(default=None, alias="Order")


class FilledMapConditionalFormattingModel(BaseModel):
    conditional_formatting_options: Sequence[
        FilledMapConditionalFormattingOptionModel
    ] = Field(alias="ConditionalFormattingOptions")


class PivotTableConditionalFormattingModel(BaseModel):
    conditional_formatting_options: Optional[
        Sequence[PivotTableConditionalFormattingOptionModel]
    ] = Field(default=None, alias="ConditionalFormattingOptions")


class TableConditionalFormattingModel(BaseModel):
    conditional_formatting_options: Optional[
        Sequence[TableConditionalFormattingOptionModel]
    ] = Field(default=None, alias="ConditionalFormattingOptions")


class UniqueValuesComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    category: DimensionFieldModel = Field(alias="Category")
    name: Optional[str] = Field(default=None, alias="Name")


class BarChartAggregatedFieldWellsModel(BaseModel):
    category: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Category"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")
    colors: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Colors"
    )
    small_multiples: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="SmallMultiples"
    )


class BoxPlotAggregatedFieldWellsModel(BaseModel):
    group_by: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="GroupBy"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class ComboChartAggregatedFieldWellsModel(BaseModel):
    category: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Category"
    )
    bar_values: Optional[Sequence[MeasureFieldModel]] = Field(
        default=None, alias="BarValues"
    )
    colors: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Colors"
    )
    line_values: Optional[Sequence[MeasureFieldModel]] = Field(
        default=None, alias="LineValues"
    )


class FilledMapAggregatedFieldWellsModel(BaseModel):
    geospatial: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Geospatial"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class ForecastComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    time: DimensionFieldModel = Field(alias="Time")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[MeasureFieldModel] = Field(default=None, alias="Value")
    periods_forward: Optional[int] = Field(default=None, alias="PeriodsForward")
    periods_backward: Optional[int] = Field(default=None, alias="PeriodsBackward")
    upper_boundary: Optional[float] = Field(default=None, alias="UpperBoundary")
    lower_boundary: Optional[float] = Field(default=None, alias="LowerBoundary")
    prediction_interval: Optional[int] = Field(default=None, alias="PredictionInterval")
    seasonality: Optional[Literal["AUTOMATIC", "CUSTOM"]] = Field(
        default=None, alias="Seasonality"
    )
    custom_seasonality_value: Optional[int] = Field(
        default=None, alias="CustomSeasonalityValue"
    )


class FunnelChartAggregatedFieldWellsModel(BaseModel):
    category: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Category"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class GaugeChartFieldWellsModel(BaseModel):
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")
    target_values: Optional[Sequence[MeasureFieldModel]] = Field(
        default=None, alias="TargetValues"
    )


class GeospatialMapAggregatedFieldWellsModel(BaseModel):
    geospatial: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Geospatial"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")
    colors: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Colors"
    )


class GrowthRateComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    time: DimensionFieldModel = Field(alias="Time")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[MeasureFieldModel] = Field(default=None, alias="Value")
    period_size: Optional[int] = Field(default=None, alias="PeriodSize")


class HeatMapAggregatedFieldWellsModel(BaseModel):
    rows: Optional[Sequence[DimensionFieldModel]] = Field(default=None, alias="Rows")
    columns: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Columns"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class HistogramAggregatedFieldWellsModel(BaseModel):
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class KPIFieldWellsModel(BaseModel):
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")
    target_values: Optional[Sequence[MeasureFieldModel]] = Field(
        default=None, alias="TargetValues"
    )
    trend_groups: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="TrendGroups"
    )


class LineChartAggregatedFieldWellsModel(BaseModel):
    category: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Category"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")
    colors: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Colors"
    )
    small_multiples: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="SmallMultiples"
    )


class MaximumMinimumComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    time: DimensionFieldModel = Field(alias="Time")
    type: Literal["MAXIMUM", "MINIMUM"] = Field(alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[MeasureFieldModel] = Field(default=None, alias="Value")


class MetricComparisonComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    time: DimensionFieldModel = Field(alias="Time")
    from_value: MeasureFieldModel = Field(alias="FromValue")
    target_value: MeasureFieldModel = Field(alias="TargetValue")
    name: Optional[str] = Field(default=None, alias="Name")


class PeriodOverPeriodComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    time: DimensionFieldModel = Field(alias="Time")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[MeasureFieldModel] = Field(default=None, alias="Value")


class PeriodToDateComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    time: DimensionFieldModel = Field(alias="Time")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[MeasureFieldModel] = Field(default=None, alias="Value")
    period_time_granularity: Optional[
        Literal[
            "DAY",
            "HOUR",
            "MILLISECOND",
            "MINUTE",
            "MONTH",
            "QUARTER",
            "SECOND",
            "WEEK",
            "YEAR",
        ]
    ] = Field(default=None, alias="PeriodTimeGranularity")


class PieChartAggregatedFieldWellsModel(BaseModel):
    category: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Category"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")
    small_multiples: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="SmallMultiples"
    )


class PivotTableAggregatedFieldWellsModel(BaseModel):
    rows: Optional[Sequence[DimensionFieldModel]] = Field(default=None, alias="Rows")
    columns: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Columns"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class RadarChartAggregatedFieldWellsModel(BaseModel):
    category: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Category"
    )
    color: Optional[Sequence[DimensionFieldModel]] = Field(default=None, alias="Color")
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class SankeyDiagramAggregatedFieldWellsModel(BaseModel):
    source: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Source"
    )
    destination: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Destination"
    )
    weight: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Weight")


class ScatterPlotCategoricallyAggregatedFieldWellsModel(BaseModel):
    xaxis: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="XAxis")
    yaxis: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="YAxis")
    category: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Category"
    )
    size: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Size")


class ScatterPlotUnaggregatedFieldWellsModel(BaseModel):
    xaxis: Optional[Sequence[DimensionFieldModel]] = Field(default=None, alias="XAxis")
    yaxis: Optional[Sequence[DimensionFieldModel]] = Field(default=None, alias="YAxis")
    size: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Size")


class TableAggregatedFieldWellsModel(BaseModel):
    group_by: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="GroupBy"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")


class TopBottomMoversComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    time: DimensionFieldModel = Field(alias="Time")
    category: DimensionFieldModel = Field(alias="Category")
    type: Literal["BOTTOM", "TOP"] = Field(alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[MeasureFieldModel] = Field(default=None, alias="Value")
    mover_size: Optional[int] = Field(default=None, alias="MoverSize")
    sort_order: Optional[Literal["ABSOLUTE_DIFFERENCE", "PERCENT_DIFFERENCE"]] = Field(
        default=None, alias="SortOrder"
    )


class TopBottomRankedComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    category: DimensionFieldModel = Field(alias="Category")
    type: Literal["BOTTOM", "TOP"] = Field(alias="Type")
    name: Optional[str] = Field(default=None, alias="Name")
    value: Optional[MeasureFieldModel] = Field(default=None, alias="Value")
    result_size: Optional[int] = Field(default=None, alias="ResultSize")


class TotalAggregationComputationModel(BaseModel):
    computation_id: str = Field(alias="ComputationId")
    value: MeasureFieldModel = Field(alias="Value")
    name: Optional[str] = Field(default=None, alias="Name")


class TreeMapAggregatedFieldWellsModel(BaseModel):
    groups: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Groups"
    )
    sizes: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Sizes")
    colors: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Colors")


class WaterfallChartAggregatedFieldWellsModel(BaseModel):
    categories: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Categories"
    )
    values: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Values")
    breakdowns: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="Breakdowns"
    )


class WordCloudAggregatedFieldWellsModel(BaseModel):
    group_by: Optional[Sequence[DimensionFieldModel]] = Field(
        default=None, alias="GroupBy"
    )
    size: Optional[Sequence[MeasureFieldModel]] = Field(default=None, alias="Size")


class TableUnaggregatedFieldWellsModel(BaseModel):
    values: Optional[Sequence[UnaggregatedFieldModel]] = Field(
        default=None, alias="Values"
    )


class SectionBasedLayoutConfigurationModel(BaseModel):
    header_sections: Sequence[HeaderFooterSectionConfigurationModel] = Field(
        alias="HeaderSections"
    )
    body_sections: Sequence[BodySectionConfigurationModel] = Field(alias="BodySections")
    footer_sections: Sequence[HeaderFooterSectionConfigurationModel] = Field(
        alias="FooterSections"
    )
    canvas_size_options: SectionBasedLayoutCanvasSizeOptionsModel = Field(
        alias="CanvasSizeOptions"
    )


class BarChartFieldWellsModel(BaseModel):
    bar_chart_aggregated_field_wells: Optional[
        BarChartAggregatedFieldWellsModel
    ] = Field(default=None, alias="BarChartAggregatedFieldWells")


class BoxPlotFieldWellsModel(BaseModel):
    box_plot_aggregated_field_wells: Optional[BoxPlotAggregatedFieldWellsModel] = Field(
        default=None, alias="BoxPlotAggregatedFieldWells"
    )


class ComboChartFieldWellsModel(BaseModel):
    combo_chart_aggregated_field_wells: Optional[
        ComboChartAggregatedFieldWellsModel
    ] = Field(default=None, alias="ComboChartAggregatedFieldWells")


class FilledMapFieldWellsModel(BaseModel):
    filled_map_aggregated_field_wells: Optional[
        FilledMapAggregatedFieldWellsModel
    ] = Field(default=None, alias="FilledMapAggregatedFieldWells")


class FunnelChartFieldWellsModel(BaseModel):
    funnel_chart_aggregated_field_wells: Optional[
        FunnelChartAggregatedFieldWellsModel
    ] = Field(default=None, alias="FunnelChartAggregatedFieldWells")


class GaugeChartConfigurationModel(BaseModel):
    field_wells: Optional[GaugeChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    gauge_chart_options: Optional[GaugeChartOptionsModel] = Field(
        default=None, alias="GaugeChartOptions"
    )
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    tooltip_options: Optional[TooltipOptionsModel] = Field(
        default=None, alias="TooltipOptions"
    )
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class GeospatialMapFieldWellsModel(BaseModel):
    geospatial_map_aggregated_field_wells: Optional[
        GeospatialMapAggregatedFieldWellsModel
    ] = Field(default=None, alias="GeospatialMapAggregatedFieldWells")


class HeatMapFieldWellsModel(BaseModel):
    heat_map_aggregated_field_wells: Optional[HeatMapAggregatedFieldWellsModel] = Field(
        default=None, alias="HeatMapAggregatedFieldWells"
    )


class HistogramFieldWellsModel(BaseModel):
    histogram_aggregated_field_wells: Optional[
        HistogramAggregatedFieldWellsModel
    ] = Field(default=None, alias="HistogramAggregatedFieldWells")


class KPIConfigurationModel(BaseModel):
    field_wells: Optional[KPIFieldWellsModel] = Field(default=None, alias="FieldWells")
    sort_configuration: Optional[KPISortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    kp_ioptions: Optional[KPIOptionsModel] = Field(default=None, alias="KPIOptions")


class LineChartFieldWellsModel(BaseModel):
    line_chart_aggregated_field_wells: Optional[
        LineChartAggregatedFieldWellsModel
    ] = Field(default=None, alias="LineChartAggregatedFieldWells")


class PieChartFieldWellsModel(BaseModel):
    pie_chart_aggregated_field_wells: Optional[
        PieChartAggregatedFieldWellsModel
    ] = Field(default=None, alias="PieChartAggregatedFieldWells")


class PivotTableFieldWellsModel(BaseModel):
    pivot_table_aggregated_field_wells: Optional[
        PivotTableAggregatedFieldWellsModel
    ] = Field(default=None, alias="PivotTableAggregatedFieldWells")


class RadarChartFieldWellsModel(BaseModel):
    radar_chart_aggregated_field_wells: Optional[
        RadarChartAggregatedFieldWellsModel
    ] = Field(default=None, alias="RadarChartAggregatedFieldWells")


class SankeyDiagramFieldWellsModel(BaseModel):
    sankey_diagram_aggregated_field_wells: Optional[
        SankeyDiagramAggregatedFieldWellsModel
    ] = Field(default=None, alias="SankeyDiagramAggregatedFieldWells")


class ScatterPlotFieldWellsModel(BaseModel):
    scatter_plot_categorically_aggregated_field_wells: Optional[
        ScatterPlotCategoricallyAggregatedFieldWellsModel
    ] = Field(default=None, alias="ScatterPlotCategoricallyAggregatedFieldWells")
    scatter_plot_unaggregated_field_wells: Optional[
        ScatterPlotUnaggregatedFieldWellsModel
    ] = Field(default=None, alias="ScatterPlotUnaggregatedFieldWells")


class ComputationModel(BaseModel):
    top_bottom_ranked: Optional[TopBottomRankedComputationModel] = Field(
        default=None, alias="TopBottomRanked"
    )
    top_bottom_movers: Optional[TopBottomMoversComputationModel] = Field(
        default=None, alias="TopBottomMovers"
    )
    total_aggregation: Optional[TotalAggregationComputationModel] = Field(
        default=None, alias="TotalAggregation"
    )
    maximum_minimum: Optional[MaximumMinimumComputationModel] = Field(
        default=None, alias="MaximumMinimum"
    )
    metric_comparison: Optional[MetricComparisonComputationModel] = Field(
        default=None, alias="MetricComparison"
    )
    period_over_period: Optional[PeriodOverPeriodComputationModel] = Field(
        default=None, alias="PeriodOverPeriod"
    )
    period_to_date: Optional[PeriodToDateComputationModel] = Field(
        default=None, alias="PeriodToDate"
    )
    growth_rate: Optional[GrowthRateComputationModel] = Field(
        default=None, alias="GrowthRate"
    )
    unique_values: Optional[UniqueValuesComputationModel] = Field(
        default=None, alias="UniqueValues"
    )
    forecast: Optional[ForecastComputationModel] = Field(default=None, alias="Forecast")


class TreeMapFieldWellsModel(BaseModel):
    tree_map_aggregated_field_wells: Optional[TreeMapAggregatedFieldWellsModel] = Field(
        default=None, alias="TreeMapAggregatedFieldWells"
    )


class WaterfallChartFieldWellsModel(BaseModel):
    waterfall_chart_aggregated_field_wells: Optional[
        WaterfallChartAggregatedFieldWellsModel
    ] = Field(default=None, alias="WaterfallChartAggregatedFieldWells")


class WordCloudFieldWellsModel(BaseModel):
    word_cloud_aggregated_field_wells: Optional[
        WordCloudAggregatedFieldWellsModel
    ] = Field(default=None, alias="WordCloudAggregatedFieldWells")


class TableFieldWellsModel(BaseModel):
    table_aggregated_field_wells: Optional[TableAggregatedFieldWellsModel] = Field(
        default=None, alias="TableAggregatedFieldWells"
    )
    table_unaggregated_field_wells: Optional[TableUnaggregatedFieldWellsModel] = Field(
        default=None, alias="TableUnaggregatedFieldWells"
    )


class LayoutConfigurationModel(BaseModel):
    grid_layout: Optional[GridLayoutConfigurationModel] = Field(
        default=None, alias="GridLayout"
    )
    free_form_layout: Optional[FreeFormLayoutConfigurationModel] = Field(
        default=None, alias="FreeFormLayout"
    )
    section_based_layout: Optional[SectionBasedLayoutConfigurationModel] = Field(
        default=None, alias="SectionBasedLayout"
    )


class BarChartConfigurationModel(BaseModel):
    field_wells: Optional[BarChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[BarChartSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    orientation: Optional[Literal["HORIZONTAL", "VERTICAL"]] = Field(
        default=None, alias="Orientation"
    )
    bars_arrangement: Optional[
        Literal["CLUSTERED", "STACKED", "STACKED_PERCENT"]
    ] = Field(default=None, alias="BarsArrangement")
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )
    small_multiples_options: Optional[SmallMultiplesOptionsModel] = Field(
        default=None, alias="SmallMultiplesOptions"
    )
    category_axis: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="CategoryAxis"
    )
    category_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryLabelOptions"
    )
    value_axis: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="ValueAxis"
    )
    value_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ValueLabelOptions"
    )
    color_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ColorLabelOptions"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    reference_lines: Optional[Sequence[ReferenceLineModel]] = Field(
        default=None, alias="ReferenceLines"
    )
    contribution_analysis_defaults: Optional[
        Sequence[ContributionAnalysisDefaultModel]
    ] = Field(default=None, alias="ContributionAnalysisDefaults")


class BoxPlotChartConfigurationModel(BaseModel):
    field_wells: Optional[BoxPlotFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[BoxPlotSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    box_plot_options: Optional[BoxPlotOptionsModel] = Field(
        default=None, alias="BoxPlotOptions"
    )
    category_axis: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="CategoryAxis"
    )
    category_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryLabelOptions"
    )
    primary_yaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="PrimaryYAxisDisplayOptions"
    )
    primary_yaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="PrimaryYAxisLabelOptions"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    reference_lines: Optional[Sequence[ReferenceLineModel]] = Field(
        default=None, alias="ReferenceLines"
    )
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class ComboChartConfigurationModel(BaseModel):
    field_wells: Optional[ComboChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[ComboChartSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    bars_arrangement: Optional[
        Literal["CLUSTERED", "STACKED", "STACKED_PERCENT"]
    ] = Field(default=None, alias="BarsArrangement")
    category_axis: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="CategoryAxis"
    )
    category_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryLabelOptions"
    )
    primary_yaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="PrimaryYAxisDisplayOptions"
    )
    primary_yaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="PrimaryYAxisLabelOptions"
    )
    secondary_yaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="SecondaryYAxisDisplayOptions"
    )
    secondary_yaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="SecondaryYAxisLabelOptions"
    )
    color_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ColorLabelOptions"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    bar_data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="BarDataLabels"
    )
    line_data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="LineDataLabels"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    reference_lines: Optional[Sequence[ReferenceLineModel]] = Field(
        default=None, alias="ReferenceLines"
    )
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class FilledMapConfigurationModel(BaseModel):
    field_wells: Optional[FilledMapFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[FilledMapSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    window_options: Optional[GeospatialWindowOptionsModel] = Field(
        default=None, alias="WindowOptions"
    )
    map_style_options: Optional[GeospatialMapStyleOptionsModel] = Field(
        default=None, alias="MapStyleOptions"
    )


class FunnelChartConfigurationModel(BaseModel):
    field_wells: Optional[FunnelChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[FunnelChartSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    category_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryLabelOptions"
    )
    value_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ValueLabelOptions"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    data_label_options: Optional[FunnelChartDataLabelOptionsModel] = Field(
        default=None, alias="DataLabelOptions"
    )
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class GaugeChartVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[GaugeChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    conditional_formatting: Optional[GaugeChartConditionalFormattingModel] = Field(
        default=None, alias="ConditionalFormatting"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class GeospatialMapConfigurationModel(BaseModel):
    field_wells: Optional[GeospatialMapFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    window_options: Optional[GeospatialWindowOptionsModel] = Field(
        default=None, alias="WindowOptions"
    )
    map_style_options: Optional[GeospatialMapStyleOptionsModel] = Field(
        default=None, alias="MapStyleOptions"
    )
    point_style_options: Optional[GeospatialPointStyleOptionsModel] = Field(
        default=None, alias="PointStyleOptions"
    )
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class HeatMapConfigurationModel(BaseModel):
    field_wells: Optional[HeatMapFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[HeatMapSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    row_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="RowLabelOptions"
    )
    column_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ColumnLabelOptions"
    )
    color_scale: Optional[ColorScaleModel] = Field(default=None, alias="ColorScale")
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")


class HistogramConfigurationModel(BaseModel):
    field_wells: Optional[HistogramFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    xaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="XAxisDisplayOptions"
    )
    xaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="XAxisLabelOptions"
    )
    yaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="YAxisDisplayOptions"
    )
    bin_options: Optional[HistogramBinOptionsModel] = Field(
        default=None, alias="BinOptions"
    )
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class KPIVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[KPIConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    conditional_formatting: Optional[KPIConditionalFormattingModel] = Field(
        default=None, alias="ConditionalFormatting"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class LineChartConfigurationModel(BaseModel):
    field_wells: Optional[LineChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[LineChartSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    forecast_configurations: Optional[Sequence[ForecastConfigurationModel]] = Field(
        default=None, alias="ForecastConfigurations"
    )
    type: Optional[Literal["AREA", "LINE", "STACKED_AREA"]] = Field(
        default=None, alias="Type"
    )
    small_multiples_options: Optional[SmallMultiplesOptionsModel] = Field(
        default=None, alias="SmallMultiplesOptions"
    )
    xaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="XAxisDisplayOptions"
    )
    xaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="XAxisLabelOptions"
    )
    primary_yaxis_display_options: Optional[LineSeriesAxisDisplayOptionsModel] = Field(
        default=None, alias="PrimaryYAxisDisplayOptions"
    )
    primary_yaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="PrimaryYAxisLabelOptions"
    )
    secondary_yaxis_display_options: Optional[
        LineSeriesAxisDisplayOptionsModel
    ] = Field(default=None, alias="SecondaryYAxisDisplayOptions")
    secondary_yaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="SecondaryYAxisLabelOptions"
    )
    default_series_settings: Optional[LineChartDefaultSeriesSettingsModel] = Field(
        default=None, alias="DefaultSeriesSettings"
    )
    series: Optional[Sequence[SeriesItemModel]] = Field(default=None, alias="Series")
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    reference_lines: Optional[Sequence[ReferenceLineModel]] = Field(
        default=None, alias="ReferenceLines"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    contribution_analysis_defaults: Optional[
        Sequence[ContributionAnalysisDefaultModel]
    ] = Field(default=None, alias="ContributionAnalysisDefaults")
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class PieChartConfigurationModel(BaseModel):
    field_wells: Optional[PieChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[PieChartSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    donut_options: Optional[DonutOptionsModel] = Field(
        default=None, alias="DonutOptions"
    )
    small_multiples_options: Optional[SmallMultiplesOptionsModel] = Field(
        default=None, alias="SmallMultiplesOptions"
    )
    category_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryLabelOptions"
    )
    value_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ValueLabelOptions"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )
    contribution_analysis_defaults: Optional[
        Sequence[ContributionAnalysisDefaultModel]
    ] = Field(default=None, alias="ContributionAnalysisDefaults")


class PivotTableConfigurationModel(BaseModel):
    field_wells: Optional[PivotTableFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[PivotTableSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    table_options: Optional[PivotTableOptionsModel] = Field(
        default=None, alias="TableOptions"
    )
    total_options: Optional[PivotTableTotalOptionsModel] = Field(
        default=None, alias="TotalOptions"
    )
    field_options: Optional[PivotTableFieldOptionsModel] = Field(
        default=None, alias="FieldOptions"
    )
    paginated_report_options: Optional[PivotTablePaginatedReportOptionsModel] = Field(
        default=None, alias="PaginatedReportOptions"
    )


class RadarChartConfigurationModel(BaseModel):
    field_wells: Optional[RadarChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[RadarChartSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    shape: Optional[Literal["CIRCLE", "POLYGON"]] = Field(default=None, alias="Shape")
    base_series_settings: Optional[RadarChartSeriesSettingsModel] = Field(
        default=None, alias="BaseSeriesSettings"
    )
    start_angle: Optional[float] = Field(default=None, alias="StartAngle")
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )
    alternate_band_colors_visibility: Optional[Literal["HIDDEN", "VISIBLE"]] = Field(
        default=None, alias="AlternateBandColorsVisibility"
    )
    alternate_band_even_color: Optional[str] = Field(
        default=None, alias="AlternateBandEvenColor"
    )
    alternate_band_odd_color: Optional[str] = Field(
        default=None, alias="AlternateBandOddColor"
    )
    category_axis: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="CategoryAxis"
    )
    category_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryLabelOptions"
    )
    color_axis: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="ColorAxis"
    )
    color_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ColorLabelOptions"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")


class SankeyDiagramChartConfigurationModel(BaseModel):
    field_wells: Optional[SankeyDiagramFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[SankeyDiagramSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )


class ScatterPlotConfigurationModel(BaseModel):
    field_wells: Optional[ScatterPlotFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    xaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="XAxisLabelOptions"
    )
    xaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="XAxisDisplayOptions"
    )
    yaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="YAxisLabelOptions"
    )
    yaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="YAxisDisplayOptions"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class InsightConfigurationModel(BaseModel):
    computations: Optional[Sequence[ComputationModel]] = Field(
        default=None, alias="Computations"
    )
    custom_narrative: Optional[CustomNarrativeOptionsModel] = Field(
        default=None, alias="CustomNarrative"
    )


class TreeMapConfigurationModel(BaseModel):
    field_wells: Optional[TreeMapFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[TreeMapSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    group_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="GroupLabelOptions"
    )
    size_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="SizeLabelOptions"
    )
    color_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="ColorLabelOptions"
    )
    color_scale: Optional[ColorScaleModel] = Field(default=None, alias="ColorScale")
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    tooltip: Optional[TooltipOptionsModel] = Field(default=None, alias="Tooltip")


class WaterfallChartConfigurationModel(BaseModel):
    field_wells: Optional[WaterfallChartFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[WaterfallChartSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    waterfall_chart_options: Optional[WaterfallChartOptionsModel] = Field(
        default=None, alias="WaterfallChartOptions"
    )
    category_axis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryAxisLabelOptions"
    )
    category_axis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="CategoryAxisDisplayOptions"
    )
    primary_yaxis_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="PrimaryYAxisLabelOptions"
    )
    primary_yaxis_display_options: Optional[AxisDisplayOptionsModel] = Field(
        default=None, alias="PrimaryYAxisDisplayOptions"
    )
    legend: Optional[LegendOptionsModel] = Field(default=None, alias="Legend")
    data_labels: Optional[DataLabelOptionsModel] = Field(
        default=None, alias="DataLabels"
    )
    visual_palette: Optional[VisualPaletteModel] = Field(
        default=None, alias="VisualPalette"
    )


class WordCloudChartConfigurationModel(BaseModel):
    field_wells: Optional[WordCloudFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[WordCloudSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    category_label_options: Optional[ChartAxisLabelOptionsModel] = Field(
        default=None, alias="CategoryLabelOptions"
    )
    word_cloud_options: Optional[WordCloudOptionsModel] = Field(
        default=None, alias="WordCloudOptions"
    )


class TableConfigurationModel(BaseModel):
    field_wells: Optional[TableFieldWellsModel] = Field(
        default=None, alias="FieldWells"
    )
    sort_configuration: Optional[TableSortConfigurationModel] = Field(
        default=None, alias="SortConfiguration"
    )
    table_options: Optional[TableOptionsModel] = Field(
        default=None, alias="TableOptions"
    )
    total_options: Optional[TotalOptionsModel] = Field(
        default=None, alias="TotalOptions"
    )
    field_options: Optional[TableFieldOptionsModel] = Field(
        default=None, alias="FieldOptions"
    )
    paginated_report_options: Optional[TablePaginatedReportOptionsModel] = Field(
        default=None, alias="PaginatedReportOptions"
    )
    table_inline_visualizations: Optional[
        Sequence[TableInlineVisualizationModel]
    ] = Field(default=None, alias="TableInlineVisualizations")


class LayoutModel(BaseModel):
    configuration: LayoutConfigurationModel = Field(alias="Configuration")


class BarChartVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[BarChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class BoxPlotVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[BoxPlotChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class ComboChartVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[ComboChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class FilledMapVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[FilledMapConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    conditional_formatting: Optional[FilledMapConditionalFormattingModel] = Field(
        default=None, alias="ConditionalFormatting"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class FunnelChartVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[FunnelChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class GeospatialMapVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[GeospatialMapConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class HeatMapVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[HeatMapConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class HistogramVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[HistogramConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class LineChartVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[LineChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class PieChartVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[PieChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class PivotTableVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[PivotTableConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    conditional_formatting: Optional[PivotTableConditionalFormattingModel] = Field(
        default=None, alias="ConditionalFormatting"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class RadarChartVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[RadarChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class SankeyDiagramVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[SankeyDiagramChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class ScatterPlotVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[ScatterPlotConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class InsightVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    data_set_identifier: str = Field(alias="DataSetIdentifier")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    insight_configuration: Optional[InsightConfigurationModel] = Field(
        default=None, alias="InsightConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class TreeMapVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[TreeMapConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class WaterfallVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[WaterfallChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class WordCloudVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[WordCloudChartConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )
    column_hierarchies: Optional[Sequence[ColumnHierarchyModel]] = Field(
        default=None, alias="ColumnHierarchies"
    )


class TableVisualModel(BaseModel):
    visual_id: str = Field(alias="VisualId")
    title: Optional[VisualTitleLabelOptionsModel] = Field(default=None, alias="Title")
    subtitle: Optional[VisualSubtitleLabelOptionsModel] = Field(
        default=None, alias="Subtitle"
    )
    chart_configuration: Optional[TableConfigurationModel] = Field(
        default=None, alias="ChartConfiguration"
    )
    conditional_formatting: Optional[TableConditionalFormattingModel] = Field(
        default=None, alias="ConditionalFormatting"
    )
    actions: Optional[Sequence[VisualCustomActionModel]] = Field(
        default=None, alias="Actions"
    )


class VisualModel(BaseModel):
    table_visual: Optional[TableVisualModel] = Field(default=None, alias="TableVisual")
    pivot_table_visual: Optional[PivotTableVisualModel] = Field(
        default=None, alias="PivotTableVisual"
    )
    bar_chart_visual: Optional[BarChartVisualModel] = Field(
        default=None, alias="BarChartVisual"
    )
    kp_ivisual: Optional[KPIVisualModel] = Field(default=None, alias="KPIVisual")
    pie_chart_visual: Optional[PieChartVisualModel] = Field(
        default=None, alias="PieChartVisual"
    )
    gauge_chart_visual: Optional[GaugeChartVisualModel] = Field(
        default=None, alias="GaugeChartVisual"
    )
    line_chart_visual: Optional[LineChartVisualModel] = Field(
        default=None, alias="LineChartVisual"
    )
    heat_map_visual: Optional[HeatMapVisualModel] = Field(
        default=None, alias="HeatMapVisual"
    )
    tree_map_visual: Optional[TreeMapVisualModel] = Field(
        default=None, alias="TreeMapVisual"
    )
    geospatial_map_visual: Optional[GeospatialMapVisualModel] = Field(
        default=None, alias="GeospatialMapVisual"
    )
    filled_map_visual: Optional[FilledMapVisualModel] = Field(
        default=None, alias="FilledMapVisual"
    )
    funnel_chart_visual: Optional[FunnelChartVisualModel] = Field(
        default=None, alias="FunnelChartVisual"
    )
    scatter_plot_visual: Optional[ScatterPlotVisualModel] = Field(
        default=None, alias="ScatterPlotVisual"
    )
    combo_chart_visual: Optional[ComboChartVisualModel] = Field(
        default=None, alias="ComboChartVisual"
    )
    box_plot_visual: Optional[BoxPlotVisualModel] = Field(
        default=None, alias="BoxPlotVisual"
    )
    waterfall_visual: Optional[WaterfallVisualModel] = Field(
        default=None, alias="WaterfallVisual"
    )
    histogram_visual: Optional[HistogramVisualModel] = Field(
        default=None, alias="HistogramVisual"
    )
    word_cloud_visual: Optional[WordCloudVisualModel] = Field(
        default=None, alias="WordCloudVisual"
    )
    insight_visual: Optional[InsightVisualModel] = Field(
        default=None, alias="InsightVisual"
    )
    sankey_diagram_visual: Optional[SankeyDiagramVisualModel] = Field(
        default=None, alias="SankeyDiagramVisual"
    )
    custom_content_visual: Optional[CustomContentVisualModel] = Field(
        default=None, alias="CustomContentVisual"
    )
    empty_visual: Optional[EmptyVisualModel] = Field(default=None, alias="EmptyVisual")
    radar_chart_visual: Optional[RadarChartVisualModel] = Field(
        default=None, alias="RadarChartVisual"
    )


class SheetDefinitionModel(BaseModel):
    sheet_id: str = Field(alias="SheetId")
    title: Optional[str] = Field(default=None, alias="Title")
    description: Optional[str] = Field(default=None, alias="Description")
    name: Optional[str] = Field(default=None, alias="Name")
    parameter_controls: Optional[Sequence[ParameterControlModel]] = Field(
        default=None, alias="ParameterControls"
    )
    filter_controls: Optional[Sequence[FilterControlModel]] = Field(
        default=None, alias="FilterControls"
    )
    visuals: Optional[Sequence[VisualModel]] = Field(default=None, alias="Visuals")
    text_boxes: Optional[Sequence[SheetTextBoxModel]] = Field(
        default=None, alias="TextBoxes"
    )
    layouts: Optional[Sequence[LayoutModel]] = Field(default=None, alias="Layouts")
    sheet_control_layouts: Optional[Sequence[SheetControlLayoutModel]] = Field(
        default=None, alias="SheetControlLayouts"
    )
    content_type: Optional[Literal["INTERACTIVE", "PAGINATED"]] = Field(
        default=None, alias="ContentType"
    )


class AnalysisDefinitionModel(BaseModel):
    data_set_identifier_declarations: Sequence[
        DataSetIdentifierDeclarationModel
    ] = Field(alias="DataSetIdentifierDeclarations")
    sheets: Optional[Sequence[SheetDefinitionModel]] = Field(
        default=None, alias="Sheets"
    )
    calculated_fields: Optional[Sequence[CalculatedFieldModel]] = Field(
        default=None, alias="CalculatedFields"
    )
    parameter_declarations: Optional[Sequence[ParameterDeclarationModel]] = Field(
        default=None, alias="ParameterDeclarations"
    )
    filter_groups: Optional[Sequence[FilterGroupModel]] = Field(
        default=None, alias="FilterGroups"
    )
    column_configurations: Optional[Sequence[ColumnConfigurationModel]] = Field(
        default=None, alias="ColumnConfigurations"
    )
    analysis_defaults: Optional[AnalysisDefaultsModel] = Field(
        default=None, alias="AnalysisDefaults"
    )


class DashboardVersionDefinitionModel(BaseModel):
    data_set_identifier_declarations: Sequence[
        DataSetIdentifierDeclarationModel
    ] = Field(alias="DataSetIdentifierDeclarations")
    sheets: Optional[Sequence[SheetDefinitionModel]] = Field(
        default=None, alias="Sheets"
    )
    calculated_fields: Optional[Sequence[CalculatedFieldModel]] = Field(
        default=None, alias="CalculatedFields"
    )
    parameter_declarations: Optional[Sequence[ParameterDeclarationModel]] = Field(
        default=None, alias="ParameterDeclarations"
    )
    filter_groups: Optional[Sequence[FilterGroupModel]] = Field(
        default=None, alias="FilterGroups"
    )
    column_configurations: Optional[Sequence[ColumnConfigurationModel]] = Field(
        default=None, alias="ColumnConfigurations"
    )
    analysis_defaults: Optional[AnalysisDefaultsModel] = Field(
        default=None, alias="AnalysisDefaults"
    )


class TemplateVersionDefinitionModel(BaseModel):
    data_set_configurations: Sequence[DataSetConfigurationModel] = Field(
        alias="DataSetConfigurations"
    )
    sheets: Optional[Sequence[SheetDefinitionModel]] = Field(
        default=None, alias="Sheets"
    )
    calculated_fields: Optional[Sequence[CalculatedFieldModel]] = Field(
        default=None, alias="CalculatedFields"
    )
    parameter_declarations: Optional[Sequence[ParameterDeclarationModel]] = Field(
        default=None, alias="ParameterDeclarations"
    )
    filter_groups: Optional[Sequence[FilterGroupModel]] = Field(
        default=None, alias="FilterGroups"
    )
    column_configurations: Optional[Sequence[ColumnConfigurationModel]] = Field(
        default=None, alias="ColumnConfigurations"
    )
    analysis_defaults: Optional[AnalysisDefaultsModel] = Field(
        default=None, alias="AnalysisDefaults"
    )


class CreateAnalysisRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")
    name: str = Field(alias="Name")
    parameters: Optional[ParametersModel] = Field(default=None, alias="Parameters")
    permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )
    source_entity: Optional[AnalysisSourceEntityModel] = Field(
        default=None, alias="SourceEntity"
    )
    theme_arn: Optional[str] = Field(default=None, alias="ThemeArn")
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    definition: Optional[AnalysisDefinitionModel] = Field(
        default=None, alias="Definition"
    )


class DescribeAnalysisDefinitionResponseModel(BaseModel):
    analysis_id: str = Field(alias="AnalysisId")
    name: str = Field(alias="Name")
    errors: List[AnalysisErrorModel] = Field(alias="Errors")
    resource_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="ResourceStatus")
    theme_arn: str = Field(alias="ThemeArn")
    definition: AnalysisDefinitionModel = Field(alias="Definition")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateAnalysisRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    analysis_id: str = Field(alias="AnalysisId")
    name: str = Field(alias="Name")
    parameters: Optional[ParametersModel] = Field(default=None, alias="Parameters")
    source_entity: Optional[AnalysisSourceEntityModel] = Field(
        default=None, alias="SourceEntity"
    )
    theme_arn: Optional[str] = Field(default=None, alias="ThemeArn")
    definition: Optional[AnalysisDefinitionModel] = Field(
        default=None, alias="Definition"
    )


class CreateDashboardRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    name: str = Field(alias="Name")
    parameters: Optional[ParametersModel] = Field(default=None, alias="Parameters")
    permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )
    source_entity: Optional[DashboardSourceEntityModel] = Field(
        default=None, alias="SourceEntity"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    version_description: Optional[str] = Field(default=None, alias="VersionDescription")
    dashboard_publish_options: Optional[DashboardPublishOptionsModel] = Field(
        default=None, alias="DashboardPublishOptions"
    )
    theme_arn: Optional[str] = Field(default=None, alias="ThemeArn")
    definition: Optional[DashboardVersionDefinitionModel] = Field(
        default=None, alias="Definition"
    )


class DescribeDashboardDefinitionResponseModel(BaseModel):
    dashboard_id: str = Field(alias="DashboardId")
    errors: List[DashboardErrorModel] = Field(alias="Errors")
    name: str = Field(alias="Name")
    resource_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="ResourceStatus")
    theme_arn: str = Field(alias="ThemeArn")
    definition: DashboardVersionDefinitionModel = Field(alias="Definition")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    dashboard_publish_options: DashboardPublishOptionsModel = Field(
        alias="DashboardPublishOptions"
    )
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateDashboardRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    dashboard_id: str = Field(alias="DashboardId")
    name: str = Field(alias="Name")
    source_entity: Optional[DashboardSourceEntityModel] = Field(
        default=None, alias="SourceEntity"
    )
    parameters: Optional[ParametersModel] = Field(default=None, alias="Parameters")
    version_description: Optional[str] = Field(default=None, alias="VersionDescription")
    dashboard_publish_options: Optional[DashboardPublishOptionsModel] = Field(
        default=None, alias="DashboardPublishOptions"
    )
    theme_arn: Optional[str] = Field(default=None, alias="ThemeArn")
    definition: Optional[DashboardVersionDefinitionModel] = Field(
        default=None, alias="Definition"
    )


class CreateTemplateRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    name: Optional[str] = Field(default=None, alias="Name")
    permissions: Optional[Sequence[ResourcePermissionModel]] = Field(
        default=None, alias="Permissions"
    )
    source_entity: Optional[TemplateSourceEntityModel] = Field(
        default=None, alias="SourceEntity"
    )
    tags: Optional[Sequence[TagModel]] = Field(default=None, alias="Tags")
    version_description: Optional[str] = Field(default=None, alias="VersionDescription")
    definition: Optional[TemplateVersionDefinitionModel] = Field(
        default=None, alias="Definition"
    )


class DescribeTemplateDefinitionResponseModel(BaseModel):
    name: str = Field(alias="Name")
    template_id: str = Field(alias="TemplateId")
    errors: List[TemplateErrorModel] = Field(alias="Errors")
    resource_status: Literal[
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "CREATION_SUCCESSFUL",
        "DELETED",
        "UPDATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
    ] = Field(alias="ResourceStatus")
    theme_arn: str = Field(alias="ThemeArn")
    definition: TemplateVersionDefinitionModel = Field(alias="Definition")
    status: int = Field(alias="Status")
    request_id: str = Field(alias="RequestId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateTemplateRequestModel(BaseModel):
    aws_account_id: str = Field(alias="AwsAccountId")
    template_id: str = Field(alias="TemplateId")
    source_entity: Optional[TemplateSourceEntityModel] = Field(
        default=None, alias="SourceEntity"
    )
    version_description: Optional[str] = Field(default=None, alias="VersionDescription")
    name: Optional[str] = Field(default=None, alias="Name")
    definition: Optional[TemplateVersionDefinitionModel] = Field(
        default=None, alias="Definition"
    )
