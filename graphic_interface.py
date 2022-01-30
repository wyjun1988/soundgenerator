from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from sound_generator import SoundGenerator
from sample_generator import get_sine_samples


class PlayerScreen(GridLayout):
    sg = SoundGenerator()

    def __init__(self, **kwargs):
        super(PlayerScreen, self).__init__(**kwargs)
        self.cols = 3
        bt_set = Button(text='set')
        bt_play = Button(text='play')
        bt_stop = Button(text='stop')
        bt_set.bind(on_press=lambda x: self._set_callback())
        bt_play.bind(on_press=lambda x: self._play_callback())
        bt_stop.bind(on_press=lambda x: self._stop_callback())
        self.add_widget(bt_set)
        self.add_widget(bt_play)
        self.add_widget(bt_stop)

    def _set_callback(self):
        self.sg.generate_using_samples(get_sine_samples(duration=1.0, sampling_rate=44100, frequency=440.0))

    def _play_callback(self):
        self.sg.start_play()

    def _stop_callback(self):
        self.sg.stop_play()


class PlayerGUI(App):

    def build(self):
        return PlayerScreen()


if __name__ == '__main__':
    PlayerGUI().run()
