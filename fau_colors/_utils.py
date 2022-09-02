from itertools import chain
from pathlib import Path
from typing import List, Sequence, Tuple

import matplotlib
from matplotlib import cm
from matplotlib.colors import ListedColormap, to_rgb


def custom_blend_colormap(colors, steps):
    colors = [to_rgb(color) for color in colors]
    name = "blend"
    pal = matplotlib.colors.LinearSegmentedColormap.from_list(name, colors)
    rgb_array = pal(steps)[:, :3]  # no alpha
    pal = list((map(tuple, rgb_array)))
    return pal


def get_register_func(cmaps):
    def register():
        for k, v in cmaps._asdict().items():
            cm.register_cmap(name=k, cmap=ListedColormap(v))

    return register


def get_unregister_func(cmaps):
    def unregister():
        for k in cmaps._asdict():
            cm.unregister_cmap(name=k)

    return unregister


def export_as_gpl(colors: Sequence[List[Tuple[float, float, float]]], file_name: str, folder_path: Path):
    assert file_name.endswith("gpl"), "`name` must end with '.gpl'"
    HEADER = f"GIMP Palette\nName: {file_name[:-4]}\n#\n"

    color_strings = []
    for rgb in chain(*colors):
        rgb_255 = [f"{str(int(c * 255)):>3}" for c in matplotlib.colors.to_rgb(rgb)]
        color_strings.append(" ".join(rgb_255))

    body = "\n".join(color_strings)
    with open(Path(folder_path) / file_name, "w") as f:
        f.write(HEADER)
        f.write(body)
