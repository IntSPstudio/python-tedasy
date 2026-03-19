#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# ID: 980001012
#|==============================================================|#

#LIBRARIES
from platform import system as plat_sys
import datetime
import os
from sys import exit as shut
from tedasy import dictionary as abc
from tedasy import update as ubc
#from it8c import file_exists
from it8c import vsl_tui_line

#CHECK OS
def sys_os(mode):
	ap = str.lower(plat_sys())
	bp =""
	if ap == "windows":
		if mode == 1:
			bp =1
		elif mode == 2:
			bp ="\\"
		elif mode == 3:
			bp ="cls"
	else:
		if mode == 1:
			bp =2
		elif mode == 2:
			bp ="/"
		elif mode == 3:
			bp ="clear"
	return bp
#ASK TIME AND DATE
def sys_datetime(mode: int):
    #DATE
    date_ref = datetime.datetime.now()
    date_year = date_ref.year
    date_month = date_ref.month
    date_day = date_ref.day
    date_hour = date_ref.hour
    date_minute = date_ref.minute
    date_second = date_ref.second
    if mode == 0:
        output = "{:04d}{:02d}{:02}{:02}{:02}{:02}".format(date_year,date_month,date_day,date_hour,date_minute,date_second)
    elif mode == 1:
        output = "{:04d}.{:02d}.{:02} {:02}:{:02}:{:02}".format(date_year,date_month,date_day,date_hour,date_minute,date_second)
    elif mode == 4:
        output = "{:04d}.{:02d}.{:02}".format(date_year,date_month,date_day)
    elif mode == 6:
        output = "{:02}:{:02}:{:02}".format(date_hour,date_minute,date_second)
    return output
#SYSTEM SHUTDOWN
def sys_exit():
	#TA
	#Pre-shutdown commands here
	#TB
	shut()
#SYSTEM SETTINGS
sys_se = {
	"runtype": "",
	"file": {
		"cwd": os.getcwd(),
		"slash": sys_os(2),
		"url_system": "",
		"url_users": "",
		"url_profile": "",
		"url_database": "",
		"nme_system": "system",
		"nme_database": "database",
		"nme_user": "users",
		"fte_userse": "config",
		"fte_user": ".json",
		"url_profile_config": "",
		"create_folders": 1
	},
	"cli": {
		"top_bar": "",
		"start_ap" :"==]",
		"start_mark": ">>",
		"prefix": "",
		"screen_width": 0,
		"screen_height": 0
	},
	"screen": {
		"width": 0,
		"height": 0
	},
	"asilus_vultur": {
		"fm" :"",
		"fd" :"",
		"fu" :""
	},
	"build": {
		"name": "Tedasy",
		"version": "0.0.0.0"
	},
	"debug": {
		"cli": {
			"print_funct_prc": 0,
			"screen_update": 1
		}
	}
}
"""
def sys_urlstruct_check(x,y,z):
	#MAIN LOCATIONS
	if x !="":
		if not os.path.exists(x): return -1
		s = sys_se["file"]["slash"]
	else: s =""
	sys_se["file"]["url_system"] = x + s + sys_se["file"]["nme_system"]
	sys_se["file"]["url_database"] = x + s + sys_se["file"]["nme_database"]
	sys_se["file"]["url_users"] = x + s + sys_se["file"]["nme_user"]
	#PROFILE LOCATIONS
	y = str(y)
	if y =="": y = "default"
	sys_se["file"]["url_profile"] = sys_se["file"]["url_users"] + sys_se["file"]["slash"] + y
	#PROFILE CONFIG
	sys_se["file"]["url_profile_config"] = sys_se["file"]["url_profile"] + sys_se["file"]["slash"] + sys_se["file"]["fte_userse"] + sys_se["file"]["fte_user"]
#START CHECK
def sys_startcheck(x,y,z):
	#MAIN LOCATIONS
	sys_urlstruct_check(x,y,z)
	if file_exists(sys_se["file"]["url_profile_config"]) == 0: return 0
	#CHECK FOLDERS
	if not os.path.exists(sys_se["file"]["url_system"]): return 0
	elif not os.path.exists(sys_se["file"]["url_database"]): return 0
	elif not os.path.exists(sys_se["file"]["url_users"]): return 0
"""
#START
def sys_start():
	#COMMAND LINE RUN
	if sys_se["runtype"] == 1:
		#SCREEN SETTINGS
		sys_se["cli"]["prefix"] = ">> "
		#
		cli_initialize()
	elif sys_se["runtype"] == 2:
		sys_se["cli"]["prefix"] = "==] "
		#
		cli_initialize()
#IMPORT FROM ANOTHER SOURCE
def import_settings(input,exp_mode):
	#SOFTWARE COMMANDS
	if exp_mode == 4:
		abc.exp_code = input
		ubc.main("f1500")

#MERGE DICTS
def deep_merge(d1, d2):
	for k, v in d2.items():
		if (
			k in d1
			and isinstance(d1[k], dict)
			and isinstance(v, dict)
		):
			deep_merge(d1[k], v)
		else:
			d1[k] = v
	return d1

#|CLI|==========================================================|#

#CLEAR SCREEN
def cli_screen_clear():
	#TA
	ap = sys_se["runtype"]
	bp = sys_se["debug"]["cli"]["screen_update"]

	#TB
	if ap == 1 or ap == 2:
		if bp == 1:
			ca = sys_os(3)
			os.system(ca)
			#VISUALS
			#HEADER
			#FOOTER
#UPDATE SCREEN
def cli_screen_update():
	#SIZE
	if sys_se["cli"]["screen_width"] == 0: sys_se["cli"]["screen_width"] = os.get_terminal_size().columns 
	if sys_se["cli"]["screen_height"] == 0: sys_se["cli"]["screen_height"] = os.get_terminal_size().lines
	#BAR
	sys_se["cli"]["topbar"] = vsl_tui_line(sys_se["cli"]["screen_width"], "=")
#INITIALIZE
def cli_initialize():
	cli_screen_clear()
	cli_screen_update()

#TASKBAR

#|DATABASE|=====================================================|#
def sys_database_load(input):
	pass

#|PROFILE|======================================================|#
def sys_profile_load(x,y,z):
	pass