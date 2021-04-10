class Funhou(object):
    
    def __init__(self, bot, user_name, channel_id):
        self.bot = bot
        self._sender_channel_id = int(channel_id[0])
        self._dest_channel_id = int(channel_id[1])
    
    async def set_channel(self):
        sender_channel = self.bot.get_channel(self._sender_channel_id)
        dest_channel = self.bot.get_channel(self._dest_channel_id)
        await sender_channel.send("分報告の送り元はここに設定されたよ!")
        await dest_channel.send("分報の送り先はここに設定されたよ!")