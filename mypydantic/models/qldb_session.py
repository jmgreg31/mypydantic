# Model Generated: Thu Mar  2 21:56:22 2023

from __future__ import annotations

from typing import Any, Dict, IO, List, Mapping, Optional, Sequence, Type, Union

from botocore.response import StreamingBody
from pydantic import Field

from mypydantic.models.base_model import BaseModel


class TimingInformationModel(BaseModel):
    processing_time_milliseconds: Optional[int] = Field(
        default=None, alias="ProcessingTimeMilliseconds"
    )


class CommitTransactionRequestModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")
    commit_digest: Union[str, bytes, Type[IO[Any]], Type[StreamingBody]] = Field(
        alias="CommitDigest"
    )


class IOUsageModel(BaseModel):
    read_ios: Optional[int] = Field(default=None, alias="ReadIOs")
    write_ios: Optional[int] = Field(default=None, alias="WriteIOs")


class ValueHolderModel(BaseModel):
    ion_binary: Optional[Union[str, bytes, Type[IO[Any]], Type[StreamingBody]]] = Field(
        default=None, alias="IonBinary"
    )
    ion_text: Optional[str] = Field(default=None, alias="IonText")


class FetchPageRequestModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")
    next_page_token: str = Field(alias="NextPageToken")


class ResponseMetadataModel(BaseModel):
    request_id: str = Field(alias="RequestId")
    host_id: str = Field(alias="HostId")
    http_status_code: int = Field(alias="HTTPStatusCode")
    http_headers: Dict[str, str] = Field(alias="HTTPHeaders")
    retry_attempts: int = Field(alias="RetryAttempts")


class StartSessionRequestModel(BaseModel):
    ledger_name: str = Field(alias="LedgerName")


class AbortTransactionResultModel(BaseModel):
    timing_information: Optional[TimingInformationModel] = Field(
        default=None, alias="TimingInformation"
    )


class EndSessionResultModel(BaseModel):
    timing_information: Optional[TimingInformationModel] = Field(
        default=None, alias="TimingInformation"
    )


class StartSessionResultModel(BaseModel):
    session_token: Optional[str] = Field(default=None, alias="SessionToken")
    timing_information: Optional[TimingInformationModel] = Field(
        default=None, alias="TimingInformation"
    )


class StartTransactionResultModel(BaseModel):
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    timing_information: Optional[TimingInformationModel] = Field(
        default=None, alias="TimingInformation"
    )


class CommitTransactionResultModel(BaseModel):
    transaction_id: Optional[str] = Field(default=None, alias="TransactionId")
    commit_digest: Optional[bytes] = Field(default=None, alias="CommitDigest")
    timing_information: Optional[TimingInformationModel] = Field(
        default=None, alias="TimingInformation"
    )
    consumed_ios: Optional[IOUsageModel] = Field(default=None, alias="ConsumedIOs")


class ExecuteStatementRequestModel(BaseModel):
    transaction_id: str = Field(alias="TransactionId")
    statement: str = Field(alias="Statement")
    parameters: Optional[Sequence[ValueHolderModel]] = Field(
        default=None, alias="Parameters"
    )


class PageModel(BaseModel):
    values: Optional[List[ValueHolderModel]] = Field(default=None, alias="Values")
    next_page_token: Optional[str] = Field(default=None, alias="NextPageToken")


class SendCommandRequestModel(BaseModel):
    session_token: Optional[str] = Field(default=None, alias="SessionToken")
    start_session: Optional[StartSessionRequestModel] = Field(
        default=None, alias="StartSession"
    )
    start_transaction: Optional[Mapping[str, Any]] = Field(
        default=None, alias="StartTransaction"
    )
    end_session: Optional[Mapping[str, Any]] = Field(default=None, alias="EndSession")
    commit_transaction: Optional[CommitTransactionRequestModel] = Field(
        default=None, alias="CommitTransaction"
    )
    abort_transaction: Optional[Mapping[str, Any]] = Field(
        default=None, alias="AbortTransaction"
    )
    execute_statement: Optional[ExecuteStatementRequestModel] = Field(
        default=None, alias="ExecuteStatement"
    )
    fetch_page: Optional[FetchPageRequestModel] = Field(default=None, alias="FetchPage")


class ExecuteStatementResultModel(BaseModel):
    first_page: Optional[PageModel] = Field(default=None, alias="FirstPage")
    timing_information: Optional[TimingInformationModel] = Field(
        default=None, alias="TimingInformation"
    )
    consumed_ios: Optional[IOUsageModel] = Field(default=None, alias="ConsumedIOs")


class FetchPageResultModel(BaseModel):
    page: Optional[PageModel] = Field(default=None, alias="Page")
    timing_information: Optional[TimingInformationModel] = Field(
        default=None, alias="TimingInformation"
    )
    consumed_ios: Optional[IOUsageModel] = Field(default=None, alias="ConsumedIOs")


class SendCommandResultModel(BaseModel):
    start_session: StartSessionResultModel = Field(alias="StartSession")
    start_transaction: StartTransactionResultModel = Field(alias="StartTransaction")
    end_session: EndSessionResultModel = Field(alias="EndSession")
    commit_transaction: CommitTransactionResultModel = Field(alias="CommitTransaction")
    abort_transaction: AbortTransactionResultModel = Field(alias="AbortTransaction")
    execute_statement: ExecuteStatementResultModel = Field(alias="ExecuteStatement")
    fetch_page: FetchPageResultModel = Field(alias="FetchPage")
    response_metadata: ResponseMetadataModel = Field(alias="ResponseMetadata")
