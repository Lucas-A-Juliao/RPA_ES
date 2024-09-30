from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *
from botcity.plugins.files import *
import os
import shutil
from watchdog.observers import *
from watchdog.events import *

class Bot:
    def bot(self):
        # Monitoring Folder Activity
        class MonitorFolderEventHandler(FileSystemEventHandler):
                def __init__(self, callback):
                        self.callback = callback

                def on_created(self, event):
                        self.callback(event.src_path)

        class MonitorFolder:
                def __init__(self, folder_path, recursive=False):
                        self.folder_path = folder_path
                        self.recursive = recursive

                def start_monitoring(self, callback):
                        event_handler = MonitorFolderEventHandler(callback)
                        observer = Observer()
                        observer.schedule(event_handler, self.folder_path, self.recursive)
                        observer.start()

                        try:
                                while True:
                                        time.sleep(2)
                        except KeyboardInterrupt:
                                observer.stop()
                        observer.join()

                def executeReturn(pathFile):
                    time.sleep(2)
                    # Assign Activity
                    sitio = "https://jornadarpa.com.br/curso/exercicios/lab100.html"

                    # Open Browser Activity
                    webBot = WebBot()
                    webBot.driver_path = "C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
                    webBot.browser = Browser.CHROME
                    webBot.headless = False
                    webBot.page_load_strategy = "Normal"
                    webBot.browse(sitio )

                    # Read Excel Activity
                    excelBot = BotExcelPlugin()
                    file_or_path = pathFile

                    dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet="lista")[1:]
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

                    # File Handler Activity - import os
                    fileName = os.path.basename(pathFile)
                    newPath = os.path.join("C:\\RPA\\botcity\\Lab\\Lab_monitor\\Monitor\\Listo", fileName)
                    shutil.move(pathFile, newPath)


        instanceMonitor = MonitorFolder("C:\\RPA\\botcity\\Lab\\Lab_monitor\\Monitor\\Nuevo Dato")
        instanceMonitor.start_monitoring(MonitorFolder.executeReturn)

        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()