# Model Generated: Thu Mar  2 21:56:16 2023

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Literal, Mapping, Optional, Sequence, Union

from pydantic import Field

from mypydantic.models.base_model import BaseModel


class ActionThresholdModel(BaseModel):
    action_threshold_value: float = Field(alias="ActionThresholdValue")
    action_threshold_type: Literal["ABSOLUTE_VALUE", "PERCENTAGE"] = Field(
        alias="ActionThresholdType"
    )


class SubscriberModel(BaseModel):
    subscription_type: Literal["EMAIL", "SNS"] = Field(alias="SubscriptionType")
    address: str = Field(alias="Address")


class HistoricalOptionsModel(BaseModel):
    budget_adjustment_period: int = Field(alias="BudgetAdjustmentPeriod")
    look_back_available_periods: Optional[int] = Field(
        default=None, alias="LookBackAvailablePeriods"
    )


class NotificationModel(BaseModel):
    notification_type: Literal["ACTUAL", "FORECASTED"] = Field(alias="NotificationType")
    comparison_operator: Literal["EQUAL_TO", "GREATER_THAN", "LESS_THAN"] = Field(
        alias="ComparisonOperator"
    )
    threshold: float = Field(alias="Threshold")
    threshold_type: Optional[Literal["ABSOLUTE_VALUE", "PERCENTAGE"]] = Field(
        default=None, alias="ThresholdType"
    )
    notification_state: Optional[Literal["ALARM", "OK"]] = Field(
        default=None, alias="NotificationState"
    )


class CostTypesModel(BaseModel):
    include_tax: Optional[bool] = Field(default=None, alias="IncludeTax")
    include_subscription: Optional[bool] = Field(
        default=None, alias="IncludeSubscription"
    )
    use_blended: Optional[bool] = Field(default=None, alias="UseBlended")
    include_refund: Optional[bool] = Field(default=None, alias="IncludeRefund")
    include_credit: Optional[bool] = Field(default=None, alias="IncludeCredit")
    include_upfront: Optional[bool] = Field(default=None, alias="IncludeUpfront")
    include_recurring: Optional[bool] = Field(default=None, alias="IncludeRecurring")
    include_other_subscription: Optional[bool] = Field(
        default=None, alias="IncludeOtherSubscription"
    )
    include_support: Optional[bool] = Field(default=None, alias="IncludeSupport")
    include_discount: Optional[bool] = Field(default=None, alias="IncludeDiscount")
    use_amortized: Optional[bool] = Field(default=None, alias="UseAmortized")


class SpendModel(BaseModel):
    amount: str = Field(alias="Amount")
    unit: str = Field(alias="Unit")


class TimePeriodModel(BaseModel):
    start: Optional[Union[datetime, str]] = Field(default=None, alias="Start")
    end: Optional[Union[datetime, str]] = Field(default=None, alias="End")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class IamActionDefinitionModel(BaseModel):
    policy_arn: str = Field(alias="PolicyArn")
    roles: Optional[Sequence[str]] = Field(default=None, alias="Roles")
    groups: Optional[Sequence[str]] = Field(default=None, alias="Groups")
    users: Optional[Sequence[str]] = Field(default=None, alias="Users")


class ScpActionDefinitionModel(BaseModel):
    policy_id: str = Field(alias="PolicyId")
    target_ids: Sequence[str] = Field(alias="TargetIds")


class SsmActionDefinitionModel(BaseModel):
    action_sub_type: Literal["STOP_EC2_INSTANCES", "STOP_RDS_INSTANCES"] = Field(
        alias="ActionSubType"
    )
    region: str = Field(alias="Region")
    instance_ids: Sequence[str] = Field(alias="InstanceIds")


class DeleteBudgetActionRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")


class DeleteBudgetRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")


class PaginatorConfigModel(BaseModel):
    max_items: Optional[int] = Field(default=None, alias="MaxItems")
    page_size: Optional[int] = Field(default=None, alias="PageSize")
    starting_token: Optional[str] = Field(default=None, alias="StartingToken")


class DescribeBudgetActionRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")


class DescribeBudgetActionsForAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeBudgetActionsForBudgetRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeBudgetNotificationsForAccountRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeBudgetRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")


class DescribeBudgetsRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeNotificationsForBudgetRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class ExecuteBudgetActionRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")
    execution_type: Literal[
        "APPROVE_BUDGET_ACTION",
        "RESET_BUDGET_ACTION",
        "RETRY_BUDGET_ACTION",
        "REVERSE_BUDGET_ACTION",
    ] = Field(alias="ExecutionType")


class AutoAdjustDataModel(BaseModel):
    auto_adjust_type: Literal["FORECAST", "HISTORICAL"] = Field(alias="AutoAdjustType")
    historical_options: Optional[HistoricalOptionsModel] = Field(
        default=None, alias="HistoricalOptions"
    )
    last_auto_adjust_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastAutoAdjustTime"
    )


class BudgetNotificationsForAccountModel(BaseModel):
    notifications: Optional[List[NotificationModel]] = Field(
        default=None, alias="Notifications"
    )
    budget_name: Optional[str] = Field(default=None, alias="BudgetName")


class CreateNotificationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification: NotificationModel = Field(alias="Notification")
    subscribers: Sequence[SubscriberModel] = Field(alias="Subscribers")


class CreateSubscriberRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification: NotificationModel = Field(alias="Notification")
    subscriber: SubscriberModel = Field(alias="Subscriber")


class DeleteNotificationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification: NotificationModel = Field(alias="Notification")


class DeleteSubscriberRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification: NotificationModel = Field(alias="Notification")
    subscriber: SubscriberModel = Field(alias="Subscriber")


class DescribeSubscribersForNotificationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification: NotificationModel = Field(alias="Notification")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class NotificationWithSubscribersModel(BaseModel):
    notification: NotificationModel = Field(alias="Notification")
    subscribers: Sequence[SubscriberModel] = Field(alias="Subscribers")


class UpdateNotificationRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    old_notification: NotificationModel = Field(alias="OldNotification")
    new_notification: NotificationModel = Field(alias="NewNotification")


class UpdateSubscriberRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification: NotificationModel = Field(alias="Notification")
    old_subscriber: SubscriberModel = Field(alias="OldSubscriber")
    new_subscriber: SubscriberModel = Field(alias="NewSubscriber")


class CalculatedSpendModel(BaseModel):
    actual_spend: SpendModel = Field(alias="ActualSpend")
    forecasted_spend: Optional[SpendModel] = Field(
        default=None, alias="ForecastedSpend"
    )


class BudgetedAndActualAmountsModel(BaseModel):
    budgeted_amount: Optional[SpendModel] = Field(default=None, alias="BudgetedAmount")
    actual_amount: Optional[SpendModel] = Field(default=None, alias="ActualAmount")
    time_period: Optional[TimePeriodModel] = Field(default=None, alias="TimePeriod")


class DescribeBudgetActionHistoriesRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")
    time_period: Optional[TimePeriodModel] = Field(default=None, alias="TimePeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class DescribeBudgetPerformanceHistoryRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    time_period: Optional[TimePeriodModel] = Field(default=None, alias="TimePeriod")
    max_results: Optional[int] = Field(default=None, alias="MaxResults")
    next_token: Optional[str] = Field(default=None, alias="NextToken")


class CreateBudgetActionResponseModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeNotificationsForBudgetResponseModel(BaseModel):
    notifications: List[NotificationModel] = Field(alias="Notifications")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeSubscribersForNotificationResponseModel(BaseModel):
    subscribers: List[SubscriberModel] = Field(alias="Subscribers")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ExecuteBudgetActionResponseModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")
    execution_type: Literal[
        "APPROVE_BUDGET_ACTION",
        "RESET_BUDGET_ACTION",
        "RETRY_BUDGET_ACTION",
        "REVERSE_BUDGET_ACTION",
    ] = Field(alias="ExecutionType")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DefinitionModel(BaseModel):
    iam_action_definition: Optional[IamActionDefinitionModel] = Field(
        default=None, alias="IamActionDefinition"
    )
    scp_action_definition: Optional[ScpActionDefinitionModel] = Field(
        default=None, alias="ScpActionDefinition"
    )
    ssm_action_definition: Optional[SsmActionDefinitionModel] = Field(
        default=None, alias="SsmActionDefinition"
    )


class DescribeBudgetActionHistoriesRequestDescribeBudgetActionHistoriesPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")
    time_period: Optional[TimePeriodModel] = Field(default=None, alias="TimePeriod")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeBudgetActionsForAccountRequestDescribeBudgetActionsForAccountPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeBudgetActionsForBudgetRequestDescribeBudgetActionsForBudgetPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeBudgetNotificationsForAccountRequestDescribeBudgetNotificationsForAccountPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeBudgetPerformanceHistoryRequestDescribeBudgetPerformanceHistoryPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    time_period: Optional[TimePeriodModel] = Field(default=None, alias="TimePeriod")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeBudgetsRequestDescribeBudgetsPaginateModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeNotificationsForBudgetRequestDescribeNotificationsForBudgetPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeSubscribersForNotificationRequestDescribeSubscribersForNotificationPaginateModel(
    BaseModel
):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification: NotificationModel = Field(alias="Notification")
    pagination_config: Optional[PaginatorConfigModel] = Field(
        default=None, alias="PaginationConfig"
    )


class DescribeBudgetNotificationsForAccountResponseModel(BaseModel):
    budget_notifications_for_account: List[BudgetNotificationsForAccountModel] = Field(
        alias="BudgetNotificationsForAccount"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class BudgetModel(BaseModel):
    budget_name: str = Field(alias="BudgetName")
    time_unit: Literal["ANNUALLY", "DAILY", "MONTHLY", "QUARTERLY"] = Field(
        alias="TimeUnit"
    )
    budget_type: Literal[
        "COST",
        "RI_COVERAGE",
        "RI_UTILIZATION",
        "SAVINGS_PLANS_COVERAGE",
        "SAVINGS_PLANS_UTILIZATION",
        "USAGE",
    ] = Field(alias="BudgetType")
    budget_limit: Optional[SpendModel] = Field(default=None, alias="BudgetLimit")
    planned_budget_limits: Optional[Mapping[str, SpendModel]] = Field(
        default=None, alias="PlannedBudgetLimits"
    )
    cost_filters: Optional[Mapping[str, Sequence[str]]] = Field(
        default=None, alias="CostFilters"
    )
    cost_types: Optional[CostTypesModel] = Field(default=None, alias="CostTypes")
    time_period: Optional[TimePeriodModel] = Field(default=None, alias="TimePeriod")
    calculated_spend: Optional[CalculatedSpendModel] = Field(
        default=None, alias="CalculatedSpend"
    )
    last_updated_time: Optional[Union[datetime, str]] = Field(
        default=None, alias="LastUpdatedTime"
    )
    auto_adjust_data: Optional[AutoAdjustDataModel] = Field(
        default=None, alias="AutoAdjustData"
    )


class BudgetPerformanceHistoryModel(BaseModel):
    budget_name: Optional[str] = Field(default=None, alias="BudgetName")
    budget_type: Optional[
        Literal[
            "COST",
            "RI_COVERAGE",
            "RI_UTILIZATION",
            "SAVINGS_PLANS_COVERAGE",
            "SAVINGS_PLANS_UTILIZATION",
            "USAGE",
        ]
    ] = Field(default=None, alias="BudgetType")
    cost_filters: Optional[Dict[str, List[str]]] = Field(
        default=None, alias="CostFilters"
    )
    cost_types: Optional[CostTypesModel] = Field(default=None, alias="CostTypes")
    time_unit: Optional[Literal["ANNUALLY", "DAILY", "MONTHLY", "QUARTERLY"]] = Field(
        default=None, alias="TimeUnit"
    )
    budgeted_and_actual_amounts_list: Optional[
        List[BudgetedAndActualAmountsModel]
    ] = Field(default=None, alias="BudgetedAndActualAmountsList")


class ActionModel(BaseModel):
    action_id: str = Field(alias="ActionId")
    budget_name: str = Field(alias="BudgetName")
    notification_type: Literal["ACTUAL", "FORECASTED"] = Field(alias="NotificationType")
    action_type: Literal[
        "APPLY_IAM_POLICY", "APPLY_SCP_POLICY", "RUN_SSM_DOCUMENTS"
    ] = Field(alias="ActionType")
    action_threshold: ActionThresholdModel = Field(alias="ActionThreshold")
    definition: DefinitionModel = Field(alias="Definition")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    approval_model: Literal["AUTOMATIC", "MANUAL"] = Field(alias="ApprovalModel")
    status: Literal[
        "EXECUTION_FAILURE",
        "EXECUTION_IN_PROGRESS",
        "EXECUTION_SUCCESS",
        "PENDING",
        "RESET_FAILURE",
        "RESET_IN_PROGRESS",
        "REVERSE_FAILURE",
        "REVERSE_IN_PROGRESS",
        "REVERSE_SUCCESS",
        "STANDBY",
    ] = Field(alias="Status")
    subscribers: List[SubscriberModel] = Field(alias="Subscribers")


class CreateBudgetActionRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    notification_type: Literal["ACTUAL", "FORECASTED"] = Field(alias="NotificationType")
    action_type: Literal[
        "APPLY_IAM_POLICY", "APPLY_SCP_POLICY", "RUN_SSM_DOCUMENTS"
    ] = Field(alias="ActionType")
    action_threshold: ActionThresholdModel = Field(alias="ActionThreshold")
    definition: DefinitionModel = Field(alias="Definition")
    execution_role_arn: str = Field(alias="ExecutionRoleArn")
    approval_model: Literal["AUTOMATIC", "MANUAL"] = Field(alias="ApprovalModel")
    subscribers: Sequence[SubscriberModel] = Field(alias="Subscribers")


class UpdateBudgetActionRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action_id: str = Field(alias="ActionId")
    notification_type: Optional[Literal["ACTUAL", "FORECASTED"]] = Field(
        default=None, alias="NotificationType"
    )
    action_threshold: Optional[ActionThresholdModel] = Field(
        default=None, alias="ActionThreshold"
    )
    definition: Optional[DefinitionModel] = Field(default=None, alias="Definition")
    execution_role_arn: Optional[str] = Field(default=None, alias="ExecutionRoleArn")
    approval_model: Optional[Literal["AUTOMATIC", "MANUAL"]] = Field(
        default=None, alias="ApprovalModel"
    )
    subscribers: Optional[Sequence[SubscriberModel]] = Field(
        default=None, alias="Subscribers"
    )


class CreateBudgetRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget: BudgetModel = Field(alias="Budget")
    notifications_with_subscribers: Optional[
        Sequence[NotificationWithSubscribersModel]
    ] = Field(default=None, alias="NotificationsWithSubscribers")


class DescribeBudgetResponseModel(BaseModel):
    budget: BudgetModel = Field(alias="Budget")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBudgetsResponseModel(BaseModel):
    budgets: List[BudgetModel] = Field(alias="Budgets")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBudgetRequestModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    new_budget: BudgetModel = Field(alias="NewBudget")


class DescribeBudgetPerformanceHistoryResponseModel(BaseModel):
    budget_performance_history: BudgetPerformanceHistoryModel = Field(
        alias="BudgetPerformanceHistory"
    )
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionHistoryDetailsModel(BaseModel):
    message: str = Field(alias="Message")
    action: ActionModel = Field(alias="Action")


class DeleteBudgetActionResponseModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action: ActionModel = Field(alias="Action")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBudgetActionResponseModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    action: ActionModel = Field(alias="Action")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBudgetActionsForAccountResponseModel(BaseModel):
    actions: List[ActionModel] = Field(alias="Actions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class DescribeBudgetActionsForBudgetResponseModel(BaseModel):
    actions: List[ActionModel] = Field(alias="Actions")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class UpdateBudgetActionResponseModel(BaseModel):
    account_id: str = Field(alias="AccountId")
    budget_name: str = Field(alias="BudgetName")
    old_action: ActionModel = Field(alias="OldAction")
    new_action: ActionModel = Field(alias="NewAction")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")


class ActionHistoryModel(BaseModel):
    timestamp: datetime = Field(alias="Timestamp")
    status: Literal[
        "EXECUTION_FAILURE",
        "EXECUTION_IN_PROGRESS",
        "EXECUTION_SUCCESS",
        "PENDING",
        "RESET_FAILURE",
        "RESET_IN_PROGRESS",
        "REVERSE_FAILURE",
        "REVERSE_IN_PROGRESS",
        "REVERSE_SUCCESS",
        "STANDBY",
    ] = Field(alias="Status")
    event_type: Literal[
        "CREATE_ACTION", "DELETE_ACTION", "EXECUTE_ACTION", "SYSTEM", "UPDATE_ACTION"
    ] = Field(alias="EventType")
    action_history_details: ActionHistoryDetailsModel = Field(
        alias="ActionHistoryDetails"
    )


class DescribeBudgetActionHistoriesResponseModel(BaseModel):
    action_histories: List[ActionHistoryModel] = Field(alias="ActionHistories")
    next_token: str = Field(alias="NextToken")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
