#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# Thank you for using this software!
# ID: 980001012
#|==============================================================|#

#SETTINGS
import tedasy as syst #SYSTEM
#import core #SOFTWARE (Coming later...)

#MAIN LOOP
def main():
    continuity =1
    input_px = syst.settings["cli"]["prefix"]
    #LOOP
    while continuity == 1:
        #TA
        input_raw = input(input_px)
        if input_raw !="":
            #SYSTEM CODES
            output = syst.user_input(input_raw)
            output = syst.user_command(output)
            #SOFTWARE CODES
            #if output != "":
            #    output = core.user_command(output)
            print("output:", output)

#START
if __name__ == "__main__":
    syst.settings["runtype"] = 1
    syst.start()
    #syst.exp(core.code,4) #Import software functions to system
    #CORE
    #core.start()
    main()