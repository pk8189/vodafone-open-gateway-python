"""File Generated by Sideko (sideko.dev)"""

import pytest
from sms_messaging_interface import Client, AsyncClient
from sms_messaging_interface.types.x.smsmessaging.v1.outbound.requests.delivery_infos import (
    models,
)
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client()
    response = client.x.smsmessaging.v1.outbound.requests.delivery_infos.list(
        customer_id="string", sender_address="string", request_id="string"
    )
    adapter = TypeAdapter(models.DeliveryInfoListRspCall)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient()
    response = await client.x.smsmessaging.v1.outbound.requests.delivery_infos.list(
        customer_id="string", sender_address="string", request_id="string"
    )
    adapter = TypeAdapter(models.DeliveryInfoListRspCall)
    adapter.validate_python(response)
