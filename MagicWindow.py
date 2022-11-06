import PySimpleGUI as sg


# class WindowTest():
#     b1 = sg.Button("push", visible=True, enable_events=True, expand_x=True, expand_y=True)
#     b2 = sg.Button("hey! push me", visible=False, enable_events=True, expand_x=True, expand_y=True)
#     b3 = sg.Button("no push me", visible=False, enable_events=True, expand_x=True, expand_y=True)
#     b4 = sg.Button("please push me", visible=False, enable_events=True, expand_x=True, expand_y=True)
#     layout = [[b1,b2,b3,b4]]
#     window = sg.Window('Window Title', layout, margins=(400, 200)).finalize()
#
#     while True:
#         event, values = window.Read()
#         if event == sg.WIN_CLOSED:
#             break
#         if event == "Click":
#


class MagicWindow():
    # layout2 = [[sg.Frame("here",[[]],background_color="blue",size=(20,20))]]
    # sg.Window("here", layout2, background_color="blue", transparent_color="blue", margins=(500,500),keep_on_top=True,finalize=True).read()
    layout = [[sg.Button("push")]]

    window = sg.Window('Click through transparent', layout, background_color='blue', margins=(500, 200),
                       keep_on_top=True, alpha_channel=.1, grab_anywhere=False,
                       resizable=True).finalize()

    mousePosx = []
    mousePosy = []
    dif = 30
    while True:
        y=window.TKroot.winfo_pointery()
        x=window.TKroot.winfo_pointerx()
        mousePosx.append(x)
        mousePosy.append(y)
        if len(mousePosy)>dif and x==mousePosx[len(mousePosx)-dif] and y==mousePosy[len(mousePosy)-dif]:
            window.Click()
        # if event == sg.WIN_CLOSED:
        #     break
        # elif window.mouse_location() == mousePos(len(mousePos) - 20):
        #     window.click()
