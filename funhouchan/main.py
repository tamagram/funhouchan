import os
import discord
from discord.ext import commands

from feature import funhou

def main():
    # Checking token
    TOKEN = os.environ.get("DISCORD_FUNHOUCHAN", None)
    if(TOKEN == None):
        print("Please set the token!")
        print("cmd> set DISCORD_FUNHOUCHAN=???")
        print("terminal> export DISCORD_FUNHOUCHAN=???")
        exit()

    bot = commands.Bot(command_prefix='?')

    @bot.event
    async def on_ready():
        print("funhouchan Activated!")


    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)

    feature_funhou = funhou.Funhou(bot)
    @bot.command()
    async def funhou_set(ctx, user_name, sender_channel_id, dest_channel_id):
        feature_funhou.sender_channel_id = sender_channel_id
        feature_funhou.dest_channel_id = dest_channel_id
        await feature_funhou.set_channel()

    bot.run(TOKEN)

    
if __name__ == "__main__":
    main()