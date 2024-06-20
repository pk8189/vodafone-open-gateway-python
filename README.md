
# SMS Messaging Interface Python SDK

## Overview
SMS messaging enables applications to send and receive text messages to one or more recipients in a single request. Delivery is confirmed by retrieving a delivery status or through subscription to a webhook notification. This API specification is based on the GMSA OneAPI framework for SMS.


## Initilization
Initialize either the synchronous or asynchronous client to authenticate

### Synchronous Client
```python
from sms_messaging_interface import Client

Client()
```

### Asynchronous Client
```python
from sms_messaging_interface import AsyncClient

AsyncClient()
```


### Unsubscribe from receiving SMS messages addressed to your web application
> Unsubscribe from receiving SMS messages addressed to your web
> application.
> 
> Once unsubscribed, your web application will no longer receive SMS
> messages when processed by your provider messaging platform.
> 
> SMS messages that have not been retrieved will expire once their
> validity period has been reached.
> 
> The sending web application is identified by their provider assigned
> senderAddress (short code).
> 

```python
client.smsmessaging.v1.inbound.subscriptions.delete(subscription_id="string")
```

---

### Unsubscribe from receiving delivery status notifications for previously submitted SMS messages
> Unsubscribe from receiving delivery status notifications for all
> previously submitted SMS messages.
> 
> The sending web application is identified by their provider assigned
> senderAddress (short code).
> 

```python
client.smsmessaging.v1.outbound.subscriptions.delete(
    sender_address="string", subscription_id="string"
)
```

---

### Unsubscribe from receiving SMS messages addressed to your web application
> Unsubscribe from receiving SMS messages addressed to your web
> application.
> 
> Once unsubscribed, your web application will no longer receive SMS
> messages when processed by your provider messaging platform.
> 
> SMS messages that have not been retrieved will expire once their
> validity period has been reached.
> 
> The sending web application is identified by their assigned customerID.
> 

```python
client.x.smsmessaging.v1.inbound.subscriptions.delete(
    customer_id="string", subscription_id="string"
)
```

---

### Unsubscribe from receiving delivery status notifications for previously submitted SMS messages
> Unsubscribe from receiving delivery status notifications for all
> previously submitted SMS messages.
> 
> The sending web application is identified by their assigned customerID.
> 

```python
client.x.smsmessaging.v1.outbound.subscriptions.delete(
    customer_id="string", sender_address="string", subscription_id="string"
)
```

---

### Retrieve SMS messages addressed to your web application
> Retrieve SMS messages addressed to your web application (identified by
> registrationID).
> 
> This operation provides a means for your web application to poll the
> messaging platform for SMS messages.
> 
> The sending web application is identified by their provider assigned
> senderAddress (short code).
> 

```python
client.smsmessaging.v1.inbound.registrations.messages.list(
    registration_id="string", max_batch_size=123.45
)
```

---

### Query an SMS message previously submitted to one or more recipients
> Query the delivery status of an SMS message previously submitted to one
> or more recipients identified by requestID.
> 
> The delivery status response is an deliveryInfoList object containing
> the delivery information for each recipient.
> 
> address for which a message was originally submitted to, in a
> deliveryInfo array.
> 
> The deliveryStatus value may be one of:
> 
> - DeliveredToTerminal: successfully delivered to recipient terminal
> 
> - DeliveryUncertain: delivery status unknown
> 
> - DeliveryImpossible: unsuccessful delivery, the message could not be
> delivered before it expired
> 
> - MessageWaiting: the message is queued for delivery. This is a
> temporary state, pending transition to one of the other states
> 
> - DeliveredToNetwork: successful delivery to the network enabler
> responsible for routing the SMS
> 
> The sending web application is identified by their provider assigned
> senderAddress (short code).
> 

```python
client.smsmessaging.v1.outbound.requests.delivery_infos.list(
    sender_address="string", request_id="string"
)
```

---

