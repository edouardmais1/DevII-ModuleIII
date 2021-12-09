from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # set the columns
        self.cols = 1

        # cree une seconde boite
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(text="email: "))

        # add input boxes
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        # add widgets
        self.top_grid.add_widget(Label(text="password: "))

        # add input boxes
        self.pswd = TextInput(multiline=False)
        self.top_grid.add_widget(self.pswd)

        # rajouter cette boite dans l'interface
        self.add_widget(self.top_grid)

        # create a submit button
        self.submit = Button(text="Submit", font_size=32)

        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, elem):
        name = self.name.text
        pswd = self.pswd.text

        self.add_widget(Label(text="hello {}, your password is {}".format(name, pswd)))

        self.name.text = ""
        self.pswd.text = ""


class MainInterface(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MainInterface().run()
