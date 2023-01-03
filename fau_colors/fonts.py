from pathlib import Path

from matplotlib import font_manager


def register_fausans_font():
    """Register the FAU Sans font.

    This function tries to register the FAU Sans font by scanning the common font directories.
    If the font is not found, it will throw an error.

    Raises
    ------
    FileNotFoundError
        If the font file is not found.

    """
    possible_paths = [
        Path("/Library/Fonts/FAUSansOffice-Regular.ttf"),  # macOS
        Path("/usr/share/fonts/truetype/fausans/FAUSansOffice-Regular.ttf"),  # Linux
        Path("C:/Windows/Fonts/FAUSansOffice-Regular.ttf"),  # Windows
    ]
    for path in possible_paths:
        if path.exists():
            font_manager.fontManager.addfont(path)
            return

    raise FileNotFoundError(
        "Could not find 'FAUSansOffice-Regular.ttf' on your system. Please install it manually and try again."
    )
