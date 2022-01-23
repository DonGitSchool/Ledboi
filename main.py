def on_pin_pressed_p0():
    pins.analog_write_pin(AnalogPin.P1, 100)
    pins.analog_write_pin(AnalogPin.P2, 100)
    pins.analog_write_pin(AnalogPin.P8, 100)
    global button_on
    if button_on == True:
        pins.analog_write_pin(AnalogPin.P8, 0)
        pins.analog_write_pin(AnalogPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P2, 0)
        button_on = False
    else:
        pins.analog_write_pin(AnalogPin.P8, 255)
        pins.analog_write_pin(AnalogPin.P1, 255)
        pins.analog_write_pin(AnalogPin.P2, 255)
        if True:
            pins.analog_write_pin(AnalogPin.P8, 255)
            pins.analog_write_pin(AnalogPin.P1, 255)
            pins.analog_write_pin(AnalogPin.P2, 255)
            button_on = True
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    pins.analog_write_pin(AnalogPin.P8, 255)
    pins.analog_write_pin(AnalogPin.P1, 255)
    pins.analog_write_pin(AnalogPin.P2, 255)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.analog_write_pin(AnalogPin.P8, 0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

button_on = False
def on_forever():
    pass
basic.forever(on_forever)
