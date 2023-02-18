from pathlib import Path

from matplotlib import font_manager
from matplotlib import pyplot as plt


def register_fausans_font():
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
        Path("~/Library/Fonts"),  # macOS
        Path("/usr/local/share/fonts"),  # Linux
        Path("/usr/share/fonts"),  # Linux
        Path("~/.fonts"),  # Linux
        Path("C:/Windows/Fonts/"),  # Windows
    ]
    for path in possible_paths:
        if path.exists():
            font_paths = sorted(path.rglob("FAUSansOffice-*.ttf"))
            for font_path in font_paths:
                if font_path.is_file():
                    # check if font is already registered
                    if "FAUSans Office" in font_manager.fontManager.get_font_names():
                        plt.rcParams["font.family"] = "sans-serif"
                        plt.rcParams["font.sans-serif"] = "FAUSans Office"
                        return
                    font_manager.fontManager.addfont(font_path)
                    print(
                        "Successfully registered FAU Sans font. "
                        "You can now use it in matplotlib by adding the following lines to your code:\n\n"
                        'plt.rcParams["font.family"] = "sans-serif"\n'
                        'plt.rcParams["font.sans-serif"] = "FAUSans Office"'
                    )
                    return

    raise FileNotFoundError(
        "Could not find 'FAUSansOffice-Regular.ttf' on your system. Please install it manually and try again."
    )
