from __future__ import annotations

_CODE_OK = 0

class Result:
    def __init__(self, code, msg):
        super().__init__()
        self.code = code or _CODE_OK
        self.msg = msg or ""

    @staticmethod
    def err(msg) -> Result:
        return Result(-1, msg)

    def isOk(self) -> bool:
        return self.code == _CODE_OK

    def requireSuccess(self):
        if not self.isOk():
            raise Exception(self.msg)