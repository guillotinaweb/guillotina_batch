from guillotina import configure
from guillotina.utils import resolve_dotted_name


@configure.service(
    name="@respond", method="POST",
    requestBody={
        "required": False,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "exception": {
                            "type": "object",
                            "required": ["class"],
                            "properties": {
                                "class": {"type": "string"},
                                "message": {"type": "string"}
                            },
                        },
                        "response": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["class"],
                            "properties": {
                                "class": {"type": "string"},
                                "content": {"type": "object", "properties": {}}
                            },
                        }
                    }
                }
            }
        }
    },
    validate=True
)
async def respond(context, request):
    """Allows to test arbitrary exceptions and responses
    """
    try:
        data = await request.json()
    except json.JSONDecodeError:
        data = None

    if not data:
        return {}

    if "exception" in data:
        kls = resolve_dotted_name(data["exception"]["class"])
        msg = data["exception"]["message"]
        raise kls(msg)

    elif "response" in data:
        kls = resolve_dotted_name(data["response"]["class"])
        content = data["response"]["content"]
        return kls(content=content)

    return {}
