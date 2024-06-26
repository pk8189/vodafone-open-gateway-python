"""File Generated by Sideko (sideko.dev)"""

import pytest
from sms_messaging_interface import Client, AsyncClient
from sms_messaging_interface.types.smsmessaging.v1.outbound.requests import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_create_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client()
    response = client.smsmessaging.v1.outbound.requests.create(
        sender_address="string",
        data={
            "outbound_sms_message_request": {
                "address": ["tel:+16309700001"],
                "client_correlator": "6587329",
                "outbound_sms_text_message": {"message": "Hello World!"},
                "receipt_request": {
                    "callback_data": "some data useful to the requestor",
                    "notify_url": "http://application-url/notify",
                },
                "sender_address": "12345",
                "sender_name": "12345",
            }
        },
    )
    adapter = TypeAdapter(models.OutboundSmsMessageRspCall)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient()
    response = await client.smsmessaging.v1.outbound.requests.create(
        sender_address="string",
        data={
            "outbound_sms_message_request": {
                "address": ["tel:+16309700001"],
                "client_correlator": "6587329",
                "outbound_sms_text_message": {"message": "Hello World!"},
                "receipt_request": {
                    "callback_data": "some data useful to the requestor",
                    "notify_url": "http://application-url/notify",
                },
                "sender_address": "12345",
                "sender_name": "12345",
            }
        },
    )
    adapter = TypeAdapter(models.OutboundSmsMessageRspCall)
    adapter.validate_python(response)
