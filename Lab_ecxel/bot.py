from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *

class Bot:
    def bot(self):
        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\Users\\HP\\Downloads\\Lista_ejemplo (1).xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet=None)[1:]
        # As Dataframe Activity - import pandas
        dataFrame = excelBot.as_dataframe(sheet="lista")

        # As list Activity
        dataList = excelBot.as_list(sheet=None)

        # Print Activity
        print(listData)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()