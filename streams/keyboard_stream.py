from streams.core_streams.basic_stream import BasicStream
from streams.core_streams.input_stream import InputStream

__all__ = ["KeyboardStream"]


class KeyboardStream(BasicStream, InputStream):
    def __init__(self, stream_name, message_in_console=""):
        super(KeyboardStream, self).__init__(stream_name)
        self.output_message = message_in_console

    def input(self, data=None, *args, **kwargs):
        data = input(self.output_message)
        return data
