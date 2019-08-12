__all__ = ["BasicStream"]


class BasicStream:
    def __init__(self, stream_name: str = None) -> None:
        self.name = stream_name
        self._next_stream = None

    def input(self, data, *args, **kwargs):
        """
        read data from buffer
        :param data: data that move in the stream
        :return data: None if there is nothing to return
        """
        return None

    def connect(self, next_stream, *args, **kwargs) -> None:
        self._next_stream = next_stream

    def next_stream(self):
        return self._next_stream
