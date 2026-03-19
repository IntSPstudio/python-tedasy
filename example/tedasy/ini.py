#|==============================================================|#
# Made by IntSPstudio
# TEDASY
# ID: 980001012
#|==============================================================|#

ini_page = {
    "P01": {
        "Title": "Settings",
        "R01": {
            "Title": "Info"
        },
        "R02": {
            "Title": "Files",
            "Link": "P03"
        },
        "R03": {
            "Title": "Profile",
            "Link": "P04"
        },
        "R04": {
            "Title": "Interface",
            "Link": "P05"
        },
        "R05": {
            "Title": "Debug"
        },
        "R06": {
            "Title": "Wizard",
            "Link": "F9010"
        },
        "R07": {
            "Title": "Exit",
            "Link": "f2"
        },
    },
    "P03": {
        "Title": "File settings",
        "R01": {
            "Title": "Default location (Empty = Local)",
            "Input": "f750",
            "Link": "P01"
        },
        "R02": {
            "Title": "Exit",
            "Link": "P01"
        }
    },
    "P04": {
        "Title": "Profile settings",
        "R01": {
            "Title": "Load",
            "Input": "f520"
        },
        "R02": {
            "Title": "Manage"
        },
        "R03": {
            "Title": "Exit",
            "Link": "P01"
        }
    },
    "P05": {
        "Title": "User interface settings",
        "R01": {
            "Title": "Screen width (Empty = Auto)",
            "Input": "f170"
        },
        "R02": {
            "Title": "Screen height (Empty = Auto)",
            "Input": "f180"
        },
        "R03": {
            "Title": "Exit",
            "Link": "P01"
        }
    }
}