"""File Generated by Sideko (sideko.dev)"""

import pytest
from open_gateway_onboarding_and_ordering_api import AsyncClient, Client
from os import getenv
import typing
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_create_201_generated_success_create_an_application_owner():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(oauth_token=getenv("API_TOKEN"))
    response = client.application_owner.create(
        fields="string", data="could be anything"
    )
    adapter = TypeAdapter(typing.Any)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_201_generated_success_create_an_application_owner():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(oauth_token=getenv("API_TOKEN"))
    response = await client.application_owner.create(
        fields="string", data="could be anything"
    )
    adapter = TypeAdapter(typing.Any)
    adapter.validate_python(response)