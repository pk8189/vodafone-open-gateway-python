
# Open Gateway - Onboarding And Ordering API Python SDK

## Overview
The TMF931 "Open Gateway - Onboarding And Ordering API" enables Channel Partners and Operators to carry out onboarding tasks via an API. 


## Initilization
Initialize either the synchronous or asynchronous client to authenticate

### Synchronous Client
```python
from open_gateway_onboarding_and_ordering_api import Client
from os import getenv

Client(oauth_token=getenv("API_TOKEN"))
```

### Asynchronous Client
```python
from open_gateway_onboarding_and_ordering_api import AsyncClient
from os import getenv

AsyncClient(oauth_token=getenv("API_TOKEN"))
```


### List or find ApiProduct objects
> List or find ApiProduct objects

```python
client.api_product.list(fields="string", limit=123, offset=123)
```

---

### Retrieves a ApiProduct by ID
> This operation retrieves a ApiProduct entity. Attribute selection enabled for all first level attributes.

```python
client.api_product.get(id="string", fields="string")
```

---

### Check the upstream system is up and running.
> This API is for checking the upstream system is up and running.

```python
client.ping.list()
```

---

### Check the downstream system is up and running.
> This API is for checking that the downstream system is up and running.

```python
client.status.list()
```

---

### Creates a ApiProductOrder
> This operation creates a ApiProductOrder entity.

```python
client.api_product_order.create(fields="string", data="could be anything")
```

---

### Creates a Application
> This operation creates a Application entity.

```python
client.application.create(fields="string", data="could be anything")
```

---

### Creates a ApplicationOwner
> This operation creates a ApplicationOwner entity.

```python
client.application_owner.create(fields="string", data="could be anything")
```


