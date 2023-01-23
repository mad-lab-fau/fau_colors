from pathlib import Path

from fau_colors import export_as_gpl, export_as_tex
from fau_colors.v2019 import cmaps as colors_2019
from fau_colors.v2021 import cmaps as colors_2021
from fau_colors.v2021 import cmaps_with_names as colors_2021_with_names

HERE = Path(__file__).parent

export_as_gpl(colors_2021, file_name="fau_colors_2021.gpl", folder_path=HERE)
export_as_gpl(colors_2019, file_name="fau_colors_2019.gpl", folder_path=HERE)


export_as_tex(colors_2021_with_names, file_name="fau_colors_2021.tex", folder_path=HERE)
