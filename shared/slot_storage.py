from functools import partial
from typing import Callable, TypeAlias, TypeVar, overload

from PySide6.QtCore import QObject

QSender = TypeVar("QSender", bound=QObject, contravariant=True)
SlotCallableWithSender: TypeAlias = Callable[[QSender], None]
SlotCallableWithoutSender: TypeAlias = Callable[..., None]
SlotCallable: TypeAlias = SlotCallableWithSender | SlotCallableWithoutSender
Slot: TypeAlias = partial[None]


class SlotStorage:
    """
    Главная цель данного класса - создавать и сохранять `*слоты`, которые предназначены
    для присоединения к сигналам. Такой слот, содержит:
        - Вызываемый объект (`callable`)
        - Объект, который вызвал сигнал (`sender`), или не содержит вовсе, если передано None
        - Параметры, которые принимает `callable` после `sender`, если `sender` вообще принимается
        (`callable` также должен принимать параметры, отправляемые сигналом)

    `*Под слотами подразумевается что-то, что можно передать сигналу для последующего вызова,
    это могут быть функции/методы, функторы и лямбда-функции`

    ### Пример 1
    >>> signal = Signal()
    >>>
    >>> def do_something(info: str):
    >>>     print(info)
    >>>
    >>> info = "Hello world"
    >>>
    >>> slot_storage = SlotStorage()
    >>>
    >>> slot = slot_storage.create_slot(do_something, None, info) # Сначала создаём слот
    >>> slot_storage.store("do_something", slot) # Затем сохраняем его
    >>>                        # ИЛИ
    >>> slot = slot_storage.create_and_store_slot("do_something", do_something, None, info) # Слот создаётся, сразу сохраняется и возвращается для последующего использования
    >>>
    >>> signal.connect(slot)
    >>>                 # ИЛИ
    >>> signal.connect(slot_storage.peek("do_something"))
    >>>
    >>> signal.emit()
    >>> signal.disconnect(slot_storage.pop("do_something"))

    ### Пример 2
    >>> class Foo:
    >>>     signal = Signal(int)
    >>>
    >>>     def __init__(self):
    >>>         self.hello = "Hello"
    >>>
    >>> def do_something(foo: Foo, world: str, num: int):
    >>>     info = f"{foo.hello}, {world}!"
    >>>     for i in range(num):
    >>>         print(info)
    >>>
    >>> foo = Foo()
    >>> slot_storage = SlotStorage()
    >>> world = "world"
    >>>
    >>> slot = slot_storage.create_and_store_slot("do_something", do_something, foo, world)
    >>> foo.signal.connect(slot)
    >>>
    >>> foo.signal.emit(10)
    >>> foo.signal.disconnect(slot_storage.pop("do_something"))
    >>>
    """  # noqa: E501

    def __init__(self) -> None:
        self.__storage: dict[str, Slot] = {}

    @staticmethod
    def create_slot(callable: SlotCallable, sender: QSender | None = None, *args, **kwargs) -> Slot:
        """Только создаёт слот и возвращает его"""

        return partial(callable, sender, *args, **kwargs) if sender is not None else partial(callable, *args, **kwargs)

    def create_and_store_slot(
        self, name: str, callable: SlotCallable, sender: QSender | None = None, *args, **kwargs
    ) -> Slot:
        """Создаёт, сохраняет и возвращает слот"""

        slot = self.create_slot(callable, sender, *args, **kwargs)
        self.store(name, slot)

        return slot

    def peek(self, name: str) -> Slot | None:
        """Возвращает стол, не удаляя его из хранилища"""

        return self.__storage.get(name, None)

    def store(self, name: str, value: Slot) -> None:
        """Сохраняет слот"""

        if name is None or name == "":
            raise ValueError("Slot name cannot be None or Empty")

        if not callable(value):
            raise ValueError("Value must be a Callable")

        self.__storage.update({name: value})

    @overload
    def pop(self, name_or_slot: str) -> Slot | None:
        ...

    @overload
    def pop(self, name_or_slot: Slot) -> Slot | None:
        ...

    def pop(self, name_or_slot: str | Slot) -> Slot | None:
        """Возвращает сохраненный слот и удалаяет его из хранилища"""

        if isinstance(name_or_slot, str):
            return self.__storage.pop(name_or_slot, None)

        if isinstance(name_or_slot, partial):
            slot = name_or_slot
            for _name, _slot in self.__storage.items():
                if _slot == slot:
                    return self.__storage.pop(_name)

        raise ValueError("Slot is not in the storage")