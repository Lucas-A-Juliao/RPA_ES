from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
import re
import pdfplumber

class Bot:
    def bot(self):
        # Open PDF Activity
        instancePDF = pdfplumber.open("C:\\Users\\HP\\Downloads\\nf\\S1-19872022.pdf")

        #  Table Setytings Activity
        table_settings = {
                "vertical_strategy": "explicit",
                "horizontal_strategy": "explicit",
                "explicit_vertical_lines": [35,539,581],
                "explicit_horizontal_lines": [195,215,235,255,275],
                "snap_tolerance": 3,
                "snap_x_tolerance": 3,
                "snap_y_tolerance": 3,
                "join_tolerance": 3,
                "join_x_tolerance": 3,
                "join_y_tolerance": 3,
                "edge_min_length": 3,
                "min_words_vertical": 3,
                "min_words_horizontal": 1,
                "intersection_tolerance": 3,
                "intersection_x_tolerance": 3,
                "intersection_y_tolerance": 3,
                "text_tolerance": 3,
                "text_x_tolerance": 3,
                "text_y_tolerance": 3,
        }

        # Extract PDF Table Activity
        page = instancePDF.pages[0]
        extractTableResult = page.extract_table(table_settings)

        # Debug Table Activity
        page = instancePDF.pages[0]
        imageResult = page.to_image(
                resolution = 72, 
                width = None, 
                height = None, 
                antialias = False, 
                force_mediabox = False)
        imageResult.reset().debug_tablefinder(table_settings)
        imageResult.show()

        # Print Activity
        print(extractTableResult)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()