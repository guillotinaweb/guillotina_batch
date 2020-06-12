from guillotina import configure
from guillotina.response import HTTPOk
from guillotina.response import Response

import json


@configure.service(
    name="@respond",
    method="POST",
    requestBody={
        "required": False,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "exception": {"type": "boolean", "default": False,},
                    },
                }
            }
        },
    },
    validate=True,
)
async def respond(context, request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        data = {}

    if data.get("exception", False):
        raise Exception("foobar")
    return HTTPOk(content={"foo": "bar"})


@configure.service(
    name="@stream",
    method="GET",
)
async def stream_something(context, request):
    n_chunks = 3
    chunk = "foobar"
    chunk_size = len(chunk)
    total_size = chunk_size * n_chunks
    stream = Response(status=200, content_type="text/plain")
    for i in range(n_chunks):
        await stream.prepare(request)
        await stream.write(chunk.encode())
    await stream.write(eof=True)
    return stream
