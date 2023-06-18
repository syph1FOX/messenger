import PySide6  # noqa: F401
from __feature__ import snake_case, true_property  # type: ignore  # noqa: F401
from PySide6.QtWidgets import QApplication

from server.main_server import Server

if __name__ == "__main__":
    port = 5555
    import sys
    a = QApplication(sys.argv)

    server = Server(port)
    sys.exit(a.exec())
