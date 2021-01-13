import os
import tkinter.messagebox
import tkinter
import time
import random

root = tkinter.Tk()
# invalid input message
highlight_font = "\033[1;31;40m{}\033[0m"
general_invalid_input_str = "\033[1;31;40mInvalid input, please input again!! \033[0m"
over_len_limit_invalid_input_str = "\033[1;31;40mInput must be {}, please input again!! \033[0m"
zero_input_invalid_input_str = "\033[1;31;40mInput should not be '0', please input again!! \033[0m"
select_menu_str = "please select menu: "
# scode1 message
random_sec_code_num_str = highlight_font.format("Please input secrity code number: ")
# variables
number = "1234567890"
randstr = []

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def openfile(file_path):
    with open(file_path, mode='r') as f:
        filelist = f.read()
    return filelist


def inputbox(showstr, showorder, length):
    """ remind string when asking input

    :param showstr: string reminding input
    :param showorder: indicates input data type, 1 means integer>0, 2 means character, 3 means number, length depending
                    on length
    :param length: indicates input length
    """
    instr = input(showstr)
    if len(instr) != 0:
        if showorder == 1:
            if str.isdigit(instr):
                if instr == "0":
                    print(zero_input_invalid_input_str)
                    return "0"
                else:
                    return instr
            else:
                print(general_invalid_input_str)
                return "0"
        if showorder == 2:
            if str.isalpha(instr):
                if len(instr) != length:
                    print(over_len_limit_invalid_input_str.format(str(length)))
                    return "0"
                else:
                    return instr
            else:
                print(general_invalid_input_str)
                return "0"
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print(over_len_limit_invalid_input_str.format(str(length)))
                    return "0"
                else:
                    return instr
            else:
                print(general_invalid_input_str)
                return "0"
    else:
        print(general_invalid_input_str)
        return "0"


def wfile(sstr, sfile, typeis, smsg, datapath):
    """ output security code to file and console

    :param sstr: security code
    :param sfile: output file name
    :param typeis: if print security code to console, "no" don't print, others string print
    :param smsg: message box message
    :param datapath: output file path

    example: wfile(randstr, "scode1.txt", "", "generated 6 digit security code: ", "codepath")
    """
    mkdir(datapath)
    datafile = os.path.join(datapath, sfile)
    pdata = ""
    with open(datafile, "w") as file:
        for i in range(len(sstr)):
            wdata = str(sstr[i].replace('[', '')).replace(']', '')
            wdata = wdata.replace('''''', '').replace('''''', '')
            file.write(str(wdata))
            pdata += wdata
    print(highlight_font.format(pdata))
    if typeis != 'no':
        tkinter.messagebox.showinfo("Tip", smsg + str(len(sstr)) + "\n security file path")
        root.withdraw()


def mainmenu():
    print("""\033[1;35m
    *************************************************
                 Security code generate
    *************************************************
        1. generate 6 digits security code (e.g. 213563)
        2. generate 9 digits series product security code (e.g. 879-335439)
        3. generate 25 digit mixed product series code (e.g. B2r12-N7Te8-9IET2-FE350-DW2K4)
        4. generate security code with analysis info (e.g. 5A61M0583D2)
        5. generate batch security code with analysis info
        6. generate additional security code (5A61M0583D2)
        7. generate batch of EAN-13 barcode
        8. generate batch of QR code
        9. customer lottery function
        0. exit
    """)

def input_validation(insel):
    if str.isdigit(insel):
        if insel == "0":
            print(general_invalid_input_str)
            return "0"
        else:
            return insel
    else:
        print(general_invalid_input_str)
        return "0"


def scode1(str_choice):
    incount = inputbox(random_sec_code_num_str, 1, 0)
    while int(incount) == 0:
        incount = inputbox(random_sec_code_num_str, 1, 0)
    randstr.clear()
    for i in range(int(incount)):
        randfir = ''
        for j in range(6):
            randfir = randfir + random.choice(number)
        randfir += "\n"
        randstr.append(randfir)
    wfile(randstr, "scode" + str(str_choice) + ".txt", "", "already generate 6 digit security codes: ", "codepath")


def main():
    mainmenu()
    choice = input(highlight_font.format(select_menu_str))
    if len(choice) != 0:
        choice = input_validation(choice)
        if choice == "1":
            scode1(str(choice))
        # if choice == 2:
        #     scode2(str(choice))
        # if choice == 3:
        #     scode3(str(choice))
        # if choice == 4:
        #     scode4(str(choice))
        # if choice == 5:
        #     scode5(str(choice))
        # if choice == 6:
        #     scode6(str(choice))
        # if choice == 7:
        #     scode7(str(choice))
        # if choice == 7:
        #     scode7(str(choice))
    else:
        print(general_invalid_input_str)
        time.sleep(2)


if __name__ == "__main__":
    main()

