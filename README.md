# Python Library for the KeyCDN API


## Installation

``` bash
pip install keycdn
```

## Usage

### Initial
```python
import keycdn

...
keycdn = keycdn.Api('<your_api_key>')

```

### Get all zones
```python
keycdn.get('zones.json')
```

### Get a specific zone
```python
keycdn.post('zones/<zoneId>.json')
```

### Purge zone cache
```python
keycdn.get('zones/purge/<zoneId>.json')
```


For more details visit https://www.keycdn.com
