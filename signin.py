from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder

Window.size= (400, 700)
Window.top = 10
Window.left = 50

#Builder.load_file('signin.kv')

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            print("invalid")
        else:
            if uname == 'admin' and passw == 'admin':
                self.parent.parent.current = 'scrn_menu'
            else:
                print("Invalid")

class SigninApp(MDApp):
    def build(self):
        self.title="MaidOnCall"
        
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()
