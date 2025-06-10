from PySide6.QtWidgets import QApplication
import sys
from Elements.Windows.MainWindow import MainWindow

class App(QApplication):
    def __init__(self, args):
        super().__init__()

app = App(sys.argv)

main_window = MainWindow()
main_window.show()

# Start the event loop.
app.exec()