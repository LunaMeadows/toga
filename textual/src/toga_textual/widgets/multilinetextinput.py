from travertino.size import at_least

from textual.widgets import TextArea
from textual.reactive import reactive

from .base import Widget

class TogaTextArea(TextArea):
    def __init__(self, impl, *args, **kwargs):
        super().__init__()
        self.interface = impl.interface
        self.impl = impl

    # def on_focus(self, event: TextArea.Changed) -> None:
    #     self.interface.on_gain_focus()

    def on_input_changed(self, event: TextArea.Changed) -> None:
        self.interface.on_change()

class MultilineTextInput(Widget):
    def create(self):
        self.native = TogaTextArea(self)
        self.native.soft_wrap = True

    def set_font(self, font):
        pass

    def get_value(self):
        return self.native.text

    def set_value(self, value):
        self.native.text = value

    def get_readonly(self):
        return self.native.disabled

    def set_readonly(self, value):
        #self.native.text = str((self.native))
        self.native.disabled = value

    def get_placeholder(self):
        return self.native.placeholder

    def set_placeholder(self, value):
        self.native.placeholder = value

    def focus(self):
        self.native.focus()

    def scroll_to_bottom(self):
        #self.native.focus()
        self.native.move_cursor([self.native.document.line_count, 0])
        self.native.action_cursor_line_end()

    def scroll_to_top(self):
        #self.native.focus()
        self.native.move_cursor([0, 0])

    def scroll_to_line(self, position):
        self.native.move_cursor([position, 0])

    def scroll_to_index(self, position):
        self.native.move_cursor(self.native.document.get_location_from_index(position))

    @property
    def width_adjustment(self):
        return 2

    @property
    def height_adjustment(self):
        return 2

    def rehint(self):
        self.interface.intrinsic.width = at_least(len(self.native.text) + 4)
        self.interface.intrinsic.height = 7