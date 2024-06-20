"""File Generated by Sideko (sideko.dev)"""

import httpx
import typing
from sms_messaging_interface.environment import Environment
from sms_messaging_interface.core import AsyncBaseClient, SyncBaseClient
from sms_messaging_interface.resources.smsmessaging import (
    SmsmessagingClient,
    AsyncSmsmessagingClient,
)
from sms_messaging_interface.resources.x import XClient, AsyncXClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.DEFAULT,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
            ),
        )

        # register auth methods (keep comment for code generation)

        # register sync resources (keep comment for code generation)
        self.smsmessaging = SmsmessagingClient(base_client=self._base_client)
        self.x = XClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.DEFAULT,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.AsyncClient(timeout=timeout)
                if httpx_client is None
                else httpx_client
            ),
        )

        # register auth methods (keep comment for code generation)

        # register async resources (keep comment for code generation)
        self.smsmessaging = AsyncSmsmessagingClient(base_client=self._base_client)
        self.x = AsyncXClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")