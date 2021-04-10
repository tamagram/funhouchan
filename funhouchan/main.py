import os

from controller import Controller 

def main():
    # Checking token
    TOKEN = os.environ.get("DISCORD_FUNHOUCHAN", None)
    if(TOKEN == None):
        print("Please set the token!")
        print("cmd> set DISCORD_FUNHOUCHAN=???")
        print("terminal> export DISCORD_FUNHOUCHAN=???")
        exit()

    

    controller = Controller(TOKEN)
    controller.run()

    # @bot.event
    # async def on_ready():
    #     print("funhouchan Activated!")


    # @bot.command()
    # async def test(ctx, arg):
    #     await ctx.send(arg)

    # @bot.command()
    # async def funhou_set(ctx, user_name, sender_channel_id, dest_channel_id):
    #     channel_id = [sender_channel_id, dest_channel_id]
    #     main_funhou = funhou.Funhou(bot, user_name, channel_id)
    #     await main_funhou.set_channel()

    # @bot.command()
    # async def tashikame(ctx):
    #     if main_funhou == None:
    #         await ctx.send("None!")
    #         return
    #     if main_funhou != None:
    #         await ctx.send("変わってる!")
    #         return
        
    # bot.run(TOKEN)

    
if __name__ == "__main__":
    main()