from telegram.ext import Updater, Filters, MessageHandler
from time import sleep

from ..basic_stream import BasicStream
from ..input_stream import InputStream


class PTBUpdatesStream(BasicStream, InputStream):
    def __init__(self, stream_name, bot_token):
        super(PTBUpdatesStream, self).__init__(stream_name)
        self.bot_token = bot_token
        self.updater = Updater(token=self.bot_token)
        self._messages = []
        self._setup_stream()

    def _setup_stream(self):
        multi_handler = MessageHandler(Filters.all, self._get_messages,
                                       pass_user_data=True,
                                       pass_chat_data=True,
                                       pass_job_queue=True,
                                       pass_update_queue=True)
        self.updater.dispatcher.add_handler(multi_handler)
        self.updater.start_polling()

    def _get_messages(self, bot, update, *args, **kwargs):
        self._messages.append(update)

    def input(self, data, *args, **kwargs):
        if not self._messages:
            sleep(0.5)
            return
        return self._messages.pop()
