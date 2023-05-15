from .base_control import BaseControl
from selenium.webdriver.support.ui import Select


class SelectBox(BaseControl):
    def __init__(self, select_box_element):
        super().__init__(Select(select_box_element))

    def select_by_visible_text(self, text):
        self.element.select_by_visible_text(text)

    def select_by_value(self, value):
        self.element.select_by_value(str(value))

    def is_enabled(self):
        self.element.is_enabled()
