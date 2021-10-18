from collections import namedtuple
from itertools import product

import seaborn as sns
from typing_extensions import Literal

from fau_colors._utils import custom_blend_colormap, get_register_func, get_unregister_func

NAMED_COLORS_T = Literal["fau", "tech", "phil", "med", "nat", "wiso"]
NAMED_COLORS = ["fau", "tech", "phil", "med", "nat", "wiso"]

_DepartmentColors = namedtuple("DepartmentColors", NAMED_COLORS)
_DepartmentColorsAll = namedtuple("DepartmentColorsAll", [f"{a}{b}" for a, b in product(NAMED_COLORS, ("", "_dark"))])
_CmapsAll = namedtuple("Cmaps", ["departments", "departments_dark", "departments_all", *_DepartmentColorsAll._fields])

_LIGHTNESS_LEVELS = [0.125, 0.25, 0.375, 0.625, 1]

colors = _DepartmentColors(
    fau="#002F6C",
    tech="#779FB5",
    phil="#FFB81C",
    med="#00A3E0",
    nat="#43B02A",
    wiso="#C8102E",
)
colors_dark = _DepartmentColors(
    fau="#041E42", tech="#41748D", phil="#E87722", med="#0061A0", nat="#228848", wiso="#971B2F"
)
colors_all: _DepartmentColorsAll = _DepartmentColorsAll(
    **colors._asdict(), **{f"{k}_dark": v for k, v in colors_dark._asdict().items()}
)

cmaps = _CmapsAll(
    departments=sns.color_palette(list(colors), as_cmap=True),
    departments_dark=sns.color_palette(list(colors_dark), as_cmap=True),
    departments_all=sns.color_palette(list(colors_all), as_cmap=True),
    **{
        k: sns.color_palette(custom_blend_colormap(["#FFFFFF", v], list(reversed(_LIGHTNESS_LEVELS))), as_cmap=True)
        for k, v in colors_all._asdict().items()
    },
)

register_cmaps = get_register_func(cmaps)
unregister_cmaps = get_unregister_func(cmaps)
