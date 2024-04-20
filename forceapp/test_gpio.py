import RPi.GPIO as gpio
import time

# Toggles our state
def toggle_out(state):
    new_state = 0
    if state == gpio.LOW:
        new_state = gpio.HIGH
    else:
        new_state = gpio.LOW
    return new_state

# Vars
num_tests = 10
t_dwell = 0.001
pin_out = 37
pin_in = 38

# Setup
gpio.setmode(gpio.BOARD)
gpio.setup(pin_out, gpio.OUT)
gpio.setup(pin_in, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# Toggle output and read, assert the output is what we expect
# NEEDS WIRE CONNECTING PINS
state = gpio.LOW
try:
    for i in range(num_tests):
        gpio.output(pin_out, state)
        time.sleep(t_dwell)
        assert gpio.input(pin_in) == state, "GPIO input did not match expected state."
        time.sleep(t_dwell)
        state = toggle_out(state)
except AssertionError:
    print("GPIO Test Failed.")
    gpio.cleanup()
    exit(1)

gpio.cleanup()
print("GPIO Test Success.")