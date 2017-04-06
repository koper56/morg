# basic code from https://github.com/kivy/kivy/blob/master/examples/camera/main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.base import stopTouchApp
import time

Builder.load_string('''
<CameraClick>:
    Camera:
        id: camera
        resolution: (480, 640)
        play: True
    Button:
        text: 'Take photo'
        size_hint_y: None
        height: '50dp'
        pos: 0, 150
        on_press: root.take_photo()
''')


class CameraClick(FloatLayout):
    # Function to capture the images and give them the names
    # according to their captured date F. ex 'Captured as IMG_2017_04_05.png'.
    def take_photo(self):
        camera = self.ids['camera']
        time_format = time.strftime("%Y_%m_%d")
        camera.export_to_png("Set_from_{}.png".format(time_format))
        print("Captured as 'Set_from_{}.png'".format(time_format))
        stopTouchApp()


class CameraModule(App):
    def build(self):
        return CameraClick()