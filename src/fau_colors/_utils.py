from __future__ import annotations

from itertools import chain
from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib
from matplotlib.colors import ListedColormap, to_rgb

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence


def custom_blend_colormap(colors: Sequence[str], steps: int = 256) -> list[tuple[float, float, float]]:
    colors = [to_rgb(color) for color in colors]
    name = "blend"
    pal = matplotlib.colors.LinearSegmentedColormap.from_list(name, colors)
    rgb_array = pal(steps)[:, :3]  # no alpha
    pal = list(map(tuple, rgb_array))
    return pal


def _get_colormap_registry() -> matplotlib.cm.ColormapRegistry | None:
    try:
        return matplotlib.colormaps
    except AttributeError:
        return None


def _is_same_colormap(name: str, expected_colors: Sequence[str | Sequence[float]]) -> bool:
    registry = _get_colormap_registry()
    if registry is None or name not in registry:
        return False

    registered_cmap = registry[name]
    registered_colors = getattr(registered_cmap, "colors", None)
    if registered_colors is None or len(registered_colors) != len(expected_colors):
        return False

    for i in range(len(expected_colors)):
        registered_rgb = to_rgb(registered_colors[i])
        expected_rgb = to_rgb(expected_colors[i])
        if any(abs(float(registered_rgb[j]) - float(expected_rgb[j])) > 1e-12 for j in range(3)):
            return False

    return True


def _register_colormap(name: str, cmap: ListedColormap) -> None:
    registry = _get_colormap_registry()
    if registry is not None:
        registry.register(name=name, cmap=cmap)
        return

    matplotlib.cm.register_cmap(name=name, cmap=cmap)


def _unregister_colormap(name: str) -> None:
    registry = _get_colormap_registry()
    if registry is not None:
        registry.unregister(name=name)
        return

    matplotlib.cm.unregister_cmap(name=name)


def get_register_func(cmaps: matplotlib.colors.Colormap) -> Callable[[], None]:
    def register() -> None:
        for k, v in cmaps._asdict().items():
            cmap = ListedColormap(v)

            if _is_same_colormap(name=k, expected_colors=cmap.colors):
                continue

            _register_colormap(name=k, cmap=cmap)

    return register


def get_unregister_func(cmaps: matplotlib.colors.Colormap) -> Callable[[], None]:
    def unregister() -> None:
        for k in cmaps._asdict():
            _unregister_colormap(name=k)

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
