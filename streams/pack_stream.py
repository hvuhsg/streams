from streams.core_streams.basic_stream import BasicStream


class PackStream(BasicStream):
    def __init__(self, stream_name, number_to_pack=20, packing_function=None):
        super(PackStream, self).__init__(stream_name)
        self.number_to_pack = number_to_pack

        if packing_function is None:
            packing_function = self.default_packing_function
        self.packing_function = packing_function

    def default_packing_function(self, package, new_data):
        if package is None:
            return [new_data]
        package.append(new_data)
        return package

    def input(self, data, *args, **kwargs):
        pass
