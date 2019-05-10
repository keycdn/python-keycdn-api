import pytest
import responses

from keycdn import Api, ENDPOINT


@responses.activate
def test_get():
    responses.add(
        responses.GET,
        ENDPOINT + '/example',
        json={'it': 'works'},
    )

    api = Api('secret')
    resp = api.get('example', {'doesit': 'work?'})
    assert resp == {'it': 'works'}
    assert len(responses.calls) == 1
