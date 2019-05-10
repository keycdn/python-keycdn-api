# Python Library for the KeyCDN API

## Installation

```bash
pip install keycdn
```

## Usage

### Initial

```python
import keycdn

...
api = keycdn.Api('<your_api_key>')

```

### Get all zones

```python
api.get('zones.json')
```

### Get a specific zone

```python
api.post('zones/<zoneId>.json')
```

### Purge zone cache

```python
api.get('zones/purge/<zoneId>.json')
```

For more details visit [https://www.keycdn.com](https://www.keycdn.com).

## Contributing

To run the test, assuming you have clone the repo first install the extras:

    pip install -e ".[dev]"

Now, to run the tests for all configured Python versions, run:

    tox

Running the whole test suite takes some time and it's going to fail if
any Python version couldn't be installed. If, for example, you know you
only have Python 3.6 available you can run like this:

    tox --listenvs  # To see what the environment names are
    tox -e py36

If you prefer to test, with a specific Python environment, without `tox`
you can do what `tox` does:

    pip install pytest responses pytest-env
    pytest

Note! Depending on your shell, you might need to reactivate the Python
virtual environment after `pip install ...` to make executables available.
