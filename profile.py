from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

Window.size= (400, 700)
Window.top = 10
Window.left = 50

Builder.load_file('profile.kv')

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class OperatorApp(MDApp):
    def build(self):
        self.title="MaidOnCall"
        
        return OperatorWindow()

if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()