import discord
from discord.ext import commands

from feature.funhou import Funhou

# Controller for funhouchan
class Controller(object):
    def __init__(self, TOKEN):
        self.bot = commands.Bot(command_prefix='?')
        self.TOKEN = TOKEN
        self.funhou = None

    # activate
    def run(self):
        @self.bot.event
        async def on_ready():
            print("funhouchan Activated!")
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if hasattr(self.funhou, "current_channel_id"):
                if message.channel.id == self.funhou.current_channel_id()[0]:
                    author = message.author
                    await self.funhou.send_funhou(author, message_content=message.content)
            await self.bot.process_commands(message)
        
        # temporary
        @self.bot.command()
        async def avatar(ctx, *,  avamember : discord.Member=None):
            userAvatarUrl = avamember.avatar_url
            await ctx.send(userAvatarUrl)

        @self.bot.command()
        async def funhou_set(ctx, user_name, sender_channel_id, dest_channel_id):
            channel_id = [sender_channel_id, dest_channel_id]
            if hasattr(self, "funhou"):
                del self.funhou
            self.funhou = Funhou(bot=self.bot, user_name=user_name, channel_id=channel_id)
            await self.funhou.set_channel()

                
        self.bot.run(self.TOKEN)