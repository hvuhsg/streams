import keyboard
from time import sleep

from streams.core_streams.basic_stream import BasicStream
from streams.core_streams.input_stream import InputStream


class KeyboardHookStream(BasicStream, InputStream):
    def __init__(self, stream_name):
        super(KeyboardHookStream, self).__init__(stream_name)
        keyboard.on_press(self._get_pressed_keys)
        self._keys = []

    def _get_pressed_keys(self, e):
        self._keys.append(e.name)

    def input(self, data, *args, **kwargs):
        if not self._keys:
            sleep(0.05)
            return
        return self._keys.pop(-1)
