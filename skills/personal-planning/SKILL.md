---
name: personal-planning
description: Support the user's vision, weekly plans, daily check-ins, and reviews with Reframe, Proceed.
---

# Reframe, Proceed: Personal Planning

Use this skill when the user asks for help setting a long-term personal vision, planning a week, checking in on progress, or reflecting on a completed week. Keep the process user-led and respond in the user's language.

## Principles

- Help the user turn their own priorities into clear, manageable next steps; do not prescribe life goals or imply that productivity defines their worth.
- Ask focused questions when required information is missing. Preserve the user's meaning rather than inventing goals, dates, measures, or commitments.
- Keep check-ins and reviews supportive and nonjudgmental. Treat missed actions as information for adjusting the plan, not as personal failure.
- This is a planning aid, not therapy, medical care, or crisis support. Do not diagnose or present it as such.

## Stored data and consent

The tools save user-provided text in Hermes-managed, profile-scoped plugin storage. Records can persist after the plugin is updated or removed. Before the first save in a conversation, explain this briefly and get the user's explicit agreement to store their information. Do not save information merely because the user discussed it. Do not claim the tools can delete stored records; they provide no deletion operation.

Prefer storing only what is useful to the user's stated planning goal. Do not repeat sensitive history unless it is relevant and the user asks for it.

## Workflow and tools

- For a long-term vision, help the user articulate the vision, horizon, and relevant life areas. Call `reframe_save_vision` only when asked to save it; the `vision` field is required. Be clear that saving a new vision replaces the current one.
- For a weekly plan, agree on the week start date in `YYYY-MM-DD` format and the objectives. Add key results and actions only when the user supplies or approves them. Call `reframe_update_plan` only when asked to save; saving the same week updates that week's plan.
- For a daily check-in, let the user describe progress, energy, blockers, and a next action in their own terms. `progress` is required. Use the user's stated date; if no date is given, explain that omitting it makes the tool use the plugin runtime's current date. Saving again for the same date updates that check-in.
- For a weekly review, ask about wins, unfinished commitments, lessons, and possible adjustments. Confirm the week start date (`YYYY-MM-DD`) before saving; `week_start` is required. Saving again for the same week updates that review.
- Use `reframe_get_context` only when prior saved information would materially help or the user asks for it. Request the narrowest useful section (`vision`, `plans`, `checkins`, `reviews`, or `all`) and a modest limit. Summarize only relevant records; do not dump the user's history.

After a tool call, report what was actually saved or retrieved and whether an existing record was updated. If a call fails, say so plainly and do not imply that data was stored.
