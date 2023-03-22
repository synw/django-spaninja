from typing import Dict, List, Any

from ninja import Schema


class MsgResponseContract(Schema):
    """A response with a text message

    Args:
        message (str): the text message
    """

    message: str


class FormInvalidResponseContract(Schema):
    """Form errors dict provided by Django from form validation

    Args:
        errors (Dict[str, List[Dict[str, Any]]]): a Django form errors dict
    """

    errors: Dict[str, List[Dict[str, Any]]]
