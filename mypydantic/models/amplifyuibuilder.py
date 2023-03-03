# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Mapping, Optional, Sequence

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class MutationActionSetStateParameterModel(BaseModel):
    component_name: str = Field(alias="componentName")
    property: str = Field(alias="property")
    set: ComponentPropertyModel = Field(alias="set")


class ComponentBindingPropertiesValuePropertiesModel(BaseModel):
    bucket: Optional[str] = Field(default=None, alias="bucket")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    field: Optional[str] = Field(default=None, alias="field")
    key: Optional[str] = Field(default=None, alias="key")
    model: Optional[str] = Field(default=None, alias="model")
    predicates: Optional[Sequence[PredicateModel]] = Field(
        default=None, alias="predicates"
    )
    slot_name: Optional[str] = Field(default=None, alias="slotName")
    user_attribute: Optional[str] = Field(default=None, alias="userAttribute")


class ComponentConditionPropertyModel(BaseModel):
    else_: Optional[ComponentPropertyModel] = Field(default=None, alias="else")
    field: Optional[str] = Field(default=None, alias="field")
    operand: Optional[str] = Field(default=None, alias="operand")
    operand_type: Optional[str] = Field(default=None, alias="operandType")
    operator: Optional[str] = Field(default=None, alias="operator")
    property: Optional[str] = Field(default=None, alias="property")
    then: Optional[ComponentPropertyModel] = Field(default=None, alias="then")


class SortPropertyModel(BaseModel):
    direction: Literal["ASC", "DESC"] = Field(alias="direction")
    field: str = Field(alias="field")


class ComponentPropertyBindingPropertiesModel(BaseModel):
    property: str = Field(alias="property")
    field: Optional[str] = Field(default=None, alias="field")


class FormBindingElementModel(BaseModel):
    element: str = Field(alias="element")
    property: str = Field(alias="property")


class ComponentSummaryModel(BaseModel):
    app_id: str = Field(alias="appId")
    component_type: str = Field(alias="componentType")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    name: str = Field(alias="name")


class ComponentVariantModel(BaseModel):
    overrides: Optional[Mapping[str, Mapping[str, str]]] = Field(
        default=None, alias="overrides"
    )
    variant_values: Optional[Mapping[str, str]] = Field(
        default=None, alias="variantValues"
    )


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class FormDataTypeConfigModel(BaseModel):
    data_source_type: Literal["Custom", "DataStore"] = Field(alias="dataSourceType")
    data_type_name: str = Field(alias="dataTypeName")


class CreateThemeDataModel(BaseModel):
    name: str = Field(alias="name")
    values: Sequence[ThemeValuesModel] = Field(alias="values")
    overrides: Optional[Sequence[ThemeValuesModel]] = Field(
        default=None, alias="overrides"
    )
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class ThemeModel(BaseModel):
    app_id: str = Field(alias="appId")
    created_at: datetime = Field(alias="createdAt")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    values: List[ThemeValuesModel] = Field(alias="values")
    modified_at: Optional[datetime] = Field(default=None, alias="modifiedAt")
    overrides: Optional[List[ThemeValuesModel]] = Field(default=None, alias="overrides")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class DeleteComponentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")


class DeleteFormRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")


class DeleteThemeRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")


class ExchangeCodeForTokenRequestBodyModel(BaseModel):
    code: str = Field(alias="code")
    redirect_uri: str = Field(alias="redirectUri")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class ExportComponentsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ExportFormsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ExportThemesRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class FieldPositionModel(BaseModel):
    below: Optional[str] = Field(default=None, alias="below")
    fixed: Optional[Literal["first"]] = Field(default=None, alias="fixed")
    right_of: Optional[str] = Field(default=None, alias="rightOf")


class FieldValidationConfigurationModel(BaseModel):
    type: str = Field(alias="type")
    num_values: Optional[Sequence[int]] = Field(default=None, alias="numValues")
    str_values: Optional[Sequence[str]] = Field(default=None, alias="strValues")
    validation_message: Optional[str] = Field(default=None, alias="validationMessage")


class FormInputValuePropertyModel(BaseModel):
    value: Optional[str] = Field(default=None, alias="value")


class FormStyleConfigModel(BaseModel):
    token_reference: Optional[str] = Field(default=None, alias="tokenReference")
    value: Optional[str] = Field(default=None, alias="value")


class GetComponentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")


class GetFormRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")


class GetMetadataRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")


class GetThemeRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")


class ListComponentsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListFormsRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ListThemesRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    max_results: Optional[int] = Field(default=None, alias="maxResults")
    next_token: Optional[str] = Field(default=None, alias="nextToken")


class ThemeSummaryModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    name: str = Field(alias="name")


class PredicateModel(BaseModel):
    and_: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="and")
    field: Optional[str] = Field(default=None, alias="field")
    operand: Optional[str] = Field(default=None, alias="operand")
    operator: Optional[str] = Field(default=None, alias="operator")
    or_: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="or")


class PutMetadataFlagBodyModel(BaseModel):
    new_value: str = Field(alias="newValue")


class RefreshTokenRequestBodyModel(BaseModel):
    token: str = Field(alias="token")


class ThemeValueModel(BaseModel):
    children: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="children")
    value: Optional[str] = Field(default=None, alias="value")


class ThemeValuesModel(BaseModel):
    key: Optional[str] = Field(default=None, alias="key")
    value: Optional[Dict[str, Any]] = Field(default=None, alias="value")


class UpdateThemeDataModel(BaseModel):
    values: Sequence[ThemeValuesModel] = Field(alias="values")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    overrides: Optional[Sequence[ThemeValuesModel]] = Field(
        default=None, alias="overrides"
    )


class ActionParametersModel(BaseModel):
    anchor: Optional[ComponentPropertyModel] = Field(default=None, alias="anchor")
    fields: Optional[Mapping[str, ComponentPropertyModel]] = Field(
        default=None, alias="fields"
    )
    global_: Optional[ComponentPropertyModel] = Field(default=None, alias="global")
    id: Optional[ComponentPropertyModel] = Field(default=None, alias="id")
    model: Optional[str] = Field(default=None, alias="model")
    state: Optional[MutationActionSetStateParameterModel] = Field(
        default=None, alias="state"
    )
    target: Optional[ComponentPropertyModel] = Field(default=None, alias="target")
    type: Optional[ComponentPropertyModel] = Field(default=None, alias="type")
    url: Optional[ComponentPropertyModel] = Field(default=None, alias="url")


class ComponentBindingPropertiesValueModel(BaseModel):
    binding_properties: Optional[
        ComponentBindingPropertiesValuePropertiesModel
    ] = Field(default=None, alias="bindingProperties")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    type: Optional[str] = Field(default=None, alias="type")


class ComponentDataConfigurationModel(BaseModel):
    model: str = Field(alias="model")
    identifiers: Optional[Sequence[str]] = Field(default=None, alias="identifiers")
    predicate: Optional[PredicateModel] = Field(default=None, alias="predicate")
    sort: Optional[Sequence[SortPropertyModel]] = Field(default=None, alias="sort")


class ComponentPropertyModel(BaseModel):
    binding_properties: Optional[ComponentPropertyBindingPropertiesModel] = Field(
        default=None, alias="bindingProperties"
    )
    bindings: Optional[Mapping[str, FormBindingElementModel]] = Field(
        default=None, alias="bindings"
    )
    collection_binding_properties: Optional[
        ComponentPropertyBindingPropertiesModel
    ] = Field(default=None, alias="collectionBindingProperties")
    component_name: Optional[str] = Field(default=None, alias="componentName")
    concat: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="concat")
    condition: Optional[Dict[str, Any]] = Field(default=None, alias="condition")
    configured: Optional[bool] = Field(default=None, alias="configured")
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    event: Optional[str] = Field(default=None, alias="event")
    imported_value: Optional[str] = Field(default=None, alias="importedValue")
    model: Optional[str] = Field(default=None, alias="model")
    property: Optional[str] = Field(default=None, alias="property")
    type: Optional[str] = Field(default=None, alias="type")
    user_attribute: Optional[str] = Field(default=None, alias="userAttribute")
    value: Optional[str] = Field(default=None, alias="value")


