from kivy.lang import Builder
from kivymd.app import MDapp

class mainWindow(MDapp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('mainWindow.kv')