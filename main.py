from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window


Window.size= (400, 750)
Window.top = 10
Window.left = 50

class MainApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    def build(self):
        screen_manager.add_widget(Builder.load_file("signin.kv"))
        screen_manager.add_widget(Builder.load_file("menu.kv"))
        #screen_manager.add_widget(Builder.load_file("profile.kv"))

        return screen_manager
    def on_start(self):
        screen_manager.current = "MainScreen"
    def ChngScreen(self):
        screen_manager.current = "MainMenu"
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

class MenuApp(MDApp):
    def build(self):
        self.title="MaidOnCall"
        return MainApp()


if __name__ == "__main__":
    oa = MainApp()
    oa.run()
