from pathlib import Path

from matplotlib import font_manager
from matplotlib import pyplot as plt


def register_fausans_font() -> None:
    """Register the FAU Sans font.

    This function tries to register the FAU Sans font by scanning the common font directories.
    If the font is not found, it will throw an error.

    After successful registration, the font can be used in matplotlib by setting the following rcParams:
    >>> import matplotlib.pyplot as plt
    >>> plt.rcParams["font.family"] = "sans-serif"
    >>> plt.rcParams["font.sans-serif"] = "FAUSans Office"


    Raises
    ------
    FileNotFoundError
        If the font file is not found.

    """
    possible_paths = [
        Path("/Library/Fonts"),  # macOS
        Path.home().joinpath("Library/Fonts"),  # macOS
        Path("/usr/local/share/fonts"),  # Linux
        Path("/usr/share/fonts"),  # Linux
        Path.home().joinpath(".fonts"),  # Linux
        Path("C:/Windows/Fonts/"),  # Windows
        Path.home().joinpath("AppData/Local/Microsoft/Windows/Fonts"),  # Windows
    ]

    font_found = False
    for path in possible_paths:
        if path.exists():
            font_paths = sorted(path.rglob("FAUSansOffice-*.ttf"))
            for font_path in font_paths:
                if font_path.is_file():
                    font_manager.fontManager.addfont(font_path)
                    if not font_found and "FAUSans Office" not in font_manager.fontManager.get_font_names():
                        print(
                            "Successfully registered FAU Sans font. "
                            "You can now use it in matplotlib by adding the following lines to your code:\n\n"
                            'plt.rcParams["font.family"] = "sans-serif"\n'
                            'plt.rcParams["font.sans-serif"] = "FAUSans Office"'
                        )
                    font_found = True

    if font_found and "FAUSans Office" in font_manager.fontManager.get_font_names():
        plt.rcParams["font.family"] = "sans-serif"
        plt.rcParams["font.sans-serif"] = "FAUSans Office"
    else:
        raise FileNotFoundError(
            "Could not find 'FAUSans Office' font on your system. Please install it manually and try again."
        )
