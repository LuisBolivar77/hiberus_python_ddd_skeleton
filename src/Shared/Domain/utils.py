import re
from turtle import dot
import json


class _Utils:

    @staticmethod
    def ends_with(needle: str, haystack: str) -> bool:
        length = len(needle)
        if length == 0:
            return True

        return haystack[-length:] == needle

    @staticmethod
    def to_snake_case(text: str) -> str:
        if text.islower():
            return text
        else:
            return re.sub(r'([^A-Z\s])([A-Z])', r'\1_\2', text).lower()

    @staticmethod
    def to_camel_case(text: str) -> str:
        return ''.join(word.capitalize() for word in text.split('_'))

    @staticmethod
    def to_pascal_case(text: str) -> str:
        return ''.join(word.capitalize() for word in text.split('_'))

    @staticmethod
    def extract_class_name(obj: object) -> str:
        return obj.__class__.__name__

    @staticmethod
    def dot(array, prepend='') -> dict:
        results = {}
        for key, value in array.items():
            if isinstance(value, dict) and value:
                results.update(dot(value, prepend + key + '.'))
            else:
                results[prepend + key] = value
        return results

    @staticmethod
    def json_encode(values):
        return json.dumps(values)

    @staticmethod
    def json_decode(json_string):
        data = json.loads(json_string)

        if data is None:
            raise ValueError('Unable to parse response body into JSON')

        return data
