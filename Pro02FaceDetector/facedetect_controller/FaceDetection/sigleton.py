def singleton(cls):
    _instance = {}

    def inner(args):
        if cls not in _instance:
            _instance[cls] = cls(args)
        return _instance[cls]

    return inner


# @singleton
# class Cls(object):
#     def __init__(self):
#         pass
#
#
# cls1 = Cls()
# cls2 = Cls()
# print(id(cls1) == id(cls2))