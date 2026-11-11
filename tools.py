"""Persistent data operations for Reframe, Proceed."""

import json
from datetime import date, datetime, timezone

from plugins.plugin_storage import plugin_db


def _db():
    conn = plugin_db("reframe-proceed")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_type TEXT NOT NULL,
            period TEXT,
            payload TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def _save(record_type, period, payload):
    now = datetime.now(timezone.utc).isoformat()
    conn = _db()

    existing = conn.execute(
        "SELECT id FROM records WHERE record_type=? AND period=?",
        (record_type, period)
    ).fetchone()

    if existing:
        conn.execute(
            """UPDATE records SET payload=?, updated_at=?
               WHERE id=?""",
            (json.dumps(payload, ensure_ascii=False), now, existing[0])
        )
        record_id = existing[0]
    else:
        cursor = conn.execute(
            """INSERT INTO records
               (record_type, period, payload, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?)""",
            (record_type, period,
             json.dumps(payload, ensure_ascii=False), now, now)
        )
        record_id = cursor.lastrowid

    conn.commit()
    return {
        "success": True,
        "record_id": record_id,
        "type": record_type,
        "period": period
    }


def save_vision(params, **kwargs):
    del kwargs
    return json.dumps(_save(
        "vision", "current",
        {
            "vision": params["vision"],
            "horizon": params.get("horizon", "3 years"),
            "areas": params.get("areas", "")
        }
    ), ensure_ascii=False)


def update_plan(params, **kwargs):
    del kwargs
    return json.dumps(_save(
        "plan", params["week_start"],
        {
            "objectives": params["objectives"],
            "key_results": params.get("key_results", ""),
            "actions": params.get("actions", "")
        }
    ), ensure_ascii=False)


def daily_checkin(params, **kwargs):
    del kwargs
    checkin_date = params.get("date") or date.today().isoformat()

    return json.dumps(_save(
        "checkin", checkin_date,
        {
            "progress": params["progress"],
            "energy": params.get("energy", ""),
            "blockers": params.get("blockers", ""),
            "next_action": params.get("next_action", "")
        }
    ), ensure_ascii=False)


def weekly_review(params, **kwargs):
    del kwargs
    return json.dumps(_save(
        "review", params["week_start"],
        {
            "wins": params.get("wins", ""),
            "misses": params.get("misses", ""),
            "lessons": params.get("lessons", ""),
            "adjustments": params.get("adjustments", "")
        }
    ), ensure_ascii=False)


def get_context(params, **kwargs):
    del kwargs
    section = params.get("section", "all")
    limit = max(1, min(int(params.get("limit", 20)), 100))

    type_map = {
        "vision": ["vision"],
        "plans": ["plan"],
        "checkins": ["checkin"],
        "reviews": ["review"]
    }

    conn = _db()

    if section == "all":
        rows = conn.execute(
            """SELECT record_type, period, payload, updated_at
               FROM records ORDER BY updated_at DESC LIMIT ?""",
            (limit,)
        ).fetchall()
    elif section in type_map:
        placeholders = ",".join("?" for _ in type_map[section])
        rows = conn.execute(
            f"""SELECT record_type, period, payload, updated_at
                FROM records WHERE record_type IN ({placeholders})
                ORDER BY updated_at DESC LIMIT ?""",
            (*type_map[section], limit)
        ).fetchall()
    else:
        return json.dumps({"success": False, "error": "Invalid section"})

    records = [
        {
            "type": row[0],
            "period": row[1],
            "data": json.loads(row[2]),
            "updated_at": row[3]
        }
        for row in rows
    ]

    return json.dumps({
        "success": True,
        "section": section,
        "count": len(records),
        "records": records
    }, ensure_ascii=False)
