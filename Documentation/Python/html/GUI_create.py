"""
#############################################################
 # 
 # Function for creating GUI.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @file 
# @defgroup putala_createGUI Function for creating GUI
# @code import GUI_create @endcode
#
# @brief This function GUI_create creates the application's GUI. It calls 
#        the functions createGUImain, createGUIset, and createGUIshow, 
#        which create the individual sections of the window.
#
# @author Antonin Putala, Dept. of Radio Electronics, Brno University 
#         of Technology, Czechia
# @copyright (c) 2024 Antonin Putala, This work is licensed under 
#                the terms of the MIT license
# @{


# Imports
from createGUIshow import createGUIshow # To create indicators.
from createGUIset import createGUIset   # To create regualtion settings.
from createGUImain import createGUImain # To create Connect, Set time, Graphical results buttons.


def createGUI(self):
    """!
    @brief   Create main GUI. Set size and
             title of the window. Window is not 
             resizable. It defines the colors used.
    @param   None
    @return  None
    """
    # Title of window.
    self.title("Tropical plants")
    # Window is not resizable.
    self.resizable(False, False) 
    # Size of window.
    self.geometry("800x500")
    # Defines the colors used.
    self.color = {'pink':'#EECCCC', 'red':'#FF4444', 
                  'blue':'#4444FF', 'cyan':'#7777FF', 'gold':'#99993A', 
                  'gray':'#DDDDDD', 'black':'#444444', 'green':'#84FFBA',
                  'yellow':'#DDDDFF', 'run_col':'#77FF77', 'stop_col':'#FF7777'}
    
    # Creates GUI widgets.
    createGUIshow(self)
    createGUIset(self)
    createGUImain(self)

##@}

    
    