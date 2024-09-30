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
        valoresList = 30,40

        # List Activity
        dataList = []
        dataList.append(valoresList)

        # List Activity
        dataList.append(20)

        # Print Activity
        print(dataList)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()