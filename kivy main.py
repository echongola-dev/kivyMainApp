import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.1')

class ChongolaApp(App):
    def build(self):
        return Label(text='Hello World, Edio Chongola!')

if __name__ == '__main__':
    ChongolaApp().run()
    
