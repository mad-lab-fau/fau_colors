from collections import namedtuple

import seaborn as sns
from typing_extensions import Literal

from fau_colors._utils import custom_blend_colormap, get_register_func, get_unregister_func

__all__ = ["colors", "cmaps", "register_cmaps", "unregister_cmaps"]


NAMED_COLORS = Literal["fau", "tech", "phil", "med", "nat", "wiso"]
_LIGHTNESS_LEVELS = [0.125, 0.25, 0.375, 0.625, 1]


_FacultyColors = namedtuple("FacultyColors", ["fau", "tech", "phil", "med", "nat", "wiso"])
_CmapsAll = namedtuple("Cmaps", ["faculties", *_FacultyColors._fields])

colors = _FacultyColors(
    fau="#003865",
    tech="#98a4ae",
    phil="#c99313",
    med="#00b1eb",
    nat="#009b77",
    wiso="#8d1429",
)


cmaps = _CmapsAll(
    faculties=sns.color_palette(list(colors)),
    **{
        k: sns.color_palette(custom_blend_colormap(["#FFFFFF", v], list(reversed(_LIGHTNESS_LEVELS))), as_cmap=True)
        for k, v in colors._asdict().items()
    },
)


register_cmaps = get_register_func(cmaps)
unregister_cmaps = get_unregister_func(cmaps)
