"""Desktop (Electron) removed in this fork — frozen symbols kept as inert no-ops.

Core code imports several of these names directly (``hermes_cli/main.py``) or through
``update_cmd``'s ``_m()`` reflection, so the *surface* must keep existing even though the
implementation (``apps/desktop`` + the desktop glue modules) is gone.
"""
from pathlib import Path


def cmd_gui(args=None):  # pragma: no cover - user-facing notice
    print("Hermes Desktop 已在本 fork 移除。用 `hermes chat` 交互，或 `hermes gateway` 起网关。")
    return 1


def _desktop_build_needed(*_a, **_k):
    return False


def _desktop_dist_exists(*_a, **_k):
    return False


def _desktop_packaged_executable(*_a, **_k):
    return None


def _desktop_macos_relaunchable_fixup(*_a, **_k):
    return False


def _install_rebuilt_desktop_app(*_a, **_k):
    return None


def _installed_desktop_apps(*_a, **_k):
    return []


def _packaged_desktop_current_for_head(*_a, **_k):
    return True  # nothing to build


def _refresh_installed_desktop_apps(*_a, **_k):
    return None


def build_prepared_desktop(*_a, **_k):
    return None


def desktop_userdata_dir():
    return Path.home() / ".hermes" / "desktop-removed"


def desktop_install_record(*_a, **_k):
    return None


def packaged_gui_app_paths(*_a, **_k):
    return []


def gui_install_summary(*_a, **_k):
    return ""


def agent_is_installed(*_a, **_k):
    return False


def uninstall_gui(*_a, **_k):
    return 0


def check_desktop_surface(*_a, **_k):
    return []


def _needs_interpreter(_path):
    return False


ONBOARDING_LATCH_DIRNAME = "onboarding"
