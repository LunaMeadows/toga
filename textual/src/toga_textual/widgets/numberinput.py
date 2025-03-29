from travertino.size import at_least

from textual.widgets import Input as TextualInput

from .base import Widget


class TogaInput(TextualInput):
    def __init__(self, impl):
        super().__init__()

        self.interface = impl.interface
        self.impl = impl

    # def on_focus(self, event: TextualInput.Changed) -> None:
    #     self.interface.on_gain_focus()

    def on_input_changed(self, event: TextualInput.Changed) -> None:
        self.interface.on_change()

    def on_input_submitted(self, event: TextualInput.Submitted) -> None:
        self.interface.on_confirm()


class NumberInput(Widget):
    def create(self):
        self.native = TogaInput(self)
        self.native.type = "number"

    def get_readonly(self):
        return self.native.disabled

    def set_readonly(self, value):
        self.native.disabled = value

    def get_placeholder(self):
        return self.native.placeholder

    def set_placeholder(self, value):
        self.native.placeholder = value

    def get_value(self):
        return int(self.native.value)

    def set_value(self, value):
        try:
            self.native.value = value
        except:
            self.native.value = ""

    def set_error(self, error_message):
        pass

    def clear_error(self):
        pass

    def is_valid(self):
        return True

    def set_step(self, step):
        pass

    def set_min_value(self, value):
        pass

    def set_max_value(self, value):
        pass

    @property
    def width_adjustment(self):
        return 2

    @property
    def height_adjustment(self):
        return 2


    def rehint(self):
        self.interface.intrinsic.width = at_least(len(self.native.value) + 4)
        self.interface.intrinsic.height = 3
