let button_on = false
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    pins.analogWritePin(AnalogPin.P1, 100)
    pins.analogWritePin(AnalogPin.P2, 100)
    pins.analogWritePin(AnalogPin.P8, 100)
    if (button_on == true) {
        pins.analogWritePin(AnalogPin.P8, 0)
        pins.analogWritePin(AnalogPin.P1, 0)
        pins.analogWritePin(AnalogPin.P2, 0)
        button_on = false
    } else {
        pins.analogWritePin(AnalogPin.P8, 100)
        pins.analogWritePin(AnalogPin.P1, 100)
        pins.analogWritePin(AnalogPin.P2, 100)
        if (true) {
            pins.analogWritePin(AnalogPin.P8, 100)
            pins.analogWritePin(AnalogPin.P1, 100)
            pins.analogWritePin(AnalogPin.P2, 100)
            button_on = true
        }
        
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    pins.analogWritePin(AnalogPin.P8, 255)
    pins.analogWritePin(AnalogPin.P1, 255)
    pins.analogWritePin(AnalogPin.P2, 255)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    pins.analogWritePin(AnalogPin.P8, 0)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
})
basic.forever(function on_forever() {
    
})
