from .base_control import BaseControl

class TextBox(BaseControl):
    def __init__(self, text_box_element):
        super().__init__(text_box_element)

    def fill_field(self, text):
        self.element.clear()
        self.element.send_keys(text)

    def clean_field(self):
        self.element.clean()

    def is_enabled(self):
        self.element.is_enabled()
