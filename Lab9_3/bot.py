from botcity.core import *
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

import subprocess
from datetime import datetime
from botcity.web import *

class Bot:
    def bot(self):
        # Assign Activity
        varColor = "Azul"

        # If Activity
        if varColor == "Azul":
            # Print Activity
            print("El color es Azul")


        # ElseIf Activity
        elif varColor == "Verde":
            # Print Activity
            print("El color es Verde")


        # Match Activity
        match varColor:
            case "Azul":
                # Print Activity
                print("El color es Azul")


            case "Verde":
                # Print Activity
                print("El color es verde")




        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()