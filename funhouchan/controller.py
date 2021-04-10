import discord
from discord.ext import commands

from feature.funhou import Funhou

class Controller(object):
    def __init__(self, TOKEN):
        self.bot = commands.Bot(command_prefix='?')
        self.TOKEN = TOKEN
        self.funhou = None

    def run(self):
        @self.bot.event
        async def on_ready():
            print("funhouchan Activated!")

        @self.bot.command()
        async def funhou_set(ctx, user_name, sender_channel_id, dest_channel_id):
            channel_id = [sender_channel_id, dest_channel_id]
            if hasattr(self, "funhou"):
                del self.funhou
            self.funhou = Funhou(bot=self.bot, user_name=user_name, channel_id=channel_id)
            await self.funhou.set_channel()
        
        self.bot.run(self.TOKEN)