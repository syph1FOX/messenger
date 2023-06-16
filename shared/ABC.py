from abc import ABC, ABCMeta
from typing import Self

import PySide6  # type: ignore # noqa: F401
from __feature__ import snake_case, true_property  # type: ignore  # noqa: F401;
from PySide6.QtCore import QObject

_ShibokenObjectType: type = type(QObject)


class _ShibokenObjectTypeFence(_ShibokenObjectType):
    ...


class _ResolverMeta(_ShibokenObjectTypeFence, ABCMeta, _ShibokenObjectType):
    ...


class QABC(ABC, metaclass=_ResolverMeta):
    """
    Абстрактный базовый класс для создания абстрактных классов,
    наследованных от классов `PySide6` (`QObject` и все, наследующиеся от него)

    ### Важно
    Данный класс должен стоять в начале при определении наследования

    ### Пример
    >>> class MyQtClass(QABC, QObject): ...
    """

    def __new__(cls, *args, **kwargs) -> Self:
        if hasattr(cls, "__abstractmethods__") and cls.__abstractmethods__.__len__() > 0:
            s = "s" if len(cls.__abstractmethods__) > 1 else ""
            raise TypeError(
                f"Can't instantiate abstract class {cls.__name__} "
                f'with abstract method{s} {", ".join(cls.__abstractmethods__)}'
            )

        return super().__new__(cls, *args, **kwargs)


class QSingleton(_ResolverMeta, type):
    """
    Singleton для классов, наследующихся от `QObject`
    Использование:
    >>> class MyClass(metaclass=Singleton):
    >>>     ...
    """

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(type):
    """
    Singleton для классов, наследующихся от `QObject`
    Использование:
    >>> class MyClass(metaclass=Singleton):
    >>>     ...
    """

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
