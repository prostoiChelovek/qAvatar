# -*- coding: utf-8 -*-

# Автор: Люнгрин Андрей aka prostoichelovek <iam.prostoi.chelovek@gmail.com>
# Лицензия: MIT License

import kivy

kivy.require("2.0.0")

from kivy.app import App  # noqa
from kivy.uix.label import Label  # noqa


class MyApp(App):
    def build(self):
        return Label(text="Hello world")


if __name__ == "__main__":
    MyApp().run()
