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
    
if __name__ == "__main__":
    main()