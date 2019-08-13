from streams.core_streams.basic_stream import BasicStream
from streams.core_streams.input_stream import InputStream


class FakeInputStream(BasicStream, InputStream):
    def __init__(self, stream_name, fake_input):
        super(FakeInputStream, self).__init__(stream_name)
        self.fake_input = fake_input

    def input(self, data, *args, **kwargs):
        return self.fake_input
