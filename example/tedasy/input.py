#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# ID: 980001012
#|==============================================================|#

#IMPORT
from tedasy import dictionary as abc
from tedasy import main as mst

#SCRAMBLING
def find_command(data, keys):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current
#USER INPUT TO CODES
def main(input_raw):
	if input_raw !="":
		try:
			#SETTINGS
			output_mode =5
			output = []
			#run =0
			ap = abc.code
			#RUN TYPE CHECK
			if mst.sys_se["runtype"] == 1 or mst.sys_se["runtype"] == 2:
				#USER INPUT
				parts = input_raw.split()
				#HELP FUNCTION
				if parts[0].lower() == "help":
					pass
				else:
					#
					if parts[-1] == "@":
						value = input(mst.sys_se["cli"]["prefix"])
						keys = parts[:-1]
					elif parts and (parts[-1].isdigit() or not parts[-1].isalpha()):
						value = parts[-1]
						keys = parts[:-1]
					else:
						value = None
						keys = parts
					#SCRAMBLING
					result = find_command(ap, keys)
					#OUTPUT = ORIGINAL OUTPUT
					if result is None:
						output.append(input_raw)
					#OUTPUT = FUNCTION CODES
					elif isinstance(result, dict):
						#INDEX = HOMEPAGE / DEFAULT PAGE
						if "index" in result:
							if value:
								output.append(result)
								output.append(value)
							else:
								output.append(result["index"])
					else:
						if value:
							output.append(result)
							output.append(value)

						else:
							output.append(result)
				#JIC
				if output == []: output = input_raw
				output.append(output_mode)
				return output
		except:
			output = [input_raw, 5]
			return output