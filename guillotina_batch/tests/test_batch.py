import json


async def test_batch_get_data(container_requester):
    """Check a value from registry."""
    async with container_requester as requester:
        await requester(
            'POST', '/db/guillotina', data=json.dumps({
                '@type': 'Item',
                'id': 'foobar1'
            }))
        await requester(
            'POST', '/db/guillotina', data=json.dumps({
                '@type': 'Item',
                'id': 'foobar2'
            }))
        response, _ = await requester(
            'POST',
            '/db/guillotina/@batch',
            data=json.dumps([{
                'method': 'GET',
                'endpoint': 'foobar1'
            }, {
                'method': 'GET',
                'endpoint': 'foobar2'
            }])
        )
        assert len(response) == 2
        assert response[1]['body']['@name'] == 'foobar2'


async def test_edit_data(container_requester):
    """Check a value from registry."""
    async with container_requester as requester:
        await requester(
            'POST', '/db/guillotina', data=json.dumps({
                '@type': 'Item',
                'id': 'foobar1'
            }))
        await requester(
            'POST', '/db/guillotina', data=json.dumps({
                '@type': 'Item',
                'id': 'foobar2'
            }))
        response, _ = await requester(
            'POST',
            '/db/guillotina/@batch',
            data=json.dumps([{
                'method': 'PATCH',
                'endpoint': 'foobar1',
                'payload': {
                    "title": "Foobar1 changed"
                }
            }, {
                'method': 'PATCH',
                'endpoint': 'foobar2',
                'payload': {
                    "title": "Foobar2 changed"
                }
            }])
        )
        response, _ = await requester(
            'POST',
            '/db/guillotina/@batch',
            data=json.dumps([{
                'method': 'GET',
                'endpoint': 'foobar1'
            }, {
                'method': 'GET',
                'endpoint': 'foobar2'
            }])
        )
        assert len(response) == 2
        assert response[0]['body']['title'] == 'Foobar1 changed'
        assert response[1]['body']['title'] == 'Foobar2 changed'
