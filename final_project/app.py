import matplotlib.pyplot as plt
import numpy as np
import math
from helpers import quadFunc, linearFunc, invFunc, cubicFunc
from sympy import *
import time
import PySimpleGUI as sg

# ================================ HELPERS =================================

selectedWindow = None

# ==========================================================================

layoutMain = [  
                [sg.Text("Welcome to Archil's graph plotter!")],
                [sg.Text("Please, select a function:")],
                [sg.Button("Quadratic\n y=ax²+bx+c", key="quad", size=(17,2)), sg.Button("Linear\n y=kx+b", key="linear", size=(17,2))],
                [sg.Button("Inverse variation\n y=k/x", key="inv", size=(17,2)), sg.Button("Cubic\n y=ax³", key="cubic", size=(17,2))]
             ]

layoutQuad = [  
                [sg.Text("Selected: Quadratic Function")],
                [sg.Text("y=ax²+bx+c")],
                [sg.Text("Enter 'a' parameter"), sg.InputText(size=(10,1), key="aQuad")],
                [sg.Text("Enter 'b' parameter"), sg.InputText(size=(10,1), key="bQuad")],
                [sg.Text("Enter 'c' parameter"), sg.InputText(size=(10,1), key="cQuad")],
                [sg.Button("Submit"), sg.Button("Cancel")]
             ]

layoutLinear = [  
                [sg.Text("Selected: Linear Function")],
                [sg.Text("y=kx+b")],
                [sg.Text("Enter 'k' parameter"), sg.InputText(size=(10,1), key="kLin")],
                [sg.Text("Enter 'b' parameter"), sg.InputText(size=(10,1), key="bLin")],
                [sg.Button("Submit"), sg.Button("Cancel")]
             ]

layoutInv = [  
                [sg.Text("Selected: Inverse variation")],
                [sg.Text("y=k/x")],
                [sg.Text("Enter 'k' parameter"), sg.InputText(size=(10,1), key="kInv")],
                [sg.Button("Submit"), sg.Button("Cancel")]
             ]

layoutCubic = [  
                [sg.Text("Selected: Cubic Function")],
                [sg.Text("y=ax³")],
                [sg.Text("Enter 'a' parameter"), sg.InputText(size=(10,1), key="aCub")],
                [sg.Button("Submit"), sg.Button("Cancel")]
             ]

window = sg.Window("Graph Plotter", layoutMain, finalize=True)
window.move_to_center()

# Tracking events and values for main menu:
while True:
    event, values = window.read()
    # If user clicked on 'quadratic function' button:
    if event == "quad":
        # Close the main window, then create and open new window with inputs necessary for quadFunction, then change selectedWindow variable to quad
        window.close()
        windowQuad = sg.Window("Graph Plotter: Quadratic", layoutQuad, finalize=True)
        windowQuad.move_to_center()
        selectedWindow = "quad"
        break
    if event == "linear":
        window.close()
        windowLinear = sg.Window("Graph Plotter: Linear", layoutLinear, finalize=True)
        windowLinear.move_to_center()
        selectedWindow = "linear"
    if event in (sg.WIN_CLOSED, "Cancel"):
        break
    if event == "inv":
        window.close()
        windowInv = sg.Window("Graph Plotter: Inverse", layoutInv, finalize=True)
        windowInv.move_to_center()
        selectedWindow = "inv"
    if event == "cubic":
        window.close()
        windowCubic = sg.Window("Graph Plotter: Cubic", layoutCubic, finalize=True)
        windowCubic.move_to_center()
        selectedWindow = "cubic"
    if event in (sg.WIN_CLOSED, "Cancel"):
        break    
    
# Tracking variables for the selected function:
while True:
    # Constantly read particular window to keep track of values and events: 
    if selectedWindow == "quad":
        event, values = windowQuad.read()
        # If user clicked on submit, close the window, then plot the function via inputted parameters:
        if event == "Submit":
            windowQuad.close()
            quadFunc(values['aQuad'], values['bQuad'], values['cQuad'])
    if selectedWindow == "linear":
        event, values = windowLinear.read()
        if event == "Submit":
            windowLinear.close()
            linearFunc(values['kLin'], values['bLin'])
    if selectedWindow == "inv":
        event, values = windowInv.read()
        if event == "Submit":
            windowInv.close()
            invFunc(values['kInv'])
    if selectedWindow == "cubic":
        event, values = windowCubic.read()
        if event == "Submit":
            windowCubic.close()
            cubicFunc(values['aCub'])
    if event in (sg.WIN_CLOSED, "Cancel"):
        break

window.close()



