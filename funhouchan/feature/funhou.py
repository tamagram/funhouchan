class Funhou(object):
    def __init__(self, bot):
        self.bot = bot
        self._sender_channel_id = None
        self._dest_channel_id = None

    @property
    def sender_channel_id(self):
        return self._sender_channel_id
    @sender_channel_id.setter
    def sender_channel_id(self, channel_id):
        self._sender_channel_id = int(channel_id)

    @property
    def dest_channel_id(self):
        return self._dest_channel_id
    @dest_channel_id.setter
    def dest_channel_id(self, channel_id):
        self._dest_channel_id = int(channel_id)
    
    async def set_channel(self):
        sender_channel = self.bot.get_channel(self._sender_channel_id)
        dest_channel = self.bot.get_channel(self._dest_channel_id)
        await sender_channel.send("分報告の送り元はここに設定されたよ!")
        await dest_channel.send("分報の送り先はここに設定されたよ!")