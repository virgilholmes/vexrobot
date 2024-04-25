#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
wheels = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      prog.skills
#	Author:       virgilholmes
#	Created:
#	Description:  Programing Skills for VRC 2023-2024 Season
# 
# ------------------------------------------

# Library imports
from vex import *


# Begin project code
wheels.set_velocity(300, PERCENT)


while True:
    wheels.spin(FORWARD)
   
def autonomous():
    wheels.set_velocity(300, PERCENT)
    while True:
        wheels.spin(FORWARD)

competition = Competition(driver_control, autonomous)
