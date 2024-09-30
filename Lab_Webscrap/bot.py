from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *
from webscrap import Webscrap

class Bot:
    def bot(self):
        """
        Extraer datos
        """
        # Custom Python Code Activity
        #Mi comentario

        # Open Browser Activity
        webBot = WebBot()
        webBot.driver_path = "C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = True
        webBot.page_load_strategy = "Normal"
        webBot.browse("https://jornadarpa.com.br/alunos/desafios/dataextractioncrm/desafios_crm-clientes.html")

        # Extract DataTable Activity
        ws = Webscrap()
        dataTable = ws.webscrap(inBot=webBot, inXPATH="/html/body/div[4]/section/div/div/div/div/div/div/div/div[2]/div/table", inLines=0,inNext="/html/body/div[4]/section/div/div/div/div/div/div/div/div[3]/div[2]/div/ul/li[5]/a")

        #  Dataframe Pandas to List Activity
        listResult = dataTable.to_dict(orient='records')

        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\Users\\HP\\Downloads\\Lista_ejemplo.xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet=None)[1:]
        # Clear Activity
        excelBot.clear(sheet="lista")

        # Create Sheet Activity
        excelBot.create_sheet(sheet="Clientes")

        # Add Rowns Activity
        excelBot.add_rows(rows=[["ID","Nome","Pais","Cidade","email"] ,listResult], sheet="Clientes")

        # Write Excel Activity
        excelBot.write(file_or_path="C:\\Users\\HP\\Downloads\\Lista_ejemplo.xlsx")


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()