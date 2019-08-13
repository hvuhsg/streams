from streams.core_streams.basic_stream import BasicStream


class FileWriteStream(BasicStream):
    def __init__(self, stream_name, filename):
        super(FileWriteStream, self).__init__(stream_name)
        self._filename = filename

    def input(self, data, *args, **kwargs):
        return open(self._filename, 'ab').write(str(data).encode())
