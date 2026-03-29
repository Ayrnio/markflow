from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import LineEdit, PushButton

# Single row height avoids a taller outer widget with shorter children (visual misalignment).
_URL_ROW_HEIGHT_PX = 46


class UrlInputBar(QWidget):
    url_submitted = Signal(str)

    def __init__(self, translate, parent=None):
        super().__init__(parent=parent)
        self.translate = translate

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.url_edit = LineEdit(self)
        self.url_edit.returnPressed.connect(self.submit_url)

        self.submit_button = PushButton(self)
        self.submit_button.clicked.connect(self.submit_url)

        self.url_edit.setFixedHeight(_URL_ROW_HEIGHT_PX)
        self.submit_button.setFixedHeight(_URL_ROW_HEIGHT_PX)
        self.setFixedHeight(_URL_ROW_HEIGHT_PX)

        layout.addWidget(self.url_edit, 1)
        layout.addWidget(self.submit_button)

        self.retranslate_ui(translate)

    def submit_url(self) -> None:
        value = self.url_edit.text().strip()
        if value:
            self.url_submitted.emit(value)

    def clear(self) -> None:
        self.url_edit.clear()

    def retranslate_ui(self, translate) -> None:
        self.translate = translate
        self.url_edit.setPlaceholderText(self.translate("home_url_placeholder"))
        self.submit_button.setText(self.translate("home_add_url_button"))
