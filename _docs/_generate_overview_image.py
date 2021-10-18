from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

import fau_colors.v2019 as ci19
import fau_colors.v2021 as ci21

HERE = Path(__file__).parent


def show_cmaps(names, out="colormaps.png"):
    """display all colormaps included in the names list. If names is None, all
    defined colormaps will be shown."""
    # base code from http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps
    matplotlib.rc("text", usetex=False)
    a = np.outer(np.arange(0, 1, 0.01), np.ones(10))  # pseudo image data
    f = plt.figure(figsize=(10, 5))
    f.subplots_adjust(top=0.8, bottom=0.05, left=0.01, right=0.99)
    l = len(names)
    for i, m in enumerate(names):
        ax = plt.subplot(1, l, i + 1)
        ax.axis("off")
        plt.imshow(a, aspect="auto", cmap=cm.get_cmap(m), origin="lower")
        plt.title(m, rotation=90, fontsize=10, verticalalignment="bottom")

    f.tight_layout()
    plt.savefig(out, dpi=100)


ci19.register_cmaps()
show_cmaps(ci19.cmaps._fields, out=HERE / "cms_19.png")
ci19.unregister_cmaps()

ci21.register_cmaps()
show_cmaps(ci21.cmaps._fields, out=HERE / "cms_21.png")
