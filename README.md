# Reframe, Proceed

Reframe, Proceed adds tools for recording a long-term personal vision, weekly plans, daily check-ins, and weekly reflections in Hermes.

## Tools

- `reframe_save_vision` saves or updates the current vision, time horizon, and life areas.
- `reframe_update_plan` saves or updates objectives, key results, and actions for a week.
- `reframe_daily_checkin` records progress, energy, blockers, and a next action for a date.
- `reframe_weekly_review` records wins, missed goals, lessons, and adjustments for a week.
- `reframe_get_context` retrieves recent saved records, optionally filtered by section.

## Data and privacy

The plugin stores the text supplied to these tools (vision, plans, check-ins, and reviews) in Hermes-managed plugin storage through `plugin_db("reframe-proceed")`. Hermes scopes plugin storage to the active profile. Records are durable and may remain after the plugin is updated or removed; reinstalling or enabling the plugin can make the same stored records available again.

Saving another vision replaces the current vision. Saving a plan, check-in, or review for the same week/date updates that record rather than creating a second one. `reframe_get_context` returns up to 100 recent records.

In this version, the plugin does not make network requests, run shell commands, read credentials, or send telemetry. It has no third-party Python dependencies. Revisit these disclosures if the implementation changes.

## Development checks

From the plugin directory:

```sh
python -m unittest discover -s tests -v
hermes plugins doctor . --ci
hermes plugins validate . --install-deps
```
