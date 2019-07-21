from .basic_stream import BasicStream


class PrintStream(BasicStream):
    def __init__(self, stream_name, data_reformat_func):
        super(PrintStream, self).__init__(stream_name)
        self.data_reformat_func = data_reformat_func

    def input(self, data, *args, **kwargs):
        print(self.data_reformat_func(data))
