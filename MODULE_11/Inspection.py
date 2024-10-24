import sys
import inspect

def introspection_info(obj):
    dict_ = {}
    dict_['type'] = type(obj) # - Тип объекта
    attributes = []
    methods = []
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if callable(attr_value):
            methods.append(attr_name)  # Если атрибут является вызываемым (методом), добавляем в список методов
        else:
            attributes.append(attr_name)  # В противном случае добавляем в список атрибутов
    dict_['attributes'] = attributes # - Атрибуты объекта
    dict_['methods'] = methods # - Методы объекта
    dict_['module'] = inspect.getmodule(obj) # - Модуль, к которому объект принадлежит
    dict_['size'] = sys.getsizeof(obj)

    return dict_


number_info = introspection_info(42)
print(number_info)
