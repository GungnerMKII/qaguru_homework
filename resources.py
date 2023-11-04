from pathlib import Path


def path(file):
    return str(Path(__file__).parent.joinpath(f"tests/resources/img/{file}"))
