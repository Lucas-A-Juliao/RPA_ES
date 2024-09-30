from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *
import win32com.client

class Bot:
    def bot(self):
        # Open Application Activity
        title = "SAP Logon 770"
        executablePath = "C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplogon.exe"
        deskBot = DesktopBot()
        deskBot.execute(executablePath)
        deskBot.connect_to_app(backend=Backend.WIN_32, timeout=60000, title=title, path=executablePath)
        popup_Window = deskBot.find_app_window(waiting_time=10000, title=title)

        # SAP Login Activity
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.OpenConnection("SAP", True)
        session = connection.Children(0)
        session.findById("wnd[0]").maximize
        session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "000"
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "SAP*"
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "minisap"
        session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "EN"
        session.findById("wnd[0]").sendVKey(0)

        # Start SAP Transaction Activity
        session.StartTransaction("SE16")

        #  SAP Type Into Activity
        session.findById("/app/con[0]/ses[0]/wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "sflight"

        #  SAP Click Into Activity
        session.findById("/app/con[0]/ses[0]/wnd[0]/tbar[0]/btn[0]").press()

        #  SAP Click Into Activity
        session.findById("/app/con[0]/ses[0]/wnd[0]/tbar[1]/btn[8]").press()

        # SAP Get Table Activity
        tableResult = "/app/con[0]/ses[0]/wnd[0]/usr/cntlGRID1/shellcont/shell"
        tableResultRowCount = session.findById(tableResult).RowCount

        # Assign Activity
        line = 0

        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\RPA\\botcity\\Lab\\Lab_Monitorizacion_test\\Monitor\\Nuevo Microsoft Excel Worksheet.xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet="Sheet1")[1:]
        # While Activity
        while line < tableResultRowCount:
            # SAP Get Cell Value Activity
            fieldDATE = session.findById(tableResult).GetCellValue(line, "FLDATE")

            # If Activity
            if fieldDATE == "":
                # Send Hotkey Activity
                deskBot.page_down(wait=0)

                # Continue Activity
                continue


            # Print Activity
            print(fieldDATE)

            # Set cell Activity
            excelBot.set_cell(column="A", row=line + 1, value=fieldDATE, sheet="Sheet1")

            # Assign Activity
            line = line + 1


        # Write Excel Activity
        excelBot.write(file_or_path="C:\\RPA\\botcity\\Lab\\Lab_Monitorizacion_test\\Monitor\\Nuevo Microsoft Excel Worksheet.xlsx")

        # Terminate SAPAuto Connection Activity
        if "session" in locals():
                session = None
        if "connection" in locals():
                connection = None
        if "application" in locals():
                application = None
        if "SapGuiAuto" in locals():
                SapGuiAuto = None

        # Find Process Activity
        currentProcess = deskBot.find_process(name="saplogon", pid=None)

        # Find Process Activity
        currentProcess = deskBot.find_process(name="saplogon", pid=None)

        # Terminate Process Activity
        deskBot.terminate_process(currentProcess)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()