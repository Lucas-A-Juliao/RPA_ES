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
        var1 = "ejemplo variable de texto"

        # Assign Activity
        var2 = 10

        # Assign Activity
        var3 = 10.5

        # Assign Activity
        var1 = 9

        # Print Activity
        print(var1,var2,var3)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()