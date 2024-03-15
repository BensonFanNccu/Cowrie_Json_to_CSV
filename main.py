import typing

from sys import argv, exit
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLineEdit,
    QApplication,
    QPushButton,
    QLabel,
)
from controller import input_path_dialog, output_path_dialog, execute_submit

PYQT_SLOT = typing.Union[typing.Callable[..., object], QtCore.pyqtBoundSignal]

class GUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.title = "Json to CSV"
        self.left = 10
        self.right = 10
        self.window_width = 500
        self.window_height = 300
        
        self._init_GUI()
        
    def _init_GUI(self) -> None:
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.window_width, self.window_height)
        
        self.input_path_button = self._init_push_button(
            label_text="Input path",
            clicked_connect=lambda: input_path_dialog(self, self.input_path),
        )
        self.input_path = self._init_line_edit()
        
        self.output_path_button = self._init_push_button(
            label_text="Output path",
            clicked_connect=lambda: output_path_dialog(self, self.output_path),
        )
        self.output_path = self._init_line_edit()
        
        self.submit_button = self._init_push_button(
            label_text="Submit",
            clicked_connect=lambda: execute_submit(
                self.input_path.text(), self.output_path.text()
            ),
        )
        
        self._move_and_resize(self.input_path, 200, 0, 280, 40)
        self._move_and_resize(self.input_path_button, 20, 0, 180, 40)

        self._move_and_resize(self.output_path, 200, 50, 280, 40)
        self._move_and_resize(self.output_path_button, 20, 50, 180, 40)
        
        self._move_and_resize(self.submit_button, 20, 150, 180, 40)
        
        self.show()
         
    def _init_label(self, label_text: str = "") -> QLabel:
        label = QLabel(self)
        label.setText(label_text)
        return label

    def _init_line_edit(self, default_text: str = "") -> QLineEdit:
        line_edit = QLineEdit(self)
        line_edit.setText(default_text)
        return line_edit
    
    def _init_push_button(
        self, label_text: str, clicked_connect: "PYQT_SLOT"
    ) -> QPushButton:
        push_button = QPushButton(self)
        push_button.setText(label_text)
        push_button.clicked.connect(clicked_connect)
        return push_button
    
    def _move_and_resize(
        self,
        widget: QWidget,
        move_x: int,
        move_y: int,
        resize_width: int,
        resize_height: int,
    ) -> QWidget:
        widget.move(move_x, move_y)
        widget.resize(resize_width, resize_height)
        return widget
    
if __name__ == "__main__":
    app = QApplication(argv)
    ex = GUI()
    exit(app.exec())
    