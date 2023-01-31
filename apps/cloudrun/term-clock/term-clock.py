import os
import time
from rich import print
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt
import random
gmt_offset = 0

one = {
    "1": "████",
    "2": "  ██",
    "3": "  ██",
    "4": "  ██",
    "5": "  ██",
    "6": "  ██",
    "7": "  ██",
}

two = {
    "1": "██████████",
    "2": "        ██",
    "3": "        ██",
    "4": "██████████",
    "5": "██        ",
    "6": "██        ",
    "7": "██████████",
}

three = {
    "1": "██████████",
    "2": "        ██",
    "3": "        ██",
    "4": "    ██████",
    "5": "        ██",
    "6": "        ██",
    "7": "██████████",
}

four = {
    "1": "██      ██",
    "2": "██      ██",
    "3": "██      ██",
    "4": "██████████",
    "5": "        ██",
    "6": "        ██",
    "7": "        ██",
}

five = {
    "1": "██████████",
    "2": "██        ",
    "3": "██        ",
    "4": "██████████",
    "5": "        ██",
    "6": "        ██",
    "7": "██████████",
}

six = {
    "1": "██████████",
    "2": "██        ",
    "3": "██        ",
    "4": "██████████",
    "5": "██      ██",
    "6": "██      ██",
    "7": "██████████",
}

seven = {
    "1": "██████████",
    "2": "        ██",
    "3": "        ██",
    "4": "      ██  ",
    "5": "      ██  ",
    "6": "      ██  ",
    "7": "      ██  ",
}

eight = {
    "1": "██████████",
    "2": "██      ██",
    "3": "██      ██",
    "4": "██████████",
    "5": "██      ██",
    "6": "██      ██",
    "7": "██████████",
}

nine = {
    "1": "██████████",
    "2": "██      ██",
    "3": "██      ██",
    "4": "██████████",
    "5": "        ██",
    "6": "        ██",
    "7": "██████████",
}

zero = {
    "1": "██████████",
    "2": "██      ██",
    "3": "██      ██",
    "4": "██      ██",
    "5": "██      ██",
    "6": "██      ██",
    "7": "██████████",
}

