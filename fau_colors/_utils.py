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
