import PySimpleGUI as sg
import math

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

pace_text = 'Pace (mm:ss)'
time_text = 'Time (hh:mm:ss)'

def time_to_seconds(time_ : str):
    time_ = time_.replace(" ", "")  # Trim spaces
    time_components_ = time_.split(":") # Split
    components_left_ = len(time_components_)
    if (components_left_>3 or (components_left_==1 and time_components_[0]=='')):
        return 0
    else:
        time_in_seconds_ = 0
        power_counter_ = 0
        while components_left_>0:
            time_in_seconds_+=int(time_components_[components_left_-1])*pow(60, power_counter_)
            components_left_-=1
            power_counter_+=1
    return time_in_seconds_

def seconds_to_time(seconds_):
    min_ = math.floor(seconds_/60)
    secs_ = seconds_%60
    time_=str(min_)+":"+str(secs_)
    return time_

# Function with a state
def addSimpleBlock():
    print("I'm inside the block"+str(addSimpleBlock.counter))
    baseBlock1 = []
    baseBlock1.append(sg.Text(pace_text))
    baseBlock1.append(sg.InputText(k='-Ipace'+str(addSimpleBlock.counter)+'-'))
    baseBlock1.append(sg.Text('Distance'))
    baseBlock1.append(sg.InputText(k='-Idistance'+str(addSimpleBlock.counter)+'-'))
    baseBlock1.append(sg.Text(time_text))
    baseBlock1.append(sg.InputText(k='-Itime'+str(addSimpleBlock.counter)+'-'))
    addSimpleBlock.counter += 1
    return baseBlock1

addSimpleBlock.counter = 0

intervalElement = [[sg.InputText(default_text='Interval'), sg.Slider((1,20), orientation='h', s=(50,10), expand_x = False, expand_y = True, k='-SLIDER-', tooltip='Reps')],
addSimpleBlock(),
[sg.InputText(default_text='Recovery')],
addSimpleBlock()]

introBlock = [[sg.Text('Workout'), sg.VerticalSeparator(k='-VER1-'), sg.Text('Name'), sg.InputText(), sg.VerticalSeparator(k='-VER2-'), sg.Combo(values=('Pace (Min/km) - Distance (km)', 'Pace (Min/mi) - Distance (mi)'), default_value='Pace (Min/km) - Distance (km)', readonly=False, k='-COMBO-'), ],
[sg.HorizontalSeparator(k='-HOR1-')]]

totalsBlock = [[sg.Text('Totals')],
[sg.Text(pace_text), sg.InputText(readonly = True, k='-TotalPace-'), sg.Text('Distance'), sg.InputText(readonly = True, k='-TotalDistance-'), sg.Text(time_text), sg.InputText(readonly = True, k='-TotalTime-')],
[sg.Button('Compute'), sg.Button('Cancel'), sg.VerticalSeparator(k='-VER3-'), sg.Button('Save to library'), sg.Button('Add interval', enable_events=True, key="-addInterval-"), sg.Button('Add rep', enable_events=True, key="-addRep-")],
[sg.HorizontalSeparator(k='-HOR4-')]]

mainBlock = [[sg.InputText(default_text='Warm up')],
addSimpleBlock(),
[sg.HorizontalSeparator(k='-HOR2-')],
[sg.Column(intervalElement, key='-IntervalElement-')]]

lastBlock = [[sg.HorizontalSeparator(k='-HOR3-')],
[sg.InputText(default_text='Cool down')],
addSimpleBlock()]
    

tab1 = [  [sg.Column(introBlock, key='-introBlock-')],
            [sg.Column(totalsBlock, key='-TotalsBlock-')],
            [sg.Column(mainBlock, key='-MainBlock-')],
            [sg.Column(lastBlock, key='-LastBlock-')]]

# Clearing section
keys_to_clear = []
last_value = 0 # Neeed for cancel button
keys_to_clear.append('-TotalPace-')
keys_to_clear.append('-TotalDistance-')
keys_to_clear.append('-TotalTime-')

def updateKeysToClear():
    global last_value
    for input_key in range(last_value,addSimpleBlock.counter):
        this_pace_key='-Ipace'+str(input_key)+'-'
        keys_to_clear.append(this_pace_key)
        this_pace_key='-Idistance'+str(input_key)+'-'
        keys_to_clear.append(this_pace_key)
        this_pace_key='-Itime'+str(input_key)+'-'
        keys_to_clear.append(this_pace_key)
    last_value = addSimpleBlock.counter-1

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
        updateKeysToClear()
        for key in keys_to_clear:
            window[key]('')
    if event == 'Compute':
        print('You entered ', values[0])
        window['-TotalPace-'].update('totallll')
        #print('Converted time ', time_to_seconds(tab1[3][5].get()))
        #1 find the handles
        #2 fill intermediate values
        #3 compute totals
        print(keys_to_clear)
    if event == '-addInterval-':
        print('')
    if event == '-addRep-':
        window.extend_layout(window['-MainBlock-'], [addSimpleBlock()])
        updateKeysToClear()

window.close()
