#интроспекция
import inspect


class NewClass:
    def __init__(self, x):
        self.x = x

    def summ(self, x):
        self.x = x + x


obj = NewClass(4)


def introspection_info(obj):
    print({'type': type(obj).__name__, 'attributes': [getattr(obj, 'x')], 'methods': dir(obj), 'module': obj.__class__.__module__})
#    print({'attributes': [dir(obj) if not callable(getattr(obj, attr))]})

introspection_info(obj)

#print(type(45))