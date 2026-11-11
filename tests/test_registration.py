import importlib.util
import sys
import types
import unittest
from pathlib import Path


PLUGIN_DIR = Path(__file__).resolve().parents[1]

# The handlers import Hermes' storage API; registration itself doesn't use it.
plugins = types.ModuleType("plugins")
plugins.__path__ = []
storage = types.ModuleType("plugins.plugin_storage")
storage.plugin_db = lambda _name: None
sys.modules.setdefault("plugins", plugins)
sys.modules.setdefault("plugins.plugin_storage", storage)

spec = importlib.util.spec_from_file_location(
    "reframe_proceed",
    PLUGIN_DIR / "__init__.py",
    submodule_search_locations=[str(PLUGIN_DIR)],
)
plugin = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = plugin
spec.loader.exec_module(plugin)


class RecordingContext:
    def __init__(self):
        self.tools = []

    def register_tool(self, **kwargs):
        self.tools.append(kwargs)


class RegistrationTests(unittest.TestCase):
    def test_register_wires_each_declared_tool_to_its_handler(self):
        context = RecordingContext()

        plugin.register(context)

        self.assertEqual(
            [entry["name"] for entry in context.tools],
            [
                "reframe_save_vision",
                "reframe_update_plan",
                "reframe_daily_checkin",
                "reframe_weekly_review",
                "reframe_get_context",
            ],
        )
        self.assertTrue(all(callable(entry["handler"]) for entry in context.tools))
        self.assertTrue(
            all(entry["schema"]["name"] == entry["name"] for entry in context.tools)
        )
