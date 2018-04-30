Simple wrapper for the groupme API.

# initialize

```python
>>> import groupme
>>> # provide your token and client_id (client_id not always needed)
>>> client = groupme.Client(token='', client_id='')
```

# Get data for user
```python
>>> r = client.user.me()
>>> r.json()
```

# Get groups
```python
>>> r = client.group.get(limit=10, page=1)
>>> r.json()
```

# Get messages for a group
```python
>>> r = client.group.get_messages(<group_id>, limit=100, page=1)
>>> r.json()
```