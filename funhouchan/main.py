import os
import discord

def main():
    # Checking token
    TOKEN = os.environ.get("DISCORD_FUNHOUCHAN",None)
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
        
    # Startup and connection
    client.run(TOKEN)

    
if __name__ == "__main__":
    main()