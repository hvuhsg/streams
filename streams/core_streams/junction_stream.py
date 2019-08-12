from threading import current_thread

from streams.core_streams.basic_stream import BasicStream
from streams.Helpers import check_stream


class JunctionStream(BasicStream):
    def __init__(self, stream_name):
        super(JunctionStream, self).__init__(stream_name)
        self._next_stream_options = dict()
        self._next_stream_id_storage = dict()  # for multi threading systems

    def connect(self, next_stream, next_stream_id, *args, **kwargs):
        check_stream(next_stream)  # check stream type
        if next_stream_id in self._next_stream_options:
            raise Warning("next_stream_id already defined")
        self._next_stream_options[next_stream_id] = next_stream

    def next_stream(self):
        return self._next_stream_options[self.next_stream_id]

    @property
    def next_stream_id(self):
        return self._next_stream_id_storage[current_thread()]

    @next_stream_id.setter
    def next_stream_id(self, next_stream_id):
        self._next_stream_id_storage[current_thread()] = next_stream_id



