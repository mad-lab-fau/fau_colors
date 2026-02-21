from collections import namedtuple
from contextlib import suppress

import pytest

from fau_colors import _utils, v2021
from fau_colors import register_cmaps as register_2024
from fau_colors import unregister_cmaps as unregister_2024


def _cleanup_2024() -> None:
    with suppress(ValueError):
        unregister_2024()


def _cleanup_2021() -> None:
    with suppress(ValueError):
        v2021.unregister_cmaps()


def test_register_cmaps_is_idempotent_for_same_palette() -> None:
    _cleanup_2024()
    register_2024()

    try:
        register_2024()
    finally:
        _cleanup_2024()


def test_register_cmaps_keeps_conflict_error_for_different_palette() -> None:
    _cleanup_2021()
    _cleanup_2024()
    register_2024()

    try:
        with pytest.raises(ValueError, match="already registered"):
            v2021.register_cmaps()
    finally:
        _cleanup_2021()
        _cleanup_2024()


def test_register_falls_back_to_legacy_matplotlib_cm_api(monkeypatch: pytest.MonkeyPatch) -> None:
    called: dict[str, object] = {}
    LegacyCmaps = namedtuple("LegacyCmaps", ["demo"])

    class LegacyCM:
        @staticmethod
        def register_cmap(*, name: str, cmap: object) -> None:
            called["name"] = name
            called["cmap_type"] = type(cmap).__name__

    monkeypatch.delattr(_utils.matplotlib, "colormaps", raising=False)
    monkeypatch.setattr(_utils.matplotlib, "cm", LegacyCM())

    register = _utils.get_register_func(LegacyCmaps(demo=[(0.0, 0.0, 0.0)]))
    register()

    assert called["name"] == "demo"
    assert called["cmap_type"] == "ListedColormap"
