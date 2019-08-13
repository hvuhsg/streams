from streams.core_streams.basic_stream import BasicStream


class PackStream(BasicStream):
    def __init__(self, stream_name, number_to_pack=20, packing_function=None):
        super(PackStream, self).__init__(stream_name)
        self.number_to_pack = number_to_pack

        if packing_function is None:
            packing_function = self.default_packing_function
        self.packing_function = packing_function
        self._package = None

    def default_packing_function(self, package, new_data):
        if package is None:
            return [new_data]
        package.append(new_data)
        return package

    def input(self, data, *args, **kwargs):
        if self._package and len(self._package) >= self.number_to_pack:
            self._package = None
        package = self.packing_function(self._package, data)
        self._package = package
        if self._package and len(self._package) >= self.number_to_pack:
            package = self._package
            return package
