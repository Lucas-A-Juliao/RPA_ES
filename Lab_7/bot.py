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
        varString = "resultado de la operacion"

        # Assign Activity
        varNumero = 10

        # Assign Activity
        varFloat = 5.2

        # Print Activity
        print(varString, varNumero, varFloat )


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()