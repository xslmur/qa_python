class Button:
    def __init__(self, button_element):
        self.element = button_element

    def click(self):
        self.element.click()

    def is_enabled(self):
        self.element.is_enabled()


class Input:
    def __init__(self, input_element):
        self.element = input_element

    def is_enabled(self):
        self.element.is_enabled()

    def clear(self):
        self.element.clear()

    def send_keys(self, keys):
        self.element.send_keys(keys)


class Link:
    def __init__(self, link_element):
        self.element = link_element

    def click(self):
        return self.element.click()
