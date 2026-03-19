#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# ID: 980001012
#|==============================================================|#

#SYSTEM LANGUE
dict = {
	"command": {
		"version": "version",
		"clear1": "clear",
		"clear2": "cls",
		"settings1": "settings",
		"screen": "screen",
		"width": "width",
        "exit1": "exit",
        "exit2": "stop"
    }
}

"""

"""
cli_code = {
    #BASIC COMMANDS
    "exit": "f2",
    "quit": "f2",
    "stop": "f2",
    "clear": "f155",
    "cls": "f155",
    "debug": "f8",
    "runtype": "f30",
    "inputtype": "f40",
    #BASIC FUNCTIONS
    "file": {
        "index": "fileindex",
        "open": "f1360"
	},
    #ALL THE SYSTEM PAGES
	"pages": {
        #
        "index": "pagesindex",
		"settings": {
			"index": "p100",
            "system": "p110",
            "screen": "p120",
            "profile": "p170"
		}
	},
    #SETTINGS PAGE
    "settings": {
        "index": "p100",
		"screen": {
			"index": "f100", #All screen settings
			"clear": "tedasy_error", #Just a screen clear
			"width": "f170", #Change screen width
			"height": "f180" #Change screen height
		},
        "profile": {
            "index": "f500", #All profile settings
            "current": "f510",
            "open": "f520",
            "change": "tedasy_error"
		},
        "database": {
            "index": "f700",
            "open": "f720",
            "new": "f730",
            "change": "tedasy_error",
            "name": "tedasy_error"
        }
	}
}
code = cli_code
exp_code ={}