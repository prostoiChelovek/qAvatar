# -*- coding: utf-8 -*-

# Автор: Люнгрин Андрей aka prostoichelovek <iam.prostoi.chelovek@gmail.com>
# Лицензия: MIT License

import kivy

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from plyer import vibrator

kivy.require("2.0.0")


class Controller(BoxLayout):
    width_input = ObjectProperty(None)
    delay_input = ObjectProperty(None)

    def vibrate(self):
        self.cancel()

        pattern = [0, self.width_input.value / 1000,
                   self.delay_input.value / 1000]
        vibrator.pattern(pattern, repeat=1)
        print(pattern)

    def cancel(self):
        vibrator.cancel()


class ControllerApp(App):
    def build(self):
        return Controller()


if __name__ == "__main__":
    # vibrator.([0, 0.1, 0.1])

    ControllerApp().run()
