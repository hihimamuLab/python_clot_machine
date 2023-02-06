import PySimpleGUI as sg
import random as rd
import time as tm

layout = [
    [sg.Text('スロットマシンです')],
    [sg.Button("実行",key="-submit-")],
    [sg.Output(size=(50,10),key="-OUTPUT-")]
]

window = sg.Window('CNNの出力画像サイズを算出',layout,size=(600,300))

rotation_count = rd.randint(10,20)
while True:
    event, values = window.read()
    if event == "-submit-":
        for i in range(1,10):
            slot_num = rd.randint(100,999)
            window["-OUTPUT-"].update("")
            print(slot_num)
            tm.sleep(0.05)
        slot_win = int(slot_num/100)*111
    if slot_num == slot_win:
        print("You Win!!")
    else:
        print("You Lose...Shall we retry?")
    if event == sg.WIN_CLOSED:
        break