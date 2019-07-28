import kivy
#import App
from kivy.app import App
# Import Widgets
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# To See How To make A Grid Layout Inside A Grid Layout Watch This - https://www.youtube.com/watch?v=fGWHQA3LhJ8&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=3

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        #Choose Number Of columns
        self.cols = 1
        #Add Label
        self.add_widget(Label(text="your Next Scheduale"))
        #Add Button
        self.button= Button(text='Enter', font_size=40)
        #Bind Function To button
        self.button.bind(on_press=self.function)
        self.add_widget(self.button)
        #Add Entry
        self.Entry=TextInput(multiline=False)
        self.add_widget(self.Entry)
    def function(self, instance):
        print('Button Clicked')
        #get input from Entry
        EntryInput= self.Entry.text
        print(EntryInput)
        #clear Text Box Input
        self.Entry.text=''
#Open App
class My_App(App):
    def build(self):
        return MyGrid()

#Run App
if __name__ == "__main__":
    My_App().run()