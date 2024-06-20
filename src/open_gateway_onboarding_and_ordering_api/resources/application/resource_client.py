"""File Generated by Sideko (sideko.dev)"""

from open_gateway_onboarding_and_ordering_api.core import (
    AsyncBaseClient,
    QueryParams,
    SyncBaseClient,
    RequestOptions,
    encode_query_param,
    default_request_options,
    to_encodable,
)
import typing


class ApplicationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Any,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation creates a Application entity.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields is not None:
            _query["fields"] = encode_query_param(fields, False)
        _json = to_encodable(item=data, dump_with=typing.Any)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/application",
            auth_names=["oAuth2ClientCredentials"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncApplicationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Any,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation creates a Application entity.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields is not None:
            _query["fields"] = encode_query_param(fields, False)
        _json = to_encodable(item=data, dump_with=typing.Any)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/application",
            auth_names=["oAuth2ClientCredentials"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
