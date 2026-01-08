import os
import httpx
from typing import Any, Dict, Optional

AUTH_BASE = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"

async def get_auth_user(username: str) -> Optional[Dict[str, Any]]:
    """
    Calls the provided Authenticator API.
    This is used as evidence of integration (not for storing passwords).
    """
    timeout = float(os.getenv("AUTH_TIMEOUT", "10"))
    async with httpx.AsyncClient(timeout=timeout) as client:
        # Try common patterns: /{username} or query-based.
        # If your module docs specify a different path, adjust here.
        r = await client.get(f"{AUTH_BASE}/{username}")
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()
