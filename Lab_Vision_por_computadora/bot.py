from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *

class Bot:
    def bot(self):
        # Open Application Activity
        executablePath = "C:\\RPA\\botcity\\Lab\\Lab_monitor\\Monitor\\Lista_ejemplo.xlsx"
        deskBot = DesktopBot()
        deskBot.execute(executablePath)
        deskBot.connect_to_app(backend=Backend.WIN_32, timeout=60000, path=executablePath)
        popup_Window = deskBot.find_app_window(waiting_time=10000)

        # Wait Activity
        deskBot.wait(10000)

        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\Users\\HP\\Downloads\\Lista_ejemplo (3).xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet="lista")[1:]
        # Print Activity
        print(dataList)

        # Assign Activity
        sitio = "https://jornadarpa.com.br/curso/exercicios/lab100.html"

        # Open Browser Activity
        webBot = WebBot()
        webBot.driver_path = "C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBot.page_load_strategy = "Normal"
        webBot.browse(sitio)

        # Maximize window Activity
        webBot.maximize_window()

        # ForEach Activity
        for item in dataList:
            # If Activity
            if item[0] == "PF":
                # Find Activity
                btnPF = webBot.find("btnPF", x = None, y = None, width = None, height = None, threshold = None, matching = 0.85, waiting_time = 10000, best = True, grayscale = False)

                # Find And Click Activity
                webBot.click()


            # Else Activity
            else:
                # Find Activity
                btnPJ = webBot.find("btnPJ", x = None, y = None, width = None, height = None, threshold = None, matching = 0.85, waiting_time = 10000, best = True, grayscale = False)

                # Find And Click Activity
                webBot.click()


            # Find Activity
            fieldName = webBot.find("fielName", x = None, y = None, width = None, height = None, threshold = None, matching = 0.8, waiting_time = 10000, best = True, grayscale = False)

            # Find And Click Activity
            webBot.click()

            # Type Into Activity
            webBot.paste(text=item[1], wait=0)

            # Find Activity
            fieldDocument = webBot.find("fieldDocument", x = None, y = None, width = None, height = None, threshold = None, matching = 0.5, waiting_time = 10000, best = True, grayscale = False)

            # Find And Click Activity
            webBot.click()

            # Type Into Activity
            webBot.paste(text=item[2], wait=0)

            # Find Activity
            btnConfirm = webBot.find("btnConfirm", x = None, y = None, width = None, height = None, threshold = None, matching = 0.8, waiting_time = 10000, best = True, grayscale = False)

            # Find And Click Activity
            webBot.click()



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()