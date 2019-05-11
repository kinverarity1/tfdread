import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime
from pathlib import Path

import tfdread


cwd = Path(os.path.dirname(__file__))


def test_ftc():
    with tfdread.open(cwd / "GO7-40-FTC_26-05-16_13-17-29.tfd") as f:
        assert f.to_dict()["timestamp"] == datetime(2016, 5, 26, 13, 17, 29)
