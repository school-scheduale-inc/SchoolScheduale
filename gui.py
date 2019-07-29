import kivy
# import App
from kivy.app import App
# Import Widgets
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout




class MyApp(App):
    def build(self):
        return FloatLayout()


# Run App
if __name__ == "__main__":
    MyApp().run()
