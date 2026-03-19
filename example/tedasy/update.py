#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# ID: 980001012
#|==============================================================|#

#LIBRARIES
from tedasy import dictionary as abc
from tedasy import main as msc

#MAIN LOOP
def main(udc):
    runtype = msc.sys_se["runtype"]

    if udc == "f250": #Update screen
        #CLI
        if runtype == 1 or runtype == 2:
            msc.cli_screen_update()
    elif udc == "f1500": #Update command line codes
        #CLI
        if runtype == 1 or runtype == 2:
            #DICTIONARYS
            abc.code = msc.deep_merge(abc.cli_code, abc.exp_code)