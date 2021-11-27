# FAU - Colors

[![PyPI](https://img.shields.io/pypi/v/fau-colors)](https://pypi.org/project/fau-colors/)
![GitHub](https://img.shields.io/github/license/mad-lab-fau/fau_colors)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fau-colors)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mad-lab-fau/fau_colors)


The official colors of Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU) as 
[matplotlib](https://matplotlib.org/) / [seaborn](https://seaborn.pydata.org/) colormaps.

We support the old colors based on the 
2019 CI-guidelines <!-- formerly available on https://www.intern.fau.de/files/2020/03/FAU-Design-Manual.pdf --> and the brand new
[2021 Brand redesign](https://www.doc.zuv.fau.de//M/Styleguide/FAU_Styleguide.pdf).

## Installation

```bash
pip install fau-colors
```

## Quick Guide

#### 2021 colormaps

![2021 colors](_docs/cms_21.png)

```python
import seaborn as sns

from fau_colors import register_cmaps
register_cmaps()

sns.set_palette("tech")
```

#### 2019 colormaps

![2019 colors](_docs/cms_19.png)

```python
import seaborn as sns

from fau_colors.v2019 import register_cmaps
register_cmaps()

sns.set_palette("tech")
```

## General Usage

The 2019 and the 2021 colors are available in the separate submodules `fau_colors.v2019` and `fau_colors.v2021` that 
contain equivalent functions.

**Note:** For convenience, the `v2021` colors can also be accessed from the top-level. In the following examples we
will use this shorter notation.

The methods below show the usage with the new color scheme.
For the old colors simply replace the module name.

### Registering color palettes

The easiest way to use the provided color palettes is to register them as global matplotlib colormaps.
This can be done by calling the `register_cmaps()` function from the respective submodule.
All available cmaps can be seen in the images above.

#### 2021 colors
```pycon
>>> from fau_colors import register_cmaps  # v2021 colors
>>> register_cmaps()
```

#### 2019 colors
```pycon
>>> from fau_colors.v2019 import register_cmaps
>>> register_cmaps()
```

**WARNING: The 2019 and 2021 cmaps have overlapping names! This means you can not register both at the same time.
You need to call `unregister_cmaps` from the correct module first, before you can register the other colormaps.
If you need colormaps from both CI-guides, use them individually, as shown below.**


### Getting the raw colors

All primary faculty colors are stored in a `namedtuple` called `colors`.


#### 2021 colors
```pycon
>>> from fau_colors import colors  # v2021 colors
>>> colors
FacultyColors(fau='#002F6C', tech='#779FB5', phil='#FFB81C', med='#00A3E0', nat='#43B02A', wiso='#C8102E')
>>> colors.fau
'#002F6C'
```

#### 2019 colors
```pycon
>>> from fau_colors.v2019 import colors
>>> colors
FacultyColors(fau='#003865', tech='#98a4ae', phil='#c99313', med='#00b1eb', nat='#009b77', wiso='#8d1429')
>>> colors.fau
'##003865'
```

For the 2021 color scheme also the variable `colors_dark` and `colors_all` are available. They contain the dark variant 
of each color, as well as light and dark colors combined, respectively.

### Manually getting the colormaps

The colormaps are stored in a `namedtuple` called `cmaps`.
There are colormaps for the primary colors and colormaps with varying lightness using each color as the base color.
The latter colormaps contain 5 colors each with 12.5, 25, 37.5, 62.5, and 100% value of the base color.
If you need more than 5 colors see below.

#### 2021 colors
```pycon
>>> from fau_colors import cmaps  # v2021 colors
>>> # Only get the names here
>>> cmaps._fields
('faculties', 'faculties_dark', 'faculties_all', 'fau', 'fau_dark', 'tech', 'tech_dark', 'phil', 'phil_dark', 'med', 'med_dark', 'nat', 'nat_dark', 'wiso', 'wiso_dark')
>>> cmaps.fau_dark
[(0.01568627450980392, 0.11764705882352941, 0.25882352941176473), (0.3823913879277201, 0.4463667820069205, 0.5349480968858131), (0.629434832756632, 0.6678200692041523, 0.7209688581314879), (0.7529565551710881, 0.7785467128027682, 0.8139792387543252), (0.876478277585544, 0.889273356401384, 0.9069896193771626)]
>>> import seaborn as sns
>>> sns.set_palette(cmaps.fau_dark)
```


#### 2019 colors
```pycon
>>> from fau_colors.v2019 import cmaps
>>> # Only get the names here
>>> cmaps._fields
('faculties', 'fau', 'tech', 'phil', 'med', 'nat', 'wiso')
>>> cmaps.fau
[(0.0, 0.2196078431372549, 0.396078431372549), (0.37254901960784315, 0.5103421760861206, 0.6210688196847366), (0.6235294117647059, 0.7062053056516724, 0.772641291810842), (0.7490196078431373, 0.8041368704344483, 0.8484275278738946), (0.8745098039215686, 0.9020684352172241, 0.9242137639369473)]
>>> import seaborn as sns
>>> sns.set_palette(cmaps.fau)
```

### Modifying the colormaps

Sometimes five colors are not enough for a colormap.
The easiest way to generate more colors is to use one of the FAU colors as base and then create custom sequential
palettes from it.
This can be done using `sns.light_palette` or `sns.dark_palette`, as explained 
[here](https://seaborn.pydata.org/tutorial/color_palettes.html#custom-sequential-palettes).

#### 2021 colors
```pycon
>>> from fau_colors import colors  # v2021 colors
>>> import seaborn as sns
>>> sns.light_palette(colors.med, n_colors=8)
[(0.9370639121761148, 0.9445189791516921, 0.9520035391049294), (0.8047725363394869, 0.9014173378043252, 0.9416168802970363), (0.6688064000629526, 0.8571184286417537, 0.9309417031889239), (0.5365150242263246, 0.8140167872943868, 0.9205550443810308), (0.40054888794979027, 0.7697178781318151, 0.9098798672729183), (0.2682575121131623, 0.7266162367844482, 0.8994932084650251), (0.13229137583662798, 0.6823173276218767, 0.8888180313569127), (0.0, 0.6392156862745098, 0.8784313725490196)]
```

#### 2019 colors
```pycon
>>> from fau_colors.v2019 import colors
>>> import seaborn as sns
>>> sns.light_palette(colors.med, n_colors=8)
[(0.9363137612705862, 0.94473936725293, 0.9520047198366567), (0.8041282890912094, 0.9093574773431737, 0.9477078597351495), (0.6682709982401831, 0.8729927571581465, 0.9432916424086003), (0.5360855260608062, 0.8376108672483904, 0.9389947823070931), (0.40022823520978, 0.8012461470633632, 0.9345785649805439), (0.2680427630304031, 0.765864257153607, 0.9302817048790367), (0.13218547217937693, 0.7294995369685797, 0.9258654875524875), (0.0, 0.6941176470588235, 0.9215686274509803)]c
```
