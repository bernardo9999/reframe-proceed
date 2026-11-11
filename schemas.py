SAVE_VISION = {
    "name": "reframe_save_vision",
    "description": "Save or update the user's long-term personal transformation vision.",
    "parameters": {
        "type": "object",
        "properties": {
            "vision": {"type": "string", "description": "The user's long-term vision."},
            "horizon": {"type": "string", "description": "Time horizon, normally three years."},
            "areas": {"type": "string", "description": "Important life areas and desired changes."}
        },
        "required": ["vision"]
    }
}

UPDATE_PLAN = {
    "name": "reframe_update_plan",
    "description": "Register or update weekly objectives, key results and planned actions.",
    "parameters": {
        "type": "object",
        "properties": {
            "week_start": {"type": "string", "description": "Week start date in YYYY-MM-DD format."},
            "objectives": {"type": "string", "description": "Weekly objectives."},
            "key_results": {"type": "string", "description": "Measurable key results."},
            "actions": {"type": "string", "description": "Planned actions and deliverables."}
        },
        "required": ["week_start", "objectives"]
    }
}

DAILY_CHECKIN = {
    "name": "reframe_daily_checkin",
    "description": "Record a daily accountability check-in, including progress and blockers.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {"type": "string", "description": "Date in YYYY-MM-DD format."},
            "progress": {"type": "string", "description": "Progress made today."},
            "energy": {"type": "string", "description": "User's perceived energy and focus."},
            "blockers": {"type": "string", "description": "Obstacles or difficulties."},
            "next_action": {"type": "string", "description": "Next concrete action."}
        },
        "required": ["progress"]
    }
}

WEEKLY_REVIEW = {
    "name": "reframe_weekly_review",
    "description": "Record a weekly review of outcomes, misses, lessons and adjustments.",
    "parameters": {
        "type": "object",
        "properties": {
            "week_start": {"type": "string", "description": "Week start date in YYYY-MM-DD format."},
            "wins": {"type": "string", "description": "Achievements and positive outcomes."},
            "misses": {"type": "string", "description": "Unfinished goals and missed commitments."},
            "lessons": {"type": "string", "description": "Insights and lessons learned."},
            "adjustments": {"type": "string", "description": "Changes for the next cycle."}
        },
        "required": ["week_start"]
    }
}

GET_CONTEXT = {
    "name": "reframe_get_context",
    "description": "Retrieve the user's saved vision, weekly plans, check-ins and reviews.",
    "parameters": {
        "type": "object",
        "properties": {
            "section": {
                "type": "string",
                "enum": ["all", "vision", "plans", "checkins", "reviews"],
                "description": "Which part of the user's history to retrieve."
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of recent records."
            }
        },
        "required": []
    }
}
