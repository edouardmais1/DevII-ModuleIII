import kivy
from kivy.app import App
from kivy.uix.label import Label

class mainWindow(App):
    def build(self):
        return Label(text="test")

if __name__ == "__main__":
    mainWindow().run()