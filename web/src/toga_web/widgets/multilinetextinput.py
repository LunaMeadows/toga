from travertino.size import at_least

from .base import Widget
from toga_web.libs import create_element, js

class MultilineTextInput(Widget):
    def create(self):
        self.native = self._create_native_widget("sl-textarea")

    def set_font(self, font):
        pass

    def get_value(self):
        return self.native.value

    def set_value(self, value):
        self.native.value = value

    def get_readonly(self):
        pass

    def set_readonly(self, value):
        self.native.readOnly = value

    def get_placeholder(self):
        return self.native.placeholder

    def set_placeholder(self, value):
        self.native.placeholder = value

    def focus(self):
        multilinetextinputelem = js.document.getElementById(f'toga_{self.interface.id}')
        multilinetextinputelem.focus()
        #self.native.focus()

    def scroll_to_bottom(self):
        #print(self.interface.id)
        multilinetextinputelem = js.document.getElementById(f'toga_{self.interface.id}')
        multilinetextinputelem.setSelectionRange(0, 0)
        #self.native.

    def scroll_to_top(self):
        pass

    def scroll_to_line(self, position):
        positions_of_new_lines = [0, ] + [i + 1 for i, char in enumerate(str(self.get_value())) if char == '\n']
        multilinetextinputelem = js.document.getElementById(f'toga_{self.interface.id}')
        multilinetextinputelem.setSelectionRange(positions_of_new_lines[int(position)], positions_of_new_lines[int(position)])

    def scroll_to_index(self, position):
        multilinetextinputelem = js.document.getElementById(f'toga_{self.interface.id}')
        multilinetextinputelem.setSelectionRange(position, position)