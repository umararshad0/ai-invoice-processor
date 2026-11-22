import hmac

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from app.config import settings


api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def require_api_key(api_key: str | None = Depends(api_key_header)) -> None:
    configured_key = settings.api_key
    if not configured_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="API authentication is not configured.",
        )

    if not api_key or not hmac.compare_digest(
        api_key.encode("utf-8"), configured_key.encode("utf-8")
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key.",
            headers={"WWW-Authenticate": "ApiKey"},
        )
