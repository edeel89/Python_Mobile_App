from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout

Window.size= (400, 750)
Window.top = 10
Window.left = 50

Builder.load_file('menu.kv')

class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def NextButton(self):

        func = self.ids.swiper.set_current(self.ids.swiper.get_current_index()+1)
        if self.ids.swiper.get_current_index() == 4:
            self.ids.swiper.set_current(3)
        else:
            func
    def BackButton(self):
        func1 = self.ids.swiper.set_current(self.ids.swiper.get_current_index()-1)
        if self.ids.swiper.get_current_index() == -1:
            self.ids.swiper.set_current(0)
        else:
            func1
class ContentNavigationDrawer(MDBoxLayout):
    pass        
class MenuApp(MDApp):
    def build(self):
        self.title="MaidOnCall"
        return MainMenu()

    

if __name__ == "__main__":
    oa = MenuApp()
    oa.run()