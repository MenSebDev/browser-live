"""Tests Logger."""


from tools.logger import Logger


def test() -> None:
    """Test logger."""
    logger = Logger()

    assert logger is not None
