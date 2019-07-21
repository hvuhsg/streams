from functools import wraps

from .basic_stream import BasicStream


def stream_validate(func):
    @wraps(func)
    def wrapped(stream, *args, **kwargs):
        if not isinstance(stream, BasicStream):
            raise TypeError("stream must inherit from BasicStream")
        return func(stream, *args, **kwargs)
    return wrapped


def class_stream_validate(func):
    @wraps(func)
    def wrapped(self, stream, *args, **kwargs):
        if not isinstance(stream, BasicStream):
            raise TypeError("stream must inherit from BasicStream")
        return func(self, stream, *args, **kwargs)
    return wrapped


def check_stream(stream):
    if not isinstance(stream, BasicStream):
        raise TypeError("next_stream argument must inherit from BasicStream")
