from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *
import re
import pdfplumber

class Bot:
    def bot(self):
        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\RPA\\botcity\\Lab\\Lab_PDF_RE\\PDF-EXTRACT.xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet="Sheet1")[1:]
        # Open PDF Activity
        instancePDF = pdfplumber.open("C:\\Users\\HP\\Downloads\\nf\\E1-0001-01.pdf")

        #  Extract Text PDF Activity
        page = instancePDF.pages[0]
        extractTextResult = page.extract_text(x_tolerance=3, 
                x_tolerance_ratio=None, 
                y_tolerance=3, 
                layout=False, 
                x_density=7.25, 
                y_density=13, 
                line_dir_render=None, 
                char_dir_render=None
        )

        # Print Activity
        print(extractTextResult)

        # Regex Search Activity
        razaoSocial = re.search("RAZÃO SOCIAL:\s([A-Za-zÀ-ú0-9\s\W\w]+)(?=\s*DISCRIMINAÇÃO)",extractTextResult).group(1)

        # Print Activity
        print(razaoSocial)

        # Regex Search Activity
        cnpj = re.search("CNPJ:\s([A-Za-zÀ-ú0-9\s\W\w]+)(?=\s*RAZÃO)",extractTextResult).group(1)

        # Assign Activity
        listaDatos = [razaoSocial,cnpj]

        # Print Activity
        print(listaDatos)

        # Add Row Activity
        excelBot.add_row(row=listaDatos, sheet="Sheet1")

        # Write Excel Activity
        excelBot.write(file_or_path="C:\\RPA\\botcity\\Lab\\Lab_PDF_RE\\PDF-EXTRACT.xlsx")


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()