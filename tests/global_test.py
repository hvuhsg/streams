import unittest

from streams.fake_input_stream import FakeInputStream
from streams.filter_stream import FilterStream
from streams.print_stream import PrintStream
from streams.system.stream_sys import StreamSystem


class GlobalStreamsTests(unittest.TestCase):
    def test_stream_simple_code(self):
        sys = StreamSystem()

        input = FakeInputStream("user_name", "My username")
        filter = FilterStream("username_length", lambda username: len(username) > 5)
        long = PrintStream("print_long_username", lambda username: 'this is vary long username')
        short = PrintStream("print_short_username", lambda username: 'this is vary short username')

        input.connect(filter)
        filter.connect(long, True)
        filter.connect(short, False)

        sys.add_stream(input)
        sys.add_stream(filter)
        sys.add_stream(long)
        sys.add_stream(short)

        sys.run()

if __name__ == '__main__':
    unittest.main()
