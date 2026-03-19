#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# Thank you for using this software!
# ID: 980001012
#|==============================================================|#

#SETTINGS
import tedasy as syst #SYSTEM
history: list = ["","",""]

#EXECUTE FUNCTION
def exec(input, value, mode:int):
    output = []
    output.append(input)
    output.append(value)
    output.append(mode)
    syst.user_command(output)

    if input !="f155":
        if input != None:
            history.append(input +": "+ str(value))

#MAIN LOOP
def show_menu(menu: dict, start_page :str="P01"):
    #TA
    continuity =1
    menu_pa = syst.settings["cli"]["prefix"] #Row start mark
    current_page = start_page
    #MAIN LOOP
    while continuity == 1:
        #CLEAR SCREEN
        exec("f155",0,5)
        #HEADER
        for i in history[-3:]:
            print(i)
        print(syst.settings["cli"]["topbar"])
        print("")
        #TB
        page = menu.get(current_page, {})
        title = page.get("Title", "Unknown")
        print(menu_pa + title)
        #MENU ROWS
        rows = [(key, val) for key, val in page.items() if key.startswith("R")]
        rows.sort()
        if not rows:
            current_page = start_page
        for idx, (key, item) in enumerate(rows, start=1):
            print(menu_pa + f"{idx}. {item['Title']}")
        #USER CHOICE
        try:
            choice = int(input(menu_pa +"?. "))
            if choice < 1 or choice > len(rows):
                print("ERROR")
                continue
        except ValueError:
            if current_page != start_page:
                current_page = start_page
            else:
                print("ERROR")
            continue
        #USER INPUT
        _, selected_item = rows[choice - 1]
        if "Input" in selected_item:
            syst_code = selected_item["Input"]
            user_input = input(menu_pa + "Input: ")
            exec(syst_code, user_input, 5)
        #RETURN VALUE (PAGE OR FUNC)
        _, selected_item = rows[choice - 1]
        next_page = selected_item.get("Link")
        if next_page and next_page in menu:
            current_page = next_page
        else:
            exec(next_page,0,5)
if __name__ == "__main__":
    #TA
    syst.settings["runtype"] = 2
    syst.start()
    #TB
    show_menu(syst.settings_pages, "P01")