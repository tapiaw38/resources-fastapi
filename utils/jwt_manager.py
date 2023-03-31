from jwt import encode, decode


def create_token(data: dict):
    token: str = encode(payload=data, key="secret", algorithm="HS256")
    return token


def validate_token(token: str) -> dict or Exception:
    try:
        return decode(token, "secret", algorithms=["HS256"])
    except Exception as e:
        return e
