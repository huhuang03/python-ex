import sys

def _is_win():
    return sys.platform == "win32"

sys.is_win = _is_win
