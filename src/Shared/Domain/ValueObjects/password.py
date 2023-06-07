import hashlib


def _encode(plain_text: str) -> str:
    hashed = hashlib.md5(plain_text.encode()).hexdigest()
    return hashed


def _is_encoded(password: str) -> bool:
    return password.startswith("$")


def _encode_password(password: str) -> str:
    if _is_encoded(password):
        return password

    return _encode(password)


class Password:
    def __init__(self, password: str):
        self._password = password
        self._encoded = _encode_password(password)

    def value(self) -> str:
        return self._encoded

    def __str__(self) -> str:
        return self._encoded

    def is_equals(self, password_to_verify: 'Password') -> bool:
        return self._verify_password(password_to_verify.password(), self._encoded)

    def password(self) -> str:
        return self._password

    @staticmethod
    def _verify_password(plain_text: str, hashed_password: str) -> bool:
        return hashlib.md5(plain_text.encode()).hexdigest() == hashed_password

    @staticmethod
    def validate(plain_text: str) -> None:
        if plain_text == '':
            raise ValueError('Password is not valid')

    def pass_(self) -> str:
        return self._password
