import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

pace_text = 'Pace (mm:ss)'
time_text = 'Time (hh:mm:ss)'

tab1 = [  [sg.Text('Workout'), sg.VerticalSeparator(k='-VER1-'), sg.Text('Name'), sg.InputText(), sg.VerticalSeparator(k='-VER2-'), sg.Combo(values=('Pace (Min/km) - Distance (km)', 'Pace (Min/mi) - Distance (mi)'), default_value='Pace (Min/km) - Distance (km)', readonly=False, k='-COMBO-'), ],
            [sg.HorizontalSeparator(k='-HOR1-')],
            [sg.Text('Warm up')],
            [sg.Text(pace_text), sg.InputText(k='-I-'), sg.Text('Distance'), sg.InputText(k='-I-'), sg.Text(time_text), sg.InputText(k='-I-')],
            [sg.HorizontalSeparator(k='-HOR2-')],
            [sg.Text('Interval'), sg.Slider((1,100), orientation='h', s=(100,10), expand_x = True, expand_y = True, k='-SLIDER-', tooltip='Reps')],
            [sg.Text(pace_text), sg.InputText(k='-I-'), sg.Text('Distance'), sg.InputText(k='-I-'), sg.Text(time_text), sg.InputText(k='-I-')],
            [sg.Text('Recovery')],
            [sg.Text(pace_text), sg.InputText(k='-I-'), sg.Text('Distance'), sg.InputText(k='-I-'), sg.Text(time_text), sg.InputText(k='-I-')],
            [sg.HorizontalSeparator(k='-HOR3-')],
            [sg.Text('Cool down')],
            [sg.Text(pace_text), sg.InputText(k='-I-'), sg.Text('Distance'), sg.InputText(k='-I-'), sg.Text(time_text), sg.InputText(k='-I-')],
            [sg.HorizontalSeparator(k='-HOR4-')],
            [sg.Text('Totals')],
            [sg.Text(pace_text), sg.InputText(readonly = True), sg.Text('Distance'), sg.InputText(readonly = True), sg.Text(time_text), sg.InputText(readonly = True)],
            [sg.Button('Compute'), sg.Button('Cancel'), sg.VerticalSeparator(k='-VER3-'), sg.Button('Save to library')] ]

tab2 = [[sg.VerticalSeparator(k='-VER1-')]]

layout = [[sg.TabGroup([
   [sg.Tab('Plan workout', tab1),
   sg.Tab('Library', tab2)]])]
]

# Create the Window
window = sg.Window('Ugly running workout planner', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cancel': # if user closes window or clicks cancel
        window['-I-'].update('')    # FIXME 
    if event == 'Compute':
        print('You entered ', values[0])
        layout[14][1].update('Hello')

window.close()
