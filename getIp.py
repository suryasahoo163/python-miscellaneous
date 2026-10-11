from kivy.app import App
from kivy.uix.button import Button
class FirstKivy(App):   
    def build(self):       
        return Button(text="Welcome to LikeGeeks!",pos=(60,80),size_hint=(.6,.2))    
FirstKivy().run()