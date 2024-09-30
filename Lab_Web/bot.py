from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *

class Bot:
    def bot(self):
        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\Users\\HP\\Downloads\\Lista_ejemplo (3).xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet="lista")[1:]
        # Open Browser Activity
        webBot = WebBot()
        webBot.driver_path = "C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBot.page_load_strategy = "Normal"
        webBot.browse("https://jornadarpa.com.br/curso/exercicios/lab100.html")

        # Find Element Activity
        btnPF = webBot.find_element(selector="pf", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        btnPJ = webBot.find_element(selector="pj", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        fieldName = webBot.find_element(selector="nome", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        fieldDocumento = webBot.find_element(selector="documento", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        btnConfirmar = webBot.find_element(selector="/html/body/div[2]/form/button", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # ForEach Activity
        for item in dataList:
            # If Activity
            if item[0] == "PF":
                # Find And Click Activity
                btnPF.click()


            # Else Activity
            else:
                # Find And Click Activity
                btnPJ.click()


            # Type Into Activity
            fieldName.send_keys(item[1])

            # Print Activity
            print(item[1])

            # Type Into Activity
            fieldDocumento.send_keys(item[2])

            # Find And Click Activity
            btnConfirmar.click()


        # Wait Activity
        webBot.wait(10000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()