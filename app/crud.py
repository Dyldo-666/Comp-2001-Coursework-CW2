from typing import Any, Dict, List, Optional
from .db import get_conn

def _row_to_dict(columns: List[str], row: Any) -> Dict[str, Any]:
    return {columns[i]: row[i] for i in range(len(columns))}

def read_profile_summary(username: str) -> Optional[Dict[str, Any]]:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("EXEC CW2.usp_UserProfile_ReadByUsername ?", username)
        row = cur.fetchone()
        if not row:
            return None
        columns = [d[0] for d in cur.description]
        return _row_to_dict(columns, row)

def list_profiles(limit: int = 50) -> List[Dict[str, Any]]:
    # For listing, query the view directly (safe; no user input used in SQL text)
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT TOP (?) * FROM CW2.vUserProfileSummary ORDER BY CreatedAtUtc DESC", limit)
        rows = cur.fetchall()
        columns = [d[0] for d in cur.description]
        return [_row_to_dict(columns, r) for r in rows]

def create_profile(payload: Dict[str, Any]) -> Dict[str, Any]:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "EXEC CW2.usp_UserProfile_Create ?,?,?,?,?,?,?,?,?,?,?",
            payload["username"],
            payload["email"],
            payload.get("display_name"),
            payload.get("city"),
            payload.get("country"),
            payload.get("date_of_birth"),
            payload.get("height_cm"),
            payload.get("weight_kg"),
            payload.get("preferred_activity_time"),
            payload.get("preferred_language"),
            payload.get("unit_system_code", "ME"),
        )
        return _fetch_success_message(cur)

def update_profile(username: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "EXEC CW2.usp_UserProfile_Update ?,?,?,?,?,?,?,?,?,?",
            username,
            payload.get("display_name"),
            payload.get("city"),
            payload.get("country"),
            payload.get("date_of_birth"),
            payload.get("height_cm"),
            payload.get("weight_kg"),
            payload.get("preferred_activity_time"),
            payload.get("preferred_language"),
            payload.get("unit_system_code"),
        )
        return _fetch_success_message(cur)

def delete_profile(username: str) -> Dict[str, Any]:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("EXEC CW2.usp_UserProfile_Delete ?", username)
        return _fetch_success_message(cur)

def _fetch_success_message(cur) -> Dict[str, Any]:
    row = cur.fetchone()
    if not row:
        return {"success": False, "message": "No response from stored procedure"}
    columns = [d[0] for d in cur.description]
    result = {columns[i].lower(): row[i] for i in range(len(columns))}
    # Expected: success + message
    return result
