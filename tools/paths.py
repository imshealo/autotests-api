from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def testdata_files_path() -> Path:
    """
    Возвращает абсолютный путь к директории clients/testdata/files.

    Returns:
        Path: Абсолютный путь к директории с тестовыми файлами.
    """
    return PROJECT_ROOT / "clients" / "testdata" / "files"
