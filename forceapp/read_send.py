import RPi.GPIO as gpio
import time
import bluetooth
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


def unsigned_to_signed24(num):
    if (num & (1 << (size_word - 1))):
        return -1 * (1 << size_word) + num
    else:
        return num

def int_to_pounds(num):
    return round((num / max_value) * max_pounds, 1)


# Bluetooth vars
laptop_address = "4C:79:6E:89:2A:E1"
rfcomm_channel = 8
wait = 0.1

# Sensor vars
size_word = 24
max_pounds = 220.4
max_value = 2**22
gain = 1
t_dwell = 0.1
pin_clk = 37
pin_data = 38

# Setup
gpio.setmode(gpio.BOARD)
gpio.setup(pin_clk, gpio.OUT, initial=gpio.LOW)
gpio.setup(pin_data, gpio.IN)
time.sleep(0.25)

# Connect!
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((laptop_address, rfcomm_channel))

# Assemble the 24-bit word
try:
    while (1):
        tc_value = 0
        tmp = 0
        for bit in range(size_word):
            clk_pulse(pin_clk)
            tmp = gpio.input(pin_data)

            # Stuff the word
            tc_value |= tmp << (size_word - bit -1)

        # Gain pulses
        for pulse in range(gain):
            clk_pulse(pin_clk)

        # print(int_to_pounds(unsigned_to_signed24(tc_value)))
        sock.send(str(int_to_pounds(unsigned_to_signed24(tc_value))))
        time.sleep(t_dwell)
except:
    print("Closing sensor reader")
    gpio.cleanup()