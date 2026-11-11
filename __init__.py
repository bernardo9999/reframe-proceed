"""Hermes plugin registration for Reframe, Proceed."""

from pathlib import Path

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

    skills_dir = Path(__file__).parent / "skills"
    if skills_dir.is_dir():
        for child in sorted(skills_dir.iterdir()):
            skill_md = child / "SKILL.md"
            if child.is_dir() and skill_md.is_file():
                ctx.register_skill(child.name, skill_md)
