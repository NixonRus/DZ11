#интроспекция
import inspect


class NewClass:
    def __init__(self, x):
        self.x = x

    def summ(self, x):
        self.x = x + x


obj = NewClass(4)


def introspection_info(obj):
    return {'type': type(obj).__name__,
           'attributes': [attr_name for attr_name in dir(obj) if not callable(getattr(obj, attr_name))],
           'methods': [attr_name for attr_name in dir(obj) if callable(getattr(obj, attr_name))],
           'module': obj.__class__.__module__}


number_info = introspection_info(42)
print(number_info)

