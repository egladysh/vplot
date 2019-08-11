import plotly
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import lldb 

color = 'rgb(0,0,0)'
traces=[]

def vplot_color(command):
    global color
    switcher = {
            "red" : "rgb(230,0,0)",
            "black" : "rgb(0,0,0)",
            "blue" : "rgb(0,0,230)",
            "green" : "rgb(0,230,0)"
            }
    color = switcher.get(command, command)
    print color

def vplot_clear():
    global traces
    traces=[]

def vplot(debugger, command, result, internal_dict):
    t = command.split(' ')
    if t[0] == "clear":
        vplot_clear()
    if t[0] == "color":
        vplot_color(t[1])

def stdvector_Summary(valobj, dict): 
    global color
    global traces

    vec = np.zeros(shape=(valobj.GetNumChildren(), 2))
    for i in range(valobj.GetNumChildren()):
        vec[i] = [i, valobj.GetChildAtIndex(i).GetValue()]

    df = pd.DataFrame(data=vec, columns=['x', 'y'], dtype='float')

    trace1 = go.Scatter(
        x=df['x'], y=df['y'],
        mode="lines",
        line={"color":color}
    )

    traces.append(trace1)


    layout = go.Layout(title=valobj.GetName() + " (size=" + str(valobj.GetNumChildren()) + ") " + valobj.GetDisplayTypeName())

    fig = go.Figure(data=traces, layout=layout)
    plot(fig)

    return 'size=' + str(valobj.GetNumChildren())


def __lldb_init_module(debugger, dict): 
    debugger.HandleCommand( 
      'type summary add -F ' + __name__ + '.stdvector_Summary -e -x "^(std::__1::)vector<.+>$" -w libcxxx --name vplot') 
    debugger.HandleCommand('command script add -f ' + __name__ + '.vplot vplot')

