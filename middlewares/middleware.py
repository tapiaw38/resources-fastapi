from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    """ JWT Bearer."""
    def __init__(self, email: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email

    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if auth.credentials:
            data: dict = validate_token(auth.credentials)
            if data["email"] != self.email:
                return HTTPException(status_code=401, detail="Invalid email")
        else:
            return HTTPException(status_code=401, detail="Invalid token")
