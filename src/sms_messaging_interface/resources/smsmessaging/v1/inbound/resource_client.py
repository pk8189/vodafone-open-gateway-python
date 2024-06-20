"""File Generated by Sideko (sideko.dev)"""

from sms_messaging_interface.core import SyncBaseClient, AsyncBaseClient
from sms_messaging_interface.resources.smsmessaging.v1.inbound.subscriptions import (
    SubscriptionsClient,
    AsyncSubscriptionsClient,
)
from sms_messaging_interface.resources.smsmessaging.v1.inbound.registrations import (
    AsyncRegistrationsClient,
    RegistrationsClient,
)


class InboundClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.subscriptions = SubscriptionsClient(base_client=self._base_client)
        self.registrations = RegistrationsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncInboundClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.subscriptions = AsyncSubscriptionsClient(base_client=self._base_client)
        self.registrations = AsyncRegistrationsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
