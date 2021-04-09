import os
import discord
from discord.ext import commands

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

    @bot.command()
    async def funhou_set(ctx, user_name, sender_channel_id, dest_channel_id):
        sender_channel = bot.get_channel(int(sender_channel_id))
        dest_channel = bot.get_channel(int(dest_channel_id))
        await sender_channel.send("分報告の送り元はここに設定されたよ!")
        await dest_channel.send("分報の送り先はここに設定されたよ!")

    bot.run(TOKEN)

    
if __name__ == "__main__":
    main()