import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader

from matcher import Matcher


class SplashScreen(Screen):
    pass


class MainScreen(Screen):
    res_label = StringProperty()

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.res_label = ''

    def describe(self, instance):
        camera = self.ids['camera']
        matcher = Matcher(camera)
        score, img = matcher.match()

        sound = SoundLoader.load('audio/camera_shutter_snap.mp3')
        sound.play()

        self.res_label = img + ': ' + str(score)


class MainApp(App):

    def build(self):
        manager = ScreenManager()
        manager.add_widget(SplashScreen(name='splash_screen'))
        manager.add_widget(MainScreen(name='main_screen'))
        return manager


if __name__ == '__main__':
    MainApp().run()
