import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Workout'), sg.Combo(values=('Pace (Min/km) - Distance (km)', 'Pace (Min/mi) - Distance (mi)'), default_value='Pace (Min/km) - Distance (km)', readonly=False, k='-COMBO-'), sg.Slider((1,100), orientation='h', s=(100,10), expand_x = True,
            expand_y = True, k='-SLIDER-')],
            [sg.Text('Warm up')],
            [sg.Text('Pace'), sg.InputText(), sg.Text('Distance'), sg.InputText(), sg.Text('Time'), sg.InputText()],
            [sg.Text('Interval')],
            [sg.Text('Pace'), sg.InputText(), sg.Text('Distance'), sg.InputText(), sg.Text('Time'), sg.InputText()],
            [sg.Text('Recovery')],
            [sg.Text('Pace'), sg.InputText(), sg.Text('Distance'), sg.InputText(), sg.Text('Time'), sg.InputText()],
            [sg.Text('Cool down')],
            [sg.Text('Pace'), sg.InputText(), sg.Text('Distance'), sg.InputText(), sg.Text('Time'), sg.InputText()],
            [sg.Text('Totals')],
            [sg.Text('Pace'), sg.InputText(readonly = True), sg.Text('Distance'), sg.InputText(readonly = True), sg.Text('Time'), sg.InputText(readonly = True)],
            [sg.Button('Compute'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Ugly running workout planner', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    layout[10][1].update('Hello')

window.close()