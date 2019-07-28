import kivy
#import App
from kivy.app import App
# Import Widgets
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty



class DailySchedule(Widget):
    email = ObjectProperty(None)


class MyApp(App):
    def build(self):
        return DailySchedule()

#Run App
if __name__ == "__main__":
    MyApp().run()