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

    client = discord.Client()

    # Works on startup
    @client.event
    async def on_ready():
        print("ログインしたよ!")

    # When a message is received
    @client.event
    async def on_message(message):
        # If the sender is a bot
        if message.author.bot:
            return
        
        if message.content == '/funhouchan':
            await message.channel.send("はろー！")
            return

        if message.content == '/setfunhou':
            await message.channel.send("分報のチャンネルIDを教えて!")
            return
        
    bot = commands.Bot(command_prefix='$')

    @bot.command()
    async def test(ctx, arg):
        await ctx.send(arg)

    # Startup and connection
    client.run(TOKEN)

    
if __name__ == "__main__":
    main()