from collections import namedtuple
from itertools import product

import seaborn as sns
from typing_extensions import Literal

from fau_colors._utils import get_register_func, get_unregister_func

__all__ = [
    "colors",
    "colors_all",
    "colors_dark",
    "cmaps",
    "cmaps_with_names",
    "register_cmaps",
    "unregister_cmaps",
]

from collections import namedtuple

NAMED_COLORS_T = Literal["fau", "tech", "phil", "med", "nat", "wiso"]
NAMED_COLORS = ["fau", "tech", "phil", "med", "nat", "wiso"]

_FacultyColors = namedtuple("FacultyColors", NAMED_COLORS)
_FacultyColorsAll = namedtuple(
    "FacultyColorsAll",
    [*(f"{a}{b}" for a, b in product(NAMED_COLORS, ("", "_dark"))), "black"],
)
_CmapsAll = namedtuple(
    "Cmaps",
    [
        "faculties",
        "faculties_dark",
        "faculties_all",
        *_FacultyColorsAll._fields,
    ],
)

colors = _FacultyColors(
    fau="#04316A",
    tech="#8C9FB1",
    phil="#FDB735",
    med="#18B4F1",
    nat="#7BB725",
    wiso="#C50F3C",
)

colors_dark = _FacultyColors(
    fau="#041E42",
    tech="#2F586E",
    phil="#E87722",
    med="#005287",
    nat="#266141",
    wiso="#971B2F",
)

colors_all: _FacultyColorsAll = _FacultyColorsAll(
    **colors._asdict(),
    **{f"{k}_dark": v for k, v in colors_dark._asdict().items()},
    black="#000000",
)

# Now we generate individuall cmaps for each color at all saturation levels.
lightness_name_postfix = ["", "-625", "-375", "-250", "-125"]
colors_with_light_levels = {
    "fau": ["#04316A", "#617DA1", "#A0B1C6", "#C0CBDA", "#D3DCF2"],
    "fau-dark": ["#041E42", "#617188", "#A0A9B7", "#C0C7D0", "#DFE2E7"],
    "tech": ["#8C9FB1", "#B6C2CE", "#D3DAE1", "#E2E7EB", "#EBF5F7"],
    "tech-dark": ["#2F586E", "#7C96A3", "#B0BFC8", "#CBD5DB", "#E4E9EC"],
    "phil": ["#FDB735", "#FECE76", "#FEE4B2", "#FEEDCC", "#FFF5E0"],
    "phil-dark": ["#EB7722", "#EFA369", "#F6CBAB", "#F9DDC8", "#FCEDE2"],
    "med": ["#18B4F1", "#6DD0F6", "#A7E2FA", "#C5ECFB", "#E3FAFC"],
    "med-dark": ["#005287", "#5E92B3", "#9EBDD1", "#BFD4E1", "#DEE9EF"],
    "nat": ["#7BB725", "#ACD275", "#CDE4AC", "#DEEDC8", "#E6FCDC"],
    "nat-dark": ["#266141", "#769B87", "#ACC3B7", "#C9D7CF", "#E3EBE6"],
    "wiso": ["#C50F3C", "#DD737C", "#EBABAE", "#F1C8C9", "#FCDCE3"],
    "wiso-dark": ["#971B2F", "#BE717D", "#D8A9B1", "#E6C6CB", "#F2E2E5"],
    "black": ["#000000", "#5E5E5E", "#9E9E9E", "#BFBFBF", "#DEDEDE"],
}

cmaps_with_names = _CmapsAll(
    faculties=([f"fau-{f}" for f in colors._fields], sns.color_palette(list(colors), as_cmap=True)),
    faculties_dark=([f"fau-{f}-dark" for f in colors_dark._fields], sns.color_palette(list(colors_dark), as_cmap=True)),
    faculties_all=([f"fau-{f}" for f in colors_all._fields], sns.color_palette(list(colors_all), as_cmap=True)),
    **{
        name.replace("-", "_"): (
            [f"fau-{name}{postfix}" for postfix in lightness_name_postfix],
            sns.color_palette(color_list, as_cmap=True),
        )
        for name, color_list in colors_with_light_levels.items()
    },
)

cmaps = _CmapsAll(**{name: cmap[1] for name, cmap in cmaps_with_names._asdict().items()})

register_cmaps = get_register_func(cmaps)
unregister_cmaps = get_unregister_func(cmaps)