### Retrieve SMS messages addressed to your web application
> Retrieve SMS messages addressed to your web application (identified by
> registrationID).
> 
> This operation provides a means for your web application to poll the
> messaging platform for SMS messages.
> 
> The sending web application is identified by their assigned customerID.
> 

```python
client.x.smsmessaging.v1.inbound.registrations.messages.list(
    customer_id="string", registration_id="string", max_batch_size=123.45
)
```

---

### Query an SMS message previously submitted to one or more recipients
> Query the delivery status of an SMS message previously submitted to one
> or more recipients identified by requestID
> 
> The delivery status response is an deliveryInfoList object containing
> the delivery information for each recipient 
> 
> address for which a message was originally submitted to, in a
> deliveryInfo array.
> 
> The deliveryStatus value may be one of:
> 
> - DeliveredToTerminal: successfully delivered to recipient terminal
> 
> - DeliveryUncertain: delivery status unknown
> 
> - DeliveryImpossible: unsuccessful delivery, the message could not be
> delivered before it expired
> 
> - MessageWaiting: the message is queued for delivery. This is a
> temporary state, pending transition to one of the other states
> 
> - DeliveredToNetwork: successful delivery to the network enabler
> responsible for routing the SMS
> 
> The sending web application is identified by their assigned customerID.
> 

```python
client.x.smsmessaging.v1.outbound.requests.delivery_infos.list(
    customer_id="string", sender_address="string", request_id="string"
)
```

---

### Subscribe to receive SMS messages addressed to your web application
> Subscribe to receive SMS messages addressed to your web application.
> 
> Once subscribed, your web application will receive SMS messages when
> processed by your provider messaging platform.
> 
> The sending web application is identified by their provider assigned
> senderAddress (short code).
> 

```python
client.smsmessaging.v1.inbound.subscriptions.create(
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
    }
)
```

---

### Send an SMS message to one or more recipients
> Send an SMS message to one or more recipients.
> 
> A recipient is addressed by their unique MSISDN.
> 
> The sending web application is identified by their provider assigned
> senderAddress (short code). 
> 

```python
client.smsmessaging.v1.outbound.requests.create(
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
```

---

### Subscribe to receive delivery status notifications for previously        submitted SMS messages
> Subscribe to receive delivery status notifications for all previously
> submitted SMS messages.
> 
> The sending web application is identified by their provider assigned
> senderAddress (short code).
> 

```python
client.smsmessaging.v1.outbound.subscriptions.create(
    sender_address="string",
    data={
        "delivery_receipt_subscription": {
            "callback_reference": {
                "callback_data": "some data useful to the requestor",
                "notify_url": "http://application-url/notify",
            },
            "filter_criteria": "string",
        }
    },
)
```

---

### Subscribe to receive SMS messages addressed to your web application
> Subscribe to receive SMS messages addressed to your web application.
> 
> Once subscribed, your web application will receive SMS messages when
> processed by your provider messaging platform.
> 
> The sending web application is identified by their assigned customerID.
> 

```python
client.x.smsmessaging.v1.inbound.subscriptions.create(
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
```

---

### Send an SMS message to one or more recipients
> Send an SMS message to one or more recipients.
> 
> A recipient is addressed by their unique MSISDN.
> 
> The sending web application is identified by their assigned customerID. 
> 

```python
client.x.smsmessaging.v1.outbound.requests.create(
    customer_id="string",
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
```

---

### Subscribe to receive delivery status notifications for previously        submitted SMS messages
> Subscribe to receive delivery status notifications for all previously
> submitted SMS messages.
> 
> The sending web application is identified by their assigned customerID.
> 

```python
client.x.smsmessaging.v1.outbound.subscriptions.create(
    customer_id="string",
    sender_address="string",
    data={
        "delivery_receipt_subscription": {
            "callback_reference": {
                "callback_data": "some data useful to the requestor",
                "notify_url": "http://application-url/notify",
            },
            "filter_criteria": "string",
        }
    },
)
```