prevtime = ""
while 1 == 1:
    try:
        curr = time.gmtime(time.time())
        hour_offset = curr.tm_hour + gmt_offset
        if hour_offset < 0:
            hour_offset += 24
        hour_offset %= 24
        hourlist = list(str(hour_offset))
        
        if not len(str(curr.tm_min)) == 2:
            minutes = "0" + str(curr.tm_min)
        else:
            minutes = str(curr.tm_min)
        minlist = list(minutes)
        fulltime = str(hour_offset) + str(curr.tm_min)

        if not fulltime == prevtime or not os.get_terminal_size().lines == height:
            row1display = ""
            row2display = ""
            row3display = ""
            row4display = ""
            row5display = ""
            row6display = ""
            row7display = ""


            for num in hourlist:
                if num == "1":
                    row1display += one["1"] + "  "
                    row2display += one["2"] + "  "
                    row3display += one["3"] + "  "
                    row4display += one["4"] + "  "
                    row5display += one["5"] + "  "
                    row6display += one["6"] + "  "
                    row7display += one["7"] + "  "
                elif num == "2":
                    row1display += two["1"] + "  "
                    row2display += two["2"] + "  "
                    row3display += two["3"] + "  "
                    row4display += two["4"] + "  "
                    row5display += two["5"] + "  "
                    row6display += two["6"] + "  "
                    row7display += two["7"] + "  "
                elif num == "3":
                    row1display += three["1"] + "  "
                    row2display += three["2"] + "  "
                    row3display += three["3"] + "  "
                    row4display += three["4"] + "  "
                    row5display += three["5"] + "  "
                    row6display += three["6"] + "  "
                    row7display += three["7"] + "  "
                elif num == "4":
                    row1display += four["1"] + "  "
                    row2display += four["2"] + "  "
                    row3display += four["3"] + "  "
                    row4display += four["4"] + "  "
                    row5display += four["5"] + "  "
                    row6display += four["6"] + "  "
                    row7display += four["7"] + "  "
                elif num == "5":
                    row1display += five["1"] + "  "
                    row2display += five["2"] + "  "
                    row3display += five["3"] + "  "
                    row4display += five["4"] + "  "
                    row5display += five["5"] + "  "
                    row6display += five["6"] + "  "
                    row7display += five["7"] + "  "
                elif num == "6":
                    row1display += six["1"] + "  "
                    row2display += six["2"] + "  "
                    row3display += six["3"] + "  "
                    row4display += six["4"] + "  "
                    row5display += six["5"] + "  "
                    row6display += six["6"] + "  "
                    row7display += six["7"] + "  "
                elif num == "7":
                    row1display += seven["1"] + "  "
                    row2display += seven["2"] + "  "
                    row3display += seven["3"] + "  "
                    row4display += seven["4"] + "  "
                    row5display += seven["5"] + "  "
                    row6display += seven["6"] + "  "
                    row7display += seven["7"] + "  "
                elif num == "8":
                    row1display += eight["1"] + "  "
                    row2display += eight["2"] + "  "
                    row3display += eight["3"] + "  "
                    row4display += eight["4"] + "  "
                    row5display += eight["5"] + "  "
                    row6display += eight["6"] + "  "
                    row7display += eight["7"] + "  "
                elif num == "9":
                    row1display += nine["1"] + "  "
                    row2display += nine["2"] + "  "
                    row3display += nine["3"] + "  "
                    row4display += nine["4"] + "  "
                    row5display += nine["5"] + "  "
                    row6display += nine["6"] + "  "
                    row7display += nine["7"] + "  "
                elif num == "0":
                    row1display += zero["1"] + "  "
                    row2display += zero["2"] + "  "
                    row3display += zero["3"] + "  "
                    row4display += zero["4"] + "  "
                    row5display += zero["5"] + "  "
                    row6display += zero["6"] + "  "
                    row7display += zero["7"] + "  "

            row1display += "    "
            row2display += "██  "
            row3display += "    "
            row4display += "    "
            row5display += "    "
            row6display += "██  "
            row7display += "    "

            for num in minlist:
                if num == "1":
                    row1display += one["1"] + "  "
                    row2display += one["2"] + "  "
                    row3display += one["3"] + "  "
                    row4display += one["4"] + "  "
                    row5display += one["5"] + "  "
                    row6display += one["6"] + "  "
                    row7display += one["7"] + "  "
                elif num == "2":
                    row1display += two["1"] + "  "
                    row2display += two["2"] + "  "
                    row3display += two["3"] + "  "
                    row4display += two["4"] + "  "
                    row5display += two["5"] + "  "
                    row6display += two["6"] + "  "
                    row7display += two["7"] + "  "
                elif num == "3":
                    row1display += three["1"] + "  "
                    row2display += three["2"] + "  "
                    row3display += three["3"] + "  "
                    row4display += three["4"] + "  "
                    row5display += three["5"] + "  "
                    row6display += three["6"] + "  "
                    row7display += three["7"] + "  "
                elif num == "4":
                    row1display += four["1"] + "  "
                    row2display += four["2"] + "  "
                    row3display += four["3"] + "  "
                    row4display += four["4"] + "  "
                    row5display += four["5"] + "  "
                    row6display += four["6"] + "  "
                    row7display += four["7"] + "  "
                elif num == "5":
                    row1display += five["1"] + "  "
                    row2display += five["2"] + "  "
                    row3display += five["3"] + "  "
                    row4display += five["4"] + "  "
                    row5display += five["5"] + "  "
                    row6display += five["6"] + "  "
                    row7display += five["7"] + "  "
                elif num == "6":
                    row1display += six["1"] + "  "
                    row2display += six["2"] + "  "
                    row3display += six["3"] + "  "
                    row4display += six["4"] + "  "
                    row5display += six["5"] + "  "
                    row6display += six["6"] + "  "
                    row7display += six["7"] + "  "
                elif num == "7":
                    row1display += seven["1"] + "  "
                    row2display += seven["2"] + "  "
                    row3display += seven["3"] + "  "
                    row4display += seven["4"] + "  "
                    row5display += seven["5"] + "  "
                    row6display += seven["6"] + "  "
                    row7display += seven["7"] + "  "
                elif num == "8":
                    row1display += eight["1"] + "  "
                    row2display += eight["2"] + "  "
                    row3display += eight["3"] + "  "
                    row4display += eight["4"] + "  "
                    row5display += eight["5"] + "  "
                    row6display += eight["6"] + "  "
                    row7display += eight["7"] + "  "
                elif num == "9":
                    row1display += nine["1"] + "  "
                    row2display += nine["2"] + "  "
                    row3display += nine["3"] + "  "
                    row4display += nine["4"] + "  "
                    row5display += nine["5"] + "  "
                    row6display += nine["6"] + "  "
                    row7display += nine["7"] + "  "
                elif num == "0":
                    row1display += zero["1"] + "  "
                    row2display += zero["2"] + "  "
                    row3display += zero["3"] + "  "
                    row4display += zero["4"] + "  "
                    row5display += zero["5"] + "  "
                    row6display += zero["6"] + "  "
                    row7display += zero["7"] + "  "

            print("\n" * (os.get_terminal_size().lines - 9) + "  " + row1display + "\n  " + row2display + "\n  " + row3display + "\n  " + row4display + "\n  " + row5display + "\n  " + row6display + "\n  " + row7display + "\n")
            prevtime = str(hour_offset) + str(curr.tm_min)
            height = os.get_terminal_size().lines
#            time.sleep(1)
    except KeyboardInterrupt:
        choice = Prompt.ask("[orange_red1]▄[/orange_red1][grey100 on orange_red1] (G)MT Offset, (Q)uit [/grey100 on orange_red1][orange_red1]▀[/orange_red1]", default="G", choices=["G", "Q"], show_choices=False, show_default=False)
        if choice == "G": 
            try:
                gmt_offset_input = Prompt.ask("[dark_cyan]▄[/dark_cyan][grey100 on dark_cyan] GMT Offset [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan]", default="0")
                gmt_offset = int(gmt_offset_input)
                prevtime = "balls"
            except: 
                gmt_offset = 0
                prevtime = "balls"
        elif choice == "Q": break
        else: otk = 0