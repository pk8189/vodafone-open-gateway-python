"""File Generated by Sideko (sideko.dev)"""

from sms_messaging_interface.core import (
    RequestOptions,
    default_request_options,
    AsyncBaseClient,
    encode_query_param,
    SyncBaseClient,
    QueryParams,
)
import typing
from sms_messaging_interface.types.x.smsmessaging.v1.inbound.registrations.messages import (
    models,
)


class MessagesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        customer_id: str,
        registration_id: str,
        max_batch_size: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InboundSmsMessageListRspCall:
        """
        Retrieve SMS messages addressed to your web application (identified by
        registrationID).

        This operation provides a means for your web application to poll the
        messaging platform for SMS messages.

        The sending web application is identified by their assigned customerID.

        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if max_batch_size is not None:
            _query["maxBatchSize"] = encode_query_param(max_batch_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/{customer_id}/smsmessaging/v1/inbound/registrations/{registration_id}/messages",
            query_params=_query,
            cast_to=models.InboundSmsMessageListRspCall,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncMessagesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        customer_id: str,
        registration_id: str,
        max_batch_size: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InboundSmsMessageListRspCall:
        """
        Retrieve SMS messages addressed to your web application (identified by
        registrationID).

        This operation provides a means for your web application to poll the
        messaging platform for SMS messages.

        The sending web application is identified by their assigned customerID.

        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if max_batch_size is not None:
            _query["maxBatchSize"] = encode_query_param(max_batch_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/{customer_id}/smsmessaging/v1/inbound/registrations/{registration_id}/messages",
            query_params=_query,
            cast_to=models.InboundSmsMessageListRspCall,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
