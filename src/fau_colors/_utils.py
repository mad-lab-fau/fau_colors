from collections.abc import Sequence
from itertools import chain
from pathlib import Path

import matplotlib
from matplotlib.colors import ListedColormap, to_rgb


def custom_blend_colormap(colors: Sequence[str], steps: int = 256) -> list[tuple[float, float, float]]:
    colors = [to_rgb(color) for color in colors]
    name = "blend"
    pal = matplotlib.colors.LinearSegmentedColormap.from_list(name, colors)
    rgb_array = pal(steps)[:, :3]  # no alpha
    pal = list(map(tuple, rgb_array))
    return pal


def get_register_func(cmaps: matplotlib.colors.Colormap) -> None:
    def register() -> None:
        for k, v in cmaps._asdict().items():
            matplotlib.colormaps.register(name=k, cmap=ListedColormap(v))

    return register


def get_unregister_func(cmaps: matplotlib.colors.Colormap) -> None:
    def unregister() -> None:
        for k in cmaps._asdict():
            matplotlib.colormaps.unregister(name=k)

    return unregister


def export_as_gpl(
    colors: Sequence[list[tuple[float, float, float]]],
    file_name: str,
    folder_path: Path,
) -> None:
    assert file_name.endswith("gpl"), "`name` must end with '.gpl'"
    HEADER = f"GIMP Palette\nName: {file_name[:-4]}\n#\n"  # noqa: N806

    color_strings = []
    for rgb in chain(*colors):
        rgb_255 = [f"{int(c * 255)!s:>3}" for c in matplotlib.colors.to_rgb(rgb)]
        color_strings.append(" ".join(rgb_255))

    body = "\n".join(color_strings)
    with Path(folder_path).joinpath(file_name).open("w") as f:
        f.write(HEADER)
        f.write(body)


def export_as_tex(
    colors: Sequence[tuple[list[str], list[tuple[float, float, float]]]],
    file_name: str,
    folder_path: Path,
) -> None:
    assert file_name.endswith("tex"), "`name` must end with '.tex'"
    HEADER = (  # noqa: N806
        f"% Tex color file defining the FAU colors.\n"
        "% To use, you need to include the `xcolor` package (\\usepackage{xcolor} in your preamble).\n"
        f"% Then copy this file into your project and include it with `\\input{{{file_name}}}`.\n\n\n"
    )

    color_strings = []
    for cmap in colors:
        for name, rgb in zip(*cmap, strict=False):
            color_as_rgb = matplotlib.colors.to_rgb(rgb)
            color_strings.append(
                f"\\definecolor{{{name}}}{{rgb}}{{{color_as_rgb[0]}, {color_as_rgb[1]}, {color_as_rgb[2]}}}"
            )

    color_strings = sorted(set(color_strings))

    body = "\n".join(color_strings)
    with Path(folder_path).joinpath(file_name).open("w") as f:
        f.write(HEADER)
        f.write(body)
