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

def clk_pulse(pin_clk):
    gpio.output(pin_clk, gpio.HIGH)
    gpio.output(pin_clk, gpio.LOW)

# Vars
n_clk_pulses = 24
t_dwell = 0.001
pin_clk = 37
pin_data = 38

# Setup
gpio.setmode(gpio.BOARD)
gpio.setup(pin_clk, gpio.OUT, initial=gpio.LOW)
gpio.setup(pin_data, gpio.IN)
time.sleep(0.25)

# Assemble the 24-bit word
tc_value = 0
tmp = 0
for bit in range(n_clk_pulses):
    clk_pulse(pin_clk)
    tmp = gpio.input(pin_data)

    # Stuff the word
    tc_value = tc_value <<<<<<<<<<<<<<<<<<<<<<<<

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