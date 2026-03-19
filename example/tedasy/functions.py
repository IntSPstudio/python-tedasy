#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# ID: 980001012
#|==============================================================|#

#LIBRARIES
from tedasy import main as mst

#USER INPUT CODES TO FUNCTIONS
#(Prio 1: System codes, Prio 2: Software codes)
def main(input_raw):
    input_rawlen = len(input_raw)
    input_mode: int = input_raw[input_rawlen-1]
    input_rawlen = input_rawlen -1
    output = input_raw

    #SYSTEM FUNCTIONS
    if input_mode == 5:
        #MAIN
        if input_raw[0] == "f2": mst.sys_exit() #EXIT
        elif input_raw[0] == "f155": mst.cli_screen_clear() #CLEAR
        #DATABASE
        elif input_raw[0] == "f720": mst.sys_database_load(output) #OPEN
        #PROFILE
        elif input_raw[0] == "f520": mst.sys_database_load(output) #OPEN
    return output