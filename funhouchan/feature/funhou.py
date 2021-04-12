import discord

class Funhou(object):
    
    def __init__(self, bot, user_name, channel_id):
        self.bot = bot
        self._sender_channel_id = int(channel_id[0])
        self._dest_channel_id = int(channel_id[1])

    def current_channel_id(self):
        return [self._sender_channel_id, self._dest_channel_id]
    
    async def set_channel(self):
        sender_channel = self.bot.get_channel(self._sender_channel_id)
        dest_channel = self.bot.get_channel(self._dest_channel_id)
        await sender_channel.send("分報告の送り元はここに設定されたよ!")
        await dest_channel.send("分報の送り先はここに設定されたよ!")

    async def send_funhou(self, author, message_content):
        dest_channel = self.bot.get_channel(self._dest_channel_id)
        await dest_channel.send(author.avatar_url)
        await dest_channel.send(message_content)