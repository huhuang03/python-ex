import sys

def _is_win():
    return sys.platform == "win32"

def _is_mac():
    return sys.platform == "darwin"

sys.is_win = _is_win
sys.is_mac = _is_mac