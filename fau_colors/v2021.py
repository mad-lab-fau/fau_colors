from collections import namedtuple
from itertools import product

import seaborn as sns
from typing_extensions import Literal

from fau_colors._utils import custom_blend_colormap, get_register_func, get_unregister_func

__all__ = [
    "colors",
    "colors_all",
    "colors_dark",
    "colors_light",
    "cmaps",
    "cmaps_with_names",
    "register_cmaps",
    "unregister_cmaps",
]

NAMED_COLORS_T = Literal["fau", "tech", "phil", "med", "nat", "wiso"]
NAMED_COLORS = ["fau", "tech", "phil", "med", "nat", "wiso"]

_FacultyColors = namedtuple("FacultyColors", NAMED_COLORS)
_FacultyColorsAll = namedtuple(
    "FacultyColorsAll",
    [f"{a}{b}" for a, b in product(NAMED_COLORS, ("", "_dark", "_light"))],
)
_CmapsAll = namedtuple(
    "Cmaps",
    [
        "faculties",
        "faculties_dark",
        "faculties_light",
        "faculties_all",
        *_FacultyColorsAll._fields,
    ],
)

_LIGHTNESS_LEVELS = [0.125, 0.25, 0.375, 0.625, 1]

colors = _FacultyColors(
    fau="#002F6C",
    tech="#779FB5",
    phil="#FFB81C",
    med="#00A3E0",
    nat="#43B02A",
    wiso="#C8102E",
)
colors_dark = _FacultyColors(
    fau="#041E42",
    tech="#41748D",
    phil="#E87722",
    med="#0061A0",
    nat="#228848",
    wiso="#971B2F",
)

colors_light = _FacultyColors(
    fau="#5F7CA3",
    tech="#AAC3D1",
    phil="#FFD271",
    med="#5FC5EC",
    nat="#89CD79",
    wiso="#DC697C",
)

colors_all: _FacultyColorsAll = _FacultyColorsAll(
    **colors._asdict(),
    **{f"{k}_dark": v for k, v in colors_dark._asdict().items()},
    **{f"{k}_light": v for k, v in colors_light._asdict().items()},
)


lightened_colors = {}
reversed_light_levels = _LIGHTNESS_LEVELS[::-1]
lightness_name_postfix = [f"-{int(i*1000)}" if i != 1 else "" for i in reversed_light_levels]
for name, color in colors_all._asdict().items():
    lightened_colors[name] = (
        [f"fau-{name.replace('_', '-')}{p}" for p in lightness_name_postfix],
        custom_blend_colormap(["#FFFFFF", color], reversed_light_levels),
    )

cmaps_with_names = _CmapsAll(
    faculties=([f"fau-{f}" for f in colors._fields], sns.color_palette(list(colors), as_cmap=True)),
    faculties_dark=([f"fau-{f}-dark" for f in colors_dark._fields], sns.color_palette(list(colors_dark), as_cmap=True)),
    faculties_light=(
        [f"fau-{f}-light" for f in colors_light._fields],
        sns.color_palette(list(colors_light), as_cmap=True),
    ),
    faculties_all=(
        [f"fau-{f.replace('_', '-')}" for f in colors_all._fields],
        sns.color_palette(list(colors_all), as_cmap=True),
    ),
    **lightened_colors,
)

cmaps = _CmapsAll(**{name: cmap[1] for name, cmap in cmaps_with_names._asdict().items()})

register_cmaps = get_register_func(cmaps)
unregister_cmaps = get_unregister_func(cmaps)
