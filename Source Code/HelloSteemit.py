from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
import time

class HelloSteemitIndonesia(BoxLayout):
    def __init__(self, **kwargs):
        super(HelloSteemitIndonesia, self).__init__(**kwargs)

        tombol1 = Button(text="Hello")
        tombol1.bind(on_press=self.hello)
        self.add_widget(tombol1)

        tombol2= Button(text="Steemit")
        tombol2.bind(on_press=self.steemit)
        self.add_widget(tombol2)

        tombol3= Button(text="Indonesia")
        tombol3.bind(on_press=self.indonesia)
        self.add_widget(tombol3)

    def hello(self, obj):
        print("--> Hello terjadi pada waktu %s" % time.ctime())

    def steemit(self, obj):
        print("--> Steemit terjadi pada waktu %s" % time.ctime())

    def indonesia(self, obj):
        print("--> Indonesia terjadi pada waktu %s" % time.ctime())


class HelloSteemitIndonesiaApp(App):
    def build(self):
        return HelloSteemitIndonesia()


if __name__ == "__main__":
    myApp = HelloSteemitIndonesiaApp()
    print("Nama Aplikasi Saya adalah %s " %myApp.name)
    myApp.run()
