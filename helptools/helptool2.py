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


class MyGrid(Widget):
    #get the id of a TextInput From kv file
    email = ObjectProperty(None)

    def click(self):
        #print Text Input on click
        print(self.email.text)
        print('clicked')
        self.email.text= ''
#Open App
class MyApp(App):
    def build(self):
        return MyGrid()

#Run App
if __name__ == "__main__":
    MyApp().run()