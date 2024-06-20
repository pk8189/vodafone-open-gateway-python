"""File Generated by Sideko (sideko.dev)"""

from sms_messaging_interface.core import (
    SyncBaseClient,
    RequestOptions,
    AsyncBaseClient,
    default_request_options,
)
import typing
from sms_messaging_interface.types.smsmessaging.v1.outbound.requests.delivery_infos import (
    models,
)


class DeliveryInfosClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        sender_address: str,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeliveryInfoListRspCall:
        """
        Query the delivery status of an SMS message previously submitted to one
        or more recipients identified by requestID.

        The delivery status response is an deliveryInfoList object containing
        the delivery information for each recipient.

        address for which a message was originally submitted to, in a
        deliveryInfo array.

        The deliveryStatus value may be one of:

        - DeliveredToTerminal: successfully delivered to recipient terminal

        - DeliveryUncertain: delivery status unknown

        - DeliveryImpossible: unsuccessful delivery, the message could not be
        delivered before it expired

        - MessageWaiting: the message is queued for delivery. This is a
        temporary state, pending transition to one of the other states

        - DeliveredToNetwork: successful delivery to the network enabler
        responsible for routing the SMS

        The sending web application is identified by their provider assigned
        senderAddress (short code).

        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/smsmessaging/v1/outbound/{sender_address}/requests/{request_id}/deliveryInfos",
            cast_to=models.DeliveryInfoListRspCall,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncDeliveryInfosClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        sender_address: str,
        request_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeliveryInfoListRspCall:
        """
        Query the delivery status of an SMS message previously submitted to one
        or more recipients identified by requestID.

        The delivery status response is an deliveryInfoList object containing
        the delivery information for each recipient.

        address for which a message was originally submitted to, in a
        deliveryInfo array.

        The deliveryStatus value may be one of:

        - DeliveredToTerminal: successfully delivered to recipient terminal

        - DeliveryUncertain: delivery status unknown

        - DeliveryImpossible: unsuccessful delivery, the message could not be
        delivered before it expired

        - MessageWaiting: the message is queued for delivery. This is a
        temporary state, pending transition to one of the other states

        - DeliveredToNetwork: successful delivery to the network enabler
        responsible for routing the SMS

        The sending web application is identified by their provider assigned
        senderAddress (short code).

        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/smsmessaging/v1/outbound/{sender_address}/requests/{request_id}/deliveryInfos",
            cast_to=models.DeliveryInfoListRspCall,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
