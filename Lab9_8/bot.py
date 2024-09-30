import subprocess
from datetime import datetime

class Bot:
    def bot(self):
        # Assign Activity
        variable1 = True

        # Assign Activity
        variable2 = True

        # If Activity
        if variable1 and variable2:
            # Print Activity
            print("Ambas variables 1 y 2 son verdaderas")


        # If Activity
        if variable1 or variable2:
            # Print Activity
            print("Al menos una de las variables es verdadera")


        # If Activity
        if not variable1 and not variable2:
            # Print Activity
            print("Ninguna de las variables es verdadera")



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()