"""File Generated by Sideko (sideko.dev)"""

from open_gateway_onboarding_and_ordering_api.core import (
    AsyncBaseClient,
    encode_query_param,
    SyncBaseClient,
    QueryParams,
    RequestOptions,
    default_request_options,
)
import typing


class ApiProductClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation retrieves a ApiProduct entity. Attribute selection enabled for all first level attributes.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields is not None:
            _query["fields"] = encode_query_param(fields, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/apiProduct/{id}",
            auth_names=["oAuth2ClientCredentials"],
            query_params=_query,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        List or find ApiProduct objects
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields is not None:
            _query["fields"] = encode_query_param(fields, False)
        if limit is not None:
            _query["limit"] = encode_query_param(limit, False)
        if offset is not None:
            _query["offset"] = encode_query_param(offset, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/apiProduct",
            auth_names=["oAuth2ClientCredentials"],
            query_params=_query,
            cast_to=typing.List[typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncApiProductClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This operation retrieves a ApiProduct entity. Attribute selection enabled for all first level attributes.
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields is not None:
            _query["fields"] = encode_query_param(fields, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/apiProduct/{id}",
            auth_names=["oAuth2ClientCredentials"],
            query_params=_query,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        List or find ApiProduct objects
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields is not None:
            _query["fields"] = encode_query_param(fields, False)
        if limit is not None:
            _query["limit"] = encode_query_param(limit, False)
        if offset is not None:
            _query["offset"] = encode_query_param(offset, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/apiProduct",
            auth_names=["oAuth2ClientCredentials"],
            query_params=_query,
            cast_to=typing.List[typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)