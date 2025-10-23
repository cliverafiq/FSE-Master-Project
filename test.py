from gpiozero import Button

button1 = Button(17)
button2 = Button(27)

def on_button1_pressed():
    print("Button 1 pressed")

def on_button2_pressed():
    print("Button 2 pressed")

button1.when_pressed = on_button1_pressed
button2.when_pressed = on_button2_pressed