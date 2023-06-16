from abc import abstractmethod

import PySide6  # type: ignore # noqa: F401
from __feature__ import snake_case, true_property  # type: ignore  # noqa: F401;
from PySide6.QtCore import QMutex, QMutexLocker, QObject, QThread, QWaitCondition

from .ABC import QABC


class ThreadBase(QABC, QThread):
    """
    Абстрактный базовый класс для потоков.


    ### Абстрактные методы
    >>> def thread_workflow(self, *args, **kwargs) -> None: ...
    """

    @abstractmethod
    def thread_workflow(self, *args, **kwargs) -> None:
        raise NotImplementedError

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self._mutex = QMutex()
        self._cond = QWaitCondition()

        self._is_working: bool = False

    def __del__(self) -> None:
        self.stop_work()
        self.delete_later()

    @property
    def is_working(self) -> bool:
        return self._is_working

    @property
    def mutex(self) -> QMutex:
        return self._mutex

    @property
    def cond(self) -> QWaitCondition:
        return self._cond

    def run(self) -> None:
        import sys

        if sys.argv.count("debug_threads") > 0:
            import debugpy  # type: ignore

            debugpy.debug_this_thread()

        self._is_working = True
        self.thread_workflow()
        self._is_working = False

    def stop_work(self) -> None:
        """
        Останавливает работу потока, если в методе `thread_workflow`
        был релизован цикл с использованием атрибута `is_working`.
        Также пробудит поток один раз, неважно, был ли он остановлен

        ### Пример 1

        В данном примере после `on_readyRead` атрибут `_is_working` переключится
        на значение `False`, и после того, как завершится метод `wait_for_readyRead`,
        цикл прервётся, поток закончит свою работу. Помните, что не стоит после такого цикла
        писать еще какой-либо код, не связанный с очисткой данных (сокет трогать не нужно)
        >>> def thread_workflow(self, socket):
        >>>     ...
        >>>     while self.is_working:
        >>>         ...
        >>>         socket.readyRead.connect(self.on_readyRead)
        >>>         self.wait_for_readyRead(socket)
        >>>
        >>> def on_readyRead(self):
        >>>     ...
        >>>     self.stop_work()

        ### Пример 2

        В данном примере наш поток блокируется, пускай есть метод, пробуждающий этот поток,
        после чего начинается новая итерация цикла. Из другого потока мы вызываем метод `stop_work`,
        из-за этого атрибут `_is_working` переключается в состояние `False`,
        а поток пробуждается и, в конечном счёте, заканчивает цикл и завершается
        >>> def thread_workflow(self, socket):
        >>>     ...
        >>>     while self.is_working:
        >>>         ...
        >>>         with QMutexLocker(self.mutex):
        >>>             self.cond.wait(self.mutex)
        >>>
        >>> ...
        >>> thread.stop_work()
        """

        self._is_working = False
        self.quit()
        
        with QMutexLocker(self.mutex):
            self.cond.wake_one()
