from typing import Dict, List, Any

from ninja import Schema


class MsgResponseContract(Schema):
    """A response with a text message"""

    message: str


class FormInvalidResponseContract(Schema):
    """Form errors dict provided by Django from form validation"""

    errors: Dict[str, List[Dict[str, Any]]]
