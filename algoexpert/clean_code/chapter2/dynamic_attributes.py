"""
При попытке получить атрибут у класса выполняются методы класса в последовательности:

1. __getattribute__
2. __getattr__
"""
from dataclasses import dataclass


@dataclass
class DynamicAttribute:
    attr: str

    def __getattr__(self, item):
        prefix = 'test_'
        if item.startswith(prefix):
            return item.replace(prefix, '')
        raise AttributeError(f'{self.__class__.__name__} has no attribute {item}')


if __name__ == '__main__':
    dynamic_attribute = DynamicAttribute('value')
    print(dynamic_attribute.attr)
    print(dynamic_attribute.test_value)
