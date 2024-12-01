# Импорт модуля для красивого вывода
from pprint import pprint

def introspection_info(obj):
    """
    Функция проводит интроспекцию объекта и возвращает его свойства:
    - тип, атрибуты, методы, модуль.
    """
    result = {}
    # Тип объекта
    result['type'] = type(obj).__name__
    # Атрибуты объекта (невызываемые)
    attributes = [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
    result['attributes'] = attributes
    # Методы объекта (вызываемые)
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    result['methods'] = methods
    # Модуль объекта (или 'Unknown', если нет атрибута)
    result['module'] = getattr(obj, '__module__', 'Unknown')
    return result

# Пример вызова
pprint(introspection_info('str'))