class EmptyResponseMetadataModel(BaseModel):
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExchangeCodeForTokenResponseModel(BaseModel):
    access_token: str = Field(alias="accessToken")
    expires_in: int = Field(alias="expiresIn")
    refresh_token: str = Field(alias="refreshToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetMetadataResponseModel(BaseModel):
    features: Dict[str, str] = Field(alias="features")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ListComponentsResponseModel(BaseModel):
    entities: List[ComponentSummaryModel] = Field(alias="entities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class RefreshTokenResponseModel(BaseModel):
    access_token: str = Field(alias="accessToken")
    expires_in: int = Field(alias="expiresIn")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FormSummaryModel(BaseModel):
    app_id: str = Field(alias="appId")
    data_type: FormDataTypeConfigModel = Field(alias="dataType")
    environment_name: str = Field(alias="environmentName")
    form_action_type: Literal["create", "update"] = Field(alias="formActionType")
    id: str = Field(alias="id")
    name: str = Field(alias="name")


class CreateThemeRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    theme_to_create: CreateThemeDataModel = Field(alias="themeToCreate")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class CreateThemeResponseModel(BaseModel):
    entity: ThemeModel = Field(alias="entity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportThemesResponseModel(BaseModel):
    entities: List[ThemeModel] = Field(alias="entities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetThemeResponseModel(BaseModel):
    theme: ThemeModel = Field(alias="theme")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateThemeResponseModel(BaseModel):
    entity: ThemeModel = Field(alias="entity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExchangeCodeForTokenRequestModel(BaseModel):
    provider: Literal["figma"] = Field(alias="provider")
    request: ExchangeCodeForTokenRequestBodyModel = Field(alias="request")


class ExportComponentsRequestExportComponentsPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ExportFormsRequestExportFormsPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ExportThemesRequestExportThemesPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListComponentsRequestListComponentsPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListFormsRequestListFormsPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class ListThemesRequestListThemesPaginateModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class FormButtonModel(BaseModel):
    children: Optional[str] = Field(default=None, alias="children")
    excluded: Optional[bool] = Field(default=None, alias="excluded")
    position: Optional[FieldPositionModel] = Field(default=None, alias="position")


class SectionalElementModel(BaseModel):
    type: str = Field(alias="type")
    level: Optional[int] = Field(default=None, alias="level")
    orientation: Optional[str] = Field(default=None, alias="orientation")
    position: Optional[FieldPositionModel] = Field(default=None, alias="position")
    text: Optional[str] = Field(default=None, alias="text")


class ValueMappingModel(BaseModel):
    value: FormInputValuePropertyModel = Field(alias="value")
    display_value: Optional[FormInputValuePropertyModel] = Field(
        default=None, alias="displayValue"
    )


class FormStyleModel(BaseModel):
    horizontal_gap: Optional[FormStyleConfigModel] = Field(
        default=None, alias="horizontalGap"
    )
    outer_padding: Optional[FormStyleConfigModel] = Field(
        default=None, alias="outerPadding"
    )
    vertical_gap: Optional[FormStyleConfigModel] = Field(
        default=None, alias="verticalGap"
    )


class ListThemesResponseModel(BaseModel):
    entities: List[ThemeSummaryModel] = Field(alias="entities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class PutMetadataFlagRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    body: PutMetadataFlagBodyModel = Field(alias="body")
    environment_name: str = Field(alias="environmentName")
    feature_name: str = Field(alias="featureName")


class RefreshTokenRequestModel(BaseModel):
    provider: Literal["figma"] = Field(alias="provider")
    refresh_token_body: RefreshTokenRequestBodyModel = Field(alias="refreshTokenBody")


class UpdateThemeRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    updated_theme: UpdateThemeDataModel = Field(alias="updatedTheme")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class ComponentEventModel(BaseModel):
    action: Optional[str] = Field(default=None, alias="action")
    binding_event: Optional[str] = Field(default=None, alias="bindingEvent")
    parameters: Optional[ActionParametersModel] = Field(
        default=None, alias="parameters"
    )


class ListFormsResponseModel(BaseModel):
    entities: List[FormSummaryModel] = Field(alias="entities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class FormCTAModel(BaseModel):
    cancel: Optional[FormButtonModel] = Field(default=None, alias="cancel")
    clear: Optional[FormButtonModel] = Field(default=None, alias="clear")
    position: Optional[Literal["bottom", "top", "top_and_bottom"]] = Field(
        default=None, alias="position"
    )
    submit: Optional[FormButtonModel] = Field(default=None, alias="submit")


class ValueMappingsModel(BaseModel):
    values: Sequence[ValueMappingModel] = Field(alias="values")


class ComponentChildModel(BaseModel):
    component_type: str = Field(alias="componentType")
    name: str = Field(alias="name")
    properties: Mapping[str, ComponentPropertyModel] = Field(alias="properties")
    children: Optional[Sequence[Dict[str, Any]]] = Field(default=None, alias="children")
    events: Optional[Mapping[str, ComponentEventModel]] = Field(
        default=None, alias="events"
    )
    source_id: Optional[str] = Field(default=None, alias="sourceId")


class ComponentModel(BaseModel):
    app_id: str = Field(alias="appId")
    binding_properties: Dict[str, ComponentBindingPropertiesValueModel] = Field(
        alias="bindingProperties"
    )
    component_type: str = Field(alias="componentType")
    created_at: datetime = Field(alias="createdAt")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    overrides: Dict[str, Dict[str, str]] = Field(alias="overrides")
    properties: Dict[str, ComponentPropertyModel] = Field(alias="properties")
    variants: List[ComponentVariantModel] = Field(alias="variants")
    children: Optional[List[ComponentChildModel]] = Field(
        default=None, alias="children"
    )
    collection_properties: Optional[Dict[str, ComponentDataConfigurationModel]] = Field(
        default=None, alias="collectionProperties"
    )
    events: Optional[Dict[str, ComponentEventModel]] = Field(
        default=None, alias="events"
    )
    modified_at: Optional[datetime] = Field(default=None, alias="modifiedAt")
    schema_version: Optional[str] = Field(default=None, alias="schemaVersion")
    source_id: Optional[str] = Field(default=None, alias="sourceId")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class CreateComponentDataModel(BaseModel):
    binding_properties: Mapping[str, ComponentBindingPropertiesValueModel] = Field(
        alias="bindingProperties"
    )
    component_type: str = Field(alias="componentType")
    name: str = Field(alias="name")
    overrides: Mapping[str, Mapping[str, str]] = Field(alias="overrides")
    properties: Mapping[str, ComponentPropertyModel] = Field(alias="properties")
    variants: Sequence[ComponentVariantModel] = Field(alias="variants")
    children: Optional[Sequence[ComponentChildModel]] = Field(
        default=None, alias="children"
    )
    collection_properties: Optional[
        Mapping[str, ComponentDataConfigurationModel]
    ] = Field(default=None, alias="collectionProperties")
    events: Optional[Mapping[str, ComponentEventModel]] = Field(
        default=None, alias="events"
    )
    schema_version: Optional[str] = Field(default=None, alias="schemaVersion")
    source_id: Optional[str] = Field(default=None, alias="sourceId")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class UpdateComponentDataModel(BaseModel):
    binding_properties: Optional[
        Mapping[str, ComponentBindingPropertiesValueModel]
    ] = Field(default=None, alias="bindingProperties")
    children: Optional[Sequence[ComponentChildModel]] = Field(
        default=None, alias="children"
    )
    collection_properties: Optional[
        Mapping[str, ComponentDataConfigurationModel]
    ] = Field(default=None, alias="collectionProperties")
    component_type: Optional[str] = Field(default=None, alias="componentType")
    events: Optional[Mapping[str, ComponentEventModel]] = Field(
        default=None, alias="events"
    )
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    overrides: Optional[Mapping[str, Mapping[str, str]]] = Field(
        default=None, alias="overrides"
    )
    properties: Optional[Mapping[str, ComponentPropertyModel]] = Field(
        default=None, alias="properties"
    )
    schema_version: Optional[str] = Field(default=None, alias="schemaVersion")
    source_id: Optional[str] = Field(default=None, alias="sourceId")
    variants: Optional[Sequence[ComponentVariantModel]] = Field(
        default=None, alias="variants"
    )


class FieldInputConfigModel(BaseModel):
    type: str = Field(alias="type")
    default_checked: Optional[bool] = Field(default=None, alias="defaultChecked")
    default_country_code: Optional[str] = Field(
        default=None, alias="defaultCountryCode"
    )
    default_value: Optional[str] = Field(default=None, alias="defaultValue")
    descriptive_text: Optional[str] = Field(default=None, alias="descriptiveText")
    is_array: Optional[bool] = Field(default=None, alias="isArray")
    max_value: Optional[float] = Field(default=None, alias="maxValue")
    min_value: Optional[float] = Field(default=None, alias="minValue")
    name: Optional[str] = Field(default=None, alias="name")
    placeholder: Optional[str] = Field(default=None, alias="placeholder")
    read_only: Optional[bool] = Field(default=None, alias="readOnly")
    required: Optional[bool] = Field(default=None, alias="required")
    step: Optional[float] = Field(default=None, alias="step")
    value: Optional[str] = Field(default=None, alias="value")
    value_mappings: Optional[ValueMappingsModel] = Field(
        default=None, alias="valueMappings"
    )


class CreateComponentResponseModel(BaseModel):
    entity: ComponentModel = Field(alias="entity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportComponentsResponseModel(BaseModel):
    entities: List[ComponentModel] = Field(alias="entities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetComponentResponseModel(BaseModel):
    component: ComponentModel = Field(alias="component")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateComponentResponseModel(BaseModel):
    entity: ComponentModel = Field(alias="entity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class CreateComponentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    component_to_create: CreateComponentDataModel = Field(alias="componentToCreate")
    environment_name: str = Field(alias="environmentName")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class UpdateComponentRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    updated_component: UpdateComponentDataModel = Field(alias="updatedComponent")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class FieldConfigModel(BaseModel):
    excluded: Optional[bool] = Field(default=None, alias="excluded")
    input_type: Optional[FieldInputConfigModel] = Field(default=None, alias="inputType")
    label: Optional[str] = Field(default=None, alias="label")
    position: Optional[FieldPositionModel] = Field(default=None, alias="position")
    validations: Optional[Sequence[FieldValidationConfigurationModel]] = Field(
        default=None, alias="validations"
    )


class CreateFormDataModel(BaseModel):
    data_type: FormDataTypeConfigModel = Field(alias="dataType")
    fields: Mapping[str, FieldConfigModel] = Field(alias="fields")
    form_action_type: Literal["create", "update"] = Field(alias="formActionType")
    name: str = Field(alias="name")
    schema_version: str = Field(alias="schemaVersion")
    sectional_elements: Mapping[str, SectionalElementModel] = Field(
        alias="sectionalElements"
    )
    style: FormStyleModel = Field(alias="style")
    cta: Optional[FormCTAModel] = Field(default=None, alias="cta")
    tags: Optional[Mapping[str, str]] = Field(default=None, alias="tags")


class FormModel(BaseModel):
    app_id: str = Field(alias="appId")
    data_type: FormDataTypeConfigModel = Field(alias="dataType")
    environment_name: str = Field(alias="environmentName")
    fields: Dict[str, FieldConfigModel] = Field(alias="fields")
    form_action_type: Literal["create", "update"] = Field(alias="formActionType")
    id: str = Field(alias="id")
    name: str = Field(alias="name")
    schema_version: str = Field(alias="schemaVersion")
    sectional_elements: Dict[str, SectionalElementModel] = Field(
        alias="sectionalElements"
    )
    style: FormStyleModel = Field(alias="style")
    cta: Optional[FormCTAModel] = Field(default=None, alias="cta")
    tags: Optional[Dict[str, str]] = Field(default=None, alias="tags")


class UpdateFormDataModel(BaseModel):
    cta: Optional[FormCTAModel] = Field(default=None, alias="cta")
    data_type: Optional[FormDataTypeConfigModel] = Field(default=None, alias="dataType")
    fields: Optional[Mapping[str, FieldConfigModel]] = Field(
        default=None, alias="fields"
    )
    form_action_type: Optional[Literal["create", "update"]] = Field(
        default=None, alias="formActionType"
    )
    name: Optional[str] = Field(default=None, alias="name")
    schema_version: Optional[str] = Field(default=None, alias="schemaVersion")
    sectional_elements: Optional[Mapping[str, SectionalElementModel]] = Field(
        default=None, alias="sectionalElements"
    )
    style: Optional[FormStyleModel] = Field(default=None, alias="style")


class CreateFormRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    form_to_create: CreateFormDataModel = Field(alias="formToCreate")
    client_token: Optional[str] = Field(default=None, alias="clientToken")


class CreateFormResponseModel(BaseModel):
    entity: FormModel = Field(alias="entity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExportFormsResponseModel(BaseModel):
    entities: List[FormModel] = Field(alias="entities")
    next_token: str = Field(alias="nextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class GetFormResponseModel(BaseModel):
    form: FormModel = Field(alias="form")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFormResponseModel(BaseModel):
    entity: FormModel = Field(alias="entity")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateFormRequestModel(BaseModel):
    app_id: str = Field(alias="appId")
    environment_name: str = Field(alias="environmentName")
    id: str = Field(alias="id")
    updated_form: UpdateFormDataModel = Field(alias="updatedForm")
    client_token: Optional[str] = Field(default=None, alias="clientToken")
