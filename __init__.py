"""Hermes plugin registration for Reframe, Proceed."""

from . import schemas, tools


def register(ctx):
    """Register the plugin's planning and reflection tools with Hermes."""
    registrations = (
        (schemas.SAVE_VISION, tools.save_vision),
        (schemas.UPDATE_PLAN, tools.update_plan),
        (schemas.DAILY_CHECKIN, tools.daily_checkin),
        (schemas.WEEKLY_REVIEW, tools.weekly_review),
        (schemas.GET_CONTEXT, tools.get_context),
    )
    for schema, handler in registrations:
        ctx.register_tool(
            name=schema["name"],
            toolset="reframe-proceed",
            schema=schema,
            handler=handler,
        )
