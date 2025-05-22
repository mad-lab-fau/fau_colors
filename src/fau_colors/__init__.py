__version__ = "1.9.0"

from fau_colors._utils import export_as_gpl, export_as_tex
from fau_colors.fonts import register_fausans_font
from fau_colors.v2024 import (
    cmaps,
    cmaps_with_names,
    colors,
    colors_all,
    colors_dark,
    register_cmaps,
    unregister_cmaps,
)

__all__ = [
    "export_as_gpl",
    "export_as_tex",
    "register_fausans_font",
    "cmaps",
    "cmaps_with_names",
    "colors",
    "colors_all",
    "colors_dark",
    "register_cmaps",
    "unregister_cmaps",
]
