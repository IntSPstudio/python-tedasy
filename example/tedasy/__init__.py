#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# Thank you for using this library!
# 0.0.0.1
# ID: 980001012
#|==============================================================|#

#|PLUGINS|======================================================|#
from tedasy import main
from tedasy import dictionary
from tedasy import input
from tedasy import functions
from tedasy import ini

#|MAIN|=========================================================|#
settings = main.sys_se #SETTINGS
settings_pages = ini.ini_page
abc = dictionary.dict #LANGUE ETC
cba = dictionary.code #CODES

def start_check(x,y,z):
    return main.sys_startcheck(x,y,z)
def start():
    main.sys_start()
def exp(x,y): #LOAD SETTINGS
    main.import_settings(x,y)

def user_input(x): #INPUTS TO CODES
    return input.main(x)
def user_command(x): #SYSTEM COMMANDS
    return functions.main(x)