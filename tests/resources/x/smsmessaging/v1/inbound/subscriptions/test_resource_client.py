"""File Generated by Sideko (sideko.dev)"""

import pytest
from sms_messaging_interface import Client, AsyncClient
from pydantic import TypeAdapter
from sms_messaging_interface.types.x.smsmessaging.v1.inbound.subscriptions import models

# test sync & async methods (keep comment for code generation)


def test_create_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client()
    response = client.x.smsmessaging.v1.inbound.subscriptions.create(
        customer_id="string",
        data={
            "subscription": {
                "callback_reference": {
                    "callback_data": "some data useful to the requestor",
                    "notify_url": "http://application-url/notify",
                },
                "client_correlator": 12345,
                "criteria": "Vote",
                "destination_address": "tel:3456",
                "notification_format": "JSON",
            }
        },
    )
    adapter = TypeAdapter(models.SubscriptionRspCall)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient()
    response = await client.x.smsmessaging.v1.inbound.subscriptions.create(
        customer_id="string",
        data={
            "subscription": {
                "callback_reference": {
                    "callback_data": "some data useful to the requestor",
                    "notify_url": "http://application-url/notify",
                },
                "client_correlator": 12345,
                "criteria": "Vote",
                "destination_address": "tel:3456",
                "notification_format": "JSON",
            }
        },
    )
    adapter = TypeAdapter(models.SubscriptionRspCall)
    adapter.validate_python(response)


def test_delete_204_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client()
    response = client.x.smsmessaging.v1.inbound.subscriptions.delete(
        customer_id="string", subscription_id="string"
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient()
    response = await client.x.smsmessaging.v1.inbound.subscriptions.delete(
        customer_id="string", subscription_id="string"
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)
