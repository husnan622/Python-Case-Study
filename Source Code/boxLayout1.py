# boxLayout1.py

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App


Builder.load_file('boxLayout_1.kv')

class MyBox(BoxLayout):
    pass

class boxLayoutApp(App):
    def build(self):
        return MyBox()


if __name__ == '__main__':
    boxLayoutApp().run()
