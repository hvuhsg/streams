from streams.core_streams.junction_stream import JunctionStream


class FilterStream(JunctionStream):
    def __init__(self, stream_name, filter_function):
        super(FilterStream, self).__init__(stream_name)
        self.filter_func = filter_function

    def input(self, data, *args, **kwargs):
        self.next_stream_id = self.filter_func(data)
        return data

    def connect(self, next_stream, next_stream_id, *args, **kwargs):
        if next_stream_id not in (True, False):
            raise TypeError("next_stream_id argument in FilterStream must be bool type.")
        super(FilterStream, self).connect(next_stream, next_stream_id, *args, **kwargs)

