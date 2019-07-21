from uuid import uuid4
import logging

from .Helpers import class_stream_validate
from .input_stream import InputStream


class StreamSystem(object):
    def __init__(self):
        self.streams = dict()
        self._input_streams = []
        self._streams_count = 0
        self._close = False
        self.logger = logging.getLogger('StreamSystem')

    @class_stream_validate
    def add_stream(self, stream):
        if not stream.name:
            name = str(uuid4())
        else:
            name = stream.name
        self.streams[name] = stream
        if isinstance(stream, InputStream):
            self._input_streams.append(stream)
        self._streams_count += 1

    def stream_loop(self, stream):
        output = None
        while stream:
            output = stream.input(output)
            if output is None:
                break
            stream = stream.next_stream()

    def run(self):
        for input_stream in self._input_streams:  # can be turn to thread system
            self.stream_loop(input_stream)

    def run_loop(self):
        while not self._close:
            self.run()

    def close(self):
        self._close = True
