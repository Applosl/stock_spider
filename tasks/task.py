"""
Task 基础类
"""


class Task(object):
    _name = ''
    _args: dict = {}

    def set_args(self, args: dict = None):
        self._args = {} if args is None else args

    def run(self):
        pass

    def _check_sign(self):
        pass
