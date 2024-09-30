from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
import win32com.client

class Bot:
    def bot(self):
        # Open Application Activity
        title = "Conexiones"
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

        # Get Data browser Activity
        dataBrowserResult = []
        startLine = 3
        while True:
            line = {}
            try:
                # SAP Data Browser Column Activity
                line['FLDATE'] = session.findById("/app/con[0]/ses[0]/wnd[0]/usr/lbl[23," + str(startLine) + "]").Text

                startLine = startLine + 2
                dataBrowserResult.append(line)
            except:
                break

        # Print Activity
        print(dataBrowserResult)

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

        # Terminate Process Activity
        deskBot.terminate_process(currentProcess)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()